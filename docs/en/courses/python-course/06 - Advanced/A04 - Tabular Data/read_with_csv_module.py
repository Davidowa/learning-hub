# A CSV file is the format every spreadsheet can export and every tool can read.
# Before reaching for a library, it is worth seeing what Python already gives you,
# because it explains what pandas is doing for you later.

# The csv module is part of the standard library. Nothing to install.
import csv
from pathlib import Path

# Build the path from the location of this file, not from where you launched it.
# Otherwise the script only works when the terminal happens to sit in the right folder.
DATA = Path(__file__).resolve().parent.parent / "data"


# ─────────────────────────────────────────────────────────── reading row by row

# csv.reader hands you each line as a plain list of strings.
with (DATA / "sales.csv").open(encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)          # the first line holds the column names
    first_row = next(reader)       # and the second is the first record

print("Header:", header)
print("First row:", first_row)

# Notice what came back. Every field is a string, including the units.
print("Type of the units field:", type(first_row[4]))

# That is the first thing to understand about a CSV: the file has no types.
# A spreadsheet guesses the format when it opens the file. Python does not guess.


# ────────────────────────────────────────────────────── reading by column name

# Counting positions (row[4]) breaks the moment somebody inserts a column.
# csv.DictReader uses the header, so you ask for the name instead.
with (DATA / "sales.csv").open(encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

print("\nRecords read:", len(rows))
print("First record:", rows[0])

# Now a field is reached by name, which survives a reordered file.
print("Region of the first record:", rows[0]["region"])


# ───────────────────────────────────────────────────────── converting the text

# To do arithmetic, the text has to become a number. Two fields need work here.
#
#   units       looks like "15", but a few records are empty
#   unit_price  looks like "$ 2,082.50": a currency symbol and a thousands comma
#
# int("") raises ValueError, and float("$ 2,082.50") raises it too, so both
# conversions need cleaning first.

def to_int(text):
    """Turn the units field into a number, treating a blank cell as zero."""
    text = text.strip()
    return int(text) if text else 0


def to_float(text):
    """Strip the currency symbol and the thousands separator, then convert."""
    return float(text.replace("$", "").replace(",", "").strip())


sample = rows[0]
units = to_int(sample["units"])
price = to_float(sample["unit_price"])

print("\nUnits as a number:", units, type(units))
print("Price as a number:", price, type(price))
print("Line total:", units * price)


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. A CSV file stores text. Types are your responsibility, not the file's.
# 2. Read by column name, not by position, so the code survives an edited file.
# 3. Every cleaning rule you write here is a rule pandas will write for you later,
#    but it will still be your decision what a blank cell means.
