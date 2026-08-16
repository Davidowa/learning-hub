"""notebooks/programacion-orientada-a-objetos/en/w01.4.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w01.4.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/4th Module/
              Code012.py, Code013.py, Code014.py, Code015.py

Code013.py does not run: line 31 calls tuple.extend. The notebook teaches that as
a trap instead of quoting it as if it worked, along with line 50 (tuple.copy),
line 117 (tuple.clear) and the false claim on lines 46 and 47.
Code014.py line 159 prints False while its comment says True.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Review 4 of 5
## Module 4 · Collections

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Four ways to hold several things in one variable, and when to reach for each.

Review 3 ended with a warning: a list used as a function's default value gets shared across every
call. This notebook explains why. The answer is that assigning a list does not copy it, and that one
sentence is what will explain, in week 6, why two objects of the same class end up looking at the
same data.

By the end of this notebook you will be able to:

1. Choose between list, tuple, set and dictionary using three questions.
2. Index and slice a list, and say why the last index is `n - 1`.
3. Use the list methods knowing which ones change the list and which ones return.
4. Look up by key with `get` instead of brackets when the field may be missing.
5. Tell copying from renaming, and prove the difference with `id`.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Nineteen fail on purpose and carry a comment saying
so.

Ten of those nineteen **raise no exception at all**. Those are the ones that matter: the program
keeps running, hands back a believable result, and is wrong. Two of the nineteen reproduce errors
that the course file still carries uncorrected.
"""),

md("""
---
# Block 1 · The four collections

A variable holds one value. When what you need to hold is thirty grades, four regions or a student's
record, you need a container.

Python ships four of them, and they are not interchangeable. You pick one by answering three
questions:

1. **Does order matter?** If you are going to talk about "the first" or "the third", yes.
2. **Will it change after it is built?** If nobody should touch it, one of them guarantees that.
3. **Can there be duplicates?** If a repeat is valid data, you cannot use the one that deletes them.
"""),

code("""
items_list = ["coffee", "filter", "mug"]
items_tuple = ("coffee", "filter", "mug")
items_set = {"coffee", "filter", "mug"}
items_dict = {"coffee": 45, "filter": 12, "mug": 89}

for name, value in [("list", items_list), ("tuple", items_tuple),
                    ("set", items_set), ("dict", items_dict)]:
    print(f"{name:<7}{type(value).__name__:<7}{len(value)} items   {value}")
"""),

md("""
Square brackets make a list, round ones make a tuple, and curly braces make either a set or a
dictionary depending on what goes inside: bare values give a set, `key: value` pairs give a
dictionary.

One detail that bites: empty `{}` is **not** an empty set, it is an empty dictionary. The empty set
is written `set()`.

## The three questions, measured

The slide's table says which one is ordered, which one can be changed and which one allows
duplicates. Rather than take its word for it, the cell below tests all four.
"""),

code("""
import copy as copy_module

RAW = ["a", "b", "a", "c"]        # four items, one of them repeated

candidates = [
    ("list", list(RAW)),
    ("tuple", tuple(RAW)),
    ("set", set(RAW)),
    ("dict", dict.fromkeys(RAW, 0)),
]


def accepts_index_zero(collection):
    try:
        collection[0]
    except (TypeError, KeyError):
        return "no"
    return "yes"


def accepts_assignment(collection):
    probe = copy_module.copy(collection)
    try:
        probe[0] = "z"
    except TypeError:
        return "no"
    return "yes"


print(f"{'Collection':<12}{'Items':>7}{'reads [0]':>12}{'[0] = z':>10}")
for name, value in candidates:
    print(f"{name:<12}{len(value):>7}"
          f"{accepts_index_zero(value):>12}{accepts_assignment(value):>10}")
"""),

md("""
Four items went in, and four came out of the list and the tuple while three came out of the set and
the dictionary. The missing one is the repeated `"a"`, and it vanished without a word.

Both right-hand columns say "no" for the set and the dictionary, but for different reasons. A set
simply has no positions. A dictionary does accept brackets, only what goes inside is a key and not a
position, and the key `0` is not there: that is why reading fails and assigning succeeds, quietly
creating a new key.

The tuple is the only one of the four that reads fine and refuses the assignment, and that is its
one and only difference from a list.

## Duplicates leave without a sound
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A set used to drop duplicates that were not duplicates.
grades = [8, 9, 8, 10, 9, 8]

unique = set(grades)

print("Recorded:", grades, "->", len(grades), "grades")
print("As a set:", unique, "->", len(unique), "grades")
print()
print(f"Real average:      {sum(grades) / len(grades):.2f}")
print(f"Average of the set: {sum(unique) / len(unique):.2f}")
"""),

md("""
Six grades went in and three came out. The average moved from 8.67 to 9.00, and both numbers are
equally believable.

The set did exactly what it promises: hold unique values. The problem is that three different
students can score an 8, and there the repeat is data rather than noise. `set` answers **which values
showed up**, never how many times each one did.

The same loss happens in a dictionary when a key repeats.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The same key written twice.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
}

print(car)
print("Keys:", len(car))
"""),

