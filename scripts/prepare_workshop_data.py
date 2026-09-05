from __future__ import annotations

#!/usr/bin/env python
"""Prepare dated, checksummed public-source snapshots for workshop fallback use."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request


STATIC_SOURCES = {
    "census_aiannh_2023.zip": "https://www2.census.gov/geo/tiger/TIGER2023/AIANNH/tl_2023_us_aiannh.zip",
    "census_oglala_lakota_roads_2023.zip": "https://www2.census.gov/geo/tiger/TIGER2023/ROADS/tl_2023_46102_roads.zip",
}

NOAA_DIRECTORY = "https://www.ncei.noaa.gov/pub/data/cirs/climdiv/"

GAUGES = {
    "06446000": "White River Near Oglala SD",
    "06446500": "White River Near Interior SD",
    "06447000": "White River Near Kadoka SD",
    "06447500": "Little White River Near Martin SD",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url: str, destination: Path, timeout: float) -> dict[str, object]:
    request = urllib.request.Request(url, headers={"User-Agent": "Ed-py workshop data preparation"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
        destination.write_bytes(payload)
        return {
            "status": "downloaded",
            "bytes": len(payload),
            "sha256": sha256(destination),
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"status": "failed", "error": f"{type(exc).__name__}: {exc}"}


def latest_noaa_pdsi_url(timeout: float) -> str:
    """Resolve NOAA's latest dated PDSI filename instead of pinning a stale URL."""
    request = urllib.request.Request(
        NOAA_DIRECTORY,
        headers={"User-Agent": "Ed-py workshop data preparation"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        listing = response.read().decode("utf-8", errors="replace")
    matches = sorted(set(re.findall(r"climdiv-pdsidv-v1\.0\.0-\d{8}", listing)))
    if not matches:
        raise RuntimeError("NOAA directory did not contain a dated PDSI file")
    return urllib.parse.urljoin(NOAA_DIRECTORY, matches[-1])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=1990)
    parser.add_argument("--end-year", type=int, default=2024)
    parser.add_argument("--timeout", type=float, default=180.0)
    args = parser.parse_args()
    if not 1900 <= args.start_year <= args.end_year <= 2100:
        parser.error("years must be ordered and between 1900 and 2100")

    repo = Path(__file__).resolve().parents[1]
    output = repo / "data" / "sample_or_fallback"
    output.mkdir(parents=True, exist_ok=True)
    accessed = datetime.now(timezone.utc).isoformat()
    manifest: dict[str, object] = {
        "created_utc": accessed,
        "purpose": "Instructor-prepared public-source fallback for the Ed-py workshop",
        "warning": "Snapshots are not current live data and are not governance approval.",
        "sources": [],
    }

    sources: dict[str, str] = dict(STATIC_SOURCES)
    failures = 0
    try:
        sources["noaa_climate_division_pdsi.txt"] = latest_noaa_pdsi_url(args.timeout)
    except (urllib.error.URLError, TimeoutError, OSError, RuntimeError) as exc:
        failures = 1
        manifest["sources"].append({
            "file": "noaa_climate_division_pdsi.txt",
            "url": NOAA_DIRECTORY,
            "accessed_utc": accessed,
            "status": "failed",
            "error": f"{type(exc).__name__}: {exc}",
        })
        print(f"Could not discover NOAA PDSI file: {exc}")

    for site_id in GAUGES:
        params = urllib.parse.urlencode({
            "format": "rdb",
            "sites": site_id,
            "startDT": f"{args.start_year}-01-01",
            "endDT": f"{args.end_year}-12-31",
            "parameterCd": "00060",
            "statCd": "00003",
        })
        sources[f"usgs_nwis_{site_id}_{args.start_year}_{args.end_year}.rdb"] = (
            f"https://waterservices.usgs.gov/nwis/dv/?{params}"
        )

    for filename, url in sources.items():
        print(f"Preparing {filename} ...")
        record = {"file": filename, "url": url, "accessed_utc": accessed}
        record.update(download(url, output / filename, args.timeout))
        if record["status"] == "failed":
            failures += 1
            print(f"  FAILED: {record['error']}")
        else:
            print(f"  downloaded {record['bytes']:,} bytes")
        manifest["sources"].append(record)

    manifest_path = output/"manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest: {manifest_path}")
    print("Review source terms and the manifest before distributing these files.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
