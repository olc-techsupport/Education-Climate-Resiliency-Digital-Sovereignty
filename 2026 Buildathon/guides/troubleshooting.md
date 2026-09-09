# Troubleshooting

## First response to any error

1. Stop; do not repeatedly rerun a download.
2. Record the notebook heading and the final line of the error.
3. Confirm the `ed-py` kernel is selected.
4. Run `python scripts/check_environment.py` from the repository root.
5. Check the matching item below or ask a mentor.

## Common problems

### `ModuleNotFoundError`

The notebook is using the wrong environment or setup is incomplete. Activate `ed-py`, run `python -m ipykernel install --user --name ed-py --display-name "Python (ed-py)"`, restart Jupyter, and select **Python (ed-py)**.

### A download times out or returns no data

Confirm general internet access and the source status in the readiness check. Wait once and retry once. If it still fails, use instructor-prepared fallback data or continue along the shortened route. Never infer that “no returned data” means the phenomenon did not occur.

### A map is blank

Check whether the printed feature count is zero. If data exist, check coordinate reference systems and whether the plotting extent covers the study area. Basemap failure alone does not invalidate local vector layers.

### `NameError`

A required earlier cell probably did not finish. Save any typed reflections, restart the kernel, and run cells from the beginning in order.

### A cell stays at `[*]`

Large geospatial downloads can take several minutes. Wait up to the instructor's posted limit. Then interrupt the kernel once and ask a mentor before rerunning.

### Permission or output-folder error

Confirm that Jupyter was launched from the repository root and that the repository is in a writable location. Run `python scripts/check_environment.py`.

### Conda cannot solve the environment

Update conda, then retry with the `conda-forge` channel defined in `environment.yml`. Do not mix ad hoc system-wide `pip` installs into a classroom machine. Ask the instructor for a prepared environment if setup time is limited.

## Useful information for a mentor

Share the operating system, selected kernel, notebook heading, final error line, output of `python scripts/check_environment.py`, and whether teammates see the same source failure. Do not share credentials or sensitive paths.
