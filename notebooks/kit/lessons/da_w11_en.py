"""notebooks/analisis-de-datos/en/w11.ipynb

Source deck: ppts/python/analisis-de-datos/en/w11.en.yaml
The Spanish half lives in da_w11.py; this week is split across two modules
because the lesson is long enough that one file was getting hard to navigate.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

en = [

md("""
# Data Analysis · Week 11
## Arguments, built-in functions and modules

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

Default and keyword arguments are what make a call with five parameters readable, and you will
see that all term in pandas and in matplotlib.

Modules are the door to week 15. Once you understand that `import` brings in tools from outside,
importing pandas stops being magic.

By the end of this notebook you will be able to:

1. Pass arguments by name, so a call with five values reads without counting positions.
2. Define default values, and explain why optional parameters always go last.
3. Use `len`, `sum`, `max`, `min`, `round` and `sorted` without writing them yourself.
4. Import a module with both forms of `import`.
5. Read the official documentation and find there what a function takes and returns.

### How to use this notebook

Run the cells in order. Five fail on purpose and carry a comment saying so.
"""),

md("""
---
# Block 1 · How arguments get passed

Three forms, and the difference shows when a function has more than three parameters.

| Form | How it looks | When it suits |
|---|---|---|
| By position | `f(250000, 0.18, 36)` | Two or three obvious values |
| By name | `f(principal=250000, months=36)` | When there are many or they are ambiguous |
| By default | `def f(insurance=0.0)` | What nearly always holds the same value |
"""),

code('''
def monthly_payment(principal, annual_rate, months, fee=0.0, insurance=0.0):
    """Monthly payment on a loan, with optional costs.

    fee        as a decimal on the principal, spread across the whole term
    insurance  a fixed amount added every month
    """
    i = annual_rate / 12
    factor = (1 + i) ** months
    base = principal * (i * factor) / (factor - 1)

    return base + principal * fee / months + insurance


print(monthly_payment(250000, 0.18, 36))
print(monthly_payment(250000, 0.18, 36, insurance=350))
'''),

md("""
**The required ones.** The first three have no default, so they always have to be given.

**The optional ones.** `fee` and `insurance` are zero unless mentioned, which is why the short
call still gives exactly the same number as last week.

**By name.** The second call skips `fee` and names `insurance`. Without naming it, both would
have to be passed.
"""),

code("""
# All four combinations, to see what each optional changes.
print(f"With nothing:   {monthly_payment(250000, 0.18, 36):>10,.2f}")
print(f"With insurance: {monthly_payment(250000, 0.18, 36, insurance=350):>10,.2f}")
print(f"With a 3% fee:  {monthly_payment(250000, 0.18, 36, fee=0.03):>10,.2f}")
print(f"With both:      {monthly_payment(250000, 0.18, 36, 0.03, 350):>10,.2f}")
"""),

md("""
## Why the optional ones go last

It is not style. Python rejects it while reading the file.
"""),

code(r'''
# FAILS ON PURPOSE. A parameter with a default before one without.
try:
    compile("def f(tax=0.16, base):\n    return base", "<example>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg}")
'''),

md("""
The reason is simple: if `tax` had a default and `base` did not, then `f(1000)` would be
ambiguous. Is the 1000 the base, or is it the tax with the base missing?

Python prefers not to guess.

## Skipping a parameter without naming it

**Predict before you run.** What does the second call print?

- **A.** 1160.0 and 1210.0
- **B.** 1160.0 and 51000
- **C.** 1160.0 and an error, arguments missing
- **D.** 1160.0 and 1050.0
"""),

code("""
def total(base, tax=0.16, shipping=0):
    return base * (1 + tax) + shipping


print(total(1000))
print(total(1000, 50))
"""),

md("""
The answer is **B**, 51000.

The 50 landed in `tax`, because that is the next one by position. The function computed
`1000 * 51` and returned a total fifty times too large, without protest.

Whoever wrote that line wanted 50 pesos of shipping.
"""),

code("""
# What they wanted, said by name.
print("With shipping of 50:", total(1000, shipping=50))

