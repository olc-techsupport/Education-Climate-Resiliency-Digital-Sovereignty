"""Local teaching provenance; records evidence without granting permissions."""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

GOVERNANCE_FIELDS = ('question','potential_benefit','authority_to_consult','community_input_needed',
                     'representation_limits','reviewer_roles','intended_audience','storage_and_access',
                     'reuse_limits','correction_withdrawal','decision','decision_reason')

def build_provenance(root, notebook, source_files, analysis, governance):
    root=Path(root).resolve()
    snapshot=root/'data/sample_or_fallback'
    manifest=json.loads((snapshot/'manifest.json').read_text(encoding='utf-8'))
    indexed={item['file']:item for item in manifest['sources']}
    sources=[]
    for name in dict.fromkeys(source_files):
        path=(snapshot/name).resolve()
        if not path.is_relative_to(snapshot.resolve()):raise ValueError('Source path escapes snapshot folder.')
        if name not in indexed:raise ValueError(f'No source manifest entry for {name}')
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual!=indexed[name]['sha256']:raise ValueError(f'Source checksum mismatch: {name}')
        item=deepcopy(indexed[name])
        item['checksum_verified']=True
        sources.append(item)
    if not sources:raise ValueError('At least one source is required.')
    missing=[key for key in GOVERNANCE_FIELDS if not isinstance(governance.get(key),str) or not governance[key].strip()]
    nb_path=(root/notebook).resolve()
    if not nb_path.is_relative_to(root):raise ValueError('Notebook must be in the repository.')
    record=dict(schema_version='1.0',created_utc=datetime.now(timezone.utc).isoformat(),
        status='classroom draft: external sharing not approved by this record',
        technical_lineage=dict(notebook=notebook,notebook_sha256=hashlib.sha256(nb_path.read_bytes()).hexdigest(),
            provenance_helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),python=platform.python_version(),
            sources=sources,analysis=deepcopy(analysis)),
        governance_decisions=deepcopy(governance),unresolved_fields=missing,
        evidence_note='Student discussion record; reviewer roles are proposed, not confirmed authorization.',
        standards_note='Teaching record informed by provenance concepts; no IEEE 2890 conformity assessment performed.')
    # Check serialization now, so failure happens before a student chooses to save.
    json.dumps(record,allow_nan=False)
    return record

def save_draft(record, folder):
    if not record.get('status','').startswith('classroom draft:'):
        raise ValueError('This helper saves classroom drafts only; it cannot grant approval.')
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    path=folder/('provenance-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
    with path.open('x',encoding='utf-8') as stream:
        json.dump(record,stream,indent=2,allow_nan=False);stream.write('\n')
    return path
