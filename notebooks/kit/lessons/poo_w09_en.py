"""notebooks/programacion-orientada-a-objetos/en/w09.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w09.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/3rd Module/  (functions)
              docs/en/courses/python-course/07 - Activities/Projects/02 - Hanoi Tower/
                  hanoi_tower.py

hanoi_tower.py cannot be run as it stands inside a notebook: it asks for the
number of disks with input(), calls os.system("cls") twice and ends with another
input(). The algorithm, which is its two middle functions, is quoted whole and
untouched; the console plumbing is left out and the notebook says so.

Review 3 (w01.3) already covered the basics of functions, including the default
list. It is not repeated here: it is picked up with __defaults__ in front of you
and then carried further.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 09
## Topic 4 · Advanced functions and structures

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

The application unit starts here. Functions that test themselves, code split into pieces, and functions
that call themselves.

None of this is new syntax. What makes a function advanced is three decisions: what it takes, what it
returns, and what it leaves changed outside itself. The third is the one hardly anyone looks at and the
one that decides whether the code can be tested.

By the end you will be able to:

1. Design a function's signature, deciding what goes positional, what carries a default and what is
   worth demanding by name.
2. Pass a function as an argument and write a sort criterion with `lambda`.
3. Split a script into functions that each do one thing.
4. Write a recursive function with a base case that stops and a call that moves towards it.
5. Say what a recursion costs before running it.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Ten fail on purpose and carry a comment saying so.

Eight of the ten **raise no exception at all**. Two of those eight are the ones that cost most outside
class: the default value that gets evaluated once, and the `lambda` inside a loop that takes the
variable rather than its value.
"""),

md("""
---
# Block 1 · Advanced functions

## Three ways of calling the same function
"""),

code("""
def register(name: str, course: str = "Undeclared", active: bool = True) -> None:
    print(f"  {name:<8}{course:<16}active={active}")


register("Ana")
register("Luis", "Mechatronics")
register("Sofia", active=False)
register(course="Industrial", name="Marco")

print()
print("Default values:", register.__defaults__)
print("Parameters:", register.__code__.co_varnames[:register.__code__.co_argcount])
"""),

md("""
Four calls, one signature.

Passing `active` by name lets `course` keep its default, and that is the whole point of keyword
arguments: **skipping the ones in the middle without repeating them**.

The last call reverses the order and works just the same, because with names the position stops
mattering.
"""),

code("""
# FAILS ON PURPOSE. Parameters with defaults go last, no exceptions.
SOURCE = "def f(a=1, b):\\n    return a + b"

try:
    compile(SOURCE, "<example>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e.msg)
    print("On the line:", e.text.strip())

print()
print("And the other way round it compiles:",
      bool(compile("def f(b, a=1):\\n    return a + b", "<example>", "exec")))
"""),

md("""
`parameter without a default follows parameter with a default`.

The reason is about reading, not about whim: if `a` had a default and `b` did not, `f(5)` would be
ambiguous. Is the five `a` or `b`? With the defaulted ones last, positionals always fill left to right
and there is nothing to guess.

This is one of the few errors in the notebook you see while typing. The ones that follow are not.

## A default value is evaluated once
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The default list, with the proof in front of you.
def add_task(task, items=[]):
    items.append(task)
    return items


print(add_task("buy coffee"))
print(add_task("send email"))
print(add_task("review tasks"))

print()
print("What the function holds:", add_task.__defaults__)
print("Is it the same list across all three calls?",
      add_task.__defaults__[0] is add_task("fourth"))
"""),

md("""
Three independent calls and one list that keeps growing.

You saw it in review 3 and in week 5. What this cell adds is the proof: `__defaults__` is a tuple that
lives **on the function**, filled once when Python read the `def`, and it contains that list. There are
not three lists, there is one.

The rule, now with the reason: **a default value is evaluated when the function is defined, not when it
is called.**

That holds for any expression, not just for lists.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A default computed once and frozen.
import itertools

next_number = itertools.count(1000).__next__


def issue(item, number=next_number()):
    return f"invoice {number}: {item}"


print(issue("consulting"))
print(issue("training"))
print(issue("maintenance"))

print()
print("The frozen number:", issue.__defaults__)
print("Are all three numbers the same?",
      len({issue(c).split(":")[0] for c in ["a", "b", "c"]}) == 1)
print()


def issue_well(item, number=None):
    if number is None:
        number = next_number()
    return f"invoice {number}: {item}"


for item in ["consulting", "training", "maintenance"]:
    print(issue_well(item))
"""),

