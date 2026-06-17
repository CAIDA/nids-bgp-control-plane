README ⮕ | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)

# Understanding the BGP Control Plane

## Learning Objectives

The goal of this assignment is to understand how origin Autonomous Systems (ASes) announce IPv4 prefixes via BGP, how to parse and analyze BGP routing table data, and how to visualize prefix distribution using complementary cumulative distribution functions (CCDFs). This assignment builds on the ASN and customer cone concepts introduced in _nids-asn-introduction_.

## Overview

Start by reading **Introduction** to get the background needed to understand the assignment. **Datasets** explains each dataset and how to access it.

- step 1 [read the introduction](Introduction.md)
- step 2 [read dataset overviews](Datasets.md)
- step 3 [review the tasks](Tasks.md)
- step 4 log into NRP's JupyterHub, upload and complete the nids-bgp-control-plane.ipynb
  - Details instructions to access NRP: [How to access NRP](https://www.caida.org/projects/nids/how-to/access-nrp/)
  - complete each task by replacing the `# YOUR CODE HERE` sections
  - answer all six questions
- step 5 download your working notebook and replace ⬅ deliverable
- step 6 commit and push to github

### Directory Structure

```
nids-bgp-control-plane
├- Introduction.md                          # Introduction and background
├- Datasets.md                              # Dataset overview and access instructions
├- Tasks.md                                 # Task checklist and instructions
├- nids-bgp-control-plane.ipynb         ⬅  # Complete / Commit / Push
```

### Glossary

- **AS (Autonomous System)**: An independently operated network on the Internet, identified by a globally unique ASN.
- **AS Path**: The sequence of ASes a BGP route advertisement has traversed, recorded in each BGP announcement.
- **BGP (Border Gateway Protocol)**: The inter-domain routing protocol used to exchange reachability information between ASes on the Internet.
- **CCDF (Complementary Cumulative Distribution Function)**: A function showing the fraction of observations _greater than or equal to_ a given value. Used here to visualize how prefix and address counts are distributed across ASes.
- **Customer Cone**: The set of all ASes reachable from a given AS by following only provider-to-customer links. Introduced in _nids-asn-introduction_.
- **MOAS (Multi-Origin AS)**: A prefix announced as originating from more than one AS. MOAS prefixes can indicate routing misconfigurations or hijacks.
- **MRT (Multi-Threaded Routing Toolkit)**: A file format used to archive BGP routing tables and updates, recorded by collectors such as RouteViews.
- **Origin AS**: The AS that originates a BGP prefix announcement — the last ASN in the AS path.
- **OSDF (Open Science Data Federation)**: Distributed data infrastructure used by CAIDA to serve large datasets; the notebook fetches BGP RIB files via OSDF automatically.
- **Prefix**: A block of IP addresses expressed in CIDR notation (e.g., 192.0.2.0/24). An AS originates a prefix by announcing it in BGP.
- **RIB (Routing Information Base)**: A snapshot of the BGP routes a collector peer has received, capturing all prefix announcements visible at that vantage point.
- **RouteViews**: A University of Oregon project that collects and archives BGP routing tables from vantage points around the Internet. [ [website](https://www.routeviews.org/) ]
- **bgpkit**: A library for parsing MRT-format BGP data files, used in this notebook to process RIB snapshots.

README ⮕ | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)
