[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Notebook](nids-bgp-control-plane.ipynb)

# Tasks

Complete the tasks below in order. Tasks 1 and 2 are completed inside [nids-bgp-control-plane.ipynb](nids-bgp-control-plane.ipynb) — replace the `# YOUR CODE HERE` sections with your code and answer the questions in the markdown cells that follow.

## Task 0: Get access to NRP's JupyterHub and run the notebook there.

Use this link if you need to [get access to NRP's JupyterHub](https://www.caida.org/projects/nids/how-to/access-nrp/)

- step 1. Go to [JupyterHub](https://jupyterhub-west.nrp-nautilus.io)
  - upload `nids-bgp-control-plane.ipynb` and run it
  - complete each task by replacing the `# YOUR CODE HERE` sections
  - answer all questions
- step 2. Download your completed notebook, commit, and submit.

## Task 1: CCDF of Origin AS IPv4 Prefix and Address Counts

Fetch a BGP RIB snapshot from a RouteViews collector. Build a `prefix → origin AS set` mapping, identify MOAS prefixes, then compute per-AS prefix count and address count (using longest-prefix-match to avoid double-counting nested prefixes). Plot a CCDF on a log-log scale with dual axes.

- [ ] Q1: What does the shape of the CCDF reveal about how IPv4 prefixes are distributed among origin ASes?
- [ ] Q2: What percentage of IPv4 prefixes are MOAS? What does MOAS represent, and why does it matter for routing security?
- [ ] Q3: Why do the prefix-count curve and the address-count curve diverge? What does this tell you about how address space is allocated relative to prefix announcements?

## Task 2: CCDF of Customer Cone IPv4 Prefix and Address Counts

Load the CAIDA PPDC customer-cone file. For each root AS, aggregate the prefix counts and address counts of every AS in its customer cone. Plot a CCDF of cone prefix count and cone address count.

- [ ] Q4: What does the shape of the customer cone CCDF reveal about how IPv4 reachability is distributed across ASes?
- [ ] Q5: Why do the prefix-count and address-count curves diverge on the cone plot? What does this tell you about how large transit providers aggregate address space?
- [ ] Q6: How does the customer cone CCDF compare to the origin AS CCDF from Task 1? Why might the customer cone CCDFs converge long before the origin CCDFs?

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Notebook](nids-bgp-control-plane.ipynb)
