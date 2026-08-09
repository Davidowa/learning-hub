# TIA503: the state of the decks

Weeks 1 to 10 exist in both languages. Seven weeks are still unwritten. This
file records what was decided, what turned out to be wrong in the source
material, and the limits that only show up once a card refuses to fit.

Read [`../../README.md`](../../README.md) for the layout catalogue and
[`../../HANDOFF.md`](../../HANDOFF.md) for the conventions the whole repository
follows. Everything there applies here; this file only covers what is specific
to TIA503.

## The state

```
ppts/vba/analisis-y-procesamiento-de-la-informacion/
  syllabus-tia503.xlsx
  Análisis y Procesamiento de la Información.pdf
  es/  w01 … w10  (.yaml + .pptx)
  en/  same
```

```bash
cd ppts
python -m kit.preflight vba
python -m kit.build      vba
python -m kit.lint       vba
python -m kit.sizes      vba
python -m kit.preview vba/analisis-y-procesamiento-de-la-informacion/es/w01.es.pptx w01 --cols 4
```

All four come back clean on all twenty decks, and the Python and C++ courses
stay clean alongside them.

**The decks carry no speaker notes.** Every `notes:` block was removed from the
twenty lesson files on the instructor's instruction, and the built `.pptx` have
an empty notes pane. Timings, sources and verification caveats live in this file
instead, which is why the source table and the verified-results tables below are
the record rather than a duplicate of it. Nothing else in any lesson changed: the
strip was checked slide by slide, layout by layout, key by key.

**The syllabus moved.** It was under `ppts/office/analisis-y-procesamiento-de-la-informacion/`
along with the course PDF. Both now sit in the subject folder above `es/` and
`en/`, which is where every other course in the repository keeps its syllabus.
`ppts/office/manejo-y-analisis-de-la-informacion/` (TIA501) was left alone.

## The colour

`kit/tokens.py` carries a `VBA` palette and an `EXCEL` one. The palette started
on `#217346`, which is not a published Excel green; a later pass replaced it with
the four official greens, each on the surface where it clears AA. Measured
independently, and the figures match:

| Slot | Value | Why |
|---|---|---|
| `BLUE` structure text | `#107C41` | Excel forest green, 4.96:1 on paper |
| `BLUE_FILL` chips and bars | `#107C41` | white text on it is 5.27:1 |
| `BLUE_DEEP` | `#185C37` | the darkest of the four, 7.53:1 |
| `DARK_CODE.kw` | `#33C481` | 2.11:1 on paper and useless there, 6.87:1 on the green canvas |
| not used | `#21A366` | 3.04:1 on paper and 4.77:1 on the canvas, it fits nowhere |
| `ACCENT` on the canvas | `#E8871E` | duck orange, 5.81:1 |
| `ACCENT_LO` on paper | `#B4530A` | duck orange, 4.73:1 |

VBA has no second brand colour, so the accent pair stays the academy's duck
orange, exactly as C++ does. Two greens would have collapsed the one thing the
accent is for.

In the syntax theme green marks the language (`Sub`, `End Sub`, `True`) and its
objects (`Columns`, `Range`, `Worksheets`), and the warm pair marks the string
and number literals, which on a recorded macro are precisely the values the
recorder copied down from what you clicked.

**The dark canvas is green too.** The template's dark surface is `NAVY`
`#0B1B3A`, which is the right neutral for a language whose logo is blue and the
wrong one for a course about a green program: it left every cover, divider, stat
and code card reading dark blue. The two Office palettes override the slot to
`#0B2A1B`, a deep Excel green, through an `_OFFICE_DARK` dict applied on top of
`_NEUTRAL`. The other three palettes are untouched.

That override is not just the background. The canvas sits a little lighter than
`NAVY` (0.018 against 0.012 relative luminance), so the secondary text and the
comment colour are re-tuned rather than inherited: the blue-greys read as another
palette showing through, and the shared comment grey would have dropped from
4.18:1 to 3.79:1. `ON_NAVY_SOFT` is `#BEDACB` at 10.3:1, `ON_NAVY_DIM` is
`#8FB3A0` at 6.7:1, and the code comment is `#93AE9E` at 6.5:1.

Every slot was measured against the surface it sits on, and every palette in the
kit now clears AA on every slot. The comment grey that the Office palettes had to
solve for the green canvas was the same one the other three were missing on navy;
it has since been raised there too, from `#6B7F9E` to `#7789A6`.