# And by position, passing the tax even though they did not mean to touch it.
print("With both positions:", total(1000, 0.16, 50))
"""),

md("""
That is the practical rule: **the moment you skip a parameter, name the ones after it.**

## When to name and when not to

Naming everything is noise. Naming nothing is guesswork. Where most people draw the line:
"""),

code("""
# Two obvious arguments: by position it reads fine.
print(round(9038.098883979254, 2))

# Five arguments of which three are bare numbers: naming saves you.
print(monthly_payment(principal=250000, annual_rate=0.18, months=36,
                      fee=0.03, insurance=350))
"""),

md("""
You will see it in every pandas and matplotlib call for the rest of the course:

```python
sales.pivot_table(index="region", columns="channel", values="amount", aggfunc="sum")
ax.plot(months, values, marker="o", linewidth=2, color="#2B5F8F")
```

Neither passes anything by position after the first pair. Now you know why.
"""),

md("""
---
# Block 2 · What Python already ships with

Half a dozen functions you were already using, and which you now know are functions like the ones
you write.

| Function | What it returns | Example |
|---|---|---|
| `len` | How many elements there are | `len(payments)` |
| `sum` | The sum of all of them | `sum(payments)` |
| `max` | The largest | `max(payments)` |
| `min` | The smallest | `min(payments)` |
| `round` | The rounded number | `round(average, 2)` |
| `sorted` | A sorted copy | `sorted(payments)` |
"""),

code("""
payments = [9038.10, 6344.53, 7220.66, 4180.25, 11902.44]

print("How many:", len(payments))
print("Sum:     ", round(sum(payments), 2))
print("Largest: ", max(payments))
print("Smallest:", min(payments))
print("Sorted:  ", sorted(payments))
"""),

md("""
Note `sorted`: it returns **a copy** in order and leaves the original list as it was.
"""),

code("""
print("Original after sorted:", payments)
"""),

md("""
That behaviour is the same as `sort_values` in pandas: almost everything in Python returns
something new rather than modifying what it received.

The other form exists, `.sort()`, which does modify and returns nothing.
"""),

code("""
copy = payments.copy()
result = copy.sort()

print("copy after .sort():", copy)
print("What .sort() returned:", result)
"""),

md("""
`None`, just like last week's function with no `return`. It is the signal that the method works on
the original instead of handing something back.

Confusing them produces this classic:
"""),

code("""
# FAILS ON PURPOSE. Storing the result of .sort() instead of using sorted().
wrong = payments.copy().sort()
right = sorted(payments)

print("With .sort():", wrong)
print("With sorted():", right[:3], "...")
"""),

md("""
## `round` and its surprises
"""),

code("""
print(round(2.675, 2), "<- not 2.68")
print(round(0.5), round(1.5), round(2.5), round(3.5), "<- rounding to even")
"""),

md("""
The first is the same problem as week 4: `2.675` in binary is a touch under 2.675, so it rounds
down.

The second is deliberate: Python rounds to the nearest even number when the fraction is exactly a
half. Across many numbers that stops rounding from always pushing upwards and inflating the sum.

For money, format on printing rather than rounding the value. That is what you have been doing
since week 5.
"""),

md("""
---
# Block 3 · Modules

Python ships hundreds of functions it does not load up front, because loading them all would slow
every program down. They are grouped by topic into **modules**, and `import` brings them in when
needed.

| Module | What it is for | When it arrives |
|---|---|---|
| `statistics` | Mean, median, mode | Today |
| `math` | Roots, powers, rounding | Today |
| `datetime` | Dates and the gaps between them | Week 14 |
| `csv` | Reading and writing data files | Week 14 |
| `pandas` | Whole tables, and it is not included | Week 15 |

The first four come with the installation, so importing them downloads nothing.

## The two forms of import
"""),

code("""
# Form 1: the whole module. It stays clear where each function came from.
import statistics

print(round(statistics.mean(payments), 2))
print(statistics.median(payments))
"""),

code("""
# Form 2: only what you use. Less to write.
from statistics import mean, median

