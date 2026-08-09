"""notebooks/programacion-orientada-a-objetos/en/w01.2.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w01.2.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/2nd Module/
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object Oriented Programming · Review 2 of 5
## Module 2 · Comparison, logic and loops

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Comparing, deciding and repeating. The four groups of operators and the two forms of loop.

By the end of this notebook you will be able to:

1. Use the six comparison operators, and know what happens when comparing strings.
2. Combine conditions with `and`, `or` and `not`, short-circuit evaluation included.
3. Tell `in` from `is`.
4. Write `if`, `elif`, `else` and the ternary.
5. Choose between `for` and `while` by the question they answer.

### How to use this notebook

Run the cells in order. Six fail on purpose and carry a comment saying so.

The infinite loop comes with a safety cap: in a notebook a real one hangs the kernel and it has to
be restarted, losing every variable.
"""),

md("""
---
# Block 1 · Comparing

Every decision starts with a question whose answer is true or false.

| Operator | Question | Example | Result |
|---|---|---|---|
| `==` | Are they equal? | `5 == 5` | `True` |
| `!=` | Are they different? | `5 != 5` | `False` |
| `>` | Greater than? | `5 > 3` | `True` |
| `<` | Less than? | `5 < 3` | `False` |
| `>=` | Greater or equal? | `5 >= 5` | `True` |
| `<=` | Less or equal? | `5 <= 5` | `True` |
"""),

code("""
for expression, result in [("5 == 5", 5 == 5), ("5 != 5", 5 != 5), ("5 > 3", 5 > 3),
                           ("5 < 3", 5 < 3), ("5 >= 5", 5 >= 5), ("5 <= 5", 5 <= 5)]:
    print(f"{expression:<8} -> {result}")
"""),

md("""
## Strings compare letter by letter

And that comparison uses each character's numeric value, not the alphabet you have in your head.
"""),

code("""
print('"Python" == "python" ->', "Python" == "python")
print('"bag" > "apple"      ->', "bag" > "apple")
print('"Z" < "a"            ->', "Z" < "a", "<- capitals come first")
print()
print("ord('b') =", ord("b"), "· ord('B') =", ord("B"),
      "· ord('Z') =", ord("Z"), "· ord('a') =", ord("a"))
"""),

md("""
`"Z" < "a"` is true because capital Z is 90 and lowercase a is 97. Every capital sorts before every
lowercase letter.

That bites when sorting a list of hand-captured names.
"""),

code("""
names = ["ana", "Beto", "carla", "Diego"]

print("Sorted as they are:", sorted(names))
print("Normalising:       ", sorted(names, key=str.lower))
"""),

md("""
## The three that combine

| Operator | True when | Example | Result |
|---|---|---|---|
| `and` | Both parts are true | `True and False` | `False` |
| `or` | At least one is true | `True or False` | `True` |
| `not` | The part is false | `not True` | `False` |
"""),

code("""
print(f"{'A':<7}{'B':<7}{'A and B':<10}{'A or B':<10}{'not A':<7}")
print("-" * 41)
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and b):<10}{str(a or b):<10}{str(not a):<7}")
"""),

md("""
## Short-circuiting

With `and`, if the first part is false, Python already knows the answer and **does not look at the
second**. With `or` the opposite happens: if the first is true, it skips the rest.
"""),

code("""
def looks(name):
    print(f"  (evaluating {name})")
    return True


print("False and looks('second'):", False and looks("second"))
print()
print("True or looks('second'):", True or looks("second"))
print()
print("True and looks('second'):", True and looks("second"))
"""),

md("""
In the first two cases `looks` never ran.

That is not a performance curiosity: **it is what lets you write safe guards.**
"""),

code("""
data = []

# The guard first: the index is never evaluated.
if data and data[0] > 10:
    print("The first one is large")
else:
    print("Empty list, or the first one does not clear ten")
"""),

code("""
# FAILS ON PURPOSE. The same two conditions, in the wrong order.
try:
    if data[0] > 10 and data:
        print("never gets here")
except IndexError as e:
    print("IndexError:", e)
"""),

md("""
**When one condition protects the other, it goes first.** Not style, it is what makes the program
run.

## The four that get confused

| Operator | Question | Example | Result |
|---|---|---|---|
| `in` | Is it inside? | `"Pro" in "Programming"` | `True` |
| `not in` | Is it not inside? | `"swift" not in "Python"` | `True` |
| `is` | Is it the same object? | `a = [1]; b = a; a is b` | `True` |
| `is not` | Is it another object? | `[1] is not [1]` | `True` |
"""),

