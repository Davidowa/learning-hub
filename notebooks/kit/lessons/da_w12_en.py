"""notebooks/analisis-de-datos/en/w12.ipynb

Source deck: ppts/python/analisis-de-datos/en/w12.en.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

en = [

md("""
# Data Analysis · Week 12
## Lists and tuples

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

A list is a column. Worth saying early and holding onto, because in week 15 a pandas `Series` is
exactly this with an index on top.

By the end of this notebook you will be able to:

1. Create and walk a list, with indexes starting at zero and also counting backwards.
2. Take a slice, and explain why the second index is excluded.
3. Use the eleven list methods, telling the ones that modify from the ones that ask.
4. Tell a list from a tuple, and say when each one suits.
5. Recognise an alias, and make a real copy.

### How to use this notebook

Run the cells in order. Six fail on purpose and carry a comment saying so.

The alias-against-copy part is counter-intuitive and does not sink in by reading. Run those cells
twice if you need to: it is the source of errors that look haunted.
"""),

md("""
---
# Block 1 · A list is a column

Values in order, under one name. The difference from a range of cells is that a list grows and
shrinks on its own, with no size declared up front.
"""),

code("""
payments = [9038.10, 6344.53, 7220.66, 4180.25, 11902.44]

print(payments)
print("How many:", len(payments))
print("Type:    ", type(payments))
"""),

md("""
## The indexes
"""),

code("""
print("The first:      ", payments[0])
print("The second:     ", payments[1])
print("The last:       ", payments[-1])
print("The second last:", payments[-2])
"""),

md("""
**The first one is zero.** It is break number one for anyone coming from row 1, and you saw it in
week 1.1.

**The negatives** count from the end. `payments[-1]` is the last one regardless of how many there
are, and it saves writing `payments[len(payments) - 1]`.
"""),

code("""
# FAILS ON PURPOSE. Five elements run from index 0 to 4.
try:
    print(payments[5])
except IndexError as e:
    print("IndexError:", e)

print("The last valid index is:", len(payments) - 1)
"""),

md("""
## Slices

A slice cuts a piece and returns **a new list**. The first index is included, the second is not.
"""),

code("""
print("payments[1:3] ->", payments[1:3])
print("payments[:2]  ->", payments[:2],  "<- from the start")
print("payments[3:]  ->", payments[3:],  "<- to the end")
print("payments[:]   ->", payments[:],   "<- the whole list")
print("payments[-2:] ->", payments[-2:], "<- the last two")
"""),

md("""
That the second index is excluded sounds arbitrary and is not: **`lst[a:b]` returns exactly
`b - a` elements.** Sizes come out round and slices join without overlapping.
"""),

code("""
print("payments[0:2] has", len(payments[0:2]), "elements")
print("payments[2:5] has", len(payments[2:5]), "elements")
print()
print("And together they rebuild the list:", payments[0:2] + payments[2:5] == payments)
"""),

md("""
A slice also takes a step, just like `range`.
"""),

code("""
print("Every other one:", payments[::2])
print("Backwards:      ", payments[::-1])
print("The original:   ", payments, "<- untouched")
"""),

md("""
`payments[::-1]` is the trick for reversing without touching the original. It is the same
`[start:stop:step]` as always, with a negative step.

## Walking

You saw this in week 8. Here is just the reminder of the three forms and when each belongs.
"""),

code("""
clients = ["Ana", "Beto", "Carla", "Diego", "Elena"]

# Values only.
for payment in payments:
    print(f"{payment:>10,.2f}", end="  ")
print()

# With the position.
for i, payment in enumerate(payments):
    print(f"{i}:{payment:,.0f}", end="  ")
print()

# Two paired lists.
for client, payment in zip(clients, payments):
    print(f"{client}={payment:,.0f}", end="  ")
print()
"""),

md("""
---
# Block 2 · The methods

Eleven in total. Six change the list, five only ask about it, and confusing them is expensive.

## The six that modify

