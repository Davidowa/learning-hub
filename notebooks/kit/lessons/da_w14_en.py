"""notebooks/analisis-de-datos/en/w14.ipynb

Source deck: ppts/python/analisis-de-datos/en/w14.en.yaml
Source code:  06 - Advanced/A04 - Tabular Data/
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

en = [

md("""
# Data Analysis · Week 14
## Text files and CSV

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

This is where data stops being typed by hand. Opening a file, reading it by column, converting it
and saving it again.

The argument of the session is that **a CSV has no types**. Week 4 said so; today you watch it
happen on a real file of 324 rows, and that is when it sticks.

By the end of this notebook you will be able to:

1. Open a file with `with`, and explain why that form closes it even when the program fails.
2. Recognise the four modes, and which one erases what was there.
3. Read a CSV by column name with `DictReader`.
4. Convert what arrives from the file, blank cells included.
5. Write an output file another program can open.

### About files in Colab

Everything this notebook writes stays in the session, next to the CSVs the setup cell brings in.
While the session is open they can be read again; when it closes they disappear.

To pull them down to your machine, the file panel on the left has a download option.

Six cells fail on purpose and carry a comment saying so.
"""),

md("""
---
## Setup
"""),

bootstrap_cell("en"),

md("""
---
# Block 1 · Opening a file

An open file is a borrowed resource. It has to be given back, and there is a form that makes that
happen on its own.
"""),

code("""
with open("sales.csv", encoding="utf-8") as f:
    first = f.readline()

print(first.strip())
"""),

md("""
Three things about that line.

**`with`.** On leaving the block the file closes itself, even if a line inside raises. It is why
this course never writes `open` without `with`.

**`encoding="utf-8"`.** Explicit. Without it a file with accents reads differently on Windows and
on Mac, and the error surfaces at row 200 of a file that opened fine on your machine.

**Outside the `with` the file is already closed.**
"""),

code("""
# FAILS ON PURPOSE. Reading after the with closed the file.
with open("sales.csv", encoding="utf-8") as f:
    pass

try:
    f.readline()
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
And `with` closes the file even when the block blows up, which is what makes it worth having.
"""),

code("""
# FAILS ON PURPOSE, and the file still ends up closed.
try:
    with open("sales.csv", encoding="utf-8") as f:
        f.readline()
        raise RuntimeError("something went wrong halfway")
except RuntimeError as e:
    print("RuntimeError:", e)

print("Did the file end up closed?", f.closed)
"""),

md("""
Without `with` you would need a `try` with a three-line `finally` to get the same.

## The three ways to read

| Form | What it returns | When |
|---|---|---|
| `f.read()` | The whole file as one string | Small files |
| `f.readline()` | One line | When you only want the header |
| `for line in f` | One line per pass | Whenever it is large |
"""),

code("""
with open("sales.csv", encoding="utf-8") as f:
    whole = f.read()

