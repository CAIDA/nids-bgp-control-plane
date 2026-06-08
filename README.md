README ⮕ | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Report](Report.md)

# Measuring BGP Control-Plane Security: ROV Deployment via RPKI Beacons

## Learning Objectives

The goal of this assignment is to measure how widely Route Origin Validation (ROV) is deployed across the Internet by analyzing a real BGP routing table snapshot. You will use three RPKI beacons — prefixes with known ROA validity states maintained by RIPE NCC specifically for this kind of measurement — to infer which BGP collector peers enforce ROV. This assignment builds directly on what you learned in `nids-asn-introduction`: you already understand what Autonomous Systems are; now you will see how they communicate routing information and how that information can be used to study routing security.

## Overview

Start by reading **Introduction** to understand BGP, RPKI, and the beacon methodology. **Setup** helps you install the tools and verify everything is working. **Datasets** explains the data you will use and how to download it. **Tasks** lays out the three tasks you need to complete.

- step 1 [read the Introduction](Introduction.md)
- step 2 [set up your environment](Setup.md)
- step 3 [download the dataset and read the dataset overview](Datasets.md)
- step 4 [follow the task instructions](Tasks.md)

## Commit/Submit

You will need to update and submit the following files.

- [scripts/beacon-updates.py](scripts/beacon-updates.py) (task 2)
- [scripts/rov-peers.py](scripts/rov-peers.py) (task 3)
- [Report.md](Report.md)
  - copy the tables you generated into the report
  - answer the questions in each section

### Directory Structure

```
nids-bgp-control-plane
├- Introduction.md                     # Introduction and background
├- Setup.md                            # Set up the environment
├- Datasets.md                         # Dataset overview and download instructions
├- Tasks.md                            # Task instructions
├- Report.md                        ⬅ # Final report — fill this in
└- scripts/
|  ├- check-setup.py                   # Verify setup (provided)
|  ├- beacon-updates.py           ⬅  # You will need to finish
|  └- rov-peers.py                ⬅  # You will need to finish
└- tables/
   ├- beacon-updates.md               # Created by beacon-updates.py
   └- rov-peers.md                    # Created by rov-peers.py
```

### Glossary

- **BGP (Border Gateway Protocol)**: the routing protocol that connects Autonomous Systems. ASes exchange BGP updates to advertise which IP prefixes they can reach.
- **BGP collector**: a passive measurement node operated by projects like RIPE RIS and RouteViews. It peers with many ASes (collector peers) to receive their routing tables.
- **Collector peer**: an AS that peers with a BGP collector and forwards its routing table to it.
- **MRT format**: a binary file format for storing BGP data. A RIB snapshot records the full routing table at a point in time.
- **RPKI (Resource Public Key Infrastructure)**: a cryptographic framework that lets IP address holders publish signed records binding prefixes to authorized origin ASNs.
- **ROA (Route Origin Authorization)**: an RPKI record stating which AS(es) may announce a specific prefix. A prefix is ROA-valid, ROA-invalid, or unknown (no ROA).
- **ROV (Route Origin Validation)**: a router policy that drops ROA-invalid routes, preventing their propagation.
- **RPKI beacon**: a prefix maintained specifically to measure ROV adoption. RIPE NCC operates one ROA-valid, one ROA-invalid, and one unknown beacon.

README ⮕ | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Report](Report.md)
