# 03 · Paths & Files

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/folder-open.svg" width="32" height="32" alt="">

Programs that **remember** things need to read and write files.

## What you'll learn

- **Paths** — where a file lives on disk. Absolute vs relative. `pathlib.Path` (the modern, cross-platform way).
- **Reading and writing text** — `open()`, the `with` statement (ensures files close even if errors happen).
- **Encodings** — why `utf-8` matters (hint: it's the difference between `niño` and `ni�o`).
- **Structured formats:**
  - **CSV** — tabular data like spreadsheets (`csv` module).
  - **JSON** — nested data structures, web-friendly (`json` module).
  - **Pickle** — Python objects straight to disk (use with care; not safe for untrusted sources).

## Plain-language analogy

A file path is like a **postal address**: the operating system needs the full address (`C:\Users\you\notes.txt`) to find your document. A relative path is "two houses down from where you're standing right now".

## Common pitfalls

- Forgetting to close files → use `with open(...) as f:` and never think about it again.
- Mixing path separators between OS → use `pathlib.Path`, never string concatenation.
- Encoding mismatches → always specify `encoding="utf-8"` unless there's a reason not to.

## Source code

[`courses/python-course/03 - Paths and Files/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/03%20-%20Paths%20and%20Files)
