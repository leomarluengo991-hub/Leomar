"""Sample data helpers for the DS4 IA starter project."""

from __future__ import annotations

from typing import Iterable


def load_sample_data() -> list[dict[str, float | str]]:
    """Return a small toy dataset for quick AI/data-science demos."""
    return [
        {"feature_a": 1.0, "feature_b": 2.0, "label": "A"},
        {"feature_a": 2.0, "feature_b": 3.0, "label": "A"},
        {"feature_a": 4.0, "feature_b": 1.0, "label": "B"},
        {"feature_a": 5.0, "feature_b": 2.0, "label": "B"},
    ]


def summarize_data(rows: Iterable[dict[str, float | str]]) -> dict[str, float]:
    """Compute a few simple summary statistics."""
    rows = list(rows)
    if not rows:
        return {"count": 0.0, "mean_a": 0.0, "mean_b": 0.0}

    feature_a = [float(row["feature_a"]) for row in rows]
    feature_b = [float(row["feature_b"]) for row in rows]
    return {
        "count": float(len(rows)),
        "mean_a": sum(feature_a) / len(feature_a),
        "mean_b": sum(feature_b) / len(feature_b),
    }
