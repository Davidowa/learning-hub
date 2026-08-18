# Exercises · Information Management and Analysis · TIA501

Fifty-one exercises across the seventeen weeks, three per week. Recognise reads a workbook or
a route and predicts what happens, Apply performs a task against a specification, and
Integrate ties the week to what came before.

This course grades differently from the programming courses in this repository, and the
difference is the point. The certification does not ask whether the cell ended up bold and
filled. It asks how you got there. Two clicks on the Home tab produce the same workbook and
earn nothing; the graded route opens Format Cells with Ctrl+1 and applies both from inside
the dialog in one operation. So the statements name the route, and the rubrics spend points
on it. Solutions live in solutions.en.md.

Nothing here depends on XLOOKUP, FILTER, SORT, UNIQUE, SEQUENCE, SORTBY, RANDARRAY or LET.
The course targets the 2019 objective domains and those functions do not exist there.

---

## Week 01 · Course framing and the rule that grades every task

### 01.1 · Recognise

**Two click logs, one picture**

A colleague formatted the same header range on two copies of the same workbook. In both copies B2:E2 holds the four quarter headings Q1, Q2, Q3 and Q4, and in both copies the goal was white bold text on a dark blue fill with a border round the block and between the cells.

This is the click log kept on copy A.

```text
Home > Font > Bold
Home > Font > Font Color > White
Home > Font > Fill Color > Dark blue
Home > Font > Borders > All Borders
```

This is the click log kept on copy B.

```text
Ctrl+1
  Font tab   > Font style > Bold, Color > White
  Fill tab   > Background Color > Dark blue
  Border tab > Line Style, Color, then Outline and Inside
OK
```

Answer four things. First, what the two ranges look like on screen once each log finishes. Second, how many operations each log spent. Third, what is left in B2:E2 after pressing Ctrl+Z exactly once on each copy. Fourth, which of the two answers an item worded "apply the cell formats from the Format Cells dialog box", and what the other one earns.

### 01.2 · Apply

**The undo audit, run on your own machine**

In a new workbook, type the four headings Model, List price, Sale price and Difference into A1:D1. Type the same four into A5:D5. Below the first heading row, in A2:D2, type `G414`, `190000`, `195000` and `5000`.

Format A1:D1 from the Home tab only: bold, a white font colour, a dark blue fill and All Borders. Count the clicks. As soon as that row is done, and before touching anything else, press Ctrl+Z once, write down what is left on screen, then press Ctrl+Y to put it back.

Now format A5:D5 to the same look in one trip through Ctrl+1. On the Font tab set Font style to Bold and Color to White. On the Fill tab pick the same dark blue. On the Border tab set the Line Style and the Color first, then click Outline and then Inside. One OK at the end. Again, straight away, press Ctrl+Z once, write down what is left, then Ctrl+Y.

Write your four findings into F1, F2, F3 and F4: the operation count for each row, and the state of each row after its single undo. Hand in the workbook.

The order of the two audits matters and the exercise is testing whether you understand why.

### 01.3 · Integrate

**Eight items, and the route each one accepts**

Below are eight tasks worded the way a certification item words them, each with the route a candidate took.

| # | The item | The route the candidate took |
|---|---|---|
| 1 | Apply the font colour, the fill and the border to A1:F1 from the Format Cells dialog box | Home tab, Font group, three buttons |
| 2 | Apply the Accounting number format with two decimals to C2:C40 | Home tab, Number group, Accounting Number Format, then Increase Decimal |
| 3 | Format D2:D40 so negative amounts show in red parentheses | Home tab, Number group, Comma Style |
| 4 | Return the list of distinct regions to H2 | `=UNIQUE(B2:B41)` |
| 5 | Look up the salesperson who took order 4471 | `=XLOOKUP(4471,A2:A41,C2:C41)` |
| 6 | Apply a diagonal border across B7 | Home tab, Font group, the Borders menu |
| 7 | Give the header block a white bold font and a dark blue fill in one operation | Ctrl+1, Font tab, then Fill tab, then one OK |
| 8 | Apply the Bad cell style to the rows that went over budget | Home tab, Styles group, Cell Styles, Bad |

Say for each row whether the route earns the mark. Where it does not, name the route that does. Two of the eight cannot be answered at all on a lab machine running Office 2019, so for those name the function, say which of the four exams in the family lists it, and say why the course will not build a graded step on it.

Then close with the term itself. From the assessment table, give the week each of the two midterms falls in, the share of a midterm that is the classroom exam, and the one condition attached to the other share on midterm 1.

---

## Week 02 · Session 4 · First contact with Excel

### 02.1 · Recognise

**Four fills into the same empty column**

Open `Exercise 1 Excel.xlsx` and look at `Hoja1`. The title sits in A1, the headings in A2:F2 and six models in rows 3 to 8. Column H is empty.

Four people were asked to put a counter into H3 and downwards. Each did it differently.

(a) Type 5 in H3. Select H3:H9. Home tab, Editing group, Fill, Series. Series in Columns, Type Linear, Step value 6. OK.

(b) Type 5 in H3. Select H3 alone. Home tab, Editing group, Fill, Series. Series in Columns, Type Linear, Step value 6, Stop value 30. OK.

(c) Type 5 in H3. Point at the fill handle and drag from H3 down to H9.

(d) Type 5 in H3 and 11 in H4. Select H3:H4. Drag the fill handle down to H9.

Say for each one which cells hold which values when the mouse is released. Then two more things: after which of the four does the Auto Fill Options button appear at the bottom right of the block, and which of the four cannot be produced by the fill handle no matter how it is dragged.

### 02.2 · Apply

**The header block of Exercise 1, done the graded way**

Work on `Hoja1` of `Exercise 1 Excel.xlsx`, the workbook you already have. The title `Detalle de ventas` is in A1, the headings in A2:F2, and the six models in rows 3 to 8. List price is column B, sale price is column C, the difference is column D, the percentage of difference is column E and the days on market is column F.

Six tasks. The route is part of each one.

1. Select A1:F1. Ctrl+1. On the Alignment tab set Horizontal to Center Across Selection and Vertical to Center. Without leaving the dialog, on the Font tab set the size to 14 and the style to Bold. One OK. The title must not be merged.

2. Select A2:F2. One trip through Ctrl+1. Font tab: Bold, Color white. Fill tab: a dark background colour. Alignment tab: Horizontal Center, Vertical Center, and the Wrap text box selected. Border tab: choose the Line Style and the Color first, then click Outline, then click Inside. One OK.

3. Select B3:D8. Home tab, Number group, the Number Format list, Accounting. Then Decrease Decimal until no decimals show. This one belongs on the ribbon and nowhere else.

4. Select E3:E8. Home tab, Number group, Percent Style. The cells already hold 0.03, 0.02 and the rest, so they are formatted, never retyped.

5. Format row 3 the way you want the data rows to look, then copy that formatting onto row 5 and onto row 7 with the brush locked. Double-click Format Painter, paint both rows, press Esc.

6. Select F3:F8 and apply the Neutral cell style from Home tab, Styles group, Cell Styles. Then select F8 alone and use Home tab, Editing group, Clear, Clear Formats. Say what F8 keeps, what it loses, and how that differs from pressing Delete on the same cell.

Two checks before you submit. Straight after task 2, select A2:F2 and press Ctrl+Z once, then Ctrl+Y. Everything the dialog set has to go and come back together. And after task 1, click the title and read the Name Box.

Hand in the workbook.

### 02.3 · Integrate

**The audit of a workbook that already looks right**

A student handed in `Hoja2` of the same workbook, four models in rows 3 to 6, and on screen it looks finished. Six pieces of evidence were collected before marking.

| # | What the task asked for | What the evidence shows |
|---|---|---|
| 1 | Apply the font colour, the fill and the border to A2:F2 from the Format Cells dialog box | One Ctrl+Z removes the border and leaves everything else |
| 2 | Centre the title across A1:F1 without merging | The Name Box reads A1:F1 when the title is selected |
| 3 | Fill the projection column from the Series dialog | The Auto Fill Options button is sitting at the bottom right of the filled block |
| 4 | Apply the Percentage format to E3:E6 | E3 shows 8% and the formula bar reads 0.08 |
| 5 | Apply the Percentage format to E3:E6 | E4 shows 0.03% and the formula bar reads 0.0003 |
| 6 | Copy the formatting of row 3 onto rows 5 and 6 | Row 5 matches row 3, row 6 does not |

For each row, name the route that was actually taken, say whether the item would score, and give the route that has to be run instead.

Then three closing points. Which of the six is a damaged sheet rather than a wrong route. Which two of the six are settled by reading the formula bar, and which one by reading the Name Box. And finally, repair rows 2 and 6 in the workbook and hand it in, leaving the repair provable by the same evidence that exposed it.

---

## Week 03 · Sessions 5 and 6 · Structure and references

### 03.1 · Recognise

**Nine formulas and one deleted column**

Part one. A sheet holds A1 with the number 8, A2 showing 12 but entered as text, A3 with 4 and A4 with 3. Say what each of these returns.

```excel
=A1+A2*2
=A1*A2
=-A4^2
=2^A4^2
=A1-A3*A4^2
=20%*A1*10
="Total "&A1+A3
=A1/(A3-4)
=A2+"a"
```

For three of them, say which rule of precedence produced the answer.

Part two. A second sheet is named `Budget`. Row 1 holds the headings, column B holds the planned amounts, column C holds the actual amounts, and D2 holds `=C2-B2`. Someone selects column B by its heading, goes to the Home tab, Cells group, clicks the arrow on Delete and clicks Delete Sheet Columns.

Say which column the actual figures sit in afterwards, which cell now holds the difference formula, what the formula bar shows in it, what the cell displays, and what it takes to repair it.

### 03.2 · Apply

**One formula, sixteen cells, and a name with a scope**

Open `Exercise 5 Excel.xlsx`. Add a sheet, name it `Grid`, and give its tab a colour.

1. Type 10 into F1. Select F1:I1. Home tab, Editing group, Fill, Series. Series in Rows, Type Linear, Step value 10. OK. The fill handle is not the route here.

2. Type the four unit prices down E2:E5: 12.50, 18.00, 24.75 and 31.20.

3. In F2 write one formula that returns the line total for that quantity at that price, and fill it across and down to cover F2:I5. Build the reference with F4 rather than by typing dollar signs, and stop the cycle on the form each half of the formula needs.

