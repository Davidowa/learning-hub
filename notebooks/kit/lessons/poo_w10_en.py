"""notebooks/programacion-orientada-a-objetos/en/w10.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w10.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/4th Module/Code012.py
                  (lists: indexes, slices, append, insert, remove, pop, copy)
              docs/en/courses/python-course/01 - Basics/4th Module/Code016.py
                  (array.array and appending a type that does not fit)
              docs/en/courses/python-course/01 - Basics/4th Module/Code017.py
                  (comprehensions, map, filter, generators, unpacking, zip,
                   stack and queue)

Code012.py and Code016.py run to the end, checked.

Code017.py does NOT run to the end. Its line 292 is numbers.append(*new_numbers)
and it raises TypeError: list.append() takes exactly one argument (3 given). The
file stops there, so its last ninety-eight lines (unpacking inside a literal,
dictionary unpacking, zip, the stack and the queue) never run in the original.
The notebook quotes the line as a pitfall, runs it inside a try, and then brings
the dead stretch back to life by hand.

Three other measured things that do not match what the repository says, all
quoted without correcting them:

  Code017.py lines 257 and 261 announce "gen: 112" and "com: 824456". Today that
  same measurement gives other values, because getsizeof measures the internal
  representation and that changes between Python versions. The file's conclusion
  still holds.

  Code017.py lines 366 to 369 have the condition inverted: the comment promises
  to avoid popping an empty stack and the if calls pop exactly when it is empty.
  It never fires because the stack holds two items, and because the file had
  already stopped two hundred lines earlier.

  Code016.py line 55 leaves an append commented out with the message "an integer
  is required (got type str)". Run for real today, the message is another one.

Code017.py line 12 defines sum and covers Python's for the rest of the file.

Week 9 ended pointing at collections. This notebook starts there and ends
pointing at week 11's exception handling.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 10
## Topic 4 · Advanced functions and structures

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Four ways of holding several things in one variable, how a list grows inside, and what can be done
without touching the disk.

Last week ended by splitting a script into functions. Every one of those functions took a collection and
returned another, and not one of them asked which collection was the right one. This week is that
question.

By the end you will be able to:

1. Choose between list, tuple, set and dictionary with three questions about order, change and how you
   search.
2. Explain what a dynamic array is and why appending at the end is cheap and inserting at the front is
   not.
3. Filter, transform and group in memory with comprehensions and with an accumulating dictionary.
4. Tell copying from sharing, and say when the equals sign left two names on one object.
5. Read an unpacking with an asterisk and say how many arguments arrive on the other side.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Twelve fail on purpose and carry a comment saying so.

Nine of the twelve **raise no exception at all**. Among them is the most expensive of the lot: the one
that deletes from a list while walking it, never looks at two of the six names, and hands back a shorter
list that looks perfectly reasonable.
"""),

md("""
---
# Block 1 · The four collections

List, tuple, set and dictionary. All four hold several things in one variable and all four are walked
with the same `for`, so at first sight they look interchangeable.

They are not. Each one answers a different question quickly and every other question slowly.
"""),

code("""
fruits_list = ["apple", "banana", "cherry", "apple"]
fruits_tuple = ("apple", "banana", "cherry", "apple")
fruits_set = {"apple", "banana", "cherry", "apple"}
fruits_dict = {"apple": 32, "banana": 18, "cherry": 95}

for name, collection in [("list", fruits_list), ("tuple", fruits_tuple),
                         ("set", fruits_set), ("dictionary", fruits_dict)]:
    print(f"  {name:<12}{len(collection)} items   {collection}")

print()
print("The four fruits written, once they are stored:")
print("  list:       ", len(fruits_list), "<- kept the repeated apple")
print("  set:        ", len(fruits_set), "<- the repeat is gone")
print()
print("Does the list have an order?    ", fruits_list[0], "is still the first")
print("Can the tuple be modified?       no, and that is why it works as a key:",
      {("a", 1): "ok"}[("a", 1)])
"""),

md("""
Four collections written from the same handful of fruits, and the set already came back with three.

A set does not keep repeats. That is not a bug, it is its definition, and it is exactly what makes it
useful: asking whether something is in there is immediate, because it never stores a pile of copies of
the same value.

The three questions that pick the container, in this order:

1. **Does the order matter?** If it does, list or tuple.
2. **Will it change?** If it will not, tuple.
3. **Do you search by key?** If you do, dictionary. If you only ask whether it is there, set.

## What asking "is it in there?" costs
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Searching a list for what a set answers straight away.
import time

STUDENT_IDS = [f"A{n:06d}" for n in range(200_000)]
AS_A_SET = set(STUDENT_IDS)
WANTED = "A199999"           # the last one, which is the list's worst case

start = time.perf_counter()
for _ in range(20):
    WANTED in STUDENT_IDS
with_list = time.perf_counter() - start

start = time.perf_counter()
for _ in range(20):
    WANTED in AS_A_SET
with_set = time.perf_counter() - start

print("Both answer the same thing:", WANTED in STUDENT_IDS, WANTED in AS_A_SET)
print()
print(f"20 searches in the list: {with_list:.4f} s")
print(f"20 searches in the set:  {with_set:.6f} s")
print(f"The list took about {with_list / with_set:,.0f} times longer.")
"""),

