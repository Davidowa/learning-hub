"""notebooks/programacion-orientada-a-objetos/en/w12.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w12.en.yaml
Source code:  docs/en/courses/python-course/03 - Paths and Files/7th Module/Code029.py
                  (pathlib: exists, resolve, name, stem, suffix, parent, glob)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code030.py
                  (read_text, write_text, modes a and w, shutil.copy)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code31.py
                  (text: read, walking it by lines, separators, dict(zip(...)))
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code32.py
                  (csv.reader, csv.DictReader, csv.writer)
              docs/en/courses/python-course/07 - Activities/Exams/2ndMidTerm/
                  script1.py, script3.py

Nothing from the 7th Module is run out of the repository: Code030.py writes
test.txt and test_copy.txt inside docs/, and Code34.py leaves files.zip and
extracted_files/. The notebook reproduces their code in the session's working
directory, which on Colab is /content and here is a temporary directory.

Measured things from the repository that the notebook teaches as a trap, without
correcting them:

  script1.py lines 9 to 12 build the path as filepath + filename, where filepath
  is the string "./07 - Activities/Exams/2ndMidTerm/". The script runs when the
  current directory is docs/en/courses/python-course and dies with
  FileNotFoundError from its own folder. Checked both ways.

  Code030.py lines 35 and 36 claim read_text is more efficient than open
  "because in the read_text method, the file is opened and closed
  automatically". read_text calls open internally; the source code is printed in
  a cell.

  Code030.py line 20 documents st_ctime as "time of creation". That is true on
  Windows and false on Linux and macOS, where it is the time of the last
  metadata change. Colab runs on Linux.

  script3.py line 25 splits each CSV row with split(","). It works with today's
  videogames.csv, whose eight titles carry no commas, and blows up with an
  unpacking ValueError as soon as one of them does.

Week 11 closed pointing here: two of its cells opened a file by hand and had to
write the finally that closed it. This notebook closes pointing at week 13's
binary files and random access.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 12
## Topic 5 · Files

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Data stops living in memory. Paths that work on any system, the block that closes on its own, and the
text format everybody already uses.

Last week two cells opened a file by hand and one of them fell over with a `NameError` inside the
`finally` that was trying to close it. This notebook starts by making that `finally` stop being written.

By the end you will be able to:

1. Build paths with `pathlib` and read the name, the suffix and the parent folder without cutting strings.
2. Explain what breaks when a file gets opened without `with`, with the proof on disk.
3. Pick an open mode knowing which one creates the file, which keeps it and which empties it on opening.
4. Read and write a CSV with `DictReader` and `DictWriter`, without depending on the order of the columns.
5. Say why a relative path typed by hand works on one machine and fails on the next one.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Eleven fail on purpose and carry a comment saying so.

Seven of the eleven **raise no exception at all**. The worst of the lot writes a hundred rows, the program
finishes without complaining, and the file on disk comes out empty.

Everything this notebook writes stays in the session's working directory, which on Colab is `/content`.
It touches nothing in the repository.
"""),

md("""
---
# Block 1 · Paths and files

Before reading anything you have to know where it is. And a path typed by hand works on your machine and
fails on the next one.
"""),

code("""
import os
from pathlib import Path, PureWindowsPath, PurePosixPath

path = Path("data") / "students.csv"

print("The path:      ", path)
print("The name:      ", path.name)
print("No suffix:     ", path.stem)
print("The suffix:    ", path.suffix)
print("The folder:    ", path.parent)
print("Is it there?   ", path.exists())
print("The parts:     ", path.parts)

print()
print("This notebook runs on", "Windows" if os.name == "nt" else "Linux or macOS",
      f"(os.name = {os.name!r})")
print()
print("The same path, written by each system:")
print("  Windows:", PureWindowsPath("data") / "students.csv")
print("  Linux:  ", PurePosixPath("data") / "students.csv")
print()
print("That is why the slash is always written the same way and Python puts in the right one.")
"""),

md("""
The slash joins pieces of a path. It is not a division: `Path` overloads it so that it means "inside of".

The cell prints the same path as each system writes it. If you write the path as a string with the
separator put in by hand, you are picking an operating system, and whoever marks the work may be on the
other one.

`parts` is the path already split, and that is what makes `name`, `stem`, `suffix` and `parent` come out
without touching a single string. `split("/")` and `[-1]` get you to the same place, right up until the
day somebody saves a file with a dot in its name.

## The backslash Python reads as something else
"""),

code("""
# FAILS ON PURPOSE. A path written as a string with backslashes.
bad = "data\\notes.txt"

print("What you typed:     data" + chr(92) + "notes.txt")
print("What Python stored:", repr(bad))
print("Characters:", len(bad), "and the backslash is gone:", chr(92) not in bad)
print()
print("Printed, it looks like this:")
print(bad)
print()
print("With Path there is nothing to escape:")
good = Path("data") / "notes.txt"
print(" ", repr(str(good)))
print()
print("And if you really do need the string, it goes with an r in front:")
print(" ", repr(r"data\\notes.txt"))
"""),

md("""
`\\n` is not two characters. It is a line break, and the `data` folder ended up stuck to an `otes.txt`
that does not exist.

It is error 02 on the slide and it happens to everybody once. The names that start with `n`, `t`, `r` and
`b` are the dangerous ones, because `\\n`, `\\t`, `\\r` and `\\b` are real escape sequences. The rest of
the letters produce a warning and survive, which is worse, because the error turns intermittent.

The two ways out: `Path` with the slash, or a raw string with an `r` in front. The first one also works on
both systems.

## `exists()` answers for what is there right now
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Asking first instead of trying.
path = Path("temp.txt")
path.write_text("important data", encoding="utf-8")

if path.exists():
    path.unlink()                 # somebody else deletes the file right here
    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        content = None
        print("The if said it was there and the read failed all the same.")
        print("  FileNotFoundError:", e.strerror)

print()
print("Content:", content)
print()
path.write_text("important data", encoding="utf-8")
try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    content = ""
print("Trying and catching:", repr(content))
"""),

md("""
The `if` said yes and the read failed anyway.

`exists()` answers for the state of the disk **at that instant**. Time passes between the question and the
read, and in that gap another program, another user or the system itself can delete, move or lock the
file. The cell does the deleting on purpose so the gap can be seen; in production chance does it, and that
is why the error shows up once every thousand runs.

It is the slide's comparison between asking first and trying and catching. **The second leaves no gap**:
it does not ask, it tries, and it deals with exactly the case where it failed.

`exists()` is still good for deciding, not for protecting. Asking whether a configuration file is there so
you can choose between reading it and using defaults is fine. Asking it to avoid a `FileNotFoundError` is
not.

## The relative path from the second midterm
"""),

code("""
# FAILS ON PURPOSE. script1.py, lines 9 to 12, with its path exactly as it is.
import os

# The tree the script expects gets rebuilt inside the working directory
target = Path("07 - Activities/Exams/2ndMidTerm")
target.mkdir(parents=True, exist_ok=True)
(target / "menu.txt").write_text("Main menu\\n1.- Option 1\\n0.- Exit\\n", encoding="utf-8")

filepath = "./07 - Activities/Exams/2ndMidTerm/"
filename = "menu.txt"


def print_menu(menu: list) -> None:
    for item in menu:
        print(item)


def load_menu():
    with open(filepath + filename, "r") as file:
        return [line.strip() for line in file.readlines()]


START = Path.cwd()
print("Current directory:", START.name)
print_menu(load_menu())

print()
try:
    os.chdir(target)
    print("Now the current directory is:", Path.cwd().name)
    load_menu()
except FileNotFoundError as e:
    print("  FileNotFoundError:", e.filename)
finally:
    os.chdir(START)

print()
print("Back in", Path.cwd().name)
"""),

md("""
The same file, the same script, two directories, and in the second one it cannot find it.

A relative path is resolved against the **process's current directory**, not against the `.py` file that
wrote it. Changing folder before running the script changes which file the path points at, and that is not
visible from reading the code.

The three scripts from the second midterm all carry this same line. They run if whoever executes them is
standing in `docs/en/courses/python-course` and they die from their own folder.

The one-line fix, for a script that wants its data next to it:

```python
HERE = Path(__file__).resolve().parent
path = HERE / "menu.txt"
```

`__file__` is the path of the file being executed, so the path stops depending on where whoever ran it was
standing. In a notebook `__file__` does not exist, and there the current directory is the right reference
because it is the only one there is.

**And while we are here: `filepath + filename` only works because somebody remembered the trailing
slash.** Without it the string runs together and the file becomes `2ndMidTermmenu.txt`. With `Path`'s `/`
there is nothing to remember.
"""),

md("""
---
# Block 2 · Opening, processing and closing

An open file is a borrowed resource. Everything borrowed gets returned, and it is better if it returns
itself.
"""),

code("""
path = Path("grades.txt")

# By hand, with the protection it needs to be correct
handle = None
try:
    handle = open(path, "w", encoding="utf-8")
    handle.write("Ana,9.2\\n")
finally:
    if handle is not None:
        handle.close()

print("By hand:", repr(path.read_text(encoding="utf-8")))

# With with, the same thing
with open(path, "a", encoding="utf-8") as handle:
    handle.write("Luis,7.8\\n")

print("With with:", repr(path.read_text(encoding="utf-8")))
print()
print("Did the with close it?", handle.closed)
print("And it stays closed even when something raises inside:")

try:
    with open(path, encoding="utf-8") as f:
        raise ValueError("something went wrong halfway through the read")
except ValueError as e:
    print("  ValueError:", e)
print("  Did f end up closed?", f.closed)
"""),

md("""
The first two halves do the same thing. The difference is six lines against two, and that the first one
has to be remembered in full.

Look at the `handle = None` up there. It is the fix for week 11's cell that fell over with a `NameError`:
without that line, if `open` fails, the `finally` touches a variable that does not exist.

The third part is the whole argument. The `with` block closes the file **on the way out of the block,
error or no error**, and it does it before the exception carries on upwards. That is what a well-written
`finally` achieves, and `with` achieves it without writing one.

## What happens when nobody closes
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A hundred rows written and an empty file.
path = Path("report.txt")
ROWS = [f"student-{i:03d}" for i in range(1, 101)]

LOG = []          # the program keeps the open file to go on using it


def write_report(rows):
    handle = open(path, "w", encoding="utf-8")
    LOG.append(handle)
    for number, row in enumerate(rows, start=1):
        handle.write(f"{number:>4}  {row}\\n")
    # handle.close() is missing


write_report(ROWS)

print("Rows the program wrote:", len(ROWS))
print("Bytes on disk right now:", path.stat().st_size)
print("Is the file still open?", not LOG[0].closed)
print()
print("No exception. The program finished cleanly.")
print()

LOG[0].close()
print("After closing it by hand:", path.stat().st_size, "bytes")
print("First row:", repr(path.read_text(encoding="utf-8").splitlines()[0]))
"""),

