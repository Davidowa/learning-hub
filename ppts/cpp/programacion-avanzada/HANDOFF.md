# COM103, Programación Avanzada: the state of the decks

All eighteen sessions are written in both languages. This file records what was
decided, what was measured rather than assumed, and what is still open.

The generator, the layouts and the house conventions are shared with COM102 and
documented in [`../../README.md`](../../README.md) and
[`../../HANDOFF.md`](../../HANDOFF.md). Read those first. This file only covers
what is different about this course.

## The state

```
ppts/cpp/
  D._S_Malik_-_C_Programming-Cengage_2017.pdf   the textbook, 8th edition
  Introducción al curso.pptx                    the instructor's week 1 deck
  programacion-avanzada/
    syllabus-com103.docx                     the official syllabus, final
    syllabus-com103.pdf                      the copy that goes to Blackboard
    com103-temario-14-unidades-2026.docx     the agreed sequence, for Blackboard
    HANDOFF.md
    es/  w00 … w17  (.yaml + .pptx)
    en/  same
```

Thirty-six lessons, eighteen per language: week zero plus the seventeen the
syllabus lists. `preflight`, `build`, `lint` and `sizes` all come back at zero,
and step five is done: every one of the thirty-six decks has been rendered to a
contact sheet and looked at, both languages, all 754 slides. Nothing was found
that the four checks had missed.

The same pass was then run across the other two Python courses, so all 122
lessons in the repository have now been rendered and looked at: COM102 with its
44, TIA502 with its 42, and these 36. Nothing turned up that the four checks had
missed, in either language, in any of the three.

Preview sheets belong nowhere but a temporary folder. Delete them once you have
looked; loose `w03-1.png` files in `ppts/` are somebody's forgotten scratch.

| Week | Unit | Figure it uses |
|---|---|---|
| 0 | — | `cpp-timeline`, `compilation` |
| 1 | U1 | `compilation` |
| 2 | U1 | none |
| 3 | U2 | none |
| 4 | U3 | `ct-01`, reused for decomposition |
| 5 | U4 | `value-vs-reference`, `scope-cpp` |
| 6 | U5 | `class-object`, `uml-class-cpp`, `access-levels-cpp` |
| 7 | U6 | `ct-05`, the four flowchart shapes |
| 8 | U6 | none |
| 9 | U7 | `hierarchy`, `access-levels-cpp` |
| 10 | U8 | `array-memory` |
| 11 | U9 | none |
| 12 | U10 | `pointer`, `stack-vs-heap`, `vtable` |
| 13 | U11 | `seek-tell` |
| 14 | U12 | none |
| 15 | U13 | none |
| 16 | U14 | `recursion` |
| 17 | — | none |

**Eight figures were drawn for this course**, all in both languages and all in
`IMAGES.md`: `value-vs-reference`, `scope-cpp`, `access-levels-cpp`,
`uml-class-cpp`, `array-memory`, `pointer`, `stack-vs-heap` and `vtable`.

Three of the eight exist because the Python original taught something that is not
true in C++, which is worth knowing before reusing anything else from the COM102
set. `access-levels-cpp` is the clearest case and it is not a relabel. The Python
drawing carries one cross, because Python enforces one of its three levels and
treats the middle one as an agreement. In C++ the compiler enforces all three, and
the interesting question becomes who is asking, so the C++ figure is a matrix:
three members against two callers, outside and a derived class. Measured on this
toolchain, reaching a protected or a private member from outside is `error C2248`,
at compile time.

The temario is the fourteen-unit outline the faculty agreed on, and it is the
document that fixes the teaching order. It still introduces itself internally as
"C++ Programming (2026) / Course Syllabus", which reads as a second syllabus next
to the real one. Left as it is by decision.

## Week zero, and what it replaced

`Introducción al curso.pptx` is eight slides of dense infographics and no text at
all. They are good, but they are built for a screen you can walk up to, and none
of the eight covers where C++ came from.

`w00` is the opening session rewritten in the house style: the history, which was
missing, plus the strongest material from those infographics laid out so it reads
from the back of a room, plus the course logistics. Twenty-three slides.

The sector percentages and the language comparison table come from the original
infographics, which label themselves as the author's own editorial assessment.
They are nobody's published figures. The speaker notes on both slides say so, and
they should keep saying so.

Two things in that comparison invert if read carelessly, so the notes spell them
out: speed is normalised against C at 1.00 and higher is better, memory is
normalised the same way and lower is better.

The original pptx stays where it is. Nothing in `w00` depends on it.

Neither document has gone out to students. The faculty are still reviewing both,
so wording and sequence can still change, and two things already have.

