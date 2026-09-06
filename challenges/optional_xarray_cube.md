# Optional offline xarray data cube

**Status:** This is optional for interested teams in any pathway and is not a primary target or assessment requirement. Each team keeps its own question.

Use the local tutorial at `C:\Users\gekek\Documents\OLC_DC_tutorial\data_cube_tutorial` as a reference. Its arrays/dimensions and time-selection activities are relevant, and its `data/cache` folder contains local NDVI CSVs. The full tutorial environment includes many geospatial and data-access packages and must not become the event installation requirement.

The smallest useful extension is to read prepared local observations with pandas, organize them in an xarray DataArray with named time and site dimensions, select a period, and produce one comparison connected to the team's question. Describe this accurately as a small site-by-time cube. Preserve missing observations and document source, spatial support, time coverage and units.

Use only xarray plus the existing pandas/numpy/matplotlib stack. Avoid map tiles, remote APIs, automatic cache refresh, cloud stores and additional geospatial packages until they have been tested at OLC. Load CSVs directly rather than importing tutorial helpers that may fetch data where possible. Keep any files needed for the exercise together in the distributed event materials.

The current core environment specification does not include xarray. Before offering this extension, prepare and test preferably on an instructor or mentor machine with xarray and the exact local files. 


## Team activity once prepared

1. State how the extension relates to your team’s question.
2. Read the prepared local CSVs and inspect dates, sites, units and missing values.
3. Build a labeled time-by-site DataArray, preserving missing observations.
4. Select a time window and compare observations using one plot or summary.
5. Explain spatial coverage, uncertainty, appropriate review and sharing arrangements using the existing seven presentation questions.

Keep the three core pathways available regardless of extension readiness. ODC and possible Cubedynamics implementation are future work after testing at OLC.

For more information about data cubes, explore the [OLC Data Cube Tutorial](https://github.com/olc-techsupport/Education-data_cube_tutorial) when internet access is available. This is an optional resource for further study, not required workshop preparation.