md("""
The same answer, the same `in`, and a gap of hundreds of times that the cell has just measured in your
own session.

`x in list` walks the list from start to finish comparing one by one. If the value sits at the end, or
if it is not there at all, it walks all two hundred thousand. `x in set` works out where that value
would have to be and looks only there.

It is error 03 on the slide and it is the only one this session you cannot see by reading the code. The
line is identical in both cases. What changes is what somebody wrote three screens earlier.

**Rule:** if a collection exists only to be asked whether something is in it, store it as a set.

## The equals sign does not copy
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Two names, one object.
numbers = [1, 2, 3, 4]
copy = numbers

copy.append(5)

print("numbers:", numbers)
print("copy:   ", copy)
print()
print("Are they equal?", numbers == copy)
print("Are they the same object?", numbers is copy)
print("Address of numbers:", id(numbers))
print("Address of copy:   ", id(copy))
print()
real_copy = numbers.copy()
real_copy.append(6)
print("With .copy():")
print("  numbers:  ", numbers)
print("  real_copy:", real_copy)
print("  the same object?", numbers is real_copy)
"""),

md("""
`copy = numbers` copied nothing. It put a second name on the same list.

`==` asks whether the contents are equal. `is` asks whether it is the same object, and that is the
question that matters here: `id()` returns the same number for both names.

It is error 02 on the slide. `Code012.py`, on line 109, puts it in these words: *"You cannot copy a list
simply by typing list2 = list1"*, and it is fixed by asking for the copy, with `.copy()` or with
`list(...)`.

The same thing happens when a list travels as an argument: the function receives the name, not a copy,
and whatever it does inside shows up outside. That was week 9's default list, seen from the other side.

## Predict before you run

```python
students = ["Ana", "Luis", "Sofia", "Marco", "Paula", "Ruben"]

for student in students:
    if student.startswith(("L", "S", "M")):
        students.remove(student)

print(students)
```

- **A.** `['Ana', 'Paula', 'Ruben']`, the loop removed all three.
- **B.** `['Ana', 'Sofia', 'Paula', 'Ruben']`, it skipped one.
- **C.** `[]`, the loop emptied the list.
- **D.** `RuntimeError`, the list changed size while it was being walked.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Deleting inside the for that walks the list.
students = ["Ana", "Luis", "Sofia", "Marco", "Paula", "Ruben"]

visited = []
for student in students:
    visited.append(student)
    if student.startswith(("L", "S", "M")):
        students.remove(student)

print("Left:", students)
print("The loop looked at:", visited, "<-", len(visited), "of 6")
print()
print("Did all three go?", not any(s[0] in "LSM" for s in students))
print()

students = ["Ana", "Luis", "Sofia", "Marco", "Paula", "Ruben"]
students = [s for s in students if not s.startswith(("L", "S", "M"))]
print("With a comprehension:", students)
"""),

md("""
The answer is **B**.

The `for` carries an index inside it that moves on one at a time. When `remove` takes `Luis` out of
position 1, `Sofia` shifts down into position 1, but the index is already on 2, so `Sofia` never gets
looked at. That is why the loop visited only four of the six names.

No exception. No warning. A shorter list that looks perfectly reasonable.

It is error 01 on the slide and it is the most expensive of the session, because the symptom turns up a
long way away: the program carries on, and the leftover name reappears three functions later.

**The fix is not to delete while you walk.** You build a new list with whatever stays, which also says
in one line what the loop was saying in four.

## What a set throws away without saying so
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A set to drop the repeats, and the order goes with them.
ENTRIES = ["A001", "A004", "A002", "A001", "A003", "A002"]

no_repeats = set(ENTRIES)
print("Entries:", ENTRIES, f"({len(ENTRIES)})")
print("Set:    ", no_repeats, f"({len(no_repeats)})")
print()
print("First one entered, according to the list:", ENTRIES[0])
print("First element of the set:                ", next(iter(no_repeats)))
print("Does the set keep the order?", list(no_repeats) == ["A001", "A004", "A002", "A003"])
print()
in_order = list(dict.fromkeys(ENTRIES))
print("No repeats and in order:", in_order)
"""),