md("""
A hundred rows written, zero bytes on disk, and not one warning.

Writing does not send anything to disk straight away. What it does is fill a **buffer** in memory, and
that buffer empties when it fills up or when somebody closes the file. Closing is what makes what was
written exist.

The `LOG.append(handle)` in the cell is not decoration: it is what a real program does when it keeps the
open file in an attribute, in a list or in a dictionary so it can go on writing to it. As long as
something points at the file, nobody closes it.

## When the slip costs nothing
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The same mistake, and this time it works.
path = Path("luck.txt")


def write_without_storing(rows):
    handle = open(path, "w", encoding="utf-8")
    for number, row in enumerate(rows, start=1):
        handle.write(f"{number:>4}  {row}\\n")
    # handle.close() is missing, same as above


write_without_storing(ROWS)

print("Bytes on disk:", path.stat().st_size, "<- this time it did get written")
print()
print("The difference from the cell above is a single line:")
print("  there the file was kept in a list and here it is not.")
print()
print("When the function ends nobody points at the file, so CPython destroys it")
print("at that instant and destroying it closes it. The mistake is still written.")
print()

with open(path, "w", encoding="utf-8") as handle:
    for number, row in enumerate(ROWS, start=1):
        handle.write(f"{number:>4}  {row}\\n")

print("With with:")
print("  Bytes on disk:", path.stat().st_size)
print("  Did it close?", handle.closed)
"""),

md("""
The same slip, and this time the file came out complete.

CPython counts how many names point at each object and destroys it as soon as the count reaches zero. When
the function ends, the local variable disappears, nobody else points at the file, and destroying it closes
it. The slip cost something in the previous cell and nothing here, and the only difference is that there
somebody kept the reference.

That is the worst thing that can happen to a bug: **that it almost always works**. It turns up when the
file gets kept in an attribute, when the program stays alive inside a server, when the buffer filled up
halfway, or when the interpreter is not CPython, because that immediate destruction is not part of the
language.

It is error 01 on the slide. **The `with` closes, and closing empties the buffer.** That is the whole
chain, and it does not depend on luck.

## The five open modes
"""),

code("""
summary = []

Path("m.txt").write_text("original", encoding="utf-8")

# r: reads and touches nothing
with open("m.txt", encoding="utf-8") as f:
    summary.append(("r", "was there", repr(f.read()), Path("m.txt").stat().st_size))

# a: keeps it and adds at the end
with open("m.txt", "a", encoding="utf-8") as f:
    f.write("+added")
summary.append(("a", "was there", repr(Path("m.txt").read_text(encoding="utf-8")),
                Path("m.txt").stat().st_size))

# w: empties it on opening
f = open("m.txt", "w", encoding="utf-8")
summary.append(("w", "was there", "(just opened, nothing written)",
                Path("m.txt").stat().st_size))
f.close()

# x: only if it is not there
Path("new.txt").unlink(missing_ok=True)
with open("new.txt", "x", encoding="utf-8") as f:
    f.write("created with x")
try:
    open("new.txt", "x", encoding="utf-8")
except FileExistsError as e:
    summary.append(("x", "already there", type(e).__name__, 0))

# r on something that is not there
try:
    open("ghost.txt", encoding="utf-8")
except FileNotFoundError as e:
    summary.append(("r", "not there", type(e).__name__, 0))

print(f"{'mode':<6}{'the file':<16}{'what happened':<40}{'bytes'}")
for mode, state, what, bytes_ in summary:
    print(f"{mode:<6}{state:<16}{what:<40}{bytes_}")
"""),

md("""
The slide's table, measured.

The row to memorise is the third one: **`w` leaves the file at zero bytes the moment it is opened**,
before a single character gets written. If the program crashes between the `open` and the first `write`,
the file that was there is gone and the new one was never written.

`x` is the insurance against that: it creates the file if it is not there and raises `FileExistsError` if
it already was. When a program should never overwrite a previous file, `x` says so in one letter.

## Predict before you run

```python
path = Path("grades.txt")

with open(path, "w") as f:
    f.write("first")

with open(path, "w") as f:
    f.write("second")

print(path.read_text())
```

- **A.** `firstsecond`
- **B.** `second`, because `w` empties the file on opening.
- **C.** `first`, because the file already existed.
- **D.** `FileExistsError` on the second open.
"""),

