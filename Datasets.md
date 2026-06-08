[README](README.md) | [Introduction](Introduction.md) | Datasets ⮕ | [Tasks](Tasks.md) | [Report](Report.md)

# Datasets

```
data/
└── bview.20230322.0000.gz    ← download with the command below
```

## Download the RIPE RIS RIB Snapshot

Download the March 22, 2023 RIB snapshot from RIPE RIS collector rrc00 (Amsterdam):

```bash
wget -O data/bview.20230322.0000.gz \
  http://data.ris.ripe.net/rrc00/2023.03/bview.20230322.0000.gz
```

This is a **full RIB (Routing Information Base) snapshot**: it records every prefix that every collector peer was announcing at midnight UTC on that date. The file is in MRT binary format and is approximately 50 MB compressed. You do not need to decompress it — bgpkit handles that automatically.

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

## BGP2GO Web Interface

BGP2GO provides an interactive web interface for exploring prefix history across BGP collectors:

- **URL**: http://nids.caida.org:44444/
- Filter to date **2023-03-22** to align with the RIB snapshot
- Search for each of the three beacon prefixes to see which collectors observe them and what AS paths they carry

You will use BGP2GO in Task 1 to explore the beacons before writing any code.

[README](README.md) | [Introduction](Introduction.md) | Datasets ⮕ | [Tasks](Tasks.md) | [Report](Report.md)
