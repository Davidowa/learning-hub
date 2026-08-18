# Exercises · Information Analysis and Processing · TIA503

This set runs alongside the seventeen sessions of the course and is written for the Business group, who arrive using Excel and leave writing it. Every week brings three exercises. Recognise is answered by reading code and predicting what it leaves in the sheet, Apply is answered by writing a macro against a specification with the figures already given, and Integrate ties the week to the ones before it. The difficulty climbs across the term as well, so the Recognise of week 12 asks more than the Integrate of week 4. Each exercise is handed in on Blackboard as an `.xlsm` file plus the exported modules as `.bas`, except where the brief asks for something else. Every problem lives in the same five working databases: sales by region, payroll, budget against actual, marketing campaigns and the supplier catalogue.

---

## Week 01 · Course framing and the first recorded macro

### 01.1 · Recognise

**What a recorded macro leaves behind**

In the workbook `Suppliers.xlsm` somebody recorded this macro while tidying up the view of the catalogue. Column D holds the unit cost and column E the margin.

```vba
Sub HideCosts()
'
' HideCosts Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = False
End Sub
```

Answer three things. First, which columns are hidden once the macro finishes. Second, for the third statement line, which part is the object, which the property and which the value. Third, how many statement lines run and how many of them change the final state of the sheet.

### 01.2 · Apply

**Cut the lines that cancel each other**

This is what was left recorded after the analyst tried three arrangements before settling on one.

```vba
Sub PrepareCatalogue()
'
' PrepareCatalogue Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = False
    Columns("D:D").EntireColumn.Hidden = False
    Columns("D:D").EntireColumn.Hidden = True
End Sub
```

Hand in the edited version, meeting three conditions: when it finishes, column D is hidden and column E visible; no line undoes what another one did; and the procedure name does not change. Say as well how many lines you deleted and why the original macro reached the same final state even with lines to spare.

### 01.3 · Integrate

**The first recording of the supplier catalogue**

Type this table into a sheet named `Suppliers`, with the headers in row 1.

| Row | A · Code | B · Supplier | C · Stock | D · Unit cost |
|---|---|---|---|---|
| 2 | P-100 | Aceros del Bajío | 420 | 185.00 |
| 3 | P-101 | Empaques Lira | 180 | 64.50 |
| 4 | P-102 | Aceros del Bajío | 75 | 240.00 |
| 5 | P-103 | Papelera Central | 1250 | 12.80 |
| 6 | P-104 | Empaques Lira | 340 | 64.50 |

Save the workbook as `.xlsm`. With the recorder running, hide column D, hide column B, show B again and hide it once more. Stop recording and open the editor.

Hand in three things: the code exactly as the recorder wrote it, the same code without the lines that came from clicks you undid, and one line explaining what happens to the macro if you save the workbook as `.xlsx`. The edited macro has to leave B and D hidden, and running it twice in a row has to give the same result as running it once.

---

## Week 02 · Unit 1 · The VBA editor

### 02.1 · Recognise

**Where each macro turns up**

The commercial targets workbook carries two procedures, in two different places of the project tree.

```vba
' In Module1, a standard module
Sub LoadTargets()
    Range("B2").Value = 120000
    Range("B3").Value = 95000
    Range("B4").Value = 143000
End Sub
```

```vba
' In Sheet1, the sheet module
Sub AnnounceTargets()
    MsgBox "Quarter targets loaded"
End Sub
```

Answer three things. Which of the two turns up in the macro dialog when you press Alt + F8, and why the other one does not. What is left in B2, B3 and B4 after running `LoadTargets` with F5. And if you stop execution with the yellow highlight already sitting on `Range("B3").Value = 95000`, what B2 and B3 hold at that instant.

### 02.2 · Apply

**Three procedures and one call**

In a standard module named `Campaigns`, write three procedures by hand. No recorder.

`ShowSegment` puts up a message box with the exact text `Premium segment: 3 campaigns`.

`WriteTotals` writes 3350 into cell B2 and 50250 into cell B3. Those are the contacts and the cost of the Premium segment.

`PrepareSummary` writes nothing and shows nothing of its own: it calls the other two with `Call`, in that order.

Hand in the module exported as `.bas` and a screenshot of the macro dialog with the three names showing.

### 02.3 · Integrate

**The recorded macro, now written by hand**

Go back to the `Suppliers.xlsm` workbook from last week. The macro you edited works, but it was recorded and its name does not say which column it touches.

In a standard module named `Catalogue`, write three procedures by hand. `HideUnitCost` hides column D and shows the message `Cost column hidden`. `ShowUnitCost` brings it back and shows the message `Cost column visible`. `ReviewCatalogue` calls the first one with `Call` and writes the text `Reviewed` into F1.

Then run `ReviewCatalogue` with F8, with the sheet and the editor side by side, and hand in this trace filled in. The first F8 highlights the `Sub` line, and from there on the highlighted line is the one about to run, not the one that just ran.

| F8 | Highlighted line | Column D | F1 |
|---|---|---|---|
| step 1 | | | |
| step 2 | | | |
| step 3 | | | |
| step 4 | | | |
| step 5 | | | |
| step 6 | | | |
| step 7 | | | |
| step 8 | | | |

---

## Week 03 · Unit 1 · Types, variables and cells

### 03.1 · Recognise

**Three declarations that do not give what they look like**

The three fragments come from the payroll workbook. Say what happens with each one.

```vba
' (a)
Dim daysWorked As Integer
daysWorked = 14.5
Range("C2").Value = daysWorked
```

```vba
' (b)
Dim firstRef, lastRef As Integer
firstRef = 41020
lastRef = 41020
```

```vba
' (c) the module has no Option Explicit
Dim units As Long
units = 420
unts = 75
MsgBox units
```

