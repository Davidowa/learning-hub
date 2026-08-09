"""notebooks/analisis-de-datos/en/w17.ipynb

Source deck: ppts/python/analisis-de-datos/en/w17.en.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

en = [

md("""
# Data Analysis · Week 17
## Revision and final exam

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

This notebook does not re-explain topics. It walks the term's map, runs the six errors that cost
the most marks, and leaves you an integrating exercise so you can measure where you stand.

By the end you will be able to:

1. Place every topic on the map and say what it depends on.
2. Recognise the six expensive errors from the symptom alone.
3. Solve an integrating exercise from file to finding.
4. Reach the exam knowing what is covered and what is allowed.

### The final exam

| Aspect | Detail |
|---|---|
| Content | All eight units, weighted towards files, pandas and visualisation |
| Weight | 20 % of the final grade |
| Format | On the classroom computer, uploaded zipped to Blackboard |
| You may bring | Notes, assignments, books and anything you generated with AI beforehand |
| You may not | Phone, headphones, AI glasses or messaging |
"""),

md("""
---
## Setup
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

bootstrap_cell("en"),

md("""
---
# Block 1 · The term on a map

Nothing we covered stands alone. Every topic is the piece that makes the next one possible.

| Topic | Rests on | Enables |
|---|---|---|
| Types and operators | The algorithm on paper | Any correct calculation |
| Selection | Boolean comparisons | Business rules |
| Repetition | Selection | Walking a whole table |
| Functions | Repetition | Code that can be tested |
| Collections | Functions | Lists, and `groupby`'s dictionary |
| Files and pandas | Collections | Analysis on real data |

## The chain running through the whole course

A list is a column. A column with an index is a `Series`. Several paired `Series` are a
`DataFrame`. A dictionary is a `VLOOKUP`, and grouping by key is what a PivotTable does.

Each of those sentences is the same idea with more tooling on top. Here it is, in four cells.
"""),

code("""
# Week 12: a list is a column, with positions.
payments = [9038.10, 6344.53, 7220.66]
print("List:", payments, "· the first:", payments[0])
"""),

code("""
# Week 15.1: a Series is that column with labels on top.
series = pd.Series(payments, index=["A", "B", "C"])
print(series)
print("The first, by label:", series["A"])
"""),

code("""
# Week 15.1: a DataFrame is several paired Series.
table = pd.DataFrame({"loan": ["A", "B", "C"], "payment": payments,
                      "region": ["North", "South", "North"]})
print(table)
"""),

code("""
# Week 9 with a dictionary, and week 15.3 with groupby. The same result.
accumulated = {}
for region, payment in zip(table["region"], table["payment"]):
    accumulated[region] = accumulated.get(region, 0) + payment

print("With a dictionary:", {k: round(v, 2) for k, v in accumulated.items()})
print("With groupby:     ", table.groupby("region")["payment"].sum().round(2).to_dict())
"""),

md("""
The same two numbers. The syntax changes and the idea does not, which is why **pandas does not have
to be memorised separately**: if you know what a loop with an accumulator does, you know what a
`groupby` does.
"""),

md("""
---
# Block 2 · What costs the most

Six errors. Not the hardest ones, the ones that turned up in every submission of the term.

All six run below. Look at them once more before the exam: what has to be recognised is the
**symptom**, not the cause.

## 1 · Counting from one
"""),

code("""
months = ["jan", "feb", "mar", "apr", "may"]

try:
    print(months[5])
except IndexError as e:
    print("Symptom -> IndexError:", e)

print("The last is months[4]:", months[4], "· or months[-1]:", months[-1])
"""),

md("""
## 2 · Calculating without converting
"""),

code("""
a, b = "5074", "320"

print("Symptom -> an absurd total and no error:", a + b)
print("Correct:", int(a) + int(b))
"""),

md("""
This is the only one of the six that **raises nothing**. Which is why it is the most expensive: the
number reaches the report.

## 3 · Confusing modifying with returning
"""),

