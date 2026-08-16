"""notebooks/programacion-orientada-a-objetos/en/w11.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w11.en.yaml
Source code:  docs/en/courses/python-course/03 - Paths and Files/7th Module/Code035.py
                  (try/except with files, the except Exception at the end)
              docs/en/courses/python-course/02 - POO/6th Module/Code026.py
                  (InvalidOperationError: the repository's own exception)
              docs/en/courses/python-course/07 - Activities/Projects/
                  01 - Login System/login_multiple_users.py
                  (the two try blocks of the editing menu)

Code035.py runs to the end from any directory and always prints the same two
lines, checked. Both of its paths point at files that do not exist, so the two
error branches are the ones that run.

Code026.py runs to the end, checked. It already turned up in weeks 7 and 8, for
the hierarchy and for ABC; here it is quoted only for its own exception.

login_multiple_users.py cannot run headless: every menu calls input() and
os.system("cls"). Two of its functions are quoted, without the console plumbing,
and the notebook says so.

Repository bug this notebook teaches as a trap, measured:

  login_multiple_users.py, edit_user_by_index_menu, lines 80 to 90. The index is
  read with int(input(...)) and one is subtracted from it, and the try only
  catches IndexError. Typing 0 leaves index at -1, which is a valid index in
  Python: the password that changes is the last user's in the list, there is no
  exception, and the program prints "User edited". Checked.

Week 10 closed pointing here: three of its cells caught an error with try and
except without explaining the syntax. This notebook explains it and closes
pointing at week 12's files.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 11
## Topic 4 · Advanced functions and structures

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

What a program does when something goes wrong, where incoming data gets checked, and how to survive the
unplanned.

Last week, three cells caught an error with `try` and `except` without explaining the syntax: the `append`
that got three arguments, the `pop` on an empty stack, and the `array` that refuses strings. Here is what
that was.

By the end you will be able to:

1. Read a full traceback, bottom to top, and say on which line the problem started.
2. Catch by type, with one `except` per error you know how to handle and none that catches what you were
   not expecting.
3. Say which of the four clauses runs in each case, and in what order.
4. Choose where to validate, and explain why the border is worth more than twenty checks scattered about.
5. Define a custom exception named after the problem, with a message that says what to fix.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Eleven fail on purpose and carry a comment saying so.

Nine of the eleven **raise no exception at all**, which in a notebook about exceptions is exactly the
point: the worst ones do not blow up, they swallow the one that mattered. One of those nine is a real bug
in the repository that has gone years without firing.
"""),

md("""
---
# Block 1 · Exception handling

An exception is an object Python creates when something goes wrong and throws upwards, looking for
someone to handle it.

If nobody catches it anywhere in the chain of calls, the program stops and prints the trail of where it
had been before giving up. That trail is the traceback, and reading it properly is half the work.
"""),

code("""
import traceback
from pathlib import Path


def read_average(text):
    return average(split_values(text))


def split_values(text):
    return [float(x) for x in text.split(",")]


def average(numbers):
    return sum(numbers) / len(numbers)


print("With good data:", read_average("9.2, 7.8, 9.5"))
print()

try:
    read_average("9.2, seven point eight, 9.5")
except ValueError as e:
    print(traceback.format_exc())
"""),

code("""
try:
    read_average("9.2, seven point eight, 9.5")
except ValueError as e:
    frames = traceback.extract_tb(e.__traceback__)
    kind, message = type(e).__name__, str(e)

print("Type:   ", kind)
print("Message:", message)
print()
print("The frames, in the order Python prints them:")
for i, frame in enumerate(frames):
    print(f"  {i}  in {frame.name:<16}{frame.line}")

print()
print("The first is where the call started:", frames[0].name)
print("The last is where it blew up:       ", frames[-1].name, "->", frames[-1].line)
"""),

md("""
A traceback is read **bottom to top**.

The last line carries the type and the message, which is what you are really after. The frame just above
it is the line that failed. The ones further up are the path taken to get there, and they earn their keep
when the line that failed was correct and whoever called it was not.

In this chain the error is not in `float`, which did its job. It is that somebody handed `split_values` a
piece of text that did not hold three numbers, and that is only visible going up.

## One `except` per type
"""),

code("""
# FAILS ON PURPOSE. Two different errors ask for two different answers.
def age_to_factor(value):
    try:
        age = int(value)
        return 10 / age
    except ValueError:
        return "That is not a whole number"
    except ZeroDivisionError:
        return "Age cannot be zero"


for value in ["abc", "0", "20", "  7 "]:
    print(f"  {value!r:<8}-> {age_to_factor(value)}")

print()
print("Both errors inherit from Exception:")
for kind in [ValueError, ZeroDivisionError]:
    print(f"  {kind.__name__:<20}{[c.__name__ for c in kind.__mro__[:-1]]}")
"""),

