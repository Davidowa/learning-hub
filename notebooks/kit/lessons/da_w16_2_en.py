"""notebooks/analisis-de-datos/en/w16.2.ipynb

Source deck: ppts/python/analisis-de-datos/en/w16.2.en.yaml
Source code:  06 - Advanced/A06 - Data Visualization/04_seaborn.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

CLEANING = """
# The cleaning from session 15.2, so this notebook opens on its own.
sales = pd.read_csv("sales.csv").drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .str.strip().astype(float))
sales["date"] = pd.to_datetime(sales["date"])
sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)
sales["amount"] = sales["units"] * sales["unit_price"]

employees = pd.read_csv("employees.csv")

print(f"{len(sales)} clean sales, {len(employees)} employees")
"""

en = [

md("""
# Data Analysis · Week 16, session 2 of 2
## seaborn and closing the project

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

The last content session. Statistical charts in one line, what an average hides, and the project
handover.

By the end of this notebook you will be able to:

1. Plot straight from a `DataFrame`, passing column names without preparing the data first.
2. Pick the right estimator, because seaborn averages by default.
3. Bring in a third variable with `hue`.
4. Read a box plot: median, middle half, range and outliers.
5. Present a finding with the conclusion first.

### How to use this notebook

Run the cells in order. Three deliberately draw a misleading chart so you can compare.
"""),

md("""
---
## Setup
"""),

code("""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("pandas", pd.__version__, "· seaborn", sns.__version__)
"""),

bootstrap_cell("en"),

code(CLEANING),

md("""
---
# Block 1 · seaborn

It sits on top of matplotlib and takes the `DataFrame` directly. You tell it which columns to use
and it works out the rest.

With matplotlib you have to group first:

```python
by_region = sales.groupby("region")["amount"].sum()
ax.bar(by_region.index, by_region.values)
```

With seaborn you name the columns:
"""),

code("""
sns.set_theme(style="whitegrid", palette="deep")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=sales, x="region", y="amount", estimator="sum",
            errorbar=None, hue="region", legend=False, ax=ax)
ax.set_title("Total revenue by region", loc="left", fontweight="bold")
ax.set_ylabel("Revenue")
plt.show()
"""),

md("""
**`set_theme`** sets grid, fonts and palette for every chart that follows. It is configured once,
which is why they look consistent.

**`estimator="sum"`** says which summary you want. And here comes the number one error with
seaborn.

**Predict before you run.** What does this line draw if you do not pass `estimator`?

- **A.** The total per region.
- **B.** The mean per region, which is what it does by default.
- **C.** The row count per region.
- **D.** An error, because the estimator is missing.
"""),

code("""
# DRAWS BADLY ON PURPOSE, on the left. Both panels carry the same data.
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.barplot(data=sales, x="region", y="amount",
            errorbar=None, hue="region", legend=False, ax=axes[0])
axes[0].set_title("No estimator: it averages", loc="left", fontweight="bold")

sns.barplot(data=sales, x="region", y="amount", estimator="sum",
            errorbar=None, hue="region", legend=False, ax=axes[1])
axes[1].set_title("With estimator='sum': it totals", loc="left", fontweight="bold")

for a in axes:
    a.set_ylabel("Revenue")
fig.tight_layout()
plt.show()
"""),

md("""
The answer is **B**. By default it averages, and the two charts rank the regions differently.

A bar showing a mean when the reader expected a total is a correct number that misleads. It is
exactly the same trap as `pivot_table` without `aggfunc` in week 15.3.

**`errorbar=None`** matters too: without it, seaborn draws a confidence interval on top of every
bar. That is almost never what you wanted, and it claims something about sampling your chart is
not saying.
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=sales, x="region", y="amount", estimator="sum",
            hue="region", legend=False, ax=ax)
ax.set_title("Without errorbar=None: the whiskers appear", loc="left", fontweight="bold")
plt.show()
"""),

md("""
## The finding

The two charts above rank differently, and that is not a defect. That is the finding.
"""),

code("""
summary = (sales.groupby("region")["amount"]
           .agg(["sum", "mean", "count"]) / [1000, 1000, 1])

print(summary.round(0).sort_values("sum", ascending=False))
"""),

md("""
**North sells more than Centre over the year. Centre sells bigger on every transaction.**

Both statements are true and both come from the same table. The chart you pick decides which of
the two your reader sees, and picking without noticing is how an honest report ends up saying
something you did not mean.

