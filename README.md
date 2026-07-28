# AraDetox

AraDetox is an Arabic text detoxification dataset containing source texts and model-generated detoxified rewrites in Modern Standard Arabic and three regional varieties:

- Gulf Arabic
- Levantine Arabic
- Egyptian Arabic

## Creator

AraDetox was created and is maintained by **Dr Mo El-Haj**.

- 🌐 Website: https://elhaj.uk
- 💻 GitHub: https://github.com/drelhaj

## Dataset contents

The repository contains 10,500 source records divided into training, development and test splits. Each source text has four detoxified rewrites from GPT and four from Gemini.

| File | Records | Description |
|---|---:|---|
| `data/AraDetox-GPT.csv` | 10,500 | Source records and four GPT-generated detoxified rewrites |
| `data/AraDetox-Gemini.csv` | 10,500 | Source records and four Gemini-generated detoxified rewrites |
| `data/merged-gpt-gemini.csv` | 10,500 | Combined GPT and Gemini columns |

Split distribution:

| Split | Records |
|---|---:|
| Train | 8,379 |
| Development | 1,069 |
| Test | 1,052 |

The source records originate from ten datasets. The `source` column identifies the source dataset for each record.

## Column descriptions

| Column | Description |
|---|---|
| `ID` | Unique record identifier |
| `split` | Dataset split: `train`, `dev` or `test` |
| `source` | Identifier of the original source dataset |
| `source_text` | Original Arabic text |
| `gpt_msa_detox` | GPT detoxification in Modern Standard Arabic |
| `gpt_gulf_detox` | GPT detoxification in Gulf Arabic |
| `gpt_levantine_detox` | GPT detoxification in Levantine Arabic |
| `gpt_egyptian_detox` | GPT detoxification in Egyptian Arabic |
| `gemini_msa_detox` | Gemini detoxification in Modern Standard Arabic |
| `gemini_gulf_detox` | Gemini detoxification in Gulf Arabic |
| `gemini_levantine_detox` | Gemini detoxification in Levantine Arabic |
| `gemini_egyptian_detox` | Gemini detoxification in Egyptian Arabic |

## Loading the data

```python
import pandas as pd

merged = pd.read_csv("data/merged-gpt-gemini.csv")
print(merged.shape)
print(merged.columns.tolist())
```

The files are UTF-8 encoded.

## Data validation

Run the validation script from the repository root:

```bash
python scripts/validate_data.py
```

The supplied files contain complete rows, unique IDs and no empty cells. The validation performed while preparing this repository identified one value in `merged-gpt-gemini.csv` that differs from the corresponding value in `AraDetox-Gemini.csv`: record ID `794`, column `gemini_levantine_detox`. This may be an intentional correction in the merged file, but it should be checked before release. No data were altered during repository preparation.

## Responsible use

The dataset contains harmful, offensive or abusive source language because it was developed for detoxification research. Some entries may be disturbing or unsuitable for general audiences. Users should handle the data carefully, restrict unnecessary exposure and consider the social and dialectal context when interpreting labels or model outputs.

Model-generated rewrites may contain errors, dialect inconsistencies, residual harmful content or meaning changes. They should not be treated as authoritative linguistic judgements or deployed without appropriate human evaluation.

## Licence

A dataset licence has not been assigned in this repository package. Before public release, confirm that redistribution is permitted under the licences and terms of all ten source datasets, then replace `LICENSE.md` with the selected licence and document any source-specific conditions.

## Citation

Please cite the AraDetox paper when using this dataset. Update `CITATION.cff` with the final paper title, complete author list, venue, year and DOI or URL before publishing the repository.

```bibtex
@inproceedings{el-haj2026aradetox,
  title     = {AraDetox: A Multi-Dialect Arabic Detoxification Dataset},
  author    = {El-Haj, Mo},
  booktitle = {Proceedings of the ArabicNLP 2026 Conference at EMNLP 2026},
  year      = {2026},
  url       = {https://github.com/ArabicNLP-UK/AraDetox}
}
```

## Contact

For questions about the dataset, please open a GitHub issue or contact the AraDetox authors through the details provided in the accompanying paper.
- 🌐 Website: https://elhaj.uk