md("""
Four inputs, three paths, and `"  7 "` with its spaces goes through anyway because `int` trims them.

The **first** `except` whose type matches runs, and the rest are never even checked. That is why the order
matters as soon as the types are related, which is the cell further down.

Look at the inheritance tree printed at the end. `ZeroDivisionError` does not hang straight off
`Exception`: it goes through `ArithmeticError`. That means `except ArithmeticError` would catch it too,
along with overflow and the floating point error.

## The four clauses, and when each one runs
"""),

code("""
def attempt(value):
    ran = []
    try:
        ran.append("try")
        number = int(value)
    except ValueError:
        ran.append("except")
        number = None
    else:
        ran.append("else")
    finally:
        ran.append("finally")
    return number, ran


print(f"{'input':<10}{'result':<12}{'clauses that ran'}")
for value in ["7", "seven"]:
    number, ran = attempt(value)
    print(f"{value!r:<10}{str(number):<12}{' -> '.join(ran)}")

print()
print("The else runs only when the try reached the end without tripping.")
print("The finally runs in both cases.")
"""),

md("""
Two inputs, and the list of what ran for each of them.

`else` is the happy path. What goes there is whatever only makes sense if the `try` went well, and the
advantage is that it leaves the `try` with the risky line and nothing else. A one-line `try` says exactly
what you expected to fail.

`finally` runs every time. What goes there is whatever has to be closed, whatever happens, and in week 12
it will be the place where a file gets closed.

## Predict before you run

```python
def read(value):
    try:
        return int(value)
    except ValueError:
        return 0
    finally:
        print("done")


print(read("7"))
```

- **A.** First `done`, then `7`.
- **B.** First `7`, then `done`.
- **C.** Only `7`, because the `return` skips the `finally`.
- **D.** Only `done`, because the `finally` discards the `return`.
"""),

code("""
def read(value):
    try:
        print("  (the try worked out the return value)")
        return int(value)
    except ValueError:
        return 0
    finally:
        print("  done")


print("Calling read('7'):")
result = read("7")
print("It returned:", result)
"""),

md("""
The answer is **A**.

`return int(value)` works out the 7 and holds it, but the function has not left yet. `finally` exists
precisely to run in that gap, between "I know what I am going to return" and "I am out". That is why
`done` comes first and the `7` is printed afterwards, when the outer `print` receives the value.

That gap has a consequence hardly anyone sees coming.

## The `finally` that swallows the exception
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A return inside the finally.
import warnings

SOURCE = '''
def save(record):
    try:
        raise ValueError(f"{record!r} could not be saved")
    finally:
        return "saved"
'''

with warnings.catch_warnings(record=True) as notices:
    warnings.simplefilter("always")
    exec(compile(SOURCE, "<example>", "exec"), globals())

print("Does this version of Python warn when it compiles that?",
      "yes:" if notices else "no", notices[0].message if notices else "")
print()
print("What it returns:", save("A001"))
print("Exceptions that reached the caller: none")
print()
print("And the ValueError was raised. You can see it by taking the return out:")


def save_well(record):
    try:
        raise ValueError(f"{record!r} could not be saved")
    finally:
        print("  (the finally ran all the same)")


try:
    save_well("A001")
except ValueError as e:
    print("  ValueError:", e)
"""),

md("""
The first function raised a `ValueError` and the caller received the string `"saved"`.

A `return` inside `finally` **replaces whatever the function was going to do**, and what it was going to
do was propagate the exception. The exception is raised, the `finally` runs, the `return` wins, and the
error disappears without leaving a trace anywhere.

It is the quietest error of the session and the hardest to find afterwards, because the symptom is that a
record did not get saved and nobody has a single line of log saying so.

**Only what closes resources goes in `finally`.** No `return`, no `break`, no `continue`.

## The variable that only exists if there was no error
"""),

code("""
# FAILS ON PURPOSE. The variable is assigned inside the try and used in the except.
def load(path):
    try:
        handle = open(path, encoding="utf-8")
        return handle.read()
    except FileNotFoundError:
        print("  The file is not there")
        return ""
    finally:
        handle.close()           # handle may never have been created


Path("exists.txt").write_text("hello", encoding="utf-8")
print("With a file that exists:", repr(load("exists.txt")))

print()
print("With one that is not there:")
try:
    load("missing.txt")
except NameError as e:
    print("  NameError:", e)
    print("  <- and this error covered up the FileNotFoundError, which was the real one")
"""),

