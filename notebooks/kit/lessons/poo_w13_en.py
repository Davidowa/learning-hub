"""notebooks/programacion-orientada-a-objetos/en/w13.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w13.en.yaml
Source code:  docs/en/courses/python-course/03 - Paths and Files/7th Module/Code33.py
                  (json.dumps, json.loads, the file pixar_movies.json)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code34.py
                  (zipfile: write, namelist, extractall)

Neither of the two is run out of the repository. Code34.py leaves files.zip and
an extracted_files/ folder inside docs/, and Code33.py overwrites
pixar_movies.json. The notebook reproduces their code in the session's working
directory, which on Colab is /content.

Measured things from the repository that the notebook teaches as a trap, without
correcting them:

  Code34.py line 56 opens the zip with "with ZipFile(...) as zip", which covers
  up Python's zip function for everything that comes after. Its own annotation
  on the deck warns about it. Measured: calling zip(a, b) after that line gives
  TypeError: 'ZipFile' object is not callable.

  Code34.py line 15 stores the file with its full relative path as the member
  name, so extractall rebuilds the folder tree inside extracted_files/. It is
  not an error, but it surprises people and is worth measuring.

  Code33.py line 56 writes the JSON with write_text and no encoding, so it uses
  the system's. On top of that json.dumps escapes non-ASCII characters by
  default, and that is why the repository's file gets away with it: there is not
  a single accent inside. The moment a movie brings one, the file depends on the
  machine.

  Code33.py line 12 says "JSON usually contains a collection of key-value pairs,
  in other words, a dictionary" and its line 13 announces "Lets create a
  dictionary of Pixar movies". What it creates is a list of dictionaries, which
  is another thing, and it is the one the rest of the file uses.

Week 12 closed pointing here: there the cursor moved on its own, one line at a
time, and nobody had to think about it. Here it gets moved by hand.

Weeks 14 and 15 carry no notebook: they are PyQt6 and a window needs a screen.
This notebook's closing says so, and the thread is picked up in week 16.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 13
## Topic 5 · Files

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

The files no editor can open, the way to jump straight to the record you want without reading the ones
before it, and the close of the unit.

Last week the cursor moved on its own, one line at a time, and nobody had to think about it. This week it
gets moved by hand, and for that you have to know exactly where it is.

By the end you will be able to:

1. Choose between text mode and binary mode by what is inside the file, not by the extension attached to
   its name.
2. Read and write bytes with `rb` and `wb`, knowing that `read` counts bytes rather than characters.
3. Work out where record n starts when every record is the same size.
4. Say what breaks when records vary in size, and why access falls back to sequential.
5. Sit the second midterm with units 4 and 5 practised by writing files.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Nine fail on purpose and carry a comment saying so.

Six of the nine **raise no exception at all**. Two of those six read a binary file without complaining and
hand back one byte fewer than the file had, which is the exact way an image gets corrupted without anyone
noticing.

Everything this notebook writes stays in the session's working directory. It touches nothing in the
repository.
"""),

md("""
---
# Block 1 · Binary files

Every file is a row of bytes. Text mode puts a layer on top that translates those bytes into letters with
an encoding and tidies the line breaks on the way past.

Binary mode removes that layer and hands over the bytes exactly as they came off the disk.
"""),

code("""
from pathlib import Path

# A real PNG image always starts with these eight bytes
PNG_HEADER = bytes([0x89]) + b"PNG" + b"\\r\\n" + bytes([0x1A]) + b"\\n"
path = Path("logo.png")
path.write_bytes(PNG_HEADER + b"\\x00\\x00\\x00\\rIHDR" + bytes(range(24)))

with open(path, "rb") as handle:
    header = handle.read(8)

print("The first eight bytes:", header)
print("How many it read:", len(header), "bytes")
print("Type:", type(header).__name__)
print()
print("Byte by byte, in decimal and in hexadecimal:")
for i, b in enumerate(header):
    letter = chr(b) if 32 <= b < 127 else "."
    print(f"  {i}  {b:>3}  0x{b:02X}  {letter}")

print()
print("Is it a PNG?", header == PNG_HEADER)
print("File size:", path.stat().st_size, "bytes")
"""),

md("""
`read(8)` asked for eight **bytes**, not eight characters. In binary there are no characters.

What comes back is a `bytes` object, which looks like a string and is not one: it is indexed with whole
numbers from 0 to 255 and has no idea which letter each one stands for.

Those eight bytes are a PNG's signature and they are there on purpose. The third, fourth and fifth are the
letters `PNG`; the first is `0x89`, a byte that cannot appear in an ASCII text file, and the `\\r\\n` in
the middle exists to catch exactly the error in the next two cells.

## Opening a binary in text mode
"""),

code("""
# FAILS ON PURPOSE. A PNG read as though it were text.
path = Path("logo.png")

try:
    contents = path.read_text(encoding="utf-8")
except UnicodeDecodeError as e:
    print("UnicodeDecodeError")
    print("  reason:  ", e.reason)
    print("  position:", e.start)
    print("  the byte:", hex(e.object[e.start]))

print()
print("The byte 0x89 cannot start a utf-8 character, and that is why it blows up")
print("before it manages to read anything.")
"""),

