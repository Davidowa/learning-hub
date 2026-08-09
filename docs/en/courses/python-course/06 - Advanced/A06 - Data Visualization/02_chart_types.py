# Which chart answers which question.
#
# Choosing the chart is not a style decision. Each shape answers one kind of
# question, and using the wrong one makes a true number say something false.
#
#   Bar      how do these categories compare?
#   Line     how did this change over time?
#   Scatter  do these two numbers move together?
#   Histogram how are the values spread out?

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

sales = pd.read_csv(DATA / "sales_clean.csv", parse_dates=["date"])
employees = pd.read_csv(DATA / "employees.csv")

BLUE = "#2B5F8F"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))


# ───────────────────────────────────── bar: comparing categories to each other

# Sorted, because an unsorted bar chart makes the reader do the ranking.
# Horizontal, because the category names are words and words read across.
by_product = sales.groupby("product")["amount"].sum().sort_values() / 1000

axes[0, 0].barh(by_product.index, by_product.values, color=BLUE)
axes[0, 0].set_title("Which product brings the most revenue?",
                     loc="left", fontweight="bold")
axes[0, 0].set_xlabel("Thousands of pesos")


# ───────────────────────────────────────────── line: change along an ordered axis

# A line implies the points are connected in a meaningful order. Never use one
# for categories: connecting North to South suggests a journey that is not there.
monthly = sales.groupby(sales["date"].dt.month)["amount"].sum() / 1000

axes[0, 1].plot(MONTHS, monthly.values, marker="o", linewidth=2, color=BLUE)
axes[0, 1].set_title("How did revenue move through the year?",
                     loc="left", fontweight="bold")
axes[0, 1].set_ylabel("Thousands of pesos")
axes[0, 1].set_ylim(bottom=0)


# ──────────────────────────────────── scatter: the relationship between two numbers

# One dot per row, positioned by two of its values. This is the chart that
# answers "does more of this come with more of that".
axes[1, 0].scatter(employees["tenure_months"], employees["monthly_salary"],
                   alpha=0.55, color=BLUE, edgecolor="none")
axes[1, 0].set_title("Does salary rise with tenure?", loc="left", fontweight="bold")
axes[1, 0].set_xlabel("Tenure in months")
axes[1, 0].set_ylabel("Monthly salary")

# The correlation puts a number on what the eye is doing. It runs from -1 to 1.
# A number near zero means the cloud has no direction, and a strong number still
# does not mean one caused the other.
r = employees["tenure_months"].corr(employees["monthly_salary"])
axes[1, 0].annotate(f"correlation = {r:.2f}", xy=(0.04, 0.92),
                    xycoords="axes fraction", fontsize=10, color="#5B6B84")


# ─────────────────────────────────── histogram: how one column is distributed

# A histogram slices one column into ranges and counts how many rows land in
# each. It answers "what does typical look like, and how wide is the spread".
# A bar chart compares named things; a histogram compares ranges of one thing.
axes[1, 1].hist(employees["monthly_salary"], bins=15, color=BLUE,
                edgecolor="white")
axes[1, 1].set_title("How are salaries spread out?", loc="left", fontweight="bold")
axes[1, 1].set_xlabel("Monthly salary")
axes[1, 1].set_ylabel("Employees")

# The average alone hides the shape. Drawing it on top shows how much it hides.
mean_salary = employees["monthly_salary"].mean()
axes[1, 1].axvline(mean_salary, color="#B4530A", linestyle="--", linewidth=2)
axes[1, 1].annotate(f"mean {mean_salary:,.0f}", xy=(mean_salary, 0),
                    xytext=(6, 6), textcoords="offset points",
                    color="#B4530A", fontsize=10)


for ax in axes.flat:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(OUT / "02_chart_types.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 02_chart_types.png")
print(f"Correlation between tenure and salary: {r:.3f}")


# ──────────────────────────────────────────────────────── the one to avoid

# A pie chart asks the reader to compare angles, which people do badly. Past
# three slices it becomes unreadable, and the same numbers as a sorted bar chart
# are understood at a glance. Draw both once and the difference is obvious.
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

shares = sales.groupby("product")["amount"].sum().sort_values(ascending=False)

axes[0].pie(shares.values, labels=shares.index, autopct="%1.0f%%",
            startangle=90, colors=plt.cm.Blues(range(60, 260, 40)))
axes[0].set_title("As a pie: which two are closest?", loc="left", fontweight="bold")

axes[1].barh(shares.sort_values().index, shares.sort_values().values / 1000,
             color=BLUE)
axes[1].set_title("As bars: now you can tell", loc="left", fontweight="bold")
axes[1].set_xlabel("Thousands of pesos")
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(OUT / "02_pie_versus_bar.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 02_pie_versus_bar.png")


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. Pick the chart from the question, not from the menu.
# 2. Sort the bars. An unsorted bar chart makes the reader rank them.
# 3. A line means the order matters. Do not use one across categories.
# 4. A histogram shows one column's shape; a bar chart compares named things.
# 5. Correlation is not causation, and a pie chart is almost never the answer.