md("""
The set dropped the repeats and threw away the order they arrived in along with them.

That is fine as long as nobody cares about the order. The trouble starts when somebody did care and
never said so: the collection looks clean, it has the right number of elements, and the first one is no
longer the first one.

`dict.fromkeys` works as a trick because Python dictionaries do keep insertion order and they do not
take repeated keys either. It drops the duplicates and respects who arrived first.

## The tuple that cannot be corrected
"""),

code("""
# FAILS ON PURPOSE. A tuple for a value that does change.
student = ("A001", "Ana Robles", 9.2)

try:
    student[2] = 9.5
except TypeError as e:
    print("TypeError:", e)

print()
student = student[:2] + (9.5,)        # the whole tuple has to be built again
print("Corrected by hand:", student)
print()
as_a_list = ["A001", "Ana Robles", 9.2]
as_a_list[2] = 9.5
print("With a list:", as_a_list)
print()
print("And even so the tuple does something the list cannot:")
MARKS = {("A001", "COM102"): 9.5, ("A002", "COM102"): 7.8}
print("  compound key:", MARKS[("A001", "COM102")])
try:
    {["A001", "COM102"]: 9.5}
except TypeError as e:
    print("  with a list as the key:", e)
"""),

md("""
`'tuple' object does not support item assignment`.

It is error 04 on the slide. A tuple for a mark forces you to rebuild the whole record every time
somebody corrects a decimal, and the correction looks ugly precisely because the container was the wrong
choice.

The second half teaches the opposite, which is the reason tuples exist at all: **a list cannot be a
dictionary key and a tuple can**. The reason is that same immutability. A key that can change after
being stored would leave the dictionary looking in the wrong place.
"""),

md("""
---
# Block 2 · Dynamic arrays

A Python list is not a row of slots of exactly the right size. It is a block of memory with room to
spare, and it moves to a bigger one when it fills up.

That is not trivia. It explains why `append` is almost free and why `insert(0, x)` is not.
"""),

code("""
from sys import getsizeof

items = []
before = getsizeof(items)
print(f"{'length':>7}{'bytes':>8}{'moved':>8}")
print(f"{0:>7}{before:>8}{'':>8}")

for n in range(1, 40):
    items.append(n)
    now = getsizeof(items)
    if now != before:
        print(f"{n:>7}{now:>8}{'yes':>8}")
        before = now

print()
print("Final length:", len(items), " bytes:", getsizeof(items))
print("Bytes per item if it fitted exactly:", 8, "(one reference)")
print("Bytes going spare right now:", getsizeof(items) - getsizeof([]) - 8 * len(items))
"""),

md("""
The list does not grow one slot at a time. It stays the same size several times in a row and then jumps.

That jump is the move: when the reserved room runs out, Python asks for a bigger block, copies what was
there and carries on. Since the new block comes with room to spare, the next `append` calls cost
nothing, and that is how the price of the copy gets spread across many cheap calls.

That is a **dynamic array**, and it is the technical name for what you have been using since day one.

## Appending at the end against inserting at the front
"""),

code("""
import time

N = 40_000

start = time.perf_counter()
at_the_end = []
for i in range(N):
    at_the_end.append(i)
cost_end = time.perf_counter() - start

start = time.perf_counter()
at_the_front = []
for i in range(N):
    at_the_front.insert(0, i)
cost_front = time.perf_counter() - start

print(f"{N:,} append(x):     {cost_end:.4f} s")
print(f"{N:,} insert(0, x):  {cost_front:.4f} s")
print(f"Inserting at the front took about {cost_front / cost_end:,.0f} times longer.")
print()
print("Both lists are the same length:", len(at_the_end) == len(at_the_front))
print("And hold the opposite:", at_the_end[:3], "against", at_the_front[:3])
"""),

md("""
The same number of insertions, the same final length, and an enormous difference in time.

`append` writes into the first free slot at the end. `insert(0, x)` has to shift **every** element
already in the list one place to the right to make room for the new one. With forty thousand elements
that is eight hundred million moves spread across the loop.

If you genuinely need to push and pop at both ends, the standard library has `deque`, which
`Code017.py` uses at the end for its queue example.

## When every value is of the same type
"""),

code("""
import array

# Code016.py, lines 26 to 51, as it stands
array1 = array.array('i', [1, 2, 3, 4, 5])
array1.append(6)
print(array1)
array1.insert(0, 0)
print(array1)
array1.pop(0)
print(array1)
array1.remove(6)
print(array1)
print(array1[0])

print()
print("Size of each slot, in bytes:", array1.itemsize)
thousand_list = list(range(1000))
thousand_array = array.array('i', range(1000))
print("1000 integers in a list:  ", getsizeof(thousand_list), "bytes")
print("1000 integers in an array:", getsizeof(thousand_array), "bytes")
print(f"The array takes about {getsizeof(thousand_array) / getsizeof(thousand_list):.0%} of what the list takes.")
"""),