md("""
`invalid start byte` at position 0.

`utf-8` has rules about which bytes may start a character, and `0x89` is not one of them. The read stops
at the file's very first byte.

This is the good case. **The read blows up before breaking anything**, and the message says where. The bad
case is the next cell.

## When text mode does not complain
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The same PNG, with an encoding that accepts everything.
path = Path("logo.png")

raw = path.read_bytes()
as_text = path.read_text(encoding="latin-1")

print("Bytes on the disk:     ", len(raw))
print("Characters it returned:", len(as_text))
print("Difference:", len(raw) - len(as_text), "byte")
print()
print("The first eight, side by side:")
print("  from the disk:", list(raw[:8]))
print("  from the text:", [ord(c) for c in as_text[:8]])
print()
print("The 13 is gone. It is the \\\\r of the signature's \\\\r\\\\n:")
print("  text mode turns \\\\r\\\\n into \\\\n and eats a byte")
print()
back = as_text.encode("latin-1")
Path("copy.png").write_bytes(back)
print("If you save that as an image:")
print("  same size?", Path("copy.png").stat().st_size == path.stat().st_size)
print("  still a PNG?", back[:8] == raw[:8])
"""),

md("""
No error, one byte fewer, and an image that no longer opens.

`latin-1` assigns a letter to each of the 256 possible bytes, so it never fails to decode. That removes
the protection from the previous cell and lets the real problem show up: **text mode also translates the
line breaks**.

A `\\r\\n` inside a file becomes `\\n` when you read it in text mode, because Python normalises the line
endings of all three systems. In a text file that is what you want. Inside a PNG, a ZIP or an executable,
it is a byte deleted in the middle of the data.

It is exactly the risk the slide announces: *"or worse, reads rubbish quietly"*.

## The same damage, in four bytes
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A round trip through text mode.
Path("raw.bin").write_bytes(b"A\\r\\nB")

raw = Path("raw.bin").read_bytes()
text = Path("raw.bin").read_text(encoding="latin-1")

print("Written:     ", raw, f"({len(raw)} bytes)")
print("Read as text:", repr(text), f"({len(text)} characters)")
print()
print("Did the same bytes come back?", text.encode("latin-1") == raw)
print()
print("And in binary mode:")
print("  ", Path("raw.bin").read_bytes() == raw)
print()
print("This happens on Windows, on Linux and on macOS alike, because the change")
print("from \\\\r\\\\n to \\\\n is made by Python on reading, not by the operating system.")
"""),

md("""
Four bytes in, three characters out, and no exception.

It is the same mechanism as the previous cell in its smallest possible version. It is worth keeping in
mind because `\\r\\n` turns up everywhere: in the CSV files week 12 wrote, in network headers, and inside
any binary file by pure statistical accident.

**The rule is one line long: the mode is chosen by the contents of the file, not by its extension.** A
`.dat` with text inside is opened as text. A `.txt` that really carries bytes is opened as binary.

## The five differences, measured
"""),

code("""
Path("text.txt").write_text("Ana,9.2\\nLuis,7.8\\n", encoding="utf-8")

with open("text.txt", encoding="utf-8") as f:
    in_text = f.read()
with open("text.txt", "rb") as f:
    in_binary = f.read()

rows = [
    ("How it opens", 'open(path, encoding="utf-8")', 'open(path, "rb")'),
    ("What read returns", type(in_text).__name__, type(in_binary).__name__),
    ("Length of what it read", str(len(in_text)), str(len(in_binary))),
    ("What each element is", repr(in_text[0]), repr(in_binary[0])),
    ("Encoding", "required in practice", "not applicable"),
]

print(f"{'Aspect':<24}{'Text mode':<30}{'Binary mode'}")
for aspect, text, binary in rows:
    print(f"{aspect:<24}{text:<30}{binary}")

print()
print("An element of bytes is a whole number:", in_binary[0], "which is the A")
print("An element of str is a character:", repr(in_text[0]))
print()
print("And to go from one to the other:")
print("  text -> bytes:", repr("Ana".encode("utf-8")))
print("  bytes -> text:", repr(b"Ana".decode("utf-8")))
"""),

md("""
The row that surprises most is the fourth. **Indexing a `bytes` object returns a whole number, not a
byte.**

`b"Ana"[0]` is `65`, not `b"A"`. Slicing it does return bytes: `b"Ana"[0:1]` is `b"A"`. That asymmetry is
where half the errors of anyone starting with binaries come from.

`encode` and `decode` are the bridge between the two worlds, and the two words say which way each one
goes: **encoding is text to bytes, decoding is bytes to text**.

## A binary handled as though it were a folder
"""),