code("""
print('"Pro" in "Programming"  ->', "Pro" in "Programming")
print('"swift" not in "Python" ->', "swift" not in "Python")
print('3 in [1, 2, 3]          ->', 3 in [1, 2, 3])
print('"a" in {"a": 1}         ->', "a" in {"a": 1}, "<- in a dictionary it looks at keys")
"""),

md("""
## `is` is not `==`

The double equals asks whether two things are **worth** the same. `is` asks whether they **are**
exactly the same object in memory.
"""),

code("""
a = [1, 2]
b = [1, 2]
c = a

print("a == b:", a == b, "<- worth the same")
print("a is b:", a is b, "<- and not the same one")
print("a is c:", a is c, "<- c is another name for a")
"""),

code("""
# FAILS ON PURPOSE, in the worst way: it sometimes works.
x = 256; y = 256
print("256 is 256   ->", x is y)

x = 1000; y = 1000
print("1000 is 1000 ->", x is y, "<- same code, different result")
"""),

md("""
Python keeps small integers in a table and reuses them. None of that is something to lean on.

**`is` is only used with `None`, `True` and `False`.** For any other comparison, the double equals
is what you want.
"""),

code("""
result = None

print("result is None     ->", result is None)
print("result is not None ->", result is not None)
"""),

md("""
Review 4 comes back to this with list copies, and that is where it really costs.
"""),

md("""
---
# Block 2 · Deciding

A condition with no block is no use. **Indentation is what says what runs.**
"""),

code("""
temperature = 20

if temperature > 30:
    print("It is hot")
elif temperature > 20:
    print("Nice day")
elif temperature > 10:
    print("A bit cold")
else:
    print("It is cold")

print("Done")
"""),

md("""
At 20 degrees the third branch runs, not the second. `temperature > 20` is false because 20 is not
greater than 20.

**That is the boundary error**, and it is the one that costs most. If 20 should count as a nice day,
the condition is `>=`.
"""),

code("""
def classify(t, include_boundary):
    if t > 30:
        return "hot"
    elif (t >= 20 if include_boundary else t > 20):
        return "nice day"
    elif t > 10:
        return "a bit cold"
    return "cold"


for t in [19, 20, 21, 30, 31]:
    print(f"{t:>3}°  with >  : {classify(t, False):<12} with >= : {classify(t, True)}")
"""),

md("""
Only the row at 20 changes. A test that skips the exact boundary finds nothing.

## The order rules

They are evaluated top to bottom and it stops at the first true one. Reversed, a branch becomes
unreachable.
"""),

code("""
# FAILS ON PURPOSE. With the order reversed, "hot" is never reached.
def classify_wrong(t):
    if t > 10:
        return "a bit cold"
    elif t > 20:
        return "nice day"
    elif t > 30:
        return "hot"
    return "cold"


for t in [5, 15, 25, 35]:
    print(f"{t:>3}°  right: {classify(t, False):<12} wrong: {classify_wrong(t)}")
"""),

md("""
With the bad order, any temperature above ten lands in "a bit cold". Two of the four branches are
unreachable and the function raises nothing.

## The ternary

When all you want is to pick between two values, it fits on one line.
"""),

code("""
age = 20

status = "adult" if age >= 18 else "minor"
print(status)

# The same with a four-line if/else.
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(status)
"""),

md("""
The ternary reads well with two options and becomes unreadable with three. There the ordinary
`if`/`elif` belongs.

## A single equals inside an `if`
"""),

code("""
# FAILS ON PURPOSE. One sign assigns, two compare.
try:
    compile("if temperature = 20:\\n    print('yes')", "<example>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e.msg)
"""),

md("""
Python rejects it while reading the file, and that is saving you. In other languages that line
compiles, assigns 20 and the condition is always true.
"""),

md("""
---
# Block 3 · Repeating

Two forms, and the question they answer is different.

| Loop | When it is used | The question |
|---|---|---|
| `for` | You know how many passes, or have something to walk | For each of these? |
| `while` | You do not know how many, only when to stop | While this holds? |
"""),

code("""
counter = 0

while counter < 3:
    print("pass", counter)
    counter += 1        # without this line it never ends

print("Left with counter =", counter)
"""),

code("""
for n in range(10):
    if n == 3:
        continue         # skip to the next pass
    if n == 6:
        break            # leave the loop entirely
    print(n, end=" ")
print()
"""),

