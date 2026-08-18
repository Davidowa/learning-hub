# Solutions · Information Management and Analysis · TIA501

The worked answer, what the sheet or the dialog shows, a ten-point rubric and the mistake
that costs the most marks. Statements are in exercises.en.md and use the same numbering, so
09.2 sits in the same place in both files.

Every rubric spends points on the route and not only on the result, because that is what the
exam grades. A workbook that looks right but was built with ribbon shortcuts does not score
what one built through the graded dialog scores, and each rubric says so in a line.

---

## Week 01 · Course framing and the rule that grades every task

### 01.1 · Recognise

**Solution**

On screen the two ranges are identical. White bold text, dark blue fill, a border round the block and a border between the cells. Nothing in the picture separates them.

Copy A spent four operations, one per ribbon button. Copy B spent one, because everything set inside Format Cells is committed by the single OK at the end.

That is what the undo reads. On copy A, Ctrl+Z takes back the last operation only, which was All Borders, and leaves the bold, the white font and the dark blue fill in place. On copy B the same single press takes the whole block back to plain, because there is only one operation to take back.

Copy B answers an item worded from the Format Cells dialog box. Copy A earns nothing on that item, which is objective 2.2.6. It is the correct answer to a differently worded task and it is still the route most people will use at work.

**Output**

```text
On screen, both copies    white bold text, dark blue fill, borders outside and inside
Operations, copy A        4
Operations, copy B        1

Copy A after one Ctrl+Z   borders gone, bold and white and dark blue still there
Copy B after one Ctrl+Z   B2:E2 plain again, every setting gone in one press

The item                  copy B scores, copy A scores nothing
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Says the two ranges look the same on screen | 2 |
| Counts four operations against one | 2 |
| Reads the single undo correctly on both copies | 4 |
| Names copy B as the route the item accepts | 2 |

**Most common mistake**

Reporting that one Ctrl+Z empties copy A as well, on the grounds that the two sheets look the same. The picture is the same and the history is not, and the undo reads the history.

### 01.2 · Apply

**Solution**

Four clicks on copy A, one trip through the dialog on copy B. What the exercise is really testing is the order of the two audits: undo is a stack over the whole workbook, not a stack per range. Format both rows first and the first Ctrl+Z takes back the dialog operation on A5:D5, which says nothing at all about A1:D1. Each reading has to be taken immediately after the operation it belongs to, with Ctrl+Y putting the formatting back before the next task starts.

F1 to F4 carry the four findings. Wording will vary; the numbers and the two undo states will not.

**Output**

```text
A1:D1   four operations, one per Home tab button
A5:D5   one operation, Ctrl+1 and a single OK

Ctrl+Z once, straight after A1:D1
  All Borders gone. Bold, white font and dark blue fill still there.

Ctrl+Z once, straight after A5:D5
  bold, white font, dark blue fill and both border sets gone together

A2:D2   G414   190000   195000   5000, untouched by either audit
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both heading rows carry the same picture | 2 |
| A5:D5 was one operation, and the single undo proves it | 3 |
| The reading for A1:D1 names the borders and only the borders | 2 |
| Each undo was taken straight after its own operation | 2 |
| The four findings are written into F1:F4, not described separately | 1 |

**Most common mistake**

Formatting both rows and only then starting to press Ctrl+Z. The first press takes back the dialog operation on A5:D5, the second takes back the borders on A1:D1, and the student writes down that the ribbon route also undoes everything at once. It gives itself away by reporting the same behaviour for both rows.

### 01.3 · Integrate

**Solution**

| # | Verdict | Why, and the route that does score |
|---|---|---|
| 1 | Fails | The item names the dialog. Ctrl+1, Font tab, Fill tab, Border tab with the style set before the edges, one OK |
| 2 | Scores | Objective 2.2.5 is written against the Number group on purpose, and this is exactly it |
| 3 | Fails | Comma Style cannot colour anything. Ctrl+1, Number tab, and a negative-numbers entry in red parentheses, or a custom code |
| 4 | Cannot run | UNIQUE is a Microsoft 365 dynamic array function, listed only by MO-210, and it does not exist in Office 2019 |
| 5 | Cannot run | XLOOKUP, same case, listed only by MO-211 |
| 6 | Fails | The Borders menu has no diagonal. It exists only in the Border tab preview box of Format Cells |
| 7 | Scores | One selection, one dialog, one OK, and a single Ctrl+Z would prove it |
| 8 | Scores | Objective 2.2.7 asks for a named cell style, and Bad is one |

Rows 4 and 5 are the version rule in practice. Eight of the eleven objectives that MO-210 and MO-211 add over the 2019 exams are dynamic array functions, and no slide, exercise or exam question in this course depends on any of them.

The term. Midterm 1 falls in week 6 and midterm 2 in week 12. The classroom exam is seventy per cent of a midterm and the assignments and activities of the weeks it covers are the other thirty. On midterm 1 that thirty is credited only to students who have covered the certification payment; the exam half is graded for everyone.

**Output**

```text
Scores        2, 7, 8
Fails         1, 3, 6
Cannot run    4 (UNIQUE, MO-210), 5 (XLOOKUP, MO-211)

Midterm 1     week 6      Midterm 2    week 12
Exam share    70 %        Coursework   30 %
Condition     the 30 % of midterm 1 needs the certification payment covered
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six runnable rows judged correctly | 3 |
| A working route named for rows 1, 3 and 6 | 3 |
| Rows 4 and 5 named as 365 only, with the function and the exam | 2 |
| The two midterm weeks, the 70 / 30 split and the payment condition | 2 |

**Most common mistake**

Marking row 2 as a failure because it used the ribbon. The ribbon is the answer there. The rule is not that the dialog always wins, it is that the route the item names wins, and 2.2.5 names the Number group.

---

## Week 02 · Session 4 · First contact with Excel

### 02.1 · Recognise

**Solution**

(a) The selection defines how far the series runs, so all seven cells fill: 5, 11, 17, 23, 29, 35, 41.

(b) With a Stop value the selection can be a single cell and Excel decides how far to go. It stops as soon as the next term would pass 30, so the last value written is 29 and H8 and H9 are never touched.

(c) Dragging the handle from a single cell holding a number copies that number. Seven cells, all holding 5. The handle infers a step only when it has two values to read.

(d) Two seeds, so the handle reads the step of 6 and produces the same seven values as (a).

The Auto Fill Options button appears at the bottom right of the block after a drag and never after Fill from the ribbon, which makes it the cheapest visible record of which route was taken. Only (b) is out of reach of the handle, because there is no way to tell a drag where to stop.

**Output**

```text
(a) H3:H9    5  11  17  23  29  35  41     no Auto Fill Options button
(b) H3:H7    5  11  17  23  29            H8 and H9 stay empty, no button
(c) H3:H9    5   5   5   5   5   5   5    Auto Fill Options button appears
(d) H3:H9    5  11  17  23  29  35  41    Auto Fill Options button appears

Same seven numbers out of (a) and (d), two different routes
Only (b) cannot be produced by the handle
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) and (d) both give the seven values, and they match | 3 |
| (b) stops at 29 and leaves H8 and H9 empty | 3 |
| (c) copies rather than counts | 2 |
| The button appears after (c) and (d) only, and (b) is the one the handle cannot do | 2 |

**Most common mistake**

Writing 5, 6, 7, 8 and so on for (c). A drag on one cell holding a number copies it. That is the whole reason (d) needs two seeds, and a student who answered (c) as a count usually answered (d) as a count too, which hides the error.

### 02.2 · Apply

**Solution**

Task 1. Center Across Selection lives only in the Horizontal list of the Alignment tab. It centres the title over the six columns and merges nothing, so the Name Box still reads A1 and the sorting and filtering of week 10 still work over that row.

Task 2. Four tabs, one OK. On the Border tab the Line Style and the Color have to be chosen before Outline and Inside are clicked; a border drawn first keeps the previous style and clicking the style afterwards does nothing to it.

Task 3. Accounting lines up the currency symbols on the left edge of the cell and the decimal points with each other. Currency is the other one, with the symbol tight against the digits, and the exam distinguishes them.

Task 4. Percent Style multiplies the picture by a hundred and leaves the stored value alone. E3 goes on showing 3% while the formula bar goes on reading 0.03.

Task 5. A single click on Format Painter arms the brush for one use. The double-click locks it, which is what a task naming two separate destinations is looking for, and Esc releases it.

Task 6. Clear Formats removes the Neutral style from F8 and leaves the number 88 where it was. Delete would do the opposite, removing the value and leaving the style behind, which is the reason objective 2.2.8 exists as its own line on the domain list.

**Output**

```text
A1    Detalle de ventas, centred over A1:F1, size 14 bold
      Name Box reads A1, not A1:F1

A2:F2 white bold on a dark fill, wrapped, centred both ways,
      outlined and ruled inside, from one trip through Ctrl+1

B3  $ 190,000    C3  $ 195,000    D3  $ 5,000
B4  $ 220,000    C4  $ 225,000    D4  $ 5,000
B5  $ 170,000    C5  $ 180,000    D5  $ 10,000
B6  $ 210,000    C6  $ 216,000    D6  $ 6,000
B7  $ 215,000    C7  $ 245,700    D7  $ 30,700
B8  $ 195,000    C8  $ 198,000    D8  $ 3,000

E3  3%    E4  2%    E5  6%    E6  3%    E7  14%    E8  2%
      formula bar on E7 still reads 0.14

F8    88, still there after Clear Formats, Neutral style gone

Ctrl+Z once after task 2   the whole heading block goes back to plain in one press
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The title is centred over A1:F1 and the Name Box still reads A1 | 2 |
| The heading block came from one trip through Ctrl+1, and the single undo proves it | 3 |
| On the Border tab the style and the colour were set before the edges | 1 |
| Accounting and Percent came from the Number group, and the formula bar still shows the raw values | 2 |
| The brush was locked with a double-click and released with Esc | 1 |
| Clear Formats leaves the value in F8 and removes the style | 1 |

**Most common mistake**

Merging A1:F1. It produces the same picture, and the Name Box gives it away by reading A1:F1 instead of A1. It also blocks the sorting and most of the filtering that arrive in week 10, so the cost of the shortcut turns up eight weeks later on a different exercise.

### 02.3 · Integrate

**Solution**

| # | Route actually taken | Scores | What has to be run instead |
|---|---|---|---|
| 1 | The Home tab buttons, one operation per button | No | Ctrl+1, Font tab, Fill tab, Border tab, one OK |
| 2 | Merge & Center | No | Unmerge Cells, then Ctrl+1, Alignment tab, Horizontal set to Center Across Selection |
| 3 | A drag of the fill handle | No | Home tab, Editing group, Fill, Series, with the step typed in |
| 4 | The Number group, Percent Style | Yes | Nothing. The value is untouched and only the picture changed |
| 5 | The value was retyped as `0.03%` into a cell already holding 0.03 | No | Retype 0.03, then apply Percent Style to it |
| 6 | Format Painter clicked once instead of double-clicked | No | Select row 3, double-click Format Painter, paint row 5 and row 6, press Esc |

Row 5 is the only one where the sheet itself is damaged. Everywhere else the numbers are intact and the route was wrong. Here the stored value moved by two decimal places, so the workbook is now carrying data that no reformatting will repair.

The formula bar settles rows 4 and 5, because it shows the stored value with no format over it. The Name Box settles row 2, because a merged block reports its whole address and an unmerged one reports the top left cell.

**Output**

```text
Fails       1, 2, 3, 5, 6
Scores      4
Damaged     5, the only one where the number itself is wrong

Formula bar decides    rows 4 and 5
Name Box decides       row 2

After the repairs
  the title reads across A1:F1 and the Name Box reads A1
  row 6 matches row 3, and the brush was armed once for both destinations
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Six verdicts, with the route named for each | 4 |
| Row 5 identified as a corrupted value rather than a wrong route | 2 |
| Formula bar for rows 4 and 5, Name Box for row 2 | 2 |
| Rows 2 and 6 repaired in the workbook, and the repair provable | 2 |

**Most common mistake**

Marking row 4 as a failure because 8% shows where the data said 0.08. That is precisely what a number format does, and it is the behaviour row 5 was supposed to be contrasted against. The tell is a student who marks both of them the same way.

---

## Week 03 · Sessions 5 and 6 · Structure and references

### 03.1 · Recognise

**Solution**

Part one. Three of the nine are worth spelling out. `=-A4^2` answers 9 because the minus sign of a negative outranks the exponent, so Excel squares the negative three rather than negating the square. `=2^A4^2` answers 64 because equal ranks resolve left to right, giving eight squared and not two to the ninth. `="Total "&A1+A3` answers `Total 12` because concatenation sits below addition, so the sum runs first and the text is glued to the result.

The two error values come from different places. `=A1/(A3-4)` divides by a zero the sheet does not display anywhere. `=A2+"a"` is arithmetic against a letter, which nothing can convert.

Note what A2 does and does not do. `=A1+A2*2` answers 32, because an arithmetic operator converts text that looks like a number. That conversion is the operator's doing and not the cell's, so A2 is still text and still sitting on the left of its cell.

Part two. Deleting column B moves the actual figures from C into B and moves the difference formula from D2 into C2. Excel rewrites the reference that pointed at the surviving column and replaces the one that pointed into what was deleted, so the formula bar reads `=B2-#REF!` and the cell displays `#REF!`.

Nothing repairs itself. Ctrl+Z pressed immediately does bring back the whole column, the planned figures and the original formula, because it reverses the delete as one operation. Once anything else has been done, the planned figures are gone, and repairing the formula means retyping the data first.

**Output**

```text
=A1+A2*2         32
=A1*A2           96
=-A4^2           9
=2^A4^2          64
=A1-A3*A4^2      -28
=20%*A1*10       16
="Total "&A1+A3  Total 12
=A1/(A3-4)       #DIV/0!
=A2+"a"          #VALUE!

After Delete Sheet Columns on column B
  the actual figures       now in column B
  the difference formula   now in C2
  formula bar              =B2-#REF!
  the cell                 #REF!
  repair                   Ctrl+Z at once, or retype the planned column
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The nine returned values, errors included | 4 |
| Explains why `=-A4^2` is 9 and `=2^A4^2` is 64 | 2 |
| Says the concatenation runs after the addition | 1 |
| The formula lands in C2 and reads `=B2-#REF!` | 2 |
| Names the repair and says Excel will not restore the reference on its own | 1 |

**Most common mistake**

Answering -9 for `=-A4^2`. School algebra reads that as the negative of three squared. Excel ranks the minus sign of a negative above the exponent, squares the negative and answers 9. The same student almost always answers 512 for `=2^A4^2`, having read it right to left.

### 03.2 · Apply

**Solution**

The formula is `=$E2*F$1`. The dollar sits on the column letter of the price, so filling right never leaves column E, and on the row number of the quantity, so filling down never leaves row 1. Four presses of F4 walk the whole cycle and land back where they started, so the trick is stopping on the second and third forms rather than on the first or the fourth.

The quantities come out of the Series dialog with Series in Rows, Type Linear and a Step value of 10. Nothing appears at the end of the block, and that absence is the record of the route.

The name has to be built from Define Name, because the Name Box offers no Scope box and no Comment box and never shows the Refers to it built. Scoped to the sheet Grid, the name is invisible from any other sheet and absent from the Go To list unless Grid is the active sheet, which is itself worth having the students see once.

On the auditing, the first click draws two arrows into I5, one from E5 and one from I1. The second click adds nothing, because both of those cells hold typed constants and a constant has no precedents. That is the correct answer and not a failed step.

**Output**

