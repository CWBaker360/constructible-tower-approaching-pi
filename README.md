# A Constructible Tower Approaching Pi

**Author:** C. Wayne Baker  
**Date:** May 24, 2026  
**Status:** Revised mathematical note / source and reproducibility archive

This repository contains:

> **A Constructible Tower Approaching \(\pi\): Explicit Compass-and-Straightedge Approximants under Transparent Algebraic Acceleration**

## Read the revised paper

- [`paper/constructible_tower_approaching_pi.pdf`](paper/constructible_tower_approaching_pi.pdf)
- [`paper/constructible_tower_approaching_pi.tex`](paper/constructible_tower_approaching_pi.tex)

## Construction

The base values are the constructible polygonal half-perimeters

\[
P_{N_i}=N_i\sin\!\left(\frac{\pi}{N_i}\right),
\qquad N_i=4\cdot2^i.
\]

They are accelerated by

\[
T_{i,j}
=
T_{i,j-1}
+
\frac{T_{i,j-1}-T_{i-1,j-1}}{4^j-1}.
\]

Every finite tableau entry remains constructible because the base lengths are
constructible and the recurrence uses only field operations with rational
numbers.

## Corrected asymptotic law

Reconstruction of the missing source exposed a factor-of-two error in the
original concept PDF's limiting digit coefficient. The corrected law is

\[
\pi-T_{i,i}
\sim
\frac{\pi^{2i+3}}{(2i+3)!}
4^{-(i+1)(i+4)/2},
\]

and therefore

\[
D(i)
=
(\log_{10}2)i^2
+
2i\log_{10}i
+
O(i),
\qquad
\frac{D(i)}{i^2}\to\log_{10}2.
\]

The original claim \(D(i)/i^2\to2\log_{10}2\) is not consistent with the
interpolation-node product or with the reported numerical data.

## Reproduce the audit

```bash
python -m pip install mpmath
python scripts/verify_constructible_tower.py --precision 650 --output-dir output
```

Expected status:

```text
verification_passed: True
```

## Historical source

The originally supplied four-page PDF is retained at:

```text
docs/original_may24_concept_version.pdf
```

It is included for provenance only. The revised LaTeX/PDF pair in `paper/` is
the authoritative version.

## Rights

Copyright © 2026 C. Wayne Baker. All rights reserved unless otherwise stated.

## Manuscript review status (October 24, 2026)

The PDF and LaTeX files currently in `paper/` are the repository's existing published/preprint versions. A subsequent editorial and mathematical review has identified proposed clarifications for a future revision. Those revisions have **not** been merged into this repository, and the current PDF must not be described as incorporating them. Existing numerical verification scripts and results are unchanged. A revised source/PDF pair will be considered separately after a source-to-PDF consistency check and further mathematical review. This status notice makes no new scientific or priority claim.


## October 30, 2026 source update (PDF synchronization pending)

The reviewed October 29, 2026 manuscript source (v1.3) is now at [`paper/constructible_tower_v1_3.tex`](paper/constructible_tower_v1_3.tex). This versioned source was added without modifying the existing authoritative `paper/` LaTeX/PDF pair. The companion v1.3 PDF has **not yet been uploaded**, so links to the existing PDF still point to the previous version. Do not cite that PDF as v1.3 until the matched PDF is committed.