4. Select F1:I1 and go to the Formulas tab, Defined Names group, Define Name. Name it `Quantities`. Set the Scope to the sheet Grid, not to the workbook. Put `Quantity headers of the price grid` in the Comment box. Check that the Refers to box reads an absolute reference to the sheet. The Name Box is not the route.

5. Press F5, pick `Quantities` from the Go to list, click OK, and read the Name Box afterwards.

6. Click I5. Formulas tab, Formula Auditing group, Trace Precedents. Click it a second time. Say how many arrows appear on the first click and how many the second one adds. Then open the arrow on Remove Arrows and remove only the precedent arrows.

7. Select F2:I5 and give it two decimals from the Home tab, Number group.

Hand in the workbook with the grid filled, the name defined and the tab coloured.

### 03.3 · Integrate

**The Earnings sheet, computed with references only**

Open `Exercise 5 Excel.xlsx` and go to the `Earnings` sheet, the ironmonger's ledger. The VAT rate sits in B3 at 0.16 and the discount rate in B4 at 0.1. The headings are in row 6 and the fourteen order lines run from row 7 to row 20, with the quantity in B, the item in C, the unit cost in D and the unit price in E. Columns F to K are empty under the headings Total Cost, Total Revenue, Discount, Net Revenue, Earnings and % Earnings.

Fill F7:K20 with one formula per column, written once in row 7 and filled down. No function of any kind this week: the six answers come out of the operators. Total cost is the quantity times the unit cost. Total revenue is the quantity times the unit price. The discount is the total revenue times the rate in B4. Net revenue is the total revenue less the discount. Earnings are the net revenue less the total cost. The last column is the earnings over the net revenue.

The rate in B4 has to be locked with F4 so the fill does not walk off it.

Then five more things, each with the route named.

1. Click the `Precedence` tab, Ctrl+click the `Earnings` tab so the title bar reads Group, and in one edit type your name into A30 and today's date into B30. Format A30:B30 in one trip through Ctrl+1. Then right-click a tab and choose Ungroup Sheets before you touch anything else.

2. Format the heading block A6:K6 in one trip through Ctrl+1, the same way you formatted Exercise 1 last week.

3. Format F7:J20 as Accounting with two decimals from the Home tab, Number group. Format K7:K20 with Percent Style and one decimal from the same group.

4. Click any single cell. Home tab, Editing group, Find & Select, Find. Click Options to expand the dialog. Set Within to Sheet and Look in to Formulas, type `$B$4` into Find what, and click Find All. Report the count in the result list. Then change Look in to Values, click Find All again, and report that count too. Explain the difference in one line.

5. Click J20. Trace Precedents twice and say how many arrows each click drew. Then open the Watch Window from the same group and add a watch on K20.

Hand in the workbook.

---

## Week 04 · Sessions 7 and 8 · Statistical, text and date

### 04.1 · Recognise

**One column of children, one column of salaries**

Open `Exercise 6 Excel.xlsx` and go to the `Employees` sheet. The headings sit in row 2 and seven employees in rows 3 to 9.

| Row | B · Registration number | C · Last name and Name | D · Area | E · Position | F · Salary | G · Status | H · Children |
|---|---|---|---|---|---|---|---|
| 3 | 25 | DUARTE, Alberto | MKT | Manager | 4500 | Married | 3 |
| 4 | | LÓPEZ, Liliana | ADM | Secretary | 1800 | Married | 2 |
| 5 | | MARTÍNEZ, Sebastián | MKT | Designer | 1750 | Single | |
| 6 | | NUÑEZ, Cecilia | RRHH | Manager | 4000 | Single | |
| 7 | | PÉREZ, Daniel | ADM | auxiliar | 890 | Married | 1 |
| 8 | | RAMIREZ, Laura | MKT | Secretary | 1700 | Single | |
| 9 | | SUAREZ, Carlos | RRHH | auxiliar | 780 | Married | 4 |

Six of the seven names in column C carry one trailing space. One does not.

Say what each of these returns.

```excel
=COUNT(H3:H9)
=COUNTA(H3:H9)
=COUNTBLANK(H3:H9)
=COUNT(B3:B9)
=SUM(F3:F9)
=AVERAGE(F3:F9)
=MAX(F3:F9)
=MIN(F3:F9)
=LARGE(F3:F9,2)
=SMALL(F3:F9,2)
=LEN(C3)
=LEN(C6)
```

Then three questions. Why COUNT and COUNTA agree over H3:H9 when the four-cell example in class had them disagree. Why COUNTA and COUNTBLANK add to exactly seven over that same range. And what the two LEN answers tell you about what will happen in week 13, when a lookup is keyed on that name column.

### 04.2 · Apply

**Sixty students, cut apart and put back together**

Open `Excel 13.xlsx` and work on the `Text` sheet. The headings sit in row 2 and sixty students run from row 3 to row 62. The ID is in column B and was typed as text, which is why 024300 keeps its leading zero. The given name is in C, the father's last name in D, the mother's last name in E and the date of birth in F. Row 3 is jennifer lópez pérez, born on 6 July 2001.

Every function goes in through the Formulas tab, Function Library group, and its Function Arguments dialog. Reading the Formula result line at the bottom left of the dialog before clicking OK is part of the task.

1. G3, the full name: CONCAT over C3, a space, D3, a space, E3. Fill down to G62.
2. H3: UPPER over G3. I3: PROPER over G3. Fill both down.
3. J3, the account name: TEXTJOIN with a full stop as the Delimiter, `Ignore_empty` set to TRUE, and three parts, the first character of C3, then D3, then the first character of E3.
4. P3: LEFT over B3, three characters. Q3: RIGHT over B3, three characters. R3: MID over B3 with `Start_num` 4 and `Num_chars` 2.
5. S3: LEN over G3.
6. L3: DAY over F3. M3: MONTH over F3. N3: YEAR over F3.
7. In T3 type `24300` as a number. Select T3, press Ctrl+1, go to the Number tab, pick Custom and write `000000` in the Type box. Then in U3 put LEFT over T3, three characters, and compare the answer with P3. Explain the difference in one line.
8. In V3 write `=F3*1` and leave the cell on General.
9. Select F3:F62 and press Ctrl+1. On the Number tab build the near miss with the Date category first, then click Custom and edit the Type box so the date reads as day, month name and four-digit year.

Hand in the workbook. Say in one line, for step 9, which code you wrote and why the year code on this machine is not the one an English keyboard would suggest.

### 04.3 · Integrate

**The totals block of the Earnings sheet**

Go back to `Exercise 5 Excel.xlsx`, the `Earnings` sheet you filled in last week. The four labels are already sitting in H22 to H25: SUBTOTAL, VAT, TOTAL and TOTAL EARNINGS. Put the figures in I22 to I25, under these definitions. The subtotal is the net revenue of all fourteen order lines. The VAT is the subtotal times the rate in B3. The total is the subtotal plus the VAT. The total earnings are the earnings of all fourteen lines.

1. Before writing anything, define two names from the Formulas tab, Defined Names group, Define Name. `Net_Revenue` for I7:I20 and `Line_Earnings` for J7:J20, both scoped to the sheet Earnings, both with an absolute Refers to.

2. Write the four formulas using the names, not the addresses. SUM comes in through the Formulas tab, Function Library group, either from the arrow under AutoSum or from Insert Function, and either way the Function Arguments dialog is what fills the argument box.

3. Lock B3 with F4 in the VAT formula.

4. Select J7:J20 and I22:I25 and give them a custom number format written into the Type box, three sections, so that a positive figure reads with a thousands separator and two decimals, a negative one reads in red and in parentheses, and a zero reads as a dash. Build the near miss with the Number category first, then click Custom.

5. In K22 put TODAY through Formulas, Function Library, Date & Time. In K23 stamp the same date with Ctrl+semicolon. Read both formula bars, and write into K24 which cell will still be right when the file is opened in November.

Hand in the workbook. Name the two rows of column J where the third section of your format is doing the work, and the two rows where the second one is.

---

## Week 05 · Rules, sparklines and IF

### 05.1 · Recognise

**Three rules on one range, and only one colour showing**

A sheet named `Deposits` holds six figures taken from the branch report of Exercise 11.

| Cell | Amount |
|---|---|
| B2 | 5000 |
| B3 | 2000 |
| B4 | 1500 |
| B5 | 4500 |
| B6 | 1200 |
| B7 | 7000 |

Three rules were written against `B2:B7`. The Conditional Formatting Rules Manager lists them in this order, and Stop If True is ticked on the first one only.

| Priority | Rule | What it applies |
|---|---|---|
| 1 | Cell Value > 4000 | Green fill |
| 2 | Formula: `=MOD(ROW(),2)=0` | Yellow fill |
| 3 | Cell Value < 2000 | Red font |

Answer three things. First, cell by cell, the fill and the font colour B2 to B7 end up showing. Second, the active cell is D1 and you open Conditional Formatting, Manage Rules...: say what the list shows and name the one setting that fixes it. Third, say which cells change appearance if Stop If True is cleared on rule 1, and give the reason.

### 05.2 · Apply

**Two rules the exercise pack does not have**

Open `Exercise 3 Excel.xlsx` and work on the sheet `Conditional formatting`. The names are in A4:A33, the status in B4:B33 and ten subject columns in C4:L33. Row 3 carries the headings and row 34 carries a stray group of figures left over from an older version of the file. Neither belongs inside any range you select.

Do four things, by the route named.

1. In W1 type `Cut` and in W2 type `85`.
2. Select C4:L33. Home tab, Styles group, Conditional Formatting, Highlight Cells Rules, Greater Than.... Do not type the number into the dialog: click the collapse arrow at the right of the left box, click W2 on the sheet, click the arrow again to expand the dialog. Open the **with** list and take Green Fill with Dark Green Text. OK.
3. Select A4:L33 with A4 as the active cell. Conditional Formatting, New Rule.... In Select a Rule Type click Use a formula to determine which cells to format. Click into the Format values where this formula is true box and press F2 before you touch an arrow key. Type `=$B4="International"`. Click Format..., set the font to bold on the Font tab, then move to the Fill tab without closing that dialog and pick a light fill. OK, then OK again.
4. Conditional Formatting, Manage Rules.... Set Show formatting rules for to This Worksheet.

Report five things. The fill of C4, C5 and L4 while W2 holds 85. What happens to H13:L13, which is empty on this sheet. The two Applies to ranges exactly as the manager prints them. How many rows the formula rule paints. And whether C4 changes when you set W2 to 65, which you then set back to 85.