md("""
The file was not there, `open` raised `FileNotFoundError`, the `except` handled it, and the `finally`
brought the whole thing down with a `NameError` about a variable that never got assigned.

It is what the slide announces as the risk of `finally`, and it comes with an aggravating factor: **the
cleanup error replaces the original one**. Whoever reads the traceback sees a `NameError` with no
connection at all to the cause.

The canonical fix is not writing that `finally`. Next week's `with` block closes the file on its own, and
only if it got as far as opening.

## The order of the `except` clauses
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A general except before the specific one.
def read_config(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError:
        return "operating system error"
    except FileNotFoundError:
        return "the file is not there"


print("A path that does not exist:", read_config("missing.txt"))
print()
print("Why? Because one inherits from the other:")
print("  FileNotFoundError.__mro__:",
      [c.__name__ for c in FileNotFoundError.__mro__[:-1]])
print("  Is FileNotFoundError an OSError?",
      issubclass(FileNotFoundError, OSError))
print("  Is IOError the very same object?", IOError is OSError)
print()


def read_config_well(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return "the file is not there"
    except OSError:
        return "operating system error"


print("With the order the right way round:", read_config_well("missing.txt"))
"""),

md("""
The second branch is unreachable and Python says nothing.

`FileNotFoundError` inherits from `OSError`, so the first `except` matches and the second is never
checked. The message that reaches the user is the generic one, and the specific one, which was the useful
one, ended up written as decoration.

**The `except` clauses go from the particular to the general.** It is the same rule as `elif`, and here
there is no warning to remind you of it.

`Code035.py`, on its lines 17 to 20, has the right order: `FileNotFoundError` first and `IOError` after.
It is worth knowing that `IOError` **is** `OSError` since Python 3.3, the same object under two names, and
that this is why that second `except` catches far more than its name suggests.
"""),

md("""
---
# Block 2 · Validating input

The difference between a program that crashes and one that explains what to fix comes down to where you
put the check.

The four errors in this block are the four on the slide, run.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Error 02: an except with pass inside.
DATA = [{"name": "Ana", "mark": "9.2"}, {"name": "Luis", "mark": "7,8"},
        {"name": "Sofia", "mark": "9.5"}]

marks = []
for row in DATA:
    try:
        marks.append(float(row["mark"]))
    except Exception:
        pass

print("Input rows:", len(DATA))
print("Marks converted:", len(marks), marks)
print("Average:", round(sum(marks) / len(marks), 2))
print()
print("The average looks reasonable and one student is missing from it.")
print("Nobody knows which one, or why, or that anyone is missing at all.")
print()

marks, rejected = [], []
for row in DATA:
    try:
        marks.append(float(row["mark"]))
    except ValueError as e:
        rejected.append((row["name"], row["mark"], str(e)))

print("With the except by type and no pass:")
print("  converted:", len(marks))
for name, value, reason in rejected:
    print(f"  rejected: {name} with {value!r} -> {reason}")
"""),

md("""
Three rows go in, two come out, and the average is worked out over the two as if nothing had happened.

`except Exception: pass` is the instruction to throw the error in the bin. The program carries on, the
result looks plausible, and the missing data shows up nowhere.

Look at the fix: taking the `pass` out is not enough. You have to **name the type** and **keep what was
rejected**, because a discarded row is information, not noise. The second half of the cell says exactly
which row fell over and with what value, which is what somebody will need in order to correct the entry.

## The `except` that does not say what of
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Error 01: an except with no type swallows a typo.
def average(rows):
    try:
        total = 0
        for r in rows:
            total += float(r["mark"])
        return total / len(rowss)            # rowss, with two esses
    except:                                  # noqa: E722
        return 0.0


print("Average:", average(DATA[:1]))
print("The program carried on with an average of zero, and nobody mistyped any data.")
print()


def average_visible(rows):
    total = 0
    for r in rows:
        total += float(r["mark"])
    return total / len(rowss)


try:
    average_visible(DATA[:1])
except NameError as e:
    print("Without the except:", type(e).__name__ + ":", e)
"""),

md("""
The error was not in the data. It was in the variable's name, and the `except` with no type swallowed it.

A bare `except` catches **everything** that inherits from `BaseException`: programming errors like this
`NameError`, the `KeyboardInterrupt` from somebody pressing Ctrl+C, and the `SystemExit` from somebody
asking to quit. Not one of those three is an error you would want to handle there.

It is error 01 on the slide, and its milder version, `except Exception`, has the same problem with
programming errors: it turns them into a default value.

## What a bare `except` catches beyond what you meant
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The except that stops the program quitting.
def exit_cleanly():
    print("  closing...")
    raise SystemExit(0)


try:
    exit_cleanly()
except:                                      # noqa: E722
    print("The bare except caught even the program's exit.")

print()
try:
    raise KeyboardInterrupt()
except:                                      # noqa: E722
    print("And the Ctrl+C from whoever was using it, too.")

print()
print("Neither of the two inherits from Exception:")
for kind in [SystemExit, KeyboardInterrupt, ValueError]:
    print(f"  {kind.__name__:<20}inherits from Exception? {issubclass(kind, Exception)}")

print()
print("That is why except Exception is already much better than a bare except.")
print("And an except by type is still better than either.")
"""),

