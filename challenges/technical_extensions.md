# Technical Extender challenges

Work in a copy or branch. Do not overwrite the track notebooks. Each contribution should include a small test or reproducible comparison.

## Optional offline xarray cube

See the [extension design and preparation checklist](optional_xarray_cube.md). Interested teams in any pathway may use a prepared, offline-tested machine to organize local observations by time and site and explore their own question.

## Validate the low-flow method

- **Prerequisite:** pandas rolling windows and hydrology fundamentals
- **Estimated time:** 2-3 hours
- Extend the Technical Extender comparison of rolling minima and seven-day means; test missing-day and cross-year behavior.
- Handle missing days explicitly and document allowable completeness.
- If adding a management threshold, document its source and local applicability; the core tracks provide no operational threshold.
- **Done when:** Tests cover a hand-calculated series and the method note uses precise terminology.

## Compare trend estimators

- **Prerequisite:** regression and SciPy
- **Estimated time:** 2 hours
- Compare ordinary least squares with a robust estimator such as Theil–Sen.
- Report slope, uncertainty, assumptions, and sensitivity to start/end years.
- **Done when:** Narrative and implementation name the same method and a reproducible comparison is included.

## Add data-quality indicators

- **Prerequisite:** pandas/groupby
- **Estimated time:** 2-4 hours
- Calculate completeness by source, gauge, year, and month.
- Prevent trend calculation below a documented completeness threshold.
- Add a visible quality note to figures and reports.
- **Done when:** Missing data cannot silently become a confident finding.

## Generalize geography safely

- **Prerequisite:** GeoPandas, APIs, and local governance consultation
- **Estimated time:** 1-2 days
- Move geography-specific parameters into a validated configuration file.
- Include boundary label/source, gauge IDs, climate divisions, road geography, study period, and review contacts.
- Fail clearly when configuration is incomplete; do not infer sensitive or governance choices.
- **Done when:** A second test geography runs and the documentation names assumptions that cannot be generalized.

## Build provenance sidecars

- **Prerequisite:** Python file I/O and metadata design
- **Estimated time:** 3 hours
- Save a JSON sidecar beside every generated figure with source URLs, access timestamps, parameters, code revision, limitations, and review status.
- **Done when:** Sidecars validate against a documented schema and contain no secrets or sensitive knowledge.

## Make execution reproducible

- **Prerequisite:** Jupyter execution tooling
- **Estimated time:** 3-5 hours
- Create a clean-environment smoke test for the readiness notebook and a non-publishing test of the three track notebooks.
- Mock or cache remote responses where licensing permits.
- **Done when:** Failures identify the source and cell without modifying instructional content or publishing outputs.