md("""
The 1964 never existed. Python read the dictionary top to bottom, stored `1964` and wrote `2020` over
it before the first line of your program ran.

That comes from the course file `Code015.py`, and there it is on purpose: it is the example that the
last one wins. In a two hundred line configuration file, the same key typed twice by accident does
exactly this and leaves no trace.

## And there is a worse version
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Three keys that Python treats as one.
odd = {True: "one", 1: "another", 1.0: "third"}

print(odd, "· keys:", len(odd))
print()
print("True == 1 :", True == 1)
print("1 == 1.0  :", 1 == 1.0)
print("same hash :", hash(True) == hash(1) == hash(1.0))
"""),

md("""
Three keys written, one stored, and the value that survived is the last one.

Two keys are the same key when they compare equal with `==` and share a `hash`. `True`, `1` and `1.0`
meet both conditions, because in Python `bool` is a subclass of `int` and the float `1.0` is worth
the same as the integer. The dictionary kept the first key it saw, which was `True`, and wrote the
last value on top of it.

Writing it that way on purpose is rare. Arriving at the same place with computed keys is easy, when
one comes from an `int` and another from a division that returned `1.0`.
"""),

md("""
---
# Block 2 · Lists

The collection you will reach for ninety per cent of the time. Ordered, changeable, duplicates
allowed.

It indexes exactly like a string, with everything you already saw in review 1: positions from zero,
negative indexes from the end, slices and step.
"""),

code("""
fruits = ["apple", "banana", "cherry", "blackcurrant"]

print("fruits[1]     ", fruits[1])          # banana
print("fruits[-1]    ", fruits[-1])         # the last one
print("fruits[1:3]   ", fruits[1:3])        # 1 up to 2, 3 stays out
print("fruits[:2]    ", fruits[:2])         # from the start
print("fruits[1:]    ", fruits[1:])         # to the end
print("fruits[-3:-1] ", fruits[-3:-1])      # negatives, same rule
print("fruits[::2]   ", fruits[::2])        # every second one
print("fruits[::-1]  ", fruits[::-1])       # backwards
print("len(fruits)   ", len(fruits))
"""),

md("""
A slice returns **a new list**. The original is untouched, exactly as with strings.

The right-hand bound never gets in. `fruits[1:3]` brings back two items, not three, and that
subtraction is the same one that makes `len` 4 while the last valid index is 3.
"""),

code("""
# FAILS ON PURPOSE. Four items, and index 4 is not one of them.
try:
    print(fruits[4])
except IndexError as e:
    print("IndexError:", e)

# Slicing, on the other hand, does not complain about going past the end.
print("fruits[1:99]:", fruits[1:99])
print("fruits[99:] :", fruits[99:])
"""),

md("""
The two lines at the bottom are the surprising ones. Indexing out of range raises `IndexError`, but
**slicing out of range raises nothing**: it trims to whatever is there and, when there is nothing,
hands back an empty list.

That asymmetry explains a common bug. A `data[0]` on an empty list blows up and tells you where. A
`data[:1]` on the same list returns `[]` and the program carries on empty-handed for another three
functions.

## Changing it in place
"""),

code("""
fruits = ["apple", "banana", "cherry", "blackcurrant"]

fruits[1] = "blackcurrant"          # a string will not allow this
print(fruits)

print()
for fruit in fruits:
    print(" -", fruit)

print()
print("Is apple there?", "apple" in fruits)
print("Is mango there?", "mango" in fruits)
print("How many blackcurrant:", fruits.count("blackcurrant"))
"""),

md("""
This is the deep difference from strings. `"hello"[0] = "H"` is a `TypeError`, because a string is
immutable and its methods always hand back a copy. A list does accept the assignment, and its methods
almost always change the one you already have.

## The methods that change the list
"""),

code("""
fruits = ["apple", "banana", "cherry"]
print("start           ", fruits)

fruits.append("orange")
print("append('orange')", fruits)

fruits.insert(1, "lemon")
print("insert(1,'lemon')", fruits)

fruits.remove("lemon")
print("remove('lemon') ", fruits)

taken = fruits.pop()
print("pop()           ", fruits, "· returned", repr(taken))

del fruits[0]
print("del fruits[0]   ", fruits)

fruits.extend(["kiwi", "pear"])
print("extend([...])   ", fruits)

fruits.clear()
print("clear()         ", fruits)
"""),

md("""
`pop` is the only one that does both things: it takes the item out **and** hands it back. Every other
one returns `None`.

That word, `None`, causes the most expensive mistake in the module.
"""),

code("""
# FAILS ON PURPOSE, and the line to blame raises nothing.
numbers = [3, 1, 2]
numbers = numbers.sort()        # looks reasonable and destroys the list

print("numbers is:", numbers, "· of type", type(numbers).__name__)

try:
    print(len(numbers))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
The assignment did not fail. `sort` sorted the list, returned `None`, and that `None` was stored over
the only reference to the sorted data. The list was lost on the very line that sorted it.

The `TypeError` arrives later, at the `len`, which is not where the problem is. It is the same shape
as review 3's function that printed instead of returning: **the error shows up far from its cause**.

The two ways to sort, and the difference between them.
"""),