**There is a second palette, `excel`.** Same green, same duck orange, different
syntax theme, for a deck whose code cards hold spreadsheet formulas instead of
VBA. It exists because `highlight.py` scans formulas with a different set of
roles: `com` never carries a comment, since Excel has no comment syntax, so it
carries an error value like `#N/A` and takes the accent instead of comment grey.
Literals drop to the neutral, because in a formula the reference and the error
matter more than the number typed inside it. TIA503 does not use it yet. TIA501,
which is Excel without VBA, is where it belongs.

## Where the code comes from

`docs/en/courses/vba-course/`, module by module, the same way the Python decks
draw on `docs/en/courses/python-course/`. The `.bas` files in the repository are
not the whole story: **the recorded macros live inside the `.xlsm`**, not in the
exported `.bas` beside it. Reading them takes `oletools`:

```python
from oletools.olevba import VBA_Parser
for _, _, name, code in VBA_Parser('amortization_table_macros.xlsm').extract_macros():
    print(name, code)
```

| Week | Source |
|---|---|
| 1 | `00 - Record Macro - Amortization Table/` — `Module2` of `amortization_table_macros.xlsm`, and `amortization_table.xlsx` for the 600-cell figure |
| 2 | `01 - Basic Concepts/BasicConcepts.bas` — module `BasicMacros`, procedure `MessageAndSubs` |
| 3 | `01 - Basic Concepts/BasicConcepts.bas` (`Variables`, `Constants`) and `02 - Access Cells/AccessCells.bas` |
| 4 | `03 - Arithmetic Operators/` (both modules) and `04 - Name Cells/DefineNameCells.bas` |
| 5 | `03 …/ArithmeticExamples.bas` (`CircleAreaInMessageWithInputs`) and `09 …/SubsFunctions.bas` (`ReadInputParametersValidation`) |
| 6 | `00 …/Module2` again, and `12 - Cells/Cells.bas` |
| 7 | `00 …/RecordMacroAmortization.bas` and `09 …/SubsFunctions.bas` |
| 8 | `05 - Comparisson Operators/`, `06 - Logical Operators/`, `07 - Conditional Statements/` |
| 9 | `08 - Repetition Statement/RepetitionStatements.bas` |
| 10 | `09 - Subs and Functions/`, both modules |

## Procedures and functions, verified

| | Result |
|---|---|
| `Summation(5, 3)` | `8` |
| a `Function` that never assigns its own name | **`0`**, silently, no error |
| `MonthlyRate(0.12)` | `9.48879293458305E-03`, the same number as week 4 |
| `ByRef n As Long`, caller's variable at 5 | caller ends at **`50`** |
| `ByVal n As Long`, same | caller stays at **`5`** |
| `n As Long` with no keyword | caller ends at **`50`**, so **ByRef is the default** |
| `Static` counter across three calls | `1`, `2`, `3` |
| `=MonthlyRate(A1)` typed into a cell | `9.48879293458305E-03` |
| `=Summation(5,3)` in a cell | `8` |
| `=MonthlyRate(A1)*12` in a cell | `0.113865515214997` |

**The user-defined function is the payoff of the session**, and for this audience
it is the strongest moment in the course so far: the student writes one
`Function` in a module and Excel then offers it in any cell, beside `SUM` and
`VLOOKUP`. It needs no registration and no add-in.

**One expectation that did not survive the test.** `Application.Run` on a
`Private Sub` in a standard module succeeded, `Err.Number` came back `0`. Private
keeps a procedure out of the macro dialog and out of reach of a direct call from
another module, but late-bound dispatch through `Application.Run` still finds it.
The slide claims only the macro-dialog part, which is editor behaviour and cannot
be checked headless; the deck does not claim `Application.Run` is blocked.

**Two names that will not compile, caught before they reached a slide.** `Double`
is a type keyword, so `Sub Double(n As Long)` is invalid, and `Format` is a
built-in function. Both were renamed. Together with `Put` from week 6, that is
three reserved words that looked like ordinary verbs.

## Loops, verified

