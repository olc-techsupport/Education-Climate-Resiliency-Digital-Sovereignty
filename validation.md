# Workshop validation

Validated 2026-09-05 using an existing Python 3.11 conda environment with pandas, SciPy, Matplotlib, nbformat and nbclient. The declared Python 3.12 core environment was not freshly installed or solved; instructors should run the readiness checker on their actual workshop environment. See [dependencies](guides/dependencies.md).

- All seven prepared-file SHA-256 checksums matched the manifest.
- All three track notebooks executed from clean kernels with outbound socket connections blocked (local kernel communication allowed). No live refresh was required.
- Guided Explorer excluded incomplete annual division coverage and produced its chart from complete years. Three offline tests verify equal-weight means, partial/missing-division exclusions, duplicate rejection, and empty/no-complete-year errors.
- Executed copies are local validation artifacts; student notebooks retain clean cells without saved outputs. The instructor-notes notebook is documentation only.
- The live data-refresh workflow was not exercised, and the readiness notebook's strict Python 3.12 check was not claimed as passed under Python 3.11.

Run `python scripts/verify_snapshots.py`, `python -m unittest discover -s tests`, and `python scripts/validate_offline.py` to repeat checks. Executed copies go to `outputs/validation/`; they are classroom drafts, not publication approvals. Code validation is not evidence that learner outcomes or award deliverables have already been achieved.


## Sovereignty and provenance revision — 2026-09-05

All three revised tracks executed successfully with outbound socket connections blocked using the existing Python 3.11 environment. All seven snapshot checksums matched. The new provenance cells resolve each track's actual source files, analytical parameters and unresolved decision notes. Four additional tests cover unresolved fields/source identity, completed notes remaining drafts, source tampering/unlisted files, and rejection of a falsely approved record by the draft writer. The existing core environment was used; no new toolkit dependency was installed.

The optional JSON draft writer was tested in a temporary directory. Notebook SAVE_DRAFT remains False, so validation did not create student decision sidecars. Records do not claim standards compliance, Tribal approval or permission to publish. The source notebook edits outside the replaced extender provenance section were preserved; existing analytical code was not changed.