md("""
`Code016.py` runs to the end and its five outputs match what its comments say.

The memory difference comes out of what each one stores. The list stores **references**: eight bytes per
slot pointing at an integer object that lives somewhere else. The `array` stores the numbers themselves,
four bytes each, packed together.

That is why the `array` is smaller and why it takes only one type. And it is why, for ninety per cent of
what you are going to write, the list is the answer: memory starts to matter when there are millions.
"""),

code("""
# FAILS ON PURPOSE. Line 55 of Code016.py, the one the file left commented out.
import array

array1 = array.array('i', [1, 2, 3, 4, 5])

try:
    array1.append("7")
except TypeError as e:
    print("TypeError:", e)

print()
print("The array is untouched:", array1)
print()
mixed = [1, "two", 3.0, True, None]
print("And a list takes the mixture without a word:", mixed)
print("Types inside:", [type(x).__name__ for x in mixed])
"""),

md("""
`Code016.py` leaves that line commented out on its line 55, with the error message written beside it:
*"an integer is required (got type str)"*. Run for real, today it says something else.

It is the same business as the two `getsizeof` numbers, now with text instead of a number: **an
exception's message is not part of the contract**. It can change between Python versions with no notice,
which is why `except` clauses are written by type and never by comparing the message string.

That the `array` complains at all is the useful half of this. **A container that restricts catches the
error on the line that caused it.** The list below takes five different types without a murmur, and if
that was an oversight, it surfaces much later, when somebody tries to add them up.
"""),

md("""
---
# Block 3 · Processing data in memory

Filter, transform and group before anything reaches the disk. Next week there will be files and this
will still be the same work, with a read in front of it.
"""),

code("""
# Code017.py, lines 147 to 208: the same filter written three ways
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = []
for product in products:
    if product[1] >= 10:
        filtered.append(product)
print("With a for:          ", filtered)

filtered = list(filter(lambda product: product[1] >= 10, products))
print("With filter:         ", filtered)

filtered = [product for product in products if product[1] >= 10]
print("With a comprehension:", filtered)

print()
students = [{"name": "Ana", "mark": 9.1}, {"name": "Luis", "mark": 6.4},
            {"name": "Sofia", "mark": 8.0}]
passing = [s["name"] for s in students if s["mark"] >= 7]
print("Passing:", passing)
print("Marks:  ", [s["mark"] for s in students])
print("Scaled: ", [round(s["mark"] * 10) for s in students])
"""),

md("""
Three ways of writing the same filter and one single answer.

A comprehension reads left to right in three beats: **what I keep**, **where it comes from**, **on what
condition**. It replaces the four-line `for` with an `append` inside it, which is exactly the pattern
`Code017.py` teaches first and then rewrites.

`filter` and `map` do the same job and hardly anyone reaches for them today, because the comprehension
says the condition on the same line and does not force you to read a `lambda`.

**When not to use it:** if it needs two conditions and an `else`, the ordinary `for` reads better.

## The generator that only works once
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Walking twice over something you only walk once.
MARKS = [9.1, 6.4, 8.0, 7.5, 5.9]

squares = (n * n for n in MARKS)

first_pass = list(squares)
second_pass = list(squares)

print("First pass: ", [round(x, 2) for x in first_pass])
print("Second pass:", second_pass, "<- empty, and nobody said a word")
print()

passing = (n for n in MARKS if n >= 7)
print("How many passing?", sum(1 for _ in passing))
print("And the average of those?", "cannot be done, it is used up:", list(passing))
print()
as_a_list = [n for n in MARKS if n >= 7]
print("With a list, as many times as you like:", len(as_a_list), "and average",
      round(sum(as_a_list) / len(as_a_list), 2))
"""),

md("""
The second pass returned an empty list and the program carried on as if nothing had happened.

A generator does not store the values, it produces them while you walk it. When it reaches the end it
stays there, and walking it again resets nothing: it hands back zero elements. `sum` over a spent
generator is zero, and a zero divided by a count that came from somewhere else is an average of zero
that looks like a real figure.

That is the actual difference from a comprehension, not the syntax. Round brackets against square
brackets is the symptom; underneath, **one stores and the other produces**.

## The numbers that grew old inside a comment
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Two numbers written by hand in Code017.py.
from sys import getsizeof
import sys

values_gen = (x * 2 for x in range(100000))
values_com = [x * 2 for x in range(100000)]

print("What Code017.py says on its lines 257 and 261:")
print("   gen: 112")
print("   com: 824456")
print()
print("What this session measures, with", f"Python {sys.version_info.major}.{sys.version_info.minor}:")
print("   gen:", getsizeof(values_gen))
print("   com:", getsizeof(values_com))
print()
print("Do they match?", getsizeof(values_gen) == 112 and getsizeof(values_com) == 824456)
print("Is what the file wanted to teach still true?",
      getsizeof(values_gen) < getsizeof(values_com) / 100)
"""),