code("""
# Code34.py, lines 8 to 16 and 56 to 64, in the working directory
from zipfile import ZipFile

folder = Path("data")
folder.mkdir(exist_ok=True)
(folder / "students.csv").write_text("student_id,grade\\nA001,9.2\\n", encoding="utf-8")
(folder / "subjects.csv").write_text("code,name\\nCOM102,OOP\\n", encoding="utf-8")
(folder / "notes.txt").write_text("scratch", encoding="utf-8")

with ZipFile("submission.zip", "w") as bundle:
    for item in folder.rglob("*.csv"):
        bundle.write(item)

print("Size of the zip:", Path("submission.zip").stat().st_size, "bytes")
print()
with ZipFile("submission.zip") as bundle:
    print("What it carries inside:", bundle.namelist())
    for info in bundle.infolist():
        print(f"  {info.filename:<22}{info.file_size:>4} bytes ->"
              f" {info.compress_size:>4} compressed")

print()
with ZipFile("submission.zip") as bundle:
    bundle.extractall("extracted")

print("What ended up on the disk:")
for p in sorted(Path("extracted").rglob("*")):
    print("  ", p)
"""),

md("""
A zip is a binary file and `zipfile` treats it as though it were a folder. You never have to touch a byte.

Look at `namelist()`. The names inside carry the **full relative path** they were added with, so
`extractall` rebuilds the folder tree. `Code34.py` stores
`03 - Paths and Files/7th Module/test.txt`, and extracting it recreates those two folders. If you want
only the name inside, you have to say so: `bundle.write(item, arcname=item.name)`.

`rglob` walks the subfolders too; `glob` stays on the top level and goes no further. And `notes.txt` did
not go into the zip because the pattern asked for `*.csv`.

## The variable that covered up a Python function
"""),

code("""
# FAILS ON PURPOSE. Code34.py, line 56, with its variable name exactly as it is.
from zipfile import ZipFile

names = ["Ana", "Luis", "Sofia"]
grades = [9.2, 7.8, 9.5]

print("Before:", list(zip(names, grades)))
print()

with ZipFile("submission.zip", "r") as zip:
    print(zip.namelist())

print()
try:
    list(zip(names, grades))
except TypeError as e:
    print("After:", type(e).__name__ + ":", e)

print()
del zip
print("Back again:", list(zip(names, grades)))
"""),

md("""
`'ZipFile' object is not callable`, and the line that failed had nothing to do with files.

`with ... as zip` assigns to `zip` like any other assignment, and that assignment **survives the block**.
From there on, `zip` in that module is the compressed file and not Python's function.

It is the same error as week 10's `sum`, and the deck's annotation spells it out: *"Do not call the
variable zip, because it covers up the zip function Python ships with"*. It hurts more here because `zip`
and `ZipFile` get used in the same kind of program.

In `Code34.py` nobody notices, because the file ends two lines later. In a real program the error shows up
wherever somebody wants to walk two lists in parallel.

## JSON: text that looks like a dictionary
"""),

code("""
# Code33.py, lines 15 to 63, with three movies instead of twenty-six
import json

pixar_movies = [
    {"id": 1, "title": "Toy Story", "year": 1995},
    {"id": 19, "title": "Coco", "year": 2017},
    {"id": 25, "title": "Turning Red", "year": 2022},
]

print("What the file calls 'a dictionary of Pixar movies' is of type:",
      type(pixar_movies).__name__)
print("And each element really is a:", type(pixar_movies[0]).__name__)
print()

json_string = json.dumps(pixar_movies)
print("As text:", json_string)
print("Type:", type(json_string).__name__)
print()

file_path = Path("pixar_movies.json")
file_path.write_text(json_string, encoding="utf-8")

data = file_path.read_text(encoding="utf-8")
read_pixar_movies = json.loads(data)

print("Back in Python:", type(read_pixar_movies).__name__,
      "with", len(read_pixar_movies), "elements")
print("Did it survive the whole trip?", read_pixar_movies == pixar_movies)
print("The year is still a number:", type(read_pixar_movies[0]["year"]).__name__)
"""),

md("""
The round trip came out intact, and the year came back as a number.

That is the big difference from last week's CSV. **A CSV has no types and a JSON does**: the format tells
numbers, strings, booleans, nulls, lists and objects apart, so `json.loads` returns the Python structures
that match without anyone converting anything.

`Code33.py` calls what it creates a dictionary, and what it creates is a **list of dictionaries**. The
distinction matters because the rest of the file walks it with a `for`, which is what you do with a list,
and because in week 16 that list becomes a table where each element is a row.

## The character above 127 that has not arrived yet
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code33.py, line 56: write_text with no encoding.
import json
import locale

with_a_dot = [{"id": 9, "title": "WALL·E", "year": 2008}]

escaped = json.dumps(with_a_dot)
print("json.dumps by default:", escaped)
print("  <- the middle dot came out as \\\\u00b7, so the file is pure ASCII")
print()
print("And that is why writing it with no encoding works on any machine:")
Path("escaped.json").write_text(escaped)
print("  bytes on disk:", Path("escaped.json").read_bytes())
print("  this machine's default encoding:",
      locale.getpreferredencoding(False))
print()

readable = json.dumps(with_a_dot, ensure_ascii=False)
print("With ensure_ascii=False:", readable)
Path("readable.json").write_text(readable, encoding="utf-8")
print("  bytes on disk:", Path("readable.json").read_bytes())
print()
print("Both versions load into the same object:",
      json.loads(escaped) == json.loads(readable))
"""),