code("""
original = [3, 1, 2]

returned = original.sort()
print("original.sort() returned", returned)
print("and the list ended up as", original)

print()
other = [3, 1, 2]
sorted_copy = sorted(other)
print("sorted(other) returned", sorted_copy)
print("and other is still    ", other)
print("same object?", sorted_copy is other)
"""),

md("""
`sort` sorts what you have and returns nothing. `sorted` leaves the original alone and hands you a
new list. Picking between them is one question: if anyone else needs the list in its original order,
`sorted`.

It is worth seeing it from the string side. `text.upper()` returns a copy and leaves `text` alone,
because it cannot do anything else. `list.sort()` can change things, so it does. Both behaviours are
consistent with the type, and mixing them up costs data.

## `remove` deletes one, not all of them
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Removing every banana with one remove.
fruits = ["apple", "banana", "cherry", "banana", "banana"]
fruits.remove("banana")

print(fruits)
print("Bananas left:", fruits.count("banana"))

# And when there are none left, then it does raise.
short = ["apple"]
try:
    short.remove("banana")
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
`remove` deletes **the first** match and stops. Two bananas were left and nobody said so.

The instinct is to wrap it in a loop over the list. That is the next trap, and the nastiest of the
four the slide lists.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Deleting while looping.
fruits = ["apple", "banana", "banana", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "banana":
        fruits.remove(fruit)

print("Asked to drop 3 bananas and got:", fruits)
print("Surviving bananas:", fruits.count("banana"))

print()
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    numbers.remove(n)          # "empty the list"

print("Asked to empty 6 items and got:", numbers)
"""),

md("""
One banana survived, and the list we were going to empty kept three items.

A `for` does not walk values, it walks positions. It goes to index 0, then 1, then 2. When you delete
the item at index 1, everything to its right shifts one place left, so whatever now sits at position
1 never gets visited: the loop is already on 2.

That is why exactly half survived in the second case. Every deletion pulls the list one place left
while the index also moves right, and the loop finishes halfway through.

Neither cell raised anything. That is the point.

The two clean ways out:
"""),

code("""
fruits = ["apple", "banana", "banana", "banana", "cherry", "date"]

# 1. Walk a copy and delete from the original.
for fruit in fruits.copy():
    if fruit == "banana":
        fruits.remove(fruit)
print("Walking a copy:      ", fruits)

# 2. Build a new list out of what stays. Almost always the better one.
fruits = ["apple", "banana", "banana", "banana", "cherry", "date"]
no_banana = [f for f in fruits if f != "banana"]
print("With a comprehension:", no_banana)
print("Original untouched:  ", fruits)
"""),

md("""
The second one changes nothing, and that is why it cannot get this wrong. A function that takes a list
and returns another can be tested with any input, while one that modifies what it was handed forces
you to check who else was using it.

That criterion is in this week's homework rubric, on the line saying no function may modify the list
it receives.

## Unpacking and nested lists
"""),

code("""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, "·", y, "·", z)

# The star collects whatever is left over, always into a list.
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
first, second, *rest = fruits
print(first, "·", second, "· rest:", rest, type(rest).__name__)

# A list can hold lists. The second bracket goes into the inner one.
nested = ["apple", "banana", "cherry", ["blackcurrant", "orange"]]
print("nested[3]   ", nested[3])
print("nested[3][1]", nested[3][1])

# And any iterable becomes a list.
print(list(range(1, 10)))
print(list("Hello"))
"""),

md("""
That `nested[3][1]` with two brackets in a row is the shape you will use all term to read structures
coming out of a file or a database. The first one picks the row, the second one the column.

---
# Block 3 · Tuples, sets and dictionaries

The other three exist because sometimes you need exactly what a list will not give you.

## Tuples

A tuple is a read-only list. Round brackets to build it, and it reads like a list.
"""),

code("""
point = (3, 4)

print("point[0]  ", point[0])
print("len(point)", len(point))

other = point + (5,)             # concatenating builds a new tuple
print("point + (5,)", other, "· point is still", point)

print("point * 2  ", point * 2)

x, y = point                     # unpacking
print("x =", x, "· y =", y)

# Swapping two variables is a tuple in disguise.
a, b = 1, 2
a, b = b, a
print("a =", a, "· b =", b)
"""),

code("""
# FAILS ON PURPOSE. A tuple does not accept assignment.
try:
    point[0] = 9
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
## The trap the course file carries

`Code013.py`, the tuple file in `01 - Basics/4th Module`, calls three methods that tuples do not
have. They are on lines 31, 50 and 117, and the file stops at the first one.

We are not going to fix them. They run here because reading each `AttributeError` teaches more than
reading an already clean version.
"""),

code("""
# FAILS ON PURPOSE. All three calls come from Code013.py and all three raise.
this_tuple = ("apple", "banana", "cherry")
another_tuple = ("orange", "mango", "grapes")

attempts = [
    ("line 31 · this_tuple.extend(another_tuple)", lambda: this_tuple.extend(another_tuple)),
    ("line 50 · this_tuple.copy()", lambda: this_tuple.copy()),
    ("line 117 · this_tuple.clear()", lambda: this_tuple.clear()),
]

for description, attempt in attempts:
    try:
        attempt()
        print(f"{description:<44} worked")
    except AttributeError as e:
        print(f"{description:<44} AttributeError: {e}")
"""),

md("""
All three messages say the same thing with a different name: `'tuple' object has no attribute ...`.

Instead of memorising which ones are missing, count them.
"""),

code("""
for kind in (list, tuple, set, dict):
    public = sorted(m for m in dir(kind) if not m.startswith("_"))
    print(f"{kind.__name__:<6}{len(public):>3} methods   {', '.join(public)}")
"""),

md("""
A tuple has **two** methods and a list has eleven. The two it keeps, `count` and `index`, are exactly
the two that only look and never change anything.

Tuples are not missing nine methods by oversight. `append`, `insert`, `remove`, `pop`, `sort`,
`reverse`, `clear` and `extend` all change things in place, and a tuple cannot do that. `copy` makes
no sense either: if nothing can change it, a copy and the original will never differ, so Python hands
you the same object back.

## The file's other claim, the one that does not raise

Lines 46 and 47 of `Code013.py` say that copying a tuple by assignment makes changes to the first one
show up in the second. The first half is true and the second half cannot be.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The claim is false, not the code.
tuple1 = ("apple", "banana", "cherry")
tuple2 = tuple1

print("Same object?", tuple1 is tuple2)
print("Same id:    ", id(tuple1) == id(tuple2))

tuple2 += ("orange",)            # looks like a change, and is not one

print()
print("tuple2:", tuple2)
print("tuple1:", tuple1, "· untouched")
print("still the same object?", tuple1 is tuple2)
"""),

md("""
They are the same object to begin with, exactly as happens with lists. And still nothing propagated,
because **there is no change to propagate**: `+=` on a tuple builds a new tuple and hangs the name
`tuple2` on it. The original object never found out.

That is the property that makes tuples useful. Hand a tuple to a function and you know it comes back
the way it left. With a list you have no such guarantee.

## The lonely comma
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Brackets do not make a tuple, the comma does.
one = (5)
other = (5,)

print("(5)  ->", one, "· type", type(one).__name__)
print("(5,) ->", other, "· type", type(other).__name__)

print()
print("len of the tuple:", len(other))
try:
    print(len(one))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`(5)` is the number five inside grouping brackets, the same ones in `(2 + 3) * 4`. No comma, no
tuple.

Where it bites hardest is on the way out of a function. `return (result)` returns the value and
`return (result,)` returns a one-element tuple, and whoever unpacks it sees two different things.

## Immutable does not mean frozen
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The tuple did not change, its contents did.
record = ("ID001", ["London", "Paris"])

print("before:", record)
record[1].append("Athens")
print("after: ", record)

print()
print("Can it be a dictionary key?")
try:
    {record: "luggage"}
except TypeError as e:
    print("TypeError:", e)

print("A tuple of immutables can:", {("ID001", "London"): "luggage"})
"""),

md("""
The tuple still has two items and is still the same tuple. What changed is the list sitting in its
second position, and the tuple has no way to stop it: all it guarantees is that its positions will
always point at the same objects, not that those objects will not change inside.

The `TypeError` below confirms it from another angle. To be a dictionary key a value has to be
*hashable*, and it only is when nothing it contains can change. A tuple with a list inside does not
qualify; a tuple of plain strings does.

That is the practical reason tuples exist in this course. A coordinate, a date or a compound
identifier can be a key. A list, never.
"""),

md("""
## Sets

A set holds unique values with no order. It cannot be indexed, and its reason to exist is set theory.
"""),

code("""
items = ["apple", "banana", "cherry", "apple", "banana"]
unique = set(items)
print(len(items), "->", len(unique), unique)

unique.add("orange")
unique.update(["mango", "grapes"])
print("after add and update:", len(unique), "items")

unique.remove("banana")          # raises if it is not there
unique.discard("kiwi")           # says nothing if it is not there
print("after remove and discard:", sorted(unique))

print()
print("is apple there?", "apple" in unique)

# FAILS ON PURPOSE. A set has no positions.
try:
    print(unique[0])
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`remove` raises `KeyError` when the item is missing and `discard` says nothing. Choosing between them
is a design decision: if a missing item is a bug, use `remove` and hear about it; if missing is
normal, `discard`.

## No order means no order
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Trusting the order of a set.
print("Typed {100, 2, 33} and out came:", {100, 2, 33})
print("Typed {'z', 'a', 'm'} and out came:", {"z", "a", "m"})

print()
numbers = {100, 2, 33}
print("Neither typed nor sorted:", list(numbers), "against", sorted(numbers))
"""),

