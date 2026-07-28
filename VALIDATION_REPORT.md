# Validation report

Validation date: 28 July 2026

## Structural checks

- All three files are readable as UTF-8 CSV.
- Each file contains 10,500 data rows.
- Each row contains the expected number of columns.
- No empty cell was detected.
- All 10,500 IDs are unique.
- GPT and Gemini files have identical `ID`, `split`, `source` and `source_text` fields.
- No duplicate `source_text` values were detected.

## Split counts

- `train`: 8,379
- `dev`: 1,069
- `test`: 1,052