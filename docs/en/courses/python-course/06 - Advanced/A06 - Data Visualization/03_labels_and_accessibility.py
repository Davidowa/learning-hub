# Turning a correct chart into a chart somebody can read.
#
# Most of the work is not the data. It is the title that states the finding, the
# numbers a reader can parse without counting zeros, and the colours that still
# separate when the slide is projected badly or printed in grey.

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

sales = pd.read_csv(DATA / "sales_clean.csv", parse_dates=["date"])
monthly = sales.groupby(sales["date"].dt.month)["amount"].sum()

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# ────────────────────────────────────────────────── the title says the finding

# "Revenue by month" describes the axes, which the reader can already see.
# "December carried a fifth of the year" is what you actually found. A chart
# titled with its conclusion is read once; a chart titled with its axes is
# stared at until somebody explains it.

peak_month = monthly.idxmax()
peak_share = monthly.max() / monthly.sum()

fig, ax = plt.subplots(figsize=(11, 5.5))

bars = ax.bar(MONTHS, monthly.values, color="#C7D6E8", edgecolor="none")

# One bar carries the point, so one bar gets the strong colour. Colouring all
# twelve makes the reader hunt for the one that matters.
bars[peak_month - 1].set_color("#2B5F8F")

ax.set_title(f"December carried {peak_share:.0%} of the year's revenue",
             fontsize=15, fontweight="bold", loc="left", pad=18)

# The subtitle is where the description goes, now that the title says the point.
ax.text(0, 1.02, "Revenue by month, 2025", transform=ax.transAxes,
        fontsize=10.5, color="#5B6B84")


# ──────────────────────────────────────────────────── numbers a reader can parse

# 2567118.5 on an axis makes the reader count digits. A formatter turns the tick
# labels into something readable without touching the underlying values.
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
ax.set_ylabel("Revenue")
ax.set_ylim(bottom=0)

# Label the bar that matters, so its value does not have to be read off the axis.
ax.annotate(f"{monthly.max() / 1_000_000:.2f}M",
            xy=(peak_month - 1, monthly.max()),
            xytext=(0, 8), textcoords="offset points",
            ha="center", fontweight="bold", color="#2B5F8F")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.grid(axis="y", alpha=0.3)
ax.tick_params(axis="y", length=0)

# Say where the numbers came from. A chart with no source is an opinion.
fig.text(0.125, -0.02, "Source: sales_clean.csv, 306 records, 2025",
         fontsize=9, color="#5B6B84")

fig.savefig(OUT / "03_annotated.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 03_annotated.png")


# ───────────────────────────────────────────────── colour that survives greyscale

# Around one man in twelve has some form of colour blindness, and every chart
# eventually gets printed in black and white. Two defences:
#
#   1. Use a palette designed for it. Blue against orange separates for almost
#      everyone; red against green does not.
#   2. Do not let colour be the only signal. Line style, marker shape and a
#      direct label all survive being turned grey.

by_channel = sales.pivot_table(index=sales["date"].dt.month,
                               columns="channel", values="amount", aggfunc="sum")

SAFE = {"Retail": "#2B5F8F", "Online": "#B4530A", "Wholesale": "#5B6B84"}
STYLE = {"Retail": "-", "Online": "--", "Wholesale": ":"}
MARKER = {"Retail": "o", "Online": "s", "Wholesale": "^"}

fig, ax = plt.subplots(figsize=(11, 5.5))

for channel in by_channel.columns:
    ax.plot(MONTHS, by_channel[channel] / 1000,
            label=channel, color=SAFE[channel],
            linestyle=STYLE[channel], marker=MARKER[channel], linewidth=2)

    # A label at the end of the line beats a legend: the reader's eye never has
    # to leave the data to find out which line is which.
    ax.annotate(channel, xy=(11, by_channel[channel].iloc[-1] / 1000),
                xytext=(8, 0), textcoords="offset points",
                color=SAFE[channel], fontweight="bold", va="center")

ax.set_title("Wholesale drives the December peak", fontsize=15,
             fontweight="bold", loc="left", pad=18)
ax.text(0, 1.02, "Revenue by channel and month, thousands of pesos",
        transform=ax.transAxes, fontsize=10.5, color="#5B6B84")
ax.set_ylim(bottom=0)
ax.set_xlim(-0.4, 12.6)      # room on the right for the end labels
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

fig.savefig(OUT / "03_colour_safe.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Wrote 03_colour_safe.png")


# ──────────────────────────────────────────────────────── the alternative text

# A chart in a report or on a web page needs a text description for anyone using
# a screen reader. Write it as the sentence you would say out loud if the chart
# failed to load: what it shows, and what it shows you.
alt_text = (
    "Line chart of 2025 revenue by month for three sales channels, in thousands "
    "of pesos. Retail stays between 120 and 320 all year. Online swings between "
    "36 and 656 with no clear trend. Wholesale is the largest channel in ten of "
    "the twelve months and jumps from 322 in November to 1,611 in December, "
    "which is what produces the year-end peak."
)
print("\nAlt text for the second chart:")
print(alt_text)

# Write it against the chart, not from memory. Every number in the paragraph
# above can be checked against the table, and describing a trend the data does
# not show is the easiest way to make an accessible chart say something false.
print("\nThe numbers behind it:")
print((by_channel / 1000).round(0).to_string())


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. Title the chart with the finding, not with the axes.
# 2. Give one element the strong colour. If everything is emphasised, nothing is.
# 3. Format the tick labels. Nobody should have to count digits.
# 4. Never let colour carry the meaning alone. Add line style, markers or labels.
# 5. Cite the source, and write the alt text.
