# pandas gives you two objects, and everything else in the library is built on them.
#
#   Series     one column, with a label for every value
#   DataFrame  a whole table: several Series that share the same labels
#
# If you already work in a spreadsheet, the mapping is exact. A Series is a
# column. A DataFrame is the sheet. The labels are the row numbers, except they
# start at 0 and they do not have to be numbers at all.

# The convention is to import it as pd. Every tutorial and every answer online
# uses that name, so following it makes the code easier to read for everyone.
import pandas as pd


# ───────────────────────────────────────────────────────────────── a Series

# The simplest way to make one is from a list.
units = pd.Series([15, 8, 22, 5, 11])
print("A Series built from a list:")
print(units)

# Two things came back that a list does not have.
# On the left there is an index, 0 to 4, which pandas created for you.
# At the bottom there is a dtype, the type shared by every value in the column.
print("\nThe index:", list(units.index))
print("The dtype:", units.dtype)

# The index does not have to be a counter. Give it meaningful labels and the
# Series starts behaving like a named range in a spreadsheet.
monthly = pd.Series(
    [42000, 51500, 38900, 60100, 55300, 47800],
    index=["jan", "feb", "mar", "apr", "may", "jun"],
)
print("\nA Series with month labels:")
print(monthly)

# Now a value is reached by its label rather than by counting positions.
print("\nMarch:", monthly["mar"])

# The summary functions you know from a spreadsheet are methods on the Series.
print("Total:", monthly.sum())
print("Average:", round(monthly.mean(), 2))
print("Best month:", monthly.idxmax(), "with", monthly.max())

# An operation applies to the whole column at once. There is no loop and no
# dragging a formula down: this is the single biggest change in how you work.
with_tax = monthly * 1.16
print("\nEvery month with tax applied:")
print(with_tax.round(2))


# ─────────────────────────────────────────────────────────────── a DataFrame

# A DataFrame is usually built from a dictionary: one key per column.
sales = pd.DataFrame({
    "month": ["jan", "feb", "mar", "apr", "may", "jun"],
    "region": ["North", "North", "South", "South", "Centre", "Centre"],
    "amount": [42000, 51500, 38900, 60100, 55300, 47800],
    "units": [15, 18, 12, 21, 19, 16],
})
print("\nA DataFrame:")
print(sales)

# Its shape reads as (rows, columns).
print("\nShape:", sales.shape)
print("Column names:", list(sales.columns))

# Each column is a Series, and you can pull it out by name.
print("\nThe amount column on its own:")
print(sales["amount"])
print("Its type:", type(sales["amount"]))

# The dtypes tell you how pandas understood each column. Since pandas 3.0 a
# column of text reports the dedicated str dtype rather than the old object.
print("\nDtypes:")
print(sales.dtypes)


# ────────────────────────────────────────────────── a new column from the others

# Assigning to a name that does not exist yet creates the column. The right-hand
# side is computed for every row at once, which is what a filled-down formula does.
sales["price_per_unit"] = (sales["amount"] / sales["units"]).round(2)
print("\nWith a computed column:")
print(sales)


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. A Series is a column plus an index. A DataFrame is several Series that
#    share one index.
# 2. Arithmetic applies to the whole column. You stop writing loops for it.
# 3. The index starts at 0 and can hold labels instead of numbers, which is the
#    part that surprises people coming from row numbers that start at 1.
