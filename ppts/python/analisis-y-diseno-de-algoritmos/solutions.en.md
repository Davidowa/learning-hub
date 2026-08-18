# Solutions · Analysis and Design of Algorithms · COM101

Instructor copy. Every exercise carries the solution as it was run, the exact output it produced, the ten-point rubric, and the mistake that turns up most often while marking it. All the Python was executed with the course interpreter; the week 2 solutions are paper work and get checked against the trace. The exercises that read from the keyboard are shown as a full session, with what the student types on the same line as the prompt.

The data are the same all term: the origination floor at Financiera Altamar, its desks MC-01 to MC-04, the payroll loan at a policy rate of 18.00 % with a band of 17.50 to 18.50 %, and the `applications.csv` file of weeks 14 to 17.

---

## Week 01 · Course introduction and the bridge from Excel to Python

### 01.1 · Recognise

**Solution**

```text
W01 1240
7990
1331.6666666666667
W04
```

`approved[3]` is week W04, with 1510 applications. In the spreadsheet the value came from, it sits on row 5: row 1 holds the headers, row 2 holds W01, and from there Python's index 3 lands two rows below what intuition says.

`print(approved[6])` raises `IndexError`. The list holds six elements and the last valid index is 5.

**Output**

```text
W01 1240
7990
1331.6666666666667
W04
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines correct, average included and unrounded | 4 |
| Identifies `approved[3]` as W04 | 2 |
| Places the spreadsheet row counting the header | 2 |
| Explains the `IndexError` and names the last valid index | 2 |

**Most common mistake**

Answering `W03 1120` on the first line and calling `approved[3]` week W03. That is counting from one, and the giveaway is that every answer ends up shifted by exactly one position.

### 01.2 · Apply

**Solution**

```python
weeks = ["W01", "W02", "W03", "W04", "W05", "W06"]
approved = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(approved)
average = total / len(approved)
best_week = weeks[approved.index(max(approved))]
best_value = max(approved)
above_average = best_value - average

print(f"Applications this term: {total:,}")
print(f"Average per week:       {average:,.1f}")
print(f"Best week:              {best_week} with {best_value:,}")
print(f"Above the average:      {above_average:,.1f}")
```

**Output**

```text
Applications this term: 7,990
Average per week:       1,331.7
Best week:              W04 with 1,510
Above the average:      178.3
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four figures are correct | 4 |
| The best week comes out of `index` and `max`, not typed by hand | 3 |
| Thousands separator and one decimal where they belong | 2 |
| The labels let the report be read without the code | 1 |

**Most common mistake**

Writing `best_week = "W04"` because it already showed up in the previous output. The program gives the right answer and stops giving it the moment one value changes, which is exactly what happens in 01.3.

### 01.3 · Integrate

**Solution**

```python
weeks = ["W01", "W02", "W03", "W04", "W05", "W06"]
approved = [1240, 1385, 1320, 1510, 1295, 1440]

total = sum(approved)
average = total / len(approved)
best_week = weeks[approved.index(max(approved))]

reference = "00847"

print(f"Batch reference:        {reference}")
print(f"Applications this term: {total:,}")
print(f"Average per week:       {average:,.1f}")
print(f"Best week:              {best_week}")
```

Before the correction: 7,990 applications, 1,331.7 average, W04. After it: 8,190 applications, 1,365.0 average, W04. The best week does not change because W03 still sits below W04.

In a spreadsheet the change would have propagated on its own. In Python nothing is recalculated until the file gets run again, and that is the second of the four breaking points. The advantage shows up the other way round: the procedure is written down, so the same correction can be applied again three months from now and give exactly the same thing.

Captured with a number format, the reference shows as 847: leading zeros are not part of a numeric value and they vanish. That is the third of the four breaking points, the one about types. A batch reference is stored as text because it is an identifier. It never gets added up, it never gets averaged, and its shape is the only thing that lets anyone find it again in the system that issued it.

**Output**

```text
Batch reference:        00847
Applications this term: 8,190
Average per week:       1,365.0
Best week:              W04
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three new figures are correct and set against the old ones | 3 |
| Notices the best week does not change and says why | 2 |
| Names the recalculation breaking point and explains it | 2 |
| Explains that the reference captured as a number shows 847 | 2 |
| Explains why a reference is text | 1 |

**Most common mistake**

Claiming the best week is now W03 because that is the one that changed. The reasoning runs on the value that was touched instead of on the result, and comparing 1320 with 1510 settles it.

---

## Week 02 · Unit 1 · Algorithm design

### 02.1 · Recognise

**Solution**

Application at 18.80 %. `18.80 > 18.50` is evaluated, it holds, and the verdict lands on «Overpriced outside policy». The other two branches are never read.

Application at 17.40 %. `17.40 > 18.50` is evaluated and fails. `17.40 < 17.50` is evaluated, it holds, and the verdict lands on «Discounted outside policy». The closing ELSE is never read.

Application at exactly 18.50 %. `18.50 > 18.50` is evaluated and fails, because the operator asks for strictly greater. `18.50 < 17.50` also fails. It drops into the ELSE and the verdict is «Within policy». The application sits right on the limit and passes.

With the second version, the 18.80 % application enters through `18.80 >= 17.50`, which holds, and comes out as «Within policy». The overpricing branch is unreachable: any rate above 18.50 is also greater than or equal to 17.50, so the first condition takes it every time.

That second version is finite, precise, defined, has input and has output. It satisfies all five properties and still approves prices that break the policy. An algorithm that is correct in its form can be solving the wrong problem, which is why the order of the conditions gets reviewed with cases and not by eye.

**Output**

```text
Application  Condition evaluated   Result      Verdict
18.80 %      18.80 > 18.50         Holds       Overpriced outside policy
17.40 %      17.40 > 18.50         Fails       -
17.40 %      17.40 < 17.50         Holds       Discounted outside policy
18.50 %      18.50 > 18.50         Fails       -
18.50 %      18.50 < 17.50         Fails       Within policy

Second version
18.80 %      18.80 >= 17.50        Holds       Within policy
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three traces correct, with the conditions never read marked | 4 |
| The 18.50 case comes out within policy and the reason is given | 2 |
| Traces the second version and spots the unreachable overpricing branch | 2 |
| Argues that it satisfies the five properties and is still wrong | 2 |

**Most common mistake**

Saying the 18.50 application is flagged outside because it «reached the limit». The limit gets confused with the exception zone, and it shows in the student reading `>` as if it were `>=`.

### 02.2 · Apply

**Solution**

```text
START
    READ file_complete, past_due, bureau_score

    IF file_complete = FALSE THEN
        WRITE "On hold: incomplete file"
    ELSE IF past_due > 0 THEN
        WRITE "On hold: past-due balance"
    ELSE IF bureau_score < 620 THEN
        WRITE "On hold: score too low"
    ELSE
        WRITE "Disbursement released"

    END
```

The flowchart carries an oval for the start, a parallelogram reading the three values, three diamonds chained through their NO exit, four parallelograms for writing, and an oval for the end. Each diamond has both exits labelled.

The order matters: the file is checked first because with no documents there is nothing to consult, and an application with no proof of income is not disbursed however good the score is.

**Output**

```text
Case 1: complete file, no past-due balance, score 688
  Diamond 1: file_complete = FALSE?      No, carry on
  Diamond 2: past_due > 0?               No, carry on
  Diamond 3: 688 < 620?                  No, carry on
  Output: Disbursement released

Case 2: complete file, no past-due balance, score 601
  Diamond 1: file_complete = FALSE?      No, carry on
  Diamond 2: past_due > 0?               No, carry on
  Diamond 3: 601 < 620?                  Yes
  Output: On hold: score too low
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The pseudocode checks the three conditions in the order asked for | 3 |
| Every failure names which condition failed, not a generic message | 2 |
| The flowchart uses the four symbols for what they mean | 2 |
| The diamonds have both exits labelled and both lead somewhere | 1 |
| Both traces are correct | 2 |

**Most common mistake**

A single diamond holding all three conditions and one «application rejected» message. The algorithm decides correctly and is useless, because the desk officer does not know what to ask the client for.

### 02.3 · Integrate

**Solution**

The two-person test: two analysts holding the same application placed at 18.60 % can decide differently, because «came out too expensive» depends on who is looking. The property that breaks is precision, and with it the property of being defined, because the same input stops producing the same result.

```text
START
    READ rate

    IF rate > 18.50 THEN
        destination = "Pricing committee"
    ELSE IF rate < 17.50 THEN
        destination = "Cancel on margin"
    ELSE
        destination = "Disburse"

    WRITE destination
END
```

Input: the rate granted to an application, as an annual percentage. Output: where that application goes, one text value out of three.

Edge case the first version did not cover: a rate of 0.00 %, which happens when the field is left empty in the system and arrives as zero. With the algorithm above that application comes out as cancel on margin, and that is not true: the application has not been priced at all. It gets covered with a branch at the top that rejects rates at or below zero and asks for the value to be captured again.

**Output**

```text
Original instruction     Two analysts, one 18.60 %, two destinations
Property broken          Precise, and with it the property of being defined

Trace of three applications
18.60 %   18.60 > 18.50    Holds     Pricing committee
17.20 %   17.20 > 18.50    Fails
17.20 %   17.20 < 17.50    Holds     Cancel on margin
18.00 %   both fail                  Disburse

Edge case added
 0.00 %   rate <= 0        Holds     Capture again
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Runs the two-person test on a concrete value | 2 |
| Names the property that breaks and justifies it | 2 |
| The algorithm has the three outputs and uses the right band | 3 |
| Input and output written down | 1 |
| The edge case broke the earlier version and the change is explained | 2 |

**Most common mistake**

Rewriting the instruction with more words and no numbers. «If the rate came out well above policy» still depends on who reads it, and the giveaway is that neither 17.50 nor 18.50 appears anywhere on the page.

---

## Week 03 · Units 1 and 2 · Paradigms and an introduction to programming

### 03.1 · Recognise

**Solution**

The trace: after the first line `applications` holds 1240, after the second 1325 and after the third 2650. The program prints 2650. The equals sign does not compare, it stores, and each line overwrites what the one before it left.

Fragment A: does not run. `NameError`, because `Sum` with a capital letter does not exist. It breaks the rule about capitals.

Fragment B: does not run. `SyntaxError` for an unterminated string, on line 2. It breaks the rule about quotation marks.

Fragment C: does not run. `SyntaxError` saying the bracket was never closed, and it complains on line 2 even though the problem sits right there at the end of the file. It breaks the rule about brackets.

Fragment D: does not run. `NameError`, because `Print` with a capital letter is not `print`. It breaks the rule about capitals.

**Output**

```text
2650

A  NameError: name 'Sum' is not defined. Did you mean: 'sum'?
B  SyntaxError: unterminated string literal (detected at line 2)
C  SyntaxError: '(' was never closed
D  NameError: name 'Print' is not defined. Did you mean: 'print'?
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The trace of the three lines with their intermediate values | 3 |
| The four fragments classified as running or not | 2 |
| The right kind of error on all four | 3 |
| Names the rule broken in each one | 2 |

**Most common mistake**

Answering 250 on the trace, multiplying before adding. The program gets read as a formula with precedence, when it is three assignments running in order.

### 03.2 · Apply

**Solution**

```python
# Amounts authorised by desk MC-01 on 8 January, in pesos.
from statistics import mean

amounts = [96500, 148200, 73400, 151100, 118900]

average = mean(amounts)
largest = max(amounts)

print("Loans:", len(amounts))
print("Average amount:", average)
print("Largest amount:", largest)
```

The table of the three deliberate breaks:

| What was broken | Message |
|---|---|
| Closing bracket | `SyntaxError: '(' was never closed`, line 9 |
| `print` with a capital | `NameError: name 'Print' is not defined. Did you mean: 'print'?`, line 9 |
| Quotation mark deleted | `SyntaxError: unterminated string literal (detected at line 9)` |

**Output**

```text
Loans: 5
Average amount: 117620
Largest amount: 151100
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The program runs and the three figures are correct | 3 |
| Carries the comment, the import and labels on the `print` calls | 2 |
| The three error messages are transcribed in full | 3 |
| Reports the line each error pointed at | 2 |

