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

Rebuild the authoritative **v1.3** paper (not the historical source):

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/constructible_tower_v1_3.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/constructible_tower_v1_3.tex
```

The analytic formula \(P_N=N\sin(\pi/N)\) is used only for verification. The
geometric construction of \(P_N\) uses regular polygons and does not require
\(\pi\) as input.

## Release verification gates (2026-11-10)

Verify the rebuilt v1.3 PDF has the expected page count and compare its extracted text with the committed `paper/constructible_tower_v1_3.pdf` (e.g. using `pdftotext` and `diff`), investigating any differences. A text match is not proof of pixel-for-pixel PDF identity.

To avoid changing historical output during initial verification, run the numerical script with a separate output directory (e.g. `--output-dir /tmp/tower_v1_3_check`) and compare the summary and CSV against archived results before preparing the release package.

## Historical checksum manifest status (2026-10-24)

`SHA256SUMS.txt` predates subsequent README and citation-metadata edits, and must not be treated as a verified manifest of the current repository checkout. The verification commands above refer to the currently checked-in scripts, not to the authoritative v1.3 manuscript unless specifically rebuilt and compared. The existing manifest is preserved as an earlier snapshot; regenerate and validate a complete manifest against the exact release commit before declaring repository-wide SHA-256 verification successful. Do not replace manuscript PDFs, source files, or scientific output merely to make a checksum match.
