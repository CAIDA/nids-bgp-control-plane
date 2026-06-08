"""Categorize collector peers by ROV enforcement inferred from RPKI beacon propagation.

Usage:
    uv run scripts/rov-peers.py --output tables/rov-peers.md data/bview.20230322.0000.gz
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# ----------------------------------------------------------------
# Use open_mrt() from lib.utils to iterate over BGP elements.
# Each element has:
#
#   elem.prefix    str — announced prefix
#   elem.peer_asn  int — ASN of the collector peer
#
# Build two sets by iterating once over the file:
#
#   peers_valid   : peer_asn values that have a route for 93.175.146.0/24
#   peers_invalid : peer_asn values that have a route for 93.175.147.0/24
#
# A peer is inferred to enforce ROV if it is in peers_valid
# but NOT in peers_invalid.
# ----------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from lib.utils import open_mrt


VALID_BEACON   = "93.175.146.0/24"
INVALID_BEACON = "93.175.147.0/24"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Categorize collector peers by ROV enforcement "
            "inferred from RPKI beacon propagation."
        )
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
        default=Path("tables/rov-peers.md"),
        help="Output markdown file path (default: tables/rov-peers.md)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    table = None
    """
    TODO:
    1. Use open_mrt(args.input) to iterate over all BGP elements.
       Build two sets in a single pass:
         - peers_valid   : all peer_asn values where elem.prefix == VALID_BEACON
         - peers_invalid : all peer_asn values where elem.prefix == INVALID_BEACON
       Also build peers_all: all peer_asn values seen for either beacon.

    2. Compute the three categories:
         - forwarded_invalid = len(peers_invalid)
         - enforced_rov      = len(peers_valid - peers_invalid)
             (announced valid but have no route for invalid)
         - forwarded_neither = len(peers_all - peers_valid - peers_invalid)
         - total_peers       = len(peers_all)

    3. Build Table 2 as a Markdown table string and assign it to `table`:
       - Columns: category, peers, percentage
       - Rows:
           forwarded invalid             [count]   [%]
           enforced ROV (valid, not invalid)  [count]   [%]
           forwarded neither beacon      [count]   [%]
           total peers                   [count]   —
       - percentage = count / total_peers * 100, one decimal place
       - The total row uses "—" instead of a percentage

    The output should look like:

    | category                          | peers | percentage |
    | --------------------------------- | ----: | ---------: |
    | forwarded invalid                 |   [n] |       [n]% |
    | enforced ROV (valid, not invalid) |   [n] |       [n]% |
    | forwarded neither beacon          |   [n] |       [n]% |
    | total peers                       |   [n] |          — |
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