print("Characters:", len(whole))
print("Lines:     ", whole.count("\\n"))
print("The first 120:")
print(whole[:120])
"""),

code("""
with open("sales.csv", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= 3:
            break
        print(f"{i}: {line.rstrip()}")
"""),

md("""
Walking the file with a `for` reads one line at a time and never loads all 324 into memory. With
this file it makes no difference; with two million rows it is the difference between running and
not running.

That `.rstrip()` removes the newline every line carries on its end.

## The four modes

| Mode | What it does | If the file exists |
|---|---|---|
| `r` | Read, and it is the default | Opens it |
| `w` | Write from scratch | **Erases all its contents** |
| `a` | Append at the end | Keeps what was there |
| `x` | Create a new one | Fails with `FileExistsError` |

**Predict before you run.** What happens to the file when this runs?

- **A.** It reads the contents into the variable.
- **B.** It erases the file on opening and then fails to read.
- **C.** It fails because the file already exists.
- **D.** It adds a blank line at the end.
"""),

code("""
# FAILS ON PURPOSE, and destroys. I do it on a throwaway copy.
with open("throwaway.txt", "w", encoding="utf-8") as f:
    f.write("original contents worth gold\\n")

print("Before:", open("throwaway.txt", encoding="utf-8").read().strip())

try:
    with open("throwaway.txt", "w", encoding="utf-8") as f:
        contents = f.read()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

print("After:", repr(open("throwaway.txt", encoding="utf-8").read()))
"""),

md("""
The answer is **B**. Mode `w` **erases the contents the instant it opens**, before you get to read
anything. The file ended up empty and the `read` failed on top.

That is the most expensive error of the session, because there is no undo. Had `throwaway.txt`
been your project file, it would be gone.

The other three modes, on the same file:
"""),

code("""
with open("throwaway.txt", "w", encoding="utf-8") as f:
    f.write("first line\\n")

with open("throwaway.txt", "a", encoding="utf-8") as f:
    f.write("second line, appended\\n")

print(open("throwaway.txt", encoding="utf-8").read())

# FAILS ON PURPOSE. Mode x refuses to overwrite an existing file.
try:
    with open("throwaway.txt", "x", encoding="utf-8") as f:
        f.write("this never gets written")
except FileExistsError as e:
    print("FileExistsError:", e)
"""),

md("""
Mode `x` is the safety net: when overwriting something existing would be a disaster, `x` fails
instead of erasing.

## Paths
"""),

code("""
from pathlib import Path

here = Path.cwd()
print("We are in:", here)
print("Files here:", sorted(p.name for p in here.glob("*.csv")))
print()
print("Does sales.csv exist?", Path("sales.csv").exists())
print("Size:", Path("sales.csv").stat().st_size, "bytes")
"""),

md("""
`pathlib` builds paths that work on Windows, Mac and Linux unchanged. Writing
`C:\\Users\\your_name\\data.csv` by hand runs on no other machine, including the classroom one.

In a real script the path is built from the file's own location:

```python
DATA = Path(__file__).resolve().parent / "data"
```

A notebook has no `__file__`, so the files live in the working directory and get named directly.
"""),

md("""
---
# Block 2 · Reading a CSV

The format any spreadsheet exports and any tool reads. Plain text, separated by commas.

You could split it by hand, and you should not.
"""),

code("""
# FAILS ON PURPOSE the moment a field carries a comma inside it.
line = '2025-12-08,South,Online,"Bean, subscription",15,"$ 1,690.00"'

print("Splitting with split:", line.split(","))
print()
print("That gave", len(line.split(",")), "fields and it should be 6.")
"""),

md("""
The `csv` module knows the rules: quotes, commas inside quotes, newlines inside a field. Splitting
with `split` works until a product is called "Coffee, roasted".
"""),

code("""
import csv, io

reader = csv.reader(io.StringIO(line))
print("With the csv module:", next(reader))
"""),

md("""
## By position, or by name
"""),

code("""
# By position: it breaks the moment somebody inserts a column.
with open("sales.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    first_row = next(reader)

print("Header:", header)
print("Region by position:", first_row[1])
"""),

code("""
# By name: it uses the header, and survives a reordered file.
with open("sales.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("Rows:", len(rows))
print("The first:", rows[0])
print()
print("Region by name:", rows[0]["region"])
"""),

md("""
`DictReader` turns every row into a dictionary, with the header as keys. It is week 13 applied to
a file.

The `list(...)` matters: without it you can only walk once, because the reader advances and does
not come back.
"""),

code("""
# FAILS ON PURPOSE. Without list, the second walk finds nothing.
with open("sales.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    first_pass = sum(1 for _ in reader)
    second_pass = sum(1 for _ in reader)

print("First pass: ", first_pass)
print("Second pass:", second_pass, "<- the reader already hit the end")
"""),

md("""
## What the file hands over
"""),

code("""
print("The value:", rows[0]["units"])
print("Its type: ", type(rows[0]["units"]))
print()
for field, value in rows[0].items():
    print(f"  {field:<12} {value!r:<22} {type(value).__name__}")
"""),

md("""
**Everything is text.** The date, the region, the units and the price. The file stores no types
because a CSV has nowhere to store them.

It is exactly what week 4 announced, now with 324 real rows.
"""),

code("""
# FAILS ON PURPOSE. Adding text concatenates.
wrong_total = ""
for row in rows[:5]:
    wrong_total += row["units"]

print("Adding without converting:", wrong_total)
print("Converted:", sum(int(r["units"]) for r in rows[:5]))
"""),

md("""
## The dirt in the real file
"""),

code("""
regions = [r["region"] for r in rows]
blanks = sum(1 for r in rows if r["units"].strip() == "")

print("Distinct regions:", len(set(regions)), "and the company has four")
print(sorted(set(regions)))
print()
print("Blank units cells:", blanks)
"""),

md("""
Eight regions where there are four, and eleven blank cells. A real file always arrives dirty, and
that is not a defect of this file: it is normal.
"""),

md("""
---
# Block 3 · Converting and saving

The file hands over text. Deciding what each thing was, and what to do with what is missing, is
your job.
"""),

code("""
def to_int(text):
    \"\"\"Convert to an integer. A blank cell counts as zero.\"\"\"
    text = text.strip()
    return int(text) if text else 0


def to_float(text):
    \"\"\"Convert a currency-formatted price to a decimal.\"\"\"
    clean = text.replace("$", "").replace(",", "")
    return float(clean.strip())


def clean_region(text):
    \"\"\"Strip spaces and normalise capitals, so North and north become one.\"\"\"
    return text.strip().title()


print(to_int("15"), to_int(""), to_int("  22  "))
print(to_float("$ 2,082.50"), to_float("690.00"))
print(clean_region(" NORTH "), clean_region("north"))
"""),

md("""
Every cleaning rule in its own function, with its docstring. That way it can be tested on its own
and reused across the file, which is exactly week 10's argument.

**And there is a business decision written down there.** `to_int("")` returns zero: somebody
decided a blank cell means zero units. It could have been dropping the row, and that would also
be defensible.

What is not acceptable is not deciding.
"""),

code("""
# FAILS ON PURPOSE. Without the decision, int of an empty string blows up.
try:
    int("")
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
## Building the clean records
"""),

code("""
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
        "unit_price": price,
        "amount": units * price,
    })

print("Records:", len(records))
print("Regions now:", sorted({r["region"] for r in records}))
print("The first:", records[0])
"""),

md("""
Eight regions became four with a one-line function.

## The duplicates
"""),

code("""
seen = set()
unique = []
for r in records:
    key = tuple(r.values())
    if key not in seen:
        seen.add(key)
        unique.append(r)

print("Before:", len(records))
print("After: ", len(unique))
print("Duplicates removed:", len(records) - len(unique))
"""),

md("""
There is last week's set doing the work. A record counts as duplicated when **every** field matches
another, which is why the key is the tuple of all its values.

A tuple, not a list, because a list cannot live in a set.
"""),

code("""
total_with = sum(r["amount"] for r in records)
total_without = sum(r["amount"] for r in unique)

print(f"Total with duplicates:    {total_with:>16,.2f}")
print(f"Total without duplicates: {total_without:>16,.2f}")
print(f"Difference:               {total_with - total_without:>16,.2f}")
"""),

md("""
Two hundred and seventy-three thousand pesos of difference from seven repeated rows. Nobody reading
the total would know it was inflated, because a total does not say how many records it was computed
over.

## The summary by region
"""),

code("""
from collections import defaultdict

by_region = defaultdict(float)
units_region = defaultdict(int)

for r in unique:
    by_region[r["region"]] += r["amount"]
    units_region[r["region"]] += r["units"]

total = sum(by_region.values())

print(f"{'Region':<10}{'Amount':>16}{'Units':>9}{'Share':>9}")
print("-" * 44)
for region in sorted(by_region, key=by_region.get, reverse=True):
    print(f"{region:<10}{by_region[region]:>16,.2f}"
          f"{units_region[region]:>9}{by_region[region] / total:>9.1%}")
print("-" * 44)
print(f"{'Total':<10}{total:>16,.2f}")
"""),

md("""
`defaultdict(float)` is a dictionary where an unseen key starts at 0.0, so last week's `get(r, 0)`
is not needed.

Those twenty lines are a PivotTable done by hand. **Next week they are eight**, and they give
exactly the same four totals to the cent.

## Writing the result
"""),

code("""
with open("summary_by_region.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["region", "amount", "units", "share"])
    for region in sorted(by_region, key=by_region.get, reverse=True):
        writer.writerow([
            region,
            round(by_region[region], 2),
            units_region[region],
            round(by_region[region] / total, 4),
        ])

print("Written. Contents:")
print(open("summary_by_region.csv", encoding="utf-8").read())
"""),

md("""
That `newline=""` is not optional. **Without it, on Windows the file comes out with a blank line
between every row**, because the `csv` module already writes its own line ending and the system
adds another.

Check it.
"""),

code("""
# FAILS ON PURPOSE. Writing a CSV without the empty newline.
with open("extra_lines.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b"])
    writer.writerow(["1", "2"])

raw = open("extra_lines.csv", newline="", encoding="utf-8").read()
print("Without newline='':", repr(raw))

with open("fine.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b"])
    writer.writerow(["1", "2"])

print("With newline='':   ", repr(open("fine.csv", newline="", encoding="utf-8").read()))
"""),

md("""
On Colab, which runs Linux, both come out identical. On Windows the first carries `\\r\\r\\n` and
shows as blank lines when opened in Excel.

Since you do not know which machine your program will run on, `newline=""` always goes in.

## And with `DictWriter`, by name
"""),

code("""
with open("clean_records.csv", "w", newline="", encoding="utf-8") as f:
    fields = ["date", "region", "channel", "product", "units", "unit_price", "amount"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(unique)

print("Wrote", len(unique), "clean records")
print(open("clean_records.csv", encoding="utf-8").readline().strip())
print(open("clean_records.csv", encoding="utf-8").readlines()[1].strip())
"""),

md("""
`DictWriter` is `DictReader`'s counterpart: it takes dictionaries and uses `fieldnames` to decide
the column order.

With that the circle closes: you read a dirty file, cleaned it, summarised it, and wrote two files
anyone can open.

## Four file errors

**Opening in mode `w` to read.** It erases the contents the instant it opens.

**Paths written by hand.** They run on no other machine.

**Adding without converting.** It concatenates and the total comes out absurd without raising.

**Forgetting `newline` when writing.** A blank line between every row, on Windows.

You watched all four run.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Opening and reading

### Exercise 1 · The three ways

Read `regions.csv` all three ways: whole with `read`, the header with `readline`, and line by line
with a `for`. Print something different in each case.

### Exercise 2 · The mode that destroys

Create a file with three lines, open it in mode `a` and add a fourth, then prove with `x` that you
cannot create it again.

Do not use mode `w` on a file you care about.

### Exercise 3 · The file that does not exist

Provoke a `FileNotFoundError` and write a function `read_safely(path)` returning an empty list
instead of blowing up, and warning on screen.

## CSV

### Exercise 4 · By name

Read `employees.csv` with `DictReader` and print how many rows it has, the column names, and the
first full record.

### Exercise 5 · The types that arrive

For the first record of `employees.csv`, print every field with its type. Then convert the two
numeric ones and print them again with their new type.

### Exercise 6 · Your own cleaning function

Write `to_int_or_none(text)` returning `None` instead of zero when the cell is blank. Then compute
the average units both ways, with zero and with `None` discarded, and say which you would report.

It is the same decision as week 15.2, taken by hand.

## Summarising and writing

### Exercise 7 · Summary by channel

With the clean records, build a summary by channel rather than by region, with amount, units and
share. Write it to `summary_by_channel.csv`.

Check that the three channels add to the same total as the four regions.

### Exercise 8 · The cross-tab

Build a summary by region **and** channel at once, using a tuple as the dictionary key. Print it as
a table with regions down the rows and channels across the columns.

It is week 9's nested loop and week 13's compound key, together.

### Exercise 9 · Your own file, start to finish

Take the CSV you brought in week 1, read it with `DictReader`, convert at least two columns to the
right type, and produce a summary by category written to a new file.

No absolute paths. And delete a value from a cell: your program has to keep running and say what
it did with it.
"""),

md("""
---
## Three ideas to take away

**A file stores text.** You supply the types. It is week 4's lesson, now on a file of 324 rows with
seven duplicates worth two hundred and seventy-three thousand pesos.

**Read by column name.** Counting positions breaks the moment somebody inserts a column, and nobody
will warn you.

**What to do with what is missing is your decision.** Dropping, filling or ignoring give three
different answers, and all three have to be defensible.

Next session is pandas, which does in eight lines what you wrote by hand today. Having written it
is what later lets you read those eight lines and know what they are doing.
"""),

md('''
---
# Solutions

### Exercise 1

```python
with open("regions.csv", encoding="utf-8") as f:
    whole = f.read()
print("Characters:", len(whole))

with open("regions.csv", encoding="utf-8") as f:
    print("Header:", f.readline().strip())

with open("regions.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        print("  ", line.strip().split(",")[0])
```

The `next(f)` in the third skips the header without needing a counter. An open file behaves like a
sequence of lines, and `next` takes the following one.

### Exercise 2

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("one\\ntwo\\nthree\\n")

with open("test.txt", "a", encoding="utf-8") as f:
    f.write("four\\n")

print(open("test.txt", encoding="utf-8").read())

try:
    with open("test.txt", "x", encoding="utf-8") as f:
        f.write("never")
except FileExistsError as e:
    print("FileExistsError:", e)
```

Mode `a` kept the three lines and added the fourth. Mode `x` refused, which is exactly what you want
when overwriting something existing would be an accident.

### Exercise 3

```python
try:
    open("does_not_exist.csv", encoding="utf-8")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)


def read_safely(path):
    """Returns the CSV rows, or an empty list if the file is not there."""
    try:
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Notice: could not find {path}, carrying on with an empty list")
        return []


print(len(read_safely("sales.csv")), "rows")
print(len(read_safely("does_not_exist.csv")), "rows")
```

Returning an empty list instead of blowing up is a decision, not a convenience. It helps when the
file is optional; when it is required, letting it blow up is correct.

### Exercise 4

```python
with open("employees.csv", encoding="utf-8") as f:
    employees = list(csv.DictReader(f))

print("Rows:   ", len(employees))
print("Columns:", list(employees[0].keys()))
print("The first:", employees[0])
```

A hundred and twenty rows and six columns. `list(employees[0].keys())` gives the header names, which
is what `DictReader` used to build the keys.

### Exercise 5

```python
first = employees[0]

for field, value in first.items():
    print(f"{field:<16} {value!r:<20} {type(value).__name__}")

print()
months = int(first["tenure_months"])
salary = int(first["monthly_salary"])
print(f"tenure_months    {months!r:<20} {type(months).__name__}")
print(f"monthly_salary   {salary!r:<20} {type(salary).__name__}")
```

All six arrive as `str`, `employee_id` included, and that one **must** stay text: it is an
identifier with leading zeros, and converting it would lose the format. Week 4's lesson again.

### Exercise 6

```python
def to_int_or_none(text):
    """Integer, or None if the cell is blank."""
    text = text.strip()
    return int(text) if text else None


with_zero = [to_int(r["units"]) for r in rows]
with_none = [to_int_or_none(r["units"]) for r in rows]
measured = [u for u in with_none if u is not None]

print(f"Blank as zero:      {sum(with_zero) / len(with_zero):>8.2f} over {len(with_zero)}")
print(f"Blanks discarded:   {sum(measured) / len(measured):>8.2f} over {len(measured)}")

# I would report the second, saying it covers 313 of 324 records. Treating a blank
# as zero claims eleven sales moved zero units, and that is false: they were not
# captured. The gap is half a point in the average, which looks small until somebody
# uses it to project the year.
```

It is exactly the decision `dropna` against `fillna(0)` takes in week 15.2, taken here by hand and
with the same consequences.

### Exercise 7

```python
by_channel = defaultdict(float)
units_channel = defaultdict(int)

for r in unique:
    by_channel[r["channel"]] += r["amount"]
    units_channel[r["channel"]] += r["units"]

total_channel = sum(by_channel.values())

with open("summary_by_channel.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["channel", "amount", "units", "share"])
    for channel in sorted(by_channel, key=by_channel.get, reverse=True):
        writer.writerow([channel, round(by_channel[channel], 2),
                         units_channel[channel],
                         round(by_channel[channel] / total_channel, 4)])

print(open("summary_by_channel.csv", encoding="utf-8").read())
print("Same total as by region?", round(total_channel, 2) == round(total, 2))
```

Both totals agree because both summaries distribute exactly the same records, only grouped by a
different column. If they disagreed, some record would have fallen outside one of the two.

That check is free and worth leaving in.

### Exercise 8

```python
cross = defaultdict(float)
for r in unique:
    cross[(r["region"], r["channel"])] += r["amount"]

regions_sorted = sorted({r for r, _ in cross})
channels_sorted = sorted({c for _, c in cross})

print(f"{'Region':<10}" + "".join(f"{c:>16}" for c in channels_sorted) + f"{'Total':>16}")
for region in regions_sorted:
    row = [cross[(region, c)] for c in channels_sorted]
    print(f"{region:<10}" + "".join(f"{v:>16,.2f}" for v in row) + f"{sum(row):>16,.2f}")
```

The compound key is a tuple, and the two set comprehensions pull out the distinct regions and
channels without repeats.

Those twelve lines are the grid `pivot_table` produces in one statement in week 15.3, and the
numbers come out identical.

### Exercise 9

There is no published solution, because the file differs for everyone. It is graded on four things:
that it uses `DictReader` rather than positions, that the conversions sit in functions with
docstrings, that there is no absolute path anywhere, and that deleting a value leaves the program
running and saying what it decided about that cell.
'''),

]

write(OUT / "en" / "w14.ipynb", en)
print("wrote", OUT / "en" / "w14.ipynb")