| | Result |
|---|---|
| `For i = 1 To 5` building the module's message | `The numbers from 1 to 5 are: 1 2 3 4 5 `, trailing space and all |
| `For i = 10 To 1 Step -3` | `10 7 4 1` |
| `Exit For` at 4 | `1 2 3` |
| module 08's 120-column loop from `B3` | last cell written is **`$DQ$3`** |
| `For Each` over `A1:B2` | `A1, B1, A2, B2`. Row-major, across then down |
| `For Each` over `Worksheets` | index order, not alphabetical |
| deleting 6 flagged rows with `For r = 1 To 6` | **3 left of 6** |
| the same with `For r = 6 To 1 Step -1` | **0 left of 6** |
| 20,000 cells written one at a time | **0.91 s** |
| the same 20,000 written from an array | **0.02 s** |

`$DQ$3` is the payoff of the whole first third of the course. It is the same
column the amortization table's 120 periods end on, so the six hundred cells the
week 1 `stat` slide counted turn out to be four lines of code. Week 9 says that
out loud.

The forward delete leaving exactly half is the cleanest demonstration in the
deck: it raises no error, it looks like it worked, and it processed three of six.
Numbers, not a warning.

The timing pair drives the `stat`. Both versions leave the sheet identical; what
differs is how many times the VBA-to-Excel boundary is crossed. Treat 0.02 as
"too fast to measure properly" rather than as a precise figure, which is why the
slide prints both numbers instead of claiming a multiple.

## The four comparisons that answer backwards

Week 8's pitfalls slide, every row run.

| | Returns |
|---|---|
| `CInt(True)` / `CInt(False)` | `-1` / `0`. So `True + True` is `-2` and `(5 > 1) * 3` is `-3` |
| `10 < 9` | `False` |
| `"10" < "9"` | **`True`**, because as text the 1 sorts before the 9 |
| `"Norte" = "norte"` | **`False`**. `Option Compare Binary` is the default |
| `"abc" < "abd"` / `"A" < "a"` | `True` / `True` |
| empty cell `= ""` | `True` |
| empty cell `= 0` | **`True` as well**, so a test for zero cannot find a missing value |
| empty cell `> 0` | `False` |
| `IsEmpty(empty cell)` | `True`, and this is the one that actually distinguishes |
| `Select Case 7.5` with `Case 7 To 7.99` | `"C"` |
| the module 07 `ElseIf` chain with 7.5 | `"C"`, so the two forms agree |

The case-sensitivity row is the one that pays off later: week 13 cleans
databases, and a column captured as Norte, norte and NORTE groups into three
categories under the default comparison. The empty-cell row changes an average,
which is the kind of error that never raises anything.

## Weeks that carry exam logistics

Week 8 closes with the first midterm and week 13 will close with the second, the
same way COM102 handles it. They are still full topic sessions; the exam material
is one block, not the whole deck. The rules on the slides come from the syllabus
policy section: classroom machines, a USB is allowed, notes and web are allowed,
no communication channel, devices at the front, answer uploaded as
`FullName.zip` to Blackboard.

## Goal Seek, run against a real model

The amortization model was rebuilt from scratch in the harness, 500,000 at 12 %
annual over 120 periods, and `GoalSeek` was called on it.

| | Result |
|---|---|
| monthly rate | `9.48879293458305E-03`, the same number week 4 shows |
| payment before | `1,000`, leaving a closing balance of `1,330,994.06` |
| payment after Goal Seek | `6,997.35869338753`, so `6,997.36` |
| closing balance after | `-5.55701262783259E-10`, **not zero** |
| total paid over 120 months | `839,683.04` |
| interest | `339,683.04`, 68 % of the principal |
| same model at 60 periods | payment `10,967.85` |
| `Application.MaxChange` / `MaxIterations` | `0.001` / `100` |
| `xlCalculationManual` / `Automatic` | `-4135` / `-4105` |

The residue is the pedagogical point and it is why week 7 spends a slide on it.
Goal Seek is iterative, not algebraic: it stops when it is within `MaxChange` of
the goal or after `MaxIterations` tries, so a macro that tests
`If Range("Balance").Value = 0` after calling it will be wrong.

The 339,683 carries the `stat` slide. For a business-school room, the interest
being two thirds of the principal is a stronger argument than anything about
programming, and the figure appears in no cell of the workbook until somebody
computes it.

