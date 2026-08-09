"""notebooks/analisis-de-datos/en/w15.2.ipynb"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

en = [

md("""
# Data Analysis · Week 15, session 2 of 3
## Selecting, filtering and cleaning

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

Last session you diagnosed the file and left it alone. Today it gets fixed. You will write
the AutoFilter instead of clicking it, and then repair the four defects `sales.csv` carries,
saying out loud what you decided about each one.

By the end of this notebook you will be able to:

1. Pick columns by name and rows by condition, with brackets and with `loc` and `iloc`.
2. Build a boolean mask and hand it back to the table.
3. Combine conditions with `&`, `|`, `~` and `isin`, and explain why the words `and` and `or`
   do not work here.
4. Repair duplicates, inconsistent text, numbers stored as text and blank cells.
5. Assign with `loc` and explain why chained assignment does nothing.

### How to use this notebook

Run the cells in order. Five fail on purpose and carry a comment saying so.

This session writes a file, `sales_clean.csv`, into the Colab session. It lives while the
session is open and disappears when it closes. That is fine: session 15.3 creates it again
when it needs it.
"""),

md("""
---
## Setup
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

md("""
### The version matters more today than last session

On top of what a text column's type is called (`object` on 2.x, `str` on 3.0), this session
touches Copy-on-Write, and the two versions do not behave the same there. Block 3
demonstrates it with both outputs written down, so you will not be left wondering which one
you got.
"""),

bootstrap_cell("en"),

md("""
---
# Block 1 · Selecting and filtering

In a spreadsheet this is scrolling, hiding columns and switching the AutoFilter on and off.
In pandas you describe what you want and get a new table back. The original is never
touched, which means you can try a filter without fear of ruining anything.

This block works on `employees.csv`, which has 120 rows and comes in clean. Practising
filtering on dirty data mixes two problems together, and today we want them one at a time.
"""),

code("""
employees = pd.read_csv("employees.csv")

print(employees.shape)
print(employees.head())
"""),

md("""
## Choosing columns

One bracket with a name gives back a `Series`, the column on its own.
"""),

code("""
print(employees["monthly_salary"].head(3))
"""),

md("""
One bracket with a list of names gives back a `DataFrame`. The double brackets confuse
everyone once: the outer pair is the selection, the inner pair is the list of names you are
selecting.
"""),

code("""
print(employees[["employee_id", "area", "monthly_salary"]].head(3))
"""),

md("""
## Choosing rows

A condition applied to a column gives back a column of trues and falses, one per row. That
is the mask, and it is the whole idea behind filtering in pandas.
"""),

code("""
mask = employees["monthly_salary"] > 50000

print(mask.head())
print()
print("Rows that satisfy it:", mask.sum())
"""),

md("""
`sum` over booleans works because `True` is one and `False` is zero. Adding up the mask
counts how many qualify, without writing a counter.

Handed back to the table inside brackets, the mask leaves only the rows marked true.
"""),

code("""
well_paid = employees[mask]

print("Earning more than 50,000:", len(well_paid))
print(well_paid.head(3))
"""),

md("""
Usually the mask is written inline rather than stored under a name. Both forms do the same
thing, and the one above only exists so you can see the mask from the inside.
"""),

code("""
print("The Finance area only:", len(employees[employees["area"] == "Finance"]))
"""),

md("""
## Combining conditions

| Symbol | Means | The rule |
|---|---|---|
| `&` | Both | Never the word `and` |
| `\\|` | Either | Never the word `or` |
| `~` | The opposite | Goes before the condition |
| `isin` | Is in the list | Replaces a row of pipes |

Two rules that must both hold. Note the ampersand, and note the parentheses: without them
Python applies the comparison in the wrong order.
"""),

code("""
senior_finance = employees[(employees["area"] == "Finance") &
                           (employees["tenure_months"] > 60)]

print("Finance with more than five years:", len(senior_finance))
"""),

code("""
either = employees[(employees["area"] == "Finance") |
                   (employees["area"] == "Sales")]

print("Finance or Sales:", len(either))
"""),

md("""
For more than two options, `isin` reads better than a chain of pipes. It is the pandas
answer to a filter with several boxes ticked.
"""),

code("""
front = employees[employees["area"].isin(["Sales", "Marketing"])]
print("Sales or Marketing:", len(front))

back = employees[~employees["area"].isin(["Sales", "Marketing"])]
print("Everything else:   ", len(back))

print("They add up:", len(front) + len(back), "of", len(employees))
"""),