**Most common mistake**

Handing in the messages paraphrased, along the lines of «it flagged a syntax error». That drops exactly the part that is useful, which is the last word of the message and the line number.

### 03.3 · Integrate

**Solution**

```python
# Translation of the week 2 pricing verdict pseudocode.
rate = 18.50

if rate > 18.50:
    verdict = "Overpriced outside policy"
elif rate < 17.50:
    verdict = "Discounted outside policy"
else:
    verdict = "Within policy"

print("Rate granted:", rate, "%")
print("Verdict:", verdict)
```

The 18.00 run prints `18.0` because the trailing zero is not part of the value. The number stored is eighteen, and how many decimals show is a presentation decision settled with formatting, not with the data.

If the first two branches are swapped, an application at 18.80 % still comes out overpriced, because `18.80 < 17.50` fails and the second branch does get evaluated. The swap that really breaks the algorithm is the one from week 2, where the within-policy branch goes first.

**Output**

```text
Rate granted: 18.5 %
Verdict: Within policy

Rate granted: 17.4 %
Verdict: Discounted outside policy

Rate granted: 18.0 %
Verdict: Within policy
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The translation keeps the order of the three branches | 3 |
| The three runs are pasted in full and are correct | 3 |
| Explains why it prints `18.0` | 2 |
| Answers correctly about swapping the branches | 2 |

**Most common mistake**

Writing three loose `if` statements instead of `if`, `elif` and `else`. With these three conditions the result matches, and the student never notices three comparisons were evaluated where one would have done.

---

## Week 04 · Unit 3 · Data, data types and primitive operations

### 04.1 · Recognise

**Solution**

```text
51.666666666666664
51
16
1850
68
True
False
0.15000000000000002
```

The second line says how many review bundles fill up completely: 51. The third says how many applications are left loose once those are filled: 16.

The sixth and seventh lines compare decimals that come out exact on paper and give opposite results. The reason is that 0.05 cannot be represented exactly in binary. In one case the rounding errors cancel and the equality holds; in the other they do not. That is why the pricing band is written with both limits as constants and never worked out by adding and subtracting inside a condition.

**Output**

```text
51.666666666666664
51
16
1850
68
True
False
0.15000000000000002
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight lines correct, with the first one unrounded | 4 |
| Reads the integer division and the remainder as bundles and applications | 2 |
| Tells text concatenation apart from integer addition | 2 |
| Explains why two similar comparisons give opposite results | 2 |

**Most common mistake**

Answering `True` on the seventh line because 0.05 times 3 is 0.15 on paper. It is the same correct reasoning that produces a band condition failing once in every thousand applications.

### 04.2 · Apply

**Solution**

```python
lender = "Altamar"
desk = "MC-01"
date = "2026-01-08"
applications = 1240
rejected = 37
analyst_hours = 86.4
desk_active = True
last_incident = None

reject_rate = rejected / applications
hours_per_application = analyst_hours / applications

print(f"{lender} {desk} {date}")
print(f"Reject rate:           {round(reject_rate * 100, 2)} %")
print(f"Hours per application: {round(hours_per_application, 4)} h")
print(type(applications), type(analyst_hours))
print(type(desk), type(desk_active), type(last_incident))
```

The date is stored as text because there is nothing to do with it yet. `last_incident` holds `None`, which is absence of data, not zero: zero minutes of system downtime is a measurement, `None` means nobody logged anything.

**Output**

```text
Altamar MC-01 2026-01-08
Reject rate:           2.98 %
Hours per application: 0.0697 h
<class 'int'> <class 'float'>
<class 'str'> <class 'bool'> <class 'NoneType'>
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight variables each with the type they deserve | 3 |
| `last_incident` on `None` and not on zero, with the explanation | 2 |
| Both metrics correct and rounded | 3 |
| The names say what they hold and none is a single letter | 2 |

**Most common mistake**

Setting `last_incident = 0`. The program runs and the average incident duration comes out wrong the moment anybody works it out, because a batch with no incidents joins the average as an incident of zero minutes.

### 04.3 · Integrate

**Solution**

```python
applications = 1240
rejected = 37
analyst_hours = 86.4
per_bundle = 24

per_application_wrong = analyst_hours / applications - rejected
per_application_right = analyst_hours / (applications - rejected)

print(f"Without brackets: {round(per_application_wrong, 4)}")
print(f"With brackets:    {round(per_application_right, 4)} h per approved application")

approved = applications - rejected
full_bundles = approved // per_bundle
loose = approved % per_bundle

print(f"Approved applications: {approved}")
print(f"Full bundles: {full_bundles}, loose applications: {loose}")

reference = "00847"

print(f"Reference: {reference}  integer: {int(reference)}  back again: {str(int(reference))}")
```

The first version shares the hours across every application and then subtracts 37 from the result, that is, it subtracts applications from a time per application. It goes negative because it is taking files away from hours. The second shares the batch hours across the 1203 applications that were actually approved, which is the question that was asked.

The reference loses its leading zeros the moment it becomes an integer, and never gets them back on the way to text. What was lost is not the number, it is the identifier.

**Output**

```text
Without brackets: -36.9303
With brackets:    0.0718 h per approved application
Approved applications: 1203
Full bundles: 50, loose applications: 3
Reference: 00847  integer: 847  back again: 847
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both expressions written out with both results | 3 |
| Explains what each one works out, not just which is right | 2 |
| Full bundles and loose applications correct | 3 |
| Reports the lost zeros on the reference and what that means | 2 |

**Most common mistake**

Working out the bundles from the 1240 applications received instead of the 1203 approved. The number lands close to the right one, and that is why nobody checks it until files are missing from the physical archive.

---

## Week 05 · Unit 4 · Statements, input and output

### 05.1 · Recognise

**Solution**

```text
Applications: 1,240
Hours: 86.40 h
Reject: 3.0%
Reject: 2.98%
MC-01         1240
Raw rate: 0.029838709677419355
Hours: {hours:.2f} h
```

The third and fourth lines show the same value with different numbers of decimals: the one-decimal version rounds 2.98 up to 3.0, and in an origination report that difference decides whether the desk lands inside or outside a 3 % target.

The last line is missing the `f` before the quotation mark. That is not an error: the string prints exactly as written, braces and format code included, and the program carries on as if nothing happened.

**Output**

```text
Applications: 1,240
Hours: 86.40 h
Reject: 3.0%
Reject: 2.98%
MC-01         1240
Raw rate: 0.029838709677419355
Hours: {hours:.2f} h
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven lines correct, commas and spaces included | 5 |
| Explains the rounding of 2.98 to 3.0 and why it matters | 2 |
| Spots the missing `f` and says it raises no error | 3 |

**Most common mistake**

Writing `Reject: 0.0%` on the third line. The percentage code already multiplies by a hundred, and the tell is that the same student also writes `2.98` as though it were the raw value.

### 05.2 · Apply

**Solution**

```python
desk = input("Desk: ")
applications = int(input("Applications received: "))
rejected = int(input("Applications rejected: "))
hours = float(input("Analyst-hours in the batch: "))

rate = rejected / applications
per_application = hours / applications

print(f"Desk:                  {desk}")
print(f"Applications:          {applications:,}")
print(f"Rejected:              {rejected:,}")
print(f"Reject rate:           {rate:.2%}")
print(f"Hours per application: {per_application:.4f} h")
```

**Output**

```text
Desk: MC-01
Applications received: 1240
Applications rejected: 37
Analyst-hours in the batch: 86.4
Desk:                  MC-01
Applications:          1,240
Rejected:              37
Reject rate:           2.98%
Hours per application: 0.0697 h
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four `input` calls carry a prompt and are converted where they should be | 3 |
| Both metrics are correct | 3 |
| Thousands, percentage and four-decimal formats applied | 2 |
| The session is handed in complete, with what was typed | 2 |

**Most common mistake**

Converting after operating, with `int(applications / rejected)` instead of converting each `input`. Dividing two strings blows up first, and when it does not it is because the student concatenated without noticing.

### 05.3 · Integrate

**Solution**

```python
SHIFT_SECONDS = 28800

desk = input("Desk: ")
applications = int(input("Applications received: "))
rejected = int(input("Applications rejected: "))
hours = float(input("Analyst-hours in the batch: "))

approved = applications - rejected
rate = rejected / applications
seconds = SHIFT_SECONDS / applications
minutes_per_approved = hours * 60 / approved

print(f"Batch report {desk}")
print(f"{'Applications received':<22}{applications:>10,}")
print(f"{'Applications approved':<22}{approved:>10,}")
print(f"{'Reject rate':<22}{rate:>10.2%}")
print(f"{'Time per application':<22}{seconds:>10.2f} s")
print(f"{'Minutes per approved':<22}{minutes_per_approved:>10.2f} min")
```

Time per application is worked out from the applications received, because the desk spent shift time on the ones it ended up rejecting too. The analysis minutes are shared only across the approved ones, because that is a cost to be charged to what actually got placed. Two different denominators in the same report, each with its reason.

**Output**

```text
Desk: MC-03
Applications received: 1512
Applications rejected: 68
Analyst-hours in the batch: 112.8
Batch report MC-03
Applications received      1,512
Applications approved      1,444
Reject rate                4.50%
Time per application       19.05 s
Minutes per approved        4.69 min
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five figures correct | 4 |
| The shift constant has a name and sits at the top | 1 |
| The five lines aligned to the widths asked for | 2 |
| Every figure carries its unit | 1 |
| Justifies the two different denominators | 2 |

**Most common mistake**

Working out the time per application from the approved ones. It gives 19.94 seconds and sounds reasonable, but the desk did not stop working on the 68 applications it ended up turning down.

---

## Week 06 · Unit 4.4 · Selection structures

### 06.1 · Recognise

**Solution**

The first program prints `18.5 Within policy`. The condition asks for strictly greater, and 18.50 is not greater than 18.50, so the application drops into the `else`. That is the correct behaviour: the upper limit is part of the authorised band.

The second program prints `18.8 Within policy`, and that is wrong. The first condition asks whether the rate is greater than or equal to the lower limit, and an application at 18.80 satisfies it. Since the first branch that holds is the one that runs, the overpricing branch is never reached: any value above 18.50 is also greater than or equal to 17.50.

The correct order runs from the most demanding to the least: overpricing first, then the discount, and within policy last as the remaining case.

**Output**

```text
18.5 Within policy
18.8 Within policy
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both outputs correct | 4 |
| Explains why 18.50 stays inside with the strict operator | 2 |
| Spots the unreachable overpricing branch and says why | 2 |
| Writes the correct order of the three conditions | 2 |

**Most common mistake**

Saying the second program raises an error because two conditions hold. There is no error: the first one runs and the rest are never read, which is exactly what makes it dangerous.

### 06.2 · Apply

**Solution**

```python
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50

application = input("Application reference: ")
rate = float(input("Rate granted in %: "))

if rate > UPPER_LIMIT:
    verdict = "Overpriced outside policy"
elif rate < LOWER_LIMIT:
    verdict = "Discounted outside policy"
else:
    verdict = "Within policy"

print(f"Application {application}: {rate:.2f} % -> {verdict}")
```

**Output**

```text
Application reference: APP-1003
Rate granted in %: 18.60
Application APP-1003: 18.60 % -> Overpriced outside policy

Application reference: APP-1005
Rate granted in %: 17.40
Application APP-1005: 17.40 % -> Discounted outside policy

Application reference: APP-1008
Rate granted in %: 18.50
Application APP-1008: 18.50 % -> Within policy

Application reference: APP-1013
Rate granted in %: 17.50
Application APP-1013: 17.50 % -> Within policy

Application reference: APP-1004
Rate granted in %: 18.00
Application APP-1004: 18.00 % -> Within policy
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three verdicts correct across the five runs | 4 |
| Both limits are named constants, not loose numbers | 2 |
| The 18.50 and 17.50 applications come out within policy | 2 |
| The reference is read as text and the rate converted to a decimal | 2 |

**Most common mistake**

Using `>=` in the first condition. Applications at 18.50 get flagged as exceptions, the desk sends roughly one in ten to committee, and the program looks perfectly correct.

### 06.3 · Integrate

**Solution**

```python
POLICY_RATE = 18.00
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50
COMMITTEE_CEILING = 19.50
MANAGEMENT_FLOOR = 16.50

