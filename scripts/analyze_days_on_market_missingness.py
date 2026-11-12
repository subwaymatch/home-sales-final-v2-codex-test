#!/usr/bin/env python3
"""Independent P1 check: city-level list-date missingness and zero-filled DOM."""
from pathlib import Path
import argparse
import json

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--json", action="store_true", help="print machine-readable city results")
args = parser.parse_args()
df = pd.read_csv(
    ROOT / "data/college_town_home_sales.csv",
    dtype={"zipcode": "string", "county_fips": "string", "parcel_number": "string"},
)
df["city_state"] = df["city"] + ", " + df["state"]
listed = pd.to_datetime(df["list_date"], errors="coerce")
contract = pd.to_datetime(df["contract_date"], errors="coerce")
df["days_on_market"] = (contract - listed).dt.days
df["zero_filled_days"] = df["days_on_market"].fillna(0)

rows = []
for city, sales in df.groupby("city_state", sort=True):
    no_list = sales["list_date"].isna() | sales["list_date"].eq("")
    correct = sales["days_on_market"].median()
    wrong = sales["zero_filled_days"].median()
    rows.append(
        {
            "city": city,
            "sales": len(sales),
            "no_list_date_sales": int(no_list.sum()),
            "no_list_date_share_pct": no_list.mean() * 100,
            "complete_date_sales": int(sales["days_on_market"].notna().sum()),
            "correct_median_days": correct,
            "zero_filled_median_days": wrong,
            "change_days": wrong - correct,
        }
    )

result = pd.DataFrame(rows)
if args.json:
    print(json.dumps(rows))
    raise SystemExit(0)

print(f"Total sales: {len(df):,}")
print(f"Sales with both dates: {df['days_on_market'].notna().sum():,}")
print("All rows included; no price filter. Missing either required date is zero-filled only in the counterfactual.")
print(
    result.to_string(
        index=False,
        formatters={
            "no_list_date_share_pct": lambda n: f"{n:.1f}%",
            "correct_median_days": lambda n: f"{n:.1f}",
            "zero_filled_median_days": lambda n: f"{n:.1f}",
            "change_days": lambda n: f"{n:+.1f}",
        },
    )
)
