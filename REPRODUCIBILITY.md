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