rate = float(input("Rate granted in %: "))

if rate <= 0 or rate > 60:
    verdict = "Invalid value: check the capture"
elif rate > COMMITTEE_CEILING:
    verdict = "Cancelled on overpricing"
elif rate > UPPER_LIMIT:
    verdict = "Overpriced: pricing committee approves"
elif rate >= LOWER_LIMIT:
    verdict = "Within policy"
elif rate >= MANAGEMENT_FLOOR:
    verdict = "Discounted: management approves"
else:
    verdict = "Cancelled on margin"

print(f"{rate:>7.2f} %  {verdict}")
```

The check goes first because a rate of -3.00 % is not an aggressive discount, it is a badly captured field, and classifying it as a cancellation on margin would hide the system failure.

Table of boundaries:

| Boundary | Exact value | Verdict | Why that operator |
|---|---|---|---|
| Committee ceiling | 19.50 | Committee | `>` leaves 19.50 on the side the committee can still authorise |
| Upper limit | 18.50 | Within policy | `>` keeps the limit inside the band, as the policy says |
| Lower limit | 17.50 | Within policy | `>=` keeps the limit inside the band |
| Management floor | 16.50 | Discount, authorisable | `>=` leaves 16.50 on the side management can sign |
| Check | 0 and 60 | Invalid | `<=` on zero because a rate of zero is an empty field |

**Output**

```text
Rate granted in %: 20.00
  20.00 %  Cancelled on overpricing
Rate granted in %: 19.50
  19.50 %  Overpriced: pricing committee approves
Rate granted in %: 18.60
  18.60 %  Overpriced: pricing committee approves
Rate granted in %: 18.50
  18.50 %  Within policy
Rate granted in %: 18.00
  18.00 %  Within policy
Rate granted in %: 17.50
  17.50 %  Within policy
Rate granted in %: 17.20
  17.20 %  Discounted: management approves
Rate granted in %: 16.50
  16.50 %  Discounted: management approves
Rate granted in %: 16.20
  16.20 %  Cancelled on margin
Rate granted in %: -3.00
  -3.00 %  Invalid value: check the capture
Rate granted in %: 75.00
  75.00 %  Invalid value: check the capture
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five categories are mutually exclusive and in the right order | 3 |
| The check runs before classifying and catches both impossible cases | 2 |
| The eleven runs are correct | 2 |
| The five boundaries are named constants | 1 |
| The table documents the verdict on the exact value of each boundary | 2 |

**Most common mistake**

Putting the check at the end, after the `else`. It never runs, because by then -3.00 has already come out classified as a cancellation on margin and the program flags nothing.

---

## Week 07 · Unit 4.4 · Nested selection and logical operators

### 07.1 · Recognise

**Solution**

```text
Critical desk
True
False
Not enough data
True
```

Line 1. The condition is `desk == "MC-01" or "MC-03"`. Python evaluates the comparison, which is false, and then evaluates the string `"MC-03"`, which counts as true because it is not empty. The whole condition is always true, MC-04 included. The correct form is `desk in ["MC-01", "MC-03"]`.

Line 2. Both lists hold the same values in the same order, so they are equal.

Line 3. They are two separate lists in memory, so `is` gives false. The double equals compares content, `is` compares identity.

Line 4. With zero applications, `applications > 0` is false and Python never evaluates the division. That is short-circuit evaluation on the `and`, and it is what avoids the `ZeroDivisionError`. With `or`, a false first condition forces the second one to be evaluated, and that is where it blows up.

Line 5. `last_incident is None` is the correct way to ask about the absence of a value.

**Output**

```text
Critical desk
True
False
Not enough data
True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines correct | 4 |
| Explains why the first condition is always true and fixes it with `in` | 2 |
| Tells `==` from `is` with the identity argument | 2 |
| Explains short-circuiting and why `or` would blow up | 2 |

**Most common mistake**

Answering «Normal desk» on the first line by reasoning about what the code meant to say. What the author intended gets read instead of what Python evaluates, and the tell is that the same student sees nothing odd about MC-04 either.

### 07.2 · Apply

**Solution**

```python
CRITICAL = ["MC-01", "MC-03"]
MAX_REJECT_RATE = 0.03
MIN_APPLICATIONS = 500

desk = input("Desk: ")
applications = int(input("Applications in the batch: "))
rejected = int(input("Applications rejected: "))
under_audit = input("Under audit (yes/no): ") == "yes"

rate = rejected / applications

if not under_audit and applications >= MIN_APPLICATIONS and rate <= MAX_REJECT_RATE:
    decision = "Batch released"
elif desk in CRITICAL:
    decision = "Hold: critical desk missed the rule"
else:
    decision = "Hold for a file-by-file review"

print(f"{desk} {applications:>5} applications  reject {rate:.2%}  -> {decision}")
```

**Output**

```text
Desk: MC-01
Applications in the batch: 1240
Applications rejected: 37
Under audit (yes/no): no
MC-01  1240 applications  reject 2.98%  -> Batch released

Desk: MC-03
Applications in the batch: 1512
Applications rejected: 68
Under audit (yes/no): no
MC-03  1512 applications  reject 4.50%  -> Hold: critical desk missed the rule

Desk: MC-04
Applications in the batch: 760
Applications rejected: 9
Under audit (yes/no): no
MC-04   760 applications  reject 1.18%  -> Batch released

Desk: MC-02
Applications in the batch: 420
Applications rejected: 5
Under audit (yes/no): no
MC-02   420 applications  reject 1.19%  -> Hold for a file-by-file review

Desk: MC-01
Applications in the batch: 1240
Applications rejected: 37
Under audit (yes/no): yes
MC-01  1240 applications  reject 2.98%  -> Hold: critical desk missed the rule
```

The fourth case is the one that teaches something: MC-02 sits at a 1.19 % reject rate, better than MC-01, and is still held. A batch of 420 applications does not reach the minimum, and without volume the rate means nothing.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five decisions correct | 4 |
| The release rule uses `and` across the three conditions | 2 |
| Membership is asked with `in` over the list of critical desks | 2 |
| The three thresholds are named constants | 1 |
| Comments on the small batch with the good rate | 1 |

**Most common mistake**

Writing `desk in "MC-01"` without the brackets. The condition turns into asking whether one string is contained in the other, works by accident with MC-01, and fails silently with anything else.

### 07.3 · Integrate

**Solution**

```python
DELINQUENCY_LIMIT = 3.0
OVERPRICE_LIMIT = 0.50

delinquency = float(input("Desk portfolio delinquency in %: "))
overprice = float(input("Average overprice in points: "))

if delinquency > DELINQUENCY_LIMIT:
    if overprice > OVERPRICE_LIMIT:
        nested = "Block the desk"
    else:
        nested = "Keep placing"
else:
    if overprice > OVERPRICE_LIMIT:
        nested = "Keep placing"
    else:
        nested = "Keep placing"

if delinquency > DELINQUENCY_LIMIT and overprice > OVERPRICE_LIMIT:
    combined = "Block the desk"
else:
    combined = "Keep placing"

print(f"{delinquency:>5.1f} %  {overprice:>4.2f} pts  "
      f"nested: {nested:<16} combined: {combined:<16} "
      f"same: {nested == combined}")
```

This nesting could be collapsed because the two inner branches of the outer `else` do exactly the same thing. When that happens, the second question adds nothing along that path, and the four branches come down to one condition joined with `and`.

A case from the same floor where the nesting does not collapse: if the desk is under audit, its overprice means nothing and the action is to wait for the ruling; if it is not, the overprice decides between raising the target, holding it and blocking. There the inner branches do three different things and the outer branch does a fourth, so the nesting earns something real.

**Output**

```text
Desk portfolio delinquency in %: 4.2
Average overprice in points: 0.80
  4.2 %  0.80 pts  nested: Block the desk   combined: Block the desk   same: True

Desk portfolio delinquency in %: 4.2
Average overprice in points: 0.30
  4.2 %  0.30 pts  nested: Keep placing     combined: Keep placing     same: True

Desk portfolio delinquency in %: 2.4
Average overprice in points: 0.80
  2.4 %  0.80 pts  nested: Keep placing     combined: Keep placing     same: True

Desk portfolio delinquency in %: 2.4
Average overprice in points: 0.30
  2.4 %  0.30 pts  nested: Keep placing     combined: Keep placing     same: True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The collapsed version is correct and uses a single condition | 3 |
| The four cases agree and the check is handed in | 3 |
| Explains that identical inner branches are the signal | 2 |
| Describes a case where the nesting is justified | 2 |

**Most common mistake**

Collapsing with `or` instead of `and`. The four cases stop agreeing on the second and the third, and the student who never ran the check hands both versions in as equivalent.

---

## Week 08 · Unit 4.5 · Repetition · First midterm

### 08.1 · Recognise

**Solution**

The `for` prints six lines: 12, 18, 24, 30, 36 and 42. A `range` with step 6 starts at 12 and stops before 48, so 48 never appears. The last term that fits is 42.

The `while` prints `7 -2500.0`. The budget starts at 50,000 pesos and each week takes 7,500, so after six weeks 5,000 is left. The condition asks whether more than zero remains, and 5,000 satisfies it, so it enters a seventh pass and subtracts 7,500 again. The counter ends at 7 and the balance at -2,500.

Full weeks the budget really covers: six. The seventh started and ran out of funds halfway, and the negative number is the evidence.

If the line that subtracts the spend is deleted, the condition never changes and the loop never ends. It has to be stopped with Control C.

**Output**

```text
12
18
24
30
36
42
7 -2500.0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines of the `for` and the count | 3 |
| The `while` output with the negative balance | 3 |
| Tells the 7 printed apart from the 6 real full weeks | 2 |
| Identifies the infinite loop if the subtraction is deleted | 2 |

**Most common mistake**

Answering that the budget covers 7 weeks because that is what the program prints. The number is worked out correctly and answers a different question, and the -2,500 sitting next to it is exactly the clue nobody reads.

### 08.2 · Apply

**Solution**

```python
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
applications = [1240, 984, 1512, 760]
rejected = [37, 12, 68, 9]
hours = [86.4, 61.5, 112.8, 48.2]

total_applications = 0
total_rejected = 0
total_hours = 0.0

print(f"{'Desk':<10}{'Applications':>14}{'Reject':>10}{'h/app':>10}")

for i in range(len(desks)):
    rate = rejected[i] / applications[i]
    per_application = hours[i] / applications[i]

    total_applications += applications[i]
    total_rejected += rejected[i]
    total_hours += hours[i]

    print(f"{desks[i]:<10}{applications[i]:>14,}{rate:>10.2%}{per_application:>10.4f}")

floor_rate = total_rejected / total_applications
floor_hours = total_hours / total_applications

print(f"{'ALTAMAR':<10}{total_applications:>14,}{floor_rate:>10.2%}{floor_hours:>10.4f}")
```

The floor row divides the sum of rejections by the sum of applications. Averaging the four rates would give 2.47 %, which weights MC-04 with its 760 applications the same as MC-03 with 1512, and that is not what the floor produced.

**Output**

```text
Desk        Applications    Reject     h/app
MC-01              1,240     2.98%    0.0697
MC-02                984     1.22%    0.0625
MC-03              1,512     4.50%    0.0746
MC-04                760     1.18%    0.0634
ALTAMAR            4,496     2.80%    0.0687
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four rows and their three figures correct | 3 |
| The floor row divides sums instead of averaging rates | 3 |
| A single pass, with the three accumulators outside the loop | 2 |
| The loop works the same if a fifth desk is added | 1 |
| Output aligned in columns | 1 |

**Most common mistake**

Working out the floor rate as the average of the four. It comes to 2.47 % instead of 2.80 %, it looks reasonable, and it understates the rejections exactly where the volume is.

### 08.3 · Integrate

**Solution**