For (a), which number ends up in C2. For (b), which of the two assignments stops and with what error, and why the other one does not. For (c), what the message shows, and what would change if the module started with `Option Explicit`.

### 03.2 · Apply

**A supplier record with the type each field deserves**

In a module starting with `Option Explicit`, write `Sub SupplierRecord()`. Declare one variable per field with the type it deserves, assign it these values and write them into row 1 of an empty sheet.

| Field | Value |
|---|---|
| Code | P-101 |
| Supplier | Empaques Lira |
| Tax ID | ELI980312QX4 |
| Stock | 180 |
| Unit cost | 64.50 |
| Active | true |

The code goes in A1 and the other fields to its right, in that order. Use `Range` for A1 and `Offset` for the other five. In G1 write the inventory value of that code, which is the stock times the unit cost.

No variable may be left as a `Variant` and none may be named with a single letter. The tax ID goes in as text, digits and all.

### 03.3 · Integrate

**From the catalogue to the record, with variables**

On the `Suppliers` sheet from week 1, write `Sub InventoryValue()` in a module with `Option Explicit`. The procedure has to do five things, in this order.

Read the stock from C2 and the unit cost from D2 into two variables declared with their type. Compute the inventory value of that row. Write it into E2. Show a message box with that same number. And at the end, hide column D with the statement from week 1.

Run the procedure from the macro dialog, not from the editor. Hand in the `.bas` and the `.xlsm` with E2 already written.

---

## Week 04 · Unit 1 · Operations and range names

### 04.1 · Recognise

**Six sums from the budget close**

Say what is left in each cell when this procedure runs.

```vba
Sub Sums()
    Range("D2").Value = 250000 - 180000 / 12
    Range("D3").Value = (250000 - 180000) / 12
    Range("D4").Value = 100 \ 7
    Range("D5").Value = 100 Mod 7
    Range("D6").Value = -3 ^ 2
    Range("D7").Value = 7.5 \ 2
End Sub
```

Then answer two questions. Which of the six expressions returns a different number if you write it as a formula in the cell instead of in VBA, and what that number is. And what D4 and D5 represent if the problem is packing 100 pieces into boxes of 7.

### 04.2 · Apply

**The equivalent monthly rate, made readable**

Finance needs annual inflation converted to its compounded monthly equivalent. Write `Sub EquivalentMonthlyRate()` doing five things.

Create two range names with `ThisWorkbook.Names.Add`: `AnnualInflation` for `Sheet1!$B$1` and `MonthlyInflation` for `Sheet1!$B$2`.

Write 0.065 into `AnnualInflation`.

Compute the equivalent monthly rate with the power formula, that is one plus the annual rate raised to one twelfth, minus one.

Leave the result in `MonthlyInflation` and give that cell the format `0.00%`.

Write into B3 the same result converted to text with `Format` and format `0.00%`, and into B4 the same result cut to six decimals with `Round`.

Hand in the `.bas` and the `.xlsm`, and add a one-line comment saying why B2 and B3 look identical on screen and are not good for the same thing.

### 04.3 · Integrate

**Budget variance with names**

Type this table into a sheet named `Budget`, with headers in row 1 and the totals already written into row 6.

| Row | A · Account | B · Budget | C · Actual |
|---|---|---|---|
| 2 | Salaries | 1850000.00 | 1912400.00 |
| 3 | Advertising | 640000.00 | 588300.50 |
| 4 | Travel | 215000.00 | 268900.00 |
| 5 | IT | 430000.00 | 430000.00 |
| 6 | Total | 3135000.00 | 3199600.50 |

Write `Sub ComputeVariance()` in a module with `Option Explicit`. It has to create four range names: `BudgetTotal` for `$B$6`, `ActualTotal` for `$C$6`, `VarianceTotal` for `$D$6` and `VariancePct` for `$E$6`. Then it reads the two totals into variables with their type, computes the variance in pesos and the variance as a proportion of the budget, and writes both into their named cells. Give the variance in pesos the format `$#,##0.00` and the proportion the format `0.00%`.

Once the names are created, no statement in your code may refer to D6 or E6 by coordinate.

---

## Week 05 · Unit 1 · Data entry and messages

### 05.1 · Recognise

**What comes back from an entry box**

The payroll macro asks for the days worked with an `InputBox`. Fill in the table with what `IsNumeric` returns and what `CDbl` does for each thing the user might type.

| What they type | IsNumeric | CDbl |
|---|---|---|
| 15 | | |
| 1,000 | | |
| $780.50 | | |
| fifteen | | |
| nothing, they pressed Cancel | | |

Then read this fragment and say exactly what happens when the user types `fifteen`, on which line it stops and with which error number.

```vba
Dim t As String
t = InputBox("Days worked", "Payroll")

If IsNumeric(t) And CDbl(t) > 0 Then
    Range("C2").Value = CDbl(t)
End If
```

### 05.2 · Apply

**Entry of days that takes no rubbish**

Write `Sub CaptureDays()`. The procedure asks for Ana Robles' days worked with an `InputBox` whose prompt is `Days worked by Ana Robles` and whose title is `Payroll`. While what they type is not a number greater than zero, it asks again, and before asking again it shows a box with the text `That is not a valid number of days.` and the warning icon.

Once the value is usable, it asks with a Yes and No box, with the question icon and the title `Confirm`, whether that number of days is to be saved. Only if the answer is Yes does it write the value into C2.

The validation has to sit in two nested `If` statements, not in a single one with `And`. Explain why in a comment.

### 05.3 · Integrate

**A payslip captured and confirmed**

Write `Sub CapturePayslip()` on a sheet named `Payroll`. Before anything else, create with `Names.Add` the names `DailyWage` for `$B$2`, `DaysWorked` for `$B$3`, `GrossPay` for `$B$4`, `Bonus` for `$B$5` and `TotalPay` for `$B$6`.