md("""
`Code33.py` writes the JSON with no `encoding` and gets away with it by a hair.

`json.dumps` escapes anything that is not ASCII by default: the middle dot comes out as `\\u00b7`. The
resulting file only has bytes below 128, and those mean the same thing in every encoding there is, so
`write_text` with no `encoding` produces the same file on any machine.

The day somebody writes `ensure_ascii=False` so the file reads better, that protection disappears and the
file starts depending on the system's encoding. The correct version carries both: `ensure_ascii=False` so
it is readable, and `encoding="utf-8"` so it depends on nobody.

Not one of the twenty-six movies in the repository carries a character above 127. The studio spells the
ninth one with a middle dot and the repository spells it `WALL-E`, with a plain hyphen. That is the only
reason `Code33.py` works.
"""),

md("""
---
# Block 2 · Sequential and random access

Every open file has a cursor. Reading pushes it forward, and there is a way to put it wherever you want.
"""),

code("""
Path("records.bin").write_bytes(bytes(range(256)) * 2)

with open("records.bin", "rb") as f:
    print("On opening, the cursor is at:", f.tell())
    f.seek(64)
    print("After seek(64):             ", f.tell())
    data = f.read(32)
    print("After read(32):             ", f.tell())
    print("  and it read", len(data), "bytes:", data[:8], "...")
    f.seek(0)
    print("After seek(0):              ", f.tell())
    f.seek(-16, 2)
    print("After seek(-16, 2):         ", f.tell(), "<- 2 means 'from the end'")
    print("  the last 16 bytes:", f.read())
"""),

md("""
`tell()` returns the cursor's current position, counted in **bytes from the start**.

Reading pushes it: after `read(32)` the cursor moved exactly 32. `seek` puts it where you say without
reading anything on the way, and that is the whole difference between sequential access and random access.

The second argument of `seek` says where the counting starts: `0` from the beginning, which is the usual
one, `1` from the current position, and `2` from the end. `seek(-16, 2)` is how you read the tail of a
file without walking it.

## Predict before you run

```python
with open("data.bin", "wb") as f:
    f.write(b"ABCDEFGH")

with open("data.bin", "rb") as f:
    f.seek(3)
    print(f.read(2))
```

- **A.** `b'DE'`, because the cursor lands before the fourth letter.
- **B.** `b'CD'`, because `seek` starts counting at one.
- **C.** `b'ABCDEFGH'`, because `seek` does not affect what `read` reads.
- **D.** An error, `seek` does not work in binary mode.
"""),

code("""
with open("data.bin", "wb") as f:
    f.write(b"ABCDEFGH")

print("The file, with its positions:")
print("  position:", "".join(f"{i:>4}" for i in range(8)))
print("  byte:    ", "".join(f"{chr(b):>4}" for b in b"ABCDEFGH"))
print()

with open("data.bin", "rb") as f:
    print("Cursor on opening:", f.tell())
    f.seek(3)
    print("Cursor after seek:", f.tell())
    got = f.read(2)
    print("read(2) returned: ", got)
    print("Cursor after read:", f.tell())
"""),

md("""
The answer is **A**.

Positions count from zero, exactly like list indexes. Position 3 does not sit *on* the fourth letter: it
sits **just before** it, in the slot between the `C` and the `D`. `read(2)` takes that one and the next.

The table above says it better than any explanation: the position is the slot, not the box.

## Jumping to record n
"""),

code("""
import time

SIZE = 32
N = 200_000

with open("roll.bin", "wb") as f:
    for i in range(N):
        student_id = f"A{i:06d}".encode("ascii")
        name = f"student-{i}".encode("ascii")
        f.write(student_id.ljust(8) + name.ljust(24))

print("Records:", f"{N:,}", " file size:",
      f"{Path('roll.bin').stat().st_size:,}", "bytes")
print("Does it match N * SIZE?", Path("roll.bin").stat().st_size == N * SIZE)
print()

print(f"{'record':>10}{'with seek':>14}{'sequential':>14}{'the same?':>14}")
with open("roll.bin", "rb") as f:
    for wanted in [1_000, 50_000, 150_000]:
        start = time.perf_counter()
        f.seek(wanted * SIZE)
        with_seek = f.read(SIZE)
        seek_cost = time.perf_counter() - start

        start = time.perf_counter()
        f.seek(0)
        for _ in range(wanted):
            f.read(SIZE)
        sequential = f.read(SIZE)
        sequential_cost = time.perf_counter() - start

        print(f"{wanted:>10,}{seek_cost:>14.6f}{sequential_cost:>14.6f}"
              f"{str(with_seek == sequential):>14}")

print()
print("The seek column does not grow. The walking one multiplies with the record")
print("number, because it really is reading them all.")
"""),

