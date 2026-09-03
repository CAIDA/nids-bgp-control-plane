[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Task 1](Task-count-addresses.md) | [Notebook](nids-bgp-control-plane.ipynb) | [Slides](slides/ETP-Week-02-BGP.pptx)

# Tasks

Complete the tasks below in order. All three tasks are completed inside [nids-bgp-control-plane.ipynb](nids-bgp-control-plane.ipynb) — replace the `# YOUR CODE HERE` sections with your code and answer the six questions in the markdown cells that follow.

## Task 0: Get access to NRP's JupyterHub and run the notebook there.

Use this link if you need to [get access to NRP's JupyterHub](https://www.caida.org/projects/nids/how-to/access-nrp/)

- step 1. Go to [JupyterHub](https://jupyterhub-west.nrp-nautilus.io)
  - upload `nids-bgp-control-plane.ipynb` and run it
  - complete each task by replacing the `# YOUR CODE HERE` sections
  - answer all questions
- step 2. Download your completed notebook, commit, and submit.

Before starting Task 1, confirm your environment:

- [ ] the setup cell (`%pip install pybgpkit-parser pelicanfs pytricia pandas`) runs without error
- [ ] the imports in that same cell succeed — in particular `import pytricia` and `from pelicanfs.core import OSDFFileSystem`
- [ ] the first Task 1 cell prints a `reading https://osdf-director.osg-htc.org/...` line, showing the RIB listing worked

## Task 1: CCDF of Origin AS IPv4 Prefix and Address Counts

Fetch a BGP RIB snapshot from a RouteViews collector. Build a `prefix → origin AS set` mapping, identify MOAS prefixes, then compute per-AS prefix count and address count (using longest-prefix-match to avoid double-counting nested prefixes). Plot a CCDF on a log-log scale with dual axes. MOAS prefixes are counted but excluded from the per-AS totals, and IPv6 prefixes are skipped. The address-counting method is explained in the [Task 1 guide](Task-count-addresses.md).

- [ ] Q1: What does the shape of the CCDF reveal about how IPv4 prefixes are distributed among origin ASes?
- [ ] Q2: What percentage of IPv4 prefixes are MOAS (announced by more than one origin AS)? What does MOAS represent, and why does it matter for routing security?
- [ ] Q3: Why do the prefix-count curve and the address-count curve diverge on the plot? What does this tell you about how address space is allocated relative to prefix announcements?

## Task 2: CCDF of Customer Cone IPv4 Prefix and Address Counts

Load the CAIDA provider-peer customer cone (`ppdc-ases`) file, which the notebook downloads for you. For each root AS, aggregate the prefix counts and address counts of every AS in its customer cone. Plot a CCDF of cone prefix count and cone address count. The notebook then overlays all four CCDFs — origin and cone, prefix and address — on a single combined plot; use it for Q5.

- [ ] Q4: What does the shape of the customer cone CCDF reveal about how IPv4 reachability is distributed across ASes?
- [ ] Q5: Why are the customer-cone values (both prefix count and address count) larger than the origin values? Reference the combined plot and the printed statistics.

## Task 3: Ranked Table of Top ASNs

Load the CAIDA AS2Org dataset and build a ranked table of every ASN that appears in the
**top 3 of any** of four size metrics: own prefix count, own address count, customer-cone
prefix count, and customer-cone address count. For each qualifying ASN show its rank and
raw count for all four metrics, plus the organization name and country from AS2Org. Sort
rows so ASNs with the best rank in any column appear first.

- [ ] Q6: Write a single sentence for each of the top 4 organizations: what are they, and why would they be ranked so high?

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Task 1](Task-count-addresses.md) | [Notebook](nids-bgp-control-plane.ipynb) | [Slides](slides/ETP-Week-02-BGP.pptx)