md("""
## Two cells that fail on purpose

The two rules above are not style. Breaking them produces the two most confusing errors in
pandas, and it is worth meeting them once so you recognise them later.

### Using the word `and`
"""),

code("""
# FAILS ON PURPOSE. With two Series you need &, not the word and.
try:
    employees[(employees["area"] == "Finance") and (employees["tenure_months"] > 60)]
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
The message talks about the truth value of a Series and never mentions `and` at all. The
reason is that `and` asks Python for a single true or false, and a mask carries 120. The `&`
does know how to work row by row.

### Forgetting the parentheses
"""),

code("""
# FAILS ON PURPOSE. Without parentheses, & is evaluated before ==.
try:
    employees[employees["area"] == "Finance" & employees["tenure_months"] > 60]
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`&` binds tighter than `==` in Python, so without parentheses the first thing attempted is
`"Finance" & employees["tenure_months"]`, which means nothing. Every condition goes inside
its own parentheses, always, even when it looks redundant.

## Filtering on text

Text columns get their own set of tools under `.str`, and they apply to the whole column at
once. This is where the wildcards of a spreadsheet end up.
"""),

code("""
managers = employees[employees["job_title"].str.contains("manager", case=False)]

print("Managers of any kind:", len(managers))
print(managers[["job_title", "area"]].head(3))
"""),

md("""
`case=False` searches without distinguishing capitals, which is almost always what you want
when a person typed the data in.

## Rows and columns together

`loc` takes rows first, columns second, and it works with labels.
"""),

code("""
print(managers.loc[:, ["area", "job_title", "monthly_salary"]].head(3))
"""),

md("""
`iloc` does the same thing with positions instead of labels. The numbers count from 0 and
the end of a range is not included, exactly as slicing worked back in week 12.
"""),

code("""
print(employees.iloc[0:2, 0:3])
"""),

md("""
A bare colon means "everything", so `loc[:, [...]]` reads as "all rows, these columns". It is
the same `:` from slicing.

## Sorting
"""),

code("""
top = employees.sort_values("monthly_salary", ascending=False)

print(top[["employee_id", "area", "job_title", "monthly_salary"]].head())
"""),

md("""
With several columns, the order of the list is the order of the tie-breaks: area
alphabetically first, and inside each area the salary from highest to lowest.
"""),

code("""
by_area = employees.sort_values(["area", "monthly_salary"], ascending=[True, False])

print(by_area[["area", "job_title", "monthly_salary"]].head())
"""),

md("""
**Predict before you run.** `sort_values` gave back a sorted table. Did `employees` end up
sorted too?
"""),

code("""
print("First row of employees:")
print(employees[["employee_id", "monthly_salary"]].head(1))
print()
print("First row of top:")
print(top[["employee_id", "monthly_salary"]].head(1))
"""),

md("""
`employees` is unchanged. Nearly every pandas method gives back a new table and leaves the
original alone, which is exactly why you can filter without fear. If you want the change to
stick, reassign: `employees = employees.sort_values(...)`.
"""),

md("""
---
# Block 2 · The four repairs

Cleaning is most of the job. `sales.csv` has four defects, and each one is the kind you meet
in a real export.

| Defect | How many | Fixed with |
|---|---|---|
| Duplicated rows | 7 | `drop_duplicates` |
| Badly captured region | 8 forms | `str.strip` and `str.title` |
| Price as text | 324 | `str.replace` and `astype` |
| Blank unit counts | 11 | `dropna` or `fillna` |

They go one at a time, and each fix writes down what it decided. The same will be asked of
you in the project.
"""),

code("""
sales = pd.read_csv("sales.csv")

print(f"Loaded {len(sales)} rows")
"""),

md("""
## Defect 1 · The duplicated rows

Seven records were captured twice. Left alone they inflate every total.
"""),

code("""
print("Duplicated rows:", sales.duplicated().sum())

sales = sales.drop_duplicates()
print("Rows after dropping them:", len(sales))
"""),

md("""
`drop_duplicates` compares whole rows by default. To treat a row as duplicated when only
some columns repeat, name them:

```python
sales.drop_duplicates(subset=["date", "region", "product"])
```

That is a business decision, not a technical one. Two genuine sales of the same product to
the same region on the same day are not a duplicate, and the computer has no way to tell
them apart.

## Defect 2 · The inconsistent text

The same region was typed as `"North"`, `"north"`, `"NORTH"` and `" North"`.
"""),