### 05.3 · Integrate

**One column of averages, one sparkline column and the boundary underneath**

Same workbook, sheet `Sparklines`. The headings are in row 2, thirty students sit in rows 3 to 32, the three yearly scores are in C, D and E, and F is empty under the heading Sparkline.

1. In J1 type `Cut` and in J2 type `80`. Select J2, then Formulas tab, Defined Names group, Define Name. In the New Name dialog type `Cut`, set Scope to Workbook, check that Refers to reads `=Sparklines!$J$2`, and click OK.
2. Click G3. Formulas tab, Function Library group, Insert Function. Category Statistical, function AVERAGE, OK. In Number1 drag over C3:E3. Read Formula result = before you commit, then OK. Fill G3 down to G32.
3. Click H3. Formulas tab, Function Library group, Logical, IF. In Logical_test click G3 and type `>=Cut`. In Value_if_true type `Above` and in Value_if_false type `Below`, both without quotation marks. Read Formula result =, then OK. Fill H3 down to H32.
4. Select F3:F32. Insert tab, Sparklines group, Line. In Create Sparklines put C3:E32 in Data Range, confirm that Location Range already reads `$F$3:$F$32`, and click OK. Then on the Sparkline contextual tab, Group group, click Axis and set Same for All Sparklines under both Minimum Value Options and Maximum Value Options.
5. Select H3:H32. Home tab, Clipboard group, Copy. Click I3. Home tab, Clipboard group, the arrow under Paste, then Paste Special.... Select Values, OK, then press Esc.

Report five things. How many students come out Above and how many Below. What H3 holds for Carolina Dubois and why. What the two counts become if the test is rewritten as `G3>Cut`, and which student that change moves. What the formula bar shows when F3 is selected, and what it shows when I3 is selected. And one line saying why step 4 would be worth no marks without the Axis setting.

---

## Week 06 · IF in depth, then the midterm

### 06.1 · Recognise

**Seven readings of one comparison**

A sheet holds two cells. C2 holds 70, typed straight in. C3 holds 70 as well, typed with a leading apostrophe, and it sits against the left edge of its cell while C2 sits against the right.

Say what each of these seven formulas puts in its cell.

```excel
=IF(C2>=70,"Pass","Fail")
=IF(C2>70,"Pass","Fail")
=IF(C2<>70,"Pass","Fail")
=IF(C2>=70,"Pass")
=IF(C2>=80,"Pass")
=IF(C2>="70","Pass","Fail")
=IF(C3>=70,"Pass","Fail")
```

Then answer two more. Which of the seven puts a word into the report that no reader wants to see there, and where that word came from. And what tells C2 apart from C3 on screen before any formula is written.

### 06.2 · Apply

**Both branches are a calculation**

Open `Exercise 7 Excel.xlsx` and go to the sheet `Exercise3`, the EMPRESA GANADORA block. D4 holds the card payment fee, 0.1, and D5 the cash payment discount, 0.05. Ten items sit in rows 8 to 17 with the list price in B, the payment method in C, and D empty under the heading Total Sales price.

A card payment adds the fee to the list price. A cash payment takes the discount off it.

Build the formula this way and no other. Click D8. Formulas tab, Function Library group, Logical, IF. In Logical_test click C8 and type `="Credit Card"`. In Value_if_true type `B8*(1+D4)`. In Value_if_false type `B8*(1-D5)`. Before you commit, put the insertion point on the `D4` inside the Value_if_true box and press F4, then do the same to the `D5` in the other box, so both read with dollar signs. Read Formula result = at the bottom left. OK, then fill D8 down to D17.

Then select D8:D17 and press Ctrl+1. On the Number tab pick Currency with two decimal places. Nothing from the Home tab.

Report the ten values, the total of D8:D17, and what D9 and D10 would have shown if F4 had never been pressed. Give the reason for each of those two.

### 06.3 · Integrate

**The one row where two correct-looking tests disagree**

Same workbook, sheet `Exercise1`. Seven students in rows 2 to 8, three grades each in B, C and D, the average already written in E with AVERAGE, and the status in F, written as `=IF(E2<=5.9,"Fail","Pass")`.

1. Add an eighth student. In A9 type `h`, and 6 in each of B9, C9 and D9. Extend the formulas of E and F down to row 9.
2. In G1 type `Status <=6`. Click G2 and build, through Formulas, Logical, IF, the formula `=IF(E2<=6,"Fail","Pass")`. Fill G2 down to G9.
3. Select A2:G9 with A2 as the active cell. Conditional Formatting, New Rule..., Use a formula to determine which cells to format. Press F2 in the formula box, then type `=$F2="Fail"`. Click Format..., set a red bold font on the Font tab, move to the Fill tab without closing, pick a fill, OK, OK.
4. Select E2:E9 and press Ctrl+1. On the Number tab pick Number with 2 decimal places.
5. Conditional Formatting, Manage Rules..., set Show formatting rules for to This Worksheet.

Report five things. The eight averages to two decimals. The rows where F and G disagree. One paragraph explaining why, with three whole-number grades, `<=5.9` and `<6` can never disagree on any row of this sheet while `<=5.9` and `<=6` do. How many rows the rule paints and over how many cells. And the Applies to range as the manager prints it.

---

## Week 07 · Compound conditions

### 07.1 · Recognise

**A staircase built from the wrong end**

Open `Excel12 (IFS).xlsx`, sheet `Ex1`. Thirty scores sit in A2:A31 and the band table sits in G2:H5: 900 to 999 Excellent, 750 to 899 Good, 500 to 749 Average, 100 to 499 Low.

Somebody wrote this into B2 and filled it down to B31.

```excel
=IF(A2>=500,"Average",IF(A2>=750,"Good",IF(A2>=900,"Excellent","Low")))
```

Answer four things. What the first five scores, 162, 847, 546, 325 and 902, come out as. How many of the thirty rows are wrong, and which of the four ratings never appear anywhere in the column. Whether Excel raises an error, a green triangle or anything else. And, with the cursor on B3 and Formulas, Formula Auditing, Evaluate Formula open, which part of the formula is underlined first and what the box shows after one click of Evaluate.

### 07.2 · Apply

**The same band twice, and the Name Box does the nesting**

Same sheet. Write the band correctly, twice, and never by typing the formula.

Column C, as a nested IF built through the dialog:

1. Click C2. Formulas tab, Function Library group, Logical, IF. Logical_test `A2>=900`. Value_if_true `Excellent`, with no quotation marks.
2. Click into Value_if_false and leave it empty. Look at the Name Box, at the left end of the formula bar: while the dialog is open it has stopped showing the cell reference and become a function list. Open it and click IF.
3. The second level opens. Logical_test `A2>=750`, Value_if_true `Good`. Leave Value_if_false empty and take IF from the Name Box again.
4. Third level. Logical_test `A2>=500`, Value_if_true `Average`, Value_if_false `Low`.
5. Click OK once, at the outer level. Do not click OK on the inner dialogs.
6. Fill C2 down to C31.

Column D, as an IFS: Formulas, Logical, IFS, with four pairs. `A2>=900` and `Excellent`, `A2>=750` and `Good`, `A2>=500` and `Average`, then the literal `TRUE` and `Low`.

Check the nest before you report anything: click into C5 and press Shift+F3. Function Arguments has to reopen on the outer IF with its three boxes filled and the next IF sitting inside Value_if_false.

Report four things. How many rows carry each of the four ratings. Whether C and D agree on all thirty rows. What the last pair of the IFS is for, and exactly what column D would show without it, on how many rows. And one line on what happens to column D if the file is opened on a build older than Office 2019.

### 07.3 · Integrate

**A criterion that is read as a pattern, and the same string where it is not**

Open `Excel 10 (Y,O, wildcard).xlsx`, sheet `WILDCARDS`. The list of place names sits in A2:A24 under the heading LIST in A1. The workbook already carries the defined name `Names`, and it points at `WILDCARDS!$A$1:$A$24`, heading included. The nine criteria are in D2:D10 and their counts belong in E2:E10, where the sheet already supplies `=COUNTIF(Names,D2)`.

Three tasks.

First, fill E2:E10 and report the nine counts. Then say whether any of the nine would change if `Names` were edited in the Name Manager to read `$A$2:$A$24`, and say what would change if A1 held the word `Zapata` instead of `LIST`. Name the criteria that move and by how much.

Second, look at the entry `México` in A11. Name every criterion of the nine that counts it, and explain in one line the one that catches people out.

Third, the tie back to week 5. Select A2:A24 with A2 as the active cell and write a formula rule whose formula is `=$A2="Tla*"`. Nothing is painted. Say why in one line. Then delete that rule from the Rules Manager with Delete Rule, write the rule that does work, `=COUNTIF($A2,"Tla*")>0`, and confirm in the manager that Applies to reads `=$A$2:$A$24` and that the rule is one rule and not three. Report the number of cells each of the two rules paints.

---

## Week 08 · Conditional aggregates

### 08.1 · Recognise

**Five formulas, and only one of them is both right and right for the right reason**

Open `Excel 11.xlsx`, sheet `Ex2`. The transactions sit in rows 4 to 33 with the month in A, the day in B, the deposit in C, the withdrawal in D and the branch in E. A row carries either a deposit or a withdrawal, never both, and the other cell is left empty.

Say what each of these returns, and for the ones that are wrong, name the fault.

```excel
=SUMIF(C4:C33,"Jan",A4:A33)
=SUMIF(A4:A33,"Jan",C4:C33)
=SUMIF(A4:A33,"Jan",C4:C500)
=SUMIFS(A4:A33,C4:C33,"Jan")
=AVERAGEIF(A4:A33,"Apr",C4:C33)
```

Then answer three more. Which of the five hand a number to a reader who has no way of telling it is wrong. What Excel does when somebody types `=COUNTIF(D4:D33,>1000)`, and what the accepted form of that criterion is together with the number it returns over this data. And one line on why the third formula gives the same answer as the second, which is not the same as being correct.

### 08.2 · Apply

**A branch and month grid from one formula, plus the two functions Exercise 11 leaves out**

Same sheet. Build the summary block below the data, starting at A36, and write each row of it once.