Ask for two values with validated entry, the daily wage and the days worked. Both have to be numbers greater than zero, and while they are not, the procedure insists. With good values in hand, compute the gross pay, the bonus, which is eight per cent of the gross, and the total pay. Write the five values into their named cells and give the format `$#,##0.00` to the three amount cells.

Close with a message box, with the information icon and the title `Payslip`, showing the three amounts on three separate lines using `vbNewLine`.

Test with a daily wage of 780.50 and 15 days. Note in the report the three amounts that came out.

---

## Week 06 · Unit 2 · Editing what you recorded

### 06.1 · Recognise

**The recorded macro against forty rows**

The `Sales` sheet has headers in row 1 and data from row 2 to row 41. The columns are A ref, B region, C salesperson and D amount. The macro was recorded last month, when the database carried eight rows.

```vba
Sub FormatAmounts()
    Range("D2:D9").Select
    Selection.NumberFormat = "$#,##0.00"
    Range("A1").Select
End Sub
```

Answer four things. How many rows end up with currency format when it runs today. Whether Excel flags any error. What `Cells(Rows.Count, 1).End(xlUp).Row` returns on this sheet. And what address `Range("A1").CurrentRegion` returns.

### 06.2 · Apply

**The same macro, for any number of rows**

Rewrite `FormatAmounts` so it works with whatever database it gets. It has to meet four conditions.

Not one `Select` and not one `Selection` is left in the code.

The last row is worked out from the bottom with `End(xlUp)` over column A and kept in a `Long` variable.

The amounts range is built with `Range(Cells(...), Cells(...))` and kept in a variable declared `As Range`, assigned with `Set`.

That range gets the format `$#,##0.00`, and F1 gets how many rows of data the database has, not counting the header.

Test it with the eight-row database and note what ended up in F1.

### 06.3 · Integrate

**The catalogue and its helper column**

On the `Suppliers` sheet from week 1, write `Sub PrepareCatalogue()` in a module with `Option Explicit`. It has to do four things.

Work out the last row with data and build with `Cells` the range of unit costs, from row 2 to the last one, in column D. Give that range the format `$#,##0.00`.

Create the range name `TotalRows` for `$G$1` and write there how many suppliers the database holds.

Check whether column E is hidden. If it is, show it; if it is not, hide it. Column E is never deleted.

Close with a message box showing the address of the cost range it built, read from the `Address` property.

Run the macro twice in a row and note what happens to column E on each run.

---

## Week 07 · Unit 2 · Goal Seek and chaining

### 07.1 · Recognise

**What a goal seek gives back**

The pricing model for a product line lives on a sheet with these range names already created.

| Name | Cell | Contents |
|---|---|---|
| UnitPrice | B2 | 120.00 |
| Units | B3 | 12000 |
| VariableCost | B4 | 84.00 |
| FixedCosts | B5 | 380000.00 |
| TotalMargin | B6 | the formula `=(UnitPrice-VariableCost)*Units-FixedCosts` |

With those values, B6 shows 52,000.00. This macro is run.

```vba
Sub SeekPrice()
    Range("TotalMargin").GoalSeek _
        Goal:=250000, _
        ChangingCell:=Range("UnitPrice")
End Sub
```

Answer four things. Which of the two cells the macro names cannot hold a formula, and why. What unit price the search arrives at. Whether B6 is worth exactly 250,000.00 when it finishes, and which two `Application` properties govern that answer. And what happens if somebody writes `ChangingCell:=Range("TotalMargin")`.

### 07.2 · Apply

**The master that bounds and seeks**

Write four procedures in the same module, over the pricing model from 7.1.

`LoadParameters` writes the four input values into their named cells: 120.00, 12000, 84.00 and 380000.00.

`FormatModel` gives the format `$#,##0.00` to the price, variable cost, fixed costs and margin cells.

`SeekPrice` runs the goal seek to leave the margin at 250,000.

`ClosePrice` is the master. It switches off screen redrawing and puts calculation on manual while the parameters are loaded and formatted, calls the other three in order with `Call`, and leaves both properties as it found them before it ends. Make sure the goal seek runs with the sheet recalculating: it is a method that gropes, and if the margin formula is not re-evaluated on every try, it has nothing to compare against.

The master may not exceed ten statement lines and may not carry a single one that touches a cell. Any of the other three has to be runnable on its own from the macro dialog.

### 07.3 · Integrate

**The margin as a function, and the price as the answer**

On the same model, add two things.

A function `ComputedTotalMargin` taking the price, the units, the variable cost and the fixed costs, all four `As Double`, and returning the margin. With 120, 12000, 84 and 380000 it has to return the same number B6 shows.

A procedure `CompareMargin` that calls that function with the current values of the named cells, writes the result into B8 and compares it against what B6 holds. If the two numbers agree, it writes the text `Matches` into B9; if they do not, it writes `Check`.

After that, run `ClosePrice` and note three numbers: the price the search found, the value left in B6 and the difference against 250,000. That third number is the point of the exercise, so report the one you measured rather than the one you expected.

---

## Week 08 · Unit 3 · Decisions and the first midterm

### 08.1 · Recognise

**Seven comparisons that answer backwards**

The region column of the `Sales` sheet was typed by hand and carries Norte, norte and NORTE mixed together. Cell A1 of a new sheet is empty, with nothing written in it. Say what each of these comparisons returns.

```vba
MsgBox "Norte" = "norte"
MsgBox "10" < "9"
MsgBox 10 < 9
MsgBox CInt(True)
MsgBox Range("A1").Value = 0
MsgBox Range("A1").Value = ""
MsgBox Range("A1").Value > 0
```