**`RecordMacroAmortization.bas` is not portable.** Its one line refers to
`Total_Payment__Monthly` and `Principal_Amount`, the double-underscore names
defined in `amortization_table.xlsx` in the same folder. Pasted into a fresh
workbook it stops with error 1004. The deck renames them to `SaldoFinal` and
`PagoMensual`, and this file is where the reason is recorded.

## Variable ranges, verified

The spine of week 6, run against a sheet filled to a known size and then refilled
to a different one.

| | Result |
|---|---|
| `xlUp` / `xlToLeft` | `-4162` / `-4159` |
| `Cells(Rows.Count, 1).End(xlUp).Row`, 12 data rows | `13` |
| `Range("A1").CurrentRegion` | `$A$1:$C$13` |
| `UsedRange` | `$A$1:$C$13` |
| `Range(Cells(2,1), Cells(last,3))`, 12 rows | `$A$2:$C$13` |
| the same line, sheet refilled to 40 rows | `$A$2:$C$41` |
| `Cells(2, 3)` | `$C$2`, and it holds what `C2` holds |
| `Range("A1:C5").Cells.Count` / `.Rows.Count` | `15` / `5` |

**Hiding is not deleting, and the sheet proves it.** Starting from a header row
of Cliente, Region, Venta:

| After | B1 says |
|---|---|
| nothing | `Region` |
| `Columns("B:B").EntireColumn.Hidden = True` | `Region`, still there, just not shown |
| `Columns("B:B").EntireColumn.Delete` | `Venta`, because C shifted across and the data is gone |

**Two names that cannot be used for a procedure.** `Put` collides with VBA's
`Put` statement for binary file writing, and a helper called `Put` made a probe
fail with an opaque `0x800A9C68` rather than anything readable. `Format` is a
built-in function and shadowing it in a slide sets the wrong example, which is
the same complaint this file makes about `Dim month`. Both were renamed.

## And and Or do not short-circuit

Verified with a counter: a function on the right-hand side of `False And f()` and
of `True Or f()` ran once in both cases. VBA evaluates both operands before it
applies the operator, unlike almost every language the students will meet later.

It matters immediately, not as trivia. The obvious way to write week 5's
validation is one condition:

```vb
If IsNumeric(t) And CDbl(t) > 0 Then    ' breaks on text
```

and it stops with error 13 on any non-numeric input, because `CDbl(t)` runs even
after `IsNumeric(t)` has already returned False. The fix is two nested `If`
statements, which is what the deck teaches, and it is worth flagging again in
week 8 when the logical operators get their own session.

Also verified this week, all of it feeding the validation slides:

| | Result |
|---|---|
| `IsNumeric("1,000")` and `CDbl("1,000")` | `True` and `1000`. The thousands separator gets through |
| `IsNumeric("$5")` and `CDbl("$5")` | `False` and error 13. The currency symbol does not |
| `IsNumeric("1e3")` | `True`. Scientific notation counts as numeric |
| `IsNumeric("")` | `False`, which makes `And userInput <> ""` in module 09 redundant |
| `CDbl("")` | error 13, `Type mismatch`. This is what an unguarded Cancel does |
| `vbOKOnly` … `vbInformation` | 0, 1, 4, 16, 32, 48, 64 |
| `vbOK`, `vbCancel`, `vbYes`, `vbNo` | 1, 2, 6, 7 |
| `vbNewLine` | `Chr(13) & Chr(10)` |

## The sheet and VBA disagree, verified both ways

The best material in week 4, and it was not obvious in advance. Every row was
run twice: once as a worksheet formula, once as VBA.

| | In the cell | In VBA |
|---|---|---|
| `-3^2` | **9** | **-9** |
| `"5"+"3"` | **8** | **53** |
| remainder of -5 by 3 | **1** | **-2** |
| `2^3^2` | 64 | 64 |

The first three are three separate decisions that went the other way, not one
bug: unary minus binds tighter than `^` in the sheet and looser in VBA; `+`
coerces text to number in the sheet and concatenates in VBA when both sides are
text; the sheet's remainder takes the sign of the divisor and `Mod` takes the
sign of the dividend. The fourth row is there so the slide is not read as "they
never agree": exponentiation is left-associative in both, so `2^3^2` is 64 and
not 512 in either.

**Locale note for the Spanish deck.** The verification ran on an English Excel,
where the function is `MOD` and the argument separator is a comma. The Spanish
slide writes `RESIDUO(-5;3)`, which is what the room will see. The value is the
same, and this file is where that is recorded.

