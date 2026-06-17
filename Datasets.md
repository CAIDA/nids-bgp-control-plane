[README](README.md) | [Introduction](Introduction.md) | Datasets ⮕ | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)

# Datasets

## BGP Routing Table (RIB) Snapshots

The notebook uses BGP RIB snapshots collected by **RouteViews**, a University of Oregon project that peers with ASes around the world and archives their full routing tables. Each snapshot captures every prefix announcement visible from a vantage point at a specific moment in time.

### MRT Format

RIB files are stored in **MRT (Multi-Threaded Routing Toolkit)** format. Each entry represents one prefix announcement and contains:

| Field     | Example         | Description                                              |
| --------- | --------------- | -------------------------------------------------------- |
| prefix    | 192.0.2.0/24    | The announced IP prefix in CIDR notation                 |
| as_path   | 3356 1299 13335 | Sequence of ASNs the route traversed                     |
| origin_as | 13335           | Last ASN in the path — the AS that originated the prefix |
| next_hop  | 198.51.100.1    | Next-hop IP address toward the destination               |

### bgpkit

The notebook uses **[bgpkit](https://bgpkit.com/)**, a library for parsing MRT-format BGP data. bgpkit handles decompression, MRT record parsing, and filtering, letting the notebook iterate over RIB entries as Python objects without dealing with the binary format directly.

### OSDF

The notebook fetches RIB files via **OSDF (Open Science Data Federation)**, a distributed data infrastructure that provides high-speed access to large scientific datasets. The notebook handles this automatically — no manual download step is needed for the RIB data.

[ [RouteViews website](https://www.routeviews.org/) | [CAIDA BGP datasets](https://catalog.caida.org/search?query=bgp) ]

---

## CAIDA AS Customer Cone

You will download the CAIDA AS Customer Cone file (`20260501.ppdc-ases.txt.bz2`) the same way you did in _nids-asn-introduction_, and place it in the `data/` directory.

As a quick reminder, the file format is:

```
# comment lines start with #
# each data line: <root AS> <member AS1> <member AS2> ...
23 23 4 1
1 1
```

The cone size for an AS is the number of space-separated tokens on its line minus one (the first token is the AS itself). Refer to [nids-asn-introduction/Datasets.md](../../nids-asn-introduction/nids-asn-introduction/Datasets.md) for full download instructions and dataset details.

[README](README.md) | [Introduction](Introduction.md) | Datasets ⮕ | [Tasks](Tasks.md) | [Notebook](nids-bgp-control-plane.ipynb)
