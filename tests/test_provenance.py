import hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from provenance import build_provenance,save_draft,GOVERNANCE_FIELDS

class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);folder=self.root/'data/sample_or_fallback';folder.mkdir(parents=True)
        (folder/'sample.txt').write_bytes(b'sample')
        (folder/'manifest.json').write_text(json.dumps({'sources':[{'file':'sample.txt','sha256':hashlib.sha256(b'sample').hexdigest(),'url':'https://example.org/data','accessed_utc':'2026-01-01'}]}))
        (self.root/'lesson.ipynb').write_text('{}')
    def build(self,notes=None):return build_provenance(self.root,'lesson.ipynb',['sample.txt'],{'units':'test'},notes or {})
    def test_unresolved_and_source_identity(self):
        r=self.build();self.assertEqual(set(r['unresolved_fields']),set(GOVERNANCE_FIELDS))
        self.assertTrue(r['technical_lineage']['sources'][0]['checksum_verified'])
    def test_completed_notes_never_grant_approval(self):
        r=self.build({key:'discussed' for key in GOVERNANCE_FIELDS})
        self.assertEqual(r['unresolved_fields'],[])
        self.assertTrue(r['status'].startswith('classroom draft:'))
        p=save_draft(r,self.root/'outputs');self.assertEqual(json.loads(p.read_text())['status'],r['status'])
    def test_tampering_and_unlisted_source(self):
        (self.root/'data/sample_or_fallback/sample.txt').write_text('changed')
        with self.assertRaisesRegex(ValueError,'checksum mismatch'):self.build()
        with self.assertRaisesRegex(ValueError,'manifest entry'):build_provenance(self.root,'lesson.ipynb',['unknown'],{}, {})
    def test_false_approval_cannot_be_saved(self):
        with self.assertRaises(ValueError):save_draft({'status':'approved'},self.root/'outputs')

if __name__=='__main__':unittest.main()