md("""
Three invoices with the same number, and no warning.

`next_number()` ran once, while Python was reading the `def`, and that number was stored in
`__defaults__` for good. With the list the symptom was that it grew; here the symptom is that it never
changes, and both come out of the same mechanism.

The fix is the usual one: **`None` as the default, and the real value computed inside**.

This error is trickier than the list one because it usually shows up with dates.
`def log(event, when=datetime.now())` stamps every event with the time the module was imported.

## Five ways of taking a value

| Form | How it looks | What it takes |
|---|---|---|
| Positional | `def f(a, b)` | In the order they are passed |
| With a default | `def f(a, b=0)` | The given value, or the default |
| By name | `f(b=3)` | Regardless of position |
| Variable | `def f(*args)` | A tuple with whatever arrives |
| Named variable | `def f(**kw)` | A dictionary with the named ones |

The last two turned up in week 5 with the shopping cart. One more is missing, and it tidies a long
signature considerably.
"""),

code("""
def transfer(amount, *, source, target, notify=False):
    \"\"\"A lone asterisk only forces everything after it to go by name.\"\"\"
    notice = " (with notice)" if notify else ""
    return f"${amount:,.2f} from {source} to {target}{notice}"


print(transfer(1500, source="savings", target="current"))
print(transfer(2000, source="current", target="savings", notify=True))

try:
    transfer(1500, "savings", "current")
except TypeError as e:
    print()
    print("TypeError:", e)
"""),

md("""
The lone asterisk in the signature collects nothing: **it marks where the positionals end**.

That matters here because `source` and `target` are two strings of the same type, and swapping them sends
the money the wrong way with no error at all. Forcing the names turns a reversed transfer into a
`TypeError`.

The same problem, without the asterisk, looks like this.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Positional booleans at the call site.
def send_report(recipient, include_detail, send_copy, compress):
    parts = []
    if include_detail:
        parts.append("with detail")
    if send_copy:
        parts.append("with a copy")
    if compress:
        parts.append("compressed")
    return f"{recipient}: " + (", ".join(parts) if parts else "basic")


print(send_report("ana@up.edu.mx", True, False, True))
print(send_report("ana@up.edu.mx", True, True, False))     # which is which?
print()
print("Both calls are legal and do different things.")
print("Reading only the call, there is no way to tell which is which.")
print()
print("With names:")
print(send_report("ana@up.edu.mx", include_detail=True,
                  send_copy=True, compress=False))
"""),

md("""
`f(True, False, True)` says absolutely nothing when you read it, and the first two calls in the cell
could be swapped without anyone noticing in a code review.

It is error 04 on the slide. The fix has two levels: write the names at the call site, or better, put a
`*` in the signature so the language demands them.

## A function passed to another function
"""),

code("""
products = [("Keyboard", 890), ("Monitor", 4200), ("Mouse", 350), ("Webcam", 890)]

by_default = sorted(products)
by_price = sorted(products, key=lambda p: p[1])
by_price_desc = sorted(products, key=lambda p: p[1], reverse=True)
by_name_length = sorted(products, key=lambda p: len(p[0]))

print("No key:        ", [p[0] for p in by_default])
print("By price:      ", [p[0] for p in by_price])
print("By price desc: ", [p[0] for p in by_price_desc])
print("By name length:", [p[0] for p in by_name_length])
print()
print("The cheapest:", by_price[0])
print("Did the two at 890 keep their original order?",
      [p[0] for p in by_price if p[1] == 890] == ["Keyboard", "Webcam"])
"""),