The kit is ready for C++. `kit/highlight.py` already knew the language, and a
`cpp` palette was added to `kit/tokens.py` for this course: the ISO C++ blue
`#00599C` takes the structure slots, and the accent pair stays the academy's duck
orange so that "the accent means this is the risk" keeps reading as a warning
instead of collapsing into a second blue. Set `language: cpp` in `meta` and
`lang: cpp` on every code slide.

## What was measured, and on what

The machine that wrote week 1 has **Visual Studio Community 2026** installed, so
several things this file used to flag as unverified were run rather than assumed.
Toolset 14.51.36231, `_MSC_VER` 1951, x64, built from the command line with
`cl /EHsc`. Anything below is a real result on that toolchain, and worth
re-measuring if the classroom machines differ.

**The compiler defaults to C++14, and `__cplusplus` lies.**

| Flags | `__cplusplus` | `_MSVC_LANG` |
|---|---|---|
| none | 199711 | 201402 |
| `/std:c++20` | 199711 | 202002 |
| `/std:c++20 /Zc:__cplusplus` | 202002 | 202002 |

The first row confirms the C++14 default. The second is the one that matters for
teaching: a student who sets the standard correctly still sees 199711, because
MSVC keeps `__cplusplus` frozen for compatibility with code that predates the
conformance work. `_MSVC_LANG` reports the real value with nothing configured.

This broke `w00`'s homework, which asked for `__cplusplus` and marked a C++20
value as the pass criterion. Both languages now ask for `_MSVC_LANG`, and the
speaker notes explain why. Week 1 shows the two macros side by side, since a
compiler answering something other than what was expected is a better first
lesson than a slide asserting it.

**Week 16's four open questions are answered.** All four came back the way the
deck needs them to:

- `<thread>` and `<mutex>` compile under `/std:c++20`.
- `std::jthread` is present in the shipped toolset.
- No extra linker setting. `cl /EHsc /std:c++20` links a threaded program with
  nothing added, so week 1's project template needs no change for week 16.
- Two threads writing to `std::cout` without a lock do interleave. **The mess is
  thinner than it sounds:** two torn lines out of four hundred in one run, of the
  shape `BBBBAAAA 0` and `AAAA 150 0`. Enough to prove the point, not enough to
  be visible from the back row at twenty iterations. Whatever the demonstration
  loops over, make it hundreds, and expect the count to change every run.

**One crash in `kit.sizes`, since fixed.** Running it against this course used to
abort on `Introducción al curso.pptx`, the instructor's original deck, which is
all images and carries no sized text runs: `min()` was called on an empty counter
before it reached the generated decks. `sizes.py` now skips a deck with no sized
runs and says so. Worth knowing only because any course that keeps a hand made
`.pptx` next to the generated ones can hit the same shape of problem.

## What is still open

**The examples are written for the course and there is no repository to point
at.** COM102 could promise that every line on a slide came from
`docs/en/courses/python-course/`, and its cover notes named the file. There is no
`docs/en/courses/cpp-course/`, so the COM103 cover notes say plainly that the code
was written for the course and that no clonable file exists. That was the option
this handoff already leaned towards, and all eighteen sessions were written under
it. If the folder is ever created, the cover notes of all thirty-six decks have to
change, and the code on the slides has to match what lands in it. Cheaper to
decide before the decks go out than after.

**The `diagram` check was too strict, and the decks were right.** A check added to
`kit/preflight.py` flagged sixteen COM102 slides for a description wrapping to
three lines in a fixed-height card. Rendering one of them settled it: `w02.es`
slide 8 draws its three descriptions on two lines each, well inside their cards.
The arithmetic explains the rest. The description row has 1.11 in of card beneath
it and a line is 0.38 in, so it holds 2.94 lines; truncating that to two rejected a
third line whose descender lands 0.02 in below the card edge. `DIAGRAM_SLACK` in
`preflight.py` buys back that rounding and nothing else, so a fourth line, which
clears the card by 0.40 in, is still caught. Verified against a deliberately
overflowing fixture. No lesson file was edited, in either course.

## Week one, and the one thing it teaches about writing the rest

Twenty-five slides, three blocks: the environment, source to executable, and the
debugger. It leans on Visual Studio being projected, and the group should be
building their own project during the first block rather than watching one.

The debugging example is an average computed from three exams and divided by
four. It is deliberately straight-line, because control structures are unit 6 and
weeks 4, 5 and 6 come before them, but the constraint bites in week 1 too and it
is worth knowing how little you need. The bug shows up in `Locals` with no
conditional anywhere, and the integer truncation it exposes hands week 2 its
opening question.