```python
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50

applications = ["APP-1001", "APP-1002", "APP-1003", "APP-1004",
                "APP-1005", "APP-1006", "APP-1007", "APP-1008",
                "APP-1009", "APP-1010", "APP-1011", "APP-1012"]
rates = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

outside = 0
running = 0.0

for i in range(len(applications)):
    rate = rates[i]
    running += rate

    if rate > UPPER_LIMIT:
        verdict = "Overpriced outside policy"
        outside += 1
    elif rate < LOWER_LIMIT:
        verdict = "Discounted outside policy"
        outside += 1
    else:
        verdict = "Within policy"

    print(f"{applications[i]:<10}{rate:>7.2f}  {verdict}")

average = running / len(rates)
share = outside / len(rates)

print(f"{'Average':<10}{average:>7.4f} %")
print(f"Outside policy: {outside} of {len(rates)} ({share:.1%})")
```

Application APP-1008 was placed at 18.50 %, which is exactly the upper limit, and the limit is part of the band. With `>=` in the first condition 4 applications would come out outside instead of 3, and the share of the batch would jump from 25.0 % to 33.3 % without a single application changing price.

**Output**

```text
APP-1001    18.10  Within policy
APP-1002    17.80  Within policy
APP-1003    18.60  Overpriced outside policy
APP-1004    18.00  Within policy
APP-1005    17.40  Discounted outside policy
APP-1006    18.30  Within policy
APP-1007    17.90  Within policy
APP-1008    18.50  Within policy
APP-1009    17.60  Within policy
APP-1010    18.20  Within policy
APP-1011    18.80  Overpriced outside policy
APP-1012    17.70  Within policy
Average   18.0750 %
Outside policy: 3 of 12 (25.0%)
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The twelve verdicts correct | 3 |
| Average to four decimals and the outside-policy count | 3 |
| The accumulator and the counter are declared before the loop | 2 |
| Explains the APP-1008 case and the effect of switching to `>=` | 2 |

**Most common mistake**

Declaring `running = 0.0` inside the `for`. It ends up holding 17.70, the average comes out at 1.4750 %, and the giveaway is that no payroll loan is ever placed at under two points.

---

## Week 09 · Unit 4.5 · Accumulators, flags and nested loops

### 09.1 · Recognise

**Solution**

The first program prints `48.2`. The expected result was 308.9, the sum of the four workloads. The line `total = 0.0` sits inside the loop, so every pass wipes what was accumulated and only the last value survives. That one line is the only thing to move, and it goes before the `for`.

The second program prints `First out of control: MC-03`. The trace of the four passes:

| i | Desk | Applications | What happens |
|---|---|---|---|
| 0 | MC-01 | 1240 | Passes the filter. 2.98 % does not go over 3 %, carry on |
| 1 | MC-02 | 984 | Fewer than 1000 applications, the `continue` skips it |
| 2 | MC-03 | 1512 | Passes the filter. 4.50 % does go over, prints and leaves with `break` |
| 3 | MC-04 | 760 | Never evaluated, the `break` already left the loop |

The `else` on the `for` does not run because the loop left through `break`. It would run if no desk with at least 1000 applications went over 3 %, for instance if MC-03 had closed the batch with 40 rejections instead of 68.

**Output**

```text
48.2
First out of control: MC-03
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both outputs correct | 3 |
| Identifies the misplaced line and says where it goes | 2 |
| The trace of the four passes with the `continue` and the `break` | 3 |
| Explains when the `else` on the `for` would run | 2 |

**Most common mistake**

Answering 308.9 on the first program. The intention of the code gets read instead of its indentation, and it is exactly the mistake that produces wrong totals nobody checks.

### 09.2 · Apply

**Solution**

```python
RATE_TARGET = 0.03
HOURS_TARGET = 0.070

desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
applications = [1240, 984, 1512, 760]
rejected = [37, 12, 68, 9]
hours = [86.4, 61.5, 112.8, 48.2]

total_hours = 0.0
off_target = 0
has_slow_desk = False

for i in range(len(desks)):
    total_hours += hours[i]

    if rejected[i] / applications[i] > RATE_TARGET:
        off_target += 1

    if hours[i] / applications[i] > HOURS_TARGET:
        has_slow_desk = True

print(f"Analyst-hours in the batch: {total_hours:,.1f} h")
print(f"Desks off target:           {off_target}")
print(f"Any desk over 0.070 h:      {has_slow_desk}")
```

The second question counts cases, not magnitudes: adding the rates up would give a number with no meaning. The first adds magnitudes: counting desks says nothing about how many analyst-hours were paid for. The flag answers whether at least one exists, and for that there is no need to count or to add.

**Output**

```text
Analyst-hours in the batch: 308.9 h
Desks off target:           1
Any desk over 0.070 h:      True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three answers correct | 3 |
| The three variables declared before the loop | 2 |
| A single pass for the three questions | 2 |
| Both targets are named constants | 1 |
| Explains the difference between counting and adding | 2 |

**Most common mistake**

Writing the flag as `has_slow_desk = hours[i] / applications[i] > HOURS_TARGET` with no `if`. The variable gets overwritten on every pass and ends up reflecting only the last desk, which on this data comes out false.

### 09.3 · Integrate

**Solution**

```python
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
applications_per_hour = [155, 123, 189, 95]
shifts = ["T1", "T2", "T3"]
hours = [8, 8, 6]

total_capacity = 0
high_combinations = 0

for i in range(len(desks)):
    for j in range(len(shifts)):
        projection = applications_per_hour[i] * hours[j]
        total_capacity += projection

        if projection > 1000:
            high_combinations += 1

        print(f"{desks[i]:<8}{shifts[j]:<5}{projection:>7,}")

print(f"{'TOTAL':<13}{total_capacity:>7,}")
print(f"Combinations above 1000 applications: {high_combinations}")
```

Four desks by three shifts are twelve rows, and that count gets written down before the program runs. With 40 desks and 3 shifts it would be 120 passes, which is still nothing. The trouble shows up when both loops walk long lists: 1000 by 1000 is a million passes, and that is where nesting stops being free.

**Output**

```text
MC-01   T1     1,240
MC-01   T2     1,240
MC-01   T3       930
MC-02   T1       984
MC-02   T2       984
MC-02   T3       738
MC-03   T1     1,512
MC-03   T2     1,512
MC-03   T3     1,134
MC-04   T1       760
MC-04   T2       760
MC-04   T3       570
TOTAL         12,364
Combinations above 1000 applications: 5
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The twelve rows with the right projection | 3 |
| The total and the count of high combinations | 3 |
| The two loop variables are named differently and say what they walk | 2 |
| Predicts the twelve rows before running the program | 1 |
| Answers how the passes grow with an example | 1 |

**Most common mistake**

Using `i` in both loops. The inner one overwrites the outer, repeated rows of the last desk come out, and the total falls apart without Python flagging anything.

---

## Week 10 · Unit 5 · User-defined functions

### 10.1 · Recognise

**Solution**

The first line prints `None`. The function works out the division and does not return it, so it hands back the value Python returns by default when there is no `return`. The second prints `4.180645161290323`, which really are the analysis minutes per application. The third raises `NameError`.

`reject_rate` is missing its `return`. The error does not show up inside the function because nothing there is written wrong: it shows up further down, the moment somebody tries to multiply, compare or format that `None`.

The third line fails because `per_unit` was born inside the function and disappeared when the function ended. Outside it, that name does not exist.

If the second function had `print(per_unit)` instead of `return per_unit`, the number would appear on screen and the function would return `None`. The value could not be stored, or added, or put into a table.

**Output**

```text
None
4.180645161290323
Traceback (most recent call last):
  File "w10_1.py", line 12, in <module>
    print(per_unit)
          ^^^^^^^^
NameError: name 'per_unit' is not defined
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three answers correct, with the `NameError` named | 4 |
| Explains the missing `return` and where the `None` blows up | 2 |
| Explains the local scope of `per_unit` | 2 |
| Tells returning apart from printing | 2 |

**Most common mistake**

Answering `0.02983` on the first line. The assumption is that a function which works something out hands it back, and that assumption is what produces the `None` blowing up three lines further down.

### 10.2 · Apply

**Solution**

```python
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50


def reject_rate(applications, rejected):
    """Return the share of applications a batch turned down."""
    return rejected / applications


def within_policy(rate):
    """Say whether a granted rate falls inside the 17.50 to 18.50 per cent band."""
    return rate >= LOWER_LIMIT and rate <= UPPER_LIMIT


print(round(reject_rate(1240, 37), 4))
print(round(reject_rate(1512, 68), 4))
print(round(reject_rate(760, 0), 4))

print(within_policy(18.00))
print(within_policy(18.50))
print(within_policy(18.60))
```

18.50 is the case that always has to be tested because it is the boundary, and it is where the decision is made about whether the limit belongs to the band. With `<` instead of `<=` that application would come out outside policy, and the function would carry on giving correct results at every other value.

**Output**

```text
0.0298
0.045
0.0
True
True
False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both functions return and neither prints | 3 |
| The six calls give the right result | 3 |
| Each function carries a one-line docstring | 2 |
| Explains why the exact boundary value gets tested | 2 |

**Most common mistake**

Putting the `print` inside `within_policy`. The function looks like it works on screen and is useless for counting how many applications comply, which is exactly what the next exercise asks for.

### 10.3 · Integrate

**Solution**

```python
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50


def within_policy(rate):
    """Say whether a granted rate falls inside the pricing band of the product."""
    return rate >= LOWER_LIMIT and rate <= UPPER_LIMIT


def verdict(rate):
    """Return where the application goes: within policy, overpriced or discounted."""
    if within_policy(rate):
        return "Within policy"
    if rate > UPPER_LIMIT:
        return "Overpriced"
    return "Discounted"


def applications_in_policy(rates):
    """Count how many rates in the list fall inside the band."""
    inside = 0

    for rate in rates:
        if within_policy(rate):
            inside += 1

    return inside


def average_rate(rates):
    """Return the mean of the list of granted rates."""
    running = 0.0

    for rate in rates:
        running += rate

    return running / len(rates)


applications = ["APP-1001", "APP-1002", "APP-1003", "APP-1004",
                "APP-1005", "APP-1006", "APP-1007", "APP-1008",
                "APP-1009", "APP-1010", "APP-1011", "APP-1012"]
rates = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

for i in range(len(applications)):
    print(f"{applications[i]:<10}{rates[i]:>7.2f}  {verdict(rates[i])}")

print(f"Reviewed:       {len(rates)}")
print(f"Within policy:  {applications_in_policy(rates)}")
print(f"Average rate:   {average_rate(rates):.4f} %")
```

The test of deleting the lower-limit comparison from `within_policy`: application APP-1005, placed at 17.40 %, would start coming out within policy and the count would climb from 9 to 10. The tests that catch it are the ones using a value below the band; if the student only tried 18.00, 18.50 and 18.60, none of them catches it and the 17.40 case has to be added.

**Output**

```text
APP-1001    18.10  Within policy
APP-1002    17.80  Within policy
APP-1003    18.60  Overpriced
APP-1004    18.00  Within policy
APP-1005    17.40  Discounted
APP-1006    18.30  Within policy
APP-1007    17.90  Within policy
APP-1008    18.50  Within policy
APP-1009    17.60  Within policy
APP-1010    18.20  Within policy
APP-1011    18.80  Overpriced
APP-1012    17.70  Within policy
Reviewed:       12
Within policy:  9
Average rate:   18.0750 %
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four functions with a docstring and none of them printing | 3 |
| `verdict` calls `within_policy` instead of repeating the comparison | 2 |
| The twelve rows and the three closing figures correct | 3 |
| The delete-a-line test and which case catches it | 2 |

**Most common mistake**

Repeating the band comparison inside `verdict` instead of calling the function. The program works the same, and when sales management moves the band somebody has to remember both places.

---

## Week 11 · Unit 5 · Arguments, built-in functions and modules

### 11.1 · Recognise

**Solution**

```text
4.18
0.35
9.18
```

On the first call nothing optional is passed: `factor` holds 60 and `extras` holds 0.0. Those are the analysis minutes per application.

On the second, the 5.0 landed in `factor`, because positional arguments fill the slots in order and `factor` is the one that follows `applications`. The function worked out 86.4 times 5 divided by 1240, which means nothing. Python flags no error because it received three valid arguments for three parameters that exist.

On the third, the 5.0 goes by name to `extras`, skips `factor`, and the result is the earlier 4.18 plus the extras.

If `factor=60` were moved ahead of `applications`, the file would not even run: a parameter with a default cannot sit before one without it, and Python rejects it with `SyntaxError` while reading it.

**Output**

```text
4.180645161290323
0.34838709677419355
9.180645161290322
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three numbers correct | 4 |
| Identifies that the 5.0 landed in `factor` on the second call | 2 |
| Explains why Python flags no error at all | 2 |
| Answers that moving the default to the front is a `SyntaxError` | 2 |