Other results this week, all run:

| Expression | Result |
|---|---|
| `7.5 \ 2` | `4`. Both operands are rounded to Long first, so it is 8 \ 2 |
| `5.5 Mod 2` and `6.5 Mod 2` | `0` and `0`. Banker's rounding sends 5.5 to 6 and 6.5 to 6 |
| `5 / 0` | error 11, `Division by zero`. The cell shows `#DIV/0!` and carries on; VBA stops |
| `Format(rate, "0.00%")` | `0.95%`, the fix for the `E-03` display |
| `Round(rate, 6)` | `0.009489` |
| circle example, module 03 | `The area of a circle with R: 5 is 78.53975 m^2`, exactly as its own comment claims |
| `Names.Add` then `Range("X").Address` | `$B$1`; a two-column name gives `$A$1:$B$5` and `Cells.Count` = 10 |

**On MsgBox and InputBox.** Both are modal, so neither can be driven from a
headless run. Neither needs to be. What a `MsgBox` shows is the string
conversion of its argument, so the harness evaluates `CStr(expression)` into a
cell and reads it back; and an `InputBox` is verified by substituting the value
a student would type. The dialog is not the thing being checked, the arithmetic
is.

## What Excel actually printed

Run through COM against a workbook with the module injected, Excel 16.0, UK
regional settings. Everything on a slide that claims a result came from this
table. Nothing here was reasoned.

| Expression | Result |
|---|---|
| `CStr(5 / 3)` | `1.66666666666667` |
| `CStr(((1 + 0.12) ^ (1 / 12)) - 1)` | `9.48879293458305E-03`, scientific notation |
| `CStr(-5 \ 3)` | `-1`, truncated toward zero, where Python's `//` gives `-2` |
| `CStr(0.1 + 0.2)` | `0.3`, where Python's `repr` gives `0.30000000000000004` |
| `"5" + 3` | `8` |
| `"5" & 3` | `53` |
| `"5a" + 3` | error 13, `Type mismatch` |
| `Dim n As Integer: n = 2.5` | `2`. And `3.5` gives `4`: banker's rounding |
| `Dim n As Integer: n = 32768` | error 6, `Overflow` |
| `Dim fila As Integer: fila = Rows.Count` | error 6, `Overflow` |
| `Dim fila As Long: fila = Rows.Count` | `1048576` |
| `Dim a, b As Integer` | `a` takes 40,000, `b` overflows. The first one really is a Variant. |
| `String` / `Double` / `Boolean` / `Integer` defaults | `""`, `0`, `False`, `0` |
| `AccessCells` from module 02 | `A1:A5` = 1..5, `B1:B5` = 2,4,6,8,10, `C1:C3` = 3,6,9, `ActiveCell` ends at `$C$3` |
| Typo with no `Option Explicit` | Runs, and the cell keeps the old value. Verified: `A1 = 250` |

Two things about this harness are worth knowing before the next session.

**Compile errors cannot be verified this way.** A compile error opens a modal
dialog inside Excel, which blocks even with `Visible = False`, so
`Application.Run` on a module that will not compile hangs until the call times
out. The `Option Explicit` half of week 3 was verified in the direction that
runs; the "Variable not defined" message comes from the Microsoft reference and
the slide says only that it stops compiling. If a later week needs a compile
error verbatim, take a screenshot by hand.

**Error text follows the Office UI language.** This machine reports `Overflow`
and `Type mismatch`. A Spanish Excel says `Desbordamiento` and `No coinciden los
tipos`. The Spanish decks show the English string, because that is what the
repository and the reference use. What a Spanish Excel shows instead is recorded
here rather than on the slide.

**Watch the labels, not just the values.** Writing `"5 - 3"` into a cell as a
label turns it into a date. Prefix any label that looks like an expression with
an apostrophe, or read `Value2` and wonder why the row says 46145.

**Read the file before quoting it, and run it before putting the result on a
slide.** Three things came out of doing that for week 1 alone.

## Bugs already found in the modules

All of these are in `docs/en/courses/vba-course/`. None has been fixed; they are
listed so a later week quotes around them, or teaches them on purpose.

