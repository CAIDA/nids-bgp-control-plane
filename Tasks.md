[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Report](Report.md)

## Overview

```
Report.md                               ⬅ Update with tables and answers
└- scripts/
|  ├- beacon-updates.py           ⬅ You will need to write
|  └- rov-peers.py               ⬅ You will need to write
└- tables/
   ├- beacon-updates.md
   └- rov-peers.md
```

- Task 1 [Download dataset, explore with bgpkit CLI and BGP2GO](Datasets.md)
  - step 1.1 download `data/bview.20230322.0000.gz`
  - step 1.2 explore with bgpkit CLI
  - step 1.3 explore with BGP2GO
  - step 1.4 answer questions 1, 2, and 3
- Task 2: Create **scripts/beacon-updates.py**
  - step 2.1 use that script to create **tables/beacon-updates.md**
  - step 2.2 use **tables/beacon-updates.md** to answer questions 4 and 5
- Task 3: Create **scripts/rov-peers.py**
  - step 3.1 use that script to create **tables/rov-peers.md**
  - step 3.2 use **tables/rov-peers.md** to answer questions 6, 7, and 8

All tables and the final Report.md are in Markdown.

---

## Task 1: Explore BGP Data and RPKI Beacons

([Download instructions](Datasets.md))

### 1.1 Download the dataset

Follow the [download instructions in Datasets.md](Datasets.md) to download `data/bview.20230322.0000.gz`.

### 1.2 Explore with bgpkit CLI

The `bgpkit-parser` command lets you filter the MRT file by prefix and print the results as JSON. Use it to look at the three beacon prefixes:

```bash
# Routes for the ROA-invalid beacon
bgpkit-parser data/bview.20230322.0000.gz --prefix 93.175.147.0/24 | head -20

# Routes for the ROA-valid beacon (for comparison)
bgpkit-parser data/bview.20230322.0000.gz --prefix 93.175.146.0/24 | head -20

# Routes for the unknown beacon
bgpkit-parser data/bview.20230322.0000.gz --prefix 84.205.83.0/24 | head -20
```

Look at the `peer_asn`, `origin_asns`, and `as_path` fields in the output.

### 1.3 Explore with BGP2GO

Open **http://nids.caida.org:44444/** and search for each of the three beacon prefixes. Filter to the date **2023-03-22** to align with the RIB snapshot you downloaded.

Observe: which collectors see each beacon? Are the AS paths for the valid and invalid beacons different?

### 1.4 Answer questions 1, 2, and 3

1. Using bgpkit or BGP2GO, approximately how many collector peers announce the ROA-valid beacon (`93.175.146.0/24`)? How does this count compare to the ROA-invalid beacon (`93.175.147.0/24`)? What does this difference suggest about ROV deployment?

2. Look at the origin ASN(s) for the ROA-invalid beacon in the bgpkit output. Is the origin AS the same as for the ROA-valid beacon? Why or why not?

3. The ROA-invalid beacon is deliberately misconfigured by RIPE NCC. Why does it still appear in routing tables at all? What does its continued presence tell you about the current state of ROV enforcement on the Internet?

---

## Task 2: RPKI Beacon Peer Summary

### 2.1 Create scripts/beacon-updates.py

You need to write **scripts/beacon-updates.py** so that it runs with the following parameters and produces **Table 1**.

We have provided a skeleton script for you to use. Please replace the **TODO** sections with your code.

```bash
uv run scripts/beacon-updates.py --output tables/beacon-updates.md data/bview.20230322.0000.gz
```

### Table 1: RPKI Beacon Peer Observations

- **prefix**: the beacon prefix
- **roa_status**: `valid`, `invalid`, or `unknown`
- **peers_announcing**: the number of distinct collector peers (by `peer_asn`) that have a route for this prefix
- **unique_origin_asns**: the number of distinct origin ASNs observed across all routes for this prefix

| prefix | roa_status | peers_announcing | unique_origin_asns |
| ------ | ---------- | ---------------: | -----------------: |
| 93.175.146.0/24 | valid | [count] | [count] |
| 93.175.147.0/24 | invalid | [count] | [count] |
| 84.205.83.0/24 | unknown | [count] | [count] |

### 2.2 Answer questions 4 and 5

4. What fraction of peers that announce the valid beacon also announce the invalid one? What fraction appear to be filtering the invalid beacon (i.e., announce valid but not invalid)?

5. How many unique origin ASNs appear for the invalid beacon? How many for the valid beacon? What would it mean if the invalid beacon had multiple distinct origin ASNs?

---

## Task 3: Measure ROV Deployment

### 3.1 Create scripts/rov-peers.py

You need to write **scripts/rov-peers.py** so that it runs with the following parameters and produces **Table 2**.

We have provided a skeleton script for you to use. Please replace the **TODO** sections with your code.

```bash
uv run scripts/rov-peers.py --output tables/rov-peers.md data/bview.20230322.0000.gz
```

The script should:
- Build a set `peers_valid`: all distinct `peer_asn` values that have a route for `93.175.146.0/24` (ROA-valid).
- Build a set `peers_invalid`: all distinct `peer_asn` values that have a route for `93.175.147.0/24` (ROA-invalid).
- Compute these categories:
  - **forwarded invalid**: peers in `peers_invalid` — they propagated the invalid beacon
  - **enforced ROV**: peers in `peers_valid` but not `peers_invalid` — they announced the valid beacon but have no route for the invalid one
  - **forwarded neither**: peers in neither set

### Table 2: Collector Peer ROV Enforcement

- **category**: description of the peer's observed behavior
- **peers**: count of peers in this category
- **percentage**: share of all peers seen in the snapshot (one decimal place)

| category | peers | percentage |
| -------- | ----: | ---------: |
| forwarded invalid | [count] | [%] |
| enforced ROV (valid, not invalid) | [count] | [%] |
| forwarded neither beacon | [count] | [%] |
| total peers | [count] | — |

### 3.2 Answer questions 6, 7, and 8

6. What percentage of peers in the snapshot appear to enforce ROV? Is this surprisingly high or low given that RPKI and ROV have been technically available since around 2012?

7. This method infers ROV from a missing route. Name one alternative explanation for why a peer might not have a route for the invalid prefix that has nothing to do with ROV enforcement.

8. What additional data — not available from this single RIB snapshot — would make you more confident in your ROV enforcement estimate?

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Report](Report.md)
