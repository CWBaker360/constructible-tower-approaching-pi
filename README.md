# A Constructible Tower Approaching Pi

**Author:** C. Wayne Baker  
**Date:** May 24, 2026  
**Status:** Revised mathematical note / source and reproducibility archive

This repository contains:

> **A Constructible Tower Approaching \(\pi\): Explicit Compass-and-Straightedge Approximants under Transparent Algebraic Acceleration**


## Current reviewed manuscript — v1.3 (October 29, 2026)

- [Read v1.3 PDF](paper/constructible_tower_v1_3.pdf)
- [LaTeX source v1.3](paper/constructible_tower_v1_3.tex)

These are the current reviewed manuscript files. The earlier `paper/constructible_tower_approaching_pi.*` pair and original concept PDF are retained as historical versions. The v1.3 update does not by itself constitute independent peer review.


## Earlier manuscript files (retained)

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
