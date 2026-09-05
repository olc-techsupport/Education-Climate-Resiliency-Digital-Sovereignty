#!/usr/bin/env python
"""Plain-language readiness check for the Ed-py workshop environment."""

from __future__ import annotations

import argparse
import importlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import tempfile
import urllib.error
import urllib.request


REQUIRED_IMPORTS = {"numpy":"numpy", "pandas":"pandas", "scipy":"scipy", "matplotlib":"matplotlib", "nbformat":"nbformat", "nbclient":"nbclient", "requests":"requests"}

ENDPOINTS = {
    "Census boundary files": "https://www2.census.gov/geo/tiger/TIGER2023/AIANNH/",
    "USGS streamflow": "https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=06446000&startDT=2023-01-01&endDT=2023-01-02&parameterCd=00060&statCd=00003",
    "NOAA climate divisions": "https://www.ncei.noaa.gov/pub/data/cirs/climdiv/",
}


def result(label: str, ok: bool, detail: str) -> dict[str, object]:
    icon = "READY" if ok else "ASK A MENTOR"
    print(f"[{icon}] {label}: {detail}")
    return {"label": label, "ok": ok, "detail": detail}


def check_imports() -> list[dict[str, object]]:
    checks = []
    for module, package in REQUIRED_IMPORTS.items():
        try:
            imported = importlib.import_module(module)
            version = getattr(imported, "__version__", "installed")
            checks.append(result(f"Package {package}", True, str(version)))
        except Exception as exc:  # Include binary/DLL failures, not just ImportError.
            checks.append(result(f"Package {package}", False, f"{type(exc).__name__}: {exc}"))
    return checks


def check_online(timeout: float) -> list[dict[str, object]]:
    checks = []
    headers = {"User-Agent": "Ed-py workshop readiness check"}
    for name, url in ENDPOINTS.items():
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                code = getattr(response, "status", 200)
                checks.append(result(name, 200 <= code < 400, f"HTTP {code}"))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            checks.append(result(name, False, str(exc)))
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="also test workshop data endpoints")
    parser.add_argument("--timeout", type=float, default=12.0, help="seconds per online check")
    parser.add_argument("--json", action="store_true", help="print a final machine-readable summary")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    checks: list[dict[str, object]] = []
    print("Ed-py readiness check")
    print(f"Python: {sys.version.split()[0]} ({platform.system()} {platform.release()})")
    print(f"Repository: {repo}")

    checks.append(result("Python 3.12", sys.version_info[:2] == (3, 12), sys.version.split()[0]))
    track_notebooks = [
        repo/"tracks"/"01_guided_explorer.ipynb",
        repo/"tracks"/"02_data_investigator.ipynb",
        repo/"tracks"/"03_technical_extender.ipynb",
    ]
    missing_tracks = [path.name for path in track_notebooks if not path.is_file()]
    checks.append(result(
        "Track notebooks",
        not missing_tracks,
        "all three present" if not missing_tracks else f"missing: {', '.join(missing_tracks)}",
    ))
    checks.append(result("Working directory", Path.cwd().resolve() == repo, str(Path.cwd().resolve())))

    free_gb = shutil.disk_usage(repo).free / (1024**3)
    checks.append(result("Free disk space", free_gb >= 3, f"{free_gb:.1f} GB available; 3 GB recommended"))

    try:
        outputs = repo/"outputs"
        outputs.mkdir(exist_ok=True)
        with tempfile.NamedTemporaryFile(prefix="ed_py_check_", dir=outputs, delete=True):
            pass
        checks.append(result("Output permissions", True, f"writable: {outputs}"))
    except OSError as exc:
        checks.append(result("Output permissions", False, str(exc)))

    checks.extend(check_imports())
    if args.online:
        checks.extend(check_online(args.timeout))
    else:
        print("[INFO] Online sources were not tested. Add --online before an event.")

    failed = [check for check in checks if not check["ok"]]
    status = "READY" if not failed else "ASK A MENTOR"
    print(f"\nOVERALL: {status} ({len(checks) - len(failed)}/{len(checks)} checks passed)")
    if args.json:
        print(json.dumps({"status": status, "checks": checks}, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
