# Teaching data

These historical local snapshots were acquired on 2026-08-24. See source_manifest.json for exact original URLs, dates and SHA-256 checksums. Original files are retained in original/. No downloads occur in the notebooks or preparation script.

- drought_monthly.csv: NOAA South Dakota climate divisions 7 and 8, monthly PDSI (dimensionless). Includes all years in the source; notebooks select their period. Values outside the original loader validity range (-99, 99) become missing.
- streamflow_daily.csv: USGS station identifier, date, daily mean discharge in cfs, and unchanged qualifier strings. Blank and nonnumeric discharge becomes missing, never zero. Original headers identify stations and describe qualifier codes. No additional qualifier-based exclusion is applied; teams must examine those limitations.

prepare_teaching_data.py verifies original checksums and reproduces the CSVs. No annual summaries or coverage filtering are precomputed: those choices are visible in the notebooks. teaching_checksums.json identifies distributed CSVs, not scientific validity or release approval.
