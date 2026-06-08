"""Count distinct peers and origin ASNs for each RPKI beacon prefix.

Usage:
    uv run scripts/beacon-updates.py --output tables/beacon-updates.md data/bview.20230322.0000.gz
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# ----------------------------------------------------------------
# We recommend iterating with open_mrt() from lib.utils.
# Each element has these fields (dot notation):
#
#   elem.prefix        str  — announced prefix, e.g. "93.175.146.0/24"
#   elem.peer_asn      int  — ASN of the collector peer
#   elem.origin_asns   set  — origin AS(es) at the end of the AS path
#
# Example:
#   for elem in open_mrt(args.input):
#       if elem.prefix in ROA_STATUS:
#           # record elem.peer_asn and elem.origin_asns for this prefix
# ----------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from lib.utils import open_mrt, BEACONS, ROA_STATUS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count peers and origin ASNs for each RPKI beacon prefix."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("data/bview.20230322.0000.gz"),
        help="Path to MRT RIB file (default: data/bview.20230322.0000.gz)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("tables/beacon-updates.md"),
        help="Output markdown file path (default: tables/beacon-updates.md)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    table = None
    """
    TODO:
    1. Use open_mrt(args.input) to iterate over all BGP elements in the RIB file.
       For each element where elem.prefix is a key in ROA_STATUS:
       - Add elem.peer_asn to a set of peers for that prefix.
       - Add all ASNs from elem.origin_asns to a set of origin ASNs for that prefix.

    2. For each beacon prefix in BEACONS order, compute:
       - peers_announcing : len of the peer set for that prefix
       - unique_origin_asns : len of the origin ASN set for that prefix

    3. Build Table 1 as a Markdown table string and assign it to `table`:
       - Columns: prefix, roa_status, peers_announcing, unique_origin_asns
       - Rows: one per beacon in BEACONS order (valid, invalid, unknown)
       - Right-align the count columns

    The output should look like:

    | prefix            | roa_status | peers_announcing | unique_origin_asns |
    | ----------------- | ---------- | ---------------: | -----------------: |
    | 93.175.146.0/24   | valid      |              [n] |                [n] |
    | 93.175.147.0/24   | invalid    |              [n] |                [n] |
    | 84.205.83.0/24    | unknown    |              [n] |                [n] |
    """

    if table is None:
        raise SystemExit(replace_todo_message)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(table, encoding="utf-8")
    print(f"Wrote table to {args.output}", file=sys.stderr)
    print(table)


replace_todo_message = """
    -----------------------------------------------
    Please replace the TODO comments with your code
    -----------------------------------------------
    """


if __name__ == "__main__":
    main()