md("""
It came out neither in the order it was typed nor sorted low to high. It came out in whatever order
the set's internal slots ended up in, which depends on each value's `hash`.

With strings it is even less predictable: Python seeds the `hash` of text randomly on every start, so
the same set can print differently tomorrow. If you are going to show a set to somebody, `sorted` is
not decoration.

## The operations, and a course comment that does not add up
"""),

code("""
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

print("union       ", sorted(set1 | set2))
print("intersection", sorted(set1 & set2))
print("difference  ", sorted(set1 - set2))
print("symmetric   ", sorted(set1 ^ set2))
print("isdisjoint  ", set1.isdisjoint(set2))
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code014.py line 159 says True and prints False.
small = {"a", "b", "c"}
big = {"c", "b", "a", "d", "e"}

print("small.issubset(big)  ", small.issubset(big))
print("small.issuperset(big)", small.issuperset(big), " <- the file says True")
print("big.issuperset(small)", big.issuperset(small), " <- this is what it meant")
"""),

md("""
The course file builds a set that does contain the other one and then asks the question backwards.
`issuperset` reads left to right: `small.issuperset(big)` asks whether the small one contains the big
one, and the answer is no.

It is the same kind of mistake as writing `a > b` when you meant `b > a`. Nothing raises, a perfectly
valid boolean comes back, and a condition written backwards lets through exactly the cases it was
supposed to stop.

## Why sets exist, measured
"""),

code("""
import timeit

N = 200_000
as_list = list(range(N))
as_set = set(as_list)
wanted = N - 1                   # worst case for the list: the last one

t_list = timeit.timeit(lambda: wanted in as_list, number=200)
t_set = timeit.timeit(lambda: wanted in as_set, number=200)

print(f"{N:,} items, 200 lookups each")
print(f"  in the list: {t_list * 1000:8.2f} ms")
print(f"  in the set:  {t_set * 1000:8.2f} ms")
print(f"  the set was {t_list / t_set:,.0f} times faster")
"""),

md("""
The exact number depends on the machine and on what Colab happens to be busy with, but the order of
magnitude does not move: the gap is counted in thousands of times, not in percentages.

The reason is that `in` on a list compares item by item until it finds one, so the work grows with
the size. A set hashes the value you are looking for and goes straight to the slot where it would
have to be, and that work is the same with ten items as with two hundred thousand.

That is the real criterion for reaching for a set: asking "is this in here?" many times over a large
collection.
"""),

md("""
## Dictionaries

They hold key and value pairs. It is the collection closest to an object, which is why it comes last
before classes: in week 3 you will find out that a Python object keeps its attributes in an actual
dictionary.
"""),

code("""
student = {
    "name": "Ana",
    "degree": "Mechatronics",
    "term": 2,
}

print(student["name"])
print(student.get("degree"))

print()
print("get for something missing:  ", student.get("grant"))
print("get with a default:         ", student.get("grant", False))
print("did the dictionary change?  ", student)
"""),

code("""
# FAILS ON PURPOSE. Brackets do not forgive a missing key.
try:
    print(student["grant"])
except KeyError as e:
    print("KeyError:", e)
"""),

md("""
`get` returns `None` and carries on; brackets stop the program. The choice is the same one as between
`remove` and `discard`, and it is settled by one question: if the field is missing, is that an error
or is that normal?

This week's homework asks for `get` under the "Access" criterion exactly where the field may be
missing. A grant may not exist. A name may not be missing, and there brackets are better because they
tell you.
"""),

code("""
student["grant"] = "partial"     # assigning a new key creates it
student["term"] = 3              # assigning an existing one replaces it

print("Keys:  ", list(student.keys()))
print("Values:", list(student.values()))
print()
for key, value in student.items():
    print(f"  {key:<8}{value}")

print()
print("has degree?", "degree" in student)
print("how many fields:", len(student))

removed = student.pop("grant")
print("pop returned:", repr(removed), "·", len(student), "fields left")
"""),

md("""
`items()` hands back one tuple per pair, which is why the `for` above can unpack it into two names. It
is the same tuple unpacking from a few cells ago, applied without saying so.

Looping over the dictionary alone, without `.items()`, walks the keys. That detail confuses people at
first because it looks like it ought to walk the values.

## Dictionaries inside dictionaries
"""),

code("""
group = {
    "A01": {"name": "Ana", "grades": [8, 9, 10]},
    "A02": {"name": "Beto", "grades": [7, 6]},
    "A03": {"name": "Carla", "grades": []},
}

for student_id, data in group.items():
    marks = data["grades"]
    average = sum(marks) / len(marks) if marks else None
    print(f"{student_id}  {data['name']:<7}{len(marks)} marks  average {average}")
"""),

md("""
That dictionary-of-dictionaries shape is how almost all real data arrives: an API response, a JSON
file, a database row.

It is also the last stop before classes. A dictionary groups data that belongs together, but it does
not bring along the functions that work on it, so the average gets computed outside and nothing
guarantees that every dictionary has the same keys. A class solves both at once, and that is week 3.
"""),