print(round(mean(payments), 2))
print(median(payments))
"""),

md("""
Both do the same thing. The first is preferred when importing from several modules, because
`statistics.mean` and `math.floor` say where they came from. The second when a function gets used
many times and its name is already unambiguous.

And there is a third, the alias, which is the one you will use with pandas:
"""),

code("""
import statistics as st

print(round(st.mean(payments), 2))
print("And in week 15 this becomes: import pandas as pd")
"""),

md("""
## Mean and median do not say the same thing
"""),

code("""
print(f"Mean:   {mean(payments):>10,.2f}")
print(f"Median: {median(payments):>10,.2f}")
print(f"Gap:    {mean(payments) - median(payments):>10,.2f}")
"""),

md("""
Five hundred pesos of difference across five loans. The payment of 11,902 pulls the mean up and
the median does not move, because the median only cares which one sits in the middle.

It is the same lesson as the salaries in week 3 and the histogram in week 16. When those two
numbers separate, the separation is the finding.

## What else `statistics` carries
"""),

code("""
import statistics

print([n for n in dir(statistics) if not n.startswith("_")])
"""),

md("""
`dir` lists everything a module carries. The list comprehension filters out the names starting
with an underscore, which are for internal use.

That line works on any module, and it is the fastest way to see what is there before going to the
documentation.
"""),

code("""
from statistics import stdev, mode, quantiles

print("Standard deviation:", round(stdev(payments), 2))
print("Quartiles:", [round(q, 2) for q in quantiles(payments)])

try:
    print("mode:", mode(payments))
except statistics.StatisticsError as e:
    print("StatisticsError:", e)
"""),

md("""
Careful: in recent versions `mode` returns the first value when nothing repeats, and in older ones
it raises. If your output shows a number instead of the error, yours is one of the returning kind.

That is information too: **a function can change behaviour between versions**, which is why the
documentation states which one it describes.

## `math`
"""),

code("""
import math

print("Square root of 144:", math.sqrt(144))
print("Round down:        ", math.floor(9038.98))
print("Round up:          ", math.ceil(9038.02))
print("Absolute value:    ", abs(-350))
print("Pi:                ", round(math.pi, 4))
"""),

md("""
`abs` needed no import: it is one of the built-ins. `floor` and `ceil` do, and they are the ones
for "how many complete months" and "how many boxes are needed".
"""),

code("""
pieces = 47
per_box = 12