**English overflows where Spanish does not.** The first build of `w01` came back
clean in Spanish and with two overflows in English, in the same two places: a
four-annotation stack beside a code card, and a `trace` verdict. English prose
sets wider here than the Mexican-neutral Spanish it is translated from, so the
language that clears `lint` first is not evidence about the other one. Build and
lint both before believing either. The fix both times was cutting a clause, not
reflowing the slide.

**The course objective called C++ a low-level language.** It read "un lenguaje
compilado de bajo nivel cercano al hardware". C++ is a high-level language that
gives close control of the hardware, which is not the same claim. Corrected in
`syllabus-com103.docx` to "un lenguaje compilado de alto nivel con control cercano
al hardware". No copy of the pre-correction wording survives, so the original
sentence is recorded above in full.

**The weekly agenda contradicted the agreed unit order.** The fourteen units were
decided jointly by the faculty, and `syllabus-com103.docx` laid its seventeen
weeks out in a different sequence: control structures at weeks 4 and 5, classes
at week 10. The agenda in that file has been reordered to follow the units. Its
subtopic numbering, the three partials and the evidence column moved with it, and
all ninety-three subtopics were checked present afterwards. The old sequence was
weeks 1, 1, 2, 6, 6, 3, 4, 8, 9, 5, 7, 11, 10, 12, 13, 14 by unit.

## The order, and the one thing it costs

`com103-temario-14-unidades-2026.docx` is the agreed sequence, and
`syllabus-com103.docx` now matches it week for week. The table below is what both
documents say.

Fourteen units over seventeen weeks leaves three weeks of slack. Two units are
large enough to take two weeks each, and the remaining week is the project. Doing
that lands the three partials exactly on the weeks the syllabus already fixes.

| Week | Unit | Topic | Milestone |
|---|---|---|---|
| 1 | U1 | Elementos básicos I: entorno, compilación, depuración, anatomía | |
| 2 | U1 | Elementos básicos II: variables, operadores, conversión, estilo | |
| 3 | U2 | Tipos, espacios de nombres y `string` | |
| 4 | U3 | Funciones I | |
| 5 | U4 | Funciones II | |
| 6 | U5 | Clases y abstracción de datos | |
| 7 | U6 | Estructuras de control I: selección | |
| 8 | U6 | Estructuras de control II: repetición | **Parcial 1** |
| 9 | U7 | Herencia y composición | |
| 10 | U8 | Arreglos y cadenas | |
| 11 | U9 | Registros (structs) | |
| 12 | U10 | Punteros, virtuales y abstractas | |
| 13 | U11 | Entrada y salida | **Parcial 2** |
| 14 | U12 | Sobrecarga y plantillas | |
| 15 | U13 | Manejo de excepciones | |
| 16 | U14 | Recursión e introducción a multihilos | **Parcial 3** |
| 17 | — | Proyecto integrador | **Proyecto** |

Partial 1 covers U1 to U6, partial 2 covers U7 to U11, partial 3 covers U12 to U14.

**One writing constraint falls out of it.** Control structures are unit 6, so
weeks 4, 5 and 6 come before `if`, `while` and `for` have been introduced. Code
examples in those three decks stay straight-line: constructors that assign,
accessors that return, member functions without a branch. A `Rectangulo` with
`getAncho`, `setAncho` and `area` works; a setter that validates its argument
waits until week 7. Worth knowing before starting those decks, because the obvious
examples all reach for a conditional in the second line.

## The textbook, and a correction worth making before writing

Both documents cite **Malik, 5th edition, 2011**. The PDF in the repository is
**C++ Programming: Program Design Including Data Structures, 8th edition, Cengage,
2018**. Between those editions Malik merged the two function chapters into one and
moved the array-applications chapter to the back, which shifts every chapter from
the seventh onwards.

So the chapter numbers written in both documents are correct for the book they
cite and wrong for the book on disk. Every one was checked against the 8th
edition's table of contents. Use the right-hand column, or get the 5th edition.

| Unit | Topic | Documents say | In the PDF on disk (8th ed.) |
|---|---|---|---|
| U1 | Basic elements | ch. 2 | ch. 1 and 2 |
| U2 | Types, namespaces, `string` | ch. 2 and 8 | ch. 2 and **7** |
| U3 | Functions I | ch. 6 | ch. 6 |
| U4 | Functions II | ch. 7 | ch. **6** (merged in this edition) |
| U5 | Classes and data abstraction | ch. 12 | ch. **10** |
| U6 | Control structures | ch. 4 and 5 | ch. 4 and 5 |
| U7 | Inheritance and composition | ch. 13 | ch. **11** |
| U8 | Arrays and strings | ch. 9 | ch. **8** |
| U9 | Records (structs) | ch. 11 | ch. **9** |
| U10 | Pointers, virtual, abstract | ch. 14 | ch. **12** |
| U11 | Input/output | ch. 3 | ch. 3 |
| U12 | Overloading and templates | ch. 15 | ch. **13** |
| U13 | Exception handling | ch. 16 | ch. **14** |
| U14 | Recursion and multithreading | ch. 17 | ch. **15**, plus outside material |

