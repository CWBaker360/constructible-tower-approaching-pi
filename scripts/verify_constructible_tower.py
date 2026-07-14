#!/usr/bin/env python3
"""Verify the constructible Richardson tower approaching pi."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import mpmath as mp


LEVELS = (5, 10, 15, 20, 25, 30)


def polygon_value(level: int) -> mp.mpf:
    n = 4 * (2**level)
    return mp.mpf(n) * mp.sin(mp.pi / n)


def build_tableau(max_level: int) -> list[list[mp.mpf]]:
    table: list[list[mp.mpf]] = []
    for i in range(max_level + 1):
        row = [polygon_value(i)]
        for j in range(1, i + 1):
            current = row[j - 1]
            previous = table[i - 1][j - 1]
            row.append(current + (current - previous) / (mp.mpf(4) ** j - 1))
        table.append(row)
    return table


def leading_error(level: int) -> mp.mpf:
    i = level
    return (
        mp.pi ** (2 * i + 3)
        / mp.factorial(2 * i + 3)
        * mp.mpf(4) ** (-(i + 1) * (i + 4) / 2)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=650)
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    args = parser.parse_args()

    if args.precision < 620:
        raise ValueError("Use at least 620 decimal digits for the level-30 audit.")

    mp.mp.dps = args.precision
    table = build_tableau(max(LEVELS))
    rows = []

    for i in LEVELS:
        n = 4 * (2**i)
        diagonal = table[i][i]
        error = abs(diagonal - mp.pi)
        digits = -mp.log10(error)
        leading = leading_error(i)
        rows.append(
            {
                "level_i": i,
                "N": n,
                "diagonal": mp.nstr(diagonal, 80),
                "absolute_error": mp.nstr(error, 40),
                "correct_digits": mp.nstr(digits, 20),
                "digits_over_i_squared": mp.nstr(digits / (i * i), 20),
                "leading_error_model": mp.nstr(leading, 40),
                "error_over_leading_model": mp.nstr(error / leading, 20),
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = args.output_dir / "constructible_tower_diagonal.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    expected_digits = {
        5: mp.mpf("19.59"),
        10: mp.mpf("57.34"),
        15: mp.mpf("112.05"),
        20: mp.mpf("183.12"),
        25: mp.mpf("270.26"),
        30: mp.mpf("373.26"),
    }

    table_values_passed = all(
        abs(mp.mpf(row["correct_digits"]) - expected_digits[int(row["level_i"])])
        < mp.mpf("0.01")
        for row in rows
    )

    model_ratios = [mp.mpf(row["error_over_leading_model"]) for row in rows]
    leading_model_passed = (
        abs(model_ratios[-1] - 1) < mp.mpf("3e-4")
        and abs(model_ratios[-1] - 1) < abs(model_ratios[-2] - 1)
    )

    ratios = [mp.mpf(row["digits_over_i_squared"]) for row in rows]
    ratio_monotone = all(a > b for a, b in zip(ratios, ratios[1:]))
    corrected_limit_consistent = ratios[-1] > mp.log10(2)
    old_limit_rejected = ratios[-1] < 2 * mp.log10(2)

    overall = bool(
        table_values_passed
        and leading_model_passed
        and ratio_monotone
        and corrected_limit_consistent
        and old_limit_rejected
    )

    summary = {
        "precision_dps": args.precision,
        "levels": list(LEVELS),
        "table_values_passed": bool(table_values_passed),
        "leading_error_model_passed": bool(leading_model_passed),
        "digit_ratio_monotone_decreasing": bool(ratio_monotone),
        "correct_asymptotic_limit": mp.nstr(mp.log10(2), 20),
        "previous_factor_two_limit_rejected": bool(old_limit_rejected),
        "verification_passed": overall,
    }

    (args.output_dir / "constructible_tower_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output_dir / "constructible_tower_summary.txt").write_text(
        "\n".join(f"{key}: {value}" for key, value in summary.items()) + "\n",
        encoding="utf-8",
    )

    print("\n".join(f"{key}: {value}" for key, value in summary.items()))
    if not overall:
        raise SystemExit("Verification failed.")


if __name__ == "__main__":
    main()