md("""
`continue` skips the rest of the body and carries on with the next pass. `break` leaves the loop
altogether, without evaluating the condition again.

That is why it printed `0 1 2 4 5`: it skipped 3 and stopped before 6.

## The three pieces of every loop

Initialisation, exit condition and advance. `while` forces you to write them; `for` supplies them
itself, which is why it is harder to get wrong.
"""),

code("""
# With while, all three visible.
i = 0                    # initialisation
while i < 5:             # exit condition
    print(i, end=" ")
    i += 1               # advance
print()

# With for, all three implicit.
for i in range(5):
    print(i, end=" ")
print()
"""),

md("""
## The infinite loop

Remove the advance and the condition never changes. Here it comes with a cap, because a real one
hangs the notebook's kernel.
"""),

code("""
# INFINITE LOOP ON PURPOSE, with a safety cap.
counter = 0
passes = 0
CAP = 500

while counter < 3:
    passes += 1
    # the counter += 1 is missing
    if passes >= CAP:
        print(f"Stopped by the cap after {passes} passes.")
        print(f"counter is still {counter} and the condition is still true.")
        break
"""),

md("""
**The review for every `while`**: point at the line in the body that changes the condition. If you
cannot find it, the loop does not end.

## Predict before you run

How many times does "hello" print?

- **A.** Three times.
- **B.** Five times.
- **C.** Six times.
- **D.** Never, the program enters an infinite loop.
"""),

code("""
counter = 0

while counter < 3:
    print("hello")
    counter += 1

for i in range(2):
    print("hello")
"""),

md("""
The answer is **B**, five.

| Step | Statement | `counter` | `i` | Prints |
|---|---|---|---|---|
| 1 | `counter = 0` | 0 | – | 0 |
| 2 | `while 0 < 3` | 1 | – | 1 |
| 3 | `while 1 < 3` | 2 | – | 2 |
| 4 | `while 2 < 3` | 3 | – | 3 |
| 5 | `while 3 < 3` is false | 3 | – | 3 |
| 6 | `for i in range(2)` | 3 | 0, 1 | 5 |

The `while` runs three times and the `for` twice.

## Four errors from this module

**Comparing with a single equals.** `SyntaxError`. One sign assigns, two compare.

**Failing at the boundary.** "Greater than 20" excludes 20.

**Infinite loop.** The control variable is never modified inside the body.

**Using `is` instead of `==`.** `is` compares identity. Only with `None`, `True` and `False`.

All four ran above.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

### Exercise 1 · The six, with strings

Compare `"Python"` against `"python"`, `"Java"` and `"Python "` with all six operators. Explain in a
comment why the third one is not equal.

### Exercise 2 · The full truth table

Generate with a loop the table for `A and not B`, `not (A and B)` and `not A or not B`. Say in a
comment which two agree.

### Exercise 3 · The guard that protects

Write a function `first_is_large(data)` returning true if the first element clears ten, and which
does not blow up on an empty list. Use short-circuiting, with no nested `if`.

Test it with an empty list, with `[5]` and with `[50]`.

### Exercise 4 · `is` against `==`

Prove the difference with four cases: two equal lists, two names for the same list, two small
integers and two large ones.

### Exercise 5 · The boundary

Write `grade(points)` with four ranges, and test the three values around each limit. That is nine
tests.

Say in a comment, for each limit, whether the exact value moves up or down a category and why.

### Exercise 6 · The unreachable branch

Deliberately write a version of `grade` with the ranges reversed, and prove in code that one
category is never reached by walking every possible score.

### Exercise 7 · The two loops

Solve the same thing twice, with `for` and with `while`: sum the numbers from 1 to 100 that are
multiples of three. Compare which reads better.

### Exercise 8 · The homework

Write a program that asks for numbers until the user types zero, and at the end says how many were
even and how many odd.

Since `input` stops the notebook, write it first with a list of simulated answers, then in a new
cell at the end with a real `input`.
"""),

md("""
---
## Three ideas to take away

**The order of the conditions matters.** It stops at the first true one, so the most specific goes
on top. Reversed, a branch becomes unreachable without raising anything.

**Short-circuiting is not a detail.** It is what lets you write guards that do not blow up on empty
data, and swapping the two conditions breaks the program.

**Every loop needs three pieces.** Initialisation, exit condition and advance, even when `for`
supplies them itself.

The next review is functions with parameters, return values and scope.
"""),

