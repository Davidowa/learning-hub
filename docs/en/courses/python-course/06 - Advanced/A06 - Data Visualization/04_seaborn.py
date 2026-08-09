# seaborn sits on top of matplotlib and takes a DataFrame directly.
#
# The trade is worth understanding. matplotlib asks you for x values and y
# values; seaborn asks you which columns to use and works the grouping out for
# itself. That makes the common statistical charts one line each, and it means
# you drop back to matplotlib whenever you need control it does not offer.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

sales = pd.read_csv(DATA / "sales_clean.csv", parse_dates=["date"])
employees = pd.read_csv(DATA / "employees.csv")

# A theme sets the defaults for every chart that follows: grid, fonts, palette.
# Setting it once at the top is why seaborn charts look consistent.
sns.set_theme(style="whitegrid", palette="deep")


# ──────────────────────────────────────────── barplot: it aggregates for you

# Given raw rows, seaborn groups by the x column and shows the mean of y, with a
# bar for the confidence interval. That default surprises people who expected a
# total, so say which summary you want: estimator="sum".
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

sns.barplot(data=sales, x="region", y="amount", estimator="sum",
            errorbar=None, ax=axes[0], hue="region", legend=False)
axes[0].set_title("Total revenue by region", loc="left", fontweight="bold")
axes[0].set_ylabel("Revenue")

sns.barplot(data=sales, x="region", y="amount", estimator="mean",
            errorbar=None, ax=axes[1], hue="region", legend=False)
axes[1].set_title("Average sale by region", loc="left", fontweight="bold")
axes[1].set_ylabel("Revenue per sale")

# The two charts rank the regions differently, and that difference is the
# finding: one region sells often, another sells big.
fig.tight_layout()
fig.savefig(OUT / "04_sum_versus_mean.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 04_sum_versus_mean.png")


# ─────────────────────────────────────────── hue: a third variable, for free

# hue splits the data by a column and gives each value its own colour, with the
# legend built for you. In matplotlib this is a loop; here it is one argument.
monthly = (sales.assign(month=sales["date"].dt.month)
           .groupby(["month", "channel"], as_index=False)["amount"].sum())

fig, ax = plt.subplots(figsize=(11, 5.5))
sns.lineplot(data=monthly, x="month", y="amount", hue="channel",
             marker="o", linewidth=2, ax=ax)
ax.set_title("Revenue by channel through the year", loc="left", fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_xticks(range(1, 13))
fig.savefig(OUT / "04_lineplot_hue.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 04_lineplot_hue.png")


# ────────────────────────────────────────── boxplot: the shape behind an average

# A bar chart of averages hides everything about the spread. A box shows the
# median, the middle half of the values, the range and the outliers, so two
# groups with the same average stop looking identical.
fig, ax = plt.subplots(figsize=(11, 5.5))
order = (employees.groupby("area")["monthly_salary"].median()
         .sort_values(ascending=False).index)

sns.boxplot(data=employees, x="area", y="monthly_salary", order=order,
            hue="area", legend=False, ax=ax)
ax.set_title("Salary spread by area, not just the average", loc="left",
             fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("Monthly salary")
fig.savefig(OUT / "04_boxplot.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 04_boxplot.png")


# ──────────────────────────────────── heatmap: a PivotTable with the numbers shaded

# Feed it the grid that pivot_table produced and the colour does the ranking for
# you. annot writes the value into each cell, fmt controls how it is rounded.
grid = sales.pivot_table(index="region", columns="channel",
                         values="amount", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(grid, annot=True, fmt=".0f", cmap="Blues",
            cbar_kws={"label": "Thousands of pesos"}, ax=ax)
ax.set_title("Revenue by region and channel", loc="left", fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("")
fig.savefig(OUT / "04_heatmap.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 04_heatmap.png")


# ─────────────────────────────────────── the whole table, in one command

# pairplot draws every numeric column against every other one. It is not a chart
# for a report. It is the first thing to run on a table you have never seen,
# because relationships and odd distributions show up immediately.
numeric = employees[["tenure_months", "monthly_salary"]]
grid_plot = sns.pairplot(numeric.assign(area=employees["area"]),
                         hue="area", height=2.6)
grid_plot.figure.suptitle("Every numeric column against every other",
                          y=1.02, fontweight="bold")
grid_plot.savefig(OUT / "04_pairplot.png", dpi=150, bbox_inches="tight")
plt.close(grid_plot.figure)
print("Wrote 04_pairplot.png")


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. seaborn takes the DataFrame and the column names. It does the grouping.
# 2. barplot shows the mean by default. Say estimator="sum" when you want totals.
# 3. hue is how a third variable enters a chart without writing a loop.
# 4. A boxplot shows what an average hides, and a heatmap is a PivotTable you
#    can read at a glance.
# 5. Every seaborn chart is still a matplotlib Axes, so all of module 03 applies.