1. In B36, C36 and D36 type `Jan`, `Feb` and `Mar`. In A37 to A40 type `Bolívar`, `Cuauhtémoc`, `Díaz Mirón` and `Miguel Alemán`, spelled as column E spells them.
2. Click B37. Formulas tab, Function Library group, Math & Trig, SUMIFS. Sum_range `$C$4:$C$33`. Criteria_range1 `$E$4:$E$33` and Criteria1 `$A37`. Criteria_range2 `$A$4:$A$33` and Criteria2 `B$36`. Use F4 inside each box to cycle a reference into the form you want rather than typing the dollar signs. Read Formula result =, click OK, then fill B37 across and down to D40 in one operation.
3. In A42 type `Largest deposit` and in A43 `Smallest deposit`. In B42, from Formulas, More Functions, Statistical, MAXIFS, build `=MAXIFS($C$4:$C$33,$A$4:$A$33,B$36,$C$4:$C$33,">0")`. Build the matching MINIFS in B43. Fill both across to D.
4. In F36 type `Above`, in F37 type `5000`, and in F38 build `=COUNTIF($C$4:$C$33,">"&$F$37)` from More Functions, Statistical, COUNTIF. The operator goes in the Criteria box inside quotation marks with an ampersand after it, and the reference follows. No number is typed into the formula.

Report four things. The twelve figures of the grid, laid out as the grid lays them out. The two extra rows. What F38 returns, and what it returns after F37 is changed to 2000. And one line on the zero in the Cuauhtémoc row for January: say what it means and how you would tell it apart from the zero that a swapped pair of arguments produces.

### 08.3 · Integrate

**Five hundred and twenty spa records, answered once each**

Open `Excel 9 (IF FUNCTIONS).xlsx`, sheet `Exercise1`. The records run from row 2 to row 521: the date in A, the category in B, the client in C, the treatment in D, the esthetician in E, the price in F, the per cent discount in G, which is empty on some rows, and column H empty under the heading TOTAL CHARGED. The questions of the exercise are already printed down column J.

1. In H2 write `=F2*(1-G2)` and fill it to H521. Then select H2:H521, press Ctrl+1, and on the Number tab set Number with 2 decimal places.
2. Against the five names in J3:J7, write in K3 `=COUNTIF($E$2:$E$521,$J3)` and fill it to K7. Build the first one from Formulas, More Functions, Statistical, COUNTIF, and read Formula result = before OK.
3. Against the eight treatments in J9:J16, write in K9 `=SUMIF($D$2:$D$521,$J9,$H$2:$H$521)` and fill it to K16. SUMIF is not with the rest of its family: Formulas, Math & Trig.
4. Against the five names in J19:J23, write in K19 `=AVERAGEIF($E$2:$E$521,$J19,$G$2:$G$521)` and fill it to K23.
5. In K25 answer the question in J24 with the counting function from week 4 rather than with anything from this week, and say in one line why that one is the right tool here.
6. In K27 write `=AVERAGEIF($E$2:$E$521,"<>Rosa",$F$2:$F$521)`. In K29 total column H, and give that one cell 0 decimal places from Ctrl+1 rather than rounding the number itself.
7. Column A shows raw serial numbers, because it was never given a date format. Select A2:A521, press Ctrl+1, and on the Number tab pick Date with the short form. Then type the first and the last day of January 2022 into M1 and M2, in whatever order of day and month your copy of Excel accepts, and check that both sit against the right edge of their cells before you go on. Answer J30 in K31 with `=COUNTIFS($A$2:$A$521,">="&$M$1,$A$2:$A$521,"<="&$M$2)`.
8. In M4 count the treatments whose name contains the word Detoxifying, with one COUNTIF and a wildcard criterion from last week.
9. Select K3:K7 with K3 as the active cell and add a formula rule, `=$K3=MAX($K$3:$K$7)`, with a fill chosen from the Format... button. Confirm in the Rules Manager that Applies to reads `=$K$3:$K$7`.

Report seven things. The five counts of step 2 and which name the rule of step 9 paints. The eight totals of step 3 to two decimals. The five averages of step 4 to four decimals, plus one line saying which rows each of those averages is actually taken over, since column G is empty on some of them. The answers in K25, K27 and K29, and why step 5 needs no criterion at all. The answers in K31 and M4, with the check you ran on M1 and M2. And one line saying what K19 would have returned instead if the discount column had held zeros where it now holds blanks.

---

## Week 09 · Data that arrives from outside

### 09.1 · Recognise

**Four ways the same twenty six rows arrive**

`Students_data.csv` ships with Exercise 14. It holds a header row and twenty six students in seven columns: NAME, LAST NAME, COUNTRY OF ORIGIN, CITY OF ORIGIN, UNIVERSITY OF ORIGIN, AVERAGE, EXAM. The file was written on a Windows machine, so the ñ of España is the single byte F1. Four people put the same file on a sheet.

```text
Route A   Data > Get & Transform Data > From Text/CSV
          File Origin           Windows (ANSI)
          Delimiter             Comma
          Data Type Detection   Based on entire dataset
          Load arrow > Load To... > Existing worksheet: =$A$1

Route B   the same three lists, except
          File Origin           65001: Unicode (UTF-8)

Route C   the same three lists, except
          Data Type Detection   Do not detect data types

Route D   double-click Students_data.csv in File Explorer
```

Answer four things for each of the four routes. First, what cell A2 shows for the student whose name is Iñaki. Second, what `=SUM(F2:F27)` returns over the AVERAGE column, and why. Third, whether the Queries and Connections pane lists anything. Fourth, whether next month's version of the file can be brought in by pressing Refresh.

Then say which single route out of the four the exam is written around, and name the one thing on screen that proves which route a colleague took.

### 09.2 · Apply

**The import and the three level sort, on the sheet Exercise 14 already gives you**

Work in the `Import,Sorting` sheet of Excel 14. Do not open the .csv and do not paste from Notepad.

Import `Students_data.csv` through **Data**, **Get & Transform Data**, **From Text/CSV**. In the preview window set **File Origin** to `Windows (ANSI)`, **Delimiter** to `Comma` and **Data Type Detection** to `Based on entire dataset`. This file carries no product codes and no postal codes, so there is nothing here that needs to survive as text. Land it with the arrow beside **Load**, **Load To...**, **Existing worksheet:** `=$A$1`.

Before you touch anything else, open **Data**, **Queries & Connections** and write down what the pane says. Then convert the block to a range from **Table Design**, **Tools**, **Convert to Range**, and clear what the table style left behind with **Home**, **Editing**, **Clear**, **Clear Formats**.

Copy the sheet with **Move or Copy** and **Create a copy** ticked. On the copy, open **Data**, **Sort & Filter**, **Sort** with a single cell selected, tick **My data has headers**, and build three levels in one visit to the dialog:

| Level | Sort by | Sort On | Order |
|---|---|---|---|
| Sort by | LAST NAME | Cell Values | A to Z |
| Then by | COUNTRY OF ORIGIN | Cell Values | A to Z |
| Then by | AVERAGE | Cell Values | Largest to Smallest |

Hand in the workbook. Report the surname in row 2 and the surname in row 27 of the sorted copy, and say what the third level decided on this data.

### 09.3 · Integrate

**A filter hides, a formula does not, and week 8 settles the argument**

Open Excel 15, the 408 appliance sales. Row 1 holds the headers, the records run from row 2 to row 409, and the columns are A Sale Date, B Product, C Brand, D Category, E Branch, F Vendor, G Payment, H Unit cost, I Unit selling price, J Quantity. Build the four columns the exercise asks for, with relative references: K Total Cost as `=H2*J2`, L Total Sale as `=I2*J2`, M Total Profit as `=L2-K2`, N % Profit as `=M2/L2`.

Add a sheet called `Checks` and write four formulas on it, all pointing at `Hoja1` so that no filter can ever hide them. Three of them come from weeks 7 and 8:

- the number of sales in the first quarter of 2018, with `COUNTIFS` and two date criteria
- the number of sales whose Brand begins with the two letters PH, with `COUNTIF` and one wildcard
- the total sale value of those PH sales, with `SUMIFS` and the same wildcard

The fourth is a plain `=SUM(Hoja1!L2:L409)`.

Now go back to `Hoja1`, put the AutoFilter on, and use **Date Filters**, **Between** to leave only the first quarter of 2018. With the filter on, read three numbers: the record count on the status bar, what the plain `SUM` on the `Checks` sheet now reads, and what the status bar Sum reports when you select L2:L409 on the filtered sheet.

Explain in two lines why two of those three numbers disagree, and say which one answers the question "how much did we sell in the first quarter".

---

## Week 10 · Tables and charts

### 10.1 · Recognise

**One filter, three numbers, and only two of them move**

These eight rows are the first eight orders of Excel 16. They sit in a table named `Orders` whose header row is row 1 and whose data runs from row 2 to row 9.

| Row | Order Num | Order Date | Order Month | Quantity | Product | Origin | Destination | Status |
|---|---|---|---|---|---|---|---|---|
| 2 | 2021-1 | 09/04/2023 | 4 | 365 | Falda | PLANTA NORTE | NUEVO LEON | Sent |
| 3 | 2021-10 | 04/06/2023 | 6 | 319 | Chamarra | PLANTA CENTRO | GUANAJUATO | In progress |
| 4 | 2021-11 | 17/01/2023 | 1 | 397 | Falda | PLANTA PONIENTE | GUANAJUATO | In progress |
| 5 | 2021-12 | 25/01/2023 | 1 | 188 | Chamarra | PLANTA ORIENTE | NUEVO LEON | Sent |
| 6 | 2021-13 | 03/05/2023 | 5 | 118 | Traje de Baño | PLANTA PONIENTE | SINALOA | Payment pending |
| 7 | 2021-14 | 11/02/2023 | 2 | 478 | Blusa | PLANTA SUR | GUANAJUATO | In progress |
| 8 | 2021-15 | 02/04/2023 | 4 | 398 | Blusa | PLANTA CENTRO | VERACRUZ | Delivered |
| 9 | 2021-16 | 11/03/2023 | 3 | 192 | Chamarra | PLANTA NORTE | NUEVO LEON | Sent |

The **Total Row** check box is ticked. The total cell under Status was set to **Count** and the total cell under Quantity was set to **Average**, both from the drop-down that appears on the right edge of the cell. Somebody else, before any of that, typed `=SUM(E2:E9)` into E12, two rows under the table.

State the three formulas Excel wrote or the user typed, exactly as the formula bar shows them, and give the value of each with no filter on. Then filter the Status column to `Sent` and give the three values again.

Say which of the three did not move and why, and say what the number would have been in the Quantity total if the drop-down had been left on **Sum** instead of Average.

