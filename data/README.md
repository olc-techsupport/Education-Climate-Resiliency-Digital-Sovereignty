# Prepared-data policy

All three teaching tracks use local public-source snapshots. The current manifest records acquisition on 2026-08-24. Run `python scripts/verify_snapshots.py` before class to confirm file identity. A checksum confirms identity, not scientific validity or sharing authority.

| Source | Core use | Snapshot |
| --- | --- | --- |
| NOAA/NCEI climate-division PDSI | Guided regional drought interpretation | Fixed-width monthly file; divisions 7 and 8 selected |
| USGS daily streamflow | Investigator and technical tracks | Four RDB gauge files requested for 1990–2024 |
| Census TIGER/Line 2023 AIANNH and roads | Optional extension context | Prepared ZIPs; not required by core tracks |

Instructors may run `python scripts/prepare_workshop_data.py` online to refresh source files before an event. Review new dates, coverage, manifest and source terms, and rerun the lesson before distributing the snapshot. Do not auto-refresh during class. Learners need no network after environment installation and delivery of the prepared files.

Keep community-held information, sensitive locations and credentials outside this repository. Completed learning/stewardship records belong in approved class storage, not Git by default. Source datasets retain their own attribution and terms.