| Where | What |
|---|---|
| `00 …/Module1` and `Module2` | `SetParametersFormat` declared in both. Public by default, so an unqualified `Application.Run` fails. Verified. |
| `00 …/Module2.HideColumn` | Hides and unhides column D, so it does nothing. Verified. This one is a feature: week 1 is built on it. |
| `04 - Name Cells/DefineNameCells.bas` | **`Sub DefineNameCells()` is declared twice in the same module.** Two procedures with one name in one module is a compile error, so this file cannot compile as it stands. Week 4 has to quote one of the two or merge them. |
| `09 …/AmortizationTable.bas` vs `SubsFunctions.bas` | `SubFunctions`, `SetupFieldsInWorksheet`, `ReadInputParameters` and `ReadInputParametersValidation` appear in both. Importing both modules into one project makes every one of those names ambiguous. |
| `13 - Tables/Tables.bas` | `tableNameToFind` is used in four `MsgBox` calls and never declared, so without `Option Explicit` it prints as empty. Worse, `Dim found As Boolean` appears twice in `AddColumnToTable` and twice in `DeleteColumnFromTable`; VBA has no block scope, so that is a duplicate declaration and the module will not compile. |
| `03 …/ArithmeticOperators.bas` | Two comments contradict their code. `MsgBox 5 - 3` is described as "we subtract 5 from 3", and the parentheses example says the alternative result would be 26 when `5 + 3 * 2` is 11. The code is right, the prose is not. |
| `07 …/ConditionalStatements.bas` | `Dim month As Integer` shadows the built-in `Month` function. Legal, and a bad habit to put on a slide without saying so. |

The pattern worth naming for the student: **four of the seven are the same
mistake**, a name declared twice in a scope that VBA flattens. It is the first
thing to check when a module refuses to compile.

## What was verified in Excel, and what it turned up

Excel 16.0 through COM, `AutomationSecurity = 1`, on a copy of the workbook.

**`HideColumn` does nothing.** The macro reads:

```vb
Columns("D:D").EntireColumn.Hidden = True
Columns("D:D").EntireColumn.Hidden = False
```

Run it and column D ends up visible, exactly as it started. The recorder was
running while the instructor hid the column and then unhid it, and it wrote down
both. This is not a defect to fix in the repository. It is the best argument the
course has for reading a recorded macro before trusting it, and week 1 is built
around it: the `code` slide shows it, the `compare` slide deletes the second
line, and the `quiz` asks what it leaves behind.

**`SetParametersFormat` is declared twice, so it cannot be called by name.** It
exists in both `Module1` and `Module2` of the same project. `Sub` procedures are
public unless declared otherwise, so `Application.Run "SetParametersFormat"`
fails with *"Cannot run the macro… The macro may not be available in this
workbook or all macros may be disabled."* Qualifying it as
`Module2.SetParametersFormat` works. A future week that wants this procedure
should either qualify every call or delete one of the copies. It is not on any
slide yet.

**`NumberFormat = "$#,##0.00"` is not locale-safe.** On a machine with UK
regional settings, running that line renders `£500,000.00`, because an unquoted
`$` in a format code is a currency placeholder rather than a literal. The
workbook's own stored format is `"$"#,##0.00`, with the dollar sign quoted, and
that one does stay a dollar sign. Nothing in week 1 puts a currency format on
screen for this reason. When a later week needs one, quote the symbol, and say
here that the displayed result depends on the machine's region.

**The 600 on the `stat` slide.** `amortization_table.xlsx`, sheet `Example`,
range `B10:DQ14`: 120 period columns by 5 rows. Counted from the file, not
estimated.

## What Microsoft's own documentation says, and where