### 10.2 · Apply

**The three things Exercise 17 never asks for**

Exercise 17 builds twenty charts on five sheets and asks for no chart sheet, no row and column switch, and no alt text. Those three are exactly what the syllabus names, so build them here on the `Classification` sheet of Excel 17, which holds five genres in A2:A6 and the months January, February and March in B1:D1.

Select A1:D6. Open the **Insert Chart** dialog through **Insert**, **Charts**, and the dialog box launcher in the bottom right corner of the group. Go to **All Charts**, click **Column** in the left list, click the **Clustered Column** subtype along the top, read the preview and click **OK**. Do not use the gallery buttons and do not press Alt+F1.

Before you change anything, count the series in the legend and the labels on the category axis and write both numbers down. Then go to **Chart Design**, **Data**, **Select Data**, click the **Switch Row/Column** button between the two lists, and click **OK**. Count both again.

Move the chart with **Chart Design**, **Location**, **Move Chart**, **New sheet:**, and type `Genre by month`. Do not accept `Chart1` and do not reach a chart sheet with F11.

Finally right-click the chart border and click **Alt Text...**, worded **Edit Alt Text...** on some builds. Write one or two sentences describing what the chart shows and what the reader is meant to take from it. Do not write the word chart and do not put the description in a cell under the object.

Hand in the workbook. Report the two pairs of counts, the tallest column in the plot with its value, and the sentence you wrote in the Alt Text pane.

### 10.3 · Integrate

**Week 8 inside a week 10 table**

Use the same `Orders` table from 10.1, still eight rows, still named `Orders`.

Add one calculated column. Click the first empty cell to the right of Status, type the header `Band`, and in the first data cell write a single formula with the IFS function of week 8 that returns `High` for a quantity of 400 or more, `Medium` for 200 or more, and `Low` for anything else. Write it once and let the table fill the column. Do not drag the fill handle.

Below the table, write four formulas. Every one of them has to hold the table name and a column name, and none of them may hold a cell address:

- the sum of the Quantity column
- the number of orders whose Status is `Sent`, with `COUNTIFS`
- the sum of Quantity for the product `Chamarra`, with `SUMIFS`
- the average Quantity for the destination `GUANAJUATO`, with `AVERAGEIFS`

Now paste one more order at the bottom of the table: `2021-17`, 26/02/2023, month 2, quantity 245, Traje de Baño, PLANTA PONIENTE, NUEVO LEON, Sent.

Give the four values before the paste and the four values after it, the band the ninth row received, and how many cells you had to edit to make the four formulas cover nine rows instead of eight. Then write one line saying what the same four would have returned had they been written over plain cell ranges, `E2:E9` and its neighbours, instead of over table columns.

---

## Week 11 · Chart choice and distribution

### 11.1 · Recognise

**Three colleagues protect the same sheet**

Excel 18 holds one sheet, `Personnel`, with the headers in row 1 and the employee records from row 2 to row 115. Column E is Area, column G is Salary, and column J is empty until somebody writes the age formula into it. Assume J2 already carries `=INT((DATE(2025,12,31)-I2)/365.25)` filled to J115.

```text
Colleague 1   Review > Protect > Protect Sheet
              Password typed, OK, confirmed
              Nothing else was done first

Colleague 2   Ctrl+A, Ctrl+1, Protection, clear Locked, OK
              Select G2:G115, Ctrl+1, Protection, tick Locked, OK
              Select J2:J115, Ctrl+1, Protection, tick Locked, OK
              Review > Protect > Protect Sheet, password, OK, confirmed

Colleague 3   Closed Excel
              Right-clicked the file in File Explorer, Properties
              Ticked Read-only on the General tab, OK
              Reopened the file
```

For each of the three, answer four things. Can a reader type a new value into E5. Can a reader type a new value into G5. What does the formula bar show when J5 is selected. And what does the **Protect** group of the Review tab read once the work is done.

Then say which of the three did what the task "leave the sheet editable except for the salaries and the age formula" actually asked for, and name the one check box the closest of them still missed.

### 11.2 · Apply

**Two magnitudes that will not share an axis**

Open the `Sales by State` sheet of Excel 17. It holds twelve states in A2:A13, the average temperature in column B, ice cream units in column C and book units in column D. The temperatures run from 11.9 to 25.1. The ice cream figures run from 185 to 614.

Select A1:C13, headers included. Go to **Insert**, **Charts**, **Insert Combo Chart**, and click **Create Custom Combo Chart...** at the bottom of that gallery. Do not go through Recommended Charts, and do not build a column chart first and repair it afterwards.

The **Insert Chart** dialog opens on **All Charts** with **Combo** already selected. Under the heading that asks you to choose the chart type and axis for your data series, leave the Ice Cream row on **Clustered Column**, set the Temperature row to **Line with Markers**, and tick **Secondary Axis** in that same row. Both edits happen before the dialog closes. Click **OK**.

Label the new axis: **Chart Design**, **Chart Layouts**, **Add Chart Element**, **Axis Titles**, **Secondary Vertical**, and type `Average temperature (C)`. Give the primary vertical axis the title `Ice cream units` the same way.

Hand in the workbook. Report how many series and how many categories the plot holds, which state sits at the top of both series and with what two values, and what the temperature series would look like if it shared the left axis with the ice cream units. Then open **Change Chart Type** and say what the dialog shows when it reopens.

### 11.3 · Integrate

**Excel 18, from a working file to a file you can send**

This one uses the dates of week 4, the counting functions of week 8, the Document Inspector habit of week 9 and everything from this week. Work on Excel 18.

Write `Age` in J1 and in J2 write `=INT((DATE(2025,12,31)-I2)/365.25)`. Fill it to J115. A fixed cut-off is used on purpose so that the answer can be marked; the live version with `TODAY()` moves every night.

In two spare cells, write with `COUNTIF` the number of employees aged sixty or over and the number aged sixty five or over.

Open **Formulas**, **Name Manager**. The workbook carries defined names left behind by an old advanced filter exercise. Report how many there are, which of them resolve to `#REF!`, and delete only those.

Leave one threaded comment on J1 through **Review**, **Comments**, **New Comment**, saying which cut-off date the age was calculated against, and post it. Open **Show Comments** and confirm it is listed. Do this before the protection goes on, because New Comment is one of the commands a protected sheet greys out.

Run **Review**, **Accessibility**, **Check Accessibility** and act on whatever it reports.

Only now protect the file, in this order and no other. Unlock the whole sheet from Ctrl+A, Ctrl+1, **Protection**, clear **Locked**. Select J2:J115 and, in one visit to Ctrl+1, tick **Locked** and **Hidden**. Then go to **Review**, **Protect**, **Allow Edit Ranges**, click **New...**, and create a range called `Payroll` over G2:G115 with a range password. Reach the next dialog through the **Protect Sheet...** button at the bottom of the Allow Edit Ranges dialog, not through the Review tab, and in the allow list leave **Select locked cells** and **Select unlocked cells** ticked and clear **Format cells** and **Sort**. Close with **Review**, **Protect**, **Protect Workbook**, **Structure**, and a password.

Hand in the workbook with the passwords written in the submission comment. Report the age in J2, the two counts, the dead names you deleted, what the formula bar shows on J5 afterwards, and what happens when a colleague clicks G5 and types.

---

## Week 12 · Midterm, mock and VLOOKUP

### 12.1 · Recognise

**Four lookups, and only one of them is written the way the task asked**

Exercise 19 has two sheets. On `Table`, the vendor reference sits in A14:C18: the header row VENDOR TYPE, BASE SALARY, SALES GOAL, then `A` 50,000 20,000,000, `B` 40,000 15,000,000, `C` 30,000 10,000,000, `D` 20,000 5,000,000. Rows 19 and below are empty. On `Report`, the headers are in row 2 and the ten salespeople occupy rows 3 to 12. Column D holds the vendor type, in this order down the ten rows: A, B, A, C, D, C, D, B, D, D.

Four people filled the BASE SALARY (MONTHLY) column in F3 and filled it down to F12.

```text
(a)  =VLOOKUP(D3,Table!A15:C18,2,FALSE)
(b)  =VLOOKUP($D3,Table!$A$15:$C$18,4,FALSE)
(c)  =VLOOKUP($D3,Table!$A$15:$C$18,2)
(d)  =VLOOKUP($D3,Table!$A$15:$C$18,2,FALSE)
     with A15 typed as "A " instead of "A"
```

For each of the four, give what F3 shows and what F12 shows. For (a), also give how many of the ten rows come back with a number rather than an error, and name them. For (c), say whether the answer is right and whether the formula is safe, which are two different questions.

Finish with one line on why version (a) is the hardest of the four to catch when you are reading somebody else's workbook.

### 12.2 · Apply

**The two lookups of the payroll model, built in the dialog**

Work on the `Report` sheet of Exercise 19. F3 will hold the monthly base salary and H3 the sales goal. Both come from A14:C18 on the `Table` sheet, both are exact matches, and both will be filled down to row 12.

Build F3 through the dialog. Select F3, go to **Formulas**, **Function Library**, **Lookup & Reference**, and click **VLOOKUP**. Fill the four boxes by their names. **Lookup_value** is the cell holding the vendor type, clicked, left relative. **Table_array** is the whole reference table with its first column, selected and then locked with **F4**. **Col_index_num** is counted from the first column of Table_array, not from column A of the worksheet. **Range_lookup** is typed out as `FALSE`, not left empty and not typed as `0`. Click **OK**, then fill down to F12.

Build H3 the same way, changing one box only.

Then add three columns of ordinary arithmetic with relative references: G, the annual base salary, twelve times the monthly figure; J, the difference in pesos between the amount sold in column E and the sales goal; and K, that difference as a percentage of the goal.

Hand in the workbook and report six things: the formula in F3 exactly as the formula bar shows it, the formula in F12, the base salary and sales goal for Javier López in row 3, the same two for Andrea Legarreta in row 11, the total of the ten monthly base salaries, and how many of the ten rows carry a negative difference. Then change the base salary for type B on the `Table` sheet and say how many rows of the report moved.

### 12.3 · Integrate

**Week 5, week 7 and week 8 on top of the lookup**

Keep the workbook from 12.2. The lookups are in place, columns G, J and K are filled, and the reference date for seniority is the one already sitting in N1 of the Report sheet, 3 June 2020.

Column N is seniority in years. Write it with date arithmetic against `$N$1`, locked, and fill it down.