md("""
The program asked to quit and the `except` would not let it.

That is the technical argument against the bare `except`, and it is no technicality: in a program with a
loop, an `except` like that inside the loop makes Ctrl+C stop working. The only way to close it is to kill
the process.

`SystemExit` and `KeyboardInterrupt` hang off `BaseException` and not off `Exception` precisely so that
`except Exception` leaves them alone. That design only works if nobody writes the bare `except`.

## The forty-line `try`
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Error 03: a try around all of the work.
RAW = "A001,Ana Robles,9.2\\nA002,Luis Ferrer,seven\\nA003,Sofia Ines,9.5"

try:
    rows = RAW.split("\\n")
    split_rows = [r.split(",") for r in rows]
    ids = [p[0] for p in split_rows]
    names = [p[1] for p in split_rows]
    marks = [float(p[2]) for p in split_rows]
    mean = sum(marks) / len(marks)
    report = f"{len(ids)} students, average {mean:.2f}"
except ValueError:
    report = "there was a problem with the data"

print(report)
print("Which of the seven lines failed? The message does not say.")
print()

marks, problems = [], []
for number, line in enumerate(RAW.split("\\n"), start=1):
    student_id, name, raw = line.split(",")
    try:
        marks.append(float(raw))
    except ValueError as e:
        problems.append(f"row {number} ({student_id}): {raw!r} is not a number")

print("With the try around the risky line and nothing else:")
print("  converted:", len(marks))
for p in problems:
    print("  ", p)
"""),

md("""
Seven lines inside the `try`, and a message that is no use to anybody.

`except ValueError` caught `float`'s error, but it would also have caught an unpacking error, one from
converting the student ID, and any other `ValueError` out of the seven lines. When it fires, you do not
know which one failed.

**The `try` wraps the risky line and nothing else.** The second half turns the same problem into a message
that gives the row, the student ID and the exact value that could not be read, and carries on with the
rest.

## Exceptions for what happens all the time
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Error 04: exceptions as the normal flow.
import time

INVENTORY = {"keyboard": 12, "monitor": 4}
QUERIES = ["keyboard", "mouse", "monitor", "webcam", "camera"] * 40_000

start = time.perf_counter()
found = 0
for part in QUERIES:
    try:
        INVENTORY[part]
        found += 1
    except KeyError:
        pass
with_exception = time.perf_counter() - start

start = time.perf_counter()
found_if = 0
for part in QUERIES:
    if part in INVENTORY:
        found_if += 1
with_if = time.perf_counter() - start

print("Both count the same:", found == found_if, f"({found:,})")
print(f"Queries: {len(QUERIES):,}, of which "
      f"{1 - found / len(QUERIES):.0%} fail")
print()
print(f"With try/except: {with_exception:.4f} s")
print(f"With if:         {with_if:.4f} s")
print(f"The version with exceptions took {with_exception / with_if:.1f} times longer.")
"""),

md("""
The same count, and the version with exceptions takes noticeably longer.

Raising an exception costs something: the object has to be built, the traceback assembled and the stack
unwound. When the case turns up once in a thousand, that goes unnoticed. When it turns up sixty per cent
of the time, it was an `if`.

It is error 04 on the slide, and the criterion is right there in the name: **exceptions are for the
exceptional**. If you can predict how often the case is going to happen, it was not exceptional.

The cost is the small argument anyway. The big one is about reading: a `try` around something that happens
all the time lies to whoever reads the code about what the unusual thing is.

## The bug that has gone years without firing
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. login_multiple_users.py, lines 80 to 90.
usernames = ["ana", "luis", "sofia"]
passws = ["pass-ana", "pass-luis", "pass-sofia"]


def edit_by_index(usernames, passws, typed, new):
    \"\"\"Lines 80 to 90 of the file, with the input() replaced by a parameter.\"\"\"
    index = int(typed)
    index -= 1
    try:
        passws[index] = new
        return "User edited."
    except IndexError:
        return "Index not found."


print("Before:", passws)
print()
print("Typing 2, which is what the menu expects:")
print(" ", edit_by_index(usernames, passws, "2", "new-luis"))
print(" ", passws)

print()
print("Typing 0, which the menu does not expect:")
print(" ", edit_by_index(usernames, passws, "0", "INTRUDER"))
print(" ", passws)
print()
print("Whose password changed?", usernames[-1])
print("Was there an IndexError?", "no, because passws[-1] is a perfectly valid index")
"""),