md("""
---
# Block 4 · Copying against renaming

The block people forget most, and the one that comes back in week 6 under another name.

## Predict before you run

What does the last line print?

```python
numbers = [1, 2, 3]
copy = numbers

copy.append(4)

print(len(numbers))
```

- **A.** 3, because `copy` is a separate list.
- **B.** 4, because both names point at the same list.
- **C.** An error, a list cannot be assigned to another variable.
- **D.** 7, because the two lists get concatenated.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The quiz answer, with the proof beside it.
numbers = [1, 2, 3]
copy = numbers

copy.append(4)

print("len(numbers):", len(numbers))
print("numbers:", numbers)
print("copy:   ", copy)
print()
print("same object?", numbers is copy)
print("same id?    ", id(numbers) == id(copy))
"""),

md("""
The answer is **B**.

| Step | Statement | numbers | copy | Same object? |
|---|---|---|---|---|
| 1 | `numbers = [1, 2, 3]` | `[1, 2, 3]` | does not exist | |
| 2 | `copy = numbers` | `[1, 2, 3]` | `[1, 2, 3]` | yes |
| 3 | `copy.append(4)` | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` | yes |
| 4 | `len(numbers)` | 4 | 4 | yes |

The equals sign never copies a list's contents. It copies the reference, which is the address where
the list lives. After line 2 there are two names and **one** list, and `append` changes it no matter
which of the two names you go through.

With numbers and strings it looks like it does copy, which is why the mistake is so common. What
happens there is that they are immutable: since they cannot be changed in place, any operation builds
a new value and the original stays intact anyway. The difference was always there, it just did not
show.

## The three real ways to copy
"""),

code("""
originals = [1, 2, 3]

by_method = originals.copy()
by_function = list(originals)
by_slice = originals[:]

originals.append(99)

print("originals ", originals)
print("copy()    ", by_method)
print("list()    ", by_function)
print("slice [:] ", by_slice)
print()
for name, value in [("copy()", by_method), ("list()", by_function),
                    ("[:]", by_slice)]:
    print(f"{name:<10} is it the same object as originals? {value is originals}")
"""),

md("""
All three do the same thing. `copy()` is the most explicit and the one worth writing; `list()` also
converts from a tuple or a set, and `[:]` is the shortest and the hardest to read.

Dictionaries and sets have their own `copy()` and behave the same way.

## The copy is shallow
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. copy() copied the outer list, not the inner ones.
teams = [["Ana", "Beto"], ["Carla", "Diego"]]
backup = teams.copy()

backup[0].append("Elena")

print("backup:", backup)
print("teams: ", teams, " <- it changed too")
print()
print("is the outer list the same?", teams is backup)
print("is the inner one the same? ", teams[0] is backup[0])
"""),

md("""
The first question says `False` and the second says `True`. `copy()` built a new outer list and filled
it with the same two references the original held. The inner lists were never copied.

It is called a shallow copy, and the slide mentions it in the side note. The deep version lives in
the standard library.
"""),

code("""
from copy import deepcopy

teams = [["Ana", "Beto"], ["Carla", "Diego"]]
shallow = teams.copy()
deep = deepcopy(teams)

shallow[0].append("Elena")
deep[1].append("Fernanda")

print("teams:   ", teams)
print("shallow: ", shallow)
print("deep:    ", deep)
print()
print("is the inner one the same as the original?")
print("  shallow:", teams[0] is shallow[0])
print("  deep:   ", teams[1] is deep[1])
"""),

md("""
`teams` picked up Elena, who was added to the shallow copy, and did not pick up Fernanda, who was
added to the deep one.

`deepcopy` walks the whole structure and duplicates everything it finds. It costs more and is rarely
needed, but when it is needed nothing else will do.

## The multiplier that looks like a shortcut
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Three rows that are one row.
grid = [[0] * 3] * 3
print("freshly built:", grid)

grid[0][0] = 9
print("after grid[0][0] = 9:", grid)
print("are the three rows the same object?",
      grid[0] is grid[1] is grid[2])

print()
good = [[0] * 3 for _ in range(3)]
good[0][0] = 9
print("with a comprehension:", good)
print("same object?", good[0] is good[1])
"""),

md("""
`[[0] * 3] * 3` repeats the reference to **one** inner list three times. Changing one item changes all
three rows, and yet `[0] * 3` for a single row works fine, because zero is immutable and there is
nothing to share.

The comprehension evaluates `[0] * 3` once per turn and builds three separate lists.

## Where all of this is going

Keep these three cells. The same mechanism shows up twice more in the course, wearing a different
costume.

In **week 3**, when an object holds a list and two objects end up looking at the same one. In
**week 6**, when an attribute written on the class instead of in the constructor gets shared across
every instance and nobody can work out why the second customer's cart already has the first
customer's products in it.

And you have seen it once already, in review 3: the list used as a function's default value is this
same problem. One list, many names, and no warning.
"""),