code("""
print("Region values before:", sales["region"].nunique())

sales["region"] = sales["region"].str.strip().str.title()

print("Region values after: ", sales["region"].nunique())
print()
print(sales["region"].value_counts())
"""),

md("""
`.str` gives access to any string method, applied to the whole column. It is the week 8 loop
without writing it. `strip` removes the surrounding spaces and `title` normalises the
capitalisation, so `" North"`, `"north"`, `"NORTH"` and `"North "` all end up as the same
value.

Eight became four, and the north went from 75 rows to 95. Those twenty rows are the ones a
`groupby` last session would have handed to regions that do not exist.

## Defect 3 · The number stored as text

`unit_price` arrived as `"$ 2,082.50"`. The symbol and the comma are formatting, and they
have to come off before the text can become a number.

First, the direct conversion, which does not work.
"""),

code("""
# FAILS ON PURPOSE. The currency sign and the comma block the conversion.
try:
    sales["unit_price"].astype(float)
except ValueError as e:
    print("ValueError:", str(e)[:120])
"""),

md("""
Now in the right order: strip the formatting, and only then convert.
"""),

code("""
print("unit_price before:", sales["unit_price"].iloc[0], "|", sales["unit_price"].dtype)

sales["unit_price"] = (
    sales["unit_price"]
    .str.replace("$", "", regex=False)   # regex=False: treat $ as a literal character
    .str.replace(",", "", regex=False)   # the thousands separator
    .str.strip()
    .astype(float)                       # only now can the text become a number
)

print("unit_price after: ", sales["unit_price"].iloc[0], "|", sales["unit_price"].dtype)
"""),

md("""
`regex=False` matters. Without it, pandas reads the currency sign as a pattern symbol rather
than as the character you want removed.

The date column deserves the same treatment. As text it sorts by luck; as a real date it can
be compared, subtracted and grouped by month.
"""),

code("""
sales["date"] = pd.to_datetime(sales["date"])

print("dtype of date:", sales["date"].dtype)
print("The oldest sale:", sales["date"].min().date())
print("The newest:     ", sales["date"].max().date())
"""),

md("""
That `.min()` is the proof the conversion worked. On text it would have compared
alphabetically, and it only came out right by accident, because the format puts the year
first.

## Defect 4 · The blank cells

Eleven rows have no unit count. There are three honest responses, and picking one is the
analyst's job, not the library's.

Before choosing, it is worth seeing what number each one leads to.
"""),

code("""
missing = sales["units"].isna().sum()
print("Rows with no unit count:", missing)
print()
print("Option A, drop them:    ", round(sales["units"].dropna().mean(), 2),
      "over", sales["units"].dropna().count(), "rows")
print("Option B, fill with 0:  ", round(sales["units"].fillna(0).mean(), 2),
      "over", sales["units"].fillna(0).count(), "rows")
print("Option C, leave them:   ", round(sales["units"].mean(), 2),
      "over", sales["units"].count(), "rows")
"""),

md("""
Here the amount cannot be computed without the units, so the row is dropped and the decision
is recorded in the output rather than hidden.
"""),

code("""
before = len(sales)
sales = sales.dropna(subset=["units"])
print(f"Dropped {before - len(sales)} rows with no unit count")

sales["units"] = sales["units"].astype(int)
print("dtype of units:", sales["units"].dtype)
print("Rows remaining:", len(sales))
"""),

md("""
With the blanks gone the column can hold whole numbers again. It is the conversion that
failed last session, and it works now for one reason only: the missing values are no longer
there.

## The column we actually wanted
"""),

code("""
sales["amount"] = sales["units"] * sales["unit_price"]

print(sales.head())
print()
print("Total for the year:", f"{sales['amount'].sum():,.2f}")
"""),

md("""
Twelve million eight hundred and fifty-three thousand, over 306 rows. That number only means
anything because the four repairs happened first. Computed on the raw file it would have
come out different and worn the same confident face.

## Saving the clean file
"""),

code("""
sales.to_csv("sales_clean.csv", index=False)

print(f"Wrote {len(sales)} clean rows to sales_clean.csv")
print(open("sales_clean.csv", encoding="utf-8").readline().strip())
"""),

md("""
`index=False` keeps pandas from adding its row numbers as a first column, which is almost
always what you want when the file is going back to a spreadsheet.

The file sits in the Colab session, next to the CSVs the setup cell brought in. Any cell
below can read it again, and it disappears when you close the session.
"""),

