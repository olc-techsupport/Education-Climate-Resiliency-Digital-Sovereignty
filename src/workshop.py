"""Completeness-aware regional PDSI teaching summary."""
from pathlib import Path
import pandas as pd

def annual_pdsi(path, start_year=1980):
    rows=[]
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        parts=line.split()
        if len(parts)!=13 or len(parts[0])!=10 or not parts[0].isdigit():continue
        code=parts[0]
        if code[:2]!='39' or code[4:6]!='05' or int(code[2:4]) not in (7,8):continue
        year=int(code[6:])
        if year<start_year:continue
        for month,value in enumerate(parts[1:],1):
            rows.append(dict(year=year,division=int(code[2:4]),month=month,pdsi=float(value)))
    data=pd.DataFrame(rows,columns=['year','division','month','pdsi'])
    if data.empty:raise ValueError('No matching PDSI records; check source and study period.')
    if data.duplicated(['year','division','month']).any():raise ValueError('Duplicate division/month records; inspect source.')
    valid=data[data.pdsi.between(-99,99,inclusive='neither') & data.pdsi.notna()]
    years=range(int(data.year.min()),int(data.year.max())+1)
    counts=valid.groupby(['year','division']).size().unstack().reindex(index=years,columns=[7,8],fill_value=0).fillna(0).astype(int)
    audit=counts.rename(columns={7:'division_7_months',8:'division_8_months'})
    audit['complete']=(counts[7]==12)&(counts[8]==12)
    eligible=audit.index[audit.complete]
    annual=valid[valid.year.isin(eligible)].groupby(['year','division']).pdsi.mean().groupby('year').mean()
    if annual.empty:raise ValueError('No complete years for both divisions; select a longer period or inspect snapshot.')
    return data,audit,annual
