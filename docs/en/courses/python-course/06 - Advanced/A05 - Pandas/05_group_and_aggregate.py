# The PivotTable, in code.
#
# groupby does exactly what dragging a field into a PivotTable does: it splits
# the rows into buckets that share a value, applies a summary to each bucket,
# and puts the results back together as a table.
#
# The whole of summarise_by_hand.py, the eighty-line script in module A04, is
# the first eight lines of this file.

import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# Start from the file 04_clean.py wrote. parse_dates tells read_csv that this
# column holds dates, so it comes back ready to work with.
sales = pd.read_csv(DATA / "sales_clean.csv", parse_dates=["date"])
print(f"Loaded {len(sales)} clean rows")


# ────────────────────────────────────────────────────────── one grouping field

# Split by region, then total the amount of each group.
by_region = sales.groupby("region")["amount"].sum()
print("\nSales by region:")
print(by_region.sort_values(ascending=False).round(2))

# The result is a Series whose index is the thing you grouped by, so the usual
# Series tools still apply.
print("\nBest region:", by_region.idxmax())
print("Its share of the year:", f"{by_region.max() / sales['amount'].sum():.1%}")


# ────────────────────────────────────────────────── several summaries at once

# agg takes a list of functions and gives a column for each. This answers "how
# much, how many times and how big on average" in one pass.
summary = sales.groupby("region")["amount"].agg(["sum", "count", "mean"]).round(2)
print("\nAmount summarised three ways:")
print(summary.sort_values("sum", ascending=False))

# Different summaries for different columns, with names you choose. The pattern
# is new_name=("source column", "function").
detailed = sales.groupby("region").agg(
    revenue=("amount", "sum"),
    units_sold=("units", "sum"),
    sales_made=("amount", "count"),
    average_sale=("amount", "mean"),
).round(2)
print("\nA named summary:")
print(detailed.sort_values("revenue", ascending=False))


# ───────────────────────────────────────────────────────── two grouping fields

# Pass a list and the groups become every combination of the two.
by_region_channel = sales.groupby(["region", "channel"])["amount"].sum().round(2)
print("\nSales by region and channel:")
print(by_region_channel)

# That reads as a long list. pivot_table lays the same numbers out as a grid,
# which is the shape a PivotTable gives you on screen.
grid = sales.pivot_table(
    index="region",       # what goes down the side
    columns="channel",    # what goes across the top
    values="amount",      # what fills the cells
    aggfunc="sum",        # how the cells are summarised
).round(2)
print("\nThe same numbers as a grid:")
print(grid)

# margins adds the row and column totals, the way a PivotTable's grand total does.
grid_with_totals = sales.pivot_table(
    index="region", columns="channel", values="amount",
    aggfunc="sum", margins=True, margins_name="Total",
).round(2)
print("\nWith totals:")
print(grid_with_totals)


# ──────────────────────────────────────────────────────── grouping over time

# A date column can be grouped by any part of itself. .dt reaches into the date
# the same way .str reaches into text.
sales["month"] = sales["date"].dt.month
monthly = sales.groupby("month")["amount"].sum().round(2)
print("\nSales by month:")
print(monthly)

print("\nBest month:", monthly.idxmax(), "| worst month:", monthly.idxmin())

# Quarter, year and day of week work the same way.
by_quarter = sales.groupby(sales["date"].dt.quarter)["amount"].sum().round(2)
print("\nSales by quarter:")
print(by_quarter)


# ──────────────────────────────────────────────────────── the top of a group

# A common question: which product sells most in each region. Group by both,
# total, then take the largest of each region.
product_region = sales.groupby(["region", "product"])["amount"].sum()
best_per_region = product_region.loc[product_region.groupby("region").idxmax()]
print("\nBest-selling product per region:")
print(best_per_region.round(2))


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. groupby is the PivotTable. Split, summarise, put back together.
# 2. agg with named arguments is how you build a report table in one statement.
# 3. pivot_table is groupby laid out as a grid, and margins gives you the totals.
# 4. .dt on a date column is what makes "by month" and "by quarter" one line.