| Method | What it does | Example |
|---|---|---|
| `append` | Adds one at the end | `payments.append(5500)` |
| `insert` | Adds one at a position | `payments.insert(0, 5500)` |
| `extend` | Adds the ones from another list | `payments.extend(others)` |
| `remove` | Removes the first occurrence | `payments.remove(5500)` |
| `pop` | Takes one out and returns it | `last = payments.pop()` |
| `clear` | Removes them all | `payments.clear()` |
"""),

code("""
demo = [300, 100, 200]
print("Start:       ", demo)

demo.append(400)
print("append(400): ", demo)

demo.insert(0, 50)
print("insert(0,50):", demo)

demo.extend([500, 600])
print("extend:      ", demo)

demo.remove(100)
print("remove(100): ", demo)

taken = demo.pop()
print("pop():       ", demo, "and it returned", taken)

demo.clear()
print("clear():     ", demo)
"""),

md("""
`pop` is the only one of the six that **modifies and also returns something**. The other five
return `None`, which is the signal that they work on the original.
"""),

code("""
lst = [1, 2, 3]

print("append returns:", lst.append(4))
print("insert returns:", lst.insert(0, 0))
print("remove returns:", lst.remove(2))
print("pop returns:   ", lst.pop())
print("The list ended:", lst)
"""),

md("""
## The remaining five

| Method | What it does | Example |
|---|---|---|
| `sort` | Sorts in place | `payments.sort()` |
| `reverse` | Reverses in place | `payments.reverse()` |
| `index` | What position it sits at | `payments.index(7220.66)` |
| `count` | How many times it appears | `payments.count(6344.53)` |
| `copy` | Returns a new copy | `other = payments.copy()` |
"""),

code("""
print("index of 7220.66:", payments.index(7220.66))
print("count of 6344.53:", payments.count(6344.53))
print("count of 99999:  ", payments.count(99999), "<- zero, it does not raise")

# FAILS ON PURPOSE. index does raise when it finds nothing.
try:
    payments.index(99999)
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
`count` returns zero when it finds nothing and `index` raises `ValueError`. The difference matters:
if all you want is whether something is there, `in` is safer than `index`.
"""),

code("""
print("Is 7220.66 there?", 7220.66 in payments)
print("Is 99999 there?  ", 99999 in payments)
"""),

md("""
## Modifying is not returning

This is the distinction that costs most in the exam.

**Predict before you run.** What does the last line print?

- **A.** `[100, 200, 300]`, the sorted list.
- **B.** `None`, because `sort` sorts and returns nothing.
- **C.** `[300, 100, 200]`, unchanged.
- **D.** An error, because an argument is missing.
"""),

code("""
# FAILS ON PURPOSE. Storing what sort returns.
sales = [300, 100, 200]
result = sales.sort()

print(result)
print("And the list did get sorted:", sales)
"""),

md("""
The answer is **B**. `sort` sorted the list and returned `None`.

The real problem is when somebody writes `sales = sales.sort()`. There **`sales` stops being a
list and becomes `None`.** The data disappears.
"""),

code("""
# FAILS ON PURPOSE. Reassigning the result of sort erases the list.
data = [300, 100, 200]
data = data.sort()

print("data is now:", data)

try:
    print(len(data))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
The two correct forms, depending on what you want:
"""),

code("""
originals = [300, 100, 200]

# I want the list sorted and do not mind losing the original order.
a = originals.copy()
a.sort()
print("With sort:  ", a)

# I want a sorted copy and want to keep the original.
b = sorted(originals)
print("With sorted:", b, "· original:", originals)
"""),

md("""
`sort` is a method and works on the list. `sorted` is a function and returns another.

The same pair exists for reversing: `reverse` modifies, `reversed` returns.
"""),

code("""
one = [1, 2, 3]
one.reverse()
print("reverse:", one)

two = [1, 2, 3]
print("reversed:", list(reversed(two)), "· original:", two)
"""),

md("""
## Deleting while walking

This is the error that produces results nobody can explain.
"""),

code("""
# FAILS ON PURPOSE. Removing elements inside the for shifts the positions.
numbers = [1, 2, 2, 3, 2, 4]

for n in numbers:
    if n == 2:
        numbers.remove(2)

