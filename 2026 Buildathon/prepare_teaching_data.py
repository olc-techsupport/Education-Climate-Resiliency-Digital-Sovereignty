"""Instructor-only conversion of bundled snapshots."""
from pathlib import Path
from io import StringIO
import json, hashlib
import pandas as pd

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'
manifest=json.loads((DATA/'source_manifest.json').read_text())
for source in manifest['sources']:
    p=DATA/'original'/source['file']
    if hashlib.sha256(p.read_bytes()).hexdigest()!=source['sha256']:
        raise ValueError('Source checksum mismatch: '+p.name)
rows=[]
for line in (DATA/'original/noaa_climate_division_pdsi.txt').read_text().splitlines():
    parts=line.split()
    if len(parts)!=13 or len(parts[0])!=10 or not parts[0].isdigit(): continue
    code=parts[0]
    if code[:2]!='39' or code[4:6]!='05' or int(code[2:4]) not in (7,8): continue
    for month,value in enumerate(parts[1:],1):
        value=float(value)
        rows.append({'date':f'{int(code[6:]):04d}-{month:02d}-01',
                     'division':int(code[2:4]),'pdsi':value if -99<value<99 else None})
pdsi=pd.DataFrame(rows)
assert not pdsi.duplicated(['date','division']).any()
pdsi.to_csv(DATA/'drought_monthly.csv',index=False)
frames=[]
for p in sorted((DATA/'original').glob('*.rdb')):
    lines=[line for line in p.read_text().splitlines() if not line.startswith('#') and line.strip()]
    raw=pd.read_csv(StringIO('\n'.join([lines[0]]+lines[2:])),sep='\t',dtype=str)
    value=next(c for c in raw if '00060_00003' in c and not c.endswith('_cd'))
    frame=pd.DataFrame({'site_id':raw['site_no'],'date':raw['datetime'],
                        'flow_cfs':pd.to_numeric(raw[value],errors='coerce'),
                        'qualifiers':raw[value+'_cd']})
    assert not frame.duplicated(['site_id','date']).any()
    frames.append(frame)
pd.concat(frames,ignore_index=True).to_csv(DATA/'streamflow_daily.csv',index=False)
products={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in DATA.glob('*.csv')}
(DATA/'teaching_checksums.json').write_text(json.dumps(products,indent=2))
print('Prepared two teaching CSVs from verified local snapshots.')
