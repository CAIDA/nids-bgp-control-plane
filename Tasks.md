[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ [Notebook](nids-bgp-control-plane.ipynb)

# Tasks

Complete the tasks below in order. Tasks 2, 3, and 4 are completed inside [nids-bgp-control-plane.ipynb](nids-bgp-control-plane.ipynb) — replace the `# YOUR CODE HERE` sections with your code and answer the questions in the markdown cells that follow.

## Task 1: Get access to NRP's JupyterHub and run the notebook there.

- step 1. [https://nrp.ai](https://nrp.ai/)
  - for more details: [How To Access NRP](https://www.caida.org/projects/nids/how-to/access-nrp/)
- step 2. Click on "Log In" in the upper right corner
- step 3. Select your organization and log in
- step 4. Send an email to [training-program-info@caida.org](mailto:training-program-info@caida.org) with the email address you used to log into NRP.
  - Details intructions to access nrp: [How to access NRP](https://www.caida.org/projects/nids/how-to/access-nrp/) and clone this repo
  - complete each task by replacing the `# YOUR CODE HERE` sections
  - answer all six questions
- step 5 download your working notebook ⬅ deliverable
- step 6 commit your version and push to github

## Task 2: Explore BGP Data and RPKI Beacons

Stream the RouteViews RIB snapshot from OSDF using bgpkit, filter to the three RPKI beacon prefixes, and examine the peer AS numbers, origin ASNs, and AS paths in the output.

- [ ] Q1: Approximately how many collector peers announce the ROA-valid beacon? How does this compare to the ROA-invalid beacon? What does the difference suggest about ROV deployment?
- [ ] Q2: Is the origin AS for the ROA-invalid beacon the same as for the ROA-valid beacon? Why or why not?
- [ ] Q3: The ROA-invalid beacon is deliberately misconfigured. Why does it still appear in routing tables at all? What does its presence tell you about ROV enforcement on the Internet?

## Task 3: RPKI Beacon Peer Summary

Count distinct collector peers and origin ASNs for each beacon prefix. The notebook writes the results to `tables/beacon-updates.md`.

- [ ] Q4: What fraction of peers that announce the valid beacon also announce the invalid one? What fraction appear to be filtering it?
- [ ] Q5: How many unique origin ASNs appear for the invalid beacon? What would it mean if the invalid beacon had multiple distinct origin ASNs?

## Task 4: Measure ROV Deployment

Categorize each collector peer as forwarding the invalid beacon, enforcing ROV, or forwarding neither. The notebook writes the results to `tables/rov-peers.md`.

- [ ] Q6: What percentage of peers appear to enforce ROV? Is this surprisingly high or low given that RPKI and ROV have been technically available since around 2012?
- [ ] Q7: This method infers ROV from a missing route. Name one alternative explanation for a missing route that has nothing to do with ROV enforcement.
- [ ] Q8: What additional data — not available from this single RIB snapshot — would make you more confident in your ROV enforcement estimate?

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | Tasks ⮕ [Notebook](nids-bgp-control-plane.ipynb)