```text
F1:I1    10    20    30    40        no Auto Fill Options button
F2       =$E2*F$1

           10        20        30        40
12.50    125.00    250.00    375.00    500.00
18.00    180.00    360.00    540.00    720.00
24.75    247.50    495.00    742.50    990.00
31.20    312.00    624.00    936.00  1,248.00

I5 formula bar        =$E5*I$1
Trace Precedents      first click, two arrows, from E5 and from I1
                      second click, nothing, both sources are constants
Name Manager          name Quantities, scope Grid, refers to =Grid!$F$1:$I$1
Name Box after F5     Quantities
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| One formula fills all sixteen cells and I5 reads `=$E5*I$1` | 3 |
| The four corner values are right | 2 |
| The quantities came from the Series dialog, with no options button left behind | 1 |
| The name carries the sheet scope, the comment and an absolute Refers to | 2 |
| Go To selects the range and the Name Box then reads the name | 1 |
| Two precedent arrows on I5, and only the precedent arrows removed | 1 |

**Most common mistake**

Writing `=$E$2*$F$1`. All sixteen cells then return 125.00, the formula is perfectly valid and nothing warns you. Click I5 and read the formula bar before handing in: one dollar belongs on the E and one on the 1, never both on both.

### 03.3 · Integrate

**Solution**

Six formulas, written once in row 7 and filled down.

```excel
F7  =B7*D7
G7  =B7*E7
H7  =G7*$B$4
I7  =G7-H7
J7  =I7-F7
K7  =J7/I7
```

Only the discount rate needs locking, because it is the only reference that must not travel. The other five all move with the fill, which is what makes them right.

On the Find. Look in set to Formulas searches the text Excel stores, so `$B$4` is found in all fourteen cells of column H. Look in set to Values searches what the cells display, and no cell on that sheet displays the characters `$B$4`, so the count drops to zero. That is the whole difference between the two entries, and it is why a search for `B4` finds nothing either way: the stored text is `$B$4` and there is a dollar sign between the B and the 4.

On the arrows. J20 reads I20 and F20, so the first click draws two. I20 comes from G20 and H20 and F20 comes from B20 and D20, so the second click adds four more and the second generation is on screen.

Grouping writes one edit onto both sheets at once. Ungrouping before doing anything else is the step people forget, and the cost is a stray entry landing on the Precedence sheet.

**Output**

```text
row   Total Cost  Total Revenue  Discount  Net Revenue  Earnings      %
  7     1,440.00       1,600.00    160.00     1,440.00      0.00    0.0%
  8     5,440.00       5,600.00    560.00     5,040.00   -400.00   -7.9%
  9     1,100.00       1,540.00    154.00     1,386.00    286.00   20.6%
 10     1,600.00       2,400.00    240.00     2,160.00    560.00   25.9%
 11     2,700.00       5,400.00    540.00     4,860.00  2,160.00   44.4%
 12     2,800.00       2,940.00    294.00     2,646.00   -154.00   -5.8%
 13        30.00          45.00      4.50        40.50     10.50   25.9%
 14       150.00         200.00     20.00       180.00     30.00   16.7%
 15         9.00          18.00      1.80        16.20      7.20   44.4%
 16       162.00         180.00     18.00       162.00      0.00    0.0%
 17       850.00       1,700.00    170.00     1,530.00    680.00   44.4%
 18       234.00         540.00     54.00       486.00    252.00   51.9%
 19       290.00         500.00     50.00       450.00    160.00   35.6%
 20     4,500.00       5,400.00    540.00     4,860.00    360.00    7.4%

Find All, $B$4, Look in Formulas, Within Sheet    14 cells, H7 to H20
Find All, $B$4, Look in Values,   Within Sheet    0 cells

Trace Precedents on J20    first click  2 arrows, from I20 and F20
                           second click 4 more, from G20, H20, B20 and D20
Watch Window               Book, Sheet, Name, Cell, Value, Formula
                           Exercise 5 Excel.xlsx · Earnings · · K20 · 7.4% · =J20/I20
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Six columns, one formula each, filled down, and no function anywhere | 3 |
| B4 locked with F4, and column H right on all fourteen rows | 2 |
| The heading block came from one trip through Ctrl+1, and the number formats from the Number group | 2 |
| Find All reports 14 under Formulas and 0 under Values, with the reason | 2 |
| Two generations of precedent arrows on J20, and a watch on K20 | 1 |

**Most common mistake**

Writing the discount as `=G7*B4` and filling down. Row 8 multiplies by the empty B5 and returns zero. Row 9 multiplies by the text in B6 and returns `#VALUE!`. Row 10 multiplies by the quantity in B7 and returns a discount of 19,200 against a sale of 2,400. Three different wrong answers out of one missing pair of dollar signs, and only the third one looks wrong at a glance.

---

## Week 04 · Sessions 7 and 8 · Statistical, text and date

### 04.1 · Recognise

**Solution**

COUNT takes numbers, COUNTA takes anything that is not empty, COUNTBLANK takes the empty and the empty-looking. Over H3:H9 the first two agree at 4, because every non-empty cell in that column holds a number and there is nothing there for COUNTA to find that COUNT cannot. In the four-cell example from class one of the cells held a formula returning an empty string, which COUNTA counts as content and COUNTBLANK counts as blank, so the two answers added up past the size of the range. There is no such cell here, so 4 and 3 add to exactly 7.

Column B is the trap. It is headed Registration number, it sits in a numeric position and it holds exactly one value, in B3. COUNT answers 1.

The two LEN results are the point of the exercise. `DUARTE, Alberto` is fifteen visible characters and LEN answers 16, so the cell carries a trailing space. `NUÑEZ, Cecilia` is fourteen and LEN answers 14, so that one is clean. The column is dirty in six rows out of seven, which is worse than a column dirty in all seven: a lookup keyed on it in week 13 will match one row and return `#N/A` for the rest, and the one that worked will make the failure look like a data problem rather than a spacing problem.

Reported as they come out of the dialog, AVERAGE returns 2202.857142857 and is shown here at two decimals.

**Output**

```text
COUNT(H3:H9)        4
COUNTA(H3:H9)       4
COUNTBLANK(H3:H9)   3
COUNT(B3:B9)        1

SUM(F3:F9)          15,420
AVERAGE(F3:F9)      2,202.86
MAX(F3:F9)          4,500
MIN(F3:F9)          780
LARGE(F3:F9,2)      4,000
SMALL(F3:F9,2)      890

LEN(C3)             16      fifteen characters showing, one trailing space
LEN(C6)             14      fourteen showing, clean
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three counts over H3:H9, with the reason the first two agree | 3 |
| COUNT(B3:B9) answers 1 | 1 |
| SUM, AVERAGE, MAX and MIN | 2 |
| LARGE with a k of 2 is 4,000 and SMALL with a k of 2 is 890 | 2 |
| The two LEN answers, and what the extra character will cost in week 13 | 2 |

**Most common mistake**

Answering 7 for `COUNT(B3:B9)` because the column is headed Registration number and reads as a numeric column. Only B3 was ever filled in. The heading is not data, and COUNT has nothing to count in the six cells below it.

### 04.2 · Apply

**Solution**

Row 3 is jennifer, lópez, pérez, born 6 July 2001, with the ID `024300` stored as text.

```excel
G3  =CONCAT(C3," ",D3," ",E3)
H3  =UPPER(G3)
I3  =PROPER(G3)
J3  =TEXTJOIN(".",TRUE,LEFT(C3,1),D3,LEFT(E3,1))
P3  =LEFT(B3,3)
Q3  =RIGHT(B3,3)
R3  =MID(B3,4,2)
S3  =LEN(G3)
L3  =DAY(F3)
M3  =MONTH(F3)
N3  =YEAR(F3)
U3  =LEFT(T3,3)
V3  =F3*1
```

MID counts from 1 at the first character, so a `Start_num` of 4 lands on the fourth digit and takes two.

Step 7 is the one worth the class time. T3 holds the number 24300 and the code `000000` pads the picture to six digits, so the cell shows `024300` and looks the same as B3. LEFT does not read the picture. It reads the stored value, converts 24300 to the text `24300`, and returns `243`. That is why the ID column in this file was typed as text in the first place, and it is the cleanest demonstration in the course of a format changing nothing but the display.

Step 9. On the professor's build the interface is English and the install language is Spanish Mexico, so the year code is `aaaa` and not `yyyy`. Writing `dd/mmmm/yyyy` prints the letters y-y-y-y literally. The code is `dd/mmmm/aaaa`, and the month name comes back in Spanish for the same reason. On an English install the same result needs `dd/mmmm/yyyy`, so this is one of the settings to check on the lab machines before the exercise is set.

**Output**

```text
G3   jennifer lópez pérez
H3   JENNIFER LÓPEZ PÉREZ
I3   Jennifer López Pérez
J3   j.lópez.p

P3   024        LEFT over the text in B3
Q3   300
R3   30
S3   20

L3   6      M3   7      N3   2001
V3   37078          the serial number behind 06/07/2001

T3   shows 024300, formula bar reads 24300
U3   243            LEFT read the value, not the picture

F3   06/julio/2001  from the custom code dd/mmmm/aaaa
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| G, H and I built with CONCAT, UPPER and PROPER through the dialog and filled to row 62 | 2 |
| TEXTJOIN carries the full stop and `Ignore_empty` set to TRUE | 1 |
| LEFT, RIGHT and MID return 024, 300 and 30 | 2 |
| DAY, MONTH and YEAR return 6, 7 and 2001, and `=F3*1` returns 37078 | 2 |
| The code `000000` shows 024300 while the formula bar still reads 24300 | 1 |
| U3 returns 243, with the difference from P3 explained | 1 |
| The date column carries a custom code, and the year code is named correctly for this build | 1 |

**Most common mistake**

Expecting U3 to read `024` because the cell above it shows `024300`. LEFT reads the stored value and the stored value is twenty-four thousand three hundred. Students who get this wrong usually also propose fixing the ID column by formatting it, which is the same error one step further on.

### 04.3 · Integrate

**Solution**

```excel
I22  =SUM(Net_Revenue)
I23  =I22*$B$3
I24  =I22+I23
I25  =SUM(Line_Earnings)
K22  =TODAY()
```

The names have to be built from Define Name, because the task asks for a sheet scope and the Name Box always scopes to the workbook. Once they exist, Formula AutoComplete offers them with a tag icon after two or three letters, and Tab inserts them; F3 opens the Paste Name dialog for the same job. The formula bar is the only place the difference between `=SUM(Net_Revenue)` and `=SUM(I7:I20)` shows, which is exactly where the marking happens.

The custom code is `#,##0.00;[Red](#,##0.00);"-"`. Three sections, in the order positive, negative, zero. The way to build it is to set the Number category first with two decimals and the 1000 separator, then click Custom, because the Type box arrives holding the code Excel just wrote and there is less to type and less to get wrong.

Column J is a good place to see all three sections working at once. Rows 7 and 16 come out at exactly zero and take the third section, so both show a dash. Rows 8 and 12 are negative and take the second, so both show red parentheses. The other ten take the first.

TODAY and Ctrl+semicolon are indistinguishable on the day they are entered. K22 reads `=TODAY()` in the formula bar and moves with the calendar. K23 reads a fixed date and will still be showing 18 August 2026 in November.

**Output**

```text
I22   SUBTOTAL          25,256.70
I23   VAT                4,041.07
I24   TOTAL             29,297.77
I25   TOTAL EARNINGS     3,951.70

Name Manager, name / scope / refers to
  Net_Revenue      Earnings   =Earnings!$I$7:$I$20
  Line_Earnings    Earnings   =Earnings!$J$7:$J$20

Column J under the custom code
  J7    -              zero, third section
  J8    (400.00)       red, second section
  J12   (154.00)       red, second section
  J16   -              zero, third section
  the other ten rows   plain, first section

K22   =TODAY()       moves every time the file is opened
K23   18/08/2026     a stamp, and it never moves again
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both names carry the sheet scope and an absolute Refers to | 2 |
| The four totals are right and the formulas show the names, not the addresses | 3 |
| SUM went in through the Function Arguments dialog, and B3 is locked with F4 | 1 |
| The custom code has three sections and column J shows a dash on rows 7 and 16 | 2 |
| Red parentheses on rows 8 and 12, named in the answer | 1 |
| K22 reads `=TODAY()` in the formula bar and K23 holds a fixed date | 1 |

**Most common mistake**

Writing `=SUM(I7:I20)`. The number is right, the sheet looks finished, and the item is not answered, because it asked for the defined name. Nothing on screen gives it away. The only place it shows is the formula bar, and a student who never reads the formula bar on their own work will lose this one every time it is asked.

---

## Week 05 · Rules, sparklines and IF

### 05.1 · Recognise

**Solution**

Rule 1 matches B2, B5 and B7, and because Stop If True is ticked on it, nothing below it is evaluated for those three cells. Rules 2 and 3 are left to decide the other three.

| Cell | Rule 1 | Rule 2 | Rule 3 | What shows |
|---|---|---|---|---|
| B2 · 5000 | TRUE, stop | not read | not read | Green fill |
| B3 · 2000 | FALSE | FALSE, row 3 is odd | FALSE, 2000 is not below 2000 | Nothing |
| B4 · 1500 | FALSE | TRUE | TRUE | Yellow fill and red font |
| B5 · 4500 | TRUE, stop | not read | not read | Green fill |
| B6 · 1200 | FALSE | TRUE | TRUE | Yellow fill and red font |
| B7 · 7000 | TRUE, stop | not read | not read | Green fill |

Rules 2 and 3 both fire on B4 and B6 and both are applied, because one sets the fill and the other sets the font. Two rules only compete when they set the same property.

With D1 as the active cell the manager opens on Current Selection and lists nothing, since D1 carries no rule. The rules have not gone anywhere. Set Show formatting rules for to This Worksheet and all three come back, in priority order.

Clearing Stop If True on rule 1 changes nothing on the sheet. B5 and B7 sit on odd rows, so rule 2 is FALSE there anyway, and neither amount is below 2000. B2 sits on row 2, so rule 2 does become live for it, but rule 2 sets the fill and rule 1 already set the fill from a higher priority, so green still wins.

**Output**

```text
Cell   Amount   Fill      Font
B2      5000    green     black
B3      2000    none      black
B4      1500    yellow    red
B5      4500    green     black
B6      1200    yellow    red
B7      7000    green     black

Manage Rules with D1 active     empty list
After This Worksheet            three rules, priorities 1, 2, 3
Stop If True cleared on rule 1  no cell changes
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six fills, and the red font on B4 and B6 only | 3 |
| Says B4 and B6 take both rules, because fill and font are different properties | 2 |
| Explains the empty list and names This Worksheet as the fix | 2 |
| Answers that no cell changes when Stop If True is cleared | 2 |
| Gives the reason for B2 in particular: same property, higher priority wins | 1 |

**Most common mistake**

Answering that B2 turns yellow once Stop If True is cleared. It reads Stop If True as the only thing holding rule 2 back, when priority was already doing that job. The giveaway is an answer that changes B2 and leaves B5 and B7 alone without saying why the three behave differently.

### 05.2 · Apply

**Solution**

Step 2 makes a Cell Value rule whose threshold is a reference rather than a number. Select the rule in the manager, click Edit Rule..., and the value box holds `=$W$2`, absolute because the collapse arrow always hands back an absolute reference. That is the point of the step: with 85 typed into the dialog instead, moving the cut would mean reopening Edit Rule every time.

Step 3 makes the rule that no exercise in the pack builds. The formula is written once for A4, the active cell, and Excel shifts it across the other 359 cells the same way it shifts a copied formula. `$B4` holds the column still and lets the row walk, so all twelve cells of a row are decided by that row's status.

The counts, on this file:

| Threshold in W2 | Cells painted, out of the 295 that hold a number |
|---|---|
| 85 | 105 |
| 65 | 213 |

Every grade in the sheet is a multiple of ten, so `>85` and `>=90` pick exactly the same 105 cells, and `>65` and `>=70` pick the same 213. C4 holds 50 and is painted at neither threshold.

C4:L33 is 300 cells and five of them, H13:L13, are empty, which is why the denominator is 295. An empty cell is not greater than 85 and not greater than 65 either, so those five never take the fill. That is worth knowing before a task asks for a rule over a column with gaps in it.

**Output**

