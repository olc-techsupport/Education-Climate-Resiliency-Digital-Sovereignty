# Core and optional dependencies

environment.yml is the core specification for the three tracks. GIS clients, basemap libraries and Daymet are not required for these activities. Prepare and test any optional extension packages on an instructor or mentor machine before the event. No participant installation is required during the workshop.

The optional [xarray cube extension](../challenges/optional_xarray_cube.md) needs xarray in addition to the existing numpy/pandas/matplotlib stack. Keep the core environment unchanged. Use local CSVs directly; avoid additional GIS, cloud, map-tile or remote-data dependencies. Do not install the full tutorial environment or ODC for this event. Verify the exact extension offline before offering it; availability of cached data alone is not validation.
