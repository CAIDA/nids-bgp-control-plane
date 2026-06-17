[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Notebook](nids-bgp-control-plane.ipynb)

# Tasks

Complete the tasks below in order. Tasks 2 and 3 are completed inside [nids-bgp-control-plane.ipynb](nids-bgp-control-plane.ipynb) — replace the `# YOUR CODE HERE` sections with your code and answer the questions in the markdown cells that follow.

## Task 1: Get access to NRP's JupyterHub and run the notebook there.

- step 1. [https://nrp.ai](https://nrp.ai/)
  - for more details [How To Access NRP](https://www.caida.org/projects/nids/how-to/access-nrp/)
- step 2. click on "Log In" in the upper right corner
- step 3. select your organization and log in
- step 4. Send an email to [training-program-info@caida.org](mailto:training-program-info@caida.org) with the email address you used to log into NRP.
  - We will add that address to the namespace `caida-nids`
- step 5. Log into NRP's JupyterHub [https://jupyterhub-west.nrp-nautilus.io/](https://jupyterhub-west.nrp-nautilus.io/)

  | Field        | Value       |
  | ------------ | ----------- |
  | Region       | Any         |
  | GPUs         | 0           |
  | Cores        | 1           |
  | RAM, GB      | 2           |
  | FPGAs        | 0           |
  | GPU type     | Any general |
  | Image        | **Scipy**   |
  | Architecture | amd64       |

- step 6. Upload nids-bgp-control-plane.ipynb and run it

## Task 2: CCDF of Origin AS IPv4 Prefix and Address Counts

Fetch a BGP RIB snapshot from a RouteViews collector via OSDF and bgpkit. For each prefix in the table, record the origin AS. Use this to compute per-AS metrics and plot their distributions.

- [ ] Build a `prefix → origin AS set` mapping and count MOAS prefixes (prefixes announced by more than one origin AS).
- [ ] Compute per-AS **prefix count**: the number of IPv4 prefixes each AS originates.
- [ ] Compute per-AS **address count**: the total IPv4 addresses covered, using longest-prefix-match to avoid double-counting nested prefixes.
- [ ] Plot a CCDF on a log-log scale with dual axes showing both prefix count and address count distributions.

- [ ] Q1: What does the shape of the CCDF reveal about how IPv4 prefixes are distributed across ASes?
- [ ] Q2: What percentage of prefixes are MOAS? What does a MOAS prefix imply for routing security?
- [ ] Q3: Why do the prefix-count and address-count CCDF curves diverge?

## Task 3: CCDF of Customer Cone IPv4 Prefix Count

Extend the per-AS analysis to customer cones. For each AS, aggregate the prefixes announced by every AS in its customer cone to measure its total routing footprint.

- [ ] Load the CAIDA PPDC customer cone file from the `data/` directory.
- [ ] Compute **cone prefix count**: sum the prefix counts of all ASes in the cone.
- [ ] Compute **cone address count**: merge the prefixes of all cone members (handling overlaps) and count the resulting address space.
- [ ] Plot a CCDF of cone prefix count and cone address count.

- [ ] Q4: What does the customer cone CCDF reveal about how IPv4 reachability is distributed across ASes?
- [ ] Q5: Why do the cone prefix-count and cone address-count curves diverge?
- [ ] Q6: How does the customer cone CCDF compare to the origin AS CCDF from Task 2? What does the difference tell you?

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ | [Notebook](nids-bgp-control-plane.ipynb)