```text
C4  = 50    not painted at 85, and not painted at 65 either
C5  = 100   green fill, dark green text
L4  = 100   green fill, dark green text
H13:L13     empty, never painted, at any threshold

Manage Rules, This Worksheet
  the formula rule      Formula: =$B4="International"   Applies to  =$A$4:$L$33
  the threshold rule    a Cell Value rule reading =$W$2 Applies to  =$C$4:$L$33

Rows painted by the formula rule   16 of 30, so 192 cells over columns A to L
Cells painted by the threshold rule   105 with W2 = 85, 213 with W2 = 65
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The threshold points at W2 through the collapse arrow, not typed into the dialog | 2 |
| The formula rule was written from New Rule with the sixth rule type, and F2 pressed first | 2 |
| The formula reads `=$B4="International"`, with the column locked and the row free | 2 |
| Font and fill were set in one visit to the Format... dialog | 1 |
| The two Applies to ranges are quoted from the manager, set to This Worksheet | 2 |
| Says the five empty cells of row 13 are never painted | 1 |

**Most common mistake**

Locking both halves of the reference. `=$B$4="International"` keeps asking about one student for all 360 cells, and since B4 holds Local the block stays plain, which reads as a rule that failed rather than a rule that is wrong. Write the same mistake one row down, `=$B$5="International"`, and every cell in the block turns colour instead. The other version is `=B4="International"`, which walks the column as well as the row and paints a scatter with no pattern in it. All three are caught in four seconds by copying the formula into a spare cell beside A4 and dragging it down: it has to read TRUE on exactly the rows that are coloured.

### 05.3 · Integrate

**Solution**

```excel
G3   =AVERAGE(C3:E3)
H3   =IF(G3>=Cut,"Above","Below")
I3   Above          a constant, left by Paste Special
```

`Cut` is a defined name, so it does not move when H3 is filled to H32. That is the week 3 reason for using a name rather than a cell reference here: F4 would have done the same job, and the name also says what the number is for.

The averages this sheet produces are unusually flat.

| Average | Students |
|---|---|
| 60.00 | 1 |
| 70.00 | 8 |
| 80.00 | 18 |
| 90.00 | 1 |
| 96.67 | 2 |

Eighteen of the thirty students average exactly 80, which is the boundary. So `>=` and `>` do not differ by one row here, they differ by eighteen. Carolina Dubois scores 80, 70 and 90, averages 80, and is the first of the eighteen to move.

The sparkline check is the pair the objective is built on. Click F3 and the formula bar stays empty, because a sparkline is drawn into the cell background and is not a cell value, and the Sparkline contextual tab appears on the ribbon. Click I3 and the formula bar holds the word Above with no equals sign, because Paste Special, Values discards the formula and keeps the result.

Without Axis, Same for All Sparklines, each of the thirty rows is scaled to its own three numbers, so a student who went 60, 50, 70 draws the same picture as one who went 100, 90, 100. The column is then decorative and the comparison it was inserted to support cannot be made. The task is asking for the scale, not for the drawing.

**Output**

```text
G3 = 80.00      H3 = Above       Carolina Dubois, 80 / 70 / 90

With  G3>=Cut     Above 21    Below  9
With  G3>Cut      Above  3    Below 27
Students sitting exactly on 80:  18

Formula bar on F3   empty, and the Sparkline tab is on the ribbon
Formula bar on I3   Above, a constant with no equals sign
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `Cut` was made from Define Name with Scope set to Workbook, not from the Name Box | 1 |
| AVERAGE and IF were both built through Function Arguments, and IF points at the name | 2 |
| The two counts, 21 and 9, and the two after the operator is changed, 3 and 27 | 2 |
| Says eighteen students sit on the boundary, and names one of them | 1 |
| The sparklines were made from Create Sparklines with Location Range `$F$3:$F$32` | 1 |
| Axis, Same for All Sparklines is set on both the minimum and the maximum | 2 |
| Column I was written with Paste Special, Values, and the formula bar proves it | 1 |

**Most common mistake**

Inserting a small line chart per row and dragging it over the cells. It looks close on screen, it belongs to the chart domain rather than this one, and it fails both halves of the ten second check: the formula bar shows selection handles and Chart Design instead of an empty bar and a Sparkline tab, and the objects stay on top of the grid when the rows are sorted.

---

## Week 06 · IF in depth, then the midterm

### 06.1 · Recognise

**Solution**

C2 holds the number 70. C3 holds the two characters 7 and 0 as text, which Excel ranks above every number that exists.

| Formula | Cell shows | Why |
|---|---|---|
| `=IF(C2>=70,"Pass","Fail")` | Pass | 70 is not below 70 |
| `=IF(C2>70,"Pass","Fail")` | Fail | the boundary row, and the only row where these two differ |
| `=IF(C2<>70,"Pass","Fail")` | Fail | they are equal, so not equal is FALSE |
| `=IF(C2>=70,"Pass")` | Pass | the test is TRUE, so the missing argument never comes up |
| `=IF(C2>=80,"Pass")` | FALSE | the test is FALSE and there is no third argument to return |
| `=IF(C2>="70","Pass","Fail")` | Fail | a number against text: numbers come first, text after them |
| `=IF(C3>=70,"Pass","Fail")` | Pass | text against a number, and the text wins for the same reason |

FALSE is the word no report wants, and it comes from the fifth formula. Nothing is flagged and no error is raised: leaving the third argument out is legal, and Excel fills the gap with the logical value FALSE.

The screen tells C2 from C3 before any formula is written. Excel right aligns numbers and left aligns text on its own, so C2 sits against the right edge of its cell and C3 against the left. The tool that flags the same thing with a green triangle, the numbers formatted as text rule, arrives next week.

**Output**

```text
C2 = 70 as a number, right aligned
C3 = 70 as text, left aligned

  =IF(C2>=70,"Pass","Fail")      Pass
  =IF(C2>70,"Pass","Fail")       Fail
  =IF(C2<>70,"Pass","Fail")      Fail
  =IF(C2>=70,"Pass")             Pass
  =IF(C2>=80,"Pass")             FALSE
  =IF(C2>="70","Pass","Fail")    Fail
  =IF(C3>=70,"Pass","Fail")      Pass
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The first four answers | 3 |
| FALSE on the fifth, named as the missing third argument rather than as an error | 2 |
| Fail on the sixth, with the three bands as the reason | 2 |
| Pass on the seventh, and it is the same reason read the other way round | 1 |
| Names alignment as the check that needs no formula | 2 |

**Most common mistake**

Answering Pass to the sixth, on the grounds that Excel converts the text and compares the numbers. It never does that in a comparison. The same belief turns a column imported as text into a report where every row answers the same way and nothing is flagged anywhere, which is why the deck spends a slide on it.

### 06.2 · Apply

**Solution**

```excel
D8   =IF(C8="Credit Card",B8*(1+$D$4),B8*(1-$D$5))
```

Neither answer is a word. Value_if_true is the list price plus the fee and Value_if_false is the list price less the discount, so the whole rule is two calculations with one test between them.

| Row | Item | List price | Method | D |
|---|---|---|---|---|
| 8 | A 1 | 50 | Credit Card | 55.00 |
| 9 | A 2 | 32 | Cash | 30.40 |
| 10 | A 3 | 18 | Cash | 17.10 |
| 11 | A 4 | 125 | Credit Card | 137.50 |
| 12 | A 5 | 230 | Credit Card | 253.00 |
| 13 | A 6 | 48 | Credit Card | 52.80 |
| 14 | A 7 | 44 | Cash | 41.80 |
| 15 | A 8 | 20 | Cash | 19.00 |
| 16 | A 9 | 12 | Cash | 11.40 |
| 17 | A 10 | 140 | Credit Card | 154.00 |

Without F4 the two rates walk down with the formula, and the column fails in two different ways within two rows of each other.

D9 becomes `=IF(C9="Credit Card",B9*(1+D5),B9*(1-D6))`. The method is Cash, so the false branch runs, and D6 is empty. An empty cell counts as zero, so the row returns 32.00, the list price with nothing taken off, and it looks like a perfectly ordinary number.

D10 becomes `=IF(C10="Credit Card",B10*(1+D6),B10*(1-D7))`. The method is Cash again, and D7 holds the heading Total Sales price. One minus a piece of text is `#VALUE!`, so this row does complain.

Two rows further down it gets worse: D12 is a card row and its true branch has landed on D8, which by then holds 55, so the cell returns 12880.00. The error at D10 is the lucky one. The silent 32.00 at D9 is the reason the objective grades the reference and not the picture.

**Output**

```text
D8   55.00     D13   52.80
D9   30.40     D14   41.80
D10  17.10     D15   19.00
D11  137.50    D16   11.40
D12  253.00    D17  154.00

Total of D8:D17            772.00

Without F4
  D9    32.00      the false branch reads the empty D6, no error raised
  D10   #VALUE!    the false branch reads the heading in D7
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The formula was built from Formulas, Logical, IF and not typed into the cell | 2 |
| Both branches are calculations that read B8, D4 and D5 | 2 |
| `$D$4` and `$D$5`, locked with F4 before the fill | 2 |
| The ten values and the total of 772.00 | 2 |
| D9 returns 32.00 with no error, and says why an empty cell produces it | 1 |
| D10 returns `#VALUE!`, and names the heading in D7 as the cause | 1 |

**Most common mistake**

Typing 0.1 and 0.05 into the formula instead of pointing at D4 and D5. It fills down correctly, it gives all ten right answers, and it fails the objective, because the fee now lives in ten formulas rather than in one cell. The check is to change D4 to 0.2 and watch: the column has to move on its own.

### 06.3 · Integrate

**Solution**

| Row | Student | Grades | E, two decimals | F, `<=5.9` | G, `<=6` |
|---|---|---|---|---|---|
| 2 | a | 5, 5, 5 | 5.00 | Fail | Fail |
| 3 | b | 9, 6, 6 | 7.00 | Pass | Pass |
| 4 | c | 8, 5, 8 | 7.00 | Pass | Pass |
| 5 | d | 7, 7, 5 | 6.33 | Pass | Pass |
| 6 | e | 10, 5, 8 | 7.67 | Pass | Pass |
| 7 | f | 10, 5, 5 | 6.67 | Pass | Pass |
| 8 | g | 9, 5, 6 | 6.67 | Pass | Pass |
| 9 | h | 6, 6, 6 | 6.00 | Pass | Fail |

Row 9 is the only disagreement, and it exists because the eighth student was added to produce it.

Three whole grades add up to a whole number, so the average is always a multiple of one third. Going up from 5, the reachable averages are 5.0000, 5.3333, 5.6667 and then 6.0000. Nothing this sheet can produce lands strictly between 5.9 and 6, so `<=5.9` and `<6` return the same word on every row that can ever exist here, and swapping one for the other proves nothing. `<=6` is a different test: it takes in the averages that are exactly 6, and row 9 is one of them. A boundary is only worth testing where a value can sit on it.

The formula rule reads `=$F2="Fail"` over `A2:G9`. Column F is locked and the row is free, so one column decides seven cells at a time. Only row 2 says Fail, so it paints seven cells, A2 to G2, and no others. Change B2 from 5 to 8 and the paint leaves row 2 on its own, which is the ten second proof that the colour came from the rule.

**Output**

```text
Averages   a 5.00   b 7.00   c 7.00   d 6.33
           e 7.67   f 6.67   g 6.67   h 6.00

F and G agree on rows 2 to 8
F and G disagree on row 9 only     F = Pass, G = Fail

Rule painted     1 row, 7 cells, A2:G2
Applies to       =$A$2:$G$9
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Row 9 added and both status columns filled to it | 1 |
| The eight averages, to two decimals set from Ctrl+1 and not from the Home tab | 2 |
| Row 9 named as the only disagreement, with Pass in F and Fail in G | 2 |
| The argument about multiples of one third, or an equivalent one | 2 |
| `=$F2="Fail"`, one rule over `A2:G9`, with the column locked | 2 |
| Applies to quoted from the manager with the list set to This Worksheet | 1 |

**Most common mistake**

Writing seven rules, one per column, because the rule was built with only column A selected and then remade six times. The manager gives it away at once: seven entries with the same description and seven one-column Applies to ranges, where the task wanted one entry reading `=$A$2:$G$9`.

---

## Week 07 · Compound conditions

### 07.1 · Recognise

**Solution**

The tests are read from the top down and the first TRUE wins, so a staircase written from the bottom up catches everything on its first step.

| Score | The formula returns | The band says | Same |
|---|---|---|---|
| 162 | Low | Low | yes |
| 847 | Average | Good | no |
| 546 | Average | Average | yes |
| 325 | Low | Low | yes |
| 902 | Average | Excellent | no |

Twelve of the thirty rows are wrong: the five Excellent scores and the seven Good ones, all of them caught by `A2>=500` before they ever reach the test that was written for them. Good and Excellent do not appear anywhere in column B. The column holds Low on nine rows and Average on the other twenty one, and it looks entirely reasonable.

Excel raises nothing at all. There is no error value, because every branch returns text. There is no green triangle either: the formula in B3 is consistent with the formulas above and below it, which is precisely the rule that would have caught a nest pasted one row short.

Evaluate Formula on B3 underlines `A3` first. A reference is resolved before anything else, which is the first line of the precedence table. One click of Evaluate replaces it with `847` in italic and moves the underline onto `847>=500`. The click after that turns the comparison into TRUE, and the click after that collapses the whole IF to `"Average"`, at which point the two inner IFs are discarded without ever being worked out.

**Output**

```text
162   Low         847   Average      546   Average
325   Low         902   Average

Rows wrong                       12 of 30
Ratings that never appear        Good, Excellent
Column B holds                   Low on 9 rows, Average on 21
Flagged by Excel                 nothing, no error and no triangle

Evaluate Formula on B3
  step 1   A3 underlined
  step 2   847 in italic, 847>=500 underlined
  step 3   TRUE
  step 4   "Average"
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five answers, with 847 and 902 both coming out as Average | 3 |
| Twelve wrong rows, and the two ratings that never appear | 2 |
| The distribution of the column, 9 and 21 | 1 |
| Says Excel raises nothing, and gives a reason for both the error and the triangle | 2 |
| `A3` underlined first, with the reference-before-everything reason | 2 |

**Most common mistake**

Answering that the formula returns an error, or that it flags the overlap between the tests. The tests do overlap and Excel has no objection to that. A staircase in the wrong order is a full column of wrong answers with a clean bill of health, which is why it is checked at the boundaries and not by looking for red.

### 07.2 · Apply

**Solution**

```excel
C2   =IF(A2>=900,"Excellent",IF(A2>=750,"Good",IF(A2>=500,"Average","Low")))

D2   =IFS(A2>=900,"Excellent",A2>=750,"Good",A2>=500,"Average",TRUE,"Low")
```

Both agree on all thirty rows.

| Rating | Rows |
|---|---|
| Excellent | 5 |
| Good | 7 |
| Average | 9 |
| Low | 9 |

The last pair of the IFS carries the default. `TRUE` is not a test that reads anything on the sheet, it is the value TRUE, so it always matches and anything that got that far takes Low. Take the pair out and IFS has nothing left to return for a value that matched no test, and it answers `#N/A`. Over this data that is the nine scores below 500, which is a third of the column.

On a build older than Office 2019 the formula in column D comes back as `_xlfn.IFS(...)` and the cell shows `#NAME?`. The nested IF in column C opens anywhere.

The route is the graded part. Shift+F3 on C5 has to reopen Function Arguments on the outer IF, with `A5>=900` in Logical_test, `Excellent` in Value_if_true and the next IF sitting inside Value_if_false. If instead the whole formula appears inside the first box, the nest was typed as a string of text and a grader that reparses the file will mark it down.

**Output**

```text
Column C, nested IF     Column D, IFS       Agree on all 30 rows

Excellent   5
Good        7
Average     9
Low         9

Without the TRUE pair, column D returns #N/A on the 9 scores below 500
On a pre-2019 build, column D reads _xlfn.IFS and shows #NAME?
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Column C was nested from the Name Box, with one OK at the outer level | 2 |
| Shift+F3 reopens on the outer IF with all three boxes filled | 1 |
| The nested IF is in the right order and returns the four bands | 2 |
| Column D uses IFS with four pairs, built from Formulas, Logical, IFS | 2 |
| The four counts, and both columns agreeing on all thirty rows | 1 |
| Explains the `TRUE` pair and names `#N/A` on the nine rows without it | 2 |

**Most common mistake**

Clicking OK on each inner dialog. Every OK writes what is in front of it into the cell and closes the whole thing, so the second level ends up in its own cell or, worse, replaces the outer formula. One OK, at the outer level, after every box on every level is filled.