md("""
The same record by both routes, and one of the two columns does not move.

The sum is the whole idea: **if every record is the same size, record `n` starts at `n * SIZE`**. `seek`
goes straight to that byte, so reading record one thousand costs the same as reading record one hundred
and fifty thousand. The sequential walk does not: every record before it really is read, and that is why
its column grows with the number you are after.

Look at the `ljust`. Each field is padded out to its fixed width, and that is why the sum works. That
padding is the price of random access: the file takes up more room than it needs, in exchange for the
position being something you can calculate.

## When records vary in size
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The same sum over records of varying length.
NAMES = ["Ana", "Luis", "Sofia", "Marco", "Paula Elena", "Ruben"]

with open("variable.bin", "wb") as f:
    for i, name in enumerate(NAMES):
        f.write(f"A{i:03d}{name}\\n".encode("utf-8"))

print("Contents:", Path("variable.bin").read_bytes())
print("Size:", Path("variable.bin").stat().st_size, "bytes")
print()

ASSUMED_SIZE = 10
for wanted in [0, 2, 4]:
    with open("variable.bin", "rb") as f:
        f.seek(wanted * ASSUMED_SIZE)
        print(f"  record {wanted} 'according to the sum':", f.read(ASSUMED_SIZE))

print()
print("What is really at each position:")
with open("variable.bin", "rb") as f:
    for i, line in enumerate(f):
        print(f"  record {i}: {line!r}")
"""),

md("""
Three jumps, three pieces of record cut in half, and no exception.

When every record is a different size, there is no multiplication that gives the position. The sum keeps
working, keeps returning bytes, and those bytes are rubbish: part of one student id and part of the name
after it.

It is error 02 on the slide. **Random access demands records of the same size**, and when there are none,
either you walk the file from the beginning or you keep an index on the side saying which byte each record
starts at. That second one is, in two sentences, what a database does, and it is where week 16 goes.

## The record shorter than the one before it
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Overwriting without padding out to the fixed size.
SIZE = 8

with open("fixed.bin", "wb") as f:
    for name in [b"ANA00000", b"LUIS0000", b"SOFIA000"]:
        f.write(name)

print("Before:", Path("fixed.bin").read_bytes())

with open("fixed.bin", "r+b") as f:
    f.seek(1 * SIZE)
    f.write(b"ED")                     # the new record is two long, not eight

print("After: ", Path("fixed.bin").read_bytes())
print()
with open("fixed.bin", "rb") as f:
    for i in range(3):
        f.seek(i * SIZE)
        print(f"  record {i}: {f.read(SIZE)}")

print()
print("With the padding it needed:")
with open("fixed.bin", "r+b") as f:
    f.seek(1 * SIZE)
    f.write(b"ED".ljust(SIZE, b"0"))

with open("fixed.bin", "rb") as f:
    for i in range(3):
        f.seek(i * SIZE)
        print(f"  record {i}: {f.read(SIZE)}")
"""),

md("""
The new record was two bytes long and the other six of the old one stayed where they were.

Writing in the middle of a file **overwrites** exactly the bytes you write and touches not one more. There
is no such thing as deleting a record: if the new one is shorter, whatever is left of the old one is still
on the disk, and the next `read(SIZE)` hands it back stuck on the end.

It is error 03 on the slide. The fix is `ljust` out to the fixed size, which is the same discipline as the
roll two cells ago.

Look at the `r+b` mode. `wb` would have emptied the file on opening, which is last week's error; `r+b`
opens for reading and writing **keeping** what was there, and it is the mode random access asks for.

## Jumping past the end
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. seek past the end of the file, and write.
with open("hole.bin", "wb") as f:
    f.write(b"START")
    print("Cursor after writing: ", f.tell())
    f.seek(20)
    print("Cursor after seek(20):", f.tell())
    f.write(b"END")

raw = Path("hole.bin").read_bytes()
print()
print("Bytes on disk:", raw)
print("Size:", len(raw))
print()
print("What sits between position 5 and position 20:", raw[5:20])
print("All zeros:", raw[5:20] == bytes(15))
print()
print("And read as text, those zeros are perfectly valid characters:")
print(" ", repr(raw.decode("latin-1")))
"""),

md("""
Fifteen zero bytes appeared in the middle of the file, and nobody said a word.

It is error 04 on the slide. `seek` checks nothing: it accepts any position, including the ones past the
end. Writing there forces the system to fill the gap, and it fills it with zeros.

That padding counts as content. The file is 23 bytes long, it reads without any trouble, and whoever
processes it afterwards is going to find fifteen null bytes nobody wrote. In a file of fixed records, that
is almost two ghost records.

**Before a calculated `seek`, the position is compared against the size of the file.** One line:
`if position > path.stat().st_size: ...`

## `seek` in text mode
"""),

