# Cleaning is most of the job.
#
# The sales file has four defects, and each one is the kind you meet in real
# exports: rows captured twice, blank cells, a name typed inconsistently, and a
# number stored as text. This script fixes all four and, just as importantly,
# says out loud what each fix decided.

import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
sales = pd.read_csv(DATA / "sales.csv")

print(f"Loaded {len(sales)} rows")


# ───────────────────────────────────────────── defect 1, the duplicated rows

# Seven records were captured twice. Left alone they inflate every total.
print("\nDuplicated rows:", sales.duplicated().sum())

sales = sales.drop_duplicates()
print("Rows after dropping them:", len(sales))

# drop_duplicates compares whole rows by default. To treat a row as duplicated
# when only some columns repeat, name them:
#     sales.drop_duplicates(subset=["date", "region", "product"])
# That is a business decision, not a technical one. Two genuine sales of the
# same product to the same region on the same day are not a duplicate.


# ──────────────────────────────────────────── defect 2, the inconsistent text

# The same region was typed as "North", "north", "NORTH" and " North".
print("\nRegion values before cleaning:", sales["region"].nunique())

# .str gives every string method, applied to the whole column at once.
# strip removes the surrounding spaces, title normalises the capitalisation.
sales["region"] = sales["region"].str.strip().str.title()
print("Region values after cleaning:", sales["region"].nunique())
print(sales["region"].value_counts())


# ─────────────────────────────────────────── defect 3, the number stored as text

# unit_price arrived as "$ 2,082.50". The symbol and the comma are formatting,
# and they have to come off before the text can become a number.
print("\nunit_price before:", sales["unit_price"].iloc[0], "|", sales["unit_price"].dtype)

sales["unit_price"] = (
    sales["unit_price"]
    .str.replace("$", "", regex=False)      # regex=False: treat $ as a literal
    .str.replace(",", "", regex=False)      # the thousands separator
    .str.strip()
    .astype(float)                          # only now can it become a number
)
print("unit_price after: ", sales["unit_price"].iloc[0], "|", sales["unit_price"].dtype)

# The date column deserves the same treatment. As text it sorts by luck; as a
# real date it can be compared, subtracted and grouped by month.
sales["date"] = pd.to_datetime(sales["date"])
print("date dtype after:", sales["date"].dtype)


# ────────────────────────────────────────────── defect 4, the missing values

# Eleven rows have no unit count. There are three honest responses, and picking
# one is the analyst's job, not the library's.
missing = sales["units"].isna().sum()
print(f"\nRows with no unit count: {missing}")

#   Option A  drop them. Correct when the row is unusable without that value.
#   Option B  fill them with something. Correct when you can justify the value.
#   Option C  leave them. pandas skips NaN in sum and mean, so a total stays
#             honest, and only the row count changes.
#
# Here the amount cannot be computed without the units, so the row is dropped
# and the decision is recorded in the output rather than hidden.
before = len(sales)
sales = sales.dropna(subset=["units"])
print(f"Dropped {before - len(sales)} rows with no unit count")

# With the blanks gone the column can hold whole numbers again.
sales["units"] = sales["units"].astype(int)
print("units dtype:", sales["units"].dtype)


# ──────────────────────────────────────────────── the column we actually wanted

sales["amount"] = sales["units"] * sales["unit_price"]
print("\nCleaned table:")
print(sales.head())
print("\nTotal for the year:", f"{sales['amount'].sum():,.2f}")


# ──────────────────────────────────────────────────────── saving the clean file

# Write it out so the next script starts from clean data. index=False keeps
# pandas from adding its row numbers as a first column, which is almost always
# what you want when the file is going back to a spreadsheet.
out = DATA / "sales_clean.csv"
sales.to_csv(out, index=False)
print(f"\nWrote {len(sales)} clean rows to {out.name}")


# ───────────────────────────────────── a trap worth meeting once, on purpose

# Since pandas 3.0, Copy-on-Write is always on. It changes what happens when you
# assign through two operations chained together.
#
# The demonstration runs on a copy, so the file saved above keeps its real
# channel values. copy() is how you say "I want a separate table from here on".
demo = sales.copy()
northern = (demo["region"] == "North").sum()

# This looks like it edits the table, and it does not:
demo[demo["region"] == "North"]["channel"] = "Retail"

# The first half builds a new table holding the matching rows. The assignment
# lands on that temporary table, which is discarded on the next line. Nothing is
# raised and nothing changes. It is a silent no-op, and that silence is what
# makes it dangerous.
print(f"\nAfter the chained assignment, on {northern} northern rows:")
print(demo.loc[demo["region"] == "North", "channel"].value_counts())

# Say it in one step with loc instead: rows first, column second.
demo.loc[demo["region"] == "North", "channel"] = "Retail"
print("\nAfter the same thing written with .loc:")
print(demo.loc[demo["region"] == "North", "channel"].value_counts())


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. Clean before you calculate. A sum over dirty data returns a number, and a
#    wrong number never announces itself.
# 2. .str applies any string method to a whole column, which is how inconsistent
#    data entry gets normalised in one line.
# 3. What to do with a missing value is a decision you have to make and record.
#    Dropping, filling and ignoring give three different answers.
# 4. Assign with .loc, in one step. Chained assignment silently does nothing.