Column R decides the award. An employee wins it when the difference in column K is above five per cent **and** the seniority in column N is above ten years. Write it as one IF with AND inside, returning `Yes` or `No`.

Column S decides the thank you letter. An employee gets one when the amount sold in column E is above ten million **or** the seniority is above fifteen years. Write it as one IF with OR inside, returning the same two words.

Apply conditional formatting to K3:K12 from **Home**, **Styles**, **Conditional Formatting**, **Highlight Cells Rules**: red fill for less than 0, green fill for greater than 50 %. Two separate rules, both visible in **Manage Rules**.

Last, in three spare cells, count with `COUNTIF` how many of the ten win the award, how many get a letter, and how many rows the red rule caught.

Report the three counts and the names whose award cell reads `Yes`. One salesperson's difference percentage lands exactly on the five per cent boundary. Name him, say what his award cell reads, and say whether changing the condition from above five per cent to five per cent or more would change that cell. Justify the answer by testing both legs of the AND, not one.

---

## Week 13 · Lookup and consolidation

### 13.1 · Recognise

**Four lookups over one fee table**

Sheet `Fees` holds the tuition by programme code, sorted ascending on the code.

| Row | A · Code | B · Fee |
|---|---|---|
| 2 | ADM | 39,750 |
| 3 | CON | 41,200 |
| 4 | FIN | 43,100 |
| 5 | MKT | 38,500 |
| 6 | NIN | 44,900 |

Sheet `Students` holds five enrolments. Column B, from row 2 down, reads `MKT`, `FIN`, `GAS`, `CON`, `ADM`. The registrar closed the GAS programme last year and nobody took it out of the intake file. Column E, over the same five rows, holds the final scores 79, 91, 58, 70 and 100. The score band table sits on the same sheet in F3:G7, sorted ascending.

| Row | F · Lower score | G · Grade |
|---|---|---|
| 3 | 0 | F |
| 4 | 60 | D |
| 5 | 70 | C |
| 6 | 80 | B |
| 7 | 90 | A |

Answer four blocks. Give values, not descriptions.

(a) `=VLOOKUP(B2,Fees!$A$2:$B$6,2,FALSE)` is written in C2 and filled to C6. Give the five results.

(b) `=VLOOKUP(B4,Fees!$A$2:$B$6,2)` is written in D4, over the GAS enrolment. Give the result and say which row of `Fees` it came from and why.

(c) `=VLOOKUP(E2,$F$3:$G$7,2,TRUE)` is written in H2 and filled to H6. Give the five grades.

(d) `=VLOOKUP(B2,Fees!A2:B6,2,FALSE)` is written in I2 with nobody pressing F4, then filled to I6. Give the five results, and name the rows that come out right by luck rather than by design.

### 13.2 · Apply

**A cost that VLOOKUP cannot reach**

Two sheets of a hardware catalogue. On `Inventory 2` the cost was captured first and the item code third, headers in row 3. That is the whole difficulty: the column the answer lives in sits behind the column the key lives in.

| Row | B · Cost | C · Description | D · Item | E · Unit |
|---|---|---|---|---|
| 4 | 18.50 | Galvanised elbow 1/2 in | FE-204 | piece |
| 5 | 12.25 | PVC tee 3/4 in | PV-118 | piece |
| 6 | 27.90 | Copper coupling 1/2 in | CU-330 | piece |
| 7 | 145.00 | Hex bolt 3/8 x 2 | TO-051 | box of 50 |
| 8 | 63.40 | Flat washer 3/8 | RO-012 | box of 100 |
| 9 | 9.80 | PVC elbow 3/4 in | PV-207 | piece |
| 10 | 41.60 | Copper tee 3/4 in | CU-415 | piece |
| 11 | 22.75 | Galvanised nipple 1 in | FE-388 | piece |

On `Inventory 3` the same catalogue is laid across instead of down. Row 3 holds the item codes in B3:G3, reading `FE-204`, `PV-118`, `CU-330`, `TO-051`, `RO-012`, `PV-207`. Row 4 holds the unit, row 5 the supplier and row 6 the cost, in the same order: 18.50, 12.25, 27.90, 145.00, 63.40, 9.80. Cell J3 holds the code being looked up, `RO-012`.

Three tasks, and each names the route because the route is what is marked.

First. Cells G4, G5 and G6 of `Inventory 2` hold the codes `PV-207`, `CU-330` and `TO-051`. In H4 build the lookup with INDEX from the **Formulas** tab, **Function Library** group, **Lookup & Reference**. Take `array,row_num,column_num` in the **Select Arguments** dialog. Put `$B$4:$B$11` in **Array**, then, with the cursor in **Row_num**, pick MATCH from the Name Box at the left of the formula bar and fill it with `$G4`, `$D$4:$D$11` and `0`. Click the word INDEX in the formula bar to come back out, then OK once, at the INDEX level. Fill H4 down to H6 and total the three in H8.

Second. In J6 of `Inventory 3` fetch the cost of `RO-012` with HLOOKUP through **Function Arguments**, with the code in J3, the table array locked to `$B$3:$G$6` with F4, `Row_index_num` counted from row 1 of that block, and `Range_lookup` written out as FALSE.

Third. Write one line for each sheet saying why VLOOKUP cannot answer it, naming the argument that fails rather than saying the function did not work.

The three tables are exercise 21, `Excer 21 (HLookup).xlsx`, over 2,585 hardware items. Get the two formulas right on this extract, then run the same two down the full file and hand in both.

### 13.3 · Integrate

**Three branches that do not list their categories in the same order**

Three sheets in one workbook saved as `Consolidation.xlsx`, each sheet holding one branch. Headers in row 1, `Category` in A and `Amount` in B.

`Norte`

| Row | A · Category | B · Amount |
|---|---|---|
| 2 | Tools | 128,400 |
| 3 | Plumbing | 96,750 |
| 4 | Electrical | 143,200 |

`Sur`

| Row | A · Category | B · Amount |
|---|---|---|
| 2 | Electrical | 87,300 |
| 3 | Tools | 210,500 |
| 4 | Plumbing | 64,100 |

`Centro`

| Row | A · Category | B · Amount |
|---|---|---|
| 2 | Plumbing | 55,900 |
| 3 | Electrical | 78,250 |
| 4 | Tools | 132,000 |
| 5 | Paint | 41,800 |

The tabs sit in the order `Norte`, `Sur`, `Centro`. Five tasks.

First. On a new sheet named `Summary`, click A1 and nothing else, then **Data** tab, **Data Tools** group, **Consolidate**. Function Sum. Add the three source ranges one at a time with **Add**, headers included. Tick **Top row** and **Left column** under **Use labels in**, leave **Create links to source data** clear, and leave the dialog with **OK** rather than Close. Report what lands in B1, what lands in A2 downwards in the order Excel wrote it, and the figure beside each label. Then put `=SUM(B2:B5)` in B7 for the grand total.

Second. In D2 write `=SUM(Norte:Centro!B2)` and fill to D5. Report the four numbers and say, in one sentence, what the number in D2 is actually the sum of.

Third. In A10 type `Electrical`. In B10 return its consolidated total with VLOOKUP built from the dialog, the table array locked with F4 and `Range_lookup` typed as FALSE. This is the week 12 function reading the week 13 summary.

Fourth. Open a second workbook named `Board.xlsx` and, without typing a path, link its cell B2 to B7 of `Summary`: type `=`, then **View** tab, **Window** group, **Switch Windows**, click the cell, press Enter. Write down what the formula bar shows while the source is open, then close the source and write down what it shows afterwards. Then open **Data** tab, **Queries & Connections** group, **Edit Links** and report the **Status** the dialog gives after **Check Status**.

Fifth. In one line, say what ticking **Create links to source data** would have added to the `Summary` sheet, and how you would see it.

Hand in the two files. Reopening **Consolidate** on A1 has to bring the three references back into **All references:**, and that list is the proof the tool was used rather than the arithmetic.

---

## Week 14 · Subtotals and PivotTables

### 14.1 · Recognise

**What the Subtotal command writes, and what it will not tell you**

Sheet `Data`, headers in row 1, twelve records in rows 2 to 13, already sorted by town.

| Row | A · Town | B · Age range | C · Gender | D · People |
|---|---|---|---|---|
| 2 | Azcapotzalco | 0-14 | F | 41,200 |
| 3 | Azcapotzalco | 15-64 | F | 138,400 |
| 4 | Azcapotzalco | 65+ | F | 26,300 |
| 5 | Azcapotzalco | 0-14 | M | 39,800 |
| 6 | Coyoacán | 15-64 | F | 201,500 |
| 7 | Coyoacán | 65+ | F | 44,700 |
| 8 | Coyoacán | 0-14 | M | 52,100 |
| 9 | Iztapalapa | 0-14 | F | 88,300 |
| 10 | Iztapalapa | 15-64 | F | 312,600 |
| 11 | Iztapalapa | 65+ | M | 61,900 |
| 12 | Iztapalapa | 0-14 | M | 90,400 |
| 13 | Iztapalapa | 15-64 | M | 298,700 |

Answer four blocks.

(a) One cell inside the list is clicked and the **Subtotal** dialog is set to **At each change in** Town, **Use function** Sum, **Add subtotal to** People, with **Replace current subtotals** and **Summary below data** left as they arrive. Say how many rows the command inserts, give the sheet row each one lands on, and give the formula and the value each of them holds.

(b) Give the formula and the value of the grand total row, and say in one sentence why it does not count the three subtotals twice. Then say what `=SUM(D2:D16)` would have returned in that same cell, with the number.

(c) The same command is run instead with **At each change in** set to Gender, on the list exactly as printed above, with nobody sorting first. Say how many subtotal rows appear and why every one of them is arithmetically correct.

(d) Back on the version from (a), rows 13 and 14 are hidden by right-clicking their row headings and clicking **Hide**. Give the value the Iztapalapa subtotal shows, then give the value it would show if the same cell held `SUBTOTAL(109,...)` instead, and name the one place in Excel that writes 109 without being asked.

### 14.2 · Apply

**One source, two reports, and the four boxes read back**

Sheet `Tickets`, headers in row 1, twelve tickets in rows 2 to 13. Column G is a real column of the sheet holding `=E2*F2` filled down.