md('''
---
# Solutions

### Exercise 1

```python
base = "Python"
for other in ["python", "Java", "Python "]:
    print(f"{other!r:<10} == {base == other}  != {base != other}  "
          f"> {base > other}  < {base < other}  >= {base >= other}  <= {base <= other}")

# "Python " is not equal because it has a trailing space, and a space is a
# character like any other. len() gives it away: seven against six. It is the same
# problem as the dirty regions in a hand-captured file.
```

### Exercise 2

```python
print(f"{'A':<7}{'B':<7}{'A and not B':<14}{'not (A and B)':<16}{'not A or not B':<15}")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and not b):<14}"
              f"{str(not (a and b)):<16}{str(not a or not b):<15}")

# not (A and B) and not A or not B agree. It is one of De Morgan's laws: negating
# a combination turns the and into an or and negates each part.
```

That law turns up every time somebody tries to negate a compound condition and only does half the
job.

### Exercise 3

```python
def first_is_large(data):
    """True if the first element clears ten. False on an empty list."""
    return bool(data) and data[0] > 10


for case in [[], [5], [50]]:
    print(f"{str(case):<8} -> {first_is_large(case)}")
```

The `bool(data)` on the left protects the index on the right. Without short-circuiting it would need
a four-line nested `if`.

The `bool(...)` around it is not required, and without it the function would return the empty list
rather than `False`. Both count as false in an `if`, and returning an actual boolean is more honest.

### Exercise 4

```python
print("[1,2] == [1,2] :", [1, 2] == [1, 2])
print("[1,2] is [1,2] :", [1, 2] is [1, 2])

a = [1, 2]; b = a
print("b is a         :", b is a)

x = 256; y = 256
print("256 is 256     :", x is y)
x = 1000; y = 1000
print("1000 is 1000   :", x is y)
```

The last two give different results from the same code, and that is the whole reason not to use `is`
with numbers.

### Exercise 5

```python
def grade(points):
    if points >= 90:
        return "excellent"
    elif points >= 80:
        return "good"
    elif points >= 70:
        return "pass"
    return "fail"


for limit in [70, 80, 90]:
    for p in [limit - 1, limit, limit + 1]:
        print(f"{p:>4} -> {grade(p)}")
    print()

# At all three limits the exact value moves up a category, because I used >=. For
# grades that seems right to me: a policy saying "80 or more is good" includes 80.
# If it said "more than 80", it would need > and 80 would land in pass. The wording
# of the policy decides, not the convenience of the code.
```

### Exercise 6

```python
def grade_wrong(points):
    if points >= 70:
        return "pass"
    elif points >= 80:
        return "good"
    elif points >= 90:
        return "excellent"
    return "fail"


count_right = {}
count_wrong = {}
for p in range(0, 101):
    count_right[grade(p)] = count_right.get(grade(p), 0) + 1
    count_wrong[grade_wrong(p)] = count_wrong.get(grade_wrong(p), 0) + 1

print("With the good order:", count_right)
print("With the bad order: ", count_wrong)
```

With the bad order, `good` and `excellent` come out at zero across 101 scores tested. A category with
zero cases after covering the whole range is the signature of an unreachable branch.

### Exercise 7

```python
total = 0
for n in range(1, 101):
    if n % 3 == 0:
        total += n
print("With for:  ", total)

total = 0
n = 1
while n <= 100:
    if n % 3 == 0:
        total += n
    n += 1
print("With while:", total)

print("And in one line:", sum(n for n in range(1, 101) if n % 3 == 0))
```

All three give 1683. The `while` version has two extra lines and neither is about the problem: they
are about keeping count.

Here the `for` is right because you know how many passes there are before starting.

### Exercise 8

```python
# First with simulated answers, so it runs without stopping.
ANSWERS = ["4", "7", "12", "9", "0"]

even = odd = 0
for typed in ANSWERS:
    n = int(typed)
    if n == 0:
        break
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even: {even} · odd: {odd}")

# And with a real input, in a new cell at the end of the notebook:
#
# even = odd = 0
# while True:
#     n = int(input("Number (0 to finish): "))
#     if n == 0:
#         break
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"Even: {even} · odd: {odd}")
```

Note that the zero is **not counted**: the `break` comes before the classification. Were it after,
zero would count as even and the tally would be one too high.

That detail of where the `break` goes is what decides whether the sentinel lands in the result.
'''),

]

write(OUT / "en" / "w01.2.ipynb", en)
print("wrote", OUT / "en" / "w01.2.ipynb")