print("Left over:", numbers, "<- there is still a 2")
"""),

md("""
A 2 survived. The loop advances by position and `remove` shifts everything one place left, so the
loop skips values.

The right way is to build a new list rather than mutilating the one you are walking.
"""),

code("""
numbers = [1, 2, 2, 3, 2, 4]

without_twos = [n for n in numbers if n != 2]

print("Original:", numbers)
print("Filtered:", without_twos)
"""),

md("""
That is a **list comprehension**, and it reads left to right: "the `n`s in `numbers` that are not
2".

It is the commonest way to filter in Python, and the direct ancestor of the pandas boolean mask
from week 15.2.
"""),

code("""
# Filter, transform, and both at once.
print("Filter:   ", [p for p in payments if p > 7000])
print("Transform:", [round(p * 1.16, 2) for p in payments])
print("Both:     ", [round(p * 1.16, 2) for p in payments if p > 7000])
"""),

md("""
`remove` has another trap: **it removes only the first occurrence.**
"""),

code("""
three_twos = [2, 5, 2, 8, 2]
three_twos.remove(2)

print("After one remove:", three_twos, "<- two left")
"""),

md("""
---
# Block 3 · Copies, aliases and tuples

Two names can point at the same list. When that happens without you knowing, the errors look
haunted.
"""),

code("""
a = [1, 2, 3]
b = a               # this does NOT copy
b.append(4)

print("b:", b)
print("a:", a, "<- it changed too")
print("Same object?", a is b)
"""),

md("""
The equals sign copies nothing. It creates **a second name for the same list**, and touching
either one touches the only one there is.

It is the same `is` from week 7, and this is where it bites.
"""),

code("""
c = [1, 2, 3]
d = c.copy()        # this DOES copy
d.append(4)

print("d:", d)
print("c:", c, "<- untouched")
print("Same object?", c is d)
print("Equal in value?", c == d)
"""),

md("""
There are three ways to copy and all three do the same:
"""),

code("""
base = [1, 2, 3]

print(base.copy())
print(base[:])
print(list(base))
print("All three are separate objects:", base is not base.copy())
"""),

md("""
## Where it really bites

With a loose list the error is visible. Inside a function, it is not.
"""),

code("""
# FAILS ON PURPOSE. The function modifies the list it was handed.
def add_fee(payment_list):
    payment_list.append(500)      # touches the original list
    return payment_list


my_payments = [9038.10, 6344.53]
result = add_fee(my_payments)

print("What it returned:", result)
print("My list:         ", my_payments, "<- it grew too")
"""),

md("""
The function received the name, not a copy. Modifying it inside modified the outside one.

Sometimes that is what you want. When it is not, the function copies first.
"""),

code("""
def with_fee(payment_list):
    \"\"\"Returns a new list. Does not touch the one it received.\"\"\"
    fresh = payment_list.copy()
    fresh.append(500)
    return fresh


my_payments = [9038.10, 6344.53]
result = with_fee(my_payments)

print("What it returned:", result)
print("My list:         ", my_payments, "<- untouched")
"""),

md("""
This is the underlying reason week 15.2 starts by calling `sales.copy()` before the Copy-on-Write
demonstration. Same problem, one level up.

## Tuples

| Aspect | List | Tuple |
|---|---|---|
| Written with | Square brackets | Parentheses |
| Can it change | Yes | No, never |
| What it is for | Data that grows | Data that must not change |
| Course example | The payments column | A loan's terms |
"""),

code("""
terms = (250000, 0.18, 36)

print(terms)
print("The second:", terms[1])
print("A slice:   ", terms[:2])
print("Length:    ", len(terms))
"""),

md("""
It indexes and slices just like a list. The only thing you cannot do is change it.
"""),

code("""
# FAILS ON PURPOSE. A tuple cannot be modified.
try:
    terms[0] = 300000
except TypeError as e:
    print("TypeError:", e)

try:
    terms.append(12)
except AttributeError as e:
    print("AttributeError:", e)
"""),

md("""
That it cannot change sounds like a limitation and is a design decision. **A tuple says "this
should not change"**, and the language enforces it.

The terms of a signed loan are exactly that: if somebody modifies them mid-run, the error is in
whoever modified them, not in the tuple.