**Most common mistake**

Answering that the second call adds 5.0 to the result. The 5.0 gets read as the extra because that is the only optional visible on the third call, and the order of the parameters never gets checked.

### 11.2 · Apply

**Solution**

```python
def outside_policy(rate, policy=18.00, band=0.50):
    """Say whether a granted rate falls outside the policy rate plus or minus the band."""
    lower = policy - band
    upper = policy + band

    return rate < lower or rate > upper


print(outside_policy(18.60))
print(outside_policy(18.50))
print(outside_policy(18.60, 18.00, 1.00))
print(outside_policy(18.60, band=1.00))
print(outside_policy(14.20, policy=14.00))

print(18.00 - 0.50 == 17.50)
print(18.00 + 0.50 == 18.50)
```

The two checks at the end come out true, so in this case the computed limits match the ones in the written policy. The check is not wasted: with a different band the result can differ, as week 4 showed with 0.05 times 3. When a function works out boundaries from decimals, the boundary gets tested before anyone trusts it.

**Output**

```text
True
False
False
False
False
True
True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The function has both optional parameters last and its docstring | 2 |
| The five calls give the right result | 4 |
| One call passes the band by name, skipping the policy rate | 2 |
| Both boundary checks appear and are commented on | 2 |

**Most common mistake**

Writing `outside_policy(18.60, 1.00)` meaning to open the band. The 1.00 lands in `policy`, the function compares against a band of 0.50 to 1.50 % and returns true for the wrong reason.

### 11.3 · Integrate

**Solution**

```python
from statistics import mean, median, pstdev

LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50

rates = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

with_outlier = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
                17.90, 18.50, 17.60, 18.20, 18.80, 17.70, 27.00]

print(f"Applications: {len(rates)}")
print(f"Average:      {mean(rates):.4f} %")
print(f"Median:       {median(rates):.4f} %")
print(f"Spread:       {pstdev(rates):.4f} points")
print(f"Lowest:       {sorted(rates)[0]:.2f} %")
print(f"Highest:      {max(rates):.2f} %")

index = (UPPER_LIMIT - LOWER_LIMIT) / (6 * pstdev(rates))
print(f"Index:        {round(index, 3)}")

print(f"Average with the 27.00 rate: {mean(with_outlier):.4f} %")
print(f"Median with the 27.00 rate:  {median(with_outlier):.4f} %")
```

The third function is `pstdev`, the population standard deviation, documented on the `statistics` module page at docs.python.org. It takes a series of numeric data and returns the standard deviation of that series taken as a complete population, not as a sample.

A capability index of 0.41 means the real variation in price is wider than the band the policy authorises. The band measures 1.00 point and six spreads measure 2.44 points, so even with the average price sitting exactly on 18.00 the desk would keep placing outside the band. The sales director is not asked to move the policy rate: he is told the pricing process is not respecting the range he authorised, and that the spread is what has to be attacked.

With the 27.00 % rate the average jumps from 18.0750 to 18.7615 and the median only shifts from 18.0500 to 18.1000. When a capture looks suspicious, the median is the one that gets reported.

**Output**

```text
Applications: 12
Average:      18.0750 %
Median:       18.0500 %
Spread:       0.4065 points
Lowest:       17.40 %
Highest:      18.80 %
Index:        0.41
Average with the 27.00 rate: 18.7615 %
Median with the 27.00 rate:  18.1000 %
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three functions imported and the seven figures correct | 3 |
| The third function comes out of the documentation and is cited | 2 |
| The capability index is correct and interpreted | 3 |
| Compares average and median with the outlier rate and picks one | 2 |

**Most common mistake**

Reporting the capability index as though it were a percentage of well-priced applications. 0.41 is not 41 %, it is a ratio between the width of the band and the width of the spread, and mixing them turns a serious alert into a number that sounds tolerable.

---

## Week 12 · Unit 6 · Lists and tuples

### 12.1 · Recognise

**Solution**

```text
18.1 17.4
[17.8, 18.6]
[17.4, 17.8, 18.0, 18.1, 18.6]
[18.1, 17.8, 18.6, 18.0, 17.4]
None
[17.4, 17.8, 18.0, 18.1, 18.6]
6 5
```

The last line raises `IndexError`. The list ended up with six elements after the `append`, so the last valid index is 5.

`rates[1:3]` gives back two values because the first index goes in and the second does not. That is what makes the size of a slice the subtraction of the two numbers.

`backup` and `copy` end up different because `backup = rates` copied nothing: it created a second name for the same list, and the `append` modified it. `copy = rates.copy()` really did build a new list, which never heard about the change.

With `rates = rates.sort()`, the method sorts the list and returns `None`, and that assignment leaves the name `rates` pointing at `None`. The data are lost and the error turns up later, on the next line that tries to use them.

**Output**

```text
18.1 17.4
[17.8, 18.6]
[17.4, 17.8, 18.0, 18.1, 18.6]
[18.1, 17.8, 18.6, 18.0, 17.4]
None
[17.4, 17.8, 18.0, 18.1, 18.6]
6 5
Traceback (most recent call last):
  File "w12_1.py", line 17, in <module>
    print(rates[6])
          ~~~~~^^^
IndexError: list index out of range
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven lines correct and the closing `IndexError` | 4 |
| Explains the slice rule with the second index excluded | 2 |
| Explains alias against copy and why they give 6 and 5 | 2 |
| Explains what happens with `rates = rates.sort()` | 2 |

**Most common mistake**

Answering `[17.8, 18.6, 18.0]` on the second line. Three positions get counted because three minus one is two and the student adds the far end back in, and checking that the length is always the subtraction of the two indices settles it.

### 12.2 · Apply

**Solution**

```python
rates = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

print("At the start:", rates)

highest = max(rates)
lowest = min(rates)
top_three = sorted(rates, reverse=True)[0:3]
position = rates.index(17.40)

print(f"Highest:            {highest:.2f} %")
print(f"Lowest:             {lowest:.2f} %")
print(f"Top three:          {top_three}")
print(f"Position of 17.40:  {position}")
print(f"Application it belongs to: APP-{1001 + position}")
print(f"Last three:         {rates[9:12]}")

print("At the end:  ", rates)
```

The ordering is asked for with `sorted` and its keyword argument `reverse`, which is week 11 applied here. With the `sort` method the original list would end up sorted, and the exercise asks for the opposite.

Position 4 belongs to the fifth application, which is APP-1005, because the references start at APP-1001 and the index starts at 0.

**Output**

```text
At the start: [18.1, 17.8, 18.6, 18.0, 17.4, 18.3, 17.9, 18.5, 17.6, 18.2, 18.8, 17.7]
Highest:            18.80 %
Lowest:             17.40 %
Top three:          [18.8, 18.6, 18.5]
Position of 17.40:  4
Application it belongs to: APP-1005
Last three:         [18.2, 18.8, 17.7]
At the end:   [18.1, 17.8, 18.6, 18.0, 17.4, 18.3, 17.9, 18.5, 17.6, 18.2, 18.8, 17.7]
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four answers correct | 4 |
| The list comes out identical at the start and at the end | 3 |
| The reference is worked out from the position, not looked up by hand | 2 |
| Uses `sorted` and not the `sort` method | 1 |

**Most common mistake**

Answering APP-1004 for the 17.40 rate. The index gets added to the first reference without noticing that position 4 is the fifth application, and the result ends up shifted by one.

### 12.3 · Integrate

**Solution**

```python
BAND = (18.00, 17.50, 18.50)

rates = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

outside = []

for rate in rates:
    if rate < BAND[1] or rate > BAND[2]:
        outside.append(rate)

outside_sorted = sorted(outside, reverse=True)

print(f"Policy {BAND[0]:.2f} %, band from {BAND[1]:.2f} to {BAND[2]:.2f} %")
print(f"Applications: {len(rates)}")
print(f"Outside:      {len(outside)}")
print(f"Outside policy, highest to lowest: {outside_sorted}")
print(f"Original untouched: {rates}")

BAND[2] = 19.00
```

The band lives in a tuple because those are the values sales management authorised and they must not change while the program runs. In a list, any line could modify it by accident and the program would carry on running under a policy different from the one that was signed. The attempted assignment fails immediately and with a clear message, which is exactly what a constant is for.

**Output**

```text
Policy 18.00 %, band from 17.50 to 18.50 %
Applications: 12
Outside:      3
Outside policy, highest to lowest: [18.8, 18.6, 17.4]
Original untouched: [18.1, 17.8, 18.6, 18.0, 17.4, 18.3, 17.9, 18.5, 17.6, 18.2, 18.8, 17.7]
Traceback (most recent call last):
  File "w12_3.py", line 20, in <module>
    BAND[2] = 19.00
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The new list holds exactly the three that fall outside | 3 |
| The original list keeps its order and its contents | 2 |
| The descending order is obtained without destroying anything | 2 |
| The tuple error is pasted in full | 1 |
| Argues why the band belongs in a tuple | 2 |

**Most common mistake**

Writing `outside = rates` and then removing the compliant applications from that list. There are not two lists, there are two names for the same one, and the line printing the original at the end gives it away.

---

## Week 13 · Unit 6 · Sets and dictionaries · Second midterm

### 13.1 · Recognise

**Solution**

```text
4
Payment capacity above 35 %
None
Reason not in the catalogue
3
['M02', 'M03']
['M01']
['M01', 'M05']
```

The last line raises `KeyError` on the key `M09`.

The dictionary ends up with four entries because `reasons["M02"] = ...` adds nothing: the key already existed and its value was overwritten. `reasons["M04"] = ...` does add a new entry. Three plus one is four.

`batch_a` holds three elements because a set does not keep repeats: the `M01` appearing twice counts once. That is the difference from the list it came from.

**Output**

```text
4
Payment capacity above 35 %
None
Reason not in the catalogue
3
['M02', 'M03']
['M01']
['M01', 'M05']
Traceback (most recent call last):
  File "w13_1.py", line 20, in <module>
    print(reasons["M09"])
          ~~~~~~~^^^^^^^
KeyError: 'M09'
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight lines correct | 4 |
| The `KeyError` on the last line, named | 2 |
| Explains why the dictionary settles at four entries | 2 |
| Explains why the set settles at three elements | 2 |

**Most common mistake**

Answering 5 on the first line. Both assignments get counted as new entries, without noticing that M02 was already there and that a key never repeats.

### 13.2 · Apply

**Solution**

```python
reasons = {"M01": "Bureau score too low",
           "M02": "Payment capacity above 35 %",
           "M03": "Incomplete documentation",
           "M04": "Not enough time in the job",
           "M05": "Income cannot be verified",
           "M06": "Client already has an active loan"}

reported = ["M01", "M03", "M01", "M05", "M01", "M02", "M03", "M09"]

print("Rejection reason catalogue")
for code, description in reasons.items():
    print(f"  {code}  {description}")

print(f"Reasons in the catalogue: {len(reasons)}")
print(f"Rejections reported:      {len(reported)}")
print(f"Distinct reasons:         {len(set(reported))}")

for code in sorted(set(reported)):
    print(f"  {code}  {reasons.get(code, 'Reason not in the catalogue')}")
```

M09 is not in the catalogue, and with square brackets the program would have stopped there. With `get` and its default, the report comes out complete and also shows that somebody is capturing a reason that does not exist, which is useful information for the floor.

**Output**

