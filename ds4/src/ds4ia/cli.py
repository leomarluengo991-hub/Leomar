"""Command-line entry point for the DS4 IA demo."""

from __future__ import annotations

import argparse

from .data import load_sample_data, summarize_data
from .model import predict_labels


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DS4 IA starter project")
    parser.add_argument("--demo", action="store_true", help="run a quick demo")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.demo:
        rows = load_sample_data()
        summary = summarize_data(rows)
        predictions = predict_labels(rows)
        print("Sample dataset summary:")
        for key, value in summary.items():
            print(f"  {key}: {value}")
        print("Predictions:")
        for row, prediction in zip(rows, predictions):
            print(f"  {row} -> {prediction}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