md("""
Neither of the two numbers in the comment is today's number, and the file's conclusion is still right.

`getsizeof` measures an object's internal representation, and that representation changes between Python
versions. The comment froze the measurement taken the day the file was written; the line of code, on the
other hand, takes it again every time it runs.

Out of that comes a rule that holds for the whole term: **a number written in a comment rots and a
measured number does not.** When the number matters, the line that produces it goes in the program.

Look at the last comparison too. What the file was teaching, that a generator takes a tiny fraction of
what the list takes, holds up without depending on the two exact values. That is how you write a claim
that lasts.

## Grouping with an accumulating dictionary
"""),

code("""
ENTRIES = [
    {"student": "Ana", "subject": "COM102", "mark": 9.1},
    {"student": "Luis", "subject": "COM102", "mark": 6.4},
    {"student": "Sofia", "subject": "COM101", "mark": 8.0},
    {"student": "Marco", "subject": "COM101", "mark": 5.5},
    {"student": "Paula", "subject": "COM102", "mark": 7.2},
]

counts = {}
for e in ENTRIES:
    key = "pass" if e["mark"] >= 7 else "fail"
    counts[key] = counts.get(key, 0) + 1

print("Counts:", counts)

by_subject = {}
for e in ENTRIES:
    by_subject.setdefault(e["subject"], []).append(e["mark"])

print("Grouped:", by_subject)
print()
for subject, marks in by_subject.items():
    print(f"  {subject}  n={len(marks)}  average={sum(marks) / len(marks):.2f}")

print()
print("The five entries are all still counted:",
      sum(len(v) for v in by_subject.values()) == len(ENTRIES))
"""),

md("""
Two patterns you will be writing for the rest of the term.

`counts.get(key, 0) + 1` solves the first-time problem: the key does not exist yet and `get` returns the
default instead of raising `KeyError`.

`setdefault(key, []).append(...)` does the same job for grouping: if the key is missing it creates it
with an empty list, and either way it hands back the list to append to.

Look at the last line. **After grouping, the sizes of the groups have to add up to the total that went
in.** It is the cheapest check there is and it catches half of all grouping mistakes.

## The unpacking that stops the file
"""),

code("""
# FAILS ON PURPOSE. Code017.py, line 292. The file stops here.
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]

numbers.append(new_numbers)
print("Without unpacking:", numbers, "<- line 285, which does run")

numbers = [1, 2, 3]
new_numbers = [4, 5, 6]

try:
    numbers.append(*new_numbers)          # line 292
except TypeError as e:
    print()
    print("TypeError:", e)

print()
print("The list is as it was:", numbers)
print("The comment on line 293 announces:  [1, 2, 3, 4, 5, 6]")
"""),

md("""
`list.append() takes exactly one argument (3 given)`.

The asterisk **unpacks**: it turns `[4, 5, 6]` into three separate arguments. `print(*numbers)` on line
276 works because `print` takes as many as arrive. `append` takes exactly one, so receiving three is a
signature error, not a type error.

The method that does join two lists is `extend`, or the usual `+`, or the unpacking inside a literal,
which is what the file itself writes three lines further down.

The line is not what matters. What matters is what the line takes down with it.
"""),

code("""
FILE_LINES = 390
STOPS_AT = 292
dead = FILE_LINES - STOPS_AT

print("Code017.py has", FILE_LINES, "lines.")
print("It stops at line", STOPS_AT)
print("Never executed:", dead, "lines, which is",
      f"{dead / FILE_LINES:.0%}", "of the file.")
print()
print("What is left on the other side of the error:")
for topic, line in [("unpacking inside a literal", 301),
                    ("dictionary unpacking", 317),
                    ("zip over two lists", 336),
                    ("zip with lists of different lengths", 346),
                    ("stack with append and pop", 357),
                    ("queue with deque and popleft", 380)]:
    print(f"  line {line:>4}  {topic}")
"""),

md("""
Ninety-eight lines that the file wrote, commented and never ran.

This is what makes an early error cost more than it looks: it does not break one line, it **cuts the
file in two**. Everything after it went untested, and the comments announcing its output are predictions
nobody ever checked.

The rest of this block brings that stretch back to life, cell by cell, and checks every prediction.

## The stretch that never ran, run
"""),

