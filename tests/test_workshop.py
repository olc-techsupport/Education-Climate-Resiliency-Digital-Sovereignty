from pathlib import Path
import sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from workshop import annual_pdsi

def row(division,year,values):return f'39{division:02d}05{year} '+' '.join(map(str,values))+'\n'
class CompletenessTests(unittest.TestCase):
    def run_data(self,text):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'pdsi.txt';p.write_text(text)
            return annual_pdsi(p)
    def test_partial_and_absent_division_excluded(self):
        text=row(7,2000,[1]*12)+row(8,2000,[3]*12)+row(7,2001,[1]*12)+row(8,2001,[3]*11+[-99.99])+row(7,2002,[1]*12)
        _,audit,annual=self.run_data(text)
        self.assertEqual(annual.to_dict(),{2000:2.0})
        self.assertEqual(audit.index[~audit.complete].tolist(),[2001,2002])
    def test_duplicates_rejected(self):
        with self.assertRaisesRegex(ValueError,'Duplicate'):self.run_data(row(7,2000,[1]*12)*2)
    def test_empty_or_no_complete_years(self):
        for text in ['',row(7,2000,[1]*12)]:
            with self.subTest(text=text),self.assertRaises(ValueError):self.run_data(text)
if __name__=='__main__':unittest.main()