code("""
path = Path("prediction.txt")

with open(path, "w", encoding="utf-8") as f:
    print("  after opening in w:", path.stat().st_size, "bytes")
    f.write("first")
print("  after closing:      ", path.stat().st_size, "bytes ->",
      repr(path.read_text(encoding="utf-8")))

with open(path, "w", encoding="utf-8") as f:
    print("  after opening in w again:", path.stat().st_size, "bytes <- already empty")
    f.write("second")

print()
print("Result:", repr(path.read_text(encoding="utf-8")))
print()
with open(path, "a", encoding="utf-8") as f:
    f.write("+third")
print("With mode a:", repr(path.read_text(encoding="utf-8")))
"""),

md("""
The answer is **B**.

The second line of the output is the proof: on opening in `w` the second time, the file already had zero
bytes and nothing had been written yet. **The emptying happens on opening, not on writing.**

To keep what was there, the mode is `a`.

## The encoding nobody wrote down
"""),

code("""
# FAILS ON PURPOSE. A file written with one encoding and read with another.
import locale

path = Path("accents.txt")
path.write_bytes("niño, año, señor".encode("latin-1"))

print("Bytes on disk:", path.read_bytes())
print()

try:
    print(path.read_text(encoding="utf-8"))
except UnicodeDecodeError as e:
    print("Read as utf-8:", type(e).__name__)
    print("  ", e.reason, "at position", e.start)

print()
print("Read as latin-1:", path.read_text(encoding="latin-1"))
print()
print("And with nothing said, Python uses the system's:")
print("  default encoding on this machine:", locale.getpreferredencoding(False))
print("  <- which is one thing on Windows, another on Linux and another on the marker's")
"""),

md("""
The same bytes, three reads, two results and one error.

A text file on disk is a row of bytes. The **encoding** is the table that says which letter each byte is,
and that table does not travel inside the file. If whoever writes and whoever reads do not use the same
one, the accents come out broken or the read blows up.

It is error 04 on the slide. `open` without `encoding` uses the system's, which is the one the last line
prints, and it is different between Windows and Linux. That is why the file reads fine on your machine and
with broken accents on the next one.

**Rule:** `encoding="utf-8"` on every `open` and on every `read_text` and `write_text`. No exceptions and
no thinking about it.

## Loading everything against walking it by lines
"""),

code("""
from sys import getsizeof

path = Path("big.txt")
with open(path, "w", encoding="utf-8") as f:
    for i in range(200_000):
        f.write(f"A{i:06d},student-{i},{(i % 100) / 10:.1f}\\n")

print("Size of the file:", f"{path.stat().st_size:,}", "bytes")
print()

with open(path, encoding="utf-8") as f:
    everything = f.read()
print("With read():        the string in memory weighs", f"{getsizeof(everything):,}", "bytes")

with open(path, encoding="utf-8") as f:
    longest = ""
    for line in f:
        if len(line) > len(longest):
            longest = line
print("Walking by lines:   the largest variable weighs",
      f"{getsizeof(longest):,}", "bytes")

print()
print("Both read the whole file. Only one holds it whole in memory.")
print("Rows:", everything.count(chr(10)))
"""),

md("""
The same file read two ways, and one of them never had more than one row in memory.

`read()` returns the whole file as one string. With six megabytes it fits; with six gigabytes it does not.
Walking the file with a `for` hands over **one line at a time**, and that costs the same in time and does
not grow in memory.

It is error 03 on the slide. `read()` is not wrong: it is wrong when you do not know how big the file is,
which is nearly always.

## Two claims from the repository, measured
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code030.py, lines 35 and 36.
import inspect
import time

print("What the file says:")
print('  "the read_text method is more efficient than the open method"')
print('  "because in the read_text method, the file is opened and closed automatically"')
print()
print("The code of read_text, exactly as it comes in this version of Python:")
try:
    print(inspect.getsource(Path.read_text))
except (OSError, TypeError):
    print("  (the source could not be read in this session)")

path = Path("measure.txt")
path.write_text("x" * 2_000_000, encoding="utf-8")

start = time.perf_counter()
for _ in range(20):
    path.read_text(encoding="utf-8")
with_read_text = time.perf_counter() - start

start = time.perf_counter()
for _ in range(20):
    with open(path, encoding="utf-8") as f:
        f.read()
with_open = time.perf_counter() - start

print(f"20 reads with read_text: {with_read_text:.4f} s")
print(f"20 reads with open:      {with_open:.4f} s")
print("Run the cell again: which one wins changes from one run to the next.")
"""),

md("""
`read_text` **calls `open` internally**. It is the `with` inside its own source code, printed above.

So it cannot be more efficient: it is the same thing with less to type. What the file describes as
efficiency is convenience, and convenience is a perfectly good reason to prefer it. It just goes by
another name.

The two times come out similar and which one wins changes between runs, because the difference left over
is measurement noise and not the code.

The technique is worth more here than the correction. **When a claim about performance can be measured, it
gets measured.** Two calls to `perf_counter` and one function from the standard library settled an
argument that had been sitting in a comment for years.

`read_text` is still the right way to read a small file whole, and `open` with `with` the right way to
walk it.

## The date that means two different things
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code030.py, line 20.
import os
from time import ctime

path = Path("date.txt")
path.write_text("first version", encoding="utf-8")
data = path.stat()

print("What the file says: 'st_ctime: time of creation'")
print()
print("st_atime (last access):       ", ctime(data.st_atime))
print("st_mtime (last modification): ", ctime(data.st_mtime))
print("st_ctime (per the system):    ", ctime(data.st_ctime))
print()
system = "Windows" if os.name == "nt" else "Linux or macOS"
print("This session runs on", system)
if os.name == "nt":
    print("  Here st_ctime really is the creation time, and the comment is right.")
else:
    print("  Here st_ctime is the time of the last metadata change, not the creation time.")
    print("  The comment in the file is false on this system.")
print()
print("The form that means the same thing everywhere:")
print("  st_birthtime, if it exists:", hasattr(data, "st_birthtime"))
"""),