code("""
# FAILS ON PURPOSE. A jump that lands in the middle of a letter.
path = Path("accents.txt")
path.write_text("naïve café", encoding="utf-8")

print("As text: ", path.read_text(encoding="utf-8"))
print("As bytes:", path.read_bytes())
print("Characters:", len(path.read_text(encoding='utf-8')),
      " bytes:", len(path.read_bytes()))
print("  <- the ï and the é take two bytes each")
print()

with open(path, encoding="utf-8") as f:
    f.seek(3)
    try:
        print("From position 3:", repr(f.read()))
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e.reason)
        print("  position 3 lands between the two bytes of the ï")

print()
with open(path, encoding="utf-8") as f:
    position = f.tell()
    f.read(3)
    saved = f.tell()
    f.seek(saved)
    print("With a position tell() returned:", repr(f.read()))
"""),

md("""
In text mode, positions are neither bytes nor characters. They are opaque values that only `tell()` knows
how to produce.

The cell teaches it with an `ï`: it takes two bytes in `utf-8`, so `seek(3)` lands between the two and the
decoder is left with no way to assemble the character.

It is error 01 on the slide. **In text mode, `seek` only accepts the positions `tell()` returned**, plus
the `0` at the start. Anything else is a gamble.

If you need to jump to a specific byte, the file is opened in binary and the piece you read is decoded by
hand. That is the technical reason files of fixed records are stored in binary and not in text.
"""),

md("""
---
# Block 3 · Second midterm

It closes units 4 and 5. Everything on it was practised in a lab, with a file actually landing on disk.

| Unit | What it covers |
|---|---|
| U4 | Parameters, modularity, recursion, collections, dynamic arrays and exception handling |
| U5 | Paths, open modes, text, CSV, binaries, and sequential and random access |
| Base | The modelling from units 1 to 3, since the exam asks for classes that read and write files |
| Out | Graphical interfaces and databases, which are assessed in the project and the final exam |

**How it is studied.** Every unit 5 question is answered by writing a file and reading it back. If you did
not practise it by running the code, you did not practise it.

The cell below is a short mock. Run the nine questions, it grades itself, and the ones you get wrong say
which week to go back to.
"""),

code("""
from pathlib import Path

QUESTIONS = []


def question(statement, week, got, expected):
    QUESTIONS.append((statement, week, got, expected))


# 1. The mutable default value (week 09)
def add(x, items=[]):
    items.append(x)
    return items


add("a")
question("A default list, after two calls", 9, len(add("b")), 2)

# 2. The alias (week 10)
a = [1, 2, 3]
b = a
b.append(4)
question("copy = list and then append", 10, len(a), 4)

# 3. Removing while walking (week 10)
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
question("Removing the even ones inside the for", 10, nums, [4, 8])

# 4. zip stops with the shortest (week 10)
question("zip of 5 and 3 elements", 10, len(list(zip(range(5), range(3)))), 3)

# 5. finally runs with a return waiting (week 11)
order = []


def read_value():
    try:
        return "value"
    finally:
        order.append("finally")


read_value()
question("Did finally run with a return waiting?", 11, order, ["finally"])


# 6. The order of the excepts (week 11)
def classify(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError:
        return "general"
    except FileNotFoundError:
        return "specific"


question("except OSError before FileNotFoundError", 11,
         classify("never_ever_exists.txt"), "general")

# 7. Mode w empties the file on opening (week 12)
p = Path("midterm.txt")
p.write_text("first", encoding="utf-8")
f = open(p, "w", encoding="utf-8")
question("Bytes after opening in w, before writing", 12, p.stat().st_size, 0)
f.close()

# 8. A CSV has no types (week 12)
import csv
p = Path("midterm.csv")
p.write_text("name,grade\\nAna,9.1\\n", encoding="utf-8")
with open(p, newline="", encoding="utf-8") as f:
    row = next(csv.DictReader(f))
question("Type of the grade column when read back", 12,
         type(row["grade"]).__name__, "str")

# 9. Positions start at zero (week 13)
Path("midterm.bin").write_bytes(b"ABCDEFGH")
with open("midterm.bin", "rb") as f:
    f.seek(3)
    got = f.read(2)
question("seek(3) and read(2) over ABCDEFGH", 13, got, b"DE")

matched = 0
print(f"{'#':<3}{'wk':<5}{'question':<42}{'result'}")
for i, (statement, week, got, expected) in enumerate(QUESTIONS, start=1):
    ok = got == expected
    matched += ok
    print(f"{i:<3}{week:<5}{statement:<42}{got!r}"
          f"{'' if ok else f'  <- {expected!r} was expected'}")

print()
print(f"Predictions that matched: {matched} of {len(QUESTIONS)}")
print("If any of them surprised you, the 'wk' column says which notebook to go back to.")
"""),

md("""
All nine are behaviours, not definitions, and all nine turn up on the exam as code you have to write.

Not one of them is answered by rereading a slide. They are answered by typing, which is what the cell just
did.

**What to review before the midterm:** the open modes, and what each one does when the file was already
there. It is one of the few things worth knowing by heart, because getting it wrong deletes the input
file.

**What is not worth memorising:** the methods on `Path`. They are one tab keypress away inside the editor,
and the exam is sat with the course repository open.
"""),