```text
Rejection reason catalogue
  M01  Bureau score too low
  M02  Payment capacity above 35 %
  M03  Incomplete documentation
  M04  Not enough time in the job
  M05  Income cannot be verified
  M06  Client already has an active loan
Reasons in the catalogue: 6
Rejections reported:      8
Distinct reasons:         5
  M01  Bureau score too low
  M02  Payment capacity above 35 %
  M03  Incomplete documentation
  M05  Income cannot be verified
  M09  Reason not in the catalogue
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The catalogue is walked with `items` and comes out complete | 2 |
| The three figures are correct | 3 |
| The lookup uses `get` with a default | 3 |
| M09 appears in the report without stopping the program | 2 |

**Most common mistake**

Counting the distinct reasons with `len(reported)`. It gives 8 instead of 5, and it confuses how many rejections were reported with how many kinds of reason there are.

### 13.3 · Integrate

**Solution**

```python
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
hours = [86.4, 61.5, 112.8, 48.2]
applications = [1240, 984, 1512, 760]

reported_a = ["M01", "M03", "M01", "M05", "M01", "M02", "M03"]
reported_b = ["M02", "M02", "M06", "M03", "M01"]

hours_per_desk = {}
for i in range(len(desks)):
    hours_per_desk[desks[i]] = hours[i]

counts = {}
for code in reported_a:
    counts[code] = counts.get(code, 0) + 1

print("Analyst-hours per desk")
for desk, h in hours_per_desk.items():
    print(f"  {desk}  {h:>6.1f} h")

print(f"Floor total: {sum(hours_per_desk.values()):.1f} h")

costliest_desk = ""
highest = 0.0
for desk, h in hours_per_desk.items():
    if h > highest:
        highest = h
        costliest_desk = desk

print(f"Costliest desk: {costliest_desk} with {highest:.1f} h")

print("Reasons in batch A")
for code in sorted(counts):
    print(f"  {code}  {counts[code]}")

codes_a = set(reported_a)
codes_b = set(reported_b)

print(f"In both batches:      {sorted(codes_a & codes_b)}")
print(f"Only in batch A:      {sorted(codes_a - codes_b)}")
print(f"New in batch B:       {sorted(codes_b - codes_a)}")
print(f"In one but not both:  {sorted(codes_a ^ codes_b)}")
```

The new reason in batch B is M06, a client who already has an active loan, and that is the one that triggers an origination decision: if applications are starting to arrive from clients who already owe, the campaign is aimed at the wrong base and the list filter has to be reviewed before any more calls go out.

The count for batch A could not be done with a set because a set drops the repeats, and what was wanted was precisely how many times each reason came up. A set answers which ones there are, a dictionary answers how many of each.

**Output**

```text
Analyst-hours per desk
  MC-01    86.4 h
  MC-02    61.5 h
  MC-03   112.8 h
  MC-04    48.2 h
Floor total: 308.9 h
Costliest desk: MC-03 with 112.8 h
Reasons in batch A
  M01  3
  M02  1
  M03  2
  M05  1
In both batches:      ['M01', 'M02', 'M03']
Only in batch A:      ['M05']
New in batch B:       ['M06']
In one but not both:  ['M05', 'M06']
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The dictionary is built with a loop from the lists | 2 |
| The total comes from `values` and the costliest desk from a pass | 2 |
| The counter uses `get` with a default of zero | 2 |
| The four comparisons use set operations | 2 |
| Both conclusions written | 2 |

**Most common mistake**

Comparing the two batches with a loop and an `if` instead of set operations. The result comes out the same, takes fifteen lines, and falls apart the moment the fourth question has to be answered, the one about what is in one but not in both.

---

## Week 14 · Unit 7 · Text and CSV files

### 14.1 · Recognise

**Solution**

```text
30
MC-01 18.10
<class 'str'>
18.1017.80
True
False
```

The fourth line raises no error because both values are text, and `+` between two strings glues them together. The result, `18.1017.80`, is not a number and the program carries on regardless. That is the most expensive conversion mistake of the term: it gives no warning.

The sixth line comes out false because the third row of the file carries the desk written as `" MC-01"`, with a space in front. Two strings that look the same on screen and differ by one character are different values, which is why a grouping by desk would report nine desks where there are four.

If that same open call carried `"w"`, the file would be emptied the instant it was opened, before anything was read. The thirty rows would be gone and the program would then fail trying to read a file opened for writing.

**Output**

```text
30
MC-01 18.10
<class 'str'>
18.1017.80
True
False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines correct | 4 |
| Explains why adding two strings raises no error | 2 |
| Spots the leading space on the third row | 2 |
| Explains what happens to the file under mode `"w"` | 2 |

**Most common mistake**

Answering `35.90` on the fourth line. The two rates get added as though `DictReader` had converted the types, when a CSV only ever holds text and nobody else is going to convert it for you.

### 14.2 · Apply

**Solution**

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent


def to_decimal(text):
    """Convert to decimal by stripping the peso sign and the thousands comma."""
    clean = text.replace("$", "").replace(",", "")
    return float(clean.strip())


def to_integer(text):
    """Convert to integer. An empty cell is reported as absence with None."""
    text = text.strip()
    return int(text) if text else None


def normalise(text):
    """Leave one single spelling of the desk: trimmed and upper case."""
    return text.strip().upper()


with (DATA / "applications.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

spellings = set()
no_hours = 0

for row in rows:
    spellings.add(row["desk"])
    if to_integer(row["resp_hours"]) is None:
        no_hours += 1

normalised = set()
for row in rows:
    normalised.add(normalise(row["desk"]))

print(f"Rows read:                 {len(rows)}")
print(f"Rows with no response hours: {no_hours}")
print(f"Spellings of the desk:     {len(spellings)}")
print(f"Desks after normalising:   {len(normalised)}")

commission = {}
count = {}
rate_total = {}

for row in rows:
    desk = normalise(row["desk"])
    commission[desk] = commission.get(desk, 0.0) + to_decimal(row["commission_mxn"])
    count[desk] = count.get(desk, 0) + 1
    rate_total[desk] = rate_total.get(desk, 0.0) + float(row["rate_pct"])

print(f"{'Desk':<10}{'Applications':>14}{'Commission':>13}{'Rate':>10}")

commission_total = 0.0
count_total = 0

for desk in sorted(commission):
    average = rate_total[desk] / count[desk]
    commission_total += commission[desk]
    count_total += count[desk]
    print(f"{desk:<10}{count[desk]:>14}{commission[desk]:>13,.0f}{average:>10.4f}")

print(f"{'ALTAMAR':<10}{count_total:>14}{commission_total:>13,.0f}")
```

`to_integer` returns `None` and not zero, because response hours that were never captured are not an instant reply. The decision about what to do with that absence is taken in the next exercise, not here.

The dictionaries with `get` and a default are week 13 applied: each desk turns up for the first time without the program having to know in advance how many there are.

**Output**

```text
Rows read:                 30
Rows with no response hours: 3
Spellings of the desk:     9
Desks after normalising:   4
Desk        Applications   Commission      Rate
MC-01                  9       11,325   18.0222
MC-02                  7        7,060   18.0714
MC-03                  8       12,125   18.1000
MC-04                  6        4,467   18.0833
ALTAMAR               30       34,977
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three functions with a docstring and a single responsibility | 3 |
| The four diagnostic lines correct | 2 |
| The table by desk and the floor total correct | 3 |
| The path is built with `pathlib` from the location of the file | 1 |
| Reads by column name, not by position | 1 |

**Most common mistake**

Converting the commission with a plain `float(row["commission_mxn"])`. It raises `ValueError` on the first row over the peso sign and the comma, and the student usually blames the file instead of the format.

### 14.3 · Integrate

**Solution**

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50


def to_decimal(text):
    """Convert to decimal by stripping the peso sign and the thousands comma."""
    clean = text.replace("$", "").replace(",", "")
    return float(clean.strip())


def normalise(text):
    """Leave one single spelling of the desk: trimmed and upper case."""
    return text.strip().upper()


def outside_policy(rate):
    """Say whether the granted rate falls outside the 17.50 to 18.50 per cent band."""
    return rate < LOWER_LIMIT or rate > UPPER_LIMIT


with (DATA / "applications.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

seen = set()
clean_rows = []

for row in rows:
    fingerprint = (row["date"], row["desk"], row["batch"],
                   row["rate_pct"], row["resp_hours"], row["commission_mxn"])

    if fingerprint in seen:
        continue

    seen.add(fingerprint)
    clean_rows.append(row)

commission = {}
count = {}
outside = {}
no_hours = 0

for row in clean_rows:
    desk = normalise(row["desk"])
    rate = float(row["rate_pct"])

    commission[desk] = commission.get(desk, 0.0) + to_decimal(row["commission_mxn"])
    count[desk] = count.get(desk, 0) + 1
    outside[desk] = outside.get(desk, 0)

    if outside_policy(rate):
        outside[desk] += 1

    if row["resp_hours"].strip() == "":
        no_hours += 1

print(f"Rows in the file:            {len(rows)}")
print(f"Exact duplicates removed:    {len(rows) - len(clean_rows)}")
print(f"Rows left:                   {len(clean_rows)}")
print(f"Rows kept with no response hours: {no_hours}")
print(f"Applications outside policy: {sum(outside.values())}")
print(f"Floor commission:            {sum(commission.values()):,.0f} pesos")

target = DATA / "desk_summary.csv"

with target.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["desk", "applications", "outside_policy", "commission_mxn"])

    for desk in sorted(commission):
        writer.writerow([desk, count[desk], outside[desk],
                         round(commission[desk], 1)])

print(f"File written: {target.name}")

with target.open(encoding="utf-8") as f:
    print(f.read().strip())
```

The fingerprint of a row is a tuple of the six columns, and the set of fingerprints is what catches the exact duplicate. Comparing only by date and desk would have deleted legitimate applications from different clients on the same day.

The 2,515 pesos of difference are the sum of the two duplicated rows: 1,260 from the MC-01 row of 9 January and 1,255 from the MC-01 row of 12 January. A duplicate inflates the commission because the amount is added twice, and barely moves the average rate because there the repeated value enters the numerator and the denominator at once.

**Output**

```text
Rows in the file:            30
Exact duplicates removed:    2
Rows left:                   28
Rows kept with no response hours: 3
Applications outside policy: 8
Floor commission:            32,462 pesos
File written: desk_summary.csv
desk,applications,outside_policy,commission_mxn
MC-01,7,3,8810.0
MC-02,7,1,7060.0
MC-03,8,4,12125.0
MC-04,6,0,4467.0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Duplicates are caught by comparing the whole row | 2 |
| The six log figures correct | 3 |
| The output file has the header and the four rows asked for | 2 |
| It is written with an empty `newline` and no blank rows | 1 |
| Explains the exact 2,515 peso difference | 2 |

**Most common mistake**

Catching duplicates by date and desk alone. Applications from different clients get deleted, the count drops from 28 to 18 and the total commission lands well below where it should, with nothing to flag it.

---

## Week 15 · Unit 8.1 · Series, DataFrame, cleaning and grouping

### 15.1 · Recognise

**Solution**

`shape` gives `(30, 6)`. The types: `date`, `desk`, `batch` and `commission_mxn` come out as text, `rate_pct` and `resp_hours` come out `float64`. There are 3 missing values in `resp_hours`, 2 duplicated rows and 9 distinct spellings of the desk.

`resp_hours` came out decimal and not integer because three cells are empty, and the missing-value marker only exists in a decimal column. That is not a pandas failure: it is the price of a column with holes, and it is why the hours print as 44.0 instead of 44.

`commission_mxn` came out as text because the peso sign and the thousands comma are formatting, not value. While they are there, that column cannot be summed.

In `value_counts` two rows look identical, `MC-01` and `MC-01 `, and they are separate entries because one carries a trailing space. That space does not show on screen and it does split the groups.

`describe` only summarises `rate_pct` and `resp_hours`, the two numeric columns. The other four are text as far as pandas is concerned, the date included, and that is why they stay out.

**Output**

```text
(30, 6)
date                  str
desk                  str
batch                 str
rate_pct          float64
resp_hours        float64
commission_mxn        str
dtype: object
3
2
9
desk
MC-03     7
MC-01     6
MC-02     6
MC-04     6
 MC-01    1
mc-01     1
MC-01     1
mc-02     1
MC-03     1
Name: count, dtype: int64
count    30.000
mean     18.067
std       0.465
min      17.100
25%      17.725
50%      18.100
75%      18.400
max      18.900
Name: rate_pct, dtype: float64
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven outputs correct, with the types of the six columns | 3 |
| Explains the `float64` on `resp_hours` from the missing values | 2 |
| Explains the text on `commission_mxn` from the sign and the comma | 2 |
| Spots the two rows that look the same in `value_counts` | 2 |
| Says which columns `describe` summarises and why | 1 |