md("""
`st_ctime` does not mean the same thing on every system.

On Windows it is the creation time, which is what the comment says. On Linux and on macOS it is the time
of the last **metadata** change: changing a file's permissions moves it, and the contents were never
touched. Colab runs on Linux, so the comment is false there.

The `c` is for *change*, not for *create*, and that letter has cost a lot of badly dated audit reports.

What to take from this is not the trivia: **a claim about the operating system gets checked on the
operating system where the program is going to run.** `os.name` is one line away.
"""),

md("""
---
# Block 3 · Text files and CSV

The simplest format that a person can still read, and the one Excel opens without asking any questions.
"""),

code("""
# Code31.py, lines 73 to 105: separators other than the comma
path = Path("data.txt")
path.write_text(
    "Username;Identifier;First name;Last name\\n"
    "booker12;9012;Rachel;Booker\\n"
    "grey07;2070;Laura;Grey\\n"
    "johnson81;4081;Craig;Johnson\\n", encoding="utf-8")

with open(path, 'r', encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(';')
        print(parts)

print()
with open(path, 'r', encoding="utf-8") as file:
    header = file.readline().strip().split(';')
    for line in file:
        parts = line.strip().split(';')
        row_dict = dict(zip(header, parts))
        print(row_dict)
"""),

md("""
`readline()` pulls out one line and **leaves the cursor where it left it**, so the `for` below starts on
the second one. That is the whole trick of reading the header separately.

`dict(zip(header, parts))` pairs each column name with its value. It is the same operation
`csv.DictReader` does, written by hand, and it works with any separator.

Look at the `.strip()`. Every line of a file carries its line break stuck to the end, and without removing
it the last field of every row finishes with an invisible `\\n` that ruins any comparison.

## The `zip` that eats a column
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A row with a field missing.
path = Path("incomplete.txt")
path.write_text(
    "Username;Identifier;First name;Last name\\n"
    "booker12;9012;Rachel;Booker\\n"
    "grey07;2070;Laura\\n"                       # this one has no surname
    "johnson81;4081;Craig;Johnson\\n", encoding="utf-8")

with open(path, encoding="utf-8") as file:
    header = file.readline().strip().split(';')
    rows = [dict(zip(header, l.strip().split(';'))) for l in file]

for r in rows:
    print(r)

print()
print("Fields per row:", [len(r) for r in rows])
print("Do they all have the four columns?", all(len(r) == len(header) for r in rows))
print()
for number, r in enumerate(rows, start=2):
    missing = [c for c in header if c not in r]
    if missing:
        print(f"  row {number}: missing {missing}")
"""),

md("""
The second row came out with three keys and the program carried on as if nothing had happened.

It is week 10's `zip`, now reading a file: it stops with the shortest list, and the shortest one was the
row. The resulting dictionary has no `Last name` key, so the `KeyError` is going to turn up much later, at
the point where somebody uses it.

With `strict=True` this would be a `ValueError` on the line that caused it. Without it, the check on the
last lines is what it takes: **counting each row's columns against the header**, which is the cheapest
validation there is for a tabular file.

## The `csv` module
"""),

code("""
import csv

path = Path("sample.csv")
path.write_text(
    "Username,Identifier,First name,Last name\\n"
    "booker12,9012,Rachel,Booker\\n"
    "grey07,2070,Laura,Grey\\n"
    "smith79,5079,Jamie,Smith\\n", encoding="utf-8")

# Code32.py, lines 44 to 54: with csv.reader each row is a list
with open(path, "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)
    header = data.pop(0)

print("Header:", header)
print("First row:", data[0])
print("The surname, by index:", data[0][3], "<- you have to know it is the 3")

print()
# Code32.py, lines 59 to 71: with DictReader each row is a dictionary
with open(path, "r", newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

print("First row:", rows[0])
print("The surname, by name:", rows[0]["Last name"])
print()
print("And if tomorrow somebody puts a column in the middle:")
path.write_text(
    "Username,Email,Identifier,First name,Last name\\n"
    "booker12,rb@up.edu.mx,9012,Rachel,Booker\\n", encoding="utf-8")
with open(path, newline="", encoding="utf-8") as file:
    row = next(csv.DictReader(file))
print("  by index [3] would give:", list(row.values())[3])
print("  by name still gives:", row["Last name"])
"""),

md("""
Both read the same file. The difference shows up the day somebody adds a column.

`csv.reader` hands over lists, and the code that uses them has to know the surname is index 3. Putting a
column in the middle shifts every index along and the program carries on running with the data moved
around.

`csv.DictReader` takes the first row as the header and hands over dictionaries. The surname is asked for
by its name and the new column does nothing to it.

**Rule:** `DictReader` unless you have a reason for the opposite.

## The third script's `split(",")`
"""),

