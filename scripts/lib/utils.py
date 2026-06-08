"""Provided utilities for nids-bgp-control-plane scripts."""

from pathlib import Path

# The three RPKI beacon prefixes used in this module.
# Each tuple is (prefix, roa_status).
BEACONS = [
    ("93.175.146.0/24", "valid"),
    ("93.175.147.0/24", "invalid"),
    ("84.205.83.0/24",  "unknown"),
]

# Convenience lookup: prefix string -> ROA validity string
ROA_STATUS = {prefix: status for prefix, status in BEACONS}


def open_mrt(path: str | Path):
    """Return a bgpkit Parser iterable for the given MRT file.

    Each element has dot-notation fields:
        elem.prefix         str   — announced prefix, e.g. "93.175.146.0/24"
        elem.peer_asn       int   — ASN of the collector peer
        elem.peer_ip        str   — IP of the collector peer
        elem.as_path        list  — sequence of ASNs from peer to origin
        elem.origin_asns    set   — origin ASN(s) (last AS(es) in the path)
        elem.elem_type      str   — "A" (announce) or "W" (withdraw)

    Usage:
        for elem in open_mrt("data/bview.20230322.0000.gz"):
            if elem.prefix in ROA_STATUS:
                print(elem.prefix, elem.peer_asn, elem.origin_asns)
    """
    import bgpkit  # type: ignore
    return bgpkit.Parser(str(path))