md("""
---
## Four errors from this module

**Storing what `sort` returns.** `items = items.sort()` leaves the variable as `None` and loses the
data. `sort` sorts and returns nothing; `sorted` does return.

**Index out of range.** The last position of a list of `n` items is `n - 1`. Indexing raises
`IndexError`, but slicing out of range returns a short or empty list and carries on.

**A key that is not there.** Brackets raise `KeyError`. Use `get` where the field may be missing, and
brackets where its absence is a bug you want to see.

**Editing a list while looping over it.** The loop skips items and says nothing. Walk a copy, or
better, build a new list out of what stays.

Of the four, three ran above without raising anything.
"""),

md("""
---
# Exercises

The solutions are at the very bottom of the notebook.

### Exercise 1 · The four, from the same data

Take the list `["red", "blue", "red", "green"]` and convert it to a tuple, a set and a dictionary with
`dict.fromkeys`. Print all four with their length.

Explain in a comment why two of them lost an item.

### Exercise 2 · Indexes and slices

With `months = ["jan", "feb", "mar", "apr", "may", "jun"]`, print the third one, the last one, the
first quarter, the second quarter, the months in even positions, and the list backwards.

Then ask for `months[6]` and catch the error. Compare it with what `months[6:]` returns.

### Exercise 3 · Sorting without losing

With `prices = [340, 120, 890, 55]`, print the sorted list without changing the original. Then sort it
in place. Show what each of the two operations returns.

### Exercise 4 · The filter that skips

Write a loop that removes every zero from `[0, 1, 0, 0, 2, 3, 0]` by deleting while it walks. Show how
many zeros are left.

Then solve it with a comprehension and check that the original was not touched.

### Exercise 5 · The lonely comma

Write a function `wrap(value)` that returns its argument in a one-element tuple. Test it with a number
and with a string, and print the type and the length of the result.

Then write the wrong version, without the comma, and explain in a comment what happens when the
argument is a five-letter string.

### Exercise 6 · Sets that answer questions

With `enrolled = {"Ana", "Beto", "Carla", "Diego"}` and `attended = {"Beto", "Diego", "Elena"}`,
answer with set operations: who was absent, who attended without being enrolled, who appears in both
lists, and how many people are involved in total.

### Exercise 7 · `get` against brackets

With a list of student dictionaries where some carry `"grant"` and some do not, print one line per
student with their name and their grant. Do it first with brackets, catch the `KeyError` and say which
student it stopped on. Then do it with `get`.

### Exercise 8 · Copying for real

Write a function `add_student(group, name)` that returns a new group with the student added, without
changing the one it received. Prove with `is` that the result is a different list.

Then write the version that does modify it and show the difference across the same two calls.

### Exercise 9 · The homework

With a list of student dictionaries, each with `name`, `degree`, `grades` and sometimes `grant`, write
three functions that return:

1. The students who passed, averaging 7 or more.
2. The group average.
3. The degrees without repeats.

The degrees come out of a set, not a loop that checks whether it is already there. The grant is read
with `get`. None of the three modifies the list it receives, and you have to prove it by printing the
original list at the end.
"""),

md("""
---
## Three things to take away

**Three questions pick the collection.** Does order matter, will it change, can there be duplicates.
Those three settle it, and settling them wrong costs data lost in silence.

**List methods change the list and return `None`.** Exactly the opposite of string methods, which
return a copy and touch nothing. `sort` against `sorted` is the pair worth memorising.

**Assigning a list does not copy it.** It leaves two names on one object, and `id` or `is` proves it
in a line. In week 6 this comes back as the class attribute every instance shares.

The next review is the last one: what a program does when something goes wrong. Almost every error in
this notebook shows up there again, `IndexError`, `KeyError`, `ValueError` and `TypeError`, but caught
with `try` instead of suffered.
"""),

