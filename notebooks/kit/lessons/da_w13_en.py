"""notebooks/analisis-de-datos/en/w13.ipynb

Source deck: ppts/python/analisis-de-datos/en/w13.en.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

en = [

md("""
# Data Analysis · Week 13
## Sets and dictionaries · Second midterm

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

The dictionary is the highest-return piece in the whole course. It is the `VLOOKUP`, and in week
15 it is what `groupby` does underneath.

By the end of this notebook you will be able to:

1. Create and query a dictionary, by key and with `get`.
2. Walk keys, values and pairs with `keys`, `values` and `items`.
3. Remove duplicates with a set, in one line.
4. Use the four set operations.
5. Choose the right collection by the question it will answer.

### The second midterm

| Aspect | Detail |
|---|---|
| Content | Units 4, 5 and 6: repetition, functions and collections |
| Weight | 20 % of the final grade |
| Format | On the classroom computer, uploaded zipped to Blackboard |
| You may bring | Notes, assignments, books and anything you generated with AI beforehand |
| You may not | Phone, headphones, AI glasses or messaging |

### How to use this notebook

Run the cells in order. Five fail on purpose and carry a comment saying so.
"""),

md("""
---
# Block 1 · The dictionary

A two-column table where the first column is unique. It is what you look up with `VLOOKUP`,
without the column number.

In the sheet you would write:

```
=VLOOKUP(B2, Catalogue, 2, FALSE)
```

Three arguments and you have to count which column holds what you want. In Python:
"""),

code("""
rates = {"AAA": 0.12, "AA": 0.18, "A": 0.24, "B": 0.32}

print(rates)
print("The AA rate:", rates["AA"])
"""),

md("""
To the left of the colon the **key**, to the right the **value**. Keys do not repeat, and access
uses brackets just like a list, except the index is the key instead of a number.

Column number three does not exist because it is not needed. And unlike `VLOOKUP`, adding a rating
dislodges nothing.

## When the key is not there
"""),

code("""
# FAILS ON PURPOSE. A key that is not there.
try:
    print(rates["C"])
except KeyError as e:
    print("KeyError:", e)
"""),

md("""
`KeyError` stops the program right there. When the key may be missing, `get` is the way out.
"""),

code("""
print("get with no default: ", rates.get("C"))
print("get with a default:  ", rates.get("C", 0.40))
print("get on one that exists:", rates.get("AA"))
"""),

md("""
`get` returns `None` when the key is missing instead of blowing up, and it takes a default.

**Which to use.** Brackets when the key *has* to be there and its absence is an error you want to
see. `get` when absence is normal and you have a sensible fallback.
"""),

code("""
# A customer with no recorded rating pays the highest rate.
RATINGS = {"Insumos SA": "AAA", "Papelera": "A", "Log Express": "B"}
UNRATED_RATE = 0.40

for customer in ["Insumos SA", "Papelera", "New Customer"]:
    rating = RATINGS.get(customer, "unrated")
    rate = rates.get(rating, UNRATED_RATE)
    print(f"{customer:<15} {rating:<10} {rate:.0%}")
"""),

md("""
Two chained `get` calls and no `if`. The new customer lands on the fallback rate without the
program stopping.

## Walking a dictionary

| Method | What it hands over | When it is used |
|---|---|---|
| `keys` | Only the keys | When knowing which ones exist is enough |
| `values` | Only the values | To sum or average |
| `items` | The full pairs | To print the whole table |
"""),

code("""
print("Keys:  ", list(rates.keys()))
print("Values:", list(rates.values()))
print("Pairs: ", list(rates.items()))
"""),

code("""
for key, value in rates.items():
    print(f"{key:<4} {value:.0%}")
"""),

md("""
`items` hands over a tuple per pass and the `for` unpacks it, exactly like last week's `zip`.

And with `values` the usual functions work as always.
"""),

code("""
values = list(rates.values())

print("Average rate:", f"{sum(values) / len(values):.2%}")
print("The highest: ", f"{max(values):.0%}")
print("The lowest:  ", f"{min(values):.0%}")
"""),

md("""
## Modifying

