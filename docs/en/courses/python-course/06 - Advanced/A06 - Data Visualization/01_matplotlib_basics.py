# A chart is an argument. Everything in this module exists to make the argument
# readable by somebody who was not in the room when you made it.
#
# matplotlib is the library everything else is built on. Learning its two
# objects first means the rest of the ecosystem stops looking like magic.

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

sales = pd.read_csv(DATA / "sales_clean.csv", parse_dates=["date"])
monthly = sales.groupby(sales["date"].dt.month)["amount"].sum()


# ─────────────────────────────────────────────────────────────── the two objects

# A Figure is the sheet of paper. An Axes is one set of axes drawn on it.
# subplots() hands you both at once, and that is how nearly every chart starts.
fig, ax = plt.subplots(figsize=(10, 5))

# The Axes is what you draw on.
ax.plot(monthly.index, monthly.values)

# Save the figure, not the axes. dpi controls how sharp the file comes out;
# 150 is enough for a slide, 300 for print. bbox_inches trims the white margin.
fig.savefig(OUT / "01_first_chart.png", dpi=150, bbox_inches="tight")
print("Wrote 01_first_chart.png")

# When you run this on your own machine, plt.show() opens the chart in a window
# instead of writing a file. It is left out here so the script finishes on its
# own, which is what you want when it runs as part of something larger.

# Close the figure when you are done. Left open, a loop that draws fifty charts
# keeps all fifty in memory and matplotlib eventually warns you about it.
plt.close(fig)


# ─────────────────────────────────────────────────────── a chart worth reading

# The chart above is technically correct and says nothing. It has no title, the
# axis numbers are unlabelled, and the reader has to guess what 1 to 12 means.
# The same data, told properly:

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(MONTHS, monthly.values / 1000, marker="o", linewidth=2, color="#2B5F8F")

ax.set_title("Revenue by month, 2025", fontsize=14, fontweight="bold", loc="left")
ax.set_ylabel("Thousands of pesos")
ax.set_ylim(bottom=0)          # a bar or line chart starts at zero, or it lies

# Strip the frame down to the two lines that carry meaning. Everything removed
# here is ink that was not saying anything.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

fig.savefig(OUT / "01_readable_chart.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 01_readable_chart.png")


# ─────────────────────────────────────────────────────── several charts at once

# subplots takes a grid. The Axes come back as an array you index into.
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

by_region = sales.groupby("region")["amount"].sum().sort_values()
by_channel = sales.groupby("channel")["amount"].sum().sort_values()

axes[0].barh(by_region.index, by_region.values / 1000, color="#3776AB")
axes[0].set_title("By region", loc="left", fontweight="bold")
axes[0].set_xlabel("Thousands of pesos")

axes[1].barh(by_channel.index, by_channel.values / 1000, color="#3776AB")
axes[1].set_title("By channel", loc="left", fontweight="bold")
axes[1].set_xlabel("Thousands of pesos")

for ax in axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# tight_layout keeps the two charts from overlapping each other's labels.
fig.tight_layout()
fig.savefig(OUT / "01_two_panels.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 01_two_panels.png")


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. fig, ax = plt.subplots() is how a chart starts. Draw on the ax, save the fig.
# 2. A chart with no title and no axis label is not finished.
# 3. Bars and lines start at zero. Cutting the axis exaggerates the difference,
#    and doing it on purpose is how charts lie.
# 4. Close each figure when you are done with it.