Then answer two business questions. If you group sales by the text of the region column exactly as it was typed, how many different regions Excel is going to report for the north. And if a sale was recorded with the amount left blank, which of the last three comparisons is no use for telling it apart from a sale of zero pesos.

### 08.2 · Apply

**Tiering a sale amount, two ways**

The commercial area tiers every sale by its amount with this table.

| Amount | Tier |
|---|---|
| 150,000 or more | A |
| 100,000 up to under 150,000 | B |
| 50,000 up to under 100,000 | C |
| under 50,000 | D |

Write two procedures reading the amount from D2 and writing the tier into E2. `ClassifyWithIf` uses `If`, `ElseIf` and `Else`. `ClassifyWithCase` uses `Select Case`. Both have to give the same result for the four test amounts: 210500, 128400, 65900 and 41200.

No sale may be left without a tier. Close with a two-line comment saying why in this case the cases are better written with `Is` than with `To`, and which of the two forms you prefer.

### 08.3 · Integrate

**First midterm review: from the click to the account tier**

This exercise crosses the three units the midterm covers. On the eight-row `Sales` sheet, hand in a module with a master named `ReviewAccount` and three procedures for it to call.

The master switches off redrawing and automatic calculation, calls the three in order and switches them back on.

`CaptureAmount` asks for an amount with `InputBox`, insists until it is a number greater than zero and writes it into the named cell `ReviewedAmount`, which your code creates pointing at `$G$2`.

`MeasureData` works out the last row with data in column A, builds with `Cells` the amounts range in column D and writes into the named cell `TotalRows` how many rows of data there are.

`ClassifyAmount` reads `ReviewedAmount`, applies the tier table from 8.2 to it with `Select Case` and writes the tier into the named cell `ReviewedTier`, which your code creates pointing at `$G$3`, as well as giving `ReviewedAmount` the format `$#,##0.00`.

There may be no loop, no `Select` and no hand-typed cell address inside `ClassifyAmount`. Hand in as well a three-row table saying which week each procedure comes from.

---

## Week 09 · Unit 3 · Repetition

### 09.1 · Recognise

**Three loops and what they leave**

Say what each one produces.

```vba
' (a)
Dim i As Long
Dim message As String
message = "Periods: "
For i = 10 To 1 Step -3
    message = message & i & " "
Next i
MsgBox message
```

```vba
' (b) over range A1:B2 of the campaigns sheet
Dim cell As Range
Dim order As String
For Each cell In Range("A1:B2")
    order = order & cell.Address & " "
Next cell
MsgBox order
```

```vba
' (c) rows 2 to 7 all carry the mark X in column E
Dim r As Long
For r = 2 To 7
    If Cells(r, 5).Value = "X" Then
        Rows(r).Delete
    End If
Next r
```

For (a), the exact text of the message. For (b), the order in which it hands over the four cells. For (c), how many of the six marked campaigns are left on the sheet when it finishes, and what changes if the loop is written `For r = 7 To 2 Step -1`.

### 09.2 · Apply

**Flagging the overdue book**

Type this database into a sheet named `Receivables`, with headers in row 1.

| Row | A · Customer | B · Invoice | C · Amount | D · Days overdue |
|---|---|---|---|---|
| 2 | Aceros del Bajío | F-2201 | 77700.00 | 12 |
| 3 | Empaques Lira | F-2202 | 11610.00 | 45 |
| 4 | Papelera Central | F-2203 | 16000.00 | 0 |
| 5 | Aceros del Bajío | F-2204 | 18000.00 | 61 |
| 6 | Empaques Lira | F-2205 | 21930.00 | 30 |
| 7 | Comercial Sáenz | F-2206 | 40120.00 | 38 |

Write `Sub FlagOverdue()`. Work out the last row with data, walk the database from row 2 and, on every row whose days overdue go past 30, write `Overdue` into column E and add its amount up. When it finishes, write into G1 how many invoices were flagged and into G2 the accumulated overdue amount, with the format `$#,##0.00`.

A row with exactly 30 days overdue is not flagged. No cell address inside the loop may be typed by hand.

### 09.3 · Integrate

**Cleaning up the campaign list**

Type this database into a sheet named `Campaigns`. Cells C4 and C6 are left empty on purpose, with no zero written in them.

| Row | A · Campaign | B · Segment | C · Contacts | D · Cost |
|---|---|---|---|---|
| 2 | C-01 | Premium | 1250 | 18750.00 |
| 3 | C-02 | New | 3400 | 27200.00 |
| 4 | C-03 | Premium | | 14700.00 |
| 5 | C-04 | Mass | 7600 | 38000.00 |
| 6 | C-05 | Premium | | 16800.00 |
| 7 | C-06 | Mass | 5300 | 26500.00 |

Write two procedures and a master that calls them.

`ClassifyCampaigns` walks the database with a variable range and writes into column E: `No data` if the contacts cell is empty, `Mass` if it carries 3000 contacts or more, and `Targeted` in any other case. It keeps three counters and writes them into G1, G2 and G3.

`DropNoData` deletes the rows classified as `No data`, walking in the direction that does not skip rows.

The master switches off redrawing, calls the two and switches it back on.

Note in the report the three counters and how many rows of data are left at the end.

---

## Week 10 · Units 1 and 3 · Procedures and functions

### 10.1 · Recognise

**A Sub that changes what nobody asked it to**

This module comes from the payroll workbook.

```vba
Sub ApplyBonus(amount As Double)
    amount = amount * 1.08
End Sub

Function PayslipTotal(gross As Double, bonus As Double) As Double
    ' the sum was meant to go here and never got written
End Function

Sub Test()
    Dim gross As Double
    gross = 11707.5

    ApplyBonus gross
    Range("B2").Value = gross
    Range("B3").Value = PayslipTotal(11707.5, 936.6)
End Sub
```