### 07.3 · Integrate

**Solution**

| Criterion | Count | What it caught |
|---|---|---|
| `Tlal*` | 2 | Tlalpan, Tlaltenango |
| `Tla*` | 3 | the two above and Tlahuac |
| `*co` | 6 | Azcapozalco, Coacalco, Cuicuilco, Iztacalco, México, Xochimilco |
| `?a*` | 2 | Zacatepec, Zacazonapan |
| `*a?` | 7 | Atocpan, Chiconcuac, Mixcoac, Tequisquiapan, Tlahuac, Tlalpan, Zacazonapan |
| `*pan` | 4 | Atocpan, Tequisquiapan, Tlalpan, Zacazonapan |
| `*x*` | 5 | Ixtapa, México, Mixcoac, Xochimilco, Xola |
| `*z*` | 6 | Azcapozalco, Iztacalco, Iztapalapa, Tepoztán, Zacatepec, Zacazonapan |
| `??a*` | 5 | Coacalco, Cuautitlán, Tlahuac, Tlalpan, Tlaltenango |

Narrowing `Names` to `$A$2:$A$24` changes none of the nine. The heading is inside the range and it is being counted, it just happens that the word LIST matches nothing here. That is luck, not design. Put `Zapata` in A1 instead and two counts move at once: `?a*` goes from 2 to 3, because the second character is an a, and `*z*` goes from 6 to 7, because criteria are matched without regard to case. A range that includes its own heading is a defect waiting for a different heading.

`México` is counted twice, by `*co` and by `*x*`. The one that catches people is `*co`. The criterion was written for the place names that end in the syllable co, and México ends in the letters c and o, so it lands in the same bucket as Azcapozalco. A wildcard has no idea what a syllable is.

The rule `=$A2="Tla*"` paints nothing, and it raises nothing either. The equals sign compares letter for letter, so it is asking for a cell holding the four characters T, l, a and an asterisk, and no cell does. Wildcards are read only where an argument decides to read them as a pattern, and a comparison is never one of those places. Neither is the logical test of an IF.

`=COUNTIF($A2,"Tla*")>0` paints three cells, A16, A17 and A18. COUNTIF over a single cell answers 1 or 0, and the criteria argument is one of the arguments that does read wildcards. The Rules Manager lists one rule with `Applies to` reading `=$A$2:$A$24`, not three rules and not one per matching cell.

**Output**

```text
Tlal*  2      Tla*  3      *co   6
?a*    2      *a?   7      *pan  4
*x*    5      *z*   6      ??a*  5

Names as $A$2:$A$24      no count changes
A1 holding Zapata        ?a* goes 2 to 3,  *z* goes 6 to 7
México counted by        *co and *x*

Formula rule  =$A2="Tla*"              0 cells painted
Formula rule  =COUNTIF($A2,"Tla*")>0   3 cells painted, A16:A18
Applies to                             =$A$2:$A$24
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The nine counts | 3 |
| Says the heading changes nothing here, and what `Zapata` would move | 1 |
| `México` caught by `*co` and `*x*`, with the syllable point made | 1 |
| The comparison rule paints nothing, with wildcards needing a reader as the reason | 2 |
| The COUNTIF rule was written from New Rule with the sixth type and paints three cells | 2 |
| The failed rule was taken out with Delete Rule, and Applies to is quoted from the manager | 1 |

**Most common mistake**

Explaining the empty rule by saying the formula needs an equals sign, or quotation marks, or a dollar sign somewhere. The formula is well formed and Excel evaluates it happily thirty times, returning FALSE each time. Nothing about the syntax is wrong. What is wrong is the belief that an asterisk means something to every part of Excel, and the way to see it is to put `=$A16="Tla*"` in a spare cell and read FALSE back next to a name that plainly starts with Tla.

---

## Week 08 · Conditional aggregates

### 08.1 · Recognise

**Solution**

| Formula | Returns | The fault |
|---|---|---|
| `=SUMIF(C4:C33,"Jan",A4:A33)` | 0 | Range and Sum_range swapped |
| `=SUMIF(A4:A33,"Jan",C4:C33)` | 16500 | none, this is the one |
| `=SUMIF(A4:A33,"Jan",C4:C500)` | 16500 | ranges of different heights |
| `=SUMIFS(A4:A33,C4:C33,"Jan")` | 0 | the plural form puts the aggregated range first |
| `=AVERAGEIF(A4:A33,"Apr",C4:C33)` | `#DIV/0!` | no matching row, and a mean over nothing is an error |

The first tests the deposit column for the text Jan. No deposit is equal to a month name, so nothing matches, and the range it would have added holds month names anyway. Zero comes back with no complaint.

The fourth is the same accident in the plural family. SUMIFS adds its first argument, so this one is asking for the total of the month column on the rows whose deposit equals Jan. Nothing matches and it also returns zero.

Those two are the ones that hand a reader a number with no way of telling it is wrong. A zero in a total column reads as a real total, and it is copied into a report long before anyone questions it. The `#DIV/0!` of the fifth is the friendly failure, because it stops the reader.

`=COUNTIF(D4:D33,>1000)` is refused before it is ever calculated: Excel puts up the message that there is a problem with the formula and offers to correct it. A comparison is a criterion, not a value, so it travels as text. `=COUNTIF(D4:D33,">1000")` is accepted and returns 12.

The third formula gives the right answer for the wrong reason. When Sum_range is not the same shape as Range, SUMIF takes its top left cell and reshapes it to the size of Range, so C4:C500 is quietly used as C4:C33. The habit survives until it meets SUMIFS, where the same mismatch returns `#VALUE!` instead of a number.

**Output**

```text
=SUMIF(C4:C33,"Jan",A4:A33)        0
=SUMIF(A4:A33,"Jan",C4:C33)    16500
=SUMIF(A4:A33,"Jan",C4:C500)   16500
=SUMIFS(A4:A33,C4:C33,"Jan")       0
=AVERAGEIF(A4:A33,"Apr",C4:C33)    #DIV/0!

Silently wrong                  the first and the fourth
=COUNTIF(D4:D33,>1000)          refused, the formula will not commit
=COUNTIF(D4:D33,">1000")        12
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five results | 3 |
| Names the swap in the first, and the first-argument rule in the fourth | 2 |
| Picks out the two silent zeros as the dangerous ones | 1 |
| Says the unquoted comparison is refused, not merely wrong | 1 |
| The quoted form returns 12 | 1 |
| Explains the reshaping in the third, and that SUMIFS answers `#VALUE!` instead | 2 |

**Most common mistake**

Marking the fourth formula correct because it has the same three pieces as the second one in the same order. The order is exactly what changed. SUMIF tests first and adds last, SUMIFS adds first and then tests in pairs, and the only place that difference is written down while you work is the Function Arguments dialog.

### 08.2 · Apply

**Solution**

```excel
B37   =SUMIFS($C$4:$C$33,$E$4:$E$33,$A37,$A$4:$A$33,B$36)
B42   =MAXIFS($C$4:$C$33,$A$4:$A$33,B$36,$C$4:$C$33,">0")
B43   =MINIFS($C$4:$C$33,$A$4:$A$33,B$36,$C$4:$C$33,">0")
F38   =COUNTIF($C$4:$C$33,">"&$F$37)
```

One formula fills all twelve cells of the grid. The record ranges are locked in both directions, the branch is `$A37` so it walks down and never leaves column A, and the month is `B$36` so it walks across and never leaves row 36. Those two mixed forms are the week 3 material doing the work.

| Deposits | Jan | Feb | Mar |
|---|---|---|---|
| Bolívar | 4500 | 2000 | 1500 |
| Cuauhtémoc | 0 | 0 | 5300 |
| Díaz Mirón | 12000 | 0 | 8750 |
| Miguel Alemán | 0 | 10500 | 0 |

The three columns add to 16500, 12500 and 15550, which are the same figures the exercise's own questions 2 and 5 produce from a single SUMIF each. That agreement is the check on the whole grid.

| | Jan | Feb | Mar |
|---|---|---|---|
| Largest deposit | 7000 | 5500 | 6250 |
| Smallest deposit | 4500 | 2000 | 1500 |

The second criteria pair on MAXIFS and MINIFS, the column tested against `">0"`, is there because the deposit column is empty on every withdrawal row. Without it the answer depends on how the function decides to treat the twenty empty cells, and a formula whose result you have to look up is not a formula you want in a report.

F38 returns 4 with 5000 in F37, and 8 after F37 is changed to 2000. Nothing inside the formula is edited to make that happen, which is the whole point of the ampersand: the operator is text, it is joined to a reference, and the reference is the only part anybody touches afterwards.

The zero in the Cuauhtémoc row for January is honest. That branch took no deposit at all in January, so SUMIFS added nothing and returned nothing. To tell it apart from the zero a swapped pair of arguments produces, type 100 into C13, whose row is January and Cuauhtémoc: the honest cell moves to 100 straight away, and a formula with its arguments in the wrong order stays at zero whatever you do to the data. Clear C13 afterwards.

**Output**

```text
Deposits          Jan      Feb      Mar
Bolívar          4500     2000     1500
Cuauhtémoc          0        0     5300
Díaz Mirón      12000        0     8750
Miguel Alemán       0    10500        0
                -----    -----    -----
                16500    12500    15550

Largest deposit  7000     5500     6250
Smallest deposit 4500     2000     1500

F38 with F37 = 5000      4
F38 with F37 = 2000      8
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| SUMIFS built from Formulas, Math & Trig, with Sum_range in the first box | 2 |
| `$A37` and `B$36`, so one formula fills all twelve cells | 2 |
| The twelve figures, and the column totals agreeing with questions 2 and 5 | 2 |
| MAXIFS and MINIFS present, from More Functions, Statistical, with the `">0"` pair | 2 |
| F38 built with `">"&$F$37` and no number typed inside the formula | 1 |
| Explains the Cuauhtémoc zero and gives a check that separates it from a swapped pair | 1 |

**Most common mistake**

Writing twelve separate SUMIFS, one per cell, each with its month and branch typed in as text. Every figure comes out right and the block is unusable: a new branch means four more formulas by hand, a renamed month means twelve edits, and the objective was never about the twelve numbers. Fill from one formula, then click any cell in the middle of the block and read the formula bar to prove it.

### 08.3 · Integrate

**Solution**

```excel
H2    =F2*(1-G2)
K3    =COUNTIF($E$2:$E$521,$J3)
K9    =SUMIF($D$2:$D$521,$J9,$H$2:$H$521)
K19   =AVERAGEIF($E$2:$E$521,$J19,$G$2:$G$521)
K25   =COUNTBLANK(G2:G521)
K27   =AVERAGEIF($E$2:$E$521,"<>Rosa",$F$2:$F$521)
K29   =SUM(H2:H521)
K31   =COUNTIFS($A$2:$A$521,">="&$M$1,$A$2:$A$521,"<="&$M$2)
M4    =COUNTIF($D$2:$D$521,"*Detoxifying*")
```

The criterion is `$J3` and not the name typed in, so the same formula fills five rows and reads its question off the sheet. Locking the record ranges and leaving the column of labels relative in the row is the same technique the branch grid used, one dimension smaller.

| Esthetician | Treatments | Average discount | Taken over |
|---|---|---|---|
| Ana | 97 | 0.0576 | 91 rows |
| Camila | 100 | 0.0515 | 94 rows |
| María | 115 | 0.0494 | 108 rows |
| Rafaella | 97 | 0.0576 | 85 rows |
| Rosa | 111 | 0.0579 | 104 rows |

The five counts add to 520, which is the check that no record was left outside a range. The rule `=$K3=MAX($K$3:$K$7)` paints K5 and nothing else, since María is the only maximum.

The last column of that table is the part worth reading twice. AVERAGEIF ignores the empty cells of Average_range, so K19 is not the mean discount over all of Ana's ninety seven treatments. It is the mean over the ninety one that carried a discount at all. Had the discount column held zeros where it now holds blanks, the same formula would have divided by ninety seven and answered 0.0540 instead of 0.0576. The formula would not have changed and neither would the label above it.

| Treatment | Total charged |
|---|---|
| Chocotherapy | 2984.48 |
| Detoxifying Algae | 2121.00 |
| Exfoliation | 1393.70 |
| Moisturizing | 1833.50 |
| Reductive integral | 2565.13 |
| Deep cleaning | 6736.20 |
| Cleaning Treatment | 2501.40 |
| Vaporization | 1265.38 |

K25 answers 38. The question asks how many treatments were given no discount, and being given no discount is recorded here by the cell being empty rather than by a number. COUNTBLANK asks that question without a criterion, because emptiness is the entire condition, and none of the functions of this week can be handed an empty cell as a value to match.

K27 answers 180.70, over the 409 records that are not Rosa's. The criterion `"<>Rosa"` is an operator and a value, so it goes inside quotation marks as one piece of text. K29 totals 89289.56 and shows 89290 once the cell is given no decimals, which is a display change and leaves the underlying number alone.

K31 answers 316, and the other 204 records fall in February. M4 answers 40, over two treatments: Detoxifying Algae and Detoxifying Wrap. The wildcard was read because it was sitting in a Criteria argument, which is the whole of last week in one cell.

**Output**

```text
Counts        Ana 97    Camila 100    María 115    Rafaella 97    Rosa 111   = 520
Rule paints   K5, María

Average discount   Ana 0.0576   Camila 0.0515   María 0.0494
                   Rafaella 0.0576   Rosa 0.0579
  taken over        91, 94, 108, 85 and 104 rows, not 97, 100, 115, 97 and 111

Totals charged     Chocotherapy 2984.48       Detoxifying Algae 2121.00
                   Exfoliation 1393.70        Moisturizing 1833.50
                   Reductive integral 2565.13 Deep cleaning 6736.20
                   Cleaning Treatment 2501.40 Vaporization 1265.38

K25   38          treatments with no discount
K27   180.70      average price of everyone except Rosa, over 409 records
K29   89289.56    shown as 89290 with no decimals
K31   316         treatments in January 2022, the other 204 fall in February
M4    40          Detoxifying Algae and Detoxifying Wrap

With zeros instead of blanks in column G, K19 would read 0.0540
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Every criterion points at a label in column J, none typed inside a formula | 2 |
| The five counts, adding to 520, and the rule painting K5 alone | 1 |
| The eight totals, from SUMIF found under Math & Trig and not with its family | 2 |
| The five averages, with the row counts they are actually taken over | 2 |
| K25 uses COUNTBLANK, and says why no criterion is needed | 1 |
| K27, K29 and K31, with the operator quoted and the dates joined with an ampersand | 1 |
| M4 returns 40, and names the two treatments the pattern caught | 1 |

**Most common mistake**

Reading the five averages as the mean discount per esthetician and writing that under them. They are the mean discount on the treatments that got one, and the gap between the two readings is about a third of a percentage point on Ana and about seven tenths on Rafaella. The blanks are not zeros and AVERAGEIF never pretended they were. Anyone who wants the other figure has to say so with a different formula.

---

## Week 09 · Data that arrives from outside

### 09.1 · Recognise

**Solution**

Route A is the graded one. The three lists were opened and answered by hand, the data lands as a table, and a query is left behind carrying every choice.

Route B changes one list and breaks the text. The ñ of España is the single byte F1, which is the Windows-1252 table. Read as UTF-8 that byte is not a valid sequence, so the decoder puts a replacement mark there. The two numeric columns are unaffected because digits are the same bytes in both tables.

Route C changes a different list and breaks the numbers. With **Do not detect data types**, every column arrives as text. The cells sit left-aligned and Excel marks each of them with the green triangle that reads that a number is stored as text, so `SUM` skips all twenty six and returns zero. That setting is the right one when the file carries product codes or postal codes that must keep their leading zeros. This file carries neither.

Route D never opens a dialog. Encoding, delimiter and every column type were decided by the machine, and nothing on the sheet records what was decided or lets you replay it next month. The 229.5 in the table below assumes what the lab machines use, a decimal point rather than a decimal comma. Change that one regional setting and the two numeric columns arrive as text and the sum falls to zero, which is the point: on this route nobody was asked.

The Queries and Connections pane is what proves which route somebody took. The import route leaves a named query with a row count under it. The open route leaves nothing.