md("""
---
## Four errors from this session

**Mixing `seek` with text mode.** In text mode, `seek` only accepts the positions `tell` returned. Any
other one lands in the middle of a letter.

**Records of varying size.** If each row is a different length, no sum gives the position, and access
falls back to sequential.

**Writing a shorter record.** Whatever is left of the previous one stays there. It has to be padded out to
the fixed size.

**Expecting `seek` to warn you.** Jumping past the end and writing leaves zeros in the middle of the file,
with no error at all.
"""),

md("""
---
# Exercises

This week's lab is a mock second midterm in pairs. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · A file's signature

Write out by hand the first bytes of a PNG, a ZIP and a PDF, and a function that opens a file in binary,
reads the first eight bytes and guesses which of the three it is.

Try it with a text file and check that it says it does not recognise it.

### Exercise 2 · The byte that goes missing

Write a binary file carrying `\\r\\n` in the middle. Read it in binary and in text with `latin-1`, and
compare the lengths.

Explain in a comment who ate the byte.

### Exercise 3 · From text to bytes and back

Take a string with accents in it. Convert it to bytes with `utf-8` and with `latin-1`, print both and
compare the lengths.

Then try decoding the `utf-8` bytes as `latin-1` and print what comes out.

### Exercise 4 · The zip

Create three files, put them into a zip with `rglob`, print `namelist()` and `infolist()`, and extract
them into another folder.

Do the exercise again passing `arcname` so that only the file name is inside.

### Exercise 5 · The cursor

Write a twenty-six byte file with the alphabet. Print `tell()` after every operation in a sequence of at
least six `seek` and `read` calls, including one with `whence=2`.

### Exercise 6 · Fixed records

Store ten students with an eight-byte id and a twenty-four-byte name, padding with `ljust`. Read the
seventh with a single call to `seek` and check that the size of the file is ten times thirty-two.

### Exercise 7 · Variable records

Store the same ten students without padding. Try to read the seventh with the same sum and show the
rubbish that comes out.

Explain in a comment what it would take to be able to jump.

### Exercise 8 · The hole

Write five bytes, jump to position fifty and write five more. Print the size of the file and what sits in
the middle.

Add the one-line check that would have prevented it.

### Exercise 9 · The lab

In pairs, each of you writes a short brief requiring a CSV to be read, something to be calculated and a
new file to be written. Swap it with the other pair and solve the one you get.

Constraints: the brief fits in five lines and allows exactly one reading of what is asked.

You hand in your own brief, the other pair's solution, and a note on what turned out ambiguous. The
criterion is that the solution runs against the test file without anyone having to edit a path.
"""),

md("""
---
## Three things to take away

**Binary mode translates nothing.** No line breaks, no accents. What sits on the disk is exactly what
arrives in memory, and text mode does not always warn you when it changed something.

**Random access wants equal records.** If records vary in size, no multiplication gives the position, and
you are back to reading it all or keeping an index on the side.

**Positions count from zero.** `seek(3)` leaves the cursor before the fourth byte, on the same logic as a
list index, and it checks absolutely nothing.

That closes the files unit. Weeks 14 and 15 are graphical interfaces with PyQt6 and carry no notebook,
because a window needs a screen and Colab has none: they are worked in class, on the editor. The thread is
picked up in week 16, where this same problem of storing and retrieving data is solved again, and where
the index you would have to write by hand today comes included.
"""),