Assigning to an existing key overwrites it. Assigning to a missing one creates it. **It is the
same line.**

**Predict before you run.** What does the last line print?

- **A.** 4, because two entries were added.
- **B.** 3, because North already existed and got overwritten.
- **C.** 2, because the dictionary does not grow.
- **D.** An error, because East did not exist.
"""),

code("""
count = {"North": 3, "South": 1}
count["North"] = 5
count["East"] = 2

print(count)
print(len(count))
"""),

md("""
The answer is **B**, three. `count["North"] = 5` overwrote and `count["East"] = 2` created.

That it is the same syntax is convenient and dangerous: a typo in a key name raises nothing, it
creates a new entry.
"""),

code("""
# FAILS ON PURPOSE. A typo in the key creates an entry, not an error.
inventory = {"Espresso": 42, "Grinder": 18}
inventory["Esprseso"] = 50      # typo

print(inventory)
print("Now there are", len(inventory), "products, and one does not exist.")
"""),

md("""
It is the same problem as the eight regions in `sales.csv`. A dictionary does not validate its
keys, so the validation has to live somewhere else.
"""),

code("""
VALID_PRODUCTS = {"Espresso", "Grinder", "Kettle"}

def register(inventory, product, quantity):
    \"\"\"Adds to the inventory, rejecting products outside the catalogue.\"\"\"
    if product not in VALID_PRODUCTS:
        return f"'{product}' is not in the catalogue"
    inventory[product] = quantity
    return f"{product}: {quantity}"


inv = {}
print(register(inv, "Espresso", 42))
print(register(inv, "Esprseso", 50))
print("Inventory:", inv)
"""),

md("""
## Counting with a dictionary

This is the pattern you will use most, and it is what pandas' `value_counts` does underneath.
"""),

code("""
regions = ["North", "Centre", "North", "South", "Centre", "North"]

count = {}
for r in regions:
    count[r] = count.get(r, 0) + 1

print(count)
"""),

md("""
The `count.get(r, 0) + 1` is the whole line: if the region was already there, add one to what was
there; if not, start at zero and add one.

Without `get` you would need an `if` for each region's first appearance.
"""),

code("""
# The same thing, with the tool that already exists for it.
from collections import Counter

print(Counter(regions))
print(Counter(regions).most_common(2))
"""),

md("""
`Counter` is a dictionary specialised in counting, and `most_common` gives the most frequent ones
already ordered. It is literally what `value_counts` returns in week 15.
"""),

md("""
---
# Block 2 · The set

Distinct values, no duplicates and no order. It is removing duplicates in one line.
"""),

code("""
regions = ["North", "Centre", "North", "South", "Centre", "North"]

unique = set(regions)

print(sorted(unique))
print(len(unique), "distinct out of", len(regions), "records")
"""),

md("""
That line replaces the loop with a helper list that almost everyone writes the first time:
"""),

code("""
# The long version, so you can see what the set saves you.
seen = []
for r in regions:
    if r not in seen:
        seen.append(r)

print(seen)
"""),

md("""
Both give the same thing with six elements. With three hundred thousand, the set version is
incomparably faster, because asking `x in set` is immediate and `x in list` walks.
"""),

code("""
import time

big = list(range(20000))
as_set = set(big)

start = time.perf_counter()
19999 in big
t_list = time.perf_counter() - start

start = time.perf_counter()
19999 in as_set
t_set = time.perf_counter() - start

print(f"Searching the list: {t_list * 1e6:>8.1f} microseconds")
print(f"Searching the set:  {t_set * 1e6:>8.1f} microseconds")
"""),

md("""
The exact times change between runs and between machines. What does not change is which is faster,
and the gap grows with size.

That is why `VALID_PRODUCTS` above is a set and not a list.

## The four operations

| Operation | Symbol | What it returns |
|---|---|---|
| Union | `\\|` | What is in either of the two |
| Intersection | `&` | Only what is in both |
| Difference | `-` | What is in the first and not the second |
| Symmetric difference | `^` | What is in one but not in both |
"""),

code("""
this_year = {"North", "Centre", "South"}
last_year = {"Centre", "South", "East"}