**Most common mistake**

Saying `resp_hours` came out decimal because the hours carry fractions. Every one of them in the file is a whole number, and anybody who does not check `isna` never finds out the cause is the three empty cells.

### 15.2 · Apply

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50

applications = pd.read_csv(DATA / "applications.csv")

print(f"On load:              {len(applications)} rows")
print(f"Exact duplicates:     {applications.duplicated().sum()}")
print(f"Desk spellings:       {applications['desk'].nunique()}")
print(f"No response hours:    {applications['resp_hours'].isna().sum()}")

applications = applications.drop_duplicates()
print(f"Without duplicates:   {len(applications)} rows")

applications["desk"] = applications["desk"].str.strip().str.upper()
print(f"Real desks:           {applications['desk'].nunique()}")

applications["commission_mxn"] = (applications["commission_mxn"]
                                  .str.replace("$", "", regex=False)
                                  .str.replace(",", "", regex=False)
                                  .str.strip()
                                  .astype(float))

applications["date"] = pd.to_datetime(applications["date"])

print(applications.dtypes)

applications["verdict"] = "Within policy"
applications.loc[(applications["rate_pct"] < LOWER_LIMIT) |
                 (applications["rate_pct"] > UPPER_LIMIT),
                 "verdict"] = "Outside policy"

print(applications["verdict"].value_counts())

critical = applications[(applications["desk"] == "MC-03") &
                        (applications["verdict"] == "Outside policy")]
print(f"MC-03 outside policy: {len(critical)}")

first_two = applications[applications["desk"].isin(["MC-01", "MC-02"])]
print(f"Applications from MC-01 and MC-02: {len(first_two)}")

print(f"Total commission:     {applications['commission_mxn'].sum():,.0f} pesos")
print(f"Average hours:        {applications['resp_hours'].mean():.2f} h")
print(f"Rows left if the three without hours are dropped: "
      f"{len(applications.dropna(subset=['resp_hours']))}")
```

Dropping the three rows with no response hours would leave 25 applications. Keeping them suits this file because the value that decides whether the price complies is the rate, and that one was captured in all three cases. Throwing them out would cost three good rates to avoid losing three response times, and the average hours can be worked out from the 25 that do carry it without deleting anything.

**Output**

```text
On load:              30 rows
Exact duplicates:     2
Desk spellings:       9
No response hours:    3
Without duplicates:   28 rows
Real desks:           4
date              datetime64[us]
desk                         str
batch                        str
rate_pct                 float64
resp_hours               float64
commission_mxn           float64
dtype: object
verdict
Within policy     20
Outside policy     8
Name: count, dtype: int64
MC-03 outside policy: 4
Applications from MC-01 and MC-02: 14
Total commission:     32,462 pesos
Average hours:        44.36 h
Rows left if the three without hours are dropped: 25
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six log figures correct | 3 |
| The four repairs applied in order and the final types correct | 2 |
| The `verdict` column is written with `loc` in a single step | 2 |
| The three filters give 4, 14 and the correct totals | 2 |
| Justifies in writing the decision on the rows with no hours | 1 |

**Most common mistake**

Writing the column with `applications[applications[...]]["verdict"] = ...`. Chained assignment does nothing, the column stays entirely on "Within policy" and the count comes out 28 and 0 without a single error being raised.

### 15.3 · Integrate

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50


def load_clean():
    """Load applications.csv and apply the four repairs from session 15.2."""
    data = pd.read_csv(DATA / "applications.csv").drop_duplicates()

    data["desk"] = data["desk"].str.strip().str.upper()
    data["commission_mxn"] = (data["commission_mxn"]
                              .str.replace("$", "", regex=False)
                              .str.replace(",", "", regex=False)
                              .str.strip()
                              .astype(float))
    data["date"] = pd.to_datetime(data["date"])

    data["verdict"] = "Within policy"
    data.loc[(data["rate_pct"] < LOWER_LIMIT) |
             (data["rate_pct"] > UPPER_LIMIT),
             "verdict"] = "Outside policy"

    return data


applications = load_clean()

board = applications.groupby("desk").agg(
    applications=("rate_pct", "count"),
    commission=("commission_mxn", "sum"),
    hours=("resp_hours", "mean"),
    rate=("rate_pct", "mean"),
).round(3)

print(board.sort_values("commission", ascending=False))

outside = applications[applications["verdict"] == "Outside policy"]
print(outside.groupby("desk").size())

grid = applications.pivot_table(index="desk", columns="batch",
                                values="commission_mxn", aggfunc="sum",
                                fill_value=0, margins=True)
print(grid.round(0))

catalogue = pd.DataFrame({
    "desk": ["MC-01", "MC-02", "MC-03", "MC-04", "MC-05"],
    "city": ["Monterrey", "Guadalajara", "Leon", "Puebla", "Merida"],
    "target_hours": [42, 40, 48, 36, 30],
})

audit = applications.merge(catalogue, on="desk", how="outer", indicator=True)
print(audit["_merge"].value_counts())

joined = board.reset_index().merge(catalogue, on="desk", how="left")
joined["hours_gap"] = (joined["hours"] / joined["target_hours"] - 1)

print(joined[["desk", "city", "applications", "hours",
              "target_hours", "hours_gap"]].round(3))
```

The outside-policy table carries three rows and not four because MC-04 contributed none. `groupby` only returns the groups that exist in the data it received, and a desk with no outside applications simply does not appear. If that table is going into a subtraction or a division, the zero has to be filled in on purpose.

The audit of the join: 28 rows crossed on both sides, 1 came from the catalogue alone and 0 from the applications alone. The one from the catalogue is MC-05, the Merida branch, already registered and with nothing placed this week: that is fine and explains itself. The zero on the other side is the figure that matters: no application was left orphaned, which means the file carries no unknown desk. If that number were not zero, it would have to be reported before publishing any total.

MC-01 runs 6.7 % above its response-time target and MC-03 6.2 %, while MC-02 sits at only 1.2 %. The operations director gets told that two of the four desks are taking around three hours more than the standard says on every application, and that at MC-03 those three hours pile on top of the longest response time on the floor.

**Output**

```text
       applications  commission   hours    rate
desk                                           
MC-03             8     12125.0  51.000  18.100
MC-01             7      8810.0  44.833  17.986
MC-02             7      7060.0  40.500  18.071
MC-04             6      4467.0  37.800  18.083
desk
MC-01    3
MC-02    1
MC-03    4
dtype: int64
batch   C-2601   C-2602  C-2603      All
desk                                    
MC-01   3740.0   2485.0  2585.0   8810.0
MC-02   1990.0   2055.0  3015.0   7060.0
MC-03   4690.0   4540.0  2895.0  12125.0
MC-04   1490.0   1500.0  1477.0   4467.0
All    11910.0  10580.0  9972.0  32462.0
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
    desk         city  applications   hours  target_hours  hours_gap
0  MC-01    Monterrey             7  44.833            42      0.067
1  MC-02  Guadalajara             7  40.500            40      0.012
2  MC-03         Leon             8  51.000            48      0.062
3  MC-04       Puebla             6  37.800            36      0.050
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The cleaning ends up wrapped in a function with a docstring | 1 |
| The board of four summaries comes out in a single statement | 2 |
| Explains why the outside-policy table carries three rows | 2 |
| The grid with row and column totals is correct | 2 |
| The join is audited both ways and the three numbers interpreted | 2 |
| The response-time gap board is correct and reported | 1 |

**Most common mistake**

Joining with `inner` instead of `left` for the board. On this data the result does not change, and that is how the student gets used to a mode that will silently delete rows the moment a desk is missing from the catalogue.

---

## Week 16 · Unit 8.2 · Visualisation with matplotlib and seaborn

### 16.1 · Recognise

**Solution**

The bar shows the average commission per application, because `barplot` averages when it is not told otherwise. For MC-01 the bar is worth 1,258.6 pesos. What the subject line says, the commission on the batch, is 8,810 pesos, seven times more. Both numbers are correct and answer different questions: one is how much each application left on average, the other is how much the desk left.

For the bar to show the total, `estimator="sum"` has to be added, and along with it `errorbar=None`, because the interval drawn on top of each bar means nothing in a revenue report.

The four charts:

- Commission of the four desks: bars, because it compares categories with no natural order. Sorted from highest to lowest, the ranking reads itself.
- Spread of the rates inside each desk: box plot, because the question is not the centre but the shape, and that is where the spread the average hides shows up.
- Average rate across the three days: line, because the horizontal axis is time and joining two dates does assert something true.
- Response hours against pricing gap: scatter, because it asks whether two numeric variables move together.

**Output**

```text
           sum    mean  count
desk                         
MC-03  12125.0  1515.6      8
MC-01   8810.0  1258.6      7
MC-02   7060.0  1008.6      7
MC-04   4467.0   744.5      6
          mean     std   min   max
desk                              
MC-04  18.0833  0.3430  17.6  18.5
MC-02  18.0714  0.4348  17.5  18.7
MC-01  17.9857  0.4880  17.3  18.6
MC-03  18.1000  0.6459  17.1  18.9
desk
MC-01    3
MC-02    1
MC-03    4
dtype: int64
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Identifies that the bar shows the average and gives both MC-01 figures | 3 |
| Names `estimator` and `errorbar` as the fix | 2 |
| The three tables print correctly | 2 |
| The four charts chosen and justified | 3 |

**Most common mistake**

Answering that the bar shows the total because the axis reaches into the thousands. All four bars look plausible at that scale, and without running the sum and average table there is no way to notice the factor of seven.

### 16.2 · Apply

**Solution**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

from cleaning import load_clean

TARGET = Path(__file__).resolve().parent

applications = load_clean()

commission = (applications.groupby("desk")["commission_mxn"]
              .sum()
              .sort_values(ascending=False))

print(commission)

peak = commission.index[0]
share = commission.iloc[0] / commission.sum()

print(f"{peak} holds {share:.1%} of the commission on the floor")

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(commission.index, commission.values, color="#C7D6E8")
bars[0].set_color("#2B5F8F")

ax.set_title(f"{peak} holds {share:.0%} of the origination commission on the floor")
ax.set_ylabel("Origination commission for the batch (pesos)")
ax.set_ylim(0, 13000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1000:.0f}k"))

fig.text(0.01, 0.01,
         "Source: applications.csv, Financiera Altamar, 8 to 12 January 2026",
         fontsize=8)

fig.savefig(TARGET / "commission_desk.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("File generated:", (TARGET / "commission_desk.png").exists())
```

The `load_clean` function is the one from 15.3, saved in a `cleaning.py` file next to this week's programs so the cleanup is not copied into every chart.

Alternative text: bar chart of the origination commission each of the four desks at Financiera Altamar left between 8 and 12 January 2026. MC-03 leads with 12,125 pesos, followed by MC-01 with 8,810, MC-02 with 7,060 and MC-04 with 4,467. MC-03 on its own accounts for 37 % of the 32,462 pesos on the floor and leaves 2.7 times what MC-04 does.

**Output**