md("""
`key` takes **a function**, not a value. `sorted` calls it once per element and orders by whatever it
returns.

Without `key`, `sorted` compares the whole tuples left to right, so it orders by name. With
`key=lambda p: p[1]` it compares only the price.

The last line checks something that gets used more than it gets named: Python's sort is **stable**. Two
elements with the same key keep the order they came in, which is why you can sort by one criterion and
then another to get tie-breaks.

`lambda` is an anonymous function of a single expression. It brings nothing `def` does not have, and when
the calculation does not fit comfortably on one line, `def` with a proper name reads better.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Sorting without saying by which field.
students = [("Robles", 9.2), ("Ferrer", 7.8), ("Ines", 9.5), ("Duarte", 6.4)]

bad_ranking = sorted(students, reverse=True)
good_ranking = sorted(students, key=lambda s: s[1], reverse=True)

print("Ranking without key:", [s[0] for s in bad_ranking])
print("Ranking with key:   ", [s[0] for s in good_ranking])
print()
print("Top of the first:", bad_ranking[0])
print("Top of the second:", good_ranking[0])
print("Do the two rankings agree?", bad_ranking == good_ranking)
"""),

md("""
The top of the ranking without `key` is Robles, on 9.2, and the real one is Ines on 9.5.

`sorted` ordered by surname descending and the result looks like a perfectly respectable ranking: four
students, in order, no errors. It is just wrong.

It is the same error as the parallel lists in week 2: **sorted output is not correct output**.

## The `lambda` that takes the variable rather than its value
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Three functions that turned out to be one.
multipliers = []
for factor in [2, 3, 10]:
    multipliers.append(lambda x: x * factor)

print("We expected 5*2, 5*3 and 5*10:")
print(" ", [f(5) for f in multipliers])
print()
print("Final value of factor:", factor)
print()

good = []
for factor in [2, 3, 10]:
    good.append(lambda x, f=factor: x * f)      # the value is captured at definition

print("Capturing the value:")
print(" ", [f(5) for f in good])
"""),

md("""
Three functions that should multiply by 2, by 3 and by 10, and all three multiply by 10.

A `lambda` defined inside a loop **does not keep the variable's value, it keeps the variable**. By the
time anyone calls them, the loop has finished and `factor` holds whatever it held last.

It is review 3's scope rule seen from the other side: there the problem was that assigning inside a
function created a local; here the problem is that there is **no** local and the lambda reaches the outer
one.

The fix in the second half uses the mechanism from three cells ago, this time in your favour: a parameter
with a default is evaluated at definition, so `f=factor` captures the value at that moment.

The same error turns up with `key`, with week 14's event handlers, and with any function stored to be
called later.
"""),

md("""
---
# Block 2 · Modularity

A function does one thing and its name describes the whole of it.

**The name test.** If you cannot name it without saying "and", it is still doing too much.

**The size test.** If it does not fit on a screen without scrolling, something inside wants out.

**The return test.** A function that returns a value and also prints is doing two jobs.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The function that computes and prints.
def process(students):
    total = 0
    for s in students:
        total += s["mark"]
    print(f"Average: {total / len(students):.2f}")


GROUP = [{"name": "Ana", "mark": 9.2}, {"name": "Luis", "mark": 7.8},
         {"name": "Sofia", "mark": 9.5}]

result = process(GROUP)

print()
print("What it returned:", result)
print("Type:", type(result).__name__)
print()
print("Can it be compared against the expected average?")
try:
    print("  ", round(result, 2) == 8.83)
except TypeError as e:
    print("   TypeError:", e)
"""),

md("""
The average came out fine on the screen and the function returned `None`.

That is the whole difference between computing and printing. A number that only exists in the console
cannot be compared, cannot be added, cannot be written to a file and cannot be tested. It is the sentence
that has been turning up since review 3, and here it reaches its final form: **a function that prints is
useful once; one that returns is useful anywhere.**
"""),

code("""
def average(marks):
    return sum(marks) / len(marks)


def marks_of(students):
    return [s["mark"] for s in students]


def passing(students, minimum=8.0):
    return [s for s in students if s["mark"] >= minimum]


def report_line(students):
    return (f"{len(students)} students · average {average(marks_of(students)):.2f} · "
            f"{len(passing(students))} passing")


print(report_line(GROUP))
print()
print("And now it can be checked without looking at the screen:")
print("  average correct:", abs(average(marks_of(GROUP)) - 8.833333) < 0.001)
print("  passing correct:", [s["name"] for s in passing(GROUP)])
print("  with another minimum:", [s["name"] for s in passing(GROUP, 7.0)])
print()
CHECKS = [(average, [1, 2, 3]), (marks_of, GROUP), (passing, GROUP),
          (report_line, GROUP)]
for f, argument in CHECKS:
    returns_something = f(argument) is not None
    has_and = "_and_" in f.__name__
    print(f"  {f.__name__:<14}returns a value: {returns_something}   "
          f"name has 'and': {has_and}")
"""),

