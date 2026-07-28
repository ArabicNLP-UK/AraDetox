#!/usr/bin/env python3
"""Validate the structure and cross-file alignment of the AraDetox CSV files."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
GPT_PATH = DATA / "AraDetox-GPT.csv"
GEMINI_PATH = DATA / "AraDetox-Gemini.csv"
MERGED_PATH = DATA / "merged-gpt-gemini.csv"

CORE = ["ID", "split", "source", "source_text"]
GPT_FIELDS = [
    "gpt_msa_detox",
    "gpt_gulf_detox",
    "gpt_levantine_detox",
    "gpt_egyptian_detox",
]
GEMINI_FIELDS = [
    "gemini_msa_detox",
    "gemini_gulf_detox",
    "gemini_levantine_detox",
    "gemini_egyptian_detox",
]


def load(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"Missing header: {path}")
        return reader.fieldnames, list(reader)


def validate_file(path: Path, expected_header: list[str]) -> list[dict[str, str]]:
    header, rows = load(path)
    errors: list[str] = []
    if header != expected_header:
        errors.append(f"Unexpected header: {header}")
    ids = [row.get("ID", "") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("IDs are not unique")
    empty = sum(any(value.strip() == "" for value in row.values()) for row in rows)
    if empty:
        errors.append(f"{empty} rows contain empty values")
    if errors:
        raise ValueError(f"{path.name}: " + "; ".join(errors))
    print(f"PASS {path.name}: {len(rows):,} rows")
    return rows


def main() -> int:
    try:
        gpt = validate_file(GPT_PATH, CORE + GPT_FIELDS)
        gemini = validate_file(GEMINI_PATH, CORE + GEMINI_FIELDS)
        merged = validate_file(MERGED_PATH, CORE + GPT_FIELDS + GEMINI_FIELDS)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not (len(gpt) == len(gemini) == len(merged)):
        print("ERROR: Row counts differ across files", file=sys.stderr)
        return 1

    mismatches: list[tuple[str, str]] = []
    for gpt_row, gemini_row, merged_row in zip(gpt, gemini, merged):
        record_id = merged_row["ID"]
        for field in CORE:
            if not (gpt_row[field] == gemini_row[field] == merged_row[field]):
                mismatches.append((record_id, field))
        for field in GPT_FIELDS:
            if gpt_row[field] != merged_row[field]:
                mismatches.append((record_id, field))
        for field in GEMINI_FIELDS:
            if gemini_row[field] != merged_row[field]:
                mismatches.append((record_id, field))

    print("Split distribution:", dict(Counter(row["split"] for row in gpt)))
    print("Source distribution:", dict(Counter(row["source"] for row in gpt)))

    if mismatches:
        print(f"WARNING: Found {len(mismatches)} cross-file mismatch(es):")
        for record_id, field in mismatches:
            print(f"  ID={record_id}, field={field}")
        return 2

    print("PASS Cross-file alignment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
