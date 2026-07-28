# AraDetox data statement

## Dataset purpose

AraDetox supports research on Arabic text detoxification, meaning preservation, dialect-aware generation and the evaluation of generative language models across Arabic varieties.

## Languages and varieties

The dataset includes Arabic source texts and detoxified outputs in:

- Modern Standard Arabic
- Gulf Arabic
- Levantine Arabic
- Egyptian Arabic

The dialect names describe the requested output varieties. Model-generated texts may not consistently represent all communities, countries or sub-varieties within these broad categories.

## Composition

The release contains 10,500 source records. Each record includes eight generated detoxifications, four from GPT and four from Gemini. The records are divided into 8,379 training, 1,069 development and 1,052 test examples.

## Source data

The `source` field records one of ten source-dataset identifiers: `jhsc`, `T-HSAB`, `MLMA`, `Let-Mi`, `L-HSAB`, `brothers`, `S-Tweets`, `OSACT`, `aracovid` and `alsafari`.

Before publication, add complete citations, licences, collection details and redistribution conditions for all source datasets.

## Sensitive content

The source texts may include offensive, hateful, abusive or otherwise harmful language. Researchers should minimise unnecessary exposure, provide appropriate warnings and avoid presenting harmful examples without a clear research need.

## Known limitations

- The detoxified outputs are model generated and may retain harmful content.
- Rewrites may alter meaning, stance, target or pragmatic force.
- Dialect realisation may be inconsistent or stereotyped.
- Coverage should not be interpreted as representative of all Arabic-speaking communities.
- Model and prompting choices may introduce systematic biases.

## Recommended evaluation

Research using AraDetox should report results separately by variety and source where possible. Human evaluation should consider offensiveness reduction, meaning preservation, new content, fluency and dialect appropriateness.
