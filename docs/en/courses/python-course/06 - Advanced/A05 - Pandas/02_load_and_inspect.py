# Loading a file and looking at it before doing anything else.
#
# The temptation is to jump straight to the answer. Resist it for two minutes.
# Almost every wrong result later in the term traces back to a column that was
# not the type you assumed, or rows that were not there.

import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# read_csv does in one line what the whole of A04 did by hand: it opens the
# file, reads the header, and builds a DataFrame out of the rows.
sales = pd.read_csv(DATA / "sales.csv")


# ──────────────────────────────────────────────────────────── the first look

# head shows the first rows. Pass a number to change how many.
print("First five rows:")
print(sales.head())

# tail shows the last ones, which is where a stray total row usually hides.
print("\nLast three rows:")
print(sales.tail(3))

# shape answers "how much data do I actually have".
rows, columns = sales.shape
print(f"\n{rows} rows and {columns} columns")


# ───────────────────────────────────────────────────────────────── the types

# info is the single most useful command in this file. It reports, per column,
# how many values are not missing and what type pandas inferred.
print("\ninfo():")
sales.info()

# Read that output carefully against the file. Three things are worth naming.
#
#   units       came in as float64, not as a whole number. pandas read the
#               digits fine, but eleven cells are blank, and a blank has to be
#               represented somehow. That marker is NaN, which only exists in a
#               float column, so the whole column became float. This is why the
#               unit counts print as 15.0 instead of 15.
#   unit_price  came in as text, because "$ 2,082.50" is not a number to Python.
#               A currency symbol and a thousands comma are formatting, and
#               formatting is not part of the value.
#   date        came in as text, because a CSV has no date type. Until it is
#               converted, sorting it works by luck: it only happens to be
#               correct because the format puts the year first.
#
# None of this is a pandas failure. It is the CSV having no types, exactly as
# the previous module showed. The next script fixes all three.


# ─────────────────────────────────────────────────────── the numeric summary

# describe gives count, mean, standard deviation, minimum, maximum and the
# quartiles for every numeric column. Only units qualifies so far, and its count
# of 313 against 324 rows is the missing data showing up again.
print("\ndescribe() on the raw file:")
print(sales.describe())

# For text columns, ask for the counts of each distinct value instead. This is
# how you catch the dirt: the region column should hold four values.
print("\nHow many distinct regions does the file think there are?")
print(sales["region"].value_counts())

# Four regions were captured, but this reports more, because the same name was
# typed with different capitalisation and stray spaces.
print("\nDistinct region strings:", sales["region"].nunique())


# ────────────────────────────────────────────────────────── missing and dupes

# isna marks every missing cell as True, and sum counts them per column.
print("\nMissing values per column:")
print(sales.isna().sum())

# duplicated marks a row as True when an identical row appeared earlier.
print("\nFully duplicated rows:", sales.duplicated().sum())


# ────────────────────────────────────────────────────────── a second table

# The regions file is the lookup table of this course: one row per region, with
# the details that do not belong in every sales record.
regions = pd.read_csv(DATA / "regions.csv")
print("\nThe lookup table:")
print(regions)

# It has five rows and the sales file only covers four regions. That difference
# is deliberate, and script 06 shows what a join does with it.


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. head, info, shape and describe, in that order, before any analysis.
# 2. info tells you the truth about types. A column of numbers read as text is
#    the most common reason a total comes back wrong.
# 3. value_counts on a text column is how you find inconsistent data entry
#    before it splits your groups in two.
