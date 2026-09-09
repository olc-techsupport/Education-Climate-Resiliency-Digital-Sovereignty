# Notebook-centered Learning Lab

Start with [00_getting_started.ipynb](00_getting_started.ipynb), then choose one parallel pathway:

- [Guided Explorer](01_guided_explorer.ipynb): original monthly drought parsing, completeness audit, annual chart, interpretation and stewardship.
- [Data Investigator](02_data_investigator.ipynb): original gauge loading and coverage, time-window trend comparison, illustrative weight sensitivity and stewardship.
- [Technical Extender](03_technical_extender.ipynb): original hand-calculated method test, low-flow completeness, OLS and Theil–Sen comparison, uncertainty and stewardship.

All original track cells are retained or expanded into visible steps. The drought helper is expanded into sequential cells. Provenance functions are defined and explained inside each notebook, with no custom-module imports. Raw historical snapshots and their manifest are bundled under data/sample_or_fallback. The getting-started notebook also uses the teaching CSVs retained under data.

Instructors: prepare the included environment.yml before the event (numpy, pandas, matplotlib and scipy are needed for the full tracks). Copy this entire folder to each machine, activate the prepared environment and launch JupyterLab here. No installation or data refresh is needed during the event.

The original low-flow method permits windows crossing calendar-year boundaries, as documented in the Technical Extender limitations. The 330-day threshold is a teaching choice. These methods do not establish water quality, management thresholds or a 7Q10 statistic.

The original learning objectives, sovereignty activities, seven presentation questions, instructor notes, guides, templates and extension prompts are retained. Each team develops its own question; explanations of attempted work count. Xarray remains optional. Preserve the scheduled final hour for student sharing.

Save a separate notebook copy per team. Optional provenance records go to outputs/governance and remain classroom drafts. See guides/instructor_guide.md and VALIDATION.md. Device readiness still requires OLC pre-training checks.
