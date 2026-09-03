[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | Task 1 ⮕ | [Notebook](nids-bgp-control-plane.ipynb) | [Slides](slides/ETP-Week-02-BGP.pptx)

<img src="images/address-counting.png">

# Task 1: Counting Addresses per Origin AS — How-To Guide

This provides a guide to one method for
implementing `addresses_per_asn`, one of the core functions in Task 1. Your goal is to count how many unique IPv4 addresses each origin AS "owns," given a list of `(prefix, asn)` pairs from a BGP RIB snapshot.

Two rules govern the count:

1. **No double-counting.** Every address is counted exactly once across all ASes.
2. **Longest-prefix match.** If two prefixes cover the same address, the more-specific one (higher `/N`) wins.

### Prefix Sizes

A prefix written as `A.B.C.D/N` covers **2^(32−N)** addresses. In Python: `1 << (32 - prefix_len)`. A `/8` covers 16,777,216 addresses; a `/24` covers only 256.

### Pytricia

**Pytricia** is a prefix trie — a data structure that acts like a dictionary keyed on IP prefixes and understands containment relationships between them. Two methods matter here:

- `pyt.children(prefix)` — returns all prefixes nested inside `prefix` at any depth. The prefix itself is included in the result; skip it with `if child == prefix: continue`.
- `pyt.parent(child)` — returns the immediately enclosing prefix of `child`.

### Counting by Subtraction

Summing raw prefix sizes would double-count addresses covered by nested prefixes. For example, if AS A originates `10.0.0.0/8` and AS B originates `10.1.0.0/16` (nested inside A's block), naively adding their sizes attributes 65,536 of A's addresses to both ASes.

The correct approach is to credit each prefix only with the addresses it exclusively covers. For each prefix, compute its raw size and subtract the sizes of its **direct children only**:

```
ASN A owns 10.0.0.0/8  (16,777,216 addresses)
ASN B owns 10.1.0.0/16 (    65,536 addresses, nested inside A)

A's count = 16,777,216 − 65,536 = 16,711,680  ✓
```

Subtracting **direct children only** — not all descendants — prevents grandchildren from being subtracted twice. If A→B→C (three levels), A subtracts B's full block, which already contains C. B then separately subtracts C. Subtracting C again from A would undercount A's contribution.

> **Gotcha:** this subtraction rule is for Task 1 only. Task 2's cone address count takes the
> union of every prefix in the cone — a sweep over prefixes sorted by address, with a running
> `covered_end` pointer — and does **not** subtract more-specifics announced by a different AS.

### Worked Example

```
Input: ("10.0.0.0/8", A), ("10.1.0.0/16", B), ("10.1.1.0/24", B)

  10.0.0.0/8  (A): size=16M,  child=10.1.0.0/16 → overlap=65K  → A += 16,711,680
  10.1.0.0/16 (B): size=65K,  child=10.1.1.0/24 → overlap=256  → B +=     65,280
  10.1.1.0/24 (B): size=256,  no children                       → B +=        256

  count[A] = 16,711,680   count[B] = 65,536   Total = 16,777,216  ✓
```

## What Your Write-Up Should Address

Task 1 asks three questions in the notebook. Once your counts run, look for:

- **Q1** — the overall shape of the CCDF: where the bulk of ASes sit, how far the tail reaches, and what a roughly straight log-log tail implies about the distribution.
- **Q2** — the MOAS share of the routing table, what a multi-origin announcement can legitimately mean, and why the same signal is used to detect hijacks.
- **Q3** — why the prefix-count and address-count curves separate, and what that says about the relationship between how many prefixes an AS announces and how much address space it holds.

[README](README.md) | [Introduction](Introduction.md) | [Datasets](Datasets.md) | [Tasks](Tasks.md) | Task 1 ⮕ | [Notebook](nids-bgp-control-plane.ipynb) | [Slides](slides/ETP-Week-02-BGP.pptx)