md("""
---
# Block 3 · The trap worth meeting once

There is a way of writing into the table that writes nothing. It raises no error and changes
nothing. It is a silent no-op, and that silence is what makes it dangerous.

When you chain two operations to assign, the first half builds a temporary table holding the
matching rows. The assignment lands on that temporary copy, which is discarded on the next
line.

The demonstration runs on a copy, so the file you just saved keeps its real channel values.
`copy()` is how you say "from here on I want a separate table".
"""),

code("""
demo = sales.copy()
northern = (demo["region"] == "North").sum()

print("Northern rows:", northern)
print(demo.loc[demo["region"] == "North", "channel"].value_counts())
"""),

md("""
**Predict before you run.** The next cell tries to put `"Retail"` in the channel of every
northern row, using a chained assignment. What happens?

- **A.** Every northern row ends up as Retail.
- **B.** Nothing changes, and no error is raised either.
- **C.** A `KeyError` is raised because `channel` does not exist.
- **D.** A new column called `channel` is created.
"""),

code("""
# FAILS ON PURPOSE. This looks like it edits the table, and it does not.
import warnings

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    demo[demo["region"] == "North"]["channel"] = "Retail"
    print("Warnings:", [type(w.message).__name__ for w in caught] or "none")

print()
print(demo.loc[demo["region"] == "North", "channel"].value_counts())
"""),

md("""
The answer is **B**. The northern channels are still spread across Retail, Online and
Wholesale, exactly as before.

Which warning appears depends on your version: `ChainedAssignmentError` on pandas 3.0,
`SettingWithCopyWarning` on 2.x. Both say the same thing under a different name, and both
are warnings, not errors. The code keeps running.

### The variant that really does change with the version

There is another way to write the same thing, with the column first and the condition
second. This one genuinely behaves differently across versions, which is why it is worth
seeing.

| | pandas 2.x | pandas 3.0 |
|---|---|---|
| `df[mask]["col"] = v` | does nothing | does nothing |
| `df["col"][mask] = v` | **does modify the table** | does nothing |

Run the cell and compare the number against the table.
"""),

code("""
demo2 = sales.copy()
before = (demo2["channel"] == "Retail").sum()

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    demo2["channel"][demo2["region"] == "North"] = "Retail"
    print("Warnings:", [type(w.message).__name__ for w in caught] or "none")

after = (demo2["channel"] == "Retail").sum()
print()
print("Rows in Retail before:", before)
print("Rows in Retail after: ", after)
print("Did anything change?", "yes, this is pandas 2.x" if before != after else "no, this is pandas 3.0")
"""),

md("""
The same code, two results, depending on which version you got. Nothing tells you which one
you are running except a warning that is easy to ignore.

That is the whole argument against chained assignment: it is not that it is badly written,
it is that its result depends on something that is not in your code.

## The right way: `loc`, in a single step

`sales.loc[condition, "column"] = value`. One instruction, rows first, column second. That is
how pandas knows you mean to write into the original table.
"""),

code("""
demo3 = sales.copy()

demo3.loc[demo3["region"] == "North", "channel"] = "Retail"

print(demo3.loc[demo3["region"] == "North", "channel"].value_counts())
"""),

md("""
Ninety-two rows in Retail, which is all of the northern ones. One instruction, no warnings,
and the same result on any version of pandas.

And yes, a moment ago the north had 95. It dropped to 92 because three of the eleven rows
with no unit count were northern and got discarded afterwards. Both numbers are right at
their point in the process, and that is exactly why it pays to print the count at each step
rather than trusting the one from five cells ago.

This is the rule that goes to the project: **anything that writes into the table goes
through `loc`.**
"""),

md("""
---
## The payoff: filtering on clean data

Now the business question that opened the session can actually be asked. Northern sales
above fifty thousand pesos, which is a two-condition filter on a column that only exists
because you cleaned.
"""),

code("""
sel = sales[(sales["region"] == "North") &
            (sales["amount"] > 50000)]

print("Large northern sales:", len(sel))
print("Channels they came through:", sorted(sel["channel"].unique()))
print()
print(sel[["date", "channel", "product", "units", "amount"]].head())
"""),