Malik has no chapter on threads in any edition. Unit 14 asks for `std::thread`,
mutexes and shared resources, and that material has to come from somewhere else.
Settle the source before writing week 16.

## Two things that are not like COM102

**There is no C++ source code in the repository.** COM102 could promise that every
line on a slide came from `docs/en/courses/python-course/`, and the cover notes
named the file. There is no `cpp-course` folder under `docs/`, so that promise
cannot be kept here without a decision. Three ways out, in the order they seem
worth considering:

Write a `docs/en/courses/cpp-course/` alongside the decks. Matches what COM102
does, gives students something to clone, and makes the cover notes honest. Costs
the most up front.

Quote Malik's programming examples. They exist, they are tested, and the book is
the course text. The cover notes would cite chapter and page instead of a repo
path. Watch the licence: the PDF carries "may not be copied, scanned, or
duplicated, in whole or in part", so a deck can teach from an example but should
not reproduce pages of it.

Write the examples in the deck only. Fastest, and it breaks the one promise that
made the COM102 decks trustworthy. If this is the choice, say so in the cover
notes rather than letting a reader assume a repo file exists.

**The grading has no homework component.** Three partial exams averaged together
are 80 %, and the integrating project is 20 %. That is the whole of it. Every
COM102 deck closes its `homework` slide with "Parte del 20 % de tareas", and
copying that line into a COM103 deck would state a weight that does not exist. Use
the `homework` layout for practice and for the evidence the syllabus asks for, and
give it the honest weight, which is none.

## Decisions already taken

**Visual Studio 2026 Community.** Week 1 shows its projects, solutions, build
configurations and the Watch, Call Stack, Locals and Immediate windows.

**C++20, set explicitly.** MSVC does not take its standard from the IDE version.
`/std` is a per-project property and has historically defaulted to `/std:c++14`,
so a fresh project gives C++14 unless somebody changes it. Week 1 has to show
Project Properties, C/C++, Language, C++ Language Standard, because getting that
wrong silently breaks half the later weeks. Pin the version in the footer the way
COM102 pins Python 3.12.

C++20 also buys `std::format`, which matters more than it sounds: a code card caps
at 63 characters and `std::cout << a << " " << b << std::endl;` burns through them.

**Both kinds of pointer.** Unit 10 teaches raw pointers, including `*` and `**`,
and `unique_ptr` alongside them. Raw first, since `new` and `delete` are what the
unit asks for, then the smart pointer as the thing you reach for afterwards.

**The code on the slides is written for the course.** No `cpp-course` folder
exists under `docs/` yet. Examples are generated rather than quoted from Malik, so
the licence question goes away, but the cover notes cannot point at a repo file
until that folder exists. Decide early whether the examples land in
`docs/en/courses/cpp-course/` so students can clone them, the way COM102 does.

**The project brief is in the syllabus.** Assigned after the first partial, built
in teams, with progress checks and a final delivery of code, written document and
oral presentation on the final exam date. Graded individually even though the work
is in teams. Rubric: correctness and robustness 40 %, design and modularity 25 %,
efficiency and memory use 20 %, documentation and presentation 15 %.

**The three partials are cumulative.** This is not a detail, it changes how weeks
8, 13 and 16 are written. Each exam covers everything taught so far, not the block
since the last one, which is why the grading table says "Acumulativo" instead of
listing units per partial.

COM102 did the opposite: its `tiers` slide on week 8 listed units 1, 2 and 3 as
the scope and named what was excluded. Copying that shape here would tell students
something false. The equivalent slide for COM103 says the partial covers unit 1 up
to the current unit, every time, and the third one covers the whole course.

## The syllabus is final

`syllabus-com103.docx` is closed. The decks follow it as written rather than the
other way round, and no further edits to it should be proposed.

Two things inside it sit oddly together, and whoever writes weeks 6 to 16 will
notice. Neither is a defect to fix, they are just worth knowing before the
question arrives from the room:

The header describes the document as date independent and numbered by "Semana N",
while the grading table gives the three partials calendar dates. When a deck needs
to name when a partial happens, use the calendar dates, since those are what
students will be holding.

