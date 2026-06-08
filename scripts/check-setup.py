"""Verify that the environment and data are ready for the assignment.

Usage:
    uv run scripts/check-setup.py
"""

import sys
from pathlib import Path

CHECKS: list[bool] = []


def check(label: str, ok: bool, fix: str = "") -> None:
    status = "OK  " if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok and fix:
        print(f"         → {fix}")
    CHECKS.append(ok)


def main() -> None:
    print("Checking setup...\n")

    # Python version
    check(
        "Python >= 3.11",
        sys.version_info >= (3, 11),
        "Run: uv python install 3.11",
    )

    # bgpkit Python package
    try:
        import bgpkit  # type: ignore  # noqa: F401
        check("bgpkit Python package (pybgpkit)", True)
    except ImportError:
        check(
            "bgpkit Python package (pybgpkit)",
            False,
            "Run: uv sync",
        )

    # bgpkit CLI
    import shutil
    check(
        "bgpkit-parser CLI",
        shutil.which("bgpkit-parser") is not None,
        "Install: brew install bgpkit/tap/bgpkit-parser  (see Setup.md for other platforms)",
    )

    # Data file
    data_file = Path("data/bview.20230322.0000.gz")
    check(
        f"data file: {data_file}",
        data_file.exists(),
        (
            "Run: wget -O data/bview.20230322.0000.gz "
            "http://data.ris.ripe.net/rrc00/2023.03/bview.20230322.0000.gz"
        ),
    )

    # Quick parse smoke-test (only if file and library are both present)
    if data_file.exists():
        try:
            import bgpkit  # type: ignore
            count = 0
            for _ in bgpkit.Parser(str(data_file)):
                count += 1
                if count >= 5:
                    break
            check("MRT file parses correctly", count > 0)
        except Exception as exc:
            check("MRT file parses correctly", False, f"Error: {exc}")

    # tables/ directory
    tables_dir = Path("tables")
    tables_dir.mkdir(exist_ok=True)
    check("tables/ directory exists", True)

    print()
    passed = sum(CHECKS)
    total = len(CHECKS)
    if passed == total:
        print(f"All {total} checks passed. You are ready to start.")
    else:
        print(f"{total - passed} check(s) failed. Fix the issues above and re-run.")
        sys.exit(1)


if __name__ == "__main__":
    main()