md("""
Typing `0` changed `sofia`'s password, the last one in the list, and the program answered `User edited.`

The function subtracts one to turn the menu option into an index, and the `try` only catches `IndexError`.
But `-1` does **not** produce an `IndexError`: in Python it is the last element. The only out-of-range
index the `except` ever gets to see is the one that goes past the top.

It is this block's error 04 the other way round: it is not that the exception is one too many, it is that
**the `except` is waiting for an error that does not happen in this case**. Catching by type is no use if
the bad case raises nothing.

The fix is not another `except`. It is a check beforehand:

```python
if not 1 <= option <= len(usernames):
    return "Index not found."
```

**A range is validated with an `if`, not with an `except`.** That is exactly what this block's slide says:
validate at the border, and from there inwards trust it.

## Where the check goes
"""),

code("""
class Account:
    \"\"\"The check lives in the constructor and in the setter. Nowhere else.\"\"\"

    def __init__(self, holder: str, balance: float = 0.0) -> None:
        if not holder.strip():
            raise ValueError("the holder cannot be empty")
        self._holder = holder.strip()
        self.balance = balance                # goes through the setter

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"the balance cannot be negative, got {value}")
        self._balance = float(value)

    def deposit(self, amount: float) -> None:
        self.balance = self.balance + amount   # goes through the setter again

    def __repr__(self) -> str:
        return f"Account({self._holder!r}, {self._balance:,.2f})"


acc = Account("Ana Robles", 1500)
acc.deposit(500)
print(acc)

for trial in [lambda: Account("   "), lambda: Account("Luis", -10),
              lambda: acc.deposit(-3000)]:
    try:
        trial()
    except ValueError as e:
        print("  ValueError:", e)

print()
print("The object never ended up in an impossible state:", acc)
"""),

md("""
Three attempts to put bad data in, and three messages that say what to fix.

The check lives in two places: the constructor and the `setter`. `deposit` checks nothing, because it
assigns to `self.balance` and that goes through the `setter`. That is week 5's property paying its first
real dividend.

What you gain is that **the rest of the program is written assuming correct data**. No function taking an
`Account` has to wonder whether the balance is negative, because there is no way to build one like that.

What you lose if the rule breaks: if every function checks on its own, the rule lives in twenty places and
sooner or later two of them say different things.
"""),

md("""
---
# Block 3 · Software robustness

An error with a name of its own and a message saying what to fix beats twenty lines of defences scattered
about.
"""),

code("""
# Code026.py, lines 7 to 37: the two versions the file writes one after the other
class GenericStream:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise Exception("Stream already opened.")
        self.opened = True


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise InvalidOperationError("Stream already opened.")
        self.opened = True

    def close(self) -> None:
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False


s = Stream()
s.open()
print("With the custom exception:")
for action in [s.open, s.close, s.close]:
    try:
        action()
        print(f"  {action.__name__}() -> ok, opened={s.opened}")
    except InvalidOperationError as e:
        print(f"  {action.__name__}() -> InvalidOperationError: {e}")

print()
print("With the generic one, the caller cannot tell it apart from anything else:")
g = GenericStream()
g.open()
try:
    g.open()
except InvalidOperationError:
    print("  caught by type")
except Exception as e:
    print("  the whole of Exception had to be caught:", e)
"""),

md("""
`Code026.py` writes the class twice, and the second time only one word changes: `Exception` becomes
`InvalidOperationError`.

The file justifies it on its line 16 with *"But we dont want a generic Exception. We want a specific
Exception"*, and that is the whole reason. A custom exception is a class inheriting from `Exception`, with
`pass` inside, and with that it is already finished.

What it buys is being able to catch it on its own. With a generic `Exception` there is no way to write an
`except` that handles "the stream was already open" without catching every other error in the program
along with it.

## What happens when a custom exception inherits from the wrong place
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A custom exception hanging off BaseException.
class InsufficientFunds(BaseException):      # <- should be Exception
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"short by {amount - balance:,.2f}")
    return balance - amount


print("Does it inherit from Exception?", issubclass(InsufficientFunds, Exception))
print("Chain:", [c.__name__ for c in InsufficientFunds.__mro__])
print()

try:
    try:
        withdraw(100, 150)
    except Exception as e:
        print("The safety net caught it:", e)
except InsufficientFunds as e:
    print("It went straight past the except Exception:", e)

print()


class InsufficientFundsWell(Exception):
    pass


try:
    raise InsufficientFundsWell("short by 50.00")
except Exception as e:
    print("Hanging off Exception, the net catches it:", type(e).__name__, "-", e)
"""),

