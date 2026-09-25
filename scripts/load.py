"""Load customers and orders, join them, report revenue per region.

Run from the project folder:  uv run python scripts/load.py

The code is mostly reasonable. Inspect the INPUT FILES before blaming it.
"""

from pathlib import Path

import pandas as pd

CUSTOMERS = Path("data/raw/customers.csv")
ORDERS = Path("data/raw/orders.csv")
OUT = Path("output/revenue_by_region.csv")


def load_customers() -> pd.DataFrame:
    df = pd.read_csv(CUSTOMERS)
    assert df.shape[1] == 4, f"expected 4 customer columns, got {df.shape[1]}: {list(df.columns)}"
    return df


def load_orders() -> pd.DataFrame:
    df = pd.read_csv(ORDERS)
    expected = ["order_id", "customer_id", "order_date", "amount", "status"]
    assert list(df.columns) == expected, f"unexpected columns: {list(df.columns)}"
    assert df["amount"].dtype.kind == "f", f"amount should be numeric, got {df['amount'].dtype}"
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df


def main() -> None:
    customers = load_customers()
    orders = load_orders()
    paid = orders[orders["status"] == "paid"]
    merged = paid.merge(customers, on="customer_id", how="left")
    by_region = merged.groupby("region")["amount"].sum().round(2)
    OUT.parent.mkdir(exist_ok=True)
    by_region.to_csv(OUT)
    print(by_region)
    print(f"rows: {len(merged)}  missing amounts: {int(merged['amount'].isna().sum())}")


if __name__ == "__main__":
    main()