print("Union:               ", sorted(this_year | last_year))
print("Intersection:        ", sorted(this_year & last_year))
print("Difference:          ", sorted(this_year - last_year))
print("The other way:       ", sorted(last_year - this_year))
print("Symmetric difference:", sorted(this_year ^ last_year))
"""),

md("""
Each one answers a different business question.

**Intersection**: which regions we operated in both years. **Difference**: which we opened this
year. **The difference reversed**: which we closed. **Symmetric difference**: where there was
movement, in either direction.

Note that `this_year - last_year` and `last_year - this_year` do **not** give the same thing.
Difference is not commutative, and confusing them reports openings as closures.
"""),

code("""
print("Opened:", sorted(this_year - last_year))
print("Closed:", sorted(last_year - this_year))
print("Are they equal?", (this_year - last_year) == (last_year - this_year))
"""),

md("""
## What a set does not have
"""),

code("""
# FAILS ON PURPOSE. A set has no positions.
try:
    print(unique[0])
except TypeError as e:
    print("TypeError:", e)

print("And its printed order is not to be trusted:", set(["b", "a", "c"]))
print("Which is why it gets sorted for display:", sorted(set(["b", "a", "c"])))
"""),

md("""
A set keeps no order, so it cannot be indexed or sliced. When you need to show it, `sorted` turns
it into an ordered list.

And it does not accept elements that can change.
"""),

code("""
# FAILS ON PURPOSE. A list cannot live inside a set.
try:
    {["North", "South"]}
except TypeError as e:
    print("TypeError:", e)

print("With a tuple it can:", {("North", "South"), ("Centre", "East")})
"""),

md("""
That is one of the practical reasons tuples exist: **a tuple can be an element of a set or a key
in a dictionary, and a list cannot.**
"""),

code("""
# A compound key: region and channel together.
sales_by_pair = {
    ("North", "Retail"): 1331426,
    ("North", "Online"): 978286,
    ("South", "Retail"): 271090,
}

print(sales_by_pair[("North", "Retail")])
for (region, channel), amount in sales_by_pair.items():
    print(f"{region:<8}{channel:<10}{amount:>12,}")
"""),

md("""
That is exactly what `groupby(["region", "channel"])` returns in week 15.3: a two-level index,
which underneath is tuples.
"""),

md("""
---
# Block 3 · Which one to use

Four collections and one question that decides between them.

| If you need | Use | Why |
|---|---|---|
| Order and duplicates | List | It is your table's column |
| Nobody to change it | Tuple | A contract's terms |
| Distinct values | Set | It removes duplicates by itself |
| Lookup by key | Dictionary | It is the `VLOOKUP`, and it is immediate |

All four, on the same data, to see what each keeps.
"""),

code("""
data = ["North", "Centre", "North", "South"]

print("List:      ", list(data), "· order yes, duplicates yes")
print("Tuple:     ", tuple(data), "· order yes, duplicates yes, cannot change")
print("Set:       ", sorted(set(data)), "· order no, duplicates no")
print("Dictionary:", {r: data.count(r) for r in set(data)}, "· unique key, free value")
"""),

md("""
That `{r: data.count(r) for r in set(data)}` is a **dictionary comprehension**, sibling of last
week's list one. It reads the same: "for each distinct `r`, the key is `r` and the value is how
many times it appears".

## All together: a campaign report
"""),

code("""
CAMPAIGNS = [
    ("Instagram", 38500), ("Google", 51200), ("Meta", 29800),
    ("Instagram", 12400), ("TikTok", 9600), ("Google", 18300),
]

# Dictionary: accumulate the spend per channel.
spend = {}
for channel, amount in CAMPAIGNS:
    spend[channel] = spend.get(channel, 0) + amount