md("""
Four functions, none with "and" in its name, and the first three return without printing.

`report_line` does build text, and it still returns rather than prints. That decision is what lets the
report be written to a file tomorrow without touching anything.

Look at `passing(students, minimum=8.0)`. The minimum moved into the signature with a default, so the
function serves today's rule and whatever the department sets next term.

## The global variable that connects functions
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Two functions talking through a global.
running_total = 0


def add_sales(amounts):
    global running_total
    for a in amounts:
        running_total += a


def apply_discount(percent):
    global running_total
    running_total *= (1 - percent / 100)


add_sales([100, 200, 300])
apply_discount(10)
add_sales([400])

print("Total:", round(running_total, 2))

running_total = 0
add_sales([100, 200, 300])
add_sales([400])
apply_discount(10)

print("The same data, another order:", round(running_total, 2))
print()
print("Same result?", round(940.0, 2) == round(900.0, 2))
"""),

md("""
The same data, the same operations, two results.

When two functions talk through a global, the result depends on the order somebody called them in, and
that order appears in no signature. To know what `apply_discount` does you have to know who touched
`running_total` first, and that is spread across the whole file.

It is error 02 on the slide, and it is week 6's shared-state problem without even the benefit of a class
holding it together.

The fix: **data comes in through parameters and leaves through the `return`**.
"""),

code("""
def total_of(amounts):
    return sum(amounts)


def with_discount(total, percent):
    return total * (1 - percent / 100)


print("Discount at the end:", round(with_discount(total_of([100, 200, 300, 400]), 10), 2))
print("Discount halfway:",
      round(total_of([400]) + with_discount(total_of([100, 200, 300]), 10), 2))
print()
print("The two results are still different, and now the line says why.")
"""),

md("""
The two sums still differ, because they genuinely are different sums. The difference is that now you can
see it on the line that writes them, without hunting through the file for who touched what.

**A function that depends only on its parameters can be read without reading anything else.** That is the
whole criterion of this block.
"""),

md("""
---
# Block 3 · Recursion

A function that calls itself with a smaller problem, until the problem is so small there is nothing left
to do.

Every recursion needs two pieces: **the base case** that stops it, and **the call that moves towards it**.
"""),

code("""
import sys


def factorial(n: int) -> int:
    if n <= 1:                   # base case
        return 1
    return n * factorial(n - 1)  # moves towards the base case


for n in [0, 1, 4, 10]:
    print(f"  factorial({n:>2}) = {factorial(n)}")

print()
print("Call limit for this session:", sys.getrecursionlimit())
"""),

code("""
# FAILS ON PURPOSE. With no base case, the stack runs out.
def no_brakes(n):
    return n + no_brakes(n - 1)      # never stops calling itself


try:
    no_brakes(10)
except RecursionError as e:
    print("RecursionError:", str(e)[:60])

print()


def bad_brakes(n):
    if n == 0:
        return 0
    return n + bad_brakes(n - 2)     # two at a time, starting from an odd number


print("With an even n:", bad_brakes(10))
try:
    bad_brakes(9)
except RecursionError as e:
    print("With an odd n:", type(e).__name__)
"""),

md("""
Both cases are the same error wearing different clothes.

The first has no base case. The second has one and **never reaches it** when it starts on an odd number,
because it steps down by two and walks straight past zero.

Writing `if n <= 0` instead of `if n == 0` would have closed that hole. **The base case has to catch
everything below it, not one exact value.**

## Predict before you run

```python
def count(n):
    if n == 0:
        return 0
    return n + count(n - 1)


print(count(3))
```

- **A.** 6, because it adds 3 plus 2 plus 1 plus 0.
- **B.** 3, because only the first call counts.
- **C.** 0, because the base case returns zero.
- **D.** `RecursionError`, the function has no base case.
"""),