Say what is left in B2 and what is left in B3, and why neither case raises an error. Then give the one-word change that would leave B2 at 11707.5, and the missing line that would leave B3 at 12644.1.

### 10.2 · Apply

**A commission function Excel will take in a cell**

The commission on a sale is worked out with this table.

| Sale amount | Commission |
|---|---|
| 150,000 or more | 6 % |
| 100,000 up to under 150,000 | 4 % |
| 50,000 up to under 100,000 | 2.5 % |
| under 50,000 | 0 % |

Write `Function SaleCommission(ByVal amount As Double) As Double` in a standard module. Then type the sales database into a sheet named `Sales`, with headers in row 1.

| Row | A · Ref | B · Region | C · Salesperson | D · Amount |
|---|---|---|---|---|
| 2 | V-1001 | Norte | Ana Robles | 128400.00 |
| 3 | V-1002 | Sur | Beto Lira | 96750.00 |
| 4 | V-1003 | Norte | Carla Méndez | 143200.00 |
| 5 | V-1004 | Centro | Darío Sáenz | 87300.00 |
| 6 | V-1005 | Sur | Ana Robles | 210500.00 |
| 7 | V-1006 | Centro | Beto Lira | 65900.00 |
| 8 | V-1007 | Norte | Carla Méndez | 54120.00 |
| 9 | V-1008 | Bajío | Darío Sáenz | 181045.00 |

In cell E2 type by hand the formula calling your function with that row's amount, and copy it down to E9. In E10 put the sum of the column. Hand in the `.xlsm` with the nine cells solved and note the commission total.

### 10.3 · Integrate

**Payroll split into pieces**

Type this database into the `Payroll` sheet, with headers in row 1.

| Row | A · Employee | B · Number | C · Days | D · Daily wage | E · Bonus |
|---|---|---|---|---|---|
| 2 | Ana Robles | 4102 | 15 | 780.50 | 0.08 |
| 3 | Beto Lira | 4118 | 15 | 612.00 | 0.05 |
| 4 | Carla Méndez | 4127 | 13 | 945.00 | 0.10 |
| 5 | Darío Sáenz | 4130 | 15 | 528.40 | 0.00 |

Write one function and three procedures.

`TotalPay` takes the days, the daily wage and the bonus percentage, all three `As Double` and all three by value, and returns the total pay of the payslip.

`ComputePay` walks the database with a variable range and writes each employee's total pay into column F, calling the function. It computes nothing on its own.

`FlagIncomplete` walks the database and writes `Check` into column G of every row where the days worked come to fewer than 15.

`TotalPayroll` adds up column F by walking it and writes the total into the row after the last one with data, with the format `$#,##0.00`.

`ProcessPayroll` is the master: it switches off redrawing, calls the three procedures in order and switches redrawing back on.

The master does not exceed ten statement lines and no procedure exceeds forty. Each one has to run on its own from the macro dialog. Note the four payments and the total.

---

## Week 11 · Units 2 and 3 · Events

### 11.1 · Recognise

**The same handler in two different places**

The two fragments are the same handler in two different places. Say what happens in each case, then answer part (c), which comes at the end.

```vba
' (a) pasted into Module1, a standard module
Private Sub Worksheet_Change(ByVal Target As Range)
    MsgBox "Changed " & Target.Address
End Sub
```

```vba
' (b) pasted into the sheet module of an empty test sheet
Private Sub Worksheet_Change(ByVal Target As Range)
    Target.Offset(0, 1).Value = "checked"
End Sub
```

For (a), what happens when you write into B2 of that sheet, and whether Excel warns you about anything. For (b), what happens when you write 15 into B2, and why.

For (c), fill in the table. It is the handler from (b) with a guard on B2, which instead of always writing the same thing asks `IsNumeric(Target.Value)` and writes `Number` or `Not a number` into C2. The two middle columns are not the same question: the handler fires after Excel has already interpreted what was typed, so `Target.Value` is not always the text the user entered. Answer both and say on which rows they differ.

| What gets typed into B2 | `IsNumeric` on that text | `IsNumeric(Target.Value)` | What gets written into C2 |
|---|---|---|---|
| 15 | | | |
| 12.5 | | | |
| $780.50 | | | |
| 15% | | | |
| fifteen | | | |

### 11.2 · Apply

**The entry cell that checks itself**

Work on the `Payroll` sheet from week 10, where column C holds the days worked. In that sheet's module write the `Worksheet_Change` handler meeting this.

It reacts only when the change happens in C2. Any other change to the sheet is ignored.

If what was entered is a number, it writes the text `Valid days` into H2 and gives C2 the format `0`. If it is not, it writes `Check entry` into H2 and gives C2 a yellow fill with `Interior.Color`.

Writing into H2 may not fire the handler again. Solve it with the address guard and explain in a comment why that guard is enough here and would not be enough if the handler also wrote into C2.

Test by writing into C2 twenty times in a row. If Excel goes down, the guard is in the wrong place.

### 11.3 · Integrate

**The payroll workbook that gets itself ready**

On the week 10 workbook, add two handlers and leave them working with the function you already have.

In `ThisWorkbook`, a `Workbook_Open` activating the `Payroll` sheet, selecting C2 and showing a box with the text `Enter the days worked in C2`.

In the module of the `Payroll` sheet, a `Worksheet_Change` reacting only to C2. If the entered value is a number greater than zero, it calls the `TotalPay` function from week 10 with that number of days, the daily wage from D2 and the bonus from E2, and writes the result into F2 with the format `$#,##0.00`. If it is not a valid number, it leaves F2 empty and writes `Check entry` into G2.

Since the handler writes into two cells, switch events off while it writes and switch them back on. Note what is left in F2 when 15 days are entered for Ana Robles.