| Row | A · Date | B · Waiter | C · Category | D · Product | E · Units | F · UnitPrice | G · Charged |
|---|---|---|---|---|---|---|---|
| 2 | 04/03/2026 | Lucía | Drinks | BEB-01 | 1 | 85.00 | 85.00 |
| 3 | 04/03/2026 | Lucía | Mains | PLA-11 | 5 | 49.00 | 245.00 |
| 4 | 05/03/2026 | Marco | Drinks | BEB-04 | 2 | 60.00 | 120.00 |
| 5 | 05/03/2026 | Marco | Desserts | POS-02 | 1 | 95.00 | 95.00 |
| 6 | 02/04/2026 | Lucía | Mains | PLA-07 | 2 | 155.00 | 310.00 |
| 7 | 02/04/2026 | Nadia | Drinks | BEB-02 | 1 | 65.00 | 65.00 |
| 8 | 11/04/2026 | Nadia | Mains | PLA-03 | 4 | 70.00 | 280.00 |
| 9 | 11/04/2026 | Marco | Desserts | POS-05 | 2 | 55.00 | 110.00 |
| 10 | 06/05/2026 | Lucía | Drinks | BEB-06 | 3 | 50.00 | 150.00 |
| 11 | 06/05/2026 | Nadia | Mains | PLA-15 | 5 | 85.00 | 425.00 |
| 12 | 20/05/2026 | Marco | Mains | PLA-09 | 3 | 65.00 | 195.00 |
| 13 | 20/05/2026 | Nadia | Desserts | POS-08 | 2 | 70.00 | 140.00 |

Build two reports. Every field goes into its area by dragging, never by ticking a check box, and every format is set on the field.

Report one, named `ByWaiter`. Click one cell inside the list, then **Insert** tab, **Tables** group, **PivotTable**, and check that **Table/Range** reads `Tickets!$A$1:$G$13` before choosing **New Worksheet**. Drag Category into **Rows**, Waiter into **Columns**, Charged into **Values**. Then click a value cell, go to **PivotTable Analyze** tab, **Active Field** group, **Field Settings**, leave **Summarize Values By** on Sum, set **Custom Name** to `Charged`, click **Number Format** and pick Currency with two decimals, and click OK once. Name the report in the **PivotTable Name** box.

Report two, named `ShareOfTotal`. Same source, same three fields in the same three areas, on its own sheet. This time, in the same one pass through **Field Settings**, go to the **Show Values As** tab and pick **% of Grand Total**, set **Custom Name** to `Share`, and set the number format to Percentage with two decimals.

Hand in the workbook and, in writing, the four boxes of the PivotTable Fields pane for report one, listed as Filters, Columns, Rows, Values. Say as well what the Desserts row shows in the Lucía column and why.

### 14.3 · Integrate

**The cost the tickets never carried**

Same `Tickets` sheet. Add a `Menu` sheet holding the unit cost of each product, headers in row 1 and twelve products in rows 2 to 13.

| Product | UnitCost |
|---|---|
| BEB-01 | 31.00 |
| BEB-02 | 24.00 |
| BEB-04 | 24.00 |
| BEB-06 | 18.00 |
| PLA-03 | 32.00 |
| PLA-07 | 72.00 |
| PLA-09 | 30.00 |
| PLA-11 | 20.00 |
| PLA-15 | 40.00 |
| POS-02 | 38.00 |
| POS-05 | 22.00 |
| POS-08 | 28.00 |

Five tasks, crossing weeks 10, 13 and 14.

First. In H1 write the header `LineCost`, and in H2 write `=E2*VLOOKUP(D2,Menu!$A$2:$B$13,2,FALSE)`, built from the dialog with the table array locked by F4. Fill to H13.

Second. Turn A1:H13 into an Excel table named `Tickets2026`, so the report grows when a ticket is added.

Third. Build one PivotTable over that table. Drag Date into **Rows**, then click a date item and use **PivotTable Analyze** tab, **Group** group, **Group Field** to group by Months and Quarters together. Drag Charged and LineCost into **Values**. Then add a calculated field through **PivotTable Analyze**, **Calculations**, **Fields, Items, & Sets**, **Calculated Field**, named `Margin`, with the formula built by clicking the fields and clicking **Insert Field** rather than typing.

Fourth. On the **Design** tab set **Report Layout** to **Show in Tabular Form** and then **Repeat All Item Labels**, and set **Grand Totals** to **On for Rows and Columns**. Set the number format of all three value fields through **Field Settings**, not with Ctrl+1 over the cells.

Fifth. Add a second calculated field named `LineCheck` with the formula `= Units * UnitPrice`, drop it beside Charged, and read the May row and the grand total row. The two columns disagree. Give both pairs of numbers, explain in two sentences why the calculated field is not adding the line amounts, and say which of the two belongs in a report that goes to the owner.

Then refresh with Alt+F5 and confirm the formats are still there. A format that vanishes was applied to cells and takes its mark with it.

---

## Week 15 · Advanced filters

### 15.1 · Recognise

**Reading a criteria range before running it**

Sheet `Staff`, headers in row 3, twelve records in rows 4 to 15.

| Row | B · Surname | C · Given name | D · Branch | E · Department | F · Start date | G · Salary |
|---|---|---|---|---|---|---|
| 4 | Escobar | Ana | Centro | Accounting | 12/03/1991 | 5,200 |
| 5 | Estrada | Beto | Azcapotzalco | Logistics | 01/07/1994 | 4,100 |
| 6 | Reyes | Carla | Centro | Logistics | 23/11/1989 | 6,300 |
| 7 | Lemus | Darío | Norte | Accounting | 15/01/1992 | 4,800 |
| 8 | Beltrán | Elena | Azcapotzalco | Administration | 30/05/1996 | 3,900 |
| 9 | Espinosa | Fabián | Centro | Accounting | 08/09/1993 | 5,600 |
| 10 | Nieto | Gabriela | Norte | Administration | 19/02/1990 | 7,100 |
| 11 | Peña | Hugo | Azcapotzalco | Logistics | 04/12/1995 | 4,400 |
| 12 | Vega | Irene | Centro | Administration | 27/08/1991 | 5,900 |
| 13 | Zamora | Julio | Norte | Accounting | 14/06/1997 | 3,600 |
| 14 | Herrera | Karla | Azcapotzalco | Accounting | 02/04/1994 | 6,800 |
| 15 | Ochoa | Luis | Centro | Logistics | 11/10/1988 | 8,200 |

For each of the four criteria ranges below, give the surnames that come out and the count. The headers shown are copies of the list headers, and the cells under them are exactly as written.

(a)

| Branch | Department |
|---|---|
| Centro | Accounting |

(b)

| Branch | Department |
|---|---|
| Centro | Accounting |
| Azcapotzalco | Logistics |

(c)

| Surname |
|---|
| ?E* |

(d)

| Salary | Salary |
|---|---|
| >4000 | <6000 |

Then two more answers. Say what the filter returns if a completely empty row is left between the header row and the condition in (a), and say why. And say what happens to (b) if the two conditions are written on one row instead of two.

### 15.2 · Apply

**Three extractions, none of them a menu**

Same `Staff` sheet. Every result is produced by **Data** tab, **Sort & Filter** group, **Advanced**, with **Copy to another location** selected. No AutoFilter anywhere in the workbook. Leave every criteria range visible on the sheet.

First. Write a criteria range in B18:C20 and extract, to B24, the people who are either in Centro and Accounting or in Azcapotzalco and Logistics. All six fields come out. Report the extracted rows and the count.

Second. Write a criteria range in E18:E19 whose condition is a formula, and extract to B32 the people earning more than the average salary of the whole list. Three rules are graded here and all three are separate marks: the header cell over the formula must not carry a field name, the reference to the first data row must be relative while the range it is compared against is locked, and the formula must return TRUE or FALSE. Report the average the list actually has, the extracted rows, and the count. Do not be alarmed that the criteria cell itself reads TRUE or FALSE for one row only.

Third. Copy the `Department` header alone to B40, then run **Advanced** with the criteria range left empty, **Copy to** set to B40, and **Unique records only** ticked. Report what lands under it, in the order Excel writes it, and say in one line why this is the non-destructive answer to "list the departments" and Remove Duplicates is not.

The fifteen filters of exercise 24, `Excel24_instructions(Advanced Filters).xlsx`, run the same three shapes over 27 employees with the extractions starting at B32. Finish that file as well, and leave one clear row between blocks so the next filter does not read an extraction as data.

### 15.3 · Integrate

**Two routes to the same two tickets, and the objects that prove it**

Go back to the `Tickets` sheet and the PivotTable of week 14. Four tasks.

First. Build a PivotChart from the report: click inside the PivotTable, **PivotTable Analyze** tab, **Tools** group, **PivotChart**, clustered column. Put the grouped date in **Axis (Categories)** and Waiter in **Legend (Series)**, with Charged in **Values**. Then clear only the legend field buttons from **PivotChart Analyze**, **Show/Hide**, **Field Buttons**, leaving the axis buttons where they are. Do not use **Hide All**.

Second. Insert a slicer on Category and a timeline on Date in one pass each, from **PivotTable Analyze**, **Filter** group. Set the slicer to two columns of buttons and type its **Height** and **Width** in the **Slicer** tab rather than dragging it. Set the timeline level to Months.

Third. With no filter applied, find the cell of the report holding May for Nadia and double-click it. Report the name Excel gave the new sheet, how many rows it holds, and the sum of its Charged column. That sum has to equal the cell you clicked, and if it does not, say which of the two is wrong.

Fourth. Reach the same rows the other way. On the `Tickets` sheet write a criteria range that says Waiter is Nadia and the date falls in May 2026, and run an advanced filter with **Copy to another location** into an empty block. Confirm the extraction and the drill-through sheet hold the same records. Then say, in two lines, which of the two routes survives a change in the source data and which one does not.

Hand in the workbook with the slicer, the timeline, the PivotChart and the drill-through sheet all still in it. The objects are the evidence.

---

## Week 16 · What-if analysis

### 16.1 · Recognise

**A model read forwards, then backwards**

Sheet `Churrumpin`. The inputs sit in their own cells and every figure below them is computed.

| Cell | Label | Content |
|---|---|---|
| B2 | Units | 50,000 |
| B3 | Price | 100.00 |
| B4 | Unit cost | 60.00 |
| B9 | Revenue | `=B2*B3` |
| B10 | Variable cost | `=B2*B4` |
| B11 | Fixed cost | 1,500,000 |
| B12 | Operating profit | `=B9-B10-B11` |
| B13 | Tax rate | 0.15 |
| B14 | Net income | `=B12*(1-B13)` |