**Output**

```text
              A2 shows           =SUM(F2:F27)   Queries & Connections   Refresh
Route A       Iñaki                     229.5   Students_data, 26 rows      yes
Route B       replacement mark          229.5   Students_data, 26 rows      yes
              where the ñ was
Route C       Iñaki                         0   Students_data, 26 rows      yes
Route D       the machine decides       229.5   nothing listed               no

Graded route            A
Proof of the route      the Queries & Connections pane
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four answers for A2, including why the UTF-8 run breaks on byte F1 | 3 |
| `SUM` returns 0 on route C, with the reason traced to the Data Type Detection list | 3 |
| A query on A, B and C, nothing on D, and Refresh only where a query exists | 2 |
| Names route A as the graded one and the pane as the proof | 2 |

**Most common mistake**

Answering that route C is the graded one because the compare slide used it. It is graded when the task mentions codes or IDs. Here it turns AVERAGE and EXAM into text and quietly costs every calculation that follows.

### 09.2 · Apply

**Solution**

Read the Queries and Connections pane before converting anything. The conversion is what detaches the block from the query, so the evidence has to be collected first.

The sort is one visit to the dialog with three levels, not three passes of Sort A to Z. Reopen it afterwards and the three levels are still listed in order, which is what a grader reads.

The third level decides nothing on these twenty six rows. The only pairs that tie on last name and country are the two Kim Jong rows and the two Francois Lacroix rows, and inside each pair the average is identical. It stays in the dialog because the task named it. Note also that both pairs survive the sort: duplicates were removed on the `Duplicates` sheet, and nothing on this sheet ever deleted a row.

**Output**

```text
Queries & Connections     Students_data     26 rows loaded

The sorted copy
  row  2   Björn       Algosson       Suecia            8.3
  row  3   Kepa        Arrizabalaga   España            8.2
  row  4   Baratunde   Aubameyang     Gabón             8.8
  row 10   Kim         Jong           Corea             9.5
  row 11   Kim         Jong           Corea             9.5
  row 27   Zhizhen     Zhang          China             9.9

Sort dialog, reopened     3 levels, in order
Pairs the third level separated                            0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Imported through From Text/CSV with the three lists set by hand, and the pane recorded before the conversion | 3 |
| Three levels built in one visit to the Sort dialog, headers ticked, and still there when it reopens | 3 |
| Converted to a range and the table style cleared afterwards | 1 |
| The sheet was copied with Move or Copy before the second sort | 1 |
| Row 2 reads Algosson and row 27 reads Zhang | 1 |
| Says the third level separated nothing on this data | 1 |

**Most common mistake**

Sorting three times with Sort A to Z from the Home tab, in reverse priority order. The rows land in the same arrangement, the Sort dialog opens empty, and the part of the work that was going to be marked left no trace.

### 09.3 · Integrate

**Solution**

The four formulas on the `Checks` sheet:

```text
=COUNTIFS(Hoja1!$A$2:$A$409,">="&DATE(2018,1,1),Hoja1!$A$2:$A$409,"<="&DATE(2018,3,31))
=COUNTIF(Hoja1!$C$2:$C$409,"PH*")
=SUMIFS(Hoja1!$L$2:$L$409,Hoja1!$C$2:$C$409,"PH*")
=SUM(Hoja1!L2:L409)
```

They live on a second sheet for one reason. A formula parked in a spare column of the filtered sheet is itself in a row the filter can hide, and a student who cannot see the number cannot compare it with anything.

`COUNTIF` and `SUMIFS` ignore case, so the one record whose brand is written `Philips` in mixed case is counted alongside the 122 written `PHILIPS` and the 8 written `PHILCO`. That is the whole 131, and it is also why the AutoFilter route, **Text Filters**, **Begins With**, returns the same number.

Two of the three filtered readings disagree because they are answering different questions. `SUM` has no idea a filter exists: it adds every row in L2:L409, hidden or not, and returns the grand total unchanged. The status bar aggregates the visible cells of the selection only, so it is the one that tracks the filter. Select L2:L409 with the quarter showing and the status bar Sum is the answer to how much was sold in the first quarter.

**Output**

```text
No filter
  COUNTIFS, first quarter of 2018                       90
  COUNTIF, brand begins with PH                        131
  SUMIFS, total sale of the PH brands           21,832,893

Filter on, Date Filters > Between, 01/01/2018 to 31/03/2018
  Status bar record count                 90 of 408 records found
  =SUM(Hoja1!L2:L409) on the Checks sheet        72,634,429
  Status bar Sum on L2:L409                      15,798,342

The number that answers the question            15,798,342
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `COUNTIFS` returns 90 with both date criteria inside one formula | 2 |
| `COUNTIF` returns 131 and the answer notes the wildcard route ignores case | 2 |
| `SUMIFS` returns 21,832,893 | 2 |
| The three filtered readings, correct | 2 |
| The four helper columns built with relative references | 1 |
| Explains that `SUM` adds the hidden rows and names the status bar Sum as the answer | 1 |

**Most common mistake**

Reading 72,634,429 off the `SUM` cell with the filter on and reporting it as the quarter. The tell is that the number does not move when the filter does, and nobody checks a number that was right the first time they looked at it.

---

## Week 10 · Tables and charts

### 10.1 · Recognise

**Solution**

The total row does not write `SUM` and it does not write `COUNT`. Picking from the drop-down on the right edge of a total cell writes a `SUBTOTAL` in the one hundred series, which ignores rows hidden by a filter and rows hidden by hand alike. **Count** is `COUNTA`, code 103, which is what a text column such as Status needs; **Count Numbers** would have skipped every entry in it.

E12 stands still because the table does not own it. It is an ordinary formula over an ordinary address, sitting two rows below a table it has no relationship with, and `SUM` was never told about the filter.

Had the Quantity drop-down been left on **Sum**, the cell would read `=SUBTOTAL(109,[Quantity])`: 2,455 with no filter and 745 with the Sent filter on.

**Output**

```text
What the formula bar shows
  Status total     =SUBTOTAL(103,[Status])
  Quantity total   =SUBTOTAL(101,[Quantity])
  E12              =SUM(E2:E9)

                          no filter     Status = Sent
  Status total                    8                 3
  Quantity total            306.875            248.33
  E12                          2455              2455

Stored value behind 248.33                     745 / 3
Left on Sum instead of Average       2455  then     745
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three formulas written as the formula bar shows them, `SUBTOTAL` and not `SUM` | 3 |
| The three filtered values, 3, 248.33 and 2,455 | 3 |
| The three unfiltered values, 8, 306.875 and 2,455 | 2 |
| Says E12 stood still because the table does not own it | 1 |
| The Sum pair, 2,455 and 745 | 1 |

**Most common mistake**

Writing the codes as 3 and 1 instead of 103 and 101. The drop-down never writes the short codes; the one hundred series is what a total row produces, and the difference shows the moment somebody hides a row by right-clicking it rather than by filtering.

### 10.2 · Apply

**Solution**

Excel plots by column here because the block has six rows and four columns, so the first chart holds three series, one per month, against five categories, one per genre. **Switch Row/Column** trades them: five series, three categories. Doing it inside **Select Data Source** rather than with the ribbon button leaves you in the dialog where the next edit already is.

`Genre by month` is a chart sheet, not a sheet holding a chart. Its tab sits in the tab bar and the sheet has no rows and no columns. F11 produces the same kind of object with the default chart type and the name Chart1, which is two thirds of the task failed in one keystroke.

The alt text is stored on the chart object as you type it. There is no OK button, and a caption typed into a cell under the chart leaves the property empty, which is exactly what the Accessibility Checker reads.

**Output**

```text
Insert > Charts > dialog box launcher > All Charts > Column > Clustered Column

Before Switch Row/Column     3 series      5 categories
  legend    January, February, March
  axis      Classics, Mistery, Romance, Sci-Fi, Young readers

After Switch Row/Column      5 series      3 categories
  legend    Classics, Mistery, Romance, Sci-Fi, Young readers
  axis      January, February, March

Tallest column        Romance, February, 131,390
Chart sheet           Genre by month, no grid, tab in the tab bar
Alt Text pane         no OK button, the text is stored as you type
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The chart came out of the Insert Chart dialog, with the family and the subtype chosen there | 2 |
| The two pairs of counts, 3 by 5 and then 5 by 3 | 2 |
| Switch Row/Column done inside Select Data Source | 2 |
| Move Chart, New sheet, named `Genre by month`, not Chart1 and not F11 | 2 |
| Alt text written on the chart object, one or two sentences, not a caption in a cell | 2 |

**Most common mistake**

Reaching the chart sheet with F11 and the chart with Alt+F1. Both work, both are fast, and neither opens a dialog, so the subtype was never chosen and the sheet was never named.

### 10.3 · Integrate

**Solution**

The calculated column is one formula written into the first data cell. The table fills the rest of the column on its own and keeps filling it as rows arrive.

```text
=IFS([@Quantity]>=400,"High",[@Quantity]>=200,"Medium",TRUE,"Low")
```

The four formulas below the table:

```text
=SUM(Orders[Quantity])
=COUNTIFS(Orders[Status],"Sent")
=SUMIFS(Orders[Quantity],Orders[Product],"Chamarra")
=AVERAGEIFS(Orders[Quantity],Orders[Destination],"GUANAJUATO")
```

Two of the four move after the paste and two do not, and both facts are correct. The ninth order is a Traje de Baño going to NUEVO LEON, so the Chamarra total and the GUANAJUATO average have nothing new to read. The sum and the Sent count do. Not one of the four formulas was edited, because a structured reference names the column, not the cells it currently occupies.

The band written into the ninth row is `Medium`, because 245 clears 200 and misses 400.

**Output**

```text
                                                    before    after
  =SUM(Orders[Quantity])                              2455     2700
  =COUNTIFS(Orders[Status],"Sent")                       3        4
  =SUMIFS(Orders[Quantity],Orders[Product],"Chamarra")
                                                       699      699
  =AVERAGEIFS(Orders[Quantity],Orders[Destination],"GUANAJUATO")
                                                       398      398

  Band written into the ninth row                            Medium
  Cells edited to cover nine rows instead of eight                0

  The same four written over E2:E9
                                          2455, 3, 699, 398 in both
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| All four formulas hold the table name and a column name, and none holds a cell address | 3 |
| The four values before the paste and the four after | 2 |
| The answer says which two moved, which two did not, and why | 2 |
| The calculated column is one `IFS` written once and filled by the table | 2 |
| Zero cells edited after the paste | 1 |

**Most common mistake**

Dragging the mouse over the quantities while writing the sum, which puts `$E$2:$E$9` in the formula. It returns 2,455 today and it will keep returning 2,455 after the ninth order lands, with no error and no warning.

---

## Week 11 · Chart choice and distribution

### 11.1 · Recognise

**Solution**

Every cell of a new worksheet already carries the **Locked** flag. That flag does nothing at all until the sheet is protected, and the instant it is, everything carrying it freezes together. Colleague 1 protected first and unlocked nothing, so the whole sheet froze, including the twelve columns a reader was supposed to be able to fill in. That is not a stricter version of the right answer, it is a different failure.

Colleague 2 did it in the order that works and stopped one check box short. `Locked` keeps J from being edited. `Hidden`, in the same visit to the **Protection** tab, is what empties the formula bar. Without it the age formula is protected and still perfectly readable.

Colleague 3 changed nothing inside the file. The Windows read-only attribute makes Excel open the workbook read-only and refuse to save over it, and cells can still be typed into for the session. **File**, **Info** reports an unprotected workbook, and the Review tab still offers **Protect Sheet**, which is the fastest way to see that nothing was protected.

**Output**

```text
                     E5          G5          J5 formula bar     Review tab
Colleague 1     refused     refused    shows the formula   Unprotect Sheet
Colleague 2    accepted     refused    shows the formula   Unprotect Sheet
Colleague 3    accepted    accepted    shows the formula     Protect Sheet

Closest to the task    Colleague 2
Still missing          Hidden, on J2:J115, in the same visit to Ctrl+1
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Colleague 1 freezes the whole sheet, and the answer traces it to the default Locked flag | 3 |
| Colleague 2 correct on all four questions | 3 |
| Colleague 3 protects nothing inside the file, and the Review tab still reads Protect Sheet | 2 |
| Names Colleague 2 and the missing `Hidden` check box | 2 |

**Most common mistake**

Calling Colleague 1's sheet the safe one because it refuses everything. Protection is not a wall around the file, it is a per cell flag, and a sheet nobody can use has failed the task as surely as one that protects nothing.

### 11.2 · Apply

**Solution**

The two magnitudes are why this chart exists. Temperatures run from 11.9 to 25.1 and ice cream units from 185 to 614. On a single value axis the entire temperature range is thinner than the gap between two gridlines, so the line lies flat along the baseline and the chart says nothing about the relationship it was built to show.

Both edits happen in the same row of the same dialog before it closes: the chart type list set to **Line with Markers** and the **Secondary Axis** check box ticked. That is one operation, and it is the operation the task is written around. Right-clicking a series afterwards reaches the same setting and never opens the Combo entry.

An unlabelled second axis is worse than no second axis, because the reader has no way of knowing which scale belongs to which series. Both titles come from **Add Chart Element**, **Axis Titles**, with the position named.

**Output**

```text
Insert > Charts > Insert Combo Chart > Create Custom Combo Chart...

Series      2    Ice Cream     Clustered Column     primary axis
                 Temperature   Line with Markers    secondary axis
Categories  12   Aguascalientes through Guerrero

Top of both series      Chihuahua              25.1  and  614
Bottom of both          Baja California Sur    11.9  and  185

Axis titles   primary vertical     Ice cream units
              secondary vertical   Average temperature (C)

On a shared axis   the temperature series lies flat on the baseline

Change Chart Type, reopened
  All Charts, Combo highlighted, the Temperature row still on
  Line with Markers with Secondary Axis still ticked
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Built from Create Custom Combo Chart, not from a column chart repaired afterwards | 3 |
| Chart type and Secondary Axis set in the same row before the dialog closed | 2 |
| Both axis titles added from Add Chart Element with the position named | 2 |
| 2 series and 12 categories | 1 |
| Chihuahua at 25.1 and 614 | 1 |
| Says what the temperature series would look like on a shared axis | 1 |

**Most common mistake**

Building a clustered column chart of both columns first and then right-clicking the temperature series to move it. The finished picture is identical, and the dialog the task was written around was never opened.

### 11.3 · Integrate

**Solution**

The age formula is a subtraction of two serial numbers divided by the average length of a year and truncated. A fixed cut-off is used so the answer can be marked; swap `DATE(2025,12,31)` for `TODAY()` and the column becomes correct and unmarkable.

Name Manager lists four names. `BD` refers to `Personnel!$A$1:$I$115` and points at live data, so it stays. The other three are the leftovers of an old advanced filter exercise and all three resolve to `Personnel!#REF!`. The Refers To column prints the answer, so nothing here needs guessing.

The order of the protection work is not negotiable. Unlock everything first, because **Format Cells** is one of the things protection blocks and once the sheet is protected the dialog you need is the dialog you locked away. Then `Locked` and `Hidden` together on the age column, in one visit. Then the edit range, then **Protect Sheet** from the button at the bottom of the **Allow Users to Edit Ranges** dialog, which is what shows the two settings are one operation.

The comment is a threaded comment, so the cell carries a small purple triangle, the box carries a Reply field, and **Show Comments** lists the thread. A note would have a red triangle and would never appear in that pane. It has to be posted before the sheet is protected: **New Comment** is one of the commands a protected sheet greys out, and a student who leaves it to the end finds the button unavailable and blames the file.

**Output**