print("Complete boxes:", math.floor(pieces / per_box))
print("Boxes to order:", math.ceil(pieces / per_box))
print("With //:       ", pieces // per_box, "<- same as floor, with nothing imported")
"""),

md("""
## Reading the documentation
"""),

code("""
help(round)
"""),

md("""
That first line, `round(number, ndigits=None)`, is the signature: it says what it takes and what
is optional. The `ndigits=None` is exactly the default values from block 1.

The official documentation lives at `docs.python.org` and says the same with more context and
examples. Being able to read it is half the battle of the final project, because nobody can teach
you from memory everything pandas carries.

## Four errors with arguments and modules

**Putting the optional before the required.** You saw it: `SyntaxError` on reading the file.

**Skipping a parameter without naming it.** You saw it: the 50 that landed in `tax`.

**Importing inside a function.** It works, and it hides the dependency.
"""),

code("""
def hidden_average(numbers):
    from statistics import mean      # works, and nobody reading the file expects it here
    return mean(numbers)


print(hidden_average(payments))
print("It runs fine, and a reader has no idea it depends on statistics.")
"""),

md("""
The `import` goes at the top, where whoever reads the file finds it in three seconds.

**Naming your file after a module.** A file called `math.py` in your folder makes `import math`
bring in yours, and the resulting error makes no sense.
"""),

code("""
# A safe demonstration: I build a fake module and give it priority by hand.
import sys, types

fake = types.ModuleType("statistics")
fake.mean = lambda x: "this is not an average"

real = sys.modules["statistics"]
sys.modules["statistics"] = fake

from statistics import mean as fake_mean
print("With the wrong file:", fake_mean(payments))

sys.modules["statistics"] = real      # put everything back
from statistics import mean
print("With the real one:", round(mean(payments), 2))
"""),

md("""
In real life this happens without anyone provoking it: somebody saves their homework as `math.py`
or `csv.py` in the same folder, and from then on the program does inexplicable things.

The rule: **never name your file after a module.**
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Arguments

### Exercise 1 · The three optionals

Write `final_price(base, tax=0.16, discount=0.0, shipping=0.0)` applying the discount first, then
the tax, and adding shipping at the end.

Call it four times: with no optionals, with a discount, with shipping, and with all three.

### Exercise 2 · The unnamed skip

With the function from exercise 1, write the call that **looks like** it sets shipping to 100 and
actually puts it somewhere else. Print both results and explain in a comment where the 100 landed.

### Exercise 3 · Readable with five

Write a function with five parameters, three of them numeric, then two calls: one purely by
position and one purely by name. Read them out loud and say which you would understand six months
from now.

## Built-ins

### Exercise 4 · All six on your data

With a list of at least eight numbers from your field, use the six built-in functions from the
table and print each result with a label.

Then check that the original list did not end up sorted.

### Exercise 5 · `sorted` against `.sort()`

Prove the difference in code: make two copies of the same list, sort one with `sorted` and the
other with `.sort()`, and print both lists and both returned values.

### Exercise 6 · `max` with a criterion

Look up what `max`'s `key` parameter does. Then use it on this list to find the loan with the
highest payment:

```python
LOANS = [("A", 250000, 9038.10), ("B", 120000, 6344.53), ("C", 480000, 11902.44)]
```

Hint: `max(LOANS, key=...)` takes a function saying which value to compare by.

## Modules

### Exercise 7 · Exploring a module

Use `dir` on `math` and pick three functions we did not cover. Read their `help` and explain in a
comment what each takes and returns.

### Exercise 8 · A `statistics` function we skipped

Find on `docs.python.org` a function from `statistics` that did not appear in the notebook,
explain in three lines what it takes and returns, and use it on the five payments from this
session.

### Exercise 9 · Your function, with the optional made optional

Take the function you wrote last week and add two parameters with default values, so the short
call still works exactly as before. Use it three times with different combinations.

The third call has to pass an argument by name while skipping another.

The test: the call with no optional arguments has to give exactly the same number as last week.
"""),

md("""
---
## Three ideas to take away

**The optional ones go last.** A parameter with a default before one without is a syntax error,
not a style decision.

**Naming the argument reads better.** Once a function passes three parameters, counting positions
stops being viable, and the 50 that lands in `tax` raises nothing.

**`import` is the door to everything.** What brings in `statistics` today is exactly what will
bring in pandas in week 15. The only difference is that pandas has to be installed once.

Next session is lists and tuples, which are the column of your spreadsheet.
"""),

md('''
---
# Solutions

### Exercise 1

```python
def final_price(base, tax=0.16, discount=0.0, shipping=0.0):
    """Final price: discount first, tax second, shipping last."""
    discounted = base * (1 - discount)
    return discounted * (1 + tax) + shipping


print(f"No optionals:   {final_price(1000):>10,.2f}")
print(f"With discount:  {final_price(1000, discount=0.10):>10,.2f}")
print(f"With shipping:  {final_price(1000, shipping=150):>10,.2f}")
print(f"With all three: {final_price(1000, 0.08, 0.10, 150):>10,.2f}")
```

That the discount comes before the tax is not a technical detail, it is a tax decision: VAT is
computed on the already-discounted price. The other way round gives a different number and it
would be wrong.

### Exercise 2

```python
print("What they wanted:", final_price(1000, shipping=100))
print("What they wrote: ", final_price(1000, 100))

# The 100 landed in tax, because it is the next parameter by position. The function
# computed 1000 * (1 + 100), so 101,000. That is a hundred times the price and it
# raised nothing, because a tax of 100 is a perfectly valid number.
```

A hundred thousand pesos for something worth a thousand. The scale of the error is the only thing
that gives it away, and in a report full of figures that does not always jump out.

### Exercise 3

```python
def quote(customer, base, tax, discount, credit_days):
    return f"{customer}: {base * (1 - discount) * (1 + tax):,.2f} at {credit_days} days"


print(quote("Insumos SA", 12000, 0.16, 0.05, 30))
print(quote(customer="Insumos SA", base=12000, tax=0.16,
            discount=0.05, credit_days=30))

# Six months from now I would understand the second. In the first, 0.16 and 0.05 are
# two decimals in a row and there is no way to tell which is which without opening
# the definition.
```

The rule that falls out of it: when two consecutive parameters are the same type and could be
swapped without anything blowing up, name them.

### Exercise 4

```python
units = [15, 8, 22, 5, 11, 35, 20, 18]

print("How many:", len(units))
print("Sum:     ", sum(units))
print("Largest: ", max(units))
print("Smallest:", min(units))
print("Average: ", round(sum(units) / len(units), 2))
print("Sorted:  ", sorted(units))
print("Original:", units)
```

The last line is what matters: the original list is still in its order. `sorted` never touched it.

### Exercise 5

```python
a = [15, 8, 22, 5]
b = [15, 8, 22, 5]

sorted_returned = sorted(a)
sort_returned = b.sort()

print("a after sorted:  ", a)
print("sorted returned: ", sorted_returned)
print("b after .sort(): ", b)
print(".sort() returned:", sort_returned)
```

`sorted` leaves `a` alone and returns the ordered copy. `.sort()` changes `b` and returns `None`.

Python's pocket rule: if a method modifies the object, it returns `None`, so you cannot chain it
by mistake.

### Exercise 6

```python
LOANS = [("A", 250000, 9038.10), ("B", 120000, 6344.53), ("C", 480000, 11902.44)]

highest_payment = max(LOANS, key=lambda loan: loan[2])
highest_principal = max(LOANS, key=lambda loan: loan[1])

print("Highest payment:  ", highest_payment)
print("Highest principal:", highest_principal)
print("Without key:      ", max(LOANS), "<- compares by the first element, the letter")
```

`key` takes a function saying which value to compare by. Without it, `max` compares whole tuples
starting from the first element, which here is the letter, and returns C alphabetically. That it
happens to match the right answer is a coincidence.

That `lambda` is a nameless function written on one line. It does exactly what a two-line `def`
does, and it gets used when the function is so short that naming it gets in the way.

### Exercise 7

```python
import math

for name in ["trunc", "hypot", "log10"]:
    print("=" * 50)
    help(getattr(math, name))

# trunc  takes a number and returns its integer part, cutting towards zero. With
#        negatives it differs from floor: trunc(-2.7) is -2 and floor(-2.7) is -3.
# hypot  takes two or more numbers and returns the root of the sum of their squares.
#        It is the straight-line distance, useful for comparing two metrics at once.
# log10  takes a positive number and returns its base ten logarithm. Useful for
#        comparing quantities that differ by orders of magnitude.
```

`getattr(math, name)` pulls a function out of a module by its name as text. That is what allows
looping over a list of names instead of writing three `help` calls by hand.

### Exercise 8

```python
from statistics import fmean, pstdev

print("fmean: ", round(fmean(payments), 2))
print("pstdev:", round(pstdev(payments), 2))
print("stdev: ", round(stdev(payments), 2))

# fmean takes a list of numbers and returns their average as a float, like mean but
# faster because it does not try to preserve exact types.
# pstdev takes a list and returns the standard deviation of the POPULATION, dividing
# by n. stdev divides by n-1 because it assumes the list is a sample of something
# larger. Which to use depends on whether your five loans are all that exist or a
# sample of a bigger book.
```

That distinction between population and sample is one a statistics course covers and a programming
course usually skips. It matters here because picking the wrong one changes the number and neither
raises an error.

### Exercise 9

There is no published solution, because the function differs for everyone. It is graded on three
things: that the short call gives exactly the same result as last week's version, that the two new
parameters have defaults and sit at the end, and that the third call skips one while naming the
next.
'''),

]

write(OUT / "en" / "w11.ipynb", en)
print("wrote", OUT / "en" / "w11.ipynb")