code("""
DEPTH = []


def count(n, level=0):
    DEPTH.append(level)
    print(f"{'  ' * level}count({n}) called, frames open: {level + 1}")
    if n == 0:
        print(f"{'  ' * level}count(0) returns 0")
        return 0
    result = n + count(n - 1, level + 1)
    print(f"{'  ' * level}count({n}) returns {result}")
    return result


print("Result:", count(3))
print()
print("Frames open at the same time, at most:", max(DEPTH) + 1)
print("Calls in total:", len(DEPTH))
"""),

md("""
The answer is **A**.

The indentation in the output is the stack. It goes down to the base case opening one frame per call, and
there it turns around: zero comes back first, then one, then three, and finally six.

No call in the middle knows the final result. Each one knows how to do one thing: add `n` to whatever the
next one hands back.

## What a badly built recursion costs
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The recursion that recomputes what it already knew.
CALLS = {"naive": 0, "memoised": 0}


def fib(n):
    CALLS["naive"] += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo={}):
    CALLS["memoised"] += 1
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


for n in [10, 20, 25]:
    CALLS["naive"] = CALLS["memoised"] = 0
    a, b = fib(n), fib_memo(n, {})
    print(f"  fib({n}) = {a:<7} naive: {CALLS['naive']:>7} calls   "
          f"memoised: {CALLS['memoised']:>3}")

print()
print("Both versions give the same number. What changes is how often they compute it.")
"""),

md("""
For `fib(25)` the naive version makes over two hundred thousand calls and the one that remembers makes
fewer than fifty.

Both are correct. Neither raises. The difference is that the first recomputes `fib(20)` thousands of
times, because every branch of the call tree ignores what the others found out.

Look at `fib_memo`'s signature: it uses a dictionary as a default value, which is exactly block 1's error.
It is deliberate here, and that is why the calls above hand it a fresh dictionary each time; if they did
not, the memory would be shared between calls and the counts would come out wrong. A mutable default used
as a cache is one of the very few cases where somebody does it knowingly, and even then it reads better
written with `None` and one extra line.

## The Towers of Hanoi

The project `07 - Activities/Projects/02 - Hanoi Tower/hanoi_tower.py` solves the puzzle with six lines of
recursion. The whole file does not run in a notebook because it asks for the number of disks with
`input()` and clears the console with `os.system("cls")`; the algorithm, which is its two middle
functions, goes here as it stands.
"""),

code("""
MOVES = []


def move_disk(n, from_rod, to_rod):
    disk = "*" * n
    MOVES.append((n, from_rod, to_rod))
    print(f"  Move disk {disk:<4} from rod {from_rod} to rod {to_rod}")


def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:                                   # base case: nothing to move
        return
    hanoi(n - 1, from_rod, aux_rod, to_rod)
    move_disk(n, from_rod, to_rod)
    hanoi(n - 1, aux_rod, to_rod, from_rod)


hanoi(3, "A", "C", "B")

print()
print("Moves with 3 disks:", len(MOVES))
print("2**3 - 1 =", 2 ** 3 - 1)
"""),

code("""
def move_disk(n, from_rod, to_rod):               # now it only counts, no printing
    MOVES.append((n, from_rod, to_rod))


print(f"{'disks':>7}{'moves':>10}{'2^n - 1':>10}{'equal':>8}")
for n in range(1, 11):
    MOVES.clear()
    hanoi(n, "A", "C", "B")
    print(f"{n:>7}{len(MOVES):>10}{2 ** n - 1:>10}"
          f"{str(len(MOVES) == 2 ** n - 1):>8}")

print()
print("With 20 disks that would be", f"{2 ** 20 - 1:,}", "moves.")
print("With 64, the number in the legend:", f"{2 ** 64 - 1:,}")
"""),

md("""
Three disks are seven moves, ten disks are one thousand and twenty-three, and the formula is exactly
`2**n - 1`.

That is not a coincidence of the code, it comes out of the recursion's shape: solving `n` disks costs
twice solving `n - 1` plus one move. `T(n) = 2·T(n-1) + 1`, and that relation gives `2**n - 1`.

The legend says monks are moving sixty-four disks at one per second. With the number above, that is more
than five hundred billion years.

**What to take from this: a recursion with two calls per level doubles the work at every level.** Being
able to count that before running the program is half of what this week teaches.
"""),