md("""
Twenty-two sales, across all three channels. Look at the road it took to reach a two-digit
number: drop duplicates, normalise the text, convert the price, resolve the holes, compute
the amount, and only then filter.

Had you filtered on the raw file, `amount` did not exist, `region` held eight different
things and seven rows were counted twice. The filter would have run just as fast and given a
different number.
"""),

md("""
---
## Four errors when cleaning

**Calculating before cleaning.** A sum over dirty data returns a number, and that number is
wrong without ever telling you.

**Using `and` instead of `&`.** The error you get talks about the truth value of a Series and
helps with nothing. You saw it above, and recognising it saves you half an hour.

**Forgetting the parentheses.** Without them Python evaluates in the wrong order, because `&`
binds tighter than `==`. Every condition goes inside its own parentheses.

**Filling holes without saying so.** Putting zero where a value was missing is a business
decision. It is made deliberately and written down, not inherited from a method's default.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom. The first four are filtering on `employees.csv`, the
next three are cleaning, and the last one is your own file.

## Filtering

### Exercise 1 · Three simple filters

On `employees`, count how many people fall into each of these cases and print the three
numbers with their labels:

1. They earn less than 30,000 a month.
2. They have more than eight years of tenure, meaning more than 96 months.
3. They work in Monterrey and earn more than 40,000.

### Exercise 2 · The negation

Print how many people are **not** in Mexico City, two different ways: with `!=` and with `~`
plus `isin`. Check that both give the same number.

### Exercise 3 · Analysts of any area

Use `.str.contains` to find everyone whose job title includes the word "analyst", ignoring
capitalisation. Print how many there are and how they split across areas.

### Exercise 4 · The five best paid in Sales

Filter the Sales area, sort by salary from highest to lowest and show the first five with
identifier, title, tenure and salary. All of it in one chain of methods.

## Cleaning

### Exercise 5 · Cleaning as a function

Write a function `clean_sales(path)` that reads the raw CSV, applies the four repairs, adds
the `amount` column and returns the clean table. Have it print a one-line log per repair,
saying what it found and what it did.

Test it from scratch on `sales.csv` and check that it reaches the same 306 rows.

### Exercise 6 · The three totals

Report the total for the year under three scenarios and put them in the same output:

1. On the raw file, without dropping duplicates, treating the holes as zero.
2. After dropping duplicates, treating the holes as zero.
3. After dropping duplicates and discarding the rows with no unit count.

Say in a comment which one you would report and why the other two would be wrong.

Watch out: to compute an amount on the raw file you have to convert the price first.

### Exercise 7 · The business decision behind a duplicate

`drop_duplicates` with no arguments removed seven identical rows. Now try
`drop_duplicates(subset=["date", "region", "product"])` on the raw file and compare how many
rows are left.

Then explain in a comment why the second number is so much smaller, and why using it would
be a mistake on this file.

## With your own data

### Exercise 8 · Clean your file and leave a record

Apply to your own CSV whatever repairs it needs and save a clean version. For each fix write
one line saying what you found, what you decided and how many records were affected.

No chained assignment: anything that writes into the table goes through `loc`.

The test: compare the total before and after cleaning. If it did not change, either the file
was clean or you did not clean it.
"""),

md("""
---
## Three ideas to take away

**A filter is a column of true and false.** Handed back to the table inside brackets, it
leaves only the marked rows and never touches the original. That is why you can experiment
without fear.

**Clean before you calculate.** A sum over dirty data returns a number, and a wrong number
never announces itself. Today's twelve million only means something because of the four
repairs that came first.

**Write with `loc`, in one step.** Chained assignment does nothing and raises nothing, which
is the worst possible combination, and on top of that its result changes between pandas
versions.

Next session is grouping and joining. The pivot table and the `VLOOKUP`, one line each.
"""),

