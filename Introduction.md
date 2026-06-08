[README](README.md) | Introduction ⮕ | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Report](Report.md)

# Introduction and Background

### Reading

- [What is BGP?](https://www.cloudflare.com/learning/security/glossary/what-is-bgp) (Cloudflare explainer)

## BGP: How ASes Exchange Routing Information

You already know from [nids-asn-introduction](https://github.com/CAIDA/nids-asn-introduction) that the Internet is a collection of Autonomous Systems (ASes) connected by provider-customer and peer-to-peer relationships. **BGP (Border Gateway Protocol)** is the protocol that makes these connections work: it is how ASes tell each other which IP prefixes they can reach and how to get there.

When an AS wants to announce that it can route traffic to a prefix (say, `203.0.113.0/24`), it sends a BGP **announcement** to its BGP neighbors. That announcement carries an **AS path** — the sequence of ASNs traffic must traverse to reach the destination. Neighbors propagate the announcement further, prepending their own ASN to the path. When a prefix is no longer reachable, the AS sends a BGP **withdrawal**.

A key property of BGP is that it relies entirely on **trust**: any AS can announce any prefix, and by default neighbors will accept and propagate those announcements. This makes BGP vulnerable to **route origin hijacking**, where a malicious (or misconfigured) AS announces a prefix it doesn't actually own, attracting traffic meant for someone else.

## BGP Collectors and MRT Files

Because BGP is a distributed protocol with no central log, researchers use **BGP collectors** to study it. RIPE NCC's [Routing Information Service (RIPE RIS)](https://ris.ripe.net) and the University of Oregon's [RouteViews](https://www.routeviews.org) project operate collectors around the world. Each collector peers with many ASes — called **collector peers** — that volunteer to forward their full routing tables to the collector.

The collector stores this data in **MRT (Multi-threaded Routing Toolkit)** files:
- **RIB (Routing Information Base) snapshots**: a full dump of what every collector peer currently announces, taken every few hours.
- **Update files**: incremental changes (announcements and withdrawals) recorded in real time.

In this module you will work with a RIB snapshot from RIPE RIS collector **rrc00** (Amsterdam). It records what each collector peer announced on March 22, 2023.

## RPKI: Cryptographic Prefix Ownership

**RPKI (Resource Public Key Infrastructure)** is a system that lets IP address holders publish cryptographically signed records — called **ROAs (Route Origin Authorizations)** — that state which AS is authorized to originate a given prefix. A route's **ROA validity state** is one of:

- **valid** — a ROA exists and the announcing AS matches it
- **invalid** — a ROA exists but the announcing AS does not match (possible hijack)
- **unknown** — no ROA has been published for the prefix

## ROV: Enforcing RPKI at the Router Level

A router that implements **ROV (Route Origin Validation)** checks incoming BGP announcements against the RPKI database and **drops routes whose origin AS makes them ROA-invalid**. If every AS on the Internet enforced ROV, BGP hijacks targeting ROA-protected prefixes would be blocked at the first ROV-enforcing hop.

In practice, ROV deployment is partial. Some ASes enforce it; many do not. This raises the empirical question: **what fraction of the Internet's routing infrastructure currently enforces ROV?**

## RPKI Beacons: Measuring ROV Adoption Empirically

RIPE NCC maintains three **RPKI beacons** — prefixes with known, stable ROA validity states — specifically for measuring ROV deployment:

| prefix | roa_status | description |
| ------ | ---------- | ----------- |
| `93.175.146.0/24` | valid | Announced by AS12654 (RIPE NCC); ROA matches |
| `93.175.147.0/24` | invalid | Announced by AS196615; ROA names a different origin AS — deliberately misconfigured |
| `84.205.83.0/24` | unknown | No ROA registered |

The inference logic is straightforward: a BGP collector peer that propagates the **valid** beacon but **not** the **invalid** beacon is likely enforcing ROV — it accepted the valid route but dropped the invalid one. A peer that propagates both beacons is likely not enforcing ROV.

This is exactly the measurement you will perform in this module.

#### Optional Further Reading

- [RIPE NCC RPKI beacons](https://www.ripe.net/manage-ips-and-asns/resource-management/rpki/routing-security-for-ris-bgp-beacons)
- [BGPkit documentation](https://bgpkit.com)
- [BGP hijacking explained](https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/) (Cloudflare)
- [RPKI overview](https://rpki.cloudflare.com) (Cloudflare)

[README](README.md) | Introduction ⮕ | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Report](Report.md)