md("""
---
## Four errors from this session

**The mutable default value.** It is created once, when the `def` is read, and every call writes into it.
That holds for lists, dictionaries, dates and any function call you put there.

**The `lambda` inside a loop.** It takes the variable, not its value, and they all end up seeing the last
one. Fixed with a parameter carrying a default.

**`global` to connect functions.** The result depends on the order of the calls, and that order appears in
no signature.

**Sorting without saying by which field.** `sorted` over tuples orders by the first element, and the
result looks like a correct ranking.
"""),

md("""
---
# Exercises

This week's lab is splitting a fifty-line script into functions. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The signature

Write a function with one positional parameter, one with a default and one demanded by name with `*`.
Call it four different ways and catch the `TypeError` from a fifth.

Print `__defaults__` and explain in a comment what it holds.

### Exercise 2 · The list that grows

Write a function with a list as its default and call it three times. Show with `is` that all three calls
share the list in `__defaults__`.

Fix it with `None` and repeat the three calls.

### Exercise 3 · The frozen default

Write a function whose default value is the result of another function, for instance a counter or the
time. Call it three times and show the value never changes.

Explain in a comment when it was computed.

### Exercise 4 · Sorting by the right thing

Take a list of tuples with a name and a mark. Sort it without `key` and with `key`, and print the top two
of each version.

Then sort it by two criteria, first by mark and then by name for ties.

### Exercise 5 · The lambda in the loop

Create three functions inside a loop with `lambda`, store them in a list and call them afterwards. Show
that all three do the same thing, then fix it.

### Exercise 6 · Computing against printing

Write a function that computes an average and prints the result, and store what it returns in a variable.
Show that it is `None`.

Split it in two and check the number with a comparison.

### Exercise 7 · No globals

Write two functions that talk through a global and show the result changes if you swap the order of the
calls. Rewrite them passing and returning the data.

### Exercise 8 · Recursion with a base case

Write a recursive function that adds up a number's digits. Try it with zero, with one digit and with six.

Then deliberately write a version whose base case is never reached and catch the `RecursionError`.

### Exercise 9 · The lab

You are handed a fifty-line script that reads marks, works out the average, counts passes and prints a
report, all in a row. Split it into functions that each do one thing.

No function goes over fifteen lines, and none computes and prints at the same time. Hand in a `.py` file
with the functions and a main block calling them in order.

The criterion is that every function's name can be said in full without using the word "and".
"""),

md("""
---
## Three things to take away

**A default value is evaluated when the function is defined.** Once, when Python reads the `def`. That is
why the list grows, the invoice number freezes and the date stays at start-up time.

**One function, one reason to change.** If the name needs a conjunction, there are two functions inside
waiting to be separated. And if it computes and prints, that is already two.

**Every recursion needs a base case and a call that moves towards it.** The base case catches everything
below it, not one exact value, and it is worth knowing what it will cost before you run it.

Week 10 goes on with collections: four ways of holding several things in one variable, how a list grows
inside, and what can be done without touching the disk.
"""),