code("""
# FAILS ON PURPOSE. script3.py, line 25, with a title that carries a comma.
path = Path("videogames.csv")
path.write_text(
    "The Legend of Zelda: Breath of the Wild,2017,Action-Adventure,Nintendo Switch\\n"
    "Super Mario Wonder,2023,Platformer,Nintendo Switch\\n"
    "God of War,2018,Action,PlayStation 4\\n", encoding="utf-8")


class Videogame:
    def __init__(self, title, year, genre, platform):
        self.title = title
        self.year = year
        self.genre = genre
        self.platform = platform

    def print_info(self):
        print(f"{self.title}, ({self.year}) - {self.genre} - {self.platform}")


def load(path):
    games = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            title, year, genre, platform = line.strip().split(",")
            games.append(Videogame(title, year, genre, platform))
    return games


for game in load(path):
    game.print_info()

print()
print("Now with a title that carries a comma, which is legal in a CSV:")
with open(path, "a", encoding="utf-8") as f:
    f.write('"Crash Bandicoot: N. Sane Trilogy, Remastered",2017,Platformer,PS4\\n')

try:
    load(path)
except ValueError as e:
    print("  ValueError:", e)
"""),

md("""
`too many values to unpack (expected 4, got 5)`, and the file was written correctly.

A CSV allows commas inside a field as long as the field is quoted. `split(",")` knows nothing about
quotes: it splits on every comma, including the ones that were inside the title.

The eight titles in `videogames.csv` carry no commas, so `script3.py` works today. What it takes to break
it is one more game.

That is the pattern of the whole session: **code that works with today's data is not the same thing as
code that works.** The `csv` module does know about quotes, and it is two lines.
"""),

code("""
import csv
import io

raw = '"Crash Bandicoot: N. Sane Trilogy, Remastered",2017,Platformer,PS4'

print("With split(','):", raw.split(","))
print("With csv.reader:", next(csv.reader(io.StringIO(raw))))
print()

path = Path("videogames.csv")
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

print("The four rows, split properly:")
for row in rows:
    print(f"  {len(row)} fields  {row[0]}")
print()
print("All four with four fields?", all(len(r) == 4 for r in rows))
"""),

md("""
Four fields in all four rows, including the one with the comma inside.

`csv.reader` knows how to read the quotes, knows that a double quote inside a quoted field is written
`""`, and knows that a line break inside quotes does not end the row. That is what separates a format from
a convention.

## Writing a CSV, and the `newline` it asks for
"""),

code("""
import csv

rows = [{"name": "Ana", "subject": "COM102", "grade": 9.1},
        {"name": "Luis", "subject": "COM102", "grade": 6.4},
        {"name": "Sofía", "subject": "COM101", "grade": 8.0}]

path = Path("report.csv")
with open(path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "subject", "grade"])
    writer.writeheader()
    writer.writerows(rows)

print(path.read_text(encoding="utf-8"))
print("The bytes left on disk:")
print(" ", path.read_bytes())

print()
with open(path, newline="", encoding="utf-8") as f:
    read_back = list(csv.DictReader(f))

print("Read back:", len(read_back))
print("The first one:", read_back[0])
print("Did the grade come back as a number?", type(read_back[0]["grade"]).__name__)
"""),

md("""
Three rows written and three read, and the grade came back as a string.

That last part is what surprises people most about CSV and it is its nature: **a CSV has no types**.
Everything that comes out of a text file is text, and converting to a number is the reader's job.
`DictWriter` wrote `9.1`; `DictReader` returned `'9.1'`.

Look at the raw bytes too. The `csv` module finishes every row with `\\r\\n`, which is what the standard
says, and that is why it asks for `newline=""` on opening.

## Why `newline=""` is not optional
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Opening a CSV for writing without newline="".
import csv
import os

rows = [["name", "grade"], ["Ana", "9.1"], ["Luis", "6.4"]]

with open("with.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

with open("without.csv", "w", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

print("This system is", "Windows" if os.name == "nt" else "Linux or macOS")
print("  with newline='':   ", Path("with.csv").read_bytes())
print("  without newline='':", Path("without.csv").read_bytes())
print()
print("Windows text mode translates every \\\\n into \\\\r\\\\n when writing.")
print("The csv module already wrote \\\\r\\\\n, so the translation leaves it like this:")
what_csv_writes = "name,grade\\r\\n"
print("  ", repr(what_csv_writes.replace("\\n", os.linesep)))
print()
print("On reading, every spare \\\\r shows up as a blank row between records.")
print("With newline='' there is no translation and the csv module writes what it meant to.")
"""),

md("""
On Linux both versions come out identical, and on Windows they do not.

Windows text mode translates every `\\n` into `\\r\\n` when writing. The `csv` module already wrote
`\\r\\n`, so the translation turns it into `\\r\\r\\n`, and whoever reads the file is going to see a blank
row between every two records.

If this session is running on Linux, the output above does not show the problem and you still have to
write `newline=""`, because the homework is going to be opened on somebody else's machine. It is the same
argument as the `encoding`: **a program's correctness is not measured on the machine where it was
written.**
"""),

