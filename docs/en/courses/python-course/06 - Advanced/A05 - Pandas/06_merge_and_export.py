# Joining two tables, and getting the result back out.
#
# merge is VLOOKUP, with two differences that matter. It brings across every
# column at once instead of one per formula, and it tells you what did not match
# instead of leaving #N/A scattered through the sheet.

import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

sales = pd.read_csv(DATA / "sales_clean.csv", parse_dates=["date"])
regions = pd.read_csv(DATA / "regions.csv")

print("Sales:", sales.shape, "| Regions:", regions.shape)
print("\nThe lookup table:")
print(regions)


# ───────────────────────────────────────────────────────────── the basic join

# on names the column both tables share. Every matching row of regions is
# attached to the sales row, bringing all of its columns with it.
joined = sales.merge(regions, on="region", how="left")
print("\nAfter the join:", joined.shape)
print(joined.head(3))

# how="left" keeps every sales row, whether or not the lookup found a match.
# That is the VLOOKUP behaviour, and it is the safe default: you never silently
# lose a sale because a region was missing from the catalogue.


# ───────────────────────────────────────────────────── what did not match

# The lookup table has five regions and the sales file only covers four. A left
# join keeps the four and quietly ignores East, which is usually what you want.
print("\nRegions in the lookup:", sorted(regions["region"]))
print("Regions with sales:   ", sorted(sales["region"].unique()))

# how="outer" keeps everything from both sides, and the indicator column tells
# you where each row came from. This is how you audit a join instead of trusting it.
audit = sales.merge(regions, on="region", how="outer", indicator=True)
print("\nWhere each row came from:")
print(audit["_merge"].value_counts())

# right_only means a lookup entry that no sale ever referenced.
orphans = audit[audit["_merge"] == "right_only"]["region"].unique()
print("Regions in the catalogue with no sales:", list(orphans))

# Run the check the other way too. A sale whose region is missing from the
# catalogue would show up as left_only, and that is a data problem to report,
# not to paper over.


# ────────────────────────────────────────────── using the joined information

# Now that every row knows its target, the comparison is a normal column.
monthly = (
    joined.assign(month=joined["date"].dt.month)
    .groupby(["region", "manager", "monthly_target", "month"])["amount"]
    .sum()
    .reset_index()
)
monthly["hit_target"] = monthly["amount"] >= monthly["monthly_target"]
monthly["attainment"] = (monthly["amount"] / monthly["monthly_target"]).round(3)

print("\nMonthly attainment, first rows:")
print(monthly.head())

# How often did each region make its number?
scoreboard = (
    monthly.groupby(["region", "manager"])
    .agg(months=("hit_target", "count"),
         months_on_target=("hit_target", "sum"),
         mean_attainment=("attainment", "mean"))
    .round(3)
    .sort_values("mean_attainment", ascending=False)
)
print("\nScoreboard:")
print(scoreboard)


# ─────────────────────────────────────────── joining on differently named keys

# When the key is called something else in each table, name both sides. Here it
# is the same name, so the example renames one on the way in to show the shape.
codes = regions.rename(columns={"region": "region_code"})
example = sales.merge(codes, left_on="region", right_on="region_code", how="left")
print("\nJoined on differently named keys:", example.shape)


# ──────────────────────────────────────────────────────────────── exporting

OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

# Back to CSV, which anything can open.
scoreboard.to_csv(OUT / "scoreboard.csv")
print(f"\nWrote {(OUT / 'scoreboard.csv').name}")

# Back to Excel, which is where this usually has to end up. Writing several
# sheets at once needs an ExcelWriter, and it needs the openpyxl package
# installed. If it is missing, pandas raises ImportError naming it.
try:
    with pd.ExcelWriter(OUT / "report.xlsx") as writer:
        scoreboard.to_excel(writer, sheet_name="Scoreboard")
        monthly.to_excel(writer, sheet_name="Monthly", index=False)
        regions.to_excel(writer, sheet_name="Regions", index=False)
    print("Wrote report.xlsx with three sheets")
except ImportError:
    print("Skipped report.xlsx: install openpyxl to write Excel files")


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. merge is VLOOKUP that brings every column at once.
# 2. how="left" keeps all your rows. It is the safe default.
# 3. indicator=True turns a join into something you can audit. Check both
#    directions before trusting the result.
# 4. The analysis ends where it started, as a file somebody else can open.