code("""
# Code017.py, lines 299 to 318, this time for real
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers = [*numbers, *new_numbers]
print(numbers)
print("Does it match its comment [1, 2, 3, 4, 5, 6]?", numbers == [1, 2, 3, 4, 5, 6])

print()
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers = [*numbers, "a", *new_numbers, *"hello"]
print(numbers)

print()
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
print("The x ended up at", combined["x"], "because the second dictionary covered the first.")
"""),

md("""
All three predictions were right. Nobody knew, because nobody got this far.

The third line deserves a second. `{**first, **second}` merges two dictionaries and, when both carry the
same key, **the last one wins**. That raises nothing and is almost never written down, so it is worth
knowing before you merge the default configuration with the user's and wonder where a value went.

## `zip` and the silent truncation
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. zip stops with the shortest list.
names = ["Ana", "Luis", "Sofia", "Marco", "Paula"]
marks = [9.1, 6.4, 8.0]

pairs = list(zip(names, marks))

print("Names:", len(names))
print("Marks:", len(marks))
print("Pairs:", len(pairs), "<- lost", len(names) - len(pairs))
print()
for name, mark in pairs:
    print(f"  {name:<8}{mark}")
print()
print("Marco and Paula vanished from the report without a single warning.")
print()
try:
    list(zip(names, marks, strict=True))
except ValueError as e:
    print("With strict=True:", e)
"""),

md("""
Five students go in, three come out, and the report looks complete.

`zip` stops with the shortest one. That is the documented behaviour and it is useful when you genuinely
want to walk in parallel as far as the data reaches, but when the two lists *should* be the same length,
that truncation is silent data loss.

`strict=True` turns the silence into a `ValueError`. It has been there since Python 3.10 and it is the
kind of flag worth setting whenever the lengths have to match.

It is the same problem as week 2's parallel lists, now with the tool that is supposed to solve it.

## The stack, the queue, and a check written backwards
"""),

code("""
from collections import deque

# Stack: the last thing in is the first thing out
browsing_session = []
browsing_session.append("home")
browsing_session.append("courses")
browsing_session.append("com102")
print("Stack:", browsing_session)
print("Back:", browsing_session.pop())
print("Stack:", browsing_session)

print()
# Queue: the first thing in is the first thing out
queue = deque([])
queue.append("doc1")
queue.append("doc2")
queue.append("doc3")
print("Queue:", queue)
print("Printing:", queue.popleft())
print("Queue:", queue)
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code017.py, lines 366 to 369.
browsing_session = ["home", "courses"]

# The file's comment says: "To avoid getting an error when popping an
# empty stack, you can check if the stack is empty before popping"
if not browsing_session:
    browsing_session.pop()

print("With a full stack nothing happens:", browsing_session)
print("And that is why the file never found out.")
print()

browsing_session = []
try:
    if not browsing_session:
        browsing_session.pop()
except IndexError as e:
    print("With an empty stack:", type(e).__name__ + ":", e)

print()
browsing_session = []
if browsing_session:                      # without the not
    print("popping:", browsing_session.pop())
else:
    print("With the condition the right way round: the stack is empty, nothing to pop.")
"""),

md("""
The condition is inverted and does exactly the opposite of what its comment promises.

`if not browsing_session` is true **when the stack is empty**, and inside it calls `pop`. That is the one
situation where `pop` raises, and it is precisely the one the comment says it wants to avoid.

With a full stack the condition is false, the `pop` never runs, and everything looks fine. That is how
the file lives alongside the error: it never reaches it. It is the same lesson as the deleting `for`
cell: **an error that does not fire is still an error, and what decides whether it fires is that day's
data.**

In `Code017.py` this block sits after line 292, so it never even got as far as not firing.

## A function that covered one of Python's
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code017.py, line 12.
def sum(*numbers: tuple) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


print("With the file's one:", sum(1, 2, 3, 4, 5))

try:
    print(sum([1, 2, 3, 4, 5]))
except TypeError as e:
    print("And with a list:", e)

print()
del sum
print("With Python's one:  ", sum([1, 2, 3, 4, 5]))
print("And with separate arguments:")
try:
    sum(1, 2, 3, 4, 5)
except TypeError as e:
    print("  ", e)
"""),

md("""
Two functions with the same name and incompatible signatures.

`Code017.py` defines `sum` on its line 12 and with that it covers Python's for everything that comes
after in that file. The file's one takes separate numbers; Python's takes an iterable. Swapping one for
the other breaks every call.

The file gets away with it because it never uses `sum` again anywhere. A longer program does not get
away with it: it comes out when somebody writes `sum(marks)` two hundred lines later and gets a
`TypeError` that makes no sense at all with the documentation open.

**Rule:** before naming a function, type the name into a cell. If Python answers with something, the
name is taken.
"""),

