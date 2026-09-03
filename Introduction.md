[README](README.md) | Introduction ⮕ | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Task 1](Task-count-addresses.md) | [Notebook](nids-bgp-control-plane.ipynb) | [Slides](slides/ETP-Week-02-BGP.pptx)

# Introduction and Background

### Reading

- [RouteViews Project](https://www.routeviews.org/) (website) — the BGP data collection infrastructure used in this assignment
- [CAIDA BGP Datasets](https://catalog.caida.org/search?query=bgp) (catalog) — CAIDA's collection of BGP-derived datasets
- [Border Gateway Protocol](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) (wikipedia) — how the protocol works
- [BGP-4 and its vulnerabilities](slides/ETP-Week-02-BGP.pptx) (slides) — the lecture deck for this assignment

### Prerequisite NIDS Assignments

- [How the Internet assigns and uses Autonomous Systems (ASes)](https://github.com/CAIDA/nids-asn-introduction)

## Introduction

In _nids-asn-introduction_ you explored how ASes are organized and measured by their customer cones. This assignment takes a closer look at **what those ASes actually do**: announce IP address space to the rest of the Internet using BGP.

<img width="100%" src="images/as-router-topology.png">

**BGP (Border Gateway Protocol)** is the inter-domain routing protocol — it carries reachability information between separately operated networks. When an organization acquires a block of IP addresses (a _prefix_), their AS announces that prefix to its BGP neighbors, and the announcement propagates across the Internet so that other networks can route traffic to it.

Each BGP announcement carries an **AS path**: the ordered sequence of ASNs a route has traversed. The last ASN in the path is the **origin AS** — the AS that originated the prefix. Route collectors like **RouteViews** peer with many ASes and archive full snapshots of their routing tables, called **RIBs (Routing Information Bases)**, in **MRT format**. This makes it possible to analyze the global view of prefix origination at a point in time.

### MOAS Prefixes

Some prefixes appear in the routing table with **more than one origin AS** — these are called **MOAS (Multi-Origin AS)** prefixes. MOAS announcements can arise from legitimate configurations (e.g., a multi-homed organization announces the same block from two ASes) or from routing incidents such as prefix hijacks. Measuring the fraction of MOAS prefixes gives some insight into the stability and security of the global routing system. In Task 1 the notebook reports how many prefixes are MOAS but excludes them from the per-AS prefix and address counts, since they cannot be attributed to a single origin.

### Prefix Count vs. Address Count

A natural way to measure an AS's contribution to the routing table is to count the number of prefixes it originates. However, prefixes vary enormously in size — a /8 covers 16 million addresses while a /24 covers only 256. A more meaningful metric is the **address count**: the total number of IP addresses covered by an AS's prefixes.

Address counting is not simply a matter of summing prefix sizes, because prefixes can overlap — a more-specific /24 may be nested inside a less-specific /16. The correct approach is to apply **longest-prefix-match** logic: an address is attributed to the most-specific prefix that covers it, avoiding double-counting. In the first part of this assignment (prefix-to-AS mapping) we map each prefix in a routing table to the AS that originates the most-specific subnet of that prefix. That is, we subtract address space in more-specific subnets originated by AS B from the address space in a corresponding less-specific prefix announced by AS A.

<img width="100%" src="images/address-counting.png">

### CCDF — Reading the Distribution

Because prefix and address counts span many orders of magnitude, we visualize their distributions using a **Complementary Cumulative Distribution Function (CCDF)** on a log-log scale. The CCDF at value _x_ gives the fraction of ASes that originate prefixes (or addresses) with a count _greater than or equal to x_. A steep initial drop-off shows that most ASes are small, while a long right-hand tail shows that a small number of ASes are very large. A straight line on a log-log CCDF is the signature of a **power-law distribution** — a pattern common in Internet topology measurements.

### Connecting Back to Customer Cones

In _nids-asn-introduction_ you measured a customer cone by counting ASes. In this assignment you will extend that idea to **prefix space**: for each AS, aggregate the prefixes announced by every AS in its customer cone. This gives a picture of how much of the Internet's address space each AS is responsible for routing, rather than just how many customer networks it serves. In our customer cone analysis we will _not_ subtract more specific subnets as we did for the prefix-to-AS mapping above.

### From Counts to Organizations

The first two tasks produce four numbers for every AS: the prefixes and addresses it originates itself, and the prefixes and addresses reachable through its customer cone. Those numbers say how big an AS is but not who it is. In the final task you rank every AS on all four metrics and use CAIDA's **AS2Org** dataset — which maps each ASN to the organization that operates it — to put names and countries to the networks at the top of each ranking, then explain why those particular organizations lead the metrics they lead.

#### Optional Reading

- [RouteViews MRT Data Archive](https://archive.routeviews.org/) (archive) — raw BGP data files
- [CAIDA RouteViews Prefix-to-AS Dataset](https://catalog.caida.org/dataset/routeviews_prefix2as) (dataset) — CAIDA's prefix-to-origin-AS mapping
- [Autonomous system](https://en.wikipedia.org/wiki/Autonomous_system_%28Internet%29) (wikipedia) — background on ASes

[README](README.md) | Introduction ⮕ | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Task 1](Task-count-addresses.md) | [Notebook](nids-bgp-control-plane.ipynb) | [Slides](slides/ETP-Week-02-BGP.pptx)
