# Home sales, measured

An interactive, report-style exploration of 35,442 completed home sales across 18 college-town cities and 11 campus areas. The page answers ten questions about prices, sale timing, property taxes and distance to campus.

## Live site

https://subwaymatch.github.io/home-sales-final-v2-codex-test/

GitHub Pages publishes the repository root through `.github/workflows/pages.yml` when `main` is pushed. Pages must be enabled with the GitHub Actions source in repository settings.

## Data notes

The report reads `data/college_town_home_sales.csv` in the browser. Prices are valid from $10,000 through $5,000,000 inclusive, except Q2 and Q3, which explicitly analyze all rows for their unrestricted comparisons. Every row remains a separate sale keyed by `listing_id`; street addresses are not unique. Days on market is `contract_date - list_date`, and rows missing either date are excluded from those calculations. Year and month come from `sale_date`, so Q9 includes all prices but requires a sale date. Campus-area groupings use `university`; city groupings combine `city` and `state`. Medians are used except where a question requests the mean. Dollar values are rounded to whole dollars and days, distances, and percentages to one decimal.

Missing dates are not zero days, and the listings with missing dates are not a random subset: the days-on-market results describe sales with both dates. The source contains implausible prices, so filtered analyses apply the stated validity range. Annual-tax ratios include only valid-price rows with a positive tax smaller than the sale price. Campus distance is straight-line distance, not driving distance.

## Tools

Plain HTML, CSS and JavaScript, with Papa Parse loaded from jsDelivr for CSV parsing. `scripts/verify_report.py` independently computes Q1–Q6 with pandas.

## Citation

College-town home sales dataset, version 1.0 (2026). University of Illinois-Deloitte Foundation Center for Business Emerging Technologies. Data collected March 2026.
