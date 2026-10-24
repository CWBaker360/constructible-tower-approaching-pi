# Reproducibility

## Requirements

- Python 3.10 or newer
- `mpmath`
- `pdflatex`

Install:

```bash
python -m pip install mpmath
```

Run:

```bash
python scripts/verify_constructible_tower.py --precision 650 --output-dir output
```

The script builds the complete triangular tableau through level 30, records
the diagonal values and correct-digit counts, and compares the exact errors
with the leading asymptotic model.

Rebuild the paper:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/constructible_tower_approaching_pi.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/constructible_tower_approaching_pi.tex
```

The analytic formula \(P_N=N\sin(\pi/N)\) is used only for verification. The
geometric construction of \(P_N\) uses regular polygons and does not require
\(\pi\) as input.

## Checksum manifest status (2026-10-24)

`SHA256SUMS.txt` predates subsequent README and citation-metadata edits, and must not be treated as a verified manifest of the current repository checkout. The verification commands above refer to the currently checked-in scripts, not to the pending revised manuscripts. The existing manifest is preserved as an earlier snapshot; regenerate and validate a complete manifest against the exact release commit before declaring repository-wide SHA-256 verification successful. Do not replace manuscript PDFs, source files, or scientific output merely to make a checksum match.