md("""
The exception went past the `except Exception` in the layer above and carried on up.

A serious program usually has, at the very top, an `except Exception` that records the error and keeps the
program alive. An exception hanging off `BaseException` skips that net, and the program falls over with a
traceback in the user's face.

**A custom exception inherits from `Exception`, never from `BaseException`.** `BaseException` is reserved
for what is not a program error: the exit and the keyboard interrupt, which are the two from the bare
`except` cell.

## The message that says what to fix
"""),

code("""
class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(f"${self.shortfall:,.2f} short to withdraw ${amount:,.2f} "
                         f"from a balance of ${balance:,.2f}")


class Account2:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds(self.balance, amount)
        self.balance -= amount


account = Account2(100)

try:
    account.withdraw(150)
except InsufficientFunds as e:
    print("Type:    ", type(e).__name__)
    print("Message: ", e)
    print("And the data as well, without having to read the text:")
    print("   shortfall:", e.shortfall)
    print("   a suggestion is possible:", f"withdraw up to ${e.balance:,.2f}")

print()
print("The balance did not move:", account.balance)
"""),

md("""
Three things arrive together: the type, the message and the data.

The message says **what to fix**, not only that something went wrong. Compared with `"Error"` or with
`"Invalid operation"`, the difference is that whoever reads it knows what to type on the next attempt.

The attributes are the other half. Keeping `balance`, `amount` and `shortfall` on the exception lets
whoever catches it use the numbers without having to pull them out of the text with `split`, which is what
people end up doing when the exception carries nothing but a string.

Look at the last line: **the object did not change state**. The check runs before touching anything, which
is why an exception does not leave the account half withdrawn.

## `raise ... from`, so the cause is not lost
"""),

code("""
class CaptureError(Exception):
    pass


def read_mark(text):
    try:
        return float(text)
    except ValueError as e:
        raise CaptureError(f"the mark {text!r} is not a number") from e


try:
    read_mark("seven point eight")
except CaptureError as e:
    print("What the caller sees:", type(e).__name__ + ":", e)
    print("The original cause:  ", type(e.__cause__).__name__ + ":", e.__cause__)

print()
import traceback
try:
    read_mark("seven point eight")
except CaptureError as e:
    print(traceback.format_exc())
"""),

md("""
Two exceptions in a single traceback, joined by the line *"The above exception was the direct cause of the
following exception"*.

`raise ... from e` translates a technical error into one from the domain **without erasing the original**.
The caller catches `CaptureError`, which is what matters to them; whoever is debugging still sees the
`ValueError` from `float` that caused it.

Without the `from`, Python chains them anyway, but with the phrase *"During handling of the above
exception, another exception occurred"*, which says something different: that the second error happened
**while** the first was being handled, not that it is a translation of it.

## The repository file, run
"""),

code("""
# Code035.py, lines 10 to 47, with the paths moved to the working directory
from pathlib import Path

try:
    file_path = Path("x.txt")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except IOError:
    print(f"An error occurred while reading the file at {file_path}.")

try:
    with open("app.py") as file:
        print("File opened")
except Exception as ex:
    print("Could not open the file")

print()
print("The original file prints these same two lines, from any directory,")
print("because both of its paths point at files that do not exist.")
"""),

md("""
`Code035.py` runs to the end and always down the error branch. Both of its paths point at files that do
not exist, so the file's happy path has never been seen.

Two things we would write differently today, and neither of them is a syntax error.

**`file_path` is assigned inside the `try`.** It does not blow up here because building a `Path` cannot
fail, but it is the exact pattern from the `NameError` cell. The assignment goes outside.

**`except Exception as ex` catches everything and never uses `ex`.** The name is captured and thrown away,
so the message printed is the same whether the file is not there, the permissions are wrong, or somebody
misspelled a variable name three lines above.

What the file does get right, and is worth copying: it puts `FileNotFoundError` **before** `IOError`.
"""),

md("""
---
## Four errors from this session

**An `except` with no type.** It catches the `NameError` from a typo, Ctrl+C and the program's exit. Name
the type you actually expect.

**An `except` with `pass` inside.** The error vanishes without a trace and the defect resurfaces three
screens later, turned into an average that does not add up.

**A `try` wrapped round forty lines.** When it fires you cannot tell which of the forty failed. Wrap the
risky line only.

**Exceptions for the normal flow.** If the case happens half the time, it was an `if`. And a range is
validated with an `if` even when the `except` is already written, as in the login system's menu.
"""),