Corroborated against [MicrosoftDocs/VBA-Docs](https://github.com/MicrosoftDocs/VBA-Docs),
the repository behind learn.microsoft.com. Week 1 leans on four pages:

| Page | What week 1 takes from it |
|---|---|
| `Library-Reference/Concepts/getting-started-with-vba-in-office.md` | The recorder as "a stable bridge between your knowledge of Office as a user and your knowledge as a programmer", with its own caveat that the generated code can confuse because the recorder assumes your intentions. Also "the macro recorder records every keystroke", the Developer tab steps, and the .docm/.xlsm security rule. |
| `Language/Reference/User-Interface-Help/sub-statement.md` | "All executable code must be in procedures", and that `Sub` procedures are public unless declared otherwise. |
| `api/Excel.Range.EntireColumn.md` | `EntireColumn` returns a `Range` for the whole column. |
| `excel/Concepts/Cells-and-Ranges/hide-and-unhide-columns.md` | `EntireColumn.Hidden = True / False` is the documented idiom, so the recorded macro is not doing anything strange. |

The noun/adjective/verb reading of a line on slide 17 is that page's own
analogy: objects are nouns, properties are the adjectives that describe them,
methods are the verbs that animate them. It lands well with a business audience
and it is not an invention.

## What week 1 decided

**No extra credit.** Unlike TIA502, this course has no DataCamp component. Five
components at twenty per cent, and that is the whole hundred.

**The recorder arrives in week 1 and never leaves.** The syllabus puts "2.1
Enabling VBA macros" and "2.2 Recording a macro" in the first session, ahead of
unit 1, and that ordering is worth defending: almost every later week is "this
thing you recorded, now write it better".

**Session numbering is "de 17".** Seventeen syllabus rows, seventeen sessions on
the covers, even though week 17 is the final exam.

**Four roadmap phases, not six units.** The syllabus has six official units but
they do not divide the calendar evenly. The roadmap groups them: weeks 1–5
programming in VBA, 6–7 editing recorded macros, 8–12 decisions, loops and
events, 13–17 Excel tools with R1C1 and security. Keep these four identical in
every week so the `now` marker is the only thing that moves.

## The caps that bit, now in preflight

The code-card caps in the top-level `HANDOFF.md` all hold. Two more showed up on
the `diagram` layout, and **`lint` cannot see either**, because the text stays
inside the safe area and simply lands on top of what is under it.

The card is a fixed 2.48 in tall, so both text rows have a hard ceiling and
neither pushes the other down:

| Field | Box, with four blocks | Cap |
|---|---|---|
| `title` | 3.04 in at 23.25 pt bold | **one line**, about 17 characters |
| `desc` | 2.84 in at 18.75 pt | **two lines**, at any block count |

A two-line title lands on the description. Three lines of description end at
5.15 in against a card that stops at 5.13, so the third line breaks out of the
card, and on a `dark: true` block it comes out in `ON_NAVY_SOFT` over white
paper, where it is close to invisible. Both happened on the first build of
slide 8 and only the contact sheet caught them.

`kit/preflight.py` now checks both. `_diagram` derives the two caps from the
tokens rather than hard-coding them, so a change to `T.block_title` or to the
card height moves the cap with it, and the message names the block and prints
the text:

```
slide 08 diagram: block 3 desc wraps to 3 lines, cap 2 with 3 blocks,
    and spills out of the card -> Los datos viajan con las funciones que los manip
```

The check errs conservative: `wrap_lines` breaks a line slightly earlier than
PowerPoint does, so a description sitting within a few hundredths of an inch of
the edge is reported as three lines even when it renders as two. For a defect
that `lint` cannot see and that only a contact sheet catches, that is the right
direction to be wrong in.

## What the new check found elsewhere

Sixteen `diagram` blocks in COM102, across `w02`, `w06`, `w08` and `w10` in both
languages. **Nine of them were confirmed against the rendered slide and really
do break out of the card**, including `w08.es` slide 15, where the stray line
lands on the dark block and comes out pale blue on paper, exactly the failure
described above. The other seven sit within a hair of the edge.

Those files were left alone. COM102 is finished and another session is working
in the tree, so this is a report, not an edit. The fix in every case is cutting
the description to two lines, which is what week 1 here does.

Both C++ and this course come back clean under the new check.

## Open, and worth someone's decision

**Settled: `dark.com` now clears AA everywhere.** It used to be `#6B7F9E` on
navy, 4.18:1, which passes only if you count 20.25 pt code as large text. The
Office palettes had to solve it anyway for the green canvas, and the other three
have since been raised to `#7789A6` at 4.80:1. Nothing left open here.

**No figures yet.** Week 1 uses the `diagram` layout for the record, read, edit,
run cycle rather than a drawn figure, so `kit/figures.py` was left untouched.
The `img/` catalogue has nothing about spreadsheets. The first one worth drawing
is the Excel object model as nesting boxes, Application to Workbook to Worksheet
to Range, for whichever week introduces the editor.

**The Spanish `vba-course` does not exist.** `docs/es/courses/` has no
`vba-course`, so the Spanish deck cites English module folders. That is what the
Python decks do too, but it is worth knowing before promising a student a
Spanish path through the repository.