```text
J1   Age
J2   =INT((DATE(2025,12,31)-I2)/365.25)                        63
J5   the cell shows 66, the formula bar is empty

=COUNTIF(J2:J115,">=60")                                       87
=COUNTIF(J2:J115,">=65")                                       43

Name Manager, 4 names
  BD            Personnel!$A$1:$I$115         keep
  CRITERIOO     Personnel!#REF!               delete
  CRITERIOY     Personnel!#REF!               delete
  RESULTADOS    Personnel!#REF!               delete

Click E5 and type      accepted
Click G5 and type      Excel asks for the Payroll range password
Review tab             Unprotect Sheet, Unprotect Workbook
Right-click a tab      Insert, Delete, Rename, Move or Copy, Tab Color,
                       Hide and Unhide all dimmed
Comments pane          one thread on J1, purple triangle on the cell
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Unlocked the whole sheet first, then `Locked` and `Hidden` on J2:J115 in one visit to Ctrl+1 | 2 |
| Allow Edit Ranges created over G2:G115, and Protect Sheet reached from the button at the bottom of that dialog | 2 |
| The age column filled and J2 reads 63 | 2 |
| Name Manager cleaned: the three `#REF!` names gone, `BD` kept | 2 |
| The two counts, 87 and 43 | 1 |
| A threaded comment posted and listed in the Comments pane, and the workbook structure protected | 1 |

**Most common mistake**

Deleting all four defined names because three of them were broken. `BD` covers the live data block and something else in the workbook may be reading it. The instruction named a condition, the Refers To column reports it, and the fix was three deletions and not four.

---

## Week 12 · Midterm, mock and VLOOKUP

### 12.1 · Recognise

**Solution**

Version (a) has a relative table array, so the range walks one row down for every row the formula is filled into. Row 3 reads A15:C18 and finds A. Row 4 reads A16:C19, which has lost A but still holds B, and returns a number. Row 5 reads A17:C20, where A no longer exists. From row 7 down the array is four blank rows, and `VLOOKUP` with `FALSE` over blanks returns `#N/A`, not `#REF!`.

Version (b) hands a three column range to a formula asking for column 4. There is nothing to walk off the edge of, so every row returns `#REF!` at once, which makes it the easiest of the four to find.

Version (c) leaves the fourth argument out, which means `TRUE`, the approximate match. Every one of the ten answers is right, because the first column of the table reads A, B, C, D in ascending order and every key hits exactly. Right answer, unsafe formula: reorder those four rows and the same formula starts returning wrong numbers with no error value anywhere.

Version (d) fails only where the trailing space is. `"A"` is not `"A "`, so row 3 returns `#N/A` and the nine rows that look up B, C and D are untouched.

Version (a) is the hardest to catch because it is the only one whose top rows are correct. The reader checks the first cell, sees 50,000, and stops reading.

**Output**

```text
        F3          F12         rows returning a number
(a)     50,000      #N/A        2   rows 3 and 4
(b)     #REF!       #REF!       0
(c)     50,000      20,000     10
(d)     #N/A        20,000      9

How (a) walks
  row  3    A15:C18    keys A B C D              50,000
  row  4    A16:C19    keys B C D blank          40,000
  row  5    A17:C20    keys C D blank blank      #N/A
  row  7    A19:C22    four blank rows           #N/A
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) both cells, the count of 2, and the walking array explained row by row | 4 |
| (b) `#REF!` everywhere, traced to a fourth column that does not exist | 2 |
| (c) right answers, unsafe formula, and the sorted first column named as the reason it works | 2 |
| (d) `#N/A` in row 3 only | 1 |
| Says (a) hides because the top of the column is correct | 1 |

**Most common mistake**

Answering `#REF!` for (a) on the grounds that the table array runs off the bottom of the reference table. A15:C18 shifted downward is still a perfectly valid range; it is simply empty, and an empty first column produces `#N/A`.

### 12.2 · Apply

**Solution**

```text
F3    =VLOOKUP(D3,Table!$A$15:$C$18,2,FALSE)
F12   =VLOOKUP(D12,Table!$A$15:$C$18,2,FALSE)
H3    =VLOOKUP(D3,Table!$A$15:$C$18,3,FALSE)
G3    =F3*12
J3    =E3-H3
K3    =J3/H3
```

`Lookup_value` stays relative, which is why F12 reads D12. `Table_array` is locked with F4, which is why F12 still reads `$A$15:$C$18` and not `$A$24:$C$27`. `Col_index_num` is 2 for the base salary and 3 for the sales goal, counted from the first column of the range handed to the function; on this table that happens to coincide with the worksheet columns, and on the next table it will not.

Changing the type B base salary moves two rows of the report, row 4 and row 10, which is what a reference table is for. The number lives in one place and every row that needs it asks.

**Output**

```text
row  employee            type    base     annual        goal        sold     difference       %
  3  Javier López           A  50,000    600,000  20,000,000  22,000,000     2,000,000   10.00%
  4  Alejandra Guzmán       B  40,000    480,000  15,000,000  16,000,000     1,000,000    6.67%
  5  Bruno Díaz             A  50,000    600,000  20,000,000  19,500,000      -500,000   -2.50%
  6  Ricardo Tapia          C  30,000    360,000  10,000,000  11,500,000     1,500,000   15.00%
  7  Jorge Negrete          D  20,000    240,000   5,000,000   8,000,000     3,000,000   60.00%
  8  Juan Camaney           C  30,000    360,000  10,000,000  10,500,000       500,000    5.00%
  9  María Félix            D  20,000    240,000   5,000,000   4,500,000      -500,000  -10.00%
 10  Diego Luna             B  40,000    480,000  15,000,000  16,500,000     1,500,000   10.00%
 11  Andrea Legarreta       D  20,000    240,000   5,000,000   2,000,000    -3,000,000  -60.00%
 12  Amauri Pérez           D  20,000    240,000   5,000,000  10,500,000     5,500,000  110.00%

Total of the ten monthly base salaries                                          320,000
Rows carrying a negative difference                                                   3
Rows that move when the type B base salary changes                       2   rows 4, 10
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `Table_array` locked with F4, and F12 still reads `$A$15:$C$18` | 2 |
| Built through Formulas, Lookup & Reference, VLOOKUP, with the four boxes filled by name | 2 |
| `Col_index_num` counted inside the table array, 2 for the salary and 3 for the goal | 2 |
| The ten values in F and the ten in H, correct | 2 |
| `Range_lookup` written out as `FALSE` in both, not left empty and not typed as 0 | 1 |
| The three reported figures: 320,000, three negatives, two rows move | 1 |

**Most common mistake**

Typing the formula and dragging the table with the mouse, without pressing F4. Rows 3 and 4 come back with numbers, everything under them turns to `#N/A`, and the student spends the next ten minutes looking for a problem in the data.

### 12.3 · Integrate

**Solution**

```text
N3   =INT(($N$1-C3)/365.25)
R3   =IF(AND(K3>0.05,N3>10),"Yes","No")
S3   =IF(OR(E3>10000000,N3>15),"Yes","No")
```

`$N$1` is locked because every row measures seniority against the same reference date. The two decisions are one `IF` each with the logical function inside it, which is how the task is worded and how the exam item is written.

Both conditional formatting rules go on K3:K12 through **Highlight Cells Rules**, one **Less Than** with 0 and one **Greater Than** with 50 %, typed with the sign and stored as 0.5. **Manage Rules** has to show two separate entries.

Juan Camaney, row 8, sits exactly on the boundary: his difference is 500,000 on a goal of 10,000,000, which is 5.00 % to the last decimal. His award cell reads `No`, and rewriting the condition as five per cent or more would not change it. The percentage leg would flip to TRUE and the seniority leg would stay FALSE at 5 years against a threshold of 10, so the `AND` returns FALSE either way. Testing one leg and declaring the answer is how that gets marked wrong.

**Output**

```text
row  employee            diff %    years   award   letter
  3  Javier López        10.00%       30     Yes      Yes
  4  Alejandra Guzmán     6.67%       16     Yes      Yes
  5  Bruno Díaz          -2.50%       22      No      Yes
  6  Ricardo Tapia       15.00%        7      No      Yes
  7  Jorge Negrete       60.00%        2      No       No
  8  Juan Camaney         5.00%        5      No      Yes
  9  María Félix        -10.00%        4      No       No
 10  Diego Luna          10.00%       12     Yes      Yes
 11  Andrea Legarreta   -60.00%        1      No       No
 12  Amauri Pérez       110.00%        1      No      Yes

=COUNTIF(R3:R12,"Yes")                                    3
=COUNTIF(S3:S12,"Yes")                                    7
=COUNTIF(K3:K12,"<0")                                     3

Manage Rules, applied to =$K$3:$K$12
  Cell Value < 0        red fill        3 cells caught
  Cell Value > 0.5      green fill      2 cells caught

Award winners    Javier López, Alejandra Guzmán, Diego Luna
On the boundary  Juan Camaney, award No, and > against >= changes nothing
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The award is one `IF` with `AND` inside it, and the letter one `IF` with `OR` | 2 |
| Two separate conditional formatting rules, both listed in Manage Rules | 2 |
| The three counts, 3, 7 and 3 | 2 |
| The ten award and letter values, correct | 2 |
| Seniority written against the locked `$N$1` | 1 |
| Juan Camaney named, award `No`, and both legs of the `AND` tested to prove it | 1 |

**Most common mistake**

Writing the award test as `K3>5` because the cell displays 10.00 %. K3 holds 0.1. The comparison is never true, the award column comes back ten times `No`, and the sheet looks plausible enough that nobody questions it. The percentage sign is a display format, so the test has to be written `>5%` or `>0.05`.

---

## Week 13 · Lookup and consolidation

### 13.1 · Recognise

**Solution**

(a) The exact match answers four of the five and stops on the fifth. `GAS` is not in `Fees`, so C4 is `#N/A` and that is the function working, not failing.

(b) 43,100. `Range_lookup` was left empty, and empty means TRUE, which is the banded match. The table is sorted ascending, `GAS` falls between `FIN` and `MKT`, so the function stops on the last code at or below the key, row 4, and hands back the Finanzas fee. Nothing on the sheet turns red.

(c) The band table is sorted ascending and holds the lower edge of each grade, so TRUE is the right answer here and the only place in the exercise where it is.

(d) With `Fees!A2:B6` unlocked, the block walks down one row per fill. I2 reads `Fees!A2:B6`, I3 reads `Fees!A3:B7`, I4 reads `Fees!A4:B8`, I5 reads `Fees!A5:B9` and I6 reads `Fees!A6:B10`. Rows 2 and 3 come out right by luck: `MKT` and `FIN` happen still to sit inside the block after it has moved. From row 4 down the block has walked past the codes being looked for. Row 4 shows `#N/A` for the wrong reason, which is the worst of the five, because it is the one that looks like the correct answer from (a).

**Output**

```text
(a)  C2  38,500
     C3  43,100
     C4  #N/A
     C5  41,200
     C6  39,750

(b)  D4  43,100     from Fees row 4, FIN

(c)  H2  C     (79)
     H3  A     (91)
     H4  F     (58)
     H5  C     (70)
     H6  A     (100)

(d)  I2  38,500    right
     I3  43,100    right by luck
     I4  #N/A      right answer, wrong reason
     I5  #N/A      wrong, CON is in the table
     I6  #N/A      wrong, ADM is in the table
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five results of (a), with `#N/A` in C4 | 2 |
| (b) answers 43,100 and names the empty argument as TRUE | 3 |
| The five grades of (c) | 2 |
| (d) gives the five results and names rows 2 and 3 as right by luck | 3 |

**Most common mistake**

Answering `#N/A` in (b) because `GAS` is not in the table. The reasoning is right for the formula in (a) and wrong for this one, and the whole point of the slide is that the two formulas differ by one missing argument.

### 13.2 · Apply

**Solution**

H4, filled to H6:

```excel
=INDEX($B$4:$B$11,MATCH($G4,$D$4:$D$11,0))
```

H8:

```excel
=SUM(H4:H6)
```

J6 on `Inventory 3`:

```excel
=HLOOKUP(J3,$B$3:$G$6,4,FALSE)
```

Why VLOOKUP is the wrong function on each sheet. On `Inventory 2` the key is in column D and the answer is in column B, so the offset would have to be negative. `Col_index_num` counts rightwards from column one of `Table_array` and cannot be given a negative number, which is the argument that fails. On `Inventory 3` the keys run across row 3 rather than down a column, so `Table_array` has no first column to search; that is what `Row_index_num` and HLOOKUP exist for.

Two details the marker looks for in the bar. `MATCH` sits inside `INDEX`'s `Row_num`, not in a separate cell wired in afterwards. And `$G4` is mixed, locked on the column and loose on the row, so the fill down works while the two ranges stay put.

**Output**

```text
H4   9.80      PV-207
H5  27.90      CU-330
H6 145.00      TO-051
H8 182.70      total of the three

J6  63.40      RO-012, read across row 3 and down to row 6
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| INDEX was built through Select Arguments and MATCH nested from the Name Box, one OK at the INDEX level | 3 |
| The three costs and the 182.70 total are right | 2 |
| Array and Lookup_array are locked and `$G4` is left free to fill down | 2 |
| The HLOOKUP returns 63.40 with `Row_index_num` 4 and FALSE written out | 2 |
| Both explanations name the argument that fails, not the function | 1 |

**Most common mistake**

Rebuilding `Inventory 2` by moving the Item column in front of the Cost column and then using VLOOKUP. The three numbers come out right and the task scored zero, because the exercise is the pairing of INDEX with MATCH and the exam item will not let you rearrange the data it hands you.

### 13.3 · Integrate

**Solution**

Consolidate writes the label from the sources' top row into B1 and the row labels down A2, in the order it first met them: Tools and Plumbing and Electrical from `Norte`, then Paint, which only `Centro` has. Because **Top row** and **Left column** were ticked, the three sheets could list their categories in three different orders and every number still landed on the right row.

The 3-D reference in D2 adds by position, not by name. It adds cell B2 of `Norte`, B2 of `Sur` and B2 of `Centro`, which is Tools plus Electrical plus Plumbing. The total is arithmetically correct and answers a question nobody asked.

B10:

```excel
=VLOOKUP(A10,$A$2:$B$5,2,FALSE)
```

The external link, written by pointing rather than typing. While `Consolidation.xlsx` is open, `Board.xlsx` shows `=[Consolidation.xlsx]Summary!$B$7`. Close the source and the same formula rewrites itself as `='C:\Reports\[Consolidation.xlsx]Summary'!$B$7`, path in single quotes. That rewrite is the product confirming the link is real. **Edit Links** lists one source and **Check Status** returns OK.

Ticking **Create links to source data** would have put an outline on `Summary`, with level buttons 1 and 2 at the top left of the row headers and one hidden detail row per source under each label, each carrying an external reference back to its branch sheet.

**Output**

```text
Summary sheet
  B1  Amount
  A2  Tools        B2    470,900
  A3  Plumbing     B3    216,750
  A4  Electrical   B4    308,750
  A5  Paint        B5     41,800
  B7  grand total       1,038,200

3-D reference, added by position
  D2  271,600   = Norte Tools + Sur Electrical + Centro Plumbing
  D3  385,500
  D4  339,300
  D5   41,800

Lookup
  A10 Electrical   B10   308,750

Board.xlsx B2
  source open    =[Consolidation.xlsx]Summary!$B$7
  source closed  ='C:\Reports\[Consolidation.xlsx]Summary'!$B$7
  Edit Links     Status: OK
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Consolidate was run from the dialog with Top row and Left column ticked, and reopening it brings the three references back | 3 |
| The four consolidated figures and the 1,038,200 total are right | 2 |
| D2 is explained as Tools plus Electrical plus Plumbing | 2 |
| The link was made by pointing and both forms of the formula are reported | 2 |
| The VLOOKUP returns 308,750 with the table array locked and FALSE written out | 1 |

**Most common mistake**

Typing the four totals by hand once the arithmetic is understood, or writing `=Norte!B2+Sur!B3+Centro!B4` to line the categories up. Both give 1,038,200 and neither survives a branch adding a category, which is what the Paint row in `Centro` is there to show.

---

## Week 14 · Subtotals and PivotTables

### 14.1 · Recognise

**Solution**

(a) The command inserts four rows, three group totals and a grand total, and builds a three-level outline while it is at it. Nobody typed any of the formulas.

(b) The grand total is another `SUBTOTAL`, and `SUBTOTAL` ignores any other `SUBTOTAL` sitting inside the range it is given. That is why it spans D2:D16, subtotal rows included, and still returns 1,395,900. `=SUM(D2:D16)` over the same block counts the twelve records once and the three group totals again, so it returns exactly twice the right answer.