md("""
---
## Four errors from this session

**Opening without `with`.** What gets written stays in the buffer and never reaches the disk. A hundred
rows and zero bytes, without a single exception.

**Paths with hand-typed slashes.** `"data\\notes.txt"` carries a hidden line break, and a relative path
depends on the directory somebody ran the program from.

**`read()` on a large file.** It loads everything into memory at once. Walking line by line costs the same
and always fits.

**Forgetting the `encoding`.** The file reads fine on your machine and with broken accents on the
marker's, and sometimes it does not read at all.
"""),

md("""
---
# Exercises

This week's lab is a report that comes out of a CSV and ends up in a text file. The exercises build
towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The parts of a path

Build a three-level path with `Path` and the slash. Print `name`, `stem`, `suffix`, `parent`, `parts` and
`exists`.

Then print the same path with `PureWindowsPath` and with `PurePosixPath` and explain in a comment why they
look different.

### Exercise 2 · The backslash

Write a path as a string with backslashes and a name starting with `n`. Print its `repr` and its length,
and show that the backslash is gone.

Write it the other two correct ways.

### Exercise 3 · With `with` and without it

Write fifty rows to a file without closing it and print the size on disk. Do it again with `with`.

Explain in a comment where the data was in the first case.

### Exercise 4 · The five modes

Write a program that tries `r`, `w`, `a` and `x` on a file that exists and on one that does not, catching
the exceptions. Print a table with what happened in each case.

### Exercise 5 · The encoding

Write a file with `encoding="latin-1"` and a word with an ñ in it. Read it with `utf-8` and catch the
`UnicodeDecodeError`. Read it with `latin-1` and check it comes out right.

Print your system's default encoding.

### Exercise 6 · Line by line

Generate a file of a hundred thousand rows. Find the longest row two ways: loading everything with
`read()` and walking it with a `for`.

Compare the size of the largest variable in each version with `getsizeof`.

### Exercise 7 · The CSV that defends itself

Write a CSV with one row missing a column and another with a comma inside a quoted field. Read it with
`DictReader` and print, for each row, how many fields it brought and which ones are missing.

### Exercise 8 · There and back

Write a list of dictionaries to a CSV with `DictWriter` and read it back with `DictReader`. Check that the
number of rows matches and convert the numeric column to `float`.

Explain in a comment why that conversion is needed.

### Exercise 9 · The lab

You are handed a CSV with a hundred grades and the columns `student_id`, `subject` and `grade`. Write a
program that reads it, works out the average per subject and saves a report into a new text file.

Constraints: every access goes through `with`, every path through `Path` and every open with an
`encoding`.

The criterion is that the program finishes cleanly even when the CSV is empty or missing a column.
"""),

md("""
---
## Three things to take away

**`Path` builds routes that work anywhere.** Joining with the slash sidesteps the separator problem, the
hidden escape character and the trailing slash somebody forgot while concatenating strings.

**The `with` closes even on a crash.** Opening by hand forces you to write a `finally`, and that `finally`
is the one people forget. Closing is what empties the buffer, and without it what was written does not
exist.

**Mode `w` wipes on opening.** Not on writing. The file is empty the instant it opens, even if the program
crashes before the first `write`.

Week 13 closes the unit with the files you cannot open in an editor: raw bytes, a zip treated as a folder,
and the way to jump to the record you want without reading the ones before it. This week the cursor moved
on its own, one row at a time; next week you move it by hand.
"""),