code("""
sales_list = [300, 100, 200]
result = sales_list.sort()

print("Symptom -> None where you expected a list:", result)
print("The list did get sorted:", sales_list)
print("Correct, with sorted:", sorted([300, 100, 200]))
"""),

md("""
## 4 · Declaring the accumulator inside
"""),

code("""
numbers = [100, 200, 300]

for n in numbers:
    wrong_total = 0
    wrong_total += n

right_total = 0
for n in numbers:
    right_total += n

print("Symptom -> the total is the last value:", wrong_total)
print("Correct:", right_total)
"""),

md("""
## 5 · Chained assignment
"""),

code("""
import warnings

df = pd.DataFrame({"region": ["North", "South", "North"], "channel": ["Retail"] * 3})
before = (df["channel"] == "Online").sum()

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    df[df["region"] == "North"]["channel"] = "Online"
    print("Warning:", [type(w.message).__name__ for w in caught] or "none")

print("Symptom -> nothing changed:", (df["channel"] == "Online").sum(), "from", before)

df.loc[df["region"] == "North", "channel"] = "Online"
print("With loc, in one step:", (df["channel"] == "Online").sum())
"""),

md("""
## 6 · Grouping before cleaning
"""),

code("""
raw = pd.read_csv("sales.csv")

print("Symptom -> more groups than exist:", raw["region"].nunique(), "regions")
print(sorted(raw["region"].unique()))

clean = raw.copy()
clean["region"] = clean["region"].str.strip().str.title()
print()
print("After normalising:", clean["region"].nunique(), "regions")
"""),

md("""
### All six, in one table

| Error | The symptom that gives it away |
|---|---|
| Counting from one | `IndexError: list index out of range` |
| Calculating without converting | An absurd total, and **no error** |
| Modifying against returning | `None` where you expected data, or `TypeError: NoneType` |
| Accumulator inside | The total is the last record |
| Chained assignment | A warning, and nothing changed in the table |
| Grouping without cleaning | More groups than the company has |

The two in the middle are the dangerous ones, because the program runs.
"""),

md("""
---
# Block 3 · From file to finding

The integrating exercise. The order matters: **inspect, clean, group, conclude.** Skipping the first
is how you reach a wrong number.

Run the cells and follow the thread.

## Inspect
"""),

code("""
sales = pd.read_csv("sales.csv")

print(sales.shape)
sales.info()
"""),

code("""
print("Missing:", sales.isna().sum().sum())
print("Duplicates:", sales.duplicated().sum())
print("Regions the file thinks exist:", sales["region"].nunique())
"""),

md("""
Three problems before computing anything: eleven holes, seven duplicates and eight regions.

## Clean
"""),

code("""
sales = sales.drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .str.strip().astype(float))
sales["date"] = pd.to_datetime(sales["date"])
sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)
sales["amount"] = sales["units"] * sales["unit_price"]

print(f"{len(sales)} clean rows · {sales['region'].nunique()} regions "
      f"· total {sales['amount'].sum():,.2f}")
"""),

md("""
## Group
"""),

code("""
grid = sales.pivot_table(index="region", columns="channel", values="amount",
                         aggfunc="sum", margins=True, margins_name="Total")

print((grid / 1000).round(0))
"""),

code("""
detail = sales.groupby(["region", "channel"]).agg(
    revenue=("amount", "sum"),
    sales_made=("amount", "count"),
    ticket=("amount", "mean"),
).round(0).sort_values("revenue", ascending=False)

print(detail.head(5))
"""),

md("""
## Conclude

The answer is **one sentence with two figures**. Not a table, not a chart: the conclusion, said out
loud.
"""),

code("""
best = detail.index[0]
revenue = detail.iloc[0]["revenue"]
share = revenue / sales["amount"].sum()

print(f"{best[0]} through {best[1]} concentrates {revenue:,.0f} pesos, "
      f"{share:.0%} of the year. That is where to look first.")
"""),