md("""
---
## Four errors from this session

**Deleting from a list while walking it.** The `for`'s index moves on even though the list shrinks, so
the loop skips items. Fixed by building a new list.

**Copying with the equals sign.** `copy = items` leaves two names on the same object. `is` and `id()`
prove it in two lines.

**Using a list to search.** `x in list` walks all of it. A set answers immediately and the line that
asks is written exactly the same.

**Tuples for data that changes.** Correcting one value forces you to build the whole tuple again.
Immutability is chosen when it buys you something, not out of habit.
"""),

md("""
---
# Exercises

This week's lab is picking the right container for five queries about a student roll. The exercises
build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The three questions

Write the same six values as a list, a tuple, a set and a dictionary. For each one print how many
elements were left and explain in a comment what was lost.

### Exercise 2 · Searching in the container that fits

Build a list of fifty thousand student ids and a set with the same ones. Measure with
`time.perf_counter` how long each one takes to answer `in` for an id that is not there.

Explain in a comment why the missing id is the list's worst case.

### Exercise 3 · Copying against sharing

Write a function that takes a list and appends an element to it. Call it and show that the list outside
changed. Then write the version that leaves the original alone.

Check both with `is`.

### Exercise 4 · The loop that skips

Take a list of eight names and delete the ones starting with a vowel inside the `for`. Print how many
the loop visited and how many were left.

Rewrite it with a comprehension and check that this time they all went.

### Exercise 5 · How it grows

Append a thousand elements to a list and print `getsizeof` every time the number changes. Count how many
moves there were.

Explain in a comment why there are so few.

### Exercise 6 · The single-pass generator

Create a generator with a condition, walk it twice and show that the second pass comes back empty. Fix
it with a comprehension and explain in a comment when each one is the right choice.

### Exercise 7 · Group and check

Take a list of twenty entries with a subject and a mark. Group them by subject in a dictionary and print
the average of each group.

Finish by checking that the sizes of the groups add up to twenty.

### Exercise 8 · The unpacking

Join two lists four ways: with `extend`, with `+`, with `[*a, *b]` and with `append` unpacking. Catch
the `TypeError` from the last one and explain in a comment how it differs from `print(*a)`.

### Exercise 9 · The lab

You are handed a student roll with an id, a name, a course and an average. Answer these five queries,
picking a container for each one and justifying the choice in a line:

1. List the students in the order they enrolled.
2. Say whether an id is registered.
3. Get the name from the id.
4. List the distinct courses that appear.
5. Store the five highest averages, which never change again.

Use at least three of the four containers. The criterion is that no query walks the whole collection if
another container would avoid it.
"""),

md("""
---
## Three things to take away

**Three questions pick the container.** Whether the order matters, whether it will change, whether you
search by key. In that order, and that is that.

**A list is a dynamic array.** It over-allocates and copies when it fills up, which is why appending at
the end nearly never costs anything while inserting at the front always does.

**Equals does not copy, it shares.** Two names on one list look identical right up until one of the two
writes to it, and by then it is too late.

Week 11 goes on with exception handling. Six cells in this notebook caught an error with `try` and
`except` without explaining the syntax; next week starts exactly there, with what gets raised, where it
travels and who decides to deal with it.
"""),

