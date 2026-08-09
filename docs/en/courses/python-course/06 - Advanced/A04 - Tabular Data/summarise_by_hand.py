# Same file, same questions a spreadsheet answers with SUM, AVERAGE and a
# PivotTable. Written by hand, with nothing but the standard library.
#
# The point of this script is not that you should work this way. It is that
# after writing it once, every pandas line in the next module has an obvious
# meaning, because you already know what it replaced.

import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with (DATA / "sales.csv").open(encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

print(f"Records in the file: {len(rows)}")


# ────────────────────────────────────────────────────────────── the conversions

def to_int(text):
    text = text.strip()
    return int(text) if text else 0


def to_float(text):
    return float(text.replace("$", "").replace(",", "").strip())


# The region column was captured inconsistently: "North", "north", "NORTH" and
# " North" all mean the same place. Left alone, the grouping below reports four
# regions that do not exist. Trimming and title-casing folds them back together.
def clean_region(text):
    return text.strip().title()


# Build one clean record per row, with the totals already computed.
records = []
for row in rows:
    units = to_int(row["units"])
    price = to_float(row["unit_price"])
    records.append({
        "date": row["date"],
        "region": clean_region(row["region"]),
        "channel": row["channel"],
        "product": row["product"],
        "units": units,
        "amount": units * price,
    })


# ─────────────────────────────────────────────────────────── the duplicated rows

# Seven records were captured twice. A sum over the raw file overstates the year.
# A record counts as duplicated when every one of its fields matches another.
seen = set()
unique = []
for record in records:
    key = tuple(record.values())
    if key not in seen:
        seen.add(key)
        unique.append(record)

print(f"Records after removing duplicates: {len(unique)}")
print(f"Duplicated rows dropped: {len(records) - len(unique)}")


# ──────────────────────────────────────────────────────────── SUM and AVERAGE

amounts = [record["amount"] for record in unique]

total = sum(amounts)
average = total / len(amounts)
biggest = max(amounts)

print(f"\nTotal for the year:  {total:>14,.2f}")
print(f"Average per sale:    {average:>14,.2f}")
print(f"Largest single sale: {biggest:>14,.2f}")


# ───────────────────────────────────────────────────── the PivotTable, by hand

# A PivotTable does two things: it groups rows that share a value, and it
# aggregates each group. A dictionary does the grouping, and a loop aggregates.
#
# defaultdict(float) means a key that has not been seen starts at 0.0, so the
# first += works without checking whether the key already exists.
by_region: defaultdict[str, float] = defaultdict(float)
units_by_region: defaultdict[str, int] = defaultdict(int)

for record in unique:
    by_region[record["region"]] += record["amount"]
    units_by_region[record["region"]] += record["units"]

print("\nSales by region")
print(f"{'Region':<10}{'Amount':>16}{'Units':>10}{'Share':>9}")
for region, amount in sorted(by_region.items(), key=lambda pair: -pair[1]):
    share = amount / total
    print(f"{region:<10}{amount:>16,.2f}{units_by_region[region]:>10}{share:>8.1%}")


# ────────────────────────────────────────────────────── two levels of grouping

# A PivotTable with a second field is the same idea with a tuple as the key.
by_region_channel: defaultdict[tuple[str, str], float] = defaultdict(float)
for record in unique:
    by_region_channel[(record["region"], record["channel"])] += record["amount"]

print("\nSales by region and channel")
for (region, channel), amount in sorted(by_region_channel.items()):
    print(f"{region:<10}{channel:<12}{amount:>16,.2f}")


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. Grouping is a dictionary. The key is what you group by, the value is what
#    you accumulate. Everything a PivotTable does starts here.
# 2. The cleaning came before the arithmetic, and it had to. A sum over dirty
#    data returns a number, and that number is wrong without warning you.
# 3. This file is about eighty lines. The next module does the same work in
#    about eight, and that is the entire argument for pandas.
