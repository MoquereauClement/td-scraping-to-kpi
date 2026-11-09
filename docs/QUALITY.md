# Extraction quality check

The local run processed 12 postings using qwen3:8b, think=false and the manual's 1,500-character input limit.

- Observed casing duplicate: `generative AI` / `Generative AI`. Counting normalizes casing and whitespace, and deduplicates within each posting.
- Two postings returned empty arrays. These remain in the denominator: an empty extraction does not prove the full offer contains no skills.
- Source comparison found a real omission: posting 8 mentions Python at character 3,717 (zero-based), outside the input window, but its extraction is empty. Postings 1 and 2 also mention Python after character 4,000. This truncation can undercount requirements.
- The first two postings have the same title and substantially similar descriptions. The manual's first-12 selection is retained; these are sampled records, not verified unique vacancies.
- Some outputs describe a company's technology rather than an explicit requirement. Treat the result as extracted mentions, not verified requirements.

This source comparison was performed by the coding assistant. It does not fulfill the required review by a classmate. Share the raw extraction and corresponding sources privately with a classmate, ask them to identify an error, and record their finding here without copying source text or company names.
