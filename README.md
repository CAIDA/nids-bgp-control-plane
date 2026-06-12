README ⮕ | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)

# Measuring BGP Control-Plane Security: ROV Deployment via RPKI Beacons

## Learning Objectives

The goal of this assignment is to measure how widely Route Origin Validation (ROV) is deployed across the Internet by analyzing a real BGP routing table snapshot. You will use three RPKI beacons — prefixes with known ROA validity states maintained by RIPE NCC specifically for this kind of measurement — to infer which BGP collector peers enforce ROV. This assignment builds directly on what you learned in [nids-asn-introduction](https://github.com/CAIDA/nids-asn-introduction): you already understand what Autonomous Systems are; now you will see how they communicate routing information and how that information can be used to study routing security.

## Overview

Start by reading **Introduction** to understand BGP, RPKI, and the beacon methodology. **Datasets** explains the data you will use. **Tasks** lays out the four tasks you need to complete.

- step 1 [read the Introduction](Introduction.md)
- step 2 [read the dataset overview](Datasets.md)
- step 3 [review the tasks](Tasks.md)
- step 4 log into NRP's JupyterHub, upload and complete [nids-bgp-control-plane.ipynb](nids-bgp-control-plane.ipynb)
  - Details intructions to access nrp: [How to access NRP](https://www.caida.org/projects/nids/how-to/access-nrp/)
  - replace all `# YOUR CODE HERE` sections with your code
  - answer all eight questions in the markdown cells
- step 5 download your completed `nids-bgp-control-plane.ipynb` ⬅ deliverable
- step 6 commit and push the completed notebook to GitHub

### Directory Structure

```
nids-bgp-control-plane
├- Introduction.md                     # Introduction and background
├- Datasets.md                         # Dataset overview
├- Tasks.md                            # Task checklist
├- nids-bgp-control-plane.ipynb    ⬅  # Complete this notebook
```

### Glossary

- **BGP (Border Gateway Protocol)**: the routing protocol that connects Autonomous Systems. ASes exchange BGP updates to advertise which IP prefixes they can reach.
- **BGP collector**: a passive measurement node operated by projects like RIPE RIS and RouteViews. It peers with many ASes (collector peers) to receive their routing tables.
- **Collector peer**: an AS that peers with a BGP collector and forwards its routing table to it.
- **MRT format**: a binary file format for storing BGP data. A RIB snapshot records the full routing table at a point in time.
- **[RPKI (Resource Public Key Infrastructure)](https://blog.cloudflare.com/rpki/)**: a cryptographic framework that lets IP address holders publish signed records binding prefixes to authorized origin ASNs.
- **ROA (Route Origin Authorization)**: an RPKI record stating which AS(es) may announce a specific prefix. A prefix is ROA-valid, ROA-invalid, or unknown (no ROA).
- **ROV (Route Origin Validation)**: a router policy that drops ROA-invalid routes, preventing their propagation.
- **RPKI beacon**: a prefix maintained specifically to measure ROV adoption. RIPE NCC operates one ROA-valid, one ROA-invalid, and one unknown beacon.

README ⮕ | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)
