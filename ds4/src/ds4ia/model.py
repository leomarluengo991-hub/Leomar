"""Simple classification example for DS4 IA."""

from __future__ import annotations

from typing import Iterable


def classify_point(feature_a: float, feature_b: float) -> str:
    """A tiny rule-based classifier for demonstration purposes."""
    if feature_a >= 3.0 and feature_b <= 2.5:
        return "B"
    return "A"


def predict_labels(rows: Iterable[dict[str, float | str]]) -> list[str]:
    """Predict labels for a list of records."""
    return [
        classify_point(float(row["feature_a"]), float(row["feature_b"]))
        for row in rows
    ]