md("""
---
# Exercises

This week's lab is hardening a marks reader. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · Reading the traceback

Write three functions that call one another in a chain and make the last one fail. Catch the exception and
print the frames with `traceback.extract_tb`.

Say in a comment which of the three frames holds the real error and why it is not the last one.

### Exercise 2 · One `except` per type

Write a function that turns a piece of text into a number and divides ten by it. Handle the text that is
not a number and the zero separately.

Try it with five different inputs and print what each one returned.

### Exercise 3 · The four clauses

Write a function with `try`, `except`, `else` and `finally` that keeps a list of which clause ran. Call it
with a good input and a bad one and print both lists.

### Exercise 4 · The `finally` that swallows

Write a function that raises a `ValueError` inside the `try` and has a `return` in the `finally`. Show
that the caller receives no exception at all.

Take the `return` out and check that now it does come up.

### Exercise 5 · The order matters

Write two versions of the same function, one with `except OSError` before `except FileNotFoundError` and
the other the other way round. Call both with a path that does not exist and show that they return
different things.

Print `FileNotFoundError.__mro__` to explain why.

### Exercise 6 · No `pass`

Take a list of ten entries where three carry the mark written wrong. Convert them, keeping the ones that
failed apart, with the name and the reason.

Print how many went in, how many were rejected, and check that the two add up to ten.

### Exercise 7 · Validating at the border

Write a `Student` class with a student ID and an average. The student ID cannot be empty and the average
has to be between zero and ten. Both checks go in the constructor and in the `setter`.

Try to build three invalid objects and catch the three `ValueError`s.

### Exercise 8 · A domain exception

Define `MarkOutOfRange(Exception)` that keeps the value it received and the range allowed, and builds its
message out of both. Raise it from the previous exercise's `setter`.

Catch it and print the message and the attributes separately.

### Exercise 9 · The lab

You are handed a script that reads marks from the console and blows up on any odd input. Make it survive
text, numbers out of range and a file that is not there.

Constraints: no `except` without a type, none left empty, and the `try` wraps only the risky line.

The criterion is that every message tells whoever reads it what to fix in order to carry on.
"""),

md("""
---
## Three things to take away

**One `except` per type, and named.** `except Exception` catches what you were not expecting and hides the
very error that mattered. The bare `except` takes Ctrl+C with it as well.

**Validation lives at the border.** The check happens where the value enters, in the constructor and in
the `setter`, and from there inwards the rest of the program trusts it. A range is validated with an `if`,
not by waiting for an `IndexError` that sometimes never arrives.

**`finally` runs every time.** With an error, without one, and with a `return` waiting its turn. It is
where you close what you opened, and it is the only thing that should go there.

Week 12 opens the files unit: paths that work on any system, the `with` block that closes on its own, and
the usual CSV. One cell in this notebook opened a file by hand and had to write the `finally` that closed
it; next week's `with` is what stops that `finally` from being written.
"""),