```text
desk
MC-03    12125.0
MC-01     8810.0
MC-02     7060.0
MC-04     4467.0
Name: commission_mxn, dtype: float64
MC-03 holds 37.4% of the commission on the floor
File generated: True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The series by desk is correct and sorted | 2 |
| The title states the finding and the percentage is worked out in the program | 2 |
| Axis labelled, base at zero and formatted in thousands | 2 |
| The peak bar highlighted and the source at the foot | 2 |
| The alternative text carries figures checkable against the series | 2 |

**Most common mistake**

Typing the 37 % into the title by hand. It works until next month's file arrives, and then the chart asserts a percentage its own bars no longer support.

### 16.3 · Integrate

**Solution**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

from cleaning import load_clean

TARGET = Path(__file__).resolve().parent

sns.set_theme(style="whitegrid", palette="deep")

applications = load_clean()

summary = applications.groupby("desk")["rate_pct"].agg(
    ["mean", "median", "std", "count"]).round(4)
print(summary.sort_values("std"))

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=applications, x="desk", y="commission_mxn", estimator="sum",
            errorbar=None, hue="desk", legend=False, ax=ax)
ax.set_title("MC-03 leaves 2.7 times the commission of MC-04 in the same batch")
ax.set_ylabel("Origination commission for the batch (pesos)")
fig.savefig(TARGET / "commission_bars.png", dpi=150, bbox_inches="tight")
plt.close(fig)

order = (applications.groupby("desk")["rate_pct"]
         .std().sort_values().index)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=applications, x="desk", y="rate_pct", order=order,
            hue="desk", legend=False, ax=ax)
ax.axhline(17.50, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(18.50, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("MC-01 sits closest to the policy rate and still prices outside the band")
ax.set_ylabel("Rate granted (%)")
fig.savefig(TARGET / "box_desk.png", dpi=150, bbox_inches="tight")
plt.close(fig)

grid = applications.pivot_table(index="desk", columns="batch",
                                values="commission_mxn", aggfunc="sum",
                                fill_value=0) / 1000
print(grid.round(2))

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(grid, annot=True, fmt=".1f", cmap="Blues", ax=ax)
ax.set_title("Batch C-2601 at MC-03 is the most profitable cell on the board")
fig.savefig(TARGET / "heatmap_desk_batch.png", dpi=150, bbox_inches="tight")
plt.close(fig)

for name in ["commission_bars.png", "box_desk.png", "heatmap_desk_batch.png"]:
    print(name, (TARGET / name).exists())
```

The conclusion from the three together: MC-03 is the desk that leaves the most and the loosest on price at the same time, with 12,125 pesos of commission, the highest spread at 0.6459 points and 4 of the 8 applications outside the band. MC-01 has the mean closest to the policy rate, 17.9857 %, and still 3 applications outside, because its spread is the second highest at 0.4880. MC-04 is the one that holds the price best: 0.3430 of spread and no application outside the band, though it is also the one that places least.

The box plot is what goes to the operations director. The bars say how much each desk leaves and the heatmap says in which batch, but the box plot is the only one showing that an average glued to policy does not mean a disciplined pricing process, which is exactly what has to be fixed at MC-01.

**Output**

```text
          mean  median     std  count
desk                                 
MC-04  18.0833   18.15  0.3430      6
MC-02  18.0714   18.10  0.4348      7
MC-01  17.9857   18.10  0.4880      7
MC-03  18.1000   18.10  0.6459      8
batch  C-2601  C-2602  C-2603
desk                         
MC-01    3.74    2.48    2.58
MC-02    1.99    2.06    3.02
MC-03    4.69    4.54    2.90
MC-04    1.49    1.50    1.48
commission_bars.png True
box_desk.png True
heatmap_desk_batch.png True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The theme is set once and the three images are generated | 2 |
| The bar chart uses `estimator` and drops the error bar | 2 |
| The box plot is ordered by spread and carries the two band lines | 2 |
| The heatmap comes from the grid, in thousands and with values written in | 1 |
| The three titles state a checkable finding | 1 |
| The conclusion carries at least three figures and picks one chart | 2 |

**Most common mistake**

Leaving the box plot in alphabetical order. The spread ranking, which is the entire content of that chart, stays hidden and has to be read box by box.

---

## Week 17 · Review and final exam

### 17.1 · Recognise

**Solution**

```text
9
False
None
48.2
$1,240$980
17.8
```

Line 1, grouping before cleaning. Nine desks come out where there are 4, because the spaces and the lower case still split the groups. The correct result is 4.

Line 2, chained assignment. The column was never created. Since pandas 3.0 the operation does nothing and raises no error, only a warning that is easy to miss. The correct form is `applications.loc[condition, "verdict"] = "Review"`.

Line 3, confusing modifying with returning. `sort` sorts the list and returns `None`, so the assignment wiped the data. The correct form is `sorted(rates)`, or calling `rates.sort()` without assigning.

Line 4, accumulator declared inside. It gives 48.2, the last workload. The correct total is 308.9.

Line 5, working things out without converting. Both values are text and `+` glues them together. The correct result, after converting, is 2,220 pesos.

Line 6, counting from one. `applications["rate_pct"][1]` returns 17.8, the second row of the file. The question was about the first one, which was placed at 18.10 and sits at index 0.

The program does not stop on any of the six because all six are valid Python operations over valid data. None of them is a syntax error or a type error: they are correct answers to questions nobody asked.

**Output**

```text
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series
through chained assignment.
  applications[applications["desk"] == "MC-03"]["verdict"] = "Review"
9
False
None
48.2
$1,240$980
17.8
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines correct | 3 |
| The six mistakes named | 3 |
| The correct result for each one | 2 |
| Explains why the program did not stop | 1 |
| Identifies the real question behind the last line | 1 |

**Most common mistake**

Answering 4 on the first line because there are four desks on the floor. The answer comes from what is known about the operation instead of from what the file carries, and it is the same reflex that stops anybody from checking a dirty total.

### 17.2 · Apply

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50

applications = pd.read_csv(DATA / "applications.csv")

print(f"Rows:              {len(applications)}")
print(f"Duplicates:        {applications.duplicated().sum()}")
print(f"Desk spellings:    {applications['desk'].nunique()}")
print(f"No response hours: {applications['resp_hours'].isna().sum()}")

applications = applications.drop_duplicates()
applications["desk"] = applications["desk"].str.strip().str.upper()
applications["commission_mxn"] = (applications["commission_mxn"]
                                  .str.replace("$", "", regex=False)
                                  .str.replace(",", "", regex=False)
                                  .str.strip()
                                  .astype(float))

applications["verdict"] = "Within policy"
applications.loc[(applications["rate_pct"] < LOWER_LIMIT) |
                 (applications["rate_pct"] > UPPER_LIMIT),
                 "verdict"] = "Outside policy"

board = applications.groupby("desk").agg(
    applications=("rate_pct", "count"),
    commission=("commission_mxn", "sum"),
    rate=("rate_pct", "mean"),
    spread=("rate_pct", "std"),
)
board["outside"] = (applications[applications["verdict"] == "Outside policy"]
                    .groupby("desk").size()
                    .reindex(board.index, fill_value=0))
board["share"] = board["outside"] / board["applications"]

print(board.round(4).sort_values("commission", ascending=False))

worst = board["share"].idxmax()
commission_share = board.loc[worst, "commission"] / board["commission"].sum()
outside_share = board.loc[worst, "outside"] / board["outside"].sum()

print(f"{worst} leaves {commission_share:.1%} of the commission on the floor "
      f"and holds {outside_share:.0%} of the applications outside policy.")
```

The `reindex` filling with zero is what keeps MC-04 from coming out empty in the outside-policy column. Without it, the share for that desk would come out as a missing value and the division at the end would give a meaningless result. Anybody who does not know `reindex` can reach the same board by joining the count and filling with `fillna(0)`, and both routes mark the same.

**Output**

```text
Rows:              30
Duplicates:        2
Desk spellings:    9
No response hours: 3
       applications  commission     rate  spread  outside   share
desk                                                             
MC-03             8     12125.0  18.1000  0.6459        4  0.5000
MC-01             7      8810.0  17.9857  0.4880        3  0.4286
MC-02             7      7060.0  18.0714  0.4348        1  0.1429
MC-04             6      4467.0  18.0833  0.3430        0  0.0000
MC-03 leaves 37.4% of the commission on the floor and holds 50% of the applications outside policy.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four inspection lines before anything is touched | 2 |
| The cleaning complete and in the right order | 2 |
| The board with the six correct columns | 3 |
| The desk with no outside applications shows zero and not empty | 1 |
| The conclusion is assembled from the board, with its two figures | 2 |

**Most common mistake**

Skipping the inspection and cleaning straight away. The program hands back the same board and the student cannot say how many duplicates were removed, which is the first question in any review.

### 17.3 · Integrate

**Solution**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 17.50
UPPER_LIMIT = 18.50


def mark_verdict(data):
    """Add the verdict column from the 17.50 to 18.50 per cent band."""
    data["verdict"] = "Within policy"
    data.loc[(data["rate_pct"] < LOWER_LIMIT) |
             (data["rate_pct"] > UPPER_LIMIT),
             "verdict"] = "Outside policy"
    return data


def load_clean():
    """Load applications.csv, drop duplicates, normalise and convert types."""
    data = pd.read_csv(DATA / "applications.csv").drop_duplicates()

    data["desk"] = data["desk"].str.strip().str.upper()
    data["commission_mxn"] = (data["commission_mxn"]
                              .str.replace("$", "", regex=False)
                              .str.replace(",", "", regex=False)
                              .str.strip()
                              .astype(float))
    data["date"] = pd.to_datetime(data["date"])

    return mark_verdict(data)


raw = mark_verdict(pd.read_csv(DATA / "applications.csv"))
clean = load_clean()

outside_raw = (raw["verdict"] == "Outside policy").sum()
outside_clean = (clean["verdict"] == "Outside policy").sum()

print(f"Unclean: {outside_raw} of {len(raw)} outside policy "
      f"({outside_raw / len(raw):.1%})")
print(f"Clean:   {outside_clean} of {len(clean)} outside policy "
      f"({outside_clean / len(clean):.1%})")

board = clean.groupby("desk").agg(
    applications=("rate_pct", "count"),
    commission=("commission_mxn", "sum"),
    rate=("rate_pct", "mean"),
    spread=("rate_pct", "std"),
).round(4)

print(board.sort_values("spread", ascending=False))

catalogue = pd.DataFrame({
    "desk": ["MC-01", "MC-02", "MC-03", "MC-04", "MC-05"],
    "city": ["Monterrey", "Guadalajara", "Leon", "Puebla", "Merida"],
    "target_hours": [42, 40, 48, 36, 30],
})

audit = clean.merge(catalogue, on="desk", how="outer", indicator=True)
print(audit["_merge"].value_counts())

sns.set_theme(style="whitegrid", palette="deep")

order = board.sort_values("spread").index

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=clean, x="desk", y="rate_pct", order=order,
            hue="desk", legend=False, ax=ax)
ax.axhline(LOWER_LIMIT, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(UPPER_LIMIT, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("MC-03 is the only desk whose upper quartile clears 18.50 %")
ax.set_ylabel("Rate granted (%)")
fig.text(0.01, 0.01, "Source: applications.csv, Financiera Altamar, January 2026",
         fontsize=8)
fig.savefig(DATA / "spread_desk.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Chart generated:", (DATA / "spread_desk.png").exists())
```

The numerator does not change because the two duplicated rows are applications that sat within policy: 17.90 and 18.40. The denominator does drop, from 30 to 28, and that is why the share climbs from 26.7 % to 28.6 %. Internal control gets the clean-file figure: 8 of 28, because a repeated record is not a repeated application and counting it twice dilutes the problem.

The upper quartile at MC-03 sits at 18.65 %, above the 18.50 limit. That means more than a quarter of what that desk places goes out on the expensive side, and not through isolated cases but through where its whole price distribution is standing.

The operations director is asked to review the pricing process at MC-03, and it is backed by two figures: a spread of 0.6459 points against 0.3430 at MC-04, and 4 of the 8 applications outside the band on the whole floor. The value this file is missing before the cause can be claimed is the amount and the risk profile of each loan: without knowing whether the overprice belongs to higher-risk clients, the desk can be named, the reason cannot.

**Output**

```text
Unclean: 8 of 30 outside policy (26.7%)
Clean:   8 of 28 outside policy (28.6%)
       applications  commission     rate  spread
desk                                            
MC-03             8     12125.0  18.1000  0.6459
MC-01             7      8810.0  17.9857  0.4880
MC-02             7      7060.0  18.0714  0.4348
MC-04             6      4467.0  18.0833  0.3430
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
Chart generated: True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two functions with a docstring and no repeated code | 2 |
| The two shares correct and the numerator and denominator explained | 2 |
| The board sorted by spread is correct | 2 |
| The join audit with its three counts | 1 |
| The chart carries order, band, a title with the finding and the source | 2 |
| The close carries the two figures and names the missing value | 1 |

**Most common mistake**

Reporting the unclean share because «that is what the system gives». 26.7 % against 28.6 % looks like a minor difference, and it is exactly the kind of dilution that makes one desk's problem look like noise across the floor.
