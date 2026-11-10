# Zenodo handoff — Constructible Tower v1.3

**Prepared:** 2026-11-10  
**Status:** Publication preparation; NOT a Zenodo deposit or verification certificate.

## Record metadata

- **Title:** A Constructible Tower Approaching Pi: Explicit Compass-and-Straightedge Approximants under Transparent Algebraic Acceleration
- **Creator:** Baker, C. Wayne
- **Resource type:** Publication / Preprint
- **Version:** v1.3
- **Manuscript dates:** Original May 24, 2026; revised October 29, 2026
- **Zenodo publication date:** Actual date of deposit, not the original manuscript date
- **Rights:** Copyright © 2026 C. Wayne Baker. All rights reserved. Use a matching custom license, and remove any default CC BY 4.0 unless its extra permissions are deliberately approved.
- **Repository:** https://github.com/CWBaker360/constructible-tower-approaching-pi
- **Programming language:** Python
- **Keywords:** constructible numbers; compass and straightedge; pi; geometric pi; polygonal approximation; Richardson extrapolation; Romberg extrapolation; geometric approximation

## Proposed description

This revised mathematical note constructs a sequence of compass-and-straightedge constructible polygonal half-perimeters and applies rational Richardson–Romberg extrapolation to approach the transcendental constant pi. Every finite tableau value remains constructible. The paper derives an explicit leading diagonal-error law, the corrected quadratic digit-growth coefficient log10(2), and refined asymptotic terms. The work separates the construction of each finite approximant from the nonconstructibility of the limiting constant; it does not claim to construct pi exactly or establish a record-speed pi computation. The original May 24, 2026 concept manuscript is preserved separately as historical provenance.

## Select for release

- `paper/constructible_tower_v1_3.pdf` (also upload separately for readers)
- `paper/constructible_tower_v1_3.tex`
- `scripts/verify_constructible_tower.py`
- `output/constructible_tower_diagonal.csv`
- `output/constructible_tower_summary.json`
- `output/constructible_tower_summary.txt`
- `REPRODUCIBILITY.md`
- `LICENSE_NOTICE.md`
- `docs/correction_note.md`
- newly generated `SHA256SUMS_RELEASE.txt` covering the exact files in the ZIP

Do not accidentally include the historical `constructible_tower_approaching_pi.*` pair as if it were v1.3. Preserve the repository's old `SHA256SUMS.txt` as historical; it has not been validated against the current checkout.

## Required checks before Zenodo publication

1. Search the published Zenodo portfolio **and authenticated drafts** for this exact title/version.
2. Run `python scripts/verify_constructible_tower.py --precision 650 --output-dir /tmp/tower_v1_3_check`. Expected: `verification_passed: True`. This uses multiprecision arithmetic for a research verification run, not binary64.
3. Compile v1.3 from `paper/constructible_tower_v1_3.tex` twice with `pdflatex`, then inspect the rebuilt PDF's page count and check extracted text against the committed v1.3 PDF. Investigate any differences.
4. Check the manuscript's revised mathematics and citations, especially the corrected digit-growth coefficient and asymptotic scope.
5. Build a versioned release ZIP from only the intended files, include a newly generated SHA-256 manifest, and verify the hashes **inside** the ZIP. Record the outer ZIP SHA-256 separately.
6. Upload ZIP and authoritative v1.3 PDF; set Public/Open; enter a consistent custom All Rights Reserved license; ensure related-work citation directions are `Cites` (not `Is cited by`).
7. Save, preview and review the Zenodo draft before publishing.
8. After publication, add Zenodo DOI to `CITATION.cff`, `README.md` and the research index as a separate GitHub metadata update.

**Claim boundary:** This is a sequence of approximate constructible quantities converging to pi, not an exact straightedge-and-compass construction of pi. Neither source-to-PDF agreement nor Zenodo publication constitutes independent peer review.