md("""
---
# Solutions

### Exercise 1

```python
import traceback


def level_1(text):
    return level_2(text)


def level_2(text):
    return level_3(text)


def level_3(text):
    return float(text)


try:
    level_1("not a number")
except ValueError as e:
    for frame in traceback.extract_tb(e.__traceback__):
        print(f"line {frame.lineno:>3}  {frame.name:<10}{frame.line}")

# The last frame is float(text), which did its job properly: it was handed text
# that was not a number. The real error is in the frame above it, in whoever
# called with that text without checking it first.
```

### Exercise 2

```python
def divide(text):
    try:
        return 10 / int(text)
    except ValueError:
        return "not a whole number"
    except ZeroDivisionError:
        return "cannot be zero"


for entry in ["5", "0", "abc", "  2  ", "3.5"]:
    print(f"{entry!r:<10}{divide(entry)}")
```

### Exercise 3

```python
def attempt(value):
    ran = []
    try:
        ran.append("try")
        n = int(value)
    except ValueError:
        ran.append("except")
        n = None
    else:
        ran.append("else")
    finally:
        ran.append("finally")
    return n, ran


print(attempt("7"))
print(attempt("seven"))
```

### Exercise 4

```python
SOURCE = '''
def save():
    try:
        raise ValueError("it was not saved")
    finally:
        return "ok"
'''
exec(compile(SOURCE, "<ex>", "exec"), globals())
print("Returns:", save())


def save_well():
    try:
        raise ValueError("it was not saved")
    finally:
        print("the finally ran")


try:
    save_well()
except ValueError as e:
    print("Now it does come up:", e)
```

### Exercise 5

```python
from pathlib import Path


def general_first(path):
    try:
        return Path(path).read_text()
    except OSError:
        return "system error"
    except FileNotFoundError:
        return "not there"


def specific_first(path):
    try:
        return Path(path).read_text()
    except FileNotFoundError:
        return "not there"
    except OSError:
        return "system error"


print(general_first("nothing.txt"))
print(specific_first("nothing.txt"))
print([c.__name__ for c in FileNotFoundError.__mro__])

# FileNotFoundError inherits from OSError, so the general except matches first
# and the specific one is left unreachable.
```

### Exercise 6

```python
ENTRIES = [("Ana", "9.2"), ("Luis", "7,8"), ("Sofia", "9.5"), ("Marco", "6.4"),
           ("Paula", ""), ("Ruben", "8.1"), ("Elena", "9,0"), ("Ivan", "7.7"),
           ("Oscar", "8.8"), ("Sara", "6.9")]

good, rejected = [], []
for name, raw in ENTRIES:
    try:
        good.append((name, float(raw)))
    except ValueError as e:
        rejected.append((name, raw, str(e)))

print("Went in:", len(good))
print("Rejected:", len(rejected))
for name, raw, reason in rejected:
    print(f"  {name}: {raw!r} -> {reason}")
print("Do they add up to ten?", len(good) + len(rejected) == len(ENTRIES))
```

### Exercise 7

```python
class Student:
    def __init__(self, student_id, average):
        if not student_id.strip():
            raise ValueError("the student ID cannot be empty")
        self._student_id = student_id.strip()
        self.average = average

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        if not 0 <= value <= 10:
            raise ValueError(f"the average has to run from 0 to 10, got {value}")
        self._average = float(value)


for trial in [lambda: Student("", 9.0), lambda: Student("A001", 11),
              lambda: Student("A002", -1)]:
    try:
        trial()
    except ValueError as e:
        print("ValueError:", e)
```

### Exercise 8

```python
class MarkOutOfRange(Exception):
    def __init__(self, value, low=0, high=10):
        self.value = value
        self.low = low
        self.high = high
        super().__init__(f"{value} is outside the range allowed "
                         f"[{low}, {high}]")


class Student2:
    def __init__(self, student_id, average):
        self._student_id = student_id
        self.average = average

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        if not 0 <= value <= 10:
            raise MarkOutOfRange(value)
        self._average = float(value)


try:
    Student2("A001", 11.5)
except MarkOutOfRange as e:
    print("Message:", e)
    print("Value:", e.value, " range:", e.low, "to", e.high)
```

### Exercise 9

```python
from pathlib import Path


class InvalidMark(Exception):
    def __init__(self, raw, reason):
        self.raw = raw
        self.reason = reason
        super().__init__(f"{raw!r}: {reason}")


def to_mark(raw):
    \"\"\"The input border. Everything that leaves here is already usable.\"\"\"
    text = raw.strip()
    try:
        value = float(text)
    except ValueError:
        raise InvalidMark(text, "is not a number") from None
    if not 0 <= value <= 10:
        raise InvalidMark(text, "is outside the range 0 to 10")
    return value


def read_lines(path):
    try:
        return Path(path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"{path} is not there. Check the name and try again.")
        return []


def process(lines):
    good, bad = [], []
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            good.append(to_mark(line))
        except InvalidMark as e:
            bad.append(f"row {number}: {e}")
    return good, bad


def report(good, bad):
    if good:
        print(f"{len(good)} marks, average "
              f"{sum(good) / len(good):.2f}")
    else:
        print("Not one valid mark went in.")
    for b in bad:
        print("  ", b)


if __name__ == "__main__":
    INPUTS = ["9.2", "seven", "11", "8.0", "-1", "", "  7.5  "]
    Path("marks.txt").write_text("\\n".join(INPUTS), encoding="utf-8")

    good, bad = process(read_lines("marks.txt"))
    report(good, bad)

    process(read_lines("missing.txt"))
```

Three decisions worth defending when you hand this in.

**`to_mark` is the only border.** It converts and validates in the same place, and from there inwards
nobody asks again whether the number is usable. `report` takes a list of floats and is written without a
single defence.

**Every `except` names a type and none of them carries `pass`.** `float`'s `ValueError` is translated into
`InvalidMark`, which is the name of the problem in the instructor's language, not in Python's.

**The `from None` is deliberate.** Here `float`'s `ValueError` adds nothing: the custom message already
says it. When the technical cause does matter, you write `from e` and the traceback chains them.
"""),

]

write(OUT / "en" / "w11.ipynb", en)
print("wrote", OUT / "en" / "w11.ipynb")