md("""
Note what is **not** in that sentence: it does not say how the file was cleaned, or how many lines
of code it took. That comes afterwards, when somebody asks.

The conclusion first, the evidence behind it.

## The exercise's trap

Had you grouped before normalising the region, the report would say something else. Check it.
"""),

code("""
uncleaned = pd.read_csv("sales.csv")
uncleaned["unit_price"] = (uncleaned["unit_price"]
                           .str.replace("$", "", regex=False)
                           .str.replace(",", "", regex=False)
                           .str.strip().astype(float))
uncleaned["amount"] = uncleaned["units"].fillna(0) * uncleaned["unit_price"]

print("Uncleaned, the north reports:")
print(uncleaned[uncleaned["region"] == "North"]["amount"].sum().round(2))
print()
print("Clean, the north reports:")
print(sales[sales["region"] == "North"]["amount"].sum().round(2))
"""),

md("""
Nearly a million pesos of difference in a single region, and both figures come from the same file.
The one above leaves out the rows that said `" North"` and `"north"`.

Neither raises an error. Only one is true.
"""),

md("""
---
# Self-check

Answer without running anything, then check. If you get more than two wrong, that is the topic to
revise.

### 1 · Indexes

`data = [10, 20, 30, 40]`. What does `data[1:3]` return, and how many elements does it have?

### 2 · Types

What does `print("3" * 3)` print and what does `print(3 * 3)` print?

### 3 · Selection

With `x = 5`, what does this print and why?

```python
if x > 10:
    print("high")
elif x > 3:
    print("medium")
elif x > 4:
    print("never")
```

### 4 · Loops

How many times does something print with `for i in range(2, 11, 4)`?

### 5 · Functions

What is `r` after `r = print("hello")`?

### 6 · Collections

How many elements does `{1, 2, 2, 3}` have, and how many does `{"a": 1, "a": 2}`?

### 7 · Files

What happens to an existing file when opened with `open(path, "w")`?

### 8 · pandas

What is the difference between `sales["units"]` and `sales[["units"]]`?

### 9 · pandas

`pivot_table` with no `aggfunc`: does it sum or average?

### 10 · Visualisation

`sns.barplot` with no `estimator`: does it sum or average?
"""),

code("""
# The answers, checked. Run this after answering.
data = [10, 20, 30, 40]
print("1 ·", data[1:3], "and it has", len(data[1:3]), "elements")
print("2 ·", repr("3" * 3), "against", 3 * 3)

x = 5
result = "high" if x > 10 else ("medium" if x > 3 else "other")
print("3 ·", result, "· the third branch is unreachable, x > 3 catches it first")

print("4 ·", len(list(range(2, 11, 4))), "times:", list(range(2, 11, 4)))
print("5 ·", repr(print("   (this is the inner print)")), "· print returns None")
print("6 ·", len({1, 2, 2, 3}), "and", len({"a": 1, "a": 2}), "· both drop the repeat")
print("7 · it empties it the instant it opens, before you can read")

print("8 ·", type(sales["units"]).__name__, "against", type(sales[["units"]]).__name__)

no_agg = sales.pivot_table(index="region", columns="channel", values="amount")
with_sum = sales.pivot_table(index="region", columns="channel", values="amount",
                             aggfunc="sum")
print("9 · it averages:", round(no_agg.loc["North", "Retail"], 2),
      "against the sum:", round(with_sum.loc["North", "Retail"], 2))
print("10 · it averages too, same as pivot_table")
"""),

md("""
---
## Three ideas to take away

**Programming is writing the procedure down.** Which is why the analysis can be repeated, reviewed
and defended when somebody asks in March.

**Clean before you calculate.** A wrong number never announces itself, and it always looks as
reasonable as the right one. Nearly a million pesos in one region, from the same table.

**The finding goes in the title.** What the reader cannot see on their own is what you found, and
that is your entire job.

Any question about grades or about what comes next, by email or on Google Chat.
"""),

]

write(OUT / "en" / "w17.ipynb", en)
print("wrote", OUT / "en" / "w17.ipynb")