for channel, amount in sorted(spend.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{channel:<12}{amount:>10,}")

print(f"{'Total':<12}{sum(spend.values()):>10,}")
"""),

code("""
# Set: which channels appear this year and not last.
this_year = set(spend)
last_year = {"Instagram", "Meta", "Radio", "Billboard"}

print("New this year:   ", sorted(this_year - last_year))
print("The ones dropped:", sorted(last_year - this_year))
print("The ones kept:   ", sorted(this_year & last_year))
"""),

md("""
Two new channels, two abandoned and two carried over. That `sorted(spend.items(), key=...)` in the
previous cell sorts a dictionary by its value, and it is the `key` you saw in week 11.

## Four collection errors

**Brackets where `get` belonged.** `KeyError` stops the program.

**Assuming a set keeps order.** It does not, and the order it shows can change between runs.

**Confusing the direction of a difference.** `a - b` and `b - a` answer opposite questions.

**A typo in a key.** It raises nothing, it creates a new entry.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Dictionaries

### Exercise 1 · Your catalogue

Build a dictionary translating a code from your field into its description or its value, with at
least six entries. Walk it with `items`, printing an aligned table.

### Exercise 2 · The lookup that does not blow up

Write a function `look_up(catalogue, key)` returning the value, or a message saying it does not
exist, without using `try`.

Test it with three keys that exist and two that do not.

### Exercise 3 · Counting without `Counter`

With a list of at least fifteen repeated values from your field, build a dictionary of counts using
`get`. Then print the most and least frequent.

Hint: `max(count, key=count.get)`.

### Exercise 4 · Summing by category

With a list of `(category, amount)` tuples, build a dictionary accumulating the amount per
category, and another counting how many records there are of each.

Print both tables and the average per category.

## Sets

### Exercise 5 · The distinct ones

With the list from exercise 3, print how many distinct values there are, which ones in order, and
how many appear exactly once.

### Exercise 6 · The four operations

Build two sets with the suppliers from two different years and answer with the four operations:
which carried over, which arrived, which left, and where there was movement.

Prove in code that `a - b` is not the same as `b - a`.

### Exercise 7 · Why the tuple

Prove that a list cannot be an element of a set and a tuple can. Then build a dictionary with keys
made of two values and walk it, unpacking the key.

## Choosing

### Exercise 8 · The right collection

For each, say in a comment which collection you would use and why: this month's invoice numbers,
the postal-code-to-city catalogue, the ratings a customer has held in order, the products sold
today without repeats, and a branch's coordinates.

### Exercise 9 · A catalogue with everything

Bring all four together: a list of records, a dictionary catalogue, a set for the distinct ones,
and a tuple for something that must not change. Produce a five-line report.

The catalogue lookup has to use `get` with a default, and the program has to keep running when
handed a key that does not exist.
"""),

md("""
---
## Three ideas to take away

**A dictionary is a `VLOOKUP`.** The key, the value, and no column number three. In week 15 this is
what `groupby` does underneath.

**`get` does not blow up.** Brackets raise `KeyError` on a missing key, and `get` returns whatever
you decide.

**A set removes duplicates by itself.** One line replaces the loop with a helper list, and searching
inside it is immediate rather than a walk.

Next session is files. That is where data stops being typed by hand and starts being read for real.
"""),

md('''
---
# Solutions

### Exercise 1

```python
AREAS = {
    "SLS": "Sales", "MKT": "Marketing", "FIN": "Finance",
    "HRS": "People", "OPS": "Operations", "LEG": "Legal",
}

print(f"{'Code':<8}{'Area'}")
print("-" * 24)
for code, name in AREAS.items():
    print(f"{code:<8}{name}")
```

Dictionaries have kept insertion order since Python 3.7. Before that they did not, which is why
older code still sorts the keys just in case.

### Exercise 2

```python
def look_up(catalogue, key):
    """Returns the value, or a notice if the key is not there."""
    return catalogue.get(key, f"'{key}' is not in the catalogue")


for c in ["SLS", "FIN", "OPS", "XYZ", ""]:
    print(f"{c!r:<8} -> {look_up(AREAS, c)}")
```

Not a single `try`. `get` with a default covers the missing case, and the default can be anything,
including a message built from the key itself.

### Exercise 3

```python
channels = ["Instagram", "Google", "Instagram", "Meta", "Google", "Instagram",
            "TikTok", "Meta", "Google", "Instagram", "LinkedIn", "Google",
            "Meta", "Instagram", "TikTok"]

count = {}
for c in channels:
    count[c] = count.get(c, 0) + 1

print(count)
print("Most frequent: ", max(count, key=count.get), "with", max(count.values()))
print("Least frequent:", min(count, key=count.get), "with", min(count.values()))
```

`max(count, key=count.get)` walks the keys and compares by their value. Without the `key` it would
compare the keys as text and return the last one alphabetically.

### Exercise 4

```python
RECORDS = [
    ("Retail", 12400), ("Online", 38500), ("Retail", 8900),
    ("Wholesale", 51200), ("Online", 18300), ("Wholesale", 29800),
    ("Retail", 5600),
]

amount = {}
how_many = {}
for category, value in RECORDS:
    amount[category] = amount.get(category, 0) + value
    how_many[category] = how_many.get(category, 0) + 1

print(f"{'Category':<12}{'Amount':>12}{'Records':>10}{'Average':>12}")
for cat in amount:
    print(f"{cat:<12}{amount[cat]:>12,}{how_many[cat]:>10}"
          f"{amount[cat] / how_many[cat]:>12,.2f}")
```

Two dictionaries filled in the same loop. It is week 9's accumulator and counter, one per category
instead of one global.

And it is exactly what `groupby("category").agg(["sum", "count", "mean"])` does in one line in week
15.3.

### Exercise 5

```python
distinct = set(channels)

print("How many distinct:", len(distinct))
print("Which ones:", sorted(distinct))
print("Appear exactly once:", sorted(c for c in distinct if channels.count(c) == 1))
```

Only LinkedIn appears once. Note that `channels.count(c)` walks the whole list once per distinct
channel: with fifteen elements it makes no difference, and with a million you would use the count
dictionary from exercise 3.

### Exercise 6

```python
this_year = {"Insumos SA", "Papelera", "Log Express", "Cafés del Sur"}
last_year = {"Papelera", "Log Express", "Empaques MX", "Tinta y Papel"}

print("Carried over:", sorted(this_year & last_year))
print("Arrived:     ", sorted(this_year - last_year))
print("Left:        ", sorted(last_year - this_year))
print("Movement:    ", sorted(this_year ^ last_year))
print()
print("Is a - b the same as b - a?", (this_year - last_year) == (last_year - this_year))
```

Two carried over, two arrived, two left. The symmetric difference gathers the four that moved,
which is the list whoever reviews the supplier book cares about.

### Exercise 7

```python
try:
    {["a", "b"]}
except TypeError as e:
    print("With a list ->", e)

print("With a tuple ->", {("a", "b"), ("c", "d")})

sales = {
    ("North", "2025"): 4351976,
    ("North", "2024"): 3980112,
    ("South", "2025"): 1553003,
}

for (region, year), amount in sorted(sales.items()):
    print(f"{region:<8}{year:<7}{amount:>12,}")
```

The technical reason is that a set and a dictionary need their elements not to change after being
stored, because they file them according to their contents. A list can change, and then it would
sit in the wrong place.

### Exercise 8

```python
# This month's invoice numbers -> set, if all you want is which exist and to spot
#   duplicates. List if the order of issue matters.
# Postal-code-to-city catalogue -> dictionary. The pure VLOOKUP.
# Ratings a customer has held, in order -> list. The order is the data: going from
#   B to AAA is not the same as the reverse.
# Products sold today without repeats -> set. That is literally its definition.
# A branch's coordinates -> tuple. Two numbers that travel together and do not change.
```

The first is the interesting one because it depends on the question. "How many distinct invoices?"
asks for a set; "in what order were they issued?" asks for a list. The question picks the
collection, not the data.

### Exercise 9

There is no published solution, because the catalogue differs for everyone. It is graded on four
things: that all four collections appear and each does something the others would do badly, that
the lookup uses `get` with a default, that the program keeps running on a missing key, and that the
report has a header and a total.
'''),

]

write(OUT / "en" / "w13.ipynb", en)
print("wrote", OUT / "en" / "w13.ipynb")
