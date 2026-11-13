#!/usr/bin/env python3
"""Independent CSV/pandas calculation of the report's fixed Q1–Q6 results."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data/college_town_home_sales.csv", dtype={"zipcode": "string", "county_fips": "string", "parcel_number": "string"})
df["city_state"] = df["city"] + ", " + df["state"]
df["sale_price"] = pd.to_numeric(df["sale_price"])
valid = df[df.sale_price.between(10_000, 5_000_000, inclusive="both")].copy()

def records(frame, group, fn):
    return frame.groupby(group, dropna=False).apply(fn, include_groups=False)

q1 = valid.groupby("city_state").sale_price.agg(median="median", sales="count").sort_values("median", ascending=False)
all_city = df.groupby("city_state").sale_price.agg(mean="mean", median="median", sales="count")
all_city["mean_above_median_pct"] = (all_city["mean"] / all_city["median"] - 1) * 100
q2 = all_city.sort_values("mean_above_median_pct", ascending=False)
all_rank = df.groupby("city_state").sale_price.mean().rank(method="min", ascending=False).astype(int)
valid_rank = valid.groupby("city_state").sale_price.mean().rank(method="min", ascending=False).astype(int)
q3 = pd.DataFrame({"all_rows_rank": all_rank, "scope_rule_rank": valid_rank})
q3["rank_change"] = q3.scope_rule_rank - q3.all_rows_rank

valid["sale_year"] = pd.to_datetime(valid.sale_date, errors="coerce").dt.year
by_year = valid[valid.sale_year.isin([2024, 2025])].groupby(["university", "sale_year"]).sale_price.median().unstack()
q4 = by_year.dropna(subset=[2024, 2025]).rename(columns={2024: "median_2024", 2025: "median_2025"})
q4["change_pct"] = (q4.median_2025 / q4.median_2024 - 1) * 100

df["days_on_market"] = (pd.to_datetime(df.contract_date, errors="coerce") - pd.to_datetime(df.list_date, errors="coerce")).dt.days
q5 = df.dropna(subset=["days_on_market"]).groupby("university").days_on_market.agg(median="median", sales="count").sort_values("median", ascending=False)
tax_amount = pd.to_numeric(valid.tax_annual_amount, errors="coerce")
tax = valid[(tax_amount > 0) & (tax_amount < 0.10 * valid.sale_price)].copy()
tax["tax_amount"] = pd.to_numeric(tax.tax_annual_amount)
q6 = tax.groupby("university").agg(
    eligible_tax_total=("tax_amount", "sum"),
    eligible_sale_price_total=("sale_price", "sum"),
    eligible_sales=("sale_price", "count"),
)
q6["aggregate_tax_to_price_pct"] = q6.eligible_tax_total / q6.eligible_sale_price_total * 100
q6 = q6.sort_values("aggregate_tax_to_price_pct", ascending=False)

print("Q1 median price by city (sale-price scope):\n", q1.to_string())
print("\nQ2 mean, median, mean premium (all rows):\n", q2.to_string())
print("\nQ3 rank all rows vs scope-rule sales:\n", q3.to_string())
print("\nQ4 campus median prices and change (sale-price scope):\n", q4.to_string())
print("\nQ5 median days on market:\n", q5.to_string())
print("\nQ6 aggregate eligible tax / sale-price ratio (%):\n", q6.to_string())