The project is assigned after the first partial and its progress checks fall in
weeks 6, 10 and 13. The week 6 check therefore lands before the assignment in the
week numbering. Slides that mention the project should refer to the progress
checks by their own schedule and not tie them to the partials.

**Threading comes from the official documentation, and it stays small.** Malik has
no threading chapter in any edition, so unit 14 takes it from cppreference for
`std::thread`, `std::jthread`, `std::mutex` and `std::lock_guard`, and from
Microsoft Learn for anything specific to the toolchain. Nothing from the standard
itself, which is not teaching material.

Small is what the unit asks for. Four of its six subtopics are recursion and the
partial; only two are threads, and the second says "overview". One demonstration
and one fix is the right size.

Since the course is C++20, prefer `std::jthread`. A `std::thread` whose `join()`
was forgotten calls `std::terminate`, so a student's first threading program
crashes for a reason that has nothing to do with concurrency. `jthread` joins in
its destructor. Show `std::thread` too, because that is what they will meet in
older code and in the book.

The four things this file used to list as unchecked before week 16 have now been
run on Visual Studio Community 2026. See "What was measured, and on what" above
for the results and for the one surprise, which is how little the unsynchronised
output actually tears.

**One constraint this puts on the deck.** Thread output has no fixed order, so the
`code_output` layout cannot promise a result the way every other week does. Either
label the panel as one possible run, or use the unsynchronised version, where the
garbled output is the point and any garbling proves it.

## Figures

Twenty-eight are already drawn, catalogued in [`../../IMAGES.md`](../../IMAGES.md).
These carry over unchanged, since they explain a mechanism rather than a language:
`ct-01` to `ct-10`, `paradigms`, `recursion`, `hierarchy`, `polymorphism`,
`class-object`, `class-vs-instance`, `seek-tell`. `ct-01` is already in use, in
week 4, for decomposition.

**`scope` was on that list and does not belong there.** The drawing itself is
language independent, three nested boxes for global, function and local, captioned
"lo local muere cuando la función termina". But the arrow pointing out of the local
box is labelled **NameError**, which is Python's exception. The equivalent in C++ is
the compiler error `C2065: undeclared identifier`, measured on this toolchain, and it
happens at compile time rather than at run time, which is a difference worth teaching
rather than papering over. Week 5 needs a `scope-cpp` variant with that label changed;
everything else in the figure can stay as drawn.

`uml-class` is still unverified and sits in the same suspicious position: the
catalogue says its three compartments are "wired to the line of Python it turns into".
Open the PNG before week 6 uses it.

These do not, and reusing them would teach something false: `access-levels` is
labelled with Python's underscore conventions and C++ has real `public`,
`protected` and `private` keywords; `file-lifecycle` draws Python's `with` block;
`collections` and `slicing` draw Python containers; `event-loop`, `layouts` and
`db-access` belong to material this course does not cover.

`compilation` was on this list and is now drawn. It carries weeks 0 and 1, and it
is the figure that explains what a compiled language even is.

Six are still worth drawing, most for mechanisms Python never made visible:

- `stack-vs-heap` — automatic storage against dynamic, and where the lifetime
  ends. Weeks 4 and 12.
- `value-vs-reference` — the same argument passed both ways, with the copy drawn.
  Week 5, and it is the hardest idea in that week.
- `pointer` — a variable, its address, and the pointer that holds it. Week 12.
- `array-memory` — contiguous cells, the index arithmetic, and where the bounds
  are not checked. Week 10.
- `vtable` — one call site, the pointer, and which override actually runs.
  Week 12.
- `access-levels-cpp` — a redraw of the existing one with the three C++ keywords
  in place of the underscore conventions.

## Everything else is inherited

The caps on code cards, the YAML traps, the accent rule, the no-em-dash rule, the
cover subtitle budget of about 130 characters, the Mexican-neutral Spanish and the
five-step verification loop are all in [`../../HANDOFF.md`](../../HANDOFF.md) and
apply here without change. The loop for this course:

```bash
cd ppts
python -m kit.preflight cpp
python -m kit.build     cpp
python -m kit.lint      cpp
python -m kit.sizes     cpp
python -m kit.preview   cpp/programacion-avanzada/es/w01.es.pptx w01-es --cols 5
```

The preview writes its sheets into `ppts/`, so delete them once you have looked.
Step five is not optional here either.

One thing to watch that COM102 never hit: C++ lines are longer than Python lines.
`std::cout << "..." << std::endl;` eats characters fast, and the cap is 63 for a
normal code card. Expect to use `using namespace std;` on slides even where a real
project would not, or to break statements across lines more often than the book
does.