And you were already using tuples without knowing.
"""),

code("""
def summary(numbers):
    return min(numbers), max(numbers), sum(numbers)


returned = summary(payments)
print("What it returns:", returned, type(returned))

lowest, highest, total = returned
print(f"lowest={lowest:,.2f}  highest={highest:,.2f}  total={total:,.2f}")
"""),

md("""
`return a, b, c` builds a tuple, and the line receiving it unpacks it. That is what you did in
week 10 without naming it.

It also turns up in every `for client, payment in zip(...)`: each pass hands over a tuple and the
`for` unpacks it.
"""),

code("""
for pair in zip(clients, payments):
    print(pair, type(pair).__name__)
    break

print()
print("And in an ordinary loop it unpacks itself:")
for client, payment in zip(clients[:2], payments[:2]):
    print(f"  {client}: {payment:,.2f}")
"""),

md("""
## Four list traps

**Storing what `sort` returns.** `payments = payments.sort()` leaves `payments` as `None`.

**Copying with the equals sign.** `other = payments` copies nothing.

**Deleting while walking.** The loop skips values.

**Assuming `remove` takes them all.** It takes only the first occurrence.

You watched all four run above.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Indexes and slices

### Exercise 1 · The six accesses

With a list of twelve values from your field, print: the first, the last, the first three, the last
three, the middle ones, and the list reversed.

Check at the end that the original list did not change.

### Exercise 2 · Why the second one is excluded

Prove in code that `lst[a:b]` returns exactly `b - a` elements, testing four different pairs.

Then cut your list of twelve into three pieces of four and check that joining them gives the
original back.

### Exercise 3 · The index that does not exist

Provoke an `IndexError` with a positive index and another with a negative one. Write down both
messages.

Then write a function `safe_item(lst, i)` returning `None` instead of blowing up.

## Methods

### Exercise 4 · The six that modify

Start with a list of three elements and apply all six modifying methods, in order, printing the
list after each. Finish with a list different from the initial one and not empty.

### Exercise 5 · The dangerous pair

Write four lines proving the difference between `sort` and `sorted`, and between `reverse` and
`reversed`. Print in each case what was returned and how the list ended up.

### Exercise 6 · Filtering without breaking

Take a list with repeated values and remove every occurrence of one of them, two ways: with a
`while` loop and `remove`, and with a list comprehension.

Say in a comment which you prefer and why.

## Copies and tuples

### Exercise 7 · The alias that bites

Write a function taking a list and appending an element, and prove it modifies the original. Then
fix it and prove it no longer does.

### Exercise 8 · List or tuple

For each, say in a comment whether you would store it in a list or a tuple and why: a branch's
coordinates, a loan's monthly payments, the months of the year, today's customers, the terms of a
signed contract.

### Exercise 9 · A column from your field

Take twelve real values from your field in a list and answer four questions: the largest, the
smallest, the top three, and what position one of your choosing sits at.

The original list has to be in its initial order when the program ends. Print it at the start and
at the end: if it changed, you used a method where a function belonged.
"""),

md("""
---
## Three ideas to take away

**A list is a column.** And in week 15 that same column will be called a `Series`, with an index
placed on top. Everything from today about walking, slicing and sorting still applies there.

**Modifying is not returning.** `sort` sorts and returns `None`; `sorted` leaves the list alone and
returns another. The confusion does not raise an error, it erases data.

**The equals sign does not copy.** It creates a second name for the same list, and touching either
one touches the only one there is.

