[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | Report

# Measuring BGP Control-Plane Security: ROV Deployment via RPKI Beacons

**Name:** (your name here)<br/>
**Date:** (date here)

## To Do

- **Task 1**: Explore BGP Data and RPKI Beacons
  - [ ] download `data/bview.20230322.0000.gz`
  - [ ] run `uv run scripts/check-setup.py` — all checks pass
  - [ ] [explore with bgpkit CLI](Tasks.md#12-explore-with-bgpkit-cli)
  - [ ] [explore with BGP2GO](Tasks.md#13-explore-with-bgp2go)
  - [ ] Answer questions 1, 2, and 3
- [**Task 2**: RPKI Beacon Peer Summary](#task-2-rpki-beacon-peer-summary)
  - [ ] [Read RPKI Beacons overview in Datasets.md](Datasets.md#rpki-beacons)
  - [ ] [Read Task 2](Tasks.md#task-2-rpki-beacon-peer-summary)
  - [ ] Replace the TODO comments with your code in [scripts/beacon-updates.py](scripts/beacon-updates.py)
  - [ ] build `tables/beacon-updates.md`
  - [ ] copy `tables/beacon-updates.md` into this document at INSERT
  - [ ] Answer questions 4 and 5
- [**Task 3**: Measure ROV Deployment](#task-3-measure-rov-deployment)
  - [ ] [Read Task 3](Tasks.md#task-3-measure-rov-deployment)
  - [ ] Replace the TODO comments with your code in [scripts/rov-peers.py](scripts/rov-peers.py)
  - [ ] build `tables/rov-peers.md`
  - [ ] copy `tables/rov-peers.md` into this document at INSERT
  - [ ] Answer questions 6, 7, and 8

---

## Task 1: Explore BGP Data and RPKI Beacons

### 1.4 Questions 1, 2, and 3

1. Using bgpkit or BGP2GO, approximately how many collector peers announce the ROA-valid beacon (`93.175.146.0/24`)? How does this count compare to the ROA-invalid beacon (`93.175.147.0/24`)? What does this difference suggest about ROV deployment?

   **(your answer here)**

2. Look at the origin ASN(s) for the ROA-invalid beacon in the bgpkit output. Is the origin AS the same as for the ROA-valid beacon? Why or why not?

   **(your answer here)**

3. The ROA-invalid beacon is deliberately misconfigured by RIPE NCC. Why does it still appear in routing tables at all? What does its continued presence tell you about the current state of ROV enforcement on the Internet?

   **(your answer here)**

---

## Task 2: RPKI Beacon Peer Summary

### Table 1: RPKI Beacon Peer Observations

{{INSERT:tables/beacon-updates.md}}

### 2.2 Questions 4 and 5

4. What fraction of peers that announce the valid beacon also announce the invalid one? What fraction appear to be filtering the invalid beacon?

   **(your answer here)**

5. How many unique origin ASNs appear for the invalid beacon? How many for the valid beacon? What would it mean if the invalid beacon had multiple distinct origin ASNs?

   **(your answer here)**

---

## Task 3: Measure ROV Deployment

### Table 2: Collector Peer ROV Enforcement

{{INSERT:tables/rov-peers.md}}

### 3.2 Questions 6, 7, and 8

6. What percentage of peers in the snapshot appear to enforce ROV? Is this surprisingly high or low given that RPKI and ROV have been technically available since around 2012?

   **(your answer here)**

7. This method infers ROV from a missing route. Name one alternative explanation for why a peer might not have a route for the invalid prefix that has nothing to do with ROV enforcement.

   **(your answer here)**

8. What additional data — not available from this single RIB snapshot — would make you more confident in your ROV enforcement estimate?

   **(your answer here)**

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | Report
