# Previous years, converted

Seventeen exercises and nine homework sets from earlier runs of this course, plus the
second-partial comprehensive exam and two loose practice files. They come out of the folder
the instructor kept as `Ejercicios anteriores`, and they were converted here so that folder
could be retired.

They are not the current material. The twenty-five exercises and twenty-three homework sets
students work through now live one directory up, in [../](../). Nothing here is assigned.
This is the archive, and it is worth keeping because a good deal of it is not repeated in the
current set: the comprehensive exam has no equivalent, the additional practices exist nowhere
else, and several of the exercises take a different run at the same objective.

## What is here

| File | What it covers |
|---|---|
| [ex01](ex01.en.md) | Formatting the grades report |
| [ex02](ex02.en.md) | Names, text joins and the imported homework record |
| [ex03](ex03.en.md) | The curve, the rounding family and the counting functions |
| [ex04](ex04.en.md) | Printing, protection and the PDF |
| [ex05](ex05.en.md) | Operators and wildcards |
| [ex06](ex06.en.md) | VLOOKUP, nested IF, and IF with AND |
| [ex07](ex07.en.md) | Text and date functions |
| [ex08](ex08.en.md) | Lookups and AutoFilter |
| [ex09](ex09.en.md) | Inspection, properties, protection and views |
| [ex10](ex10.en.md) | Charts and tables |
| [ex11](ex11.en.md) | Advanced filters |
| [ex12](ex12.en.md) | Subtotals, and a first PivotTable |
| [ex14](ex14.en.md) | PivotTables over a restaurant's tickets |
| [ex15](ex15.en.md) | What-if analysis |
| [hw01](hw01.en.md) | Formatting |
| [hw02](hw02.en.md) | Absolute and relative references |
| [hw03](hw03.en.md) | Concatenate, formatting and basic formulas |
| [hw04](hw04.en.md) | Written operations practice |
| [hw05](hw05.en.md) | IF with AND and OR |
| [hw06](hw06.en.md) | VLOOKUP and IF |
| [hw07](hw07.en.md) | IF, IFERROR, sparklines and conditional formatting |
| [hw08](hw08.en.md) | Text to Columns, HLOOKUP, data validation |
| [hw09](hw09.en.md) | Filters, validation and formatting |
| [hw11](hw11.en.md) | Advanced filters |
| [comprehensive-2nd-partial](comprehensive-2nd-partial.en.md) | The gym usage log, the whole second-partial exam |
| [additional-practices](additional-practices.en.md) | Five loose sheets, five topics |
| [tables-and-pivot-tables-practice](tables-and-pivot-tables-practice.en.md) | Extra table and PivotTable work |
| [answer-key-formulas](answer-key-formulas.en.md) | Every formula the solved workbooks held |

There is no exercise 13 and no homework 10 in the source folder. They are not missing from
the conversion; they were never there.

## The data

`data/` holds 53 CSV files, 34,776 rows, one file per sheet. A sheet of forty rows or fewer
is also written inline in its exercise so the file can be rebuilt by typing.

## What the CSV could not carry, and where it went instead

A CSV holds values. It does not hold a formula, a conditional formatting rule, a validation
list, a protection setting, a chart or a picture. Each of those was written out as text
before the workbooks were retired, because after that the text is the only copy.

**Formulas.** The solved comprehensive exam held 10,272 of them, which are 27 distinct
patterns filled down long columns. They are all in
[answer-key-formulas](answer-key-formulas.en.md), together with the defined names they
depend on, including `FNAC`, which one column cannot be rebuilt without.

**Conditional formatting, validation and protection.** Written into the exercise that owns
them, with the exact range, the exact condition and the colour as a hex value.

**Charts.** The five in the comprehensive exam are described by type, title and the exact
ranges they plot.

**Pictures.** Homework 4 carried its six statistical formulas as Windows metafiles, an image
format with no text in it. They were rendered, read and transcribed into
[hw04](hw04.en.md), which is now the only record of what they said. The instruction
documents also carried screenshots of Excel running in Spanish; those were read for their
interface strings, which went into the glossary in [../../procedures.es.md](../../procedures.es.md)
under the source key `IMG`, and the images themselves were not kept, because they were taken
on someone else's screen and carry her name and desktop in the frame.

## What was lost on purpose

Cell-level formatting that no exercise teaches: column widths, fonts, fills and borders that
were decoration rather than instruction. Where formatting is the subject of the exercise it
was written down; where it was just how the sheet happened to look, it went.

The two Certiport objective-domain PDFs and the instructor's syllabus PDF are third-party or
administrative material and are excluded by the repository's own rule in `ppts/.gitignore`.

## A note on the source

These files record what the originals said, including where they contradicted themselves.
Several exercises state a rule two different ways, name a file that does not exist, or ask
for something that cannot be done as written. Those are left in place and flagged in each
file's own notes rather than quietly fixed, because the next person to teach from them needs
to know which decisions are still open.