md("""
---
# Solutions

### Exercise 1

```python
colours = ["red", "blue", "red", "green"]

as_tuple = tuple(colours)
as_set = set(colours)
as_dict = dict.fromkeys(colours, 0)

for name, value in [("list", colours), ("tuple", as_tuple),
                    ("set", as_set), ("dict", as_dict)]:
    print(f"{name:<7}{len(value)}  {value}")

# The set and the dictionary lost one "red". Both store unique values, the set
# in its items and the dictionary in its keys, so the second "red" was never
# added. The list and the tuple allow duplicates and kept all four.
```

### Exercise 2

```python
months = ["jan", "feb", "mar", "apr", "may", "jun"]

print("third:    ", months[2])
print("last:     ", months[-1])
print("q1:       ", months[:3])
print("q2:       ", months[3:])
print("even pos: ", months[::2])
print("backwards:", months[::-1])

try:
    print(months[6])
except IndexError as e:
    print("IndexError:", e)

print("months[6:] returns:", months[6:])
```

`months[6]` raises and `months[6:]` returns `[]`. The difference matters: an index out of range tells
you where the problem is, and a slice out of range lets you carry on with an empty list that later
turns into an average of zero or a division by zero.

### Exercise 3

```python
prices = [340, 120, 890, 55]

sorted_copy = sorted(prices)
print("sorted returned:", sorted_copy)
print("prices is still:", prices)

returned = prices.sort()
print("sort returned:  ", returned)
print("prices ended as:", prices)
```

`sorted` returns a list and touches nothing. `sort` returns `None` and leaves the list sorted. Storing
what `sort` returns is error number one in this module.

### Exercise 4

```python
numbers = [0, 1, 0, 0, 2, 3, 0]
for n in numbers:
    if n == 0:
        numbers.remove(n)

print("deleting while walking:", numbers)
print("zeros left:", numbers.count(0))

numbers = [0, 1, 0, 0, 2, 3, 0]
no_zeros = [n for n in numbers if n != 0]
print("with a comprehension:", no_zeros)
print("original untouched:", numbers)
```

Zeros are left. Every deletion pulls the list left while the loop index moves right, so the item that
took the deleted one's place is never visited. The comprehension cannot fail that way because it
changes nothing while it reads.

### Exercise 5

```python
def wrap(value):
    return (value,)


def wrap_wrong(value):
    return (value)


for probe in [7, "hello"]:
    good = wrap(probe)
    bad = wrap_wrong(probe)
    print(f"{repr(probe):<9} good: {good} len {len(good)}   "
          f"bad: {repr(bad)} type {type(bad).__name__}")

# With the string "hello", the version without the comma returns the string
# itself. len gives 5 instead of 1, and a for over the result walks letters
# instead of walking one item. The mistake does not raise, it just hands back
# something else.
```

### Exercise 6

```python
enrolled = {"Ana", "Beto", "Carla", "Diego"}
attended = {"Beto", "Diego", "Elena"}

print("absent:       ", sorted(enrolled - attended))
print("not enrolled: ", sorted(attended - enrolled))
print("in both:      ", sorted(enrolled & attended))
print("people in all:", len(enrolled | attended))
```

All four answers are one operator each. The version with loops and flags runs twenty lines and gets
the third case wrong.

### Exercise 7

```python
students = [
    {"name": "Ana", "grant": "partial"},
    {"name": "Beto"},
    {"name": "Carla", "grant": "full"},
]

try:
    for student in students:
        print(student["name"], "->", student["grant"])
except KeyError as e:
    print("KeyError:", e, "· it stopped on Beto")

print()
for student in students:
    print(student["name"], "->", student.get("grant", "no grant"))
```

The first version got as far as Ana and stopped. Brackets are right for `"name"`, which always has to
be there, and wrong for `"grant"`, which may legitimately be missing.

### Exercise 8

```python
def add_student(group, name):
    fresh = group.copy()
    fresh.append(name)
    return fresh


def add_student_mutating(group, name):
    group.append(name)
    return group


group = ["Ana", "Beto"]
result = add_student(group, "Carla")
print("returned:", result)
print("original:", group)
print("same object?", result is group)

print()
group = ["Ana", "Beto"]
result = add_student_mutating(group, "Carla")
print("returned:", result)
print("original:", group, " <- it changed too")
print("same object?", result is group)
```

The second one is dangerous precisely because it also returns. Whoever calls it sees a list with Carla
in it and assumes their own was left alone.

### Exercise 9

```python
STUDENTS = [
    {"name": "Ana", "degree": "Mechatronics", "grades": [8, 9, 10],
     "grant": "partial"},
    {"name": "Beto", "degree": "Systems", "grades": [6, 7, 5]},
    {"name": "Carla", "degree": "Mechatronics", "grades": [9, 9, 8]},
    {"name": "Diego", "degree": "Industrial", "grades": [7, 7, 7]},
]


def average_of(student):
    marks = student["grades"]
    return sum(marks) / len(marks) if marks else None


def get_passing(students, minimum=7):
    return [s for s in students
            if average_of(s) is not None and average_of(s) >= minimum]


def get_group_average(students):
    averages = [average_of(s) for s in students if average_of(s) is not None]
    return sum(averages) / len(averages) if averages else None


def list_degrees(students):
    return sorted({s["degree"] for s in students})


print("Passing:", [s["name"] for s in get_passing(STUDENTS)])
print(f"Group average: {get_group_average(STUDENTS):.2f}")
print("Degrees:", list_degrees(STUDENTS))
print()
for student in STUDENTS:
    print(f"  {student['name']:<7}{student.get('grant', 'no grant')}")

print()
print("The original list, untouched:")
for student in STUDENTS:
    print(" ", student)
```

`list_degrees` uses a set comprehension, which is the short way to write `set(...)` around what comes
out. All three functions read and none of them writes, so the last print shows the list exactly as it
was declared.

`average_of` returns `None` for a student with no grades recorded, and both functions that use it have
to decide what to do with that `None`. That is not an annoying detail, it is the same decision as
review 3: there is no average is not the same as the average is zero.
"""),

]

write(OUT / "en" / "w01.4.ipynb", en)
print("wrote", OUT / "en" / "w01.4.ipynb")