md("""
---
# Solutions

### Exercise 1

```python
from pathlib import Path

SIGNATURES = {
    bytes([0x89]) + b"PNG\\r\\n\\x1a\\n": "PNG",
    b"PK\\x03\\x04": "ZIP",
    b"%PDF-": "PDF",
}


def recognise(path):
    with open(path, "rb") as f:
        header = f.read(8)
    for signature, name in SIGNATURES.items():
        if header.startswith(signature):
            return name
    return "not recognised"


Path("a.png").write_bytes(bytes([0x89]) + b"PNG\\r\\n\\x1a\\n" + b"rest")
Path("a.txt").write_text("hello", encoding="utf-8")

print(recognise("a.png"))
print(recognise("a.txt"))
```

### Exercise 2

```python
from pathlib import Path

Path("x.bin").write_bytes(b"12\\r\\n34")
raw = Path("x.bin").read_bytes()
text = Path("x.bin").read_text(encoding="latin-1")

print(raw, len(raw))
print(repr(text), len(text))

# Python's text mode ate it, not the operating system. On reading in text,
# Python turns \\r\\n and \\r into \\n, so two bytes become one.
```

### Exercise 3

```python
word = "naïve"

in_utf8 = word.encode("utf-8")
in_latin = word.encode("latin-1")

print(in_utf8, len(in_utf8))
print(in_latin, len(in_latin))

print(repr(in_utf8.decode("latin-1")))

# The ï takes two bytes in utf-8 and one in latin-1, so the same five-letter
# word measures six bytes in one and five in the other. Decoding the utf-8
# bytes as latin-1 does not blow up and gives back rubbish.
```

### Exercise 4

```python
from pathlib import Path
from zipfile import ZipFile

folder = Path("submission")
folder.mkdir(exist_ok=True)
for n in range(3):
    (folder / f"file{n}.txt").write_text(f"contents {n}", encoding="utf-8")

with ZipFile("with_path.zip", "w") as bundle:
    for p in folder.rglob("*.txt"):
        bundle.write(p)

with ZipFile("without_path.zip", "w") as bundle:
    for p in folder.rglob("*.txt"):
        bundle.write(p, arcname=p.name)

for name in ["with_path.zip", "without_path.zip"]:
    with ZipFile(name) as bundle:
        print(name, bundle.namelist())
```

### Exercise 5

```python
from pathlib import Path
import string

Path("abc.bin").write_bytes(string.ascii_uppercase.encode("ascii"))

with open("abc.bin", "rb") as f:
    print("open       ", f.tell())
    print("read(5)    ", f.read(5), f.tell())
    f.seek(10)
    print("seek(10)   ", f.tell())
    print("read(3)    ", f.read(3), f.tell())
    f.seek(-4, 2)
    print("seek(-4, 2)", f.tell())
    print("read()     ", f.read(), f.tell())
```

### Exercise 6

```python
from pathlib import Path

ID_SIZE, NAME_SIZE = 8, 24
SIZE = ID_SIZE + NAME_SIZE

with open("students.bin", "wb") as f:
    for i in range(10):
        f.write(f"A{i:06d}".encode("ascii").ljust(ID_SIZE))
        f.write(f"student-{i}".encode("ascii").ljust(NAME_SIZE))

with open("students.bin", "rb") as f:
    f.seek(6 * SIZE)
    record = f.read(SIZE)

print(record[:ID_SIZE].strip(), record[ID_SIZE:].strip())
print("Size:", Path("students.bin").stat().st_size == 10 * SIZE)
```

### Exercise 7

```python
from pathlib import Path

with open("variable.bin", "wb") as f:
    for i in range(10):
        f.write(f"A{i:06d}student-{i}\\n".encode("utf-8"))

with open("variable.bin", "rb") as f:
    f.seek(6 * 32)
    print("With the sum:", f.read(32))

with open("variable.bin", "rb") as f:
    for i, line in enumerate(f):
        if i == 6:
            print("Really:      ", line)

# Being able to jump would take one of two things: padding every record out to
# a fixed size, or keeping a separate list of the byte each one starts at. That
# second one is an index, and it is what a database does.
```

### Exercise 8

```python
from pathlib import Path

with open("hole.bin", "wb") as f:
    f.write(b"AAAAA")
    f.seek(50)
    f.write(b"BBBBB")

raw = Path("hole.bin").read_bytes()
print("Size:", len(raw))
print("In the middle:", raw[5:50])
print("All zeros:", raw[5:50] == bytes(45))

# The check that prevents it
POSITION = 50
size = Path("hole.bin").stat().st_size
if POSITION > size:
    print(f"position {POSITION} is past the end ({size} bytes)")
```

### Exercise 9

```python
# My own brief, in five lines:
#
#   The file entries.csv carries the columns student_id, subject and grade.
#   Write a program that reads the file, counts how many students passed each
#   subject with a grade of seven or more, and writes a new file called
#   passes.csv with the columns subject and passes, one row per subject and
#   sorted by subject code.

import csv
from pathlib import Path

SOURCE = Path("entries.csv")
TARGET = Path("passes.csv")
MINIMUM = 7.0


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_passes(rows, minimum=MINIMUM):
    counts = {}
    for row in rows:
        subject = row["subject"]
        counts.setdefault(subject, 0)
        if float(row["grade"]) >= minimum:
            counts[subject] += 1
    return counts


def save(counts, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["subject", "passes"])
        w.writeheader()
        for subject in sorted(counts):
            w.writerow({"subject": subject, "passes": counts[subject]})


if __name__ == "__main__":
    SOURCE.write_text(
        "student_id,subject,grade\\n"
        "A001,COM102,9.1\\nA002,COM102,6.4\\n"
        "A003,COM101,8.0\\nA004,COM101,5.5\\nA005,COM102,7.0\\n",
        encoding="utf-8")

    save(count_passes(read(SOURCE)), TARGET)
    print(TARGET.read_text(encoding="utf-8"))
```

Three decisions worth defending when you hand this in.

**The brief names the output file and its columns.** Without that, two people solve two different things
and both are right. The commonest ambiguity in briefs like this one is not saying what happens to a
subject with no passes; here the `setdefault` settles it, leaving it at zero instead of making it
disappear.

**The three functions can be tested separately.** `count_passes` takes a list and returns a dictionary, so
it is tested with no file and no disk.

**The paths are module constants and relative to the working directory.** Whoever runs it does not have to
edit a single one, which is the lab's criterion.
"""),

]

write(OUT / "en" / "w13.ipynb", en)
print("wrote", OUT / "en" / "w13.ipynb")