md("""
---
# Solutions

### Exercise 1

```python
DATA = ["A001", "A004", "A002", "A001", "A003", "A002"]

as_a_list = list(DATA)
as_a_tuple = tuple(DATA)
as_a_set = set(DATA)
as_a_dict = {sid: i for i, sid in enumerate(DATA)}

for name, c in [("list", as_a_list), ("tuple", as_a_tuple),
                ("set", as_a_set), ("dictionary", as_a_dict)]:
    print(f"{name:<12}{len(c)}  {c}")

# The list and the tuple keep all six, repeats included and in order.
# The set kept four: it lost the repeats and it lost the order.
# The dictionary also kept four, because the repeated key is overwritten, but it
# keeps insertion order and stores the last position.
```

### Exercise 2

```python
import time

STUDENT_IDS = [f"A{n:06d}" for n in range(50_000)]
AS_A_SET = set(STUDENT_IDS)
MISSING = "Z999999"

for name, collection in [("list", STUDENT_IDS), ("set", AS_A_SET)]:
    start = time.perf_counter()
    for _ in range(50):
        MISSING in collection
    print(f"{name:<12}{time.perf_counter() - start:.5f} s")

# The missing id is the list's worst case because answering "not there" means
# comparing against all fifty thousand. An id that is present can turn up early
# and cut the walk short; a missing one never does.
```

### Exercise 3

```python
def append_badly(items, value):
    items.append(value)
    return items


def append_well(items, value):
    return items + [value]


original = [1, 2, 3]
returned = append_badly(original, 4)
print(original, returned, original is returned)

original = [1, 2, 3]
returned = append_well(original, 4)
print(original, returned, original is returned)
```

### Exercise 4

```python
names = ["Ana", "Elena", "Ivan", "Luis", "Oscar", "Ubaldo", "Sofia", "Marco"]

visited = []
copy = list(names)
for n in copy:
    visited.append(n)
    if n[0] in "AEIOU":
        copy.remove(n)

print("Visited:", len(visited), "of", len(names))
print("Left:", copy)

clean = [n for n in names if n[0] not in "AEIOU"]
print("With a comprehension:", clean)
print("Did they all go?", all(n[0] not in "AEIOU" for n in clean))
```

### Exercise 5

```python
from sys import getsizeof

items = []
before = getsizeof(items)
moves = 0
for n in range(1000):
    items.append(n)
    now = getsizeof(items)
    if now != before:
        moves += 1
        before = now

print("Moves to reach 1000:", moves)

# There are few of them because every new block is proportionally bigger than
# the last, not one slot longer. A thousand elements take around twenty moves,
# and a million do not reach fifty.
```

### Exercise 6

```python
MARKS = [9.1, 6.4, 8.0, 7.5, 5.9]

gen = (n for n in MARKS if n >= 7)
print("First: ", list(gen))
print("Second:", list(gen))

items = [n for n in MARKS if n >= 7]
print("First: ", items)
print("Second:", items)

# The generator is the right choice when the data does not fit in memory or when
# it will only be walked once. The comprehension wins as soon as you have to walk
# it twice, measure its length or index into it.
```

### Exercise 7

```python
import random

rng = random.Random(2026)
SUBJECTS = ["COM101", "COM102", "COM103"]
ENTRIES = [{"subject": rng.choice(SUBJECTS), "mark": round(rng.uniform(5, 10), 1)}
           for _ in range(20)]

by_subject = {}
for e in ENTRIES:
    by_subject.setdefault(e["subject"], []).append(e["mark"])

for subject, marks in sorted(by_subject.items()):
    print(f"{subject}  n={len(marks):<4}average={sum(marks) / len(marks):.2f}")

print("Were they all counted?",
      sum(len(v) for v in by_subject.values()) == len(ENTRIES))
```

### Exercise 8

```python
a = [1, 2, 3]
b = [4, 5, 6]

with_extend = list(a)
with_extend.extend(b)
print(with_extend)

print(a + b)
print([*a, *b])

try:
    items = list(a)
    items.append(*b)
except TypeError as e:
    print("TypeError:", e)

# print(*a) works because print takes as many arguments as arrive. append takes
# exactly one, so unpacking three is a signature error. The asterisk does not
# join lists: it spreads one list into separate arguments.
```

### Exercise 9

```python
ROLL = [
    {"student_id": "A001", "name": "Ana Robles", "course": "Mechatronics", "average": 9.2},
    {"student_id": "A002", "name": "Luis Ferrer", "course": "Industrial", "average": 7.8},
    {"student_id": "A003", "name": "Sofia Ines", "course": "Mechatronics", "average": 9.5},
    {"student_id": "A004", "name": "Marco Duarte", "course": "Civil", "average": 6.4},
    {"student_id": "A005", "name": "Paula Lara", "course": "Industrial", "average": 8.7},
]

# 1. In enrolment order -> list. It is the only container that keeps the order
#    and takes being walked whole, which is exactly what the query asks for.
enrolled = [s["name"] for s in ROLL]
print(enrolled)

# 2. Is it registered? -> set. Only membership is asked, and it answers without
#    walking.
REGISTERED = {s["student_id"] for s in ROLL}
print("A003" in REGISTERED, "Z999" in REGISTERED)

# 3. Name from the id -> dictionary. It is a lookup by key.
BY_ID = {s["student_id"]: s["name"] for s in ROLL}
print(BY_ID["A003"])

# 4. Distinct courses -> set. The requirement is "distinct", which is its
#    definition.
print(sorted({s["course"] for s in ROLL}))

# 5. The five highest, which no longer change -> tuple. It is worked out once and
#    the immutability documents that the cut is closed.
TOP = tuple(sorted(ROLL, key=lambda s: s["average"], reverse=True)[:5])
print([s["name"] for s in TOP])
```

Three decisions worth defending when you hand this in.

**No query walks the whole roll except the first**, which has to by definition. The other four lean on a
container built once.

**The helper containers are built once and reused.** If `REGISTERED` were built inside the query, the
query would walk the roll again and the set would have bought nothing.

**The tuple in point 5 is not decoration.** It says, in the type, that the cut no longer takes
corrections. It is the only one of the five where immutability adds anything.
"""),

]

write(OUT / "en" / "w10.ipynb", en)
print("wrote", OUT / "en" / "w10.ipynb")
