# Correction to the Original Concept PDF

The original concept PDF stated

\[
\frac{D(i)}{i^2}\to2\log_{10}2.
\]

The interpolation nodes are

\[
x_r=(4\cdot2^r)^{-2}=4^{-(r+2)},
\]

so

\[
\prod_{r=0}^{i}x_r
=
4^{-(i+1)(i+4)/2}.
\]

This contributes

\[
\log_{10}2\,i^2+O(i)
\]

to the correct-digit count, not \(2\log_{10}2\,i^2\). The factorial in the
first omitted sine coefficient contributes

\[
2i\log_{10}i+O(i).
\]

Hence

\[
D(i)
=
(\log_{10}2)i^2
+
2i\log_{10}i
+
O(i),
\qquad
D(i)/i^2\to\log_{10}2.
\]

The original table is consistent with the corrected limit: its ratio decreases
from \(0.78355\) to \(0.41474\), remaining above
\(\log_{10}2\approx0.30103\).