---

## Week 12 · Unit 3 · Custom classes

### 12.1 · Recognise

**Two names for the same object**

The project carries a class module named `Supplier` with one private field per value, `Get` and `Let` properties for `Code`, `Stock` and `UnitCost`, and a function `Value` returning the stock times the unit cost. The `Let UnitCost` property leaves the field at zero if it is handed a negative number.

Say what each block prints, or with which error it stops.

```vba
' (a)
Dim a As Supplier, b As Supplier
Set a = New Supplier
Set b = a

a.UnitCost = 185
a.Stock = 420
b.Stock = 75

Debug.Print a.Value
```

```vba
' (b)
Dim s As Supplier
s.Code = "P-100"
```

```vba
' (c)
Dim s As Supplier
Set s = New Supplier
s.Stock = 420
s.UnitCost = -185

Debug.Print s.Value
```

For (a) say as well how many objects were created in total and what would have to change for `a` and `b` to be independent.

### 12.2 · Apply

**The Supplier class**

Create a class module and name it `Supplier`. It has to carry this.

Three private fields: `pCode As String`, `pStock As Long` and `pUnitCost As Double`.

`Get` and `Let` properties for all three. The stock one and the unit cost one reject negatives: handed one, they leave the field at zero. The validation lives in the class, never in the macro using it.

A public function `Value` returning the stock times the unit cost.

A `Class_Initialize` leaving the code at `no code` and both numbers at zero.

Write as well a `Sub TestSupplier()` in a standard module creating an object, printing its newborn state, assigning it P-100, 420 and 185.00, printing its value, then assigning it a cost of -50 and printing its value again. Use `Debug.Print` and hand in the Immediate window in the screenshot.

### 12.3 · Integrate

**One object per row of the catalogue**

On the `Suppliers` sheet from week 1, write `Sub ValueCatalogue()`.

Work out the last row with data. Walk the database from row 2 and, on every turn, create a fresh `Supplier` object, assign it the code, the stock and the unit cost of that row, and write into column E the value the object returns. Accumulate that value into a variable and, at the end, write it into the named cell `TotalValue`, which your code creates pointing at `$G$1`, with the format `$#,##0.00`.

Three conditions. The `New` goes inside the loop, not before it. No value calculation lives outside the class. And if a row carries an empty stock cell, the object stays at zero and the row is flagged with `Check` in column F.

Note the value per row and the total.

---

## Week 13 · Unit 4 · Cleaning and sorting

### 13.1 · Recognise

**What dirties a database and does not show**

Answer the four blocks.

```vba
' (a)
Debug.Print "[" & Trim("  Aceros del Bajío  ") & "]"
Debug.Print "[" & Trim("Aceros    del Bajío") & "]"
Debug.Print "[" & WorksheetFunction.Trim("Aceros    del Bajío") & "]"
```

```vba
' (b)
Dim s As String
s = "Lira" & Chr(160)

Debug.Print Len(s), Len(Trim(s))
Debug.Print Trim(s) = "Lira"
```

```vba
' (c)
Debug.Print WorksheetFunction.Proper("empaques lira")
Debug.Print WorksheetFunction.Proper("aceros del bajío")
Debug.Print WorksheetFunction.Proper("PAPELERA central")
```

```vba
' (d) the database occupies B1:C4, with headers
'     B: Supplier        C: Code
'     Empaques Lira      P-101
'     Aceros del Bajío   P-100
'     Empaques Lira      P-104

Range("B1:C4").RemoveDuplicates Columns:=2, Header:=xlYes
```

For (c) say which of the three results is not what the user wanted. For (d), how many rows are left and what number would have to be passed in `Columns` to strip the repeated suppliers.

### 13.2 · Apply

**Cleaning the supplier column**

Column A of the `Dirty` sheet carries the names exactly as they arrived from another system, from row 2 onwards.

| Row | What the cell holds |
|---|---|
| 2 | two spaces, `aceros del bajío`, one space |
| 3 | `empaques    lira`, with four spaces in the middle |
| 4 | `PAPELERA central` |
| 5 | `comercial sáenz` followed by a hard space, `Chr(160)` |

Write `Sub CleanSuppliers()`. Work out the last row with data, walk column A with `For Each` over the range you build, and leave each name clean in three steps: first swap the hard space for an ordinary one, then collapse the spare spaces with the sheet version of `Trim`, and finally even out the case with `Proper`.

The order of the three steps matters. Explain it in a comment. Note the four names that came out.

### 13.3 · Integrate

**Second midterm review: the database ready for the report**

This exercise crosses week 8 to week 13. Type the dirty database into a sheet named `Sales`, exactly as it stands, with row 4 completely empty.

| Row | A · Ref | B · Region | C · Salesperson | D · Amount |
|---|---|---|---|---|
| 2 | V-1001 | Norte | Ana Robles | 128400.00 |
| 3 | V-1002 | sur | Beto Lira | 96750.00 |
| 4 | | | | |
| 5 | V-1003 | NORTE | Carla Méndez | 143200.00 |
| 6 | V-1002 | sur | Beto Lira | 96750.00 |
| 7 | V-1004 | Centro | Darío Sáenz | 87300.00 |
| 8 | V-1005 | Sur | Ana Robles | 210500.00 |

Write a master calling four procedures, in this order.

`EvenOutRegion` leaves column B with even case and no spare spaces.

`DeleteBlanks` deletes the rows with no data at all, walking in the right direction.

`RemoveRepeats` strips the sales with a repeated ref and keeps the first one that appeared.

`SortSales` sorts the whole database by region ascending and, inside each region, by amount descending, with the header declared.