(c) Six subtotal rows, plus the grand total, so seven inserted rows. Every one of the six is arithmetically correct: the command breaks wherever the column changes value and adds the run of rows above the break. The gender column runs F F F M F F M F F M M M, which is six runs. A run is not a group, and that is the whole difference the sort makes.

(d) The Iztapalapa subtotal does not move. Function code 9 ignores rows hidden by a filter and counts rows hidden by hand. Code 109 ignores both. The one place in Excel that writes 109 without being asked is the Total Row of an Excel table.

**Output**

```text
(a)  row  6   Azcapotzalco Total   =SUBTOTAL(9,D2:D5)      245,700
     row 10   Coyoacán Total       =SUBTOTAL(9,D7:D9)      298,300
     row 16   Iztapalapa Total     =SUBTOTAL(9,D11:D15)    851,900
     row 17   Grand Total          =SUBTOTAL(9,D2:D16)   1,395,900

(b)  =SUBTOTAL(9,D2:D16)   1,395,900
     =SUM(D2:D16)          2,791,800

(c)  6 subtotal rows, 7 rows inserted in all

(d)  code 9    851,900
     code 109  699,600
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four inserted rows land on rows 6, 10, 16 and 17 with the right formulas and values | 3 |
| (b) gives 1,395,900 and 2,791,800 and explains why SUBTOTAL does not double count | 3 |
| (c) answers six subtotal rows and says why each one is still correct arithmetic | 2 |
| (d) gives 851,900 and 699,600 and names the table Total Row as the source of 109 | 2 |

**Most common mistake**

Answering that the grand total is wrong because it covers the subtotal rows. The range really does cover them, and that is the point of the function: `SUM` over the same block is the one that comes out at 2,791,800.

### 14.2 · Apply

**Solution**

Both reports are built the same way and differ in one tab of one dialog. Click one cell inside the list, **Insert**, **PivotTable**, confirm `Tickets!$A$1:$G$13`, **New Worksheet**. Then drag: Category into **Rows**, Waiter into **Columns**, Charged into **Values**. Ticking the check boxes would have sent Category and Waiter to Rows and Charged to Values, which is a different report out of the same three fields.

For report one, click a value cell, **PivotTable Analyze**, **Active Field**, **Field Settings**. **Summarize Values By** stays on Sum, **Custom Name** becomes `Charged`, and **Number Format** opens the cut-down Format Cells where Currency with two decimals is set. One OK. For report two the same dialog is used, and without closing it the **Show Values As** tab is set to **% of Grand Total**, the name to `Share`, and the format to Percentage with two decimals.

The Desserts cell under Lucía is empty because she sold no dessert in these twelve tickets. A PivotTable leaves the cell blank rather than writing a zero, and the string it writes there instead is set in **PivotTable Options**, **Layout & Format**, under "For empty cells show".

**Output**

```text
ByWaiter, Sum of Charged, Currency 2 dp

                Lucía     Marco     Nadia   Grand Total
Desserts                 205.00    140.00        345.00
Drinks         235.00    120.00     65.00        420.00
Mains          555.00    195.00    705.00      1,455.00
Grand Total    790.00    520.00    910.00      2,220.00

ShareOfTotal, % of Grand Total, Percentage 2 dp

                Lucía     Marco     Nadia   Grand Total
Desserts                   9.23%     6.31%        15.54%
Drinks         10.59%      5.41%     2.93%        18.92%
Mains          25.00%      8.78%    31.76%        65.54%
Grand Total    35.59%     23.42%    40.99%       100.00%

The four boxes of report one
  Filters   (empty)
  Columns   Waiter
  Rows      Category
  Values    Charged
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Every field was dragged into the area the task named, and the four boxes are reported as they read | 3 |
| The twelve figures of report one and the grand total 2,220.00 are right | 2 |
| Function, calculation, caption and number format were set in Field Settings rather than on the cells | 3 |
| Report two shows % of Grand Total and its percentages are right | 1 |
| The blank Desserts cell is explained, not filled in with a zero by hand | 1 |

**Most common mistake**

Selecting the value cells and clicking Currency or Percent Style on the Home tab. The screen is identical and the format is stuck to a block of cells, so the first refresh that adds a waiter loses it. Field Settings is the difference between the two reports scoring and not scoring.

### 14.3 · Integrate

**Solution**

H2, filled to H13:

```excel
=E2*VLOOKUP(D2,Menu!$A$2:$B$13,2,FALSE)
```

The multiplication is on the outside because `Menu` holds a unit cost and the ticket holds units. A2:H13 then becomes the table `Tickets2026`, so the PivotTable source grows when a ticket is added instead of having to be repointed.

In the report, Date goes into **Rows**, and with a date item selected, **PivotTable Analyze**, **Group**, **Group Field** is set to Months and Quarters together. The **By** list toggles, so both stay lit without Ctrl. Excel then adds a Quarters field to the pane and leaves the original Date field holding the months, which is the fingerprint of the graded route.

`Margin` is a calculated field built from **Fields, Items, & Sets**, **Calculated Field**, with the formula assembled by clicking Charged, **Insert Field**, the minus sign, LineCost, **Insert Field**. It comes out right because the difference of two sums is the sum of the two differences.

`LineCheck` is the same dialog and the wrong idea. A calculated field is evaluated against the totals inside each cell of the report, so `= Units * UnitPrice` returns the sum of the units multiplied by the sum of the unit prices. On the May row that is 13 units times 270.00, and on the grand total row it is 31 units times 904.00. Neither is the sum of anything anybody charged. Notice as well that the Q2 subtotal of `LineCheck` is not the two month rows added up, for the same reason. Charged is the column that goes to the owner; `LineCheck` exists so you can see the trap once and never build it again.

**Output**

```text
LineCost, H2:H13
  31.00  100.00   48.00   38.00  144.00   24.00
 128.00   44.00   54.00  200.00   90.00   56.00

PivotTable over Tickets2026, tabular layout, all item labels repeated

Quarters  Date    Charged   LineCost    Margin   LineCheck
Qtr1      Mar      545.00     217.00    328.00    2,601.00
Qtr1 Total         545.00     217.00    328.00    2,601.00
Qtr2      Apr      765.00     340.00    425.00    3,105.00
Qtr2      May      910.00     400.00    510.00    3,510.00
Qtr2 Total       1,675.00     740.00    935.00   13,530.00
Grand Total      2,220.00     957.00  1,263.00   28,024.00

The disagreement
  May row       Charged   910.00   LineCheck  3,510.00   out by  2,600.00
  Grand total   Charged 2,220.00   LineCheck 28,024.00   out by 25,804.00
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| LineCost is a lookup with the table array locked and FALSE written out, and the twelve values are right | 2 |
| The source is the table `Tickets2026` and the report was built over it | 1 |
| Group Field was used and the Quarters field appears in the field pane | 2 |
| `Margin` is a calculated field in the dialog, not a helper column, and its three figures are right | 2 |
| Tabular layout, repeated item labels, and all three formats set on the field | 1 |
| Both LineCheck figures are given and the totals explanation is correct | 2 |

**Most common mistake**

Adding a `Margin` column to the source data with `=G2-H2`, refreshing and dragging it into Values. The arithmetic is more correct that way, and the task said calculated field, so no calculated field exists in the workbook and the objective is untouched.

---

## Week 15 · Advanced filters

### 15.1 · Recognise

**Solution**

(a) Two conditions on one row are joined with AND, so both have to hold on the same record. Escobar and Espinosa are the only two people in Centro doing Accounting.

(b) Two rows are joined with OR, and each row keeps its own AND. So this asks for Centro and Accounting, or Azcapotzalco and Logistics, which is four people out of three branches and three departments.

(c) The question mark stands for exactly one character and the asterisk for any run of them, so `?E*` reads as "second letter is E". Six surnames qualify. Case is ignored, and so are the accents on Beltrán and Peña, because the wildcard is not looking at those positions.

(d) The same field written twice on one row is how you state both ends of a range. Above 4,000 and below 6,000, both exclusive as written, gives six people. Nobody sits exactly on either boundary here, so the difference between `>` and `>=` does not show, which is exactly the kind of thing that shows up on somebody else's data.

The blank row. An empty condition matches every record, so the filter returns all twelve and looks as though it did nothing at all. It did what was written.

The four conditions on one row. That asks for a person who works in Centro and in Azcapotzalco at the same time, doing Accounting and Logistics at the same time. Nothing comes out, and no error appears either.

**Output**

```text
(a)  Escobar, Espinosa                                    2
(b)  Escobar, Estrada, Espinosa, Peña                     4
(c)  Reyes, Lemus, Beltrán, Peña, Vega, Herrera           6
(d)  Escobar, Estrada, Lemus, Espinosa, Peña, Vega        6

blank row inside the criteria       all 12 records
all four conditions on one row      0 records
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) two surnames, and same row read as AND | 2 |
| (b) four surnames, and separate rows read as OR without losing the pairing | 3 |
| (c) six surnames, with `?` read as exactly one character | 2 |
| (d) six surnames, and the repeated field read as two ends of one range | 2 |
| The blank row is answered as twelve records, not as nothing | 1 |

**Most common mistake**

Reading (b) as Centro or Azcapotzalco crossed with Accounting or Logistics, which would return six. The geometry keeps each row's conditions together; two rows are two complete alternatives, not a pool of four loose conditions.

### 15.2 · Apply

**Solution**

The criteria ranges, written with headers copied from row 3 of the list rather than retyped.

```text
B18:C20                       E18:E19
Branch        Department      (header left blank)
Centro        Accounting      =$G4>AVERAGE($G$4:$G$15)
Azcapotzalco  Logistics
```

Each filter is **Data**, **Sort & Filter**, **Advanced**, with **Copy to another location** selected, **List range** `$B$3:$G$15`, the criteria range selected to the last condition row and no further, and **Copy to** the single destination cell.

The formula criterion carries the three rules that are marked separately. Its header is blank, because a field name there makes Excel compare the text of the formula against that column instead of running it, and nothing matches while nothing goes wrong on screen. `$G4` is relative down and points at the first data row, so the filter walks the list re-evaluating it once per record. `$G$4:$G$15` is locked, because the thing being compared against must not move. The cell itself shows `FALSE` for row 4 and that is correct; it is showing you one evaluation out of twelve.

The third filter is the non-destructive way to answer "which departments are there". Remove Duplicates deletes rows out of the list and does not put them back after a save. The advanced filter with **Unique records only** ticked and the criteria range left empty writes the answer somewhere else and leaves all twelve records alone.

**Output**

```text
Extraction at B24, criteria B18:C20                       4 records
  Escobar   Ana       Centro        Accounting      12/03/1991  5,200
  Estrada   Beto      Azcapotzalco  Logistics       01/07/1994  4,100
  Espinosa  Fabián    Centro        Accounting      08/09/1993  5,600
  Peña      Hugo      Azcapotzalco  Logistics       04/12/1995  4,400

Average salary of the list = 5,491.67

Extraction at B32, criteria E18:E19                       6 records
  Reyes     Carla     Centro        Logistics       23/11/1989  6,300
  Espinosa  Fabián    Centro        Accounting      08/09/1993  5,600
  Nieto     Gabriela  Norte         Administration  19/02/1990  7,100
  Vega      Irene     Centro        Administration  27/08/1991  5,900
  Herrera   Karla     Azcapotzalco  Accounting      02/04/1994  6,800
  Ochoa     Luis      Centro        Logistics       11/10/1988  8,200

Unique departments at B40                                 3 rows
  Accounting
  Logistics
  Administration
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| All three results were produced by the Advanced dialog with Copy to another location, and no AutoFilter is in the workbook | 3 |
| The four records of the first extraction are right | 2 |
| The formula criterion has a blank header, a relative first data row and a locked comparison range | 2 |
| The six records above the 5,491.67 average are right | 2 |
| The three departments come out unique with the list left untouched | 1 |

**Most common mistake**

Retyping the headers over the criteria range instead of copying them. A trailing space is invisible, the field is not recognised, and the filter returns nothing while reporting no error. The second most common is writing the comparison as `>5491.67`, which is the right answer today and stops being the right answer the moment a salary changes.

### 15.3 · Integrate

**Solution**

The PivotChart is built from the report that already exists: click inside it, **PivotTable Analyze**, **Tools**, **PivotChart**, clustered column. In the **PivotChart Fields** pane the areas are called Filters, Legend (Series), Axis (Categories) and Values, so the grouped date goes into Axis (Categories) and Waiter into Legend (Series). **Field Buttons** on **PivotChart Analyze**, **Show/Hide**, is a menu that lists the four kinds separately rather than toggling them together: clearing the legend entry is the answer, and **Hide All** is a different answer that removes buttons the task never mentioned.

The slicer and the timeline come from **PivotTable Analyze**, **Filter**. Both leave an object on the sheet, which is what makes them gradeable at all: a filter arrow leaves nothing behind. The slicer's **Height**, **Width** and **Columns** are typed on the **Slicer** tab rather than dragged, and the timeline's level list is set to Months.

The drill. Double-clicking the value cell where May meets Nadia writes a new worksheet holding only the source rows behind that number, formatted as a table. It comes out with Excel's next free default name, so it is `Sheet1` or `Sheet2` depending on what the workbook already has; the name is not the evidence, the two rows and the total are. Sum the Charged column of that sheet and it has to equal the 565.00 you clicked. If it does not, the report is stale and needs Alt+F5, because the drill always reads the current source.

The advanced filter reaches the same two tickets from the other end. Criteria: Waiter is Nadia, and the date field written twice on one row for the two ends of May.

Neither result is live. The difference is what it costs to redo them. The extraction is rebuilt by editing one cell of the criteria range and reopening one dialog; the drill-through sheet has to be deleted and produced again from a refreshed report. The PivotTable behind both is the only thing in the workbook that updates on a refresh.

**Output**

```text
Drill-through sheet, from the May column of the Nadia series      2 rows

  06/05/2026  Nadia  Mains     PLA-15  5   85.00  425.00
  20/05/2026  Nadia  Desserts  POS-08  2   70.00  140.00

  Sum of Charged            565.00
  Cell that was clicked     565.00

Criteria range for the same two records
  Waiter    Date            Date
  Nadia     >=01/05/2026    <=31/05/2026

Extraction                                                        2 rows, total 565.00
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The PivotChart was made from the existing report, with the two fields in Axis (Categories) and Legend (Series) | 2 |
| Only the legend field buttons were cleared, from the Field Buttons menu, not Hide All | 1 |
| Slicer and timeline are objects on the sheet, sized by typed numbers, timeline set to Months | 2 |
| The drill-through sheet exists, holds the two tickets and sums to 565.00 | 3 |
| The criteria range reaches the same two records with the date field written twice on one row | 1 |
| The two routes are compared on what it costs to redo them | 1 |

**Most common mistake**

Filtering the report with the axis field's own filter arrow, or dragging Category into the Filters area, and calling it a slicer. Both filter the same report and neither leaves an object, so the sheet a grader opens has nothing on it to mark.

---

## Week 16 · What-if analysis

### 16.1 · Recognise

**Solution**

(a) Fifty thousand units at 100.00 against a 60.00 unit cost is 40.00 of contribution each, 2,000,000 in all, less 1,500,000 of fixed cost, and 15 per cent of what is left goes in tax.

(b) 37,500 units. The algebra is one line, 1,500,000 divided by the 40.00 each unit contributes, and the point of the tool is that the same three boxes answer the same question on a model nobody can rearrange. **Goal Seek Status** reports that a solution was found and shows **Target value:** 0 against **Current value:**, usually with a tail of decimals, because Goal Seek stops at a tolerance rather than landing exactly. Pointed at B9 it refuses outright: B9 holds a formula, and Goal Seek will not overwrite the model with a number. That refusal is the tool protecting the sheet, not a fault.

(c) The nine results below. Clicking any body cell shows `{=TABLE(,B2)}` in the formula bar, with an empty first argument because there is no row input and B2 as the column input. The braces mean an array and cannot be typed. Deleting one cell of the block returns "You cannot change part of a data table": the rectangle is one object and comes out whole or not at all. Worth saying out loud in class: below break-even this model applies the 15 per cent to a loss as well, so the 300,000 shortfall at thirty thousand units is reported as 255,000. That is what the formula in B14 says, and it is a modelling decision somebody made, not an Excel behaviour.