Answer four blocks.

(a) Give the value of B9, B10, B12 and B14 as the sheet stands.

(b) **Goal Seek** is opened with **Set cell** B14, **To value** 0 and **By changing cell** B2. Give the number that lands in B2, and say what the **Goal Seek Status** dialog reports. Then say what happens if **By changing cell** is pointed at B9 instead, and why, in your own words.

(c) A one-variable data table is laid out clear of the model: the unit counts 30,000 to 70,000 in steps of 5,000 down H11:H19, the reference `=B14` in I10, the whole rectangle H10:I19 selected, and **Column input cell** set to B2. Give the nine results. Then say what the body cells hold when you click one of them, and what Excel says if you try to delete a single cell of that block.

(d) Somebody types `425000` into the reference cell instead of `=B14` and runs the same data table. Say exactly what the nine results become and why nothing on screen looks broken.

### 16.2 · Apply

**A payment, a term, and the same answer twice**

Build sheet `Credit` from scratch. Inputs first, in labelled cells, because every formula has to read them.

| Cell | Label | Value |
|---|---|---|
| B2 | Annual rate | 12.5% |
| B3 | Term in years | 4 |
| B4 | Amount borrowed | 285,000 |

Five tasks.

First. In B5 build PMT from **Formulas** tab, **Function Library** group, **Financial**. Put `B2/12` in **Rate**, `B3*12` in **Nper** and `B4` in **Pv**. Read **Formula result =** at the bottom of the dialog before clicking OK. Then format B5 as Currency with two decimals through Ctrl+1. Report the payment and say what its sign means.

Second. In B6 build NPER from the same list, with `B2/12` in **Rate**, `B5` in **Pmt** and `B4` in **Pv**. Report the number of periods. Then, on a scratch cell, write the same function with `-B5` in **Pmt** instead, report what comes back, and say in one line what that number is telling you about the signs.

Third. In B7 build the decision with IF from **Formulas**, **Logical**, nesting AND into **Logical_test** through the Name Box: the term in months must be 36 or fewer and the payment must be no worse than 5,000 a month. Report the word the cell shows.

Fourth. Run **Goal Seek** with **Set cell** B5, **To value** -5000 and **By changing cell** B3. Report the term Goal Seek lands on, in years and then in months. Then check it a second way: in a free cell build NPER with `B2/12` in Rate, `-5000` in Pmt and `B4` in Pv, and confirm the two agree. Undo the Goal Seek before going on, so B3 is 4 again.

Fifth. Build a two-variable data table. Put the annual rates 10%, 11%, 12%, 13% and 14% down H10:H14, the amounts 250,000, 285,000 and 320,000 across I9:K9, and `=B5` in the corner cell H9. Select the whole rectangle H9:K14 before opening **Data**, **Forecast**, **What-If Analysis**, **Data Table**, then set **Row input cell** to B4 and **Column input cell** to B2. Report the fifteen payments. Before you build it, set **Formulas** tab, **Calculation** group, **Calculation Options** to **Automatic Except for Data Tables**, and say in one line why.

### 16.3 · Integrate

**Three futures for the same product, stored rather than copied**

Back to the `Churrumpin` sheet, with one change. The unit cost is no longer typed. Add a `Suppliers` sheet with the headers in row 1 and three rows.

| Supplier | Unit cost |
|---|---|
| Bajío | 58.00 |
| Central | 63.50 |
| Lira | 60.00 |

Put the supplier name in B5 of `Churrumpin` and make B4 read it: `=VLOOKUP(B5,Suppliers!$A$2:$B$4,2,FALSE)`, built from the dialog, table array locked, `Range_lookup` typed out. With `Lira` in B5 the model has to return the same net income as last week.

Then store three futures with **Data**, **Forecast**, **What-If Analysis**, **Scenario Manager**. Changing cells B2, B3 and B5, chosen with Ctrl+click. Three scenarios, named in words a reader understands rather than Scenario 1.

| Name | Units | Price | Supplier |
|---|---|---|---|
| Cautious | 35,000 | 95.00 | Central |
| Planned | 50,000 | 100.00 | Lira |
| Ambitious | 62,000 | 108.00 | Bajío |

Use **Add** to go straight from one scenario into the next rather than closing the dialog three times.

Four things to hand in.

First, the operating profit and the net income under each of the three, taken from the **Scenario summary** report with **Result cells** set to B12 and B14. The report is a sheet Excel writes, and that sheet is what gets opened.

Second, the break-even volume under each of the three, found with Goal Seek on B2 against a net income of 0, with the scenario shown first. Three numbers, and one line saying which input moved the break-even most.

Third, one sentence saying why B4 cannot be a changing cell in any of the three scenarios, and what would happen to the `Suppliers` link if somebody made it one.

Fourth, one sentence saying what three copies of the sheet would have given you instead, and what a grader would find on each of them.

---

## Week 17 · Printing, views and the final exam

### 17.1 · Recognise

**The workbook seen from the printer and from the screen**

Workbook `Exercise 4 Excel.xlsx`, one sheet named `World Data 2023`. Headers in row 1, 196 countries in rows 2 to 197, thirty-five columns running A to AI. Untouched, it prints on twenty pages.

Answer four blocks.

(a) The sheet has to keep row 1 and columns A and B on screen while the rest scrolls. Name the single cell that has to be clicked before **View**, **Window**, **Freeze Panes**, **Freeze Panes**, and give the two values that read back afterwards, `SplitRow` and `SplitColumn`. Then say what **Freeze Top Row** would have produced instead, with both numbers, and name the cheapest way to prove a freeze rather than a split is in effect.

(b) The print area is set to A1:J197 through **Page Layout**, **Page Setup**, **Print Area**, **Set Print Area**, and afterwards **Rows to repeat at top** is set to `$1:$1` on the **Sheet** tab. Say what **Name Manager** holds when you open it, giving both names and what each one refers to, and say what **Page Break Preview** shows about columns K to AI.

(c) The centre section of a custom footer is built with the field buttons and ends up reading `Page &P of &N`, and the right section reads `&A`. The job now prints on eight pages. Give both lines exactly as they print on page 3. Then say what would print on all eight pages if somebody had typed `Page 3 of 8` as literal text instead.

(d) Five settings are chosen in the Ctrl+P pane: Copies 3, **Print Entire Workbook**, **Landscape Orientation**, **Fit All Columns on One Page**, and **Collated**. The pane is closed without printing. Say which of the five are still there when the **Page Setup** dialog is reopened from the ribbon, and which are gone.

### 17.2 · Apply

**Twenty pages down to eight, and one pass through one dialog**

Work on `Exercise 4 Excel.xlsx`. Seven tasks, in this order, because the page counts only mean anything if the print area goes first.

First. Read the page counter under the Ctrl+P preview and write it down. Then set the print area to A1:J197 through **Page Layout** tab, **Page Setup** group, **Print Area**, **Set Print Area**. Read the counter again. Report both.

Second. Prove it was set rather than printed. Open **Formulas** tab, **Defined Names** group, **Name Manager** and report every name it now holds, with what each one refers to.

Third. Open **Page Layout** tab, **Page Setup** group, and click the dialog box launcher in the corner of the group. Do not close the dialog until every one of these is set. On **Page**: Landscape, and **Fit to** 4 pages wide by 5 tall. On **Margins**: **Center on page** horizontally. On **Header/Footer**: **Custom Footer**, with the page number and the number of pages in the centre section and the sheet name on the right, all inserted with the buttons above the boxes rather than typed. On **Sheet**: **Rows to repeat at top** `$1:$1`, and **Gridlines** ticked under **Print**. Click **Print Preview** inside the dialog, then **OK** once. Report the counter afterwards and what the **Page** tab reads when you reopen it.

Fourth. Make three copies of the sheet and treat each one differently: freeze the first column on the first, freeze at B4 on the second, and on the third put a split with the vertical bar past column C. For each copy say what stays put when you scroll, and how you would tell the third one from the other two without touching the ribbon.

Fifth. Export the whole file, not the sheet you are looking at: **File**, **Export**, **Create PDF/XPS Document**, **Create PDF/XPS**, then **Options**, then **Entire workbook** under **Publish what**, then **OK** and **Publish**. Report how many sheets came out and what the PDF would have held if **Options** had been skipped.

Sixth. Set the zoom to exactly 85 per cent. The slider at the corner cannot land on it, so use **View** tab, **Zoom** group, **Zoom**, and the **Custom** box. Report what the status bar reads.

Seventh. Open **New Window**, then **Arrange All** with **Vertical** and **Windows of active workbook** ticked. Report the two window captions exactly as the title bars show them, and say what tells you these are two windows onto one file rather than the file opened twice.

### 17.3 · Integrate

**The project workbook, ready to leave your screen**

Take the workbook you handed in for week 16. It carries the `Churrumpin` model with its data table, the `Credit` sheet, the `Tickets` data with its Excel table, the PivotTable and PivotChart of weeks 14 and 15, and the `Scenario Summary` sheet. Seven tasks, and this is the whole term walking out of the door.

First. Freeze `Tickets` so the header row and the Date and Waiter columns stay on screen. Name the anchor cell in your answer.

Second. Set a print area on `Tickets` covering the data and nothing else, and repeat the header row at the top of every page. Then do the same page setup on the `Churrumpin` and `Credit` sheets in a single operation, by Ctrl-clicking the three tabs before opening the dialog. Say which settings that grouping applied to all three and which one it could not.

Third. Build one custom footer with the file name on the left, `Page &P of &N` in the centre and the sheet name on the right, all through the field buttons. Then say what the right section prints on each of the three sheets, and why that is not the same string three times.

Fourth. Run **File**, **Info**, **Check for Issues**, **Check Compatibility**. Use **Select versions to show** to test against Excel 97-2003 and Excel 2010, and then click **Copy to New Sheet**. Hand in that sheet. Say in one line why this is the only one of the three inspection tools that leaves a record in the workbook.

Fifth. Try to store the current setup with **View**, **Workbook Views**, **Custom Views**. The button is greyed out. Say why, in one line, naming the feature that is blocking it and the week it arrived from.

Sixth. Export the entire workbook to PDF through **File**, **Export**, and report the page count. Then, through **File**, **Export**, **Change File Type**, save a second copy as an Excel Template. Say where Excel put it without asking you, and what that tells you about the format.

Seventh. In no more than six lines, say which route earned the mark on each of tasks one to six, and which faster route would have produced a workbook that looks the same and scores nothing.