| Question | Answered by |
|---|---|
| How much came in? | The total |
| How big is each sale? | The mean |
| How often do we sell? | The count |

All three together tell the story: **North sells often, Centre sells dear.** That sentence appears
in neither chart on its own.

## A third variable with `hue`
"""),

code("""
fig, ax = plt.subplots(figsize=(10, 4.5))
sns.barplot(data=sales, x="region", y="amount", hue="channel",
            estimator="sum", errorbar=None, ax=ax)
ax.set_title("Wholesale dominates in all four regions", loc="left", fontweight="bold")
ax.set_ylabel("Revenue")
plt.show()
"""),

md("""
`hue` separates by colour and builds the legend by itself. Twelve bars that in matplotlib would
have cost a loop and a colour list.

And the title states the finding, not the axes, which is last session's rule.
"""),

md("""
---
# Block 2 · What an average hides

Two areas with the same mean salary can look nothing alike. The box shows it at a glance.
"""),

code("""
print(employees.groupby("area")["monthly_salary"]
      .agg(["mean", "median", "std", "count"]).round(0))
"""),

code("""
order = (employees.groupby("area")["monthly_salary"]
         .median().sort_values(ascending=False).index)

fig, ax = plt.subplots(figsize=(10, 4.5))
sns.boxplot(data=employees, x="area", y="monthly_salary", order=order,
            hue="area", legend=False, ax=ax)
ax.set_title("The typical salary and how uneven each area is",
             loc="left", fontweight="bold")
ax.set_ylabel("Monthly salary")
plt.show()
"""),

md("""
**The box** holds the middle half of the values, from the first to the third quartile. The line
inside is the **median**, not the mean.

**The whiskers** reach the typical range. The loose dots beyond them are the outliers.

**`order`** sorts by median, which makes the ranking read by itself. Same rule as sorting the bars.

Compare the box with the mean drawn on top:
"""),

code("""
fig, ax = plt.subplots(figsize=(10, 4.5))
sns.boxplot(data=employees, x="area", y="monthly_salary", order=order,
            hue="area", legend=False, ax=ax)
sns.pointplot(data=employees, x="area", y="monthly_salary", order=order,
              errorbar=None, color="#B4530A", linestyle="none",
              markers="D", ax=ax)
ax.set_title("The diamond is the mean, the line is the median",
             loc="left", fontweight="bold")
ax.set_ylabel("Monthly salary")
plt.show()
"""),

md("""
In every area the diamond sits above the line. That is the tail of high salaries pulling the mean
up, and it is the same thing you saw with the five salaries in week 3.

## The histogram, now in one line
"""),

code("""
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(data=employees, x="monthly_salary", bins=15, ax=axes[0])
axes[0].set_title("All together", loc="left", fontweight="bold")

sns.histplot(data=employees, x="monthly_salary", hue="area",
             element="step", bins=15, ax=axes[1])
axes[1].set_title("Split by area", loc="left", fontweight="bold")

fig.tight_layout()
plt.show()
"""),

md("""
## The heatmap

It takes the grid `pivot_table` produced in session 15.3, with no extra preparation.
"""),

code("""
grid = sales.pivot_table(index="region", columns="channel",
                         values="amount", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(7, 4))