Next session is dictionaries and sets, and the second midterm.
"""),

md('''
---
# Solutions

### Exercise 1

```python
units = [15, 8, 22, 5, 11, 35, 20, 18, 9, 27, 13, 31]

print("Original:      ", units)
print("The first:     ", units[0])
print("The last:      ", units[-1])
print("First three:   ", units[:3])
print("Last three:    ", units[-3:])
print("The middle:    ", units[4:8])
print("Reversed:      ", units[::-1])
print("Still the same:", units)
```

No slice touched the original, because they all return new lists. That is the difference from the
methods in block 2.

### Exercise 2

```python
for a, b in [(0, 3), (2, 7), (4, 12), (5, 6)]:
    print(f"[{a}:{b}] returns {len(units[a:b])} elements, and b-a is {b - a}")

one, two, three = units[0:4], units[4:8], units[8:12]
print("\\nJoined:", one + two + three == units)
```

The three pieces join with no overlap and no gaps precisely because the end is excluded. If it were
included you would have to write `[0:3]`, `[4:7]`, `[8:11]` and remember to add one each time.

### Exercise 3

```python
for i in [12, -13]:
    try:
        units[i]
    except IndexError as e:
        print(f"units[{i}] -> IndexError: {e}")


def safe_item(lst, i):
    """Returns the element, or None if the position does not exist."""
    try:
        return lst[i]
    except IndexError:
        return None


print(safe_item(units, 3), safe_item(units, 99))
```

Both messages say the same thing, `list index out of range`, without saying which index or how many
elements there were. Which is why printing `len` beside it helps while debugging.

### Exercise 4

```python
lst = [10, 20, 30]
print("Start:  ", lst)

lst.append(40);        print("append: ", lst)
lst.insert(0, 5);      print("insert: ", lst)
lst.extend([50, 60]);  print("extend: ", lst)
lst.remove(20);        print("remove: ", lst)
lst.pop();             print("pop:    ", lst)
lst.clear();           print("clear:  ", lst)

lst.extend([1, 2, 3])
print("At the end:", lst)
```

`clear` empties the list without destroying it: it is still the same list, which is why the later
`extend` works.

### Exercise 5

```python
a = [3, 1, 2]
print("sort returned:    ", a.sort(), "· list:", a)

b = [3, 1, 2]
print("sorted returned:  ", sorted(b), "· list:", b)

c = [3, 1, 2]
print("reverse returned: ", c.reverse(), "· list:", c)

d = [3, 1, 2]
print("reversed returned:", list(reversed(d)), "· list:", d)
```

Both methods return `None` and change the list. Both functions return something and leave it alone.
`reversed` also returns a lazy object, hence the `list()` around it.

### Exercise 6

```python
values = [2, 5, 2, 8, 2, 9]

with_while = values.copy()
while 2 in with_while:
    with_while.remove(2)

with_comprehension = [v for v in values if v != 2]

print("With while+remove:  ", with_while)
print("With a comprehension:", with_comprehension)

# I prefer the comprehension. It says what I want in one line instead of how to
# remove it in three, it modifies nothing, and it cannot get stuck in an infinite
# loop if I get the condition wrong. The while+remove also walks the list once per
# element it removes.
```

The comprehension is also the one that resembles what you will write in pandas:
`sales[sales["region"] != "North"]` is the same idea in another syntax.

### Exercise 7

```python
def adds_badly(lst):
    lst.append(999)
    return lst


def adds_well(lst):
    fresh = lst.copy()
    fresh.append(999)
    return fresh


original = [1, 2, 3]
adds_badly(original)
print("After adds_badly:", original)

original = [1, 2, 3]
returned = adds_well(original)
print("After adds_well: ", original, "· returned", returned)
```

The practical rule: if your function returns something, it should not also modify what it received.
Doing both is what surprises whoever calls it.

### Exercise 8

```python
# A branch's coordinates -> tuple. Two numbers that travel together and do not
#   change. A tuple can also be a dictionary key and a list cannot.
# A loan's monthly payments -> list. They get added as they are paid.
# The months of the year -> tuple. There are twelve, always the same, and nobody
#   should be able to add a thirteenth by accident.
# Today's customers -> list. It grows through the day.
# The terms of a signed contract -> tuple. Changing them after signing is exactly
#   what must not happen, and the tuple prevents it.
```

The question that decides: is this going to grow or change during the run? If not, tuple, and the
language watches your back.

### Exercise 9

There is no published solution, because the values differ for everyone. It is graded on three
things: that all four answers are labelled, that the list printed at the end is identical to the one
at the start, and that "the top three" used `sorted` rather than `sort`.
'''),

]

write(OUT / "en" / "w12.ipynb", en)
print("wrote", OUT / "en" / "w12.ipynb")