md("""
---
# Solutions

### Exercise 1

```python
print("Earning less than 30,000:",
      len(employees[employees["monthly_salary"] < 30000]))

print("More than eight years:",
      len(employees[employees["tenure_months"] > 96]))

print("Monterrey and more than 40,000:",
      len(employees[(employees["city"] == "Monterrey") &
                    (employees["monthly_salary"] > 40000)]))
```

The third is the only one that needs parentheses, because it combines two conditions. The
other two can carry them as well and they do no harm.

### Exercise 2

```python
with_not_equal = employees[employees["city"] != "Mexico City"]
with_isin = employees[~employees["city"].isin(["Mexico City"])]

print("With !=:   ", len(with_not_equal))
print("With ~isin:", len(with_isin))
print("Same?", len(with_not_equal) == len(with_isin))
```

With a single value both forms give the same answer and `!=` reads better. `~isin` starts
winning the moment there are three or four cities, because `!=` chained with `&` becomes
unreadable.

### Exercise 3

```python
analysts = employees[employees["job_title"].str.contains("analyst", case=False)]

print("Analysts:", len(analysts))
print(analysts["area"].value_counts())
```

`case=False` is what makes "Analyst" and "analyst" count the same. Without it the result
depends on how whoever filled in the file typed the job titles.

### Exercise 4

```python
print(
    employees[employees["area"] == "Sales"]
    .sort_values("monthly_salary", ascending=False)
    [["employee_id", "job_title", "tenure_months", "monthly_salary"]]
    .head()
)
```

It reads top to bottom: filter, sort, pick columns, take five. Each step receives the table
the previous one left, and none of them touches `employees`.

### Exercise 5

```python
def clean_sales(path):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows")

    dupes = df.duplicated().sum()
    df = df.drop_duplicates()
    print(f"Duplicates: {dupes} found, {dupes} dropped, {len(df)} left")

    before = df["region"].nunique()
    df["region"] = df["region"].str.strip().str.title()
    print(f"Region: {before} distinct values, normalised to {df['region'].nunique()}")

    df["unit_price"] = (df["unit_price"]
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.strip()
                        .astype(float))
    df["date"] = pd.to_datetime(df["date"])
    print("unit_price converted to float, date converted to a date")

    holes = df["units"].isna().sum()
    df = df.dropna(subset=["units"])
    df["units"] = df["units"].astype(int)
    print(f"Units: {holes} holes, rows discarded, {len(df)} left")

    df["amount"] = df["units"] * df["unit_price"]
    print(f"Done: {len(df)} rows, total {df['amount'].sum():,.2f}")
    return df


clean = clean_sales("sales.csv")
```

It reaches the same 306 rows and the same total. That the cleaning fits inside a function is
what makes it repeatable, and repeatable is what makes it auditable: anyone can run it on the
original file and arrive at your number.

### Exercise 6

```python
raw = pd.read_csv("sales.csv")
raw["unit_price"] = (raw["unit_price"]
                     .str.replace("$", "", regex=False)
                     .str.replace(",", "", regex=False)
                     .str.strip()
                     .astype(float))

one = raw["units"].fillna(0) * raw["unit_price"]
no_dupes = raw.drop_duplicates()
two = no_dupes["units"].fillna(0) * no_dupes["unit_price"]
clean = no_dupes.dropna(subset=["units"])
three = clean["units"] * clean["unit_price"]

print(f"1. Raw, holes as zero:          {one.sum():>15,.2f}  over {len(raw)} rows")
print(f"2. No duplicates, holes zero:   {two.sum():>15,.2f}  over {len(no_dupes)} rows")
print(f"3. No duplicates, no holes:     {three.sum():>15,.2f}  over {len(clean)} rows")

# The third one. The first counts seven sales twice, so it inflates the total with
# money that never came in. The second no longer double-counts them, but it assigns
# zero pesos to eleven sales that did happen, which understates the year.
```

Scenarios two and three give the same total, because a row with zero units contributes zero
pesos. What changes is the row count, and therefore any per-sale average. Worth noticing: two
different routes can agree on the total and diverge on everything else.

### Exercise 7

```python
raw = pd.read_csv("sales.csv")

print("Rows:                             ", len(raw))
print("Without exact duplicates:         ", len(raw.drop_duplicates()))
print("Without repeating date, region, product:",
      len(raw.drop_duplicates(subset=["date", "region", "product"])))

# The second number is much smaller because the file covers 52 weeks with only five
# products and four regions, so the same combination legitimately appears many times.
# Using that subset here would erase real sales: two sales of the same product to the
# same region on the same day are two sales, not a capture error. The subset is the
# right tool when the combination of columns genuinely identifies the record, like a
# receipt number or a customer key plus a date.
```

This exercise exists so `subset` does not become a reflex. It is the correct tool when there
is a real key, and a data eraser when there is not.

### Exercise 8

There is no published solution, because the file is different for everyone. It is graded on
three things: that the log has one line per repair with the affected count, that there is no
chained assignment anywhere, and that the total before and after is reported.
"""),

]

write(OUT / "en" / "w15.2.ipynb", en)
print("wrote", OUT / "en" / "w15.2.ipynb")