(d) All nine read 425,000. The table did run, nine times, and each time it collected a cell holding a typed constant. Nothing is red, no error appears, and the column of identical numbers is the only symptom.

**Output**

```text
(a)  B9   5,000,000
     B10  3,000,000
     B12    500,000
     B14    425,000

(b)  B2      37,500

(c)  units      net income
     30,000      -255,000
     35,000       -85,000
     40,000        85,000
     45,000       255,000
     50,000       425,000
     55,000       595,000
     60,000       765,000
     65,000       935,000
     70,000     1,105,000

     body cells      {=TABLE(,B2)}
     one cell deleted  "You cannot change part of a data table"

(d)  all nine cells  425,000
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four values in (a) | 2 |
| (b) answers 37,500 and explains why B9 is refused | 3 |
| The nine results in (c) | 3 |
| `{=TABLE(,B2)}` is reported and the delete message is named | 1 |
| (d) answers 425,000 nine times and says why nothing looks wrong | 1 |

**Most common mistake**

Reading the negative rows as an error in the table. They are the model saying the product loses money under thirty-seven and a half thousand units, which is the entire reason anybody opened Goal Seek in the first place.

### 16.2 · Apply

**Solution**

```excel
B5  =PMT(B2/12,B3*12,B4)
B6  =NPER(B2/12,B5,B4)
B7  =IF(AND(B6<=36,-B5<=5000),"Approve","Reject")
```

`B2/12` and `B3*12` are typed into the boxes themselves so the sheet stays readable and the rate and the periods agree. Putting the annual rate in raw is the single most common wrong answer in this objective, and it is caught by one sanity check: the payment times the term has to exceed the amount borrowed, because the excess is the interest. Here that is 363,614.38 against 285,000, so 78,614.38 of interest over four years, which is the right order of magnitude for 12.5 per cent.

The payment comes back negative because Pv was entered positive. That is Excel signing cash flows, not an error, and the sign has to be decided once and kept. NPER then needs Pmt and Pv carrying opposite signs, so `B5` goes in as it stands. Writing `-B5` there makes both positive, and the function answers -31.91 periods. A negative term means the signs are wrong even though the formula is spelled right, and it is the only warning you get.

Goal Seek on B3 with **To value** -5000 lands on 7.2438 years, which is 86.93 months. NPER reaches the same number from the other side, with `-5000` in **Pmt**, and two tools agreeing is worth more than either of them alone.

The two-variable table needs the reference in the corner, the whole rectangle H9:K14 selected before the dialog opens, and the two boxes filled the right way round: the amounts run across, so B4 is the **Row input cell**, and the rates run down, so B2 is the **Column input cell**. Set **Calculation Options** to **Automatic Except for Data Tables** first, because a data table reruns the whole model once per body cell on every keystroke anywhere in the workbook, and fifteen model runs per character is fifteen too many.

**Output**

```text
B5   -7,575.30      (payment leaving, monthly)
B6           48     periods
B7       Reject     48 months is over 36, and 7,575.30 is over the 5,000 budget

NPER written with -B5 instead        -31.91

Goal Seek, Set cell B5, To value -5000, By changing cell B3
  B3   7.2438 years   =  86.93 months
  NPER(B2/12,-5000,B4)  86.93 months

Two-variable data table, payments

              250,000     285,000     320,000
  10%       -6,340.65   -7,228.34   -8,116.03
  11%       -6,461.38   -7,365.97   -8,270.57
  12%       -6,583.46   -7,505.14   -8,426.83
  13%       -6,706.87   -7,645.84   -8,584.80
  14%       -6,831.62   -7,788.05   -8,744.47
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| PMT and NPER were built from the Financial list with `B2/12` and `B3*12` in the boxes, not hard numbers | 2 |
| -7,575.30 and 48, with the sign convention explained | 2 |
| The `-B5` version is reported as -31.91 and read as a sign fault | 1 |
| AND is nested inside IF's Logical_test and B7 reads Reject | 1 |
| Goal Seek gives 7.2438 years and NPER confirms 86.93 months | 2 |
| The whole rectangle was selected, Row and Column input cells the right way round, fifteen payments right | 2 |

**Most common mistake**

Filling the data table body by copying the PMT formula across and down with the right absolute references. It produces the same fifteen numbers, it takes longer, and there is no `{=TABLE(B4,B2)}` anywhere in the block for a marker to find.

### 16.3 · Integrate

**Solution**

```excel
B4  =VLOOKUP(B5,Suppliers!$A$2:$B$4,2,FALSE)
```

With `Lira` in B5 the unit cost comes back as 60.00 and the model returns last week's 425,000, which is the check that the lookup did not change the answer, only where the answer comes from.

The three scenarios are stored, not copied. **Add** goes from one straight into the next without leaving the dialog, and the names are what appear in the report, so they have to be words. **Summary...** with **Result cells** B12 and B14 writes a sheet called Scenario Summary, and that sheet is what gets opened when the work is marked.

Break-even is Goal Seek run three times, once per scenario shown, with **Set cell** B14, **To value** 0 and **By changing cell** B2. The answers say something the summary does not: break-even depends only on the contribution per unit, so the units input moved it not at all, the price and the supplier moved it a great deal. Going from Cautious to Ambitious the contribution goes from 31.50 to 50.00 and the break-even volume falls by more than seventeen thousand units.

B4 cannot be a changing cell in any of the three. It holds the VLOOKUP, and a scenario stores a constant, so showing a scenario would write a number over the formula and cut B4 loose from `Suppliers` for good. Nothing later puts it back, and the next scenario carries the same dead number. The supplier name in B5 is the input; B4 is a result of it.

Three copies of the sheet would have reached the same comparison. What a grader finds on them is three sheets. There is no scenario to open, no Scenario Summary to read, no way to show one set of inputs on the live model and no record anywhere of what was changed or why, which is the exact mess Scenario Manager exists to prevent.

**Output**

```text
Scenario Summary, result cells B12 and B14

                     Cautious      Planned     Ambitious
  Units                35,000       50,000        62,000
  Price                 95.00       100.00        108.00
  Supplier            Central         Lira         Bajío
  Unit cost (B4)        63.50        60.00         58.00
  Operating profit   -397,500      500,000     1,600,000
  Net income         -337,875      425,000     1,360,000

Break-even units, Goal Seek on B2 against a net income of 0

  Cautious    47,619.05     contribution 31.50
  Planned     37,500.00     contribution 40.00
  Ambitious   30,000.00     contribution 50.00
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| B4 is a locked exact-match VLOOKUP over `Suppliers` and returns 60.00 for Lira | 2 |
| Three named scenarios exist in Scenario Manager with B2, B3 and B5 as changing cells | 3 |
| A Scenario Summary sheet exists with B12 and B14 as result cells, and its six figures are right | 2 |
| The three break-even volumes were found with Goal Seek and are right | 2 |
| The answer on why B4 cannot be a changing cell is about the formula, not about the dialog | 1 |

**Most common mistake**

Building the three cases as three copies of the sheet and writing a paragraph comparing them. Every number is right, the comparison is sound, and the objective asked for scenarios: reopening Scenario Manager on the handed-in file reads "No Scenarios defined."

---

## Week 17 · Printing, views and the final exam

### 17.1 · Recognise

**Solution**

(a) C2. Excel freezes everything above the selected cell and everything to its left, so the anchor for row 1 plus columns A and B is the cell below row 1 and to the right of column B. It reads back as `SplitRow 1` and `SplitColumn 2`. **Freeze Top Row** ignores the selection entirely and freezes exactly one row, `SplitRow 1` and `SplitColumn 0`, so the country names in column A scroll off to the left and nothing announces it. The cheapest proof of a freeze is to reopen the menu: the first entry now reads **Unfreeze Panes**. A freeze also draws one thin dark line where a split draws two thick grey bars, and a split scrolls in both halves.

(b) Setting a print area writes a sheet-scoped defined name, and so does setting print titles. If those names are not in **Name Manager**, no print area was set, whatever came out of the printer.

(c) `&P` and `&N` are fields, so they resolve per page and per job. Typed as literal text they resolve to nothing: the same eight pages all carry the words `Page 3 of 8`, and page one is wrong the moment it prints.

(d) The Ctrl+P pane is two things at once. Orientation, margins and scaling are the sheet's own settings shown in another place, so they write back. Copies, what to print and collation belong to this print job only and are gone when the pane closes. Students expect all of it to be sticky and half of it is not.

**Output**

```text
(a)  anchor cell   C2          SplitRow 1   SplitColumn 2
     Freeze Top Row            SplitRow 1   SplitColumn 0

(b)  'World Data 2023'!Print_Area    ='World Data 2023'!$A$1:$J$197
     'World Data 2023'!Print_Titles  ='World Data 2023'!$1:$1
     Page Break Preview greys columns K to AI

(c)  page 3, centre   Page 3 of 8
     page 3, right    World Data 2023
     typed literally  Page 3 of 8 on all eight pages

(d)  writes back to the sheet   Landscape Orientation
                                Fit All Columns on One Page
     this print job only        Copies 3
                                Print Entire Workbook
                                Collated
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) answers C2 with both readback numbers, and both numbers for Freeze Top Row | 3 |
| (a) names a proof that separates a freeze from a split | 1 |
| (b) gives both defined names with what each refers to | 3 |
| (c) gives both footer lines and what a literal footer prints | 1 |
| (d) sorts the five settings correctly into the two groups | 2 |

**Most common mistake**

Answering B2 in (a), because two things are being kept and B2 feels like the second cell. The rule counts what stays, not how many things there are: columns A and B both have to be left of the anchor, and that puts it in column C.

### 17.2 · Apply

**Solution**

The order matters. Setting the print area first is what makes the page count mean something, and the two numbers are the cheapest evidence in the whole exercise that the sheet was actually reduced rather than reformatted.

`Print_Area` and `Print_Titles` are sheet-scoped defined names written by the two commands. Nothing else writes them, and typing the range into the **Print area:** box on the **Sheet** tab of Page Setup writes the same name, which is the legitimate second route when the task hands you an address instead of a range to select.

The one pass through **Page Setup** is the graded route for objective 1.3.1. Everything the five ribbon galleries do lives on those four tabs, and doing it there is one operation with one undo step. Reopening the dialog is the check: the **Page** tab shows **Fit to** 4 wide by 5 tall with **Adjust to** back at 100 per cent, because the two scaling buttons are exclusive and setting one resets the other without saying so. Fit to is a ceiling and not a target, so the counter does not have to reach twenty; report what it says.

The three copies. Freezing the first column gives `SplitRow 0` and `SplitColumn 1`. Freezing at B4 keeps rows 1 to 3 and column A, `SplitRow 3` and `SplitColumn 1`. The split is not a freeze at all: two thick grey bars instead of one thin line, and both halves scroll on their own, which is how you tell them apart without going near the ribbon.

The PDF. **Options** is the whole step. Without it, **Publish what** stays on **Active sheet(s)** and "export the entire workbook" produces one sheet, which is the most common way this objective is failed.

Zoom and windows. The slider cannot land on 85 and neither can Ctrl with the wheel, so the **Zoom** dialog and its **Custom** box are the only route to an exact percentage. **New Window** is the one that a snapped pair of desktop windows cannot imitate: two windows onto one file, both captions carrying the file name with a number appended, and typing in one showing up in the other immediately.

**Output**

```text
Page counter under Ctrl+P
  before the print area     1 of 20
  after Set Print Area      1 of 8
  after the Page Setup pass  report what the counter says; Fit to 4 by 5 is a ceiling

Name Manager
  'World Data 2023'!Print_Area    ='World Data 2023'!$A$1:$J$197
  'World Data 2023'!Print_Titles  ='World Data 2023'!$1:$1

Page tab, reopened
  Fit to: 4 page(s) wide by 5 tall,  Adjust to: 100 %

The three copies
  freeze first column   SplitRow 0   SplitColumn 1
  freeze at B4          SplitRow 3   SplitColumn 1
  split past column C   two grey bars, both halves scroll, menu still reads Freeze Panes

PDF
  Entire workbook       4 sheets
  Options skipped       1 sheet, the one on screen

Zoom       status bar reads 85%
Windows    Exercise 4 Excel.xlsx  -  1
           Exercise 4 Excel.xlsx  -  2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The print area was set with Set Print Area and both page counts are reported | 2 |
| Name Manager holds both names with the right references | 2 |
| Every page setting was made in one pass through the Page Setup dialog, not from the galleries | 2 |
| The three copies read back correctly and the split is told apart from the two freezes | 2 |
| The PDF holds all four sheets and Options is named as the step that did it | 1 |
| Zoom is exactly 85 per cent from the dialog, and the two window captions are reported | 1 |

**Most common mistake**

Selecting A1:J197 and using **Print Selection** in the Ctrl+P pane. It prints the right ten columns once, stores nothing, and the next print is all thirty-five columns again. Name Manager is empty, so there is nothing to mark whatever came out of the printer.

### 17.3 · Integrate

**Solution**

The anchor on `Tickets` is C2: row 1 is the header, columns A and B are Date and Waiter, and the anchor is the cell below and to the right of everything that stays.

The grouped page setup is worth doing slowly. Ctrl-click the three tabs and open the dialog once, and everything on **Page**, **Margins** and **Header/Footer** lands on all three sheets in a single operation. The two boxes on the **Sheet** tab that describe a particular sheet, **Print area:** and **Print titles**, are unavailable while a group is selected, so those two are set sheet by sheet afterwards. Ungroup the tabs before you carry on, or the next thing you type goes into three sheets at once.

The footer's right section is `&A`, a field and not a word, so it resolves per sheet: `Churrumpin`, `Credit`, `Tickets`. That is the difference between a footer that describes the page it is on and three identical labels, and it is the reason the objective says to use the buttons above the boxes.

The Compatibility Checker is the third leg of objective 1.5.4, after the Document Inspector in week 9 and the Accessibility Checker in week 11. It is also the only one of the three that leaves a record: **Copy to New Sheet** writes a dated, itemised report into the workbook that survives the dialog closing. The other two report into a dialog or a pane and are gone when you close them.

**Custom Views** is greyed out because the workbook holds an Excel table, `Tickets2026`, from weeks 10 and 14. A workbook containing a table cannot store custom views at all. There is no message and no explanation, just a dead button.

The template. Picking **Excel Template** in the type list makes Excel redirect the Save As location to the templates folder without asking, which is the product saying that a template is not a file you keep next to your data, it is a file the New pane goes looking for.

**Output**

```text
Freeze on Tickets      anchor C2       SplitRow 1   SplitColumn 2

Grouped page setup, three tabs Ctrl-clicked
  applied to all three   orientation, scaling, margins, centring, header and footer
  set sheet by sheet     Print area, Print titles     (greyed while grouped)

Footer, right section &A
  Churrumpin sheet   Churrumpin
  Credit sheet       Credit
  Tickets sheet      Tickets

Check for Issues
  Compatibility Report sheet, written by Copy to New Sheet, in the workbook

Custom Views           greyed out, the workbook holds the table Tickets2026

Export
  PDF, Entire workbook   one continuous file, page count equal to the sheets added up
  Excel Template         .xltx, saved into the templates folder without being asked
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The freeze anchor is C2 and reads back as 1 and 2 | 1 |
| Print area and repeated titles are set on `Tickets` and both names are in Name Manager | 2 |
| The three sheets were set up in one grouped pass, and the two Sheet tab exceptions are named | 2 |
| The footer is built from fields and `&A` is shown resolving differently on each sheet | 1 |
| A Compatibility Report sheet is in the workbook and is explained as the only record any of the three tools leaves | 2 |
| The Custom Views answer names the Excel table | 1 |
| The PDF covers the whole workbook and the template landed in the templates folder | 1 |

**Most common mistake**

Doing the page setup three times, once per sheet, from the ribbon galleries. Every sheet ends up correct, the work took three times as long, and the objective that says apply a page setup in one operation was never attempted. The runner-up is typing the sheet name into the footer as text, which prints the right word on one sheet and the wrong word on the other two.