md("""
---
# Solutions

### Exercise 1

```python
from pathlib import Path, PureWindowsPath, PurePosixPath

path = Path("data") / "2026" / "students.csv"

for attribute in ["name", "stem", "suffix", "parent", "parts"]:
    print(f"{attribute:<10}{getattr(path, attribute)}")
print("exists   ", path.exists())

print(PureWindowsPath(path))
print(PurePosixPath(path))

# They look different because each system uses a different separator between
# folders. Path picks the one from the system it runs on; the two Pure classes
# are for writing another system's without depending on where you are.
```

### Exercise 2

```python
bad = "data\\notes.txt"
print(repr(bad), len(bad))
print("Is the backslash still there?", "\\\\" in bad)

print(repr(str(Path("data") / "notes.txt")))
print(repr(r"data\\notes.txt"))
```

### Exercise 3

```python
from pathlib import Path

path = Path("not_closed.txt")
f = open(path, "w", encoding="utf-8")
for i in range(50):
    f.write(f"row {i}\\n")
print("Not closed:", path.stat().st_size, "bytes")

with open(path, "w", encoding="utf-8") as g:
    for i in range(50):
        g.write(f"row {i}\\n")
print("With with: ", path.stat().st_size, "bytes")

# In the first case the data was in the write buffer, in memory.
# The file exists and stays empty until somebody closes it.
```

### Exercise 4

```python
from pathlib import Path

Path("exists.txt").write_text("hello", encoding="utf-8")
Path("missing.txt").unlink(missing_ok=True)

for mode in ["r", "w", "a", "x"]:
    for name in ["exists.txt", "missing.txt"]:
        try:
            with open(name, mode, encoding="utf-8"):
                result = "opened"
        except Exception as e:
            result = type(e).__name__
        print(f"{mode:<4}{name:<16}{result}")
        Path("missing.txt").unlink(missing_ok=True)
```

### Exercise 5

```python
import locale
from pathlib import Path

path = Path("tilde.txt")
path.write_text("mañana", encoding="latin-1")

try:
    print(path.read_text(encoding="utf-8"))
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e.reason)

print(path.read_text(encoding="latin-1"))
print("Default encoding:", locale.getpreferredencoding(False))
```

### Exercise 6

```python
from pathlib import Path
from sys import getsizeof

path = Path("hundred_thousand.txt")
with open(path, "w", encoding="utf-8") as f:
    for i in range(100_000):
        f.write(f"{'x' * (i % 60 + 1)}\\n")

with open(path, encoding="utf-8") as f:
    everything = f.read()
longest_a = max(everything.splitlines(), key=len)

with open(path, encoding="utf-8") as f:
    longest_b = ""
    for line in f:
        if len(line) > len(longest_b):
            longest_b = line

print("The same:", longest_a == longest_b.strip())
print("read(): largest variable", f"{getsizeof(everything):,}", "bytes")
print("for:    largest variable", f"{getsizeof(longest_b):,}", "bytes")
```

### Exercise 7

```python
import csv
from pathlib import Path

path = Path("defensive.csv")
path.write_text(
    'student_id,name,subject\\n'
    'A001,Ana Robles,COM102\\n'
    'A002,Luis Ferrer\\n'
    '"A003, provisional",Sofía Ines,COM101\\n', encoding="utf-8")

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames
    for number, row in enumerate(reader, start=2):
        missing = [c for c in columns if row.get(c) is None]
        print(f"row {number}: {len(row)} fields",
              f"missing {missing}" if missing else "complete")
```

### Exercise 8

```python
import csv
from pathlib import Path

rows = [{"student_id": "A001", "grade": 9.1},
        {"student_id": "A002", "grade": 6.4}]

path = Path("round_trip.csv")
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["student_id", "grade"])
    w.writeheader()
    w.writerows(rows)

with open(path, newline="", encoding="utf-8") as f:
    read_back = list(csv.DictReader(f))

print("Rows:", len(read_back) == len(rows))
print("Type on reading:", type(read_back[0]["grade"]).__name__)
converted = [{**r, "grade": float(r["grade"])} for r in read_back]
print("After converting:", type(converted[0]["grade"]).__name__)

# It is needed because a CSV is a text file and does not store types. Everything
# that comes out of it is str, including the column that was written as a float.
```

### Exercise 9

```python
import csv
from pathlib import Path

COLUMNS = ["student_id", "subject", "grade"]


def read_entries(path):
    \"\"\"Input boundary: returns clean rows and a list of problems.\"\"\"
    good, problems = [], []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                return [], ["the file is empty"]
            missing = [c for c in COLUMNS if c not in reader.fieldnames]
            if missing:
                return [], [f"missing columns: {missing}"]
            for number, row in enumerate(reader, start=2):
                try:
                    good.append({"student_id": row["student_id"],
                                 "subject": row["subject"],
                                 "grade": float(row["grade"])})
                except (TypeError, ValueError):
                    problems.append(f"row {number}: grade "
                                    f"{row.get('grade')!r} is not a number")
    except FileNotFoundError:
        problems.append(f"{path} is not there")
    return good, problems


def averages_by_subject(rows):
    grouped = {}
    for r in rows:
        grouped.setdefault(r["subject"], []).append(r["grade"])
    return {s: sum(g) / len(g) for s, g in sorted(grouped.items())}


def report_lines(averages, problems, total):
    lines = [f"Entries read: {total}", ""]
    for subject, average in averages.items():
        lines.append(f"{subject}: {average:.2f}")
    if problems:
        lines += ["", "Problems:"] + [f"  {p}" for p in problems]
    return lines


def save(lines, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\\n".join(lines) + "\\n")


if __name__ == "__main__":
    source = Path("entries.csv")
    source.write_text(
        "student_id,subject,grade\\n"
        "A001,COM102,9.1\\n"
        "A002,COM102,6.4\\n"
        "A003,COM101,8.0\\n"
        "A004,COM101,seven\\n", encoding="utf-8")

    rows, problems = read_entries(source)
    save(report_lines(averages_by_subject(rows), problems, len(rows)),
         Path("final_report.txt"))
    print(Path("final_report.txt").read_text(encoding="utf-8"))

    rows, problems = read_entries(Path("missing.csv"))
    print("With a file that is not there:", problems)
```

Three decisions worth defending when you hand this in.

**`read_entries` returns two lists and prints nothing.** The good rows and the problems come out together,
so the report can say both things and the function can be tested with a CSV written by hand.

**The empty file and the missing column are dealt with before the loop.** `fieldnames is None` is the sign
that the file had no header at all, and checking the columns once avoids repeating the same review a
hundred times.

**Every disk access goes through `with` and carries an `encoding`.** Block 2's two rules, no exceptions,
including writing the report.
"""),

]

write(OUT / "en" / "w12.ipynb", en)
print("wrote", OUT / "en" / "w12.ipynb")