md("""
---
# Solutions

### Exercise 1

```python
def enrol(student_id, group="01", *, active=True, scholarship=False):
    return f"{student_id} group {group} active={active} scholarship={scholarship}"


print(enrol("A001"))
print(enrol("A002", "02"))
print(enrol("A003", active=False))
print(enrol("A004", "03", scholarship=True))

try:
    enrol("A005", "04", False)
except TypeError as e:
    print("TypeError:", e)

print(enrol.__defaults__)
print(enrol.__kwdefaults__)

# __defaults__ only carries the positional parameters' defaults, here ("01",).
# The ones after the asterisk live separately, in __kwdefaults__.
```

### Exercise 2

```python
def sign_up(name, items=[]):
    items.append(name)
    return items


print(sign_up("Ana"))
print(sign_up("Luis"))
print(sign_up("Sofia"))
print("The list in the signature:", sign_up.__defaults__[0])
print("The same one?", sign_up.__defaults__[0] is sign_up("Marco"))


def sign_up_well(name, items=None):
    items = [] if items is None else list(items)
    items.append(name)
    return items


print(sign_up_well("Ana"))
print(sign_up_well("Luis"))
print(sign_up_well("Sofia"))
```

### Exercise 3

```python
COUNTER = [0]


def next_one():
    COUNTER[0] += 1
    return COUNTER[0]


def label(text, number=next_one()):
    return f"#{number} {text}"


print(label("one"))
print(label("two"))
print(label("three"))
print("Times next_one() ran:", COUNTER[0])

# It ran once, while Python was reading the def, before the first call. The
# counter stopped at 1 and all three labels share that number.
```

### Exercise 4

```python
students = [("Robles", 9.2), ("Ferrer", 7.8), ("Ines", 9.5), ("Duarte", 9.2)]

no_key = sorted(students, reverse=True)
with_key = sorted(students, key=lambda s: s[1], reverse=True)

print("No key:  ", no_key[:2])
print("With key:", with_key[:2])

two_criteria = sorted(students, key=lambda s: (-s[1], s[0]))
print("By mark, ties broken by name:", two_criteria)

# The minus in front of the mark sorts it high to low without reversing the name,
# which is the usual trick for mixing two directions in one key.
```

### Exercise 5

```python
functions = []
for tag in ["a", "b", "c"]:
    functions.append(lambda: tag)

print([f() for f in functions])

good = []
for tag in ["a", "b", "c"]:
    good.append(lambda t=tag: t)

print([f() for f in good])
```

### Exercise 6

```python
def report(marks):
    print(f"Average: {sum(marks) / len(marks):.2f}")


returned = report([9.2, 7.8, 9.5])
print("Returned:", returned)


def average(marks):
    return sum(marks) / len(marks)


value = average([9.2, 7.8, 9.5])
print(f"Average: {value:.2f}")
print("Is it the expected one?", abs(value - 8.8333) < 0.001)
```

### Exercise 7

```python
balance = 0


def deposit(amount):
    global balance
    balance += amount


def charge_fee(pounds):
    global balance
    balance -= pounds


deposit(1000)
charge_fee(50)
deposit(500)
print("Order A:", balance)

balance = 0
deposit(1000)
deposit(500)
charge_fee(50)
print("Order B:", balance)


def after_deposit(balance, amount):
    return balance + amount


def after_fee(balance, pounds):
    return balance - pounds


print("No globals:", after_fee(after_deposit(after_deposit(0, 1000), 500), 50))
```

### Exercise 8

```python
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


for n in [0, 7, 942817]:
    print(f"digit_sum({n}) = {digit_sum(n)}")


def broken_sum(n):
    if n == 0:
        return 0
    return n % 10 + broken_sum(n // 10 - 1)     # walks past zero


try:
    broken_sum(942817)
except RecursionError as e:
    print("RecursionError:", str(e)[:50])
```

### Exercise 9

```python
def read_marks(text):
    \"\"\"From the raw text to a list of pairs.\"\"\"
    students = []
    for line in text.strip().splitlines():
        name, mark = line.split(",")
        students.append((name.strip(), float(mark)))
    return students


def average(marks):
    return sum(marks) / len(marks)


def passing(students, minimum=8.0):
    return [s for s in students if s[1] >= minimum]


def best(students):
    return max(students, key=lambda s: s[1])


def report_lines(students, minimum=8.0):
    marks = [s[1] for s in students]
    return [
        f"Students: {len(students)}",
        f"Average: {average(marks):.2f}",
        f"Passing: {len(passing(students, minimum))} of {len(students)}",
        f"Top mark: {best(students)[0]} with {best(students)[1]}",
    ]


def show(lines):
    for line in lines:
        print(line)


RAW = \"\"\"
Ana Robles, 9.2
Luis Ferrer, 7.8
Sofia Ines, 9.5
Marco Duarte, 6.4
\"\"\"

if __name__ == "__main__":
    group = read_marks(RAW)
    show(report_lines(group))
```

Three decisions worth defending when you hand this in.

**`read_marks` returns data and prints nothing.** With that, the report can be tested against a
hand-written list, with no file and no console.

**`report_lines` returns a list of strings rather than printing them.** Printing is `show`'s job, and that
is why the same report can go to a file in week 12 without touching a line.

**None of the names needs the word "and".** `read_marks`, `average`, `passing`, `best`, `report_lines`,
`show`. If one had ended up as `read_and_average`, there were two functions in there.
"""),

]

write(OUT / "en" / "w09.ipynb", en)
print("wrote", OUT / "en" / "w09.ipynb")