sns.heatmap(grid, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_title("Revenue by region and channel, in thousands",
             loc="left", fontweight="bold")
plt.show()
"""),

md("""
**`annot`** writes the value inside each cell. Without it, the colour forces the reader to estimate
against the side bar.

**`fmt`** controls how what gets written is rounded. In thousands with no decimals it fits
comfortably.

The colour does the ranking for you: you see where the high values are without comparing figures
one by one.

## The scatter, with a line
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.regplot(data=employees, x="tenure_months", y="monthly_salary",
            scatter_kws={"alpha": 0.5}, line_kws={"color": "#B4530A"}, ax=ax)

r = employees["tenure_months"].corr(employees["monthly_salary"])
ax.set_title(f"Tenure explains little of the salary, correlation {r:.2f}",
             loc="left", fontweight="bold")
ax.set_xlabel("Tenure in months")
ax.set_ylabel("Monthly salary")
plt.show()
"""),

md("""
`regplot` draws the cloud and fits a line to it. The line rises, and the cloud is so scattered that
the correlation is 0.28.

And there is a trap worth naming: **a line can always be drawn.** That it exists does not mean it
explains anything. The number beside it is what says how much it is worth, and without it the line
suggests more than there is.
"""),

md("""
---
# Block 3 · The integrating project

It is handed in and presented today. It is worth twenty per cent, and the assessment is individual
even though the work is in teams.

| Aspect | Detail |
|---|---|
| What | Notebook or code, the dataset used, and a PDF report |
| Where | Blackboard. Email submissions are not graded |
| Weight | 20 % of the final grade |
| Code and analysis | 70 %: it runs and answers, correct cleaning, honest charts |
| Report | 30 %: narrative, justified decisions and integrated evidence |

## The conclusion first, the evidence behind it

Start by saying what you found. Then show how you got there, and finish with what you would do
about it.

Whoever is listening decides in the first thirty seconds whether to pay attention to the rest.

| Wrong order | Order that works |
|---|---|
| "We cleaned the file, dropped duplicates..." | "The north sells often and the centre sells dear" |
| "...then we grouped by region..." | "It shows in these two bars" |
| "...and the result was this" | "I suggest moving budget from volume to ticket" |

## A check before handing in

Run this cell against your own analysis. The four questions are the ones that cost the most marks.
"""),

code("""
CHECKLIST = [
    "Does the notebook run from zero, kernel restarted, with no errors?",
    "Are all paths relative, with the data sitting next to the code?",
    "Does every chart have a finding in its title, axis labels and a source?",
    "Does the report say what you did with the holes and the duplicates?",
    "Does every bar chart's vertical axis start at zero?",
    "Can each team member explain any part, not only their own?",
]

for i, question in enumerate(CHECKLIST, 1):
    print(f"{i}. {question}")
"""),

md("""
**A notebook that does not run from zero** costs the most: if it blows up, the maximum mark is
30 %. Restart it and run it through before handing in.

**Absolute paths** work on your machine and on no other. It is week 14's error.

**Charts with no title and no source** are the first thing looked at, and the cheapest thing in the
whole project to fix.

**Cleaning without a record** makes the analysis indefensible. If the report does not say what you
did with the holes, nobody can judge whether it was right.

## The presentation

Three minutes per team. The question, the finding, how you got there and what you would recommend.

**Two charts on screen maximum.** If you need five, you do not know what the finding is yet.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

### Exercise 1 · The estimator

Draw the same bar chart three times, with `sum`, `mean` and `count`, in a row of three panels. Give
each the title matching the question it answers.

Then say in a comment which you would use to decide where to put more budget, and why.

### Exercise 2 · The third variable

With `hue`, draw revenue by channel split by region. It is the same information as the notebook's
with the axes swapped.

Say in a comment which of the two reads better and why.

### Exercise 3 · The box of your data

Make a `boxplot` of `amount` by channel, ordered by median. Then answer: which channel has the
largest typical sale, and which has the most spread?

### Exercise 4 · Mean against median

For each channel, work out the mean and median of `amount` and the gap between them. Sort by that
gap.

The channel with the largest gap has the longest tail. Draw it with a histogram and confirm.

### Exercise 5 · The heatmap by month

Build a heatmap with the month down the rows and the region across the columns. Use `fmt=".0f"` and
divide by a thousand.

Say in a comment which cell is the highest and whether that surprises you.

### Exercise 6 · The line that says nothing

Draw a `regplot` of `units` against `unit_price` in `sales`, with the correlation in the title.

Then explain in a comment why that line should not be used to predict anything.

### Exercise 7 · Your project, checked

Run the checklist against your own analysis and answer all six in writing. For every "no", fix it
and answer again.

### Exercise 8 · The two charts

Pick the only two charts going into your presentation. Write for each: the finding it communicates,
why that shape and not another, and its alternative text.

If you cannot pick two, you do not know what the finding is yet.
"""),

md("""
---
## Three ideas to take away

**seaborn averages by default.** If you wanted the total and did not say `estimator`, the bar shows
a correct number that misleads.

**The average hides the shape.** Two areas with the same mean salary can be distributed in ways that
look nothing alike, and the box shows it at a glance.

**The conclusion goes first.** Whoever is listening decides in the first thirty seconds whether to
pay attention to the rest.

Next session is revision and the final exam.
"""),

md('''
---
# Solutions

### Exercise 1

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
titles = [("sum", "How much came in?"), ("mean", "How big is each sale?"),
          ("count", "How often do we sell?")]

for ax, (est, title) in zip(axes, titles):
    sns.barplot(data=sales, x="region", y="amount", estimator=est,
                errorbar=None, hue="region", legend=False, ax=ax)
    ax.set_title(title, loc="left", fontweight="bold")
    ax.set_ylabel("")

fig.tight_layout()
plt.show()

# For a budget decision I would use all three, not one. The total says where the
# money is today, the mean says where each peso invested returns more per
# transaction, and the count says where there is volume to sustain. North has the
# highest total and Centre the best mean: moving budget from one to the other
# changes what kind of business you are buying.
```

That the three bar charts rank differently is the point. A single chart would have hidden two of the
three answers.

### Exercise 2

```python
fig, ax = plt.subplots(figsize=(10, 4.5))
sns.barplot(data=sales, x="channel", y="amount", hue="region",
            estimator="sum", errorbar=None, ax=ax)
ax.set_title("Wholesale concentrates the revenue in every region",
             loc="left", fontweight="bold")
plt.show()

# This one reads better, with the channel on the axis. The difference between
# channels is far larger than the difference between regions, so putting it on the
# axis lets the eye compare what matters most. With the region on the axis, the
# three bars in each group look similar and the pattern has to be hunted for.
```

The rule that falls out: the variable with the most contrast goes on the axis, the other one in the
colour.

### Exercise 3

```python
channel_order = (sales.groupby("channel")["amount"]
                 .median().sort_values(ascending=False).index)

fig, ax = plt.subplots(figsize=(8, 4.5))
sns.boxplot(data=sales, x="channel", y="amount", order=channel_order,
            hue="channel", legend=False, ax=ax)
ax.set_title("Wholesale has the largest typical sale and the widest spread",
             loc="left", fontweight="bold")
plt.show()

print(sales.groupby("channel")["amount"].agg(["median", "std"]).round(0))
```

Wholesale wins both: the largest typical sale and the greatest spread. That makes sense, because a
wholesale order can be three units or sixty.

### Exercise 4

```python
comparison = sales.groupby("channel")["amount"].agg(["mean", "median"])
comparison["gap"] = comparison["mean"] - comparison["median"]
print(comparison.round(0).sort_values("gap", ascending=False))

worst = comparison["gap"].idxmax()

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data=sales[sales["channel"] == worst], x="amount", bins=25, ax=ax)
ax.axvline(sales[sales["channel"] == worst]["amount"].mean(),
           color="#B4530A", linestyle="--")
ax.axvline(sales[sales["channel"] == worst]["amount"].median(),
           color="#0B1B3A", linestyle=":")
ax.set_title(f"{worst}: the long tail pulls the mean", loc="left", fontweight="bold")
plt.show()
```

The tail on the right is the espresso machine sales. There are few of them and they are very large,
and they are what separates the mean from the median.

### Exercise 5

```python
by_month = sales.pivot_table(index=sales["date"].dt.month, columns="region",
                             values="amount", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(by_month, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_title("Revenue by month and region, in thousands", loc="left", fontweight="bold")
ax.set_ylabel("Month")
plt.show()

print("The highest cell:", by_month.stack().idxmax(), round(by_month.stack().max()))

# The highest cell is December in the north, and it does not surprise me after
# session 15.3: December carried 20 % of the year and the north is the largest
# region by volume. What does surprise me is how far it stands out from everything
# else.
```

`stack()` flattens the grid into a Series with a two-level index, so `idxmax` returns the cell as a
pair of labels.

### Exercise 6

```python
r = sales["units"].corr(sales["unit_price"])

fig, ax = plt.subplots(figsize=(8, 4.5))
sns.regplot(data=sales, x="units", y="unit_price",
            scatter_kws={"alpha": 0.4}, line_kws={"color": "#B4530A"}, ax=ax)
ax.set_title(f"Correlation of {r:.2f}: the line explains nothing",
             loc="left", fontweight="bold")
plt.show()

# The cloud shows as horizontal bands, one per product, because unit_price only
# takes fifteen distinct values. A line fitted over bands does not describe a
# relationship, it describes an average of things that are not alike. On top of
# that the correlation is near zero, so the line is practically flat and still
# gets drawn, which is exactly the problem: regplot always gives you a line.
```

That is the reflex worth taking away: the line always appears, and deciding whether it means
anything is on you.

### Exercise 7

There is no published solution, because it is about your own project. It is graded on all six being
answered in writing and the "no" answers being fixed rather than hidden.

### Exercise 8

There is no published solution. It is graded on three things: that there are exactly two charts,
that each has its finding and its shape justified in writing, and that both alternative texts can be
checked against the data.
'''),

]

write(OUT / "en" / "w16.2.ipynb", en)
print("wrote", OUT / "en" / "w16.2.ipynb")
