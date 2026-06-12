[README](README.md) | [Introduction](Introduction.md) | Datasets ⮕ | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)

# Datasets

The notebook streams the RIB snapshot directly from OSDF — no manual download is required.

## RIB Snapshot: RouteViews route-views4 via OSDF

**OSDF URL:**
```
https://osdf-director.osg-htc.org/routeviews/route-views4/bgpdata/2023.03/RIBS/rib.20230322.1800.bz2
```

This is a **full RIB (Routing Information Base) snapshot** from the [RouteViews](https://www.routeviews.org/) route-views4 collector, captured at 18:00 UTC on March 22, 2023. RouteViews peers with hundreds of networks worldwide to collect a global view of BGP routing. The file is in MRT binary format (~94 MB compressed).

The data is hosted on the [Open Science Data Federation (OSDF)](https://osg-htc.org/services/osdf.html), which mirrors the full RouteViews archive (2008–present) across regional caches. `bgpkit.Parser` streams it directly from the nearest cache — no local copy needed.

The notebook's first cell lists all available snapshots for the date so you can see what is there.

### MRT File Fields

When bgpkit parses the RIB snapshot, each element represents one prefix-peer pair (one route that one collector peer is announcing). The fields you will use are:

| field | type | description |
| ----- | ---- | ----------- |
| `prefix` | string | IP prefix being announced (e.g., `"93.175.146.0/24"`) |
| `peer_asn` | int | ASN of the collector peer forwarding this route |
| `peer_ip` | string | IP address of the collector peer |
| `as_path` | list[int] | Sequence of ASNs from the peer to the origin |
| `origin_asns` | set[int] | Origin AS(es) — the last AS(es) in the AS path |
| `elem_type` | string | `"A"` (announcement) or `"W"` (withdrawal) — all entries in a RIB are `"A"` |

## RPKI Beacons

No separate download is needed. The three RPKI beacons are ordinary prefixes that appear as routes within the RIB snapshot above:

| prefix | roa_status | operator | purpose |
| ------ | ---------- | -------- | ------- |
| `93.175.146.0/24` | valid | RIPE NCC (AS12654) | Origin AS matches the ROA — a normal, valid route |
| `93.175.147.0/24` | invalid | RIPE NCC (AS196615) | Origin AS deliberately does not match the ROA — measures ROV enforcement |
| `84.205.83.0/24` | unknown | RIPE NCC | No ROA registered — baseline for comparison |

RIPE NCC maintains these prefixes specifically so that researchers can measure ROV deployment by counting which collector peers do and do not propagate the ROA-invalid beacon.

[README](README.md) | [Introduction](Introduction.md) | Datasets ⮕ | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)