When it finishes, the master writes into F1 how many rows of data are left and into F2 the total amount, with the format `$#,##0.00`. Hand in the database before and after on two sheets, and check row by row that every amount is still with its salesperson.

---

## Week 14 · Unit 4 · Filters, subtotals and tables

### 14.1 · Recognise

**The total that adds up what you cannot see**

Over the eight-row sales database from week 10, this is run.

```vba
Range("A1:D9").AutoFilter Field:=2, Criteria1:="Norte"
```

Three rows are left on the screen. The total of column D is then worked out four ways: with a `For Each` over `Range("D2:D9")`, with a `For Each` over that same range but asking it for `SpecialCells(xlCellTypeVisible)`, with the formula `SUBTOTAL(9,D2:D9)` written into a cell, and with the formula `SUM(D2:D9)`.

Say what each of the four returns and why two of them return the same wrong number.

Then answer this: the sheet has the header `Department` in F1 and the value `Norte` in F2, and the database has the header `Region` in B1. `Range("A1:D9").AdvancedFilter xlFilterInPlace, Range("F1:F2")` is run. How many rows are left visible and what error message appears.

### 14.2 · Apply

**The total of the filtered region**

Write `Sub VisibleRegionTotal()` over the sales database.

Read from cell H1 the name of the region to filter by. Apply the autofilter over the region column with that criterion. Walk only the visible cells of the amounts column and accumulate the total. Write into H2 how many rows were left visible and into H3 the total, with the format `$#,##0.00`.

Then, in H4, write the formula computing that same total with `SUBTOTAL` and check that the two numbers agree. If they do not, the loop is not respecting the filter.

Run the macro with `Norte`, with `Sur` and with `Bajío` in H1, and note the three pairs of numbers.

### 14.3 · Integrate

**The database as a table, with its summary by region**

Over the eight-row sales database, hand in three procedures and a master.

`ConvertToTable` turns the block surrounding A1 into a `ListObject` named `Sales2026`. If running it twice blows up because the name already exists, your code has to prevent that by checking first whether the sheet already has a table.

`SummariseByRegion` writes into the `Summary` sheet, starting at A1, one row for each of the four regions of the database, with its name, its number of sales and its total amount. It walks the table through the data body, not through a hand-typed address.

`TableHasRows` is a function returning `Boolean`. If the table body has no rows at all, it shows the message `The table has no rows` and returns false. The master asks it before requesting the summary.

The master switches off redrawing, calls what is needed in order and switches it back on.

Note the complete summary. Then add two new sales at the end of the table, run the master again and check that they turn up in the summary without a single range in the code having been touched.

---

## Week 15 · Units 4 and 5 · Reports and R1C1

### 15.1 · Recognise

**Two libraries and a lookup that falls over**

Answer the four blocks. The range named `Catalogue` runs from A1 to B4 on the `Codes` sheet, and carries P-100 with Aceros del Bajío, P-101 with Empaques Lira and P-103 with Papelera Central.

```vba
' (a)
Debug.Print WorksheetFunction.Left("Aceros del Bajío", 6)
Debug.Print Left("Aceros del Bajío", 6)
```

```vba
' (b)
Dim v As Variant

Debug.Print WorksheetFunction.VLookup("P-999", Range("Catalogue"), 2, False)

v = Application.VLookup("P-999", Range("Catalogue"), 2, False)
Debug.Print IsError(v)
```

```vba
' (c) A1 is worth 10 and A2 is worth 20
Range("C1").Formula = "=SUM(A1:A2)"
Range("D1").Value = WorksheetFunction.Sum(Range("A1:A2"))
' and now somebody changes A1 to 100
```

```vba
' (d)
Range("C2").Formula = "=A2*B2"
Debug.Print Range("C2").FormulaR1C1
```

For (b) say the error number of each one and which of the two lets you carry on. For (c), what C1 and D1 show before and after the change. For (d), the exact string it prints.

### 15.2 · Apply

**The description for each code, without stopping the report**

The `Codes` sheet carries the range named `Catalogue` in A1:B4, with headers in row 1 and these three matches: P-100 with Aceros del Bajío, P-101 with Empaques Lira and P-103 with Papelera Central. The `Movements` sheet carries this, with headers in row 1.

| Row | A · Code | B · Amount |
|---|---|---|
| 2 | P-100 | 25000.00 |
| 3 | P-101 | 12400.00 |
| 4 | P-100 | 18600.00 |
| 5 | P-103 | 9750.00 |
| 6 | P-107 | 31200.00 |
| 7 | P-101 | 7300.00 |
| 8 | P-100 | 22050.00 |
| 9 | P-103 | 14800.00 |

Write `Sub CompleteMovements()`. Walk the eight rows with a variable range and, for each one, look up the supplier name in the catalogue and write it into column C. If the code is not there, write `not in catalogue` into column C and paint the three cells of that row yellow. The macro may not stop on row 6.

Then write into E1 the total of Aceros del Bajío amounts using `SumIfs` over the names column, and into E2 how many movements those are, with `CountIf`.

The variable receiving the lookup result has to be declared `As Variant`. Explain in a comment why a `String` is no use there.

### 15.3 · Integrate

**The monthly catalogue report**

On the five-row `Suppliers` sheet, build the complete report. On the `Codes` sheet leave the range named `Catalogue`, with headers and two matches only: `Aceros Del Bajío` with `Metals` and `Empaques Lira` with `Packaging`. Papelera Central is not in the catalogue, on purpose.

Hand in a master and four procedures.

`CleanNames` leaves column B with no spare spaces, no hard spaces and even case.

`ComputeValue` writes column E, the inventory value of each row, with a single statement in R1C1 notation over the whole range. No loops and no building the formula string by gluing the row number in.

