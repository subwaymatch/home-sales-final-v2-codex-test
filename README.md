# Home sales, measured

An interactive report about 35,442 home sales across 18 college-town cities and 11 campus areas. It answers ten questions about sale prices, time on market, property taxes, and distance to campus, with charts, an interactive dashboard, and two data-quality insights.

Use the dashboard to filter by campus area, city, year, bedrooms, price, living area, and home features. Compare cities or campuses, select cities on the map, and share filter settings through the page URL. Q1–Q6 always use the full dataset and the rules stated with each question.

## Live site

[Open Home sales, measured](https://subwaymatch.github.io/home-sales-final-v2-codex-test/)

## How this site was built

This site was built with ChatGPT Codex in the cloud (model: GPT-6 Luna) over seven rounds of prompts and pull requests. P2 on the site describes the experience.

## Data and methods

The report reads [`data/college_town_home_sales.csv`](data/college_town_home_sales.csv). The dataset is the College-town home sales dataset, version 1.0 (2026), from the University of Illinois-Deloitte Foundation Center for Business Emerging Technologies; data was collected in March 2026. See the [data description sheet](docs/data_description_sheet.md) for the source details and cautions.

The $10,000–$5,000,000 sale-price range is a scope rule: it removes clear errors such as a $0 sale, along with a small number of very high sales, some of which are real luxury homes. Q2 uses all rows; Q3 compares all rows with rows in this price scope. Q6's aggregate tax burden sums eligible annual taxes and sale prices by campus area, using in-scope sales with positive annual tax below 10% of sale price. Each row is a sale keyed by `listing_id`, never the street address. Days on market is `contract_date - list_date` and requires both dates. Year and month come from `sale_date`. Campus areas use the `university` column; cities combine city and state. The report uses medians except where a question requests the mean. The dashboard's filters do not change the fixed answers in Q1–Q6.

## Check the numbers

With Python and pandas available, run these independent checks from the repository root:

- `python3 scripts/verify_report.py` recalculates Q1–Q6.
- `python3 scripts/analyze_days_on_market_missingness.py` recalculates the P1 city-level missing-date shares and compares the correct median with the zero-filled counterfactual.

Interactive Q7–Q10 answers are calculated in the page from the CSV and update when their controls change.