`SummariseBySupplier` writes into the `Summary` sheet one row per supplier with its total value, computed with `SumIfs` over column E, and the sector brought in from the `Catalogue` range with a lookup that does not stop the macro when the supplier is missing.

`ChartSummary` adds a clustered column chart over the summary, with the title `Value by supplier`. If a chart already exists on that sheet, it deletes it before creating the new one.

The master switches off redrawing and calculation, calls the four and switches them back on. Note the total value per supplier and the grand total, and say whether you left column E as a live formula or as a frozen value, with one line of justification.

---

## Week 16 · Units 4 and 6 · Pivots, errors and protection

### 16.1 · Recognise

**The pivot that shows yesterday's total**

Over the eight-row sales database, with a total of 967,215.00, a PivotTable is created from a macro with the cache built over `A1:D9`, the region down the rows and the amount in the data. Then this happens, in order: the amount on row 2 is changed from 128,400.00 to 200,000.00; `pt.RefreshTable` is run; a new sale of 50,000.00 is added on row 10 and it is refreshed again.

Say what grand total the pivot shows at each of the four moments, and why refreshing does not fix the last one.

Then answer this block.

```vba
On Error Resume Next

Set wb = Workbooks.Open("C:\closes\january.xlsx")   ' the file does not exist
total = 2 + 2

If Err.Number <> 0 Then
    MsgBox "The sum failed"
End If
```

What the message shows, what value `Err.Number` carries on each line, and which two statements would have to be added for the diagnosis to point at the line that actually failed.

### 16.2 · Apply

**The regional breakdown, with a net**

Write `Sub RegionalBreakdown()` over the sales database.

Create the PivotTable from code, with the cache built over the block surrounding A1, the region as row field and the amount as data field, with its destination in cell A1 of the `Summary` sheet. If a pivot by that name already exists, delete it before creating it. Refresh it when you finish.

The whole procedure goes under a real error handler, with `On Error GoTo` and a label at the end showing the error number and description and switching redrawing and calculation back on. Between the body and the label has to go the statement stopping the normal flow from falling into the handler.

Note the four rows of the breakdown and the grand total.

### 16.3 · Integrate

**Closing the project workbook**

On the sales workbook, leave the three pieces still missing before it can be handed in.

Turn the database into a table and build the pivot from 16.2 taking the table as its source, not a range. Check that adding rows and refreshing brings them into the breakdown.

Protect every sheet with a password and with `UserInterfaceOnly` set to `True`, from a `Workbook_Open` in `ThisWorkbook`. Check that the user cannot write into a cell by hand and that your macros can.

Give the master an error handler that, as well as warning, leaves events switched on, calculation on automatic and redrawing switched on, whatever happens.

In the report explain in three lines why `UserInterfaceOnly` has to be reapplied on every open and what would happen if the macro stopped just after switching events off.

---

## Week 17 · Closing · Final exam

### 17.1 · Recognise

**Five errors with a number and six silent failures**

First, say with which error number each scenario stops and why.

| Scenario | Err |
|---|---|
| The amount is divided by the number of invoices and that cell is empty | |
| `CDbl` is used on what the user typed as `fifteen` | |
| A `Supplier` object is declared and given its code without having been given `New` | |
| `WorksheetFunction.Left` is asked for over a piece of text | |
| `WorksheetFunction.VLookup` is used to look up a code that is not in the catalogue | |

Then, of these six operations, say what wrong result each one produces and confirm that none of them raises an error.

Sorting the amounts column without including the rest of the database. Walking a filtered range with `For Each`. Writing the criteria header of an advanced filter with another name. Inserting subtotals without having sorted first. Reading a pivot without refreshing it. Checking `Err.Number` three lines after the statement that could fail.

### 17.2 · Apply

**Repairing a macro that runs and lies**

This macro runs from start to finish, raises no error at all, and the report it produces is wrong in five separate ways.

```vba
Sub PendingReport()
    Application.Calculation = xlCalculationManual

    Dim r As Long
    For r = 2 To 9
        If Cells(r, 4).Value < 50000 Then
            Rows(r).Delete
        End If
    Next r

    Range("D2:D9").Sort Key1:=Range("D2"), _
                        Order1:=xlAscending, Header:=xlNo

    For r = 2 To 9
        Cells(r, 5).Value = WorksheetFunction.VLookup( _
            Cells(r, 1).Value, Range("Catalogue"), 2, False)
    Next r
End Sub
```

Hand in the corrected version and a five-row table saying, for each defect, what it does wrong, what result it produces and which week of the course the fix comes from. The corrected version has to work with a database of any size.

### 17.3 · Integrate

**The exam: a dirty database and a report that defends itself**

You are handed a workbook with a `Sales` sheet carrying headers in row 1, an unknown number of data rows, regions typed with uneven case and spare spaces, some completely empty rows, repeated refs and some blank amounts. It also carries the `Codes` sheet, with the range named `Catalogue` matching each salesperson to their manager, and with one salesperson missing.

Hand in a module with a master and whatever procedures are needed, one per task, leaving the workbook like this.

The database clean: even regions, no empty rows, no repeated refs, sorted by region ascending and by amount descending inside each region.

A tier column, computed with the table from week 8, written by a function of your own that can also be used from a cell.

A manager column, brought in from the catalogue with a lookup that does not stop the macro and that flags the missing salesperson as `not in catalogue`.

A `Summary` sheet with a PivotTable created from code, with the region down the rows and the amount in the data, taking a table as its source so it grows on its own, plus a column chart.

An error handler on the master leaving calculation on automatic, redrawing switched on and events switched on even if something blows up, and the protection with `UserInterfaceOnly` reapplied when the workbook opens.

No hand-typed cell address inside the loops. In the written report, explain one design decision you took and which alternative you ruled out, and point out which of the procedures fails in silence if you remove the line that works out the last row.
