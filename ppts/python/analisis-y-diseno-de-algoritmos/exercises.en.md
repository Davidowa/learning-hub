# Exercises · Analysis and Design of Algorithms · COM101

This set runs alongside the seventeen sessions of the course and is written for the first-semester Engineering group. Every week carries three exercises: Recognise is answered by reading code and predicting what it prints, Apply asks for a program written against a specification that already states its data and its expected result, and Integrate ties the topic of the week back to the weeks before it. Difficulty climbs inside each week and across the term, so the Recognise of week 12 asks for more than the Integrate of week 4. Every problem happens in the same place: the origination floor at Financiera Altamar, its four credit desks MC-01 to MC-04, the payroll loans they place, and the batch where internal control reviews the price of every authorised application. Hand in one `.py` file per exercise through Blackboard, except where the statement asks for paper, with the output exactly as your program produced it.

The pricing band on the product is the same all term: 18.00 % policy rate a year, 17.50 % lower limit, 18.50 % upper limit. Both limits are written as constants at the top of the program and never worked out inside a condition.

---

## Week 01 · Course introduction and the bridge from Excel to Python

### 01.1 · Recognise

**Six weeks at desk MC-01**

Desk MC-01 places payroll loans. These are the applications it approved over the six weeks of the last period, in two paired lists. Without running anything, write the four lines this program prints.

```python
weeks = ["W01", "W02", "W03", "W04", "W05", "W06"]
approved = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(approved)
average = total / len(approved)
best = weeks[approved.index(max(approved))]

print(weeks[0], approved[0])
print(total)
print(average)
print(best)
```

Then answer two things. Which week `approved[3]` belongs to, and which row that value would sit on in the spreadsheet it came from, if row 1 holds the headers. And what happens if you add `print(approved[6])` at the end of the program.

### 01.2 · Apply

**The period summary, formatted**

Write the program that summarises those same six weeks and prints four aligned lines: applications approved over the period with a thousands separator, average per week to one decimal, the best week with its figure, and how far above the average that week finished.

The figures it has to give are 7,990 applications for the period, 1,331.7 on average, and week W04 with 1,510, which sits 178.3 applications above the average. No number gets typed by hand inside a `print`: all four come out of the two lists.

### 01.3 · Integrate

**The value that got captured again**

Internal control reports that week W03 was captured wrong. Not 1120 applications but 1320. Fix the value in your 01.2 program, run it again, and report the three new figures next to the old ones.

The program also prints the reference number of the batch under review, `00847`, held in a text variable.

Then answer three things, one line each. What would have happened with that change in a spreadsheet, and which of the four breaking points from the session explains the difference. What shows in the cell if somebody captures that reference with a number format. And which of the four breaking points that one is about.

---

## Week 02 · Unit 1 · Algorithm design

### 02.1 · Recognise

**Tracing the pricing verdict**

Payroll loans go out at a policy rate of 18.00 % a year, and the authorised band runs from 17.50 to 18.50 %. This is the pseudocode internal control follows for every authorised application that reaches it.

```text
START
    READ rate

    IF rate > 18.50 THEN
        verdict = "Overpriced outside policy"
    ELSE IF rate < 17.50 THEN
        verdict = "Discounted outside policy"
    ELSE
        verdict = "Within policy"

    WRITE verdict
END
```

Write the full trace for three applications: one at 18.80 %, one at 17.40 %, and one at exactly 18.50 %. On each one note which conditions were evaluated, which were never read, and the verdict it ends on.

The desk officer then reorders the branches like this and claims the algorithm does the same thing.

```text
IF rate >= 17.50 THEN
    verdict = "Within policy"
ELSE IF rate > 18.50 THEN
    verdict = "Overpriced outside policy"
ELSE
    verdict = "Discounted outside policy"
```

Trace the 18.80 % application against this second version and say which verdict it leaves with. Explain in two lines why this version satisfies the five properties of an algorithm and still cannot be used on the batch review.

### 02.2 · Apply

**Releasing the disbursement, on paper**

Write the algorithm for the check that runs before a payroll loan is disbursed, in pseudocode and as a flowchart. The sequence checks three things in this order: that the file is complete, that the client carries no past-due balance, and that the bureau score reaches at least 620. If all three hold, release the disbursement. If any one fails, name the one that failed and leave the application on hold.

Hand in the pseudocode in the words of the course, the flowchart with the four symbols, and the expected trace of two cases: complete file, no past-due balance and a score of 688; and complete file, no past-due balance and a score of 601. No computer.

### 02.3 · Integrate

**An instruction that is not an algorithm**

The email going round the desk reads: «if the application came out too expensive, send it to committee».

Run the two-person test on it and explain in two lines which of the five properties breaks and why. Then rewrite it as an algorithm, with the 17.50 to 18.50 % band and three outputs: pricing committee if the rate came out high, cancel on margin if it came out low, and disburse if it sits inside.

Write down which values are the input and what the output is. Add at the end one edge case your first version did not cover, and say what you had to change to cover it.

---

## Week 03 · Units 1 and 2 · Paradigms and an introduction to programming

### 03.1 · Recognise

**Three lines that overwrite each other and four files that will not run**

First, the trace. Write what `applications` holds after each line and what the program prints.

```python
applications = 1240
applications = applications + 85
applications = applications * 2

print(applications)
```

Then four fragments, each saved in its own file. For each one say whether it runs. When it does not, say which of the five rules from the session was broken, which kind of error is raised, and on which line Python complains about it.

```python
# A
amounts = [96500, 148200]
print(Sum(amounts))

# B
amounts = [96500, 148200]
print("average:, amounts)

# C
total = 96500 + 148200
print(total

# D
total = 244700
Print(total)
```

### 03.2 · Apply

**The first program of the desk**

Desk MC-01 authorised five loans on 8 January: 96,500, 148,200, 73,400, 151,100 and 118,900 pesos. Write a program with the full anatomy from the session: a comment at the top saying where the data came from, the import of `mean` from `statistics`, the list of amounts, and three `print` calls showing how many loans there are, the average amount and the largest amount, each one with its label.

The average comes to 117,620 pesos and the largest amount to 151,100 pesos.

Then break your own program three ways, one at a time: remove the bracket that closes a `print`, change `print` to `Print`, and delete a quotation mark. Hand in a three-row table with the exact message each one gave, the line it pointed at included.

### 03.3 · Integrate

**The week 2 pseudocode, said in Python**

Translate the pricing verdict pseudocode from 02.1 into Python, with the rate held in a variable at the top of the program and the result printed with its label. The translation is almost line for line: five words change and the colons appear.

Run it three times, with 18.50, with 17.40 and with 18.00, and paste the three outputs. Answer two more things: why the 18.00 run prints `18.0` and not `18.00`, and what verdict an application at 18.80 % would get if you swapped the first two branches.

---

## Week 04 · Unit 3 · Data, data types and primitive operations

### 04.1 · Recognise

**Eight lines of bundle arithmetic**

Applications are split into bundles of 24 for the document review. Without running anything, write the eight lines this program prints.

```python
applications = 1240
per_bundle = 24

print(applications / per_bundle)
print(applications // per_bundle)
print(applications % per_bundle)
print("18" + "50")
print(int("18") + int("50"))
print(18.00 + 0.50 == 18.50)
print(0.05 * 3 == 0.15)
print(0.05 * 3)
```

Then answer two things. What the second and third results mean, in bundles and in applications. And why the sixth line gives one answer and the seventh gives the opposite, when both of them add rate adjustments that come out exact on paper.

### 04.2 · Apply

**The MC-01 batch, every value in its own type**

Desk MC-01 closed the batch of 8 January 2026 with 1240 applications received, 37 rejected and 86.4 analyst-hours spent. The desk stayed active and logged no incident.

Declare eight variables with the type each value deserves, the active-desk flag and the last incident included, which does not exist. Work out the reject rate as a percentage and the analyst-hours per application, rounded to two and to four decimals. Print both metrics with their label and their unit, and then the `type` of five variables to check what Python understood.

The reject rate comes to 2.98 % and the hours per application to 0.0697. No variable name may be a single letter.

### 04.3 · Integrate

**Two brackets that change the answer**

With the same MC-01 data, somebody wants to know how much analyst time each approved application costs and writes this.

```python
per_application = analyst_hours / applications - rejected
```

Write both versions, the one above and the one that actually answers the question, print both rounded to four decimals, and say in one line what each one works out. One gives a negative number and the other gives 0.0718 hours per approved application.

Solve two more things in the same program. How many full bundles of 24 come out of the approved applications and how many are left loose, with integer division and remainder. And what happens to the batch reference, `"00847"`, when you convert it to an integer and back to text: print the three values on one line and explain in one line what got lost on the way.

---

## Week 05 · Unit 4 · Statements, input and output

### 05.1 · Recognise

**Seven lines of formatting**

Without running anything, write exactly what each line prints, commas, decimals and spaces included.

```python
applications = 1240
hours = 86.4
rate = 37 / 1240

print(f"Applications: {applications:,}")
print(f"Hours: {hours:,.2f} h")
print(f"Reject: {rate:.1%}")
print(f"Reject: {rate:.2%}")
print(f"{'MC-01':<10}{applications:>8}")
print(f"Raw rate: {rate}")
print("Hours: {hours:.2f} h")
```

Then explain in one line why the third and fourth lines show the same value with two different figures, and in another what the last line is missing to do what it looks like it does.

### 05.2 · Apply

**Capturing the batch**

Write the program that captures a batch from the keyboard and returns the desk report. Ask for four values, each with its own prompt: the desk, the applications received, the applications rejected and the analyst-hours in the batch. Convert whatever needs converting before you work with it.

The report is five labelled lines: desk, applications with a thousands separator, rejected, reject rate to two decimals of a percentage, and hours per application to four decimals.

Test it with MC-01, 1240, 37 and 86.4. It has to give 2.98 % and 0.0697 h. Hand in the full session, with what you typed on the same line as the prompt.

### 05.3 · Integrate

**The report that goes up to sales management**

Extend the previous program so that it also works out the time per application and the analysis minutes per approved application. The desk shift runs eight hours, that is 28800 seconds, and that constant goes at the top of the program with a name. Time per application is the shift divided by the applications received. Minutes per approved application are the analyst-hours turned into minutes and shared across the applications that were not rejected.

The five figures in the report line up in a column, name on the left in twenty-two spaces and number on the right in ten, each with its own format and its unit.

Test it with MC-03, 1512 applications, 68 rejected and 112.8 analyst-hours. It has to give 1,444 approved applications, a 4.50 % reject rate, 19.05 seconds per application and 4.69 minutes per approved application. Hand in the full session.

---

## Week 06 · Unit 4.4 · Selection structures

### 06.1 · Recognise

**The application that lands right on the limit**

Two programs, each with a different application. Without running anything, say what each one prints and why.

```python
# First
rate = 18.50

if rate > 18.50:
    verdict = "Overpriced outside policy"
else:
    verdict = "Within policy"

print(rate, verdict)
```

```python
# Second
rate = 18.80

if rate >= 17.50:
    verdict = "Within policy"
elif rate > 18.50:
    verdict = "Overpriced outside policy"
else:
    verdict = "Discounted outside policy"

print(rate, verdict)
```

The second program passes an application placed at 18.80 %, thirty basis points above the upper limit. Explain in two lines why the second branch is never reached and write the correct order of the three conditions.

### 06.2 · Apply

**The pricing classifier for the batch**

Write the program that asks from the keyboard for an application reference and the rate it was granted, and gives it one of three verdicts: overpriced outside policy above 18.50 %, discounted outside policy below 17.50 %, and within policy in every other case. Both limits go at the top of the program as named constants.

The output is a single line with the reference, the rate to two decimals and the verdict.

Test five applications and hand in all five runs: 18.60, 17.40, 18.50, 17.50 and 18.00. The two that land exactly on a limit have to come out within policy.

### 06.3 · Integrate

**Five destinations and one impossible value**

Sales management decides three categories are not enough. An overprice can be authorised in committee as long as it does not pass 19.50 %; above that the product stops being sellable and the application is cancelled. A discount can be authorised with management sign-off as long as it does not drop below 16.50 %; below that the loan no longer covers its funding cost and it is cancelled on margin.

Write the five-category classifier with those five destinations, plus a check that rejects an impossible value before classifying anything: any rate at or below zero, or above 60 %, comes out as an invalid value and gets sent back for capture review. All five boundaries go in as named constants.

Test these eleven rates and hand in the full table: 20.00, 19.50, 18.60, 18.50, 18.00, 17.50, 17.20, 16.50, 16.20, -3.00 and 75.00. Close with a five-row table documenting which verdict the exact value of each boundary gets and why you chose `>` or `>=` on each one.

---

## Week 07 · Unit 4.4 · Nested selection and logical operators

### 07.1 · Recognise

**Four conditions that do not say what they look like**

Without running anything, write the five lines this program prints and explain each one in a line.

```python
desk = "MC-03"

if desk == "MC-01" or "MC-03":
    print("Critical desk")
else:
    print("Normal desk")

rates_a = [18.10, 17.80, 18.60]
rates_b = [18.10, 17.80, 18.60]

print(rates_a == rates_b)
print(rates_a is rates_b)

applications = 0
rejected = 0

if applications > 0 and rejected / applications > 0.03:
    print("Block the desk")
else:
    print("Not enough data")

last_incident = None
print(last_incident is None)
```

Answer two more things. What the first condition would print if the desk were MC-04, and how it is written correctly. And why the `and` in the third condition avoids a `ZeroDivisionError` that `or` would have blown up on.

### 07.2 · Apply

**The release policy for a batch**

A batch is released when three things hold at once: the desk is not under audit, the batch carries at least 500 applications, and the reject rate does not pass 3 %. If it is not released, there are two paths: if the desk is one of the critical ones, which are MC-01 and MC-03, it is held and flagged as a critical desk that missed the rule; if not, it is held for a file-by-file review.

Write the program that asks from the keyboard for the desk, the applications in the batch, the rejected ones and whether it is under audit, and decides. The list of critical desks and both thresholds go in as constants at the top. Membership is asked with `in`, not with a row of `or`.

Test these five cases and hand in all five runs: MC-01 with 1240 and 37 not under audit; MC-03 with 1512 and 68 not under audit; MC-04 with 760 and 9 not under audit; MC-02 with 420 and 5 not under audit; and MC-01 with 1240 and 37 under audit.

### 07.3 · Integrate

**The nesting that was really an and**

The automatic desk-blocking rule arrived from the origination system vendor written like this, with four branches.

```python
if delinquency > 3.0:
    if overprice > 0.50:
        action = "Block the desk"
    else:
        action = "Keep placing"
else:
    if overprice > 0.50:
        action = "Keep placing"
    else:
        action = "Keep placing"
```

Write a program that asks from the keyboard for the delinquency on the desk portfolio as a percentage and its average overprice in rate points, works out the action with that nested version and with the version collapsed into a single condition, and prints both alongside a `True` or `False` saying whether they agree.

Run the four cases of the truth table and hand in the four outputs: 4.2 with 0.80; 4.2 with 0.30; 2.4 with 0.80; and 2.4 with 0.30.

Close with two lines. The first explains why this nesting could be collapsed. The second describes a case from the same floor where the nesting cannot be collapsed, and says what its inner branches have to look like for that to happen.

---

## Week 08 · Unit 4.5 · Repetition · First midterm

### 08.1 · Recognise

**A for that steps by six and a budget that runs out**

Without running anything, write everything this program prints and how many lines that is.

```python
for term in range(12, 48, 6):
    print(term)

budget = 50000.0
weekly_spend = 7500.0
weeks = 0

while budget > 0:
    budget -= weekly_spend
    weeks += 1

print(weeks, budget)
```

Then answer three things. Why the `for` does not print 48 even though it shows up in the `range`. How many full weeks the promotion budget really covers and why the printed number is not that one. And what would happen if you deleted the line that subtracts the spend.

### 08.2 · Apply

**The four desks, in a single pass**

These are the figures from the batch of 8 January, in four paired lists.

```python
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
applications = [1240, 984, 1512, 760]
rejected = [37, 12, 68, 9]
hours = [86.4, 61.5, 112.8, 48.2]
```

Write the program that walks them once and produces the batch table: a header and one row per desk with the desk, the applications with a thousands separator, the reject rate to two decimals of a percentage and the analyst-hours per application to four decimals, all lined up in columns.

The last row is the whole floor, with 4,496 applications, a 2.80 % reject rate and 0.0687 hours per application. That row is worked out by adding and dividing the totals, not by averaging the four rates.

The loop has to keep working if a fifth desk is added to the four lists tomorrow, without touching a single line inside it.

### 08.3 · Integrate

**First midterm review: batch C-2601 in full**

This exercise crosses everything the midterm covers: types, formatting, selection and repetition. These are the twelve applications in batch C-2601 with the rate each one was granted.

```python
applications = ["APP-1001", "APP-1002", "APP-1003", "APP-1004",
                "APP-1005", "APP-1006", "APP-1007", "APP-1008",
                "APP-1009", "APP-1010", "APP-1011", "APP-1012"]
rates = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]
```

Write the program that walks the two paired lists and prints one row per application with its reference, its rate to two decimals and its verdict, using the three categories from week 6 and the constants of the band.

When the pass ends, print two more lines: the average rate of the batch to four decimals, and how many of the twelve applications came out outside policy, with the percentage to one decimal. The average comes to 18.0750 % and 3 of 12 come out.

Close by answering in two lines why application APP-1008, placed at 18.50 %, does not count as outside policy, and what would have happened to that count if the program used `>=` instead of `>` in the first condition.

---

## Week 09 · Unit 4.5 · Accumulators, flags and nested loops

### 09.1 · Recognise

**An accumulator that wipes itself and a search that leaves early**

Two programs. Without running anything, say what each one prints.

```python
# First
hours = [86.4, 61.5, 112.8, 48.2]

for hour in hours:
    total = 0.0
    total += hour

print(total)
```

```python
# Second
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
applications = [1240, 984, 1512, 760]
rejected = [37, 12, 68, 9]

for i in range(len(desks)):
    if applications[i] < 1000:
        continue

    if rejected[i] / applications[i] > 0.03:
        print("First out of control:", desks[i])
        break
else:
    print("No desk goes over the limit")
```

On the first one, say what the expected result was, what comes out, and which single line has to move. On the second one, write the trace of the four passes saying what happens on each, and explain why the `else` on the `for` does not run and in which case it would.

### 09.2 · Apply

**Three questions, one single pass**

With the four lists from the batch in 08.2, write the program that answers three different questions inside one `for`, with all three variables declared before the loop.

How many analyst-hours the whole floor spent, which is an accumulator. How many desks went past the 3 % reject target, which is a counter. And whether there is at least one desk spending more than 0.070 hours per application, which is a flag.

The three answers are printed with a label: 308.9 hours, 1 desk off target and the flag on `True`. Both targets go in as named constants.

Close by explaining in one line why the second question cannot be answered with an accumulator and the first cannot be answered with a counter.

### 09.3 · Integrate

**The capacity projection, desk by shift**

Planning wants the decision capacity of each desk on each of the three service shifts of the day. These are the decision-engine speeds and the durations.

```python
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
applications_per_hour = [155, 123, 189, 95]
shifts = ["T1", "T2", "T3"]
hours = [8, 8, 6]
```

Write the program with two nested loops that prints one row per combination, with the desk, the shift and the projection with a thousands separator, lined up. Before you run it, write in your notebook how many rows should come out; if it does not match what the program prints, the nesting is wrong.

When it finishes, print two summary lines: the projected capacity of the floor, which comes to 12,364 applications, and how many combinations pass 1000 applications, which is 5.

The two loop variables have to be named differently and say what they walk. Close by explaining in two lines how many passes this program would make if the lender had 40 desks and 3 shifts, and at what size you would start worrying.

---

## Week 10 · Unit 5 · User-defined functions

### 10.1 · Recognise

**A function that works it out and hands back nothing**

Without running anything, say what each of the three final lines of this program prints.

```python
def reject_rate(applications, rejected):
    rejected / applications


def minutes_per_application(hours, applications):
    per_unit = hours * 60 / applications
    return per_unit


print(reject_rate(1240, 37))
print(minutes_per_application(86.4, 1240))
print(per_unit)
```

Then answer three things, one line each. What the first function is missing, and why the error does not show up inside it but wherever somebody uses its result. Why the third line fails even though `per_unit` really was worked out. And what would happen if the second function had `print(per_unit)` instead of `return per_unit`.

### 10.2 · Apply

**Two batch calculations, packaged**

Write two functions with a one-line docstring each. The first, `reject_rate(applications, rejected)`, returns the share of applications turned down. The second, `within_policy(rate)`, returns true or false against the 17.50 to 18.50 % band, which lives in two constants outside the function.

Neither of them may print anything. They only take values and give values back.

Test them with six calls and paste the output: the rate for MC-01 with 1240 and 37, the one for MC-03 with 1512 and 68, the one for a batch of 760 applications with no rejections at all, and the policy check on 18.00, on 18.50 and on 18.60. The three rates rounded to four decimals come to 0.0298, 0.045 and 0.0.

Close by explaining in one line why 18.50 is the case that always has to be tested and what would have happened if the function used `<` instead of `<=`.

### 10.3 · Integrate

**Batch C-2601, solved with functions**

Solve exercise 08.3 again, this time with four functions and without repeating a single condition.

`within_policy(rate)` answers whether the application sits inside the band. `verdict(rate)` returns within policy, overpriced or discounted, and calls the first one from inside instead of comparing again. `applications_in_policy(rates)` counts how many rates in a list fall inside. `average_rate(rates)` returns the mean.

None of the functions prints. The main program walks the twelve applications, prints the row for each one and closes with three lines: reviewed, within policy and average rate. It comes to 12 reviewed, 9 within policy and 18.0750 %.

Close with two lines. Delete the comparison against the lower limit from the body of `within_policy` and say which of your four tests catches it; if none of them catches it, add the one that is missing and say so.

---

## Week 11 · Unit 5 · Arguments, built-in functions and modules

### 11.1 · Recognise

**The argument that landed in the wrong slot**

Without running anything, write the three numbers this program prints, rounded to two decimals, and say which parameter the 5.0 reached on each call.

```python
def minutes_per_application(hours, applications, factor=60, extras=0.0):
    return hours * factor / applications + extras


print(minutes_per_application(86.4, 1240))
print(minutes_per_application(86.4, 1240, 5.0))
print(minutes_per_application(86.4, 1240, extras=5.0))
```

The second call returns a number that looks nothing like the other two. Explain in two lines what happened, why Python flagged no error at all, and what would happen to the definition if you moved `factor=60` ahead of `applications`.

### 11.2 · Apply

**A function that works for more than one product**

The floor also places car loans at a policy rate of 14.00 % with the same band, and now and then runs a campaign with an open band of 1.00 point. Write `outside_policy(rate, policy=18.00, band=0.50)`, with its docstring, working out both limits inside and returning true when the application falls outside.

Test it with five calls: 18.60 with the defaults; 18.50 with the defaults; 18.60 with policy and band given by position; 18.60 passing only the band by name; and 14.20 passing only the policy rate by name.

Add two lines at the end that check, before you trust the function, that `18.00 - 0.50` gives exactly 17.50 and that `18.00 + 0.50` gives exactly 18.50. Explain in one line why that check is not wasted effort, even though both come out true here.

### 11.3 · Integrate

**What the batch average does not say**

With the twelve rates from batch C-2601, write the program that imports `mean`, `median` and a third function from the `statistics` module that we did not cover in class, one that measures how spread out the granted rates are. Look that third function up on docs.python.org and cite the page.

The program prints seven lines: number of applications, mean, median and spread to four decimals, the lowest and the highest rate to two, and the capability index, which is the width of the policy band divided by six times the spread. It gives 18.0750 for the mean, 18.0500 for the median, 0.4065 for the spread and an index of 0.41.

At the end, repeat the mean and the median over a list of thirteen values, the same one plus a rate of 27.00 % that somebody captured by typing the term into the rate field. One of the two numbers moves much further than the other.

Close with three lines: what a capability index of 0.41 means for the pricing policy, what you would tell the sales director with that figure, and which of the two measures of centre you would report when you suspect a bad capture.

---

## Week 12 · Unit 6 · Lists and tuples

### 12.1 · Recognise

**A method that sorts and wipes the backup**

Without running anything, write the seven lines this program prints and what happens on the last one.

```python
rates = [18.10, 17.80, 18.60, 18.00, 17.40]

print(rates[0], rates[-1])
print(rates[1:3])
print(sorted(rates))
print(rates)

ordered = rates.sort()
print(ordered)
print(rates)

backup = rates
copy = rates.copy()
rates.append(19.00)

print(len(backup), len(copy))
print(rates[6])
```

Answer three more things. Why `rates[1:3]` gives back two values and not three. Why `backup` and `copy` end up with a different number of elements, when both were created at the same moment. And what would have happened to the data if instead of `ordered = rates.sort()` somebody wrote `rates = rates.sort()`.

### 12.2 · Apply

**Four questions about the rate column**

With the twelve rates from batch C-2601, write the program that prints the list at the start, answers four questions and prints the list again at the end, which has to come out identical.

The highest and the lowest rate. The three highest rates, sorted from highest to lowest. Which position the 17.40 rate sits in and which reference it belongs to, given that the first application is APP-1001. And the last three rates in the batch, with a slice.

The three highest are 18.80, 18.60 and 18.50. The 17.40 rate sits in position 4 and belongs to application APP-1005.

### 12.3 · Integrate

**The applications outside the band, without touching the original**

Write the program that walks the twelve rates and builds a new list with the ones that fall outside the band, without modifying the original list. Then sort it from highest to lowest and print it.

The band goes in a three-value tuple, `(18.00, 17.50, 18.50)`, which is policy rate, lower limit and upper limit. Every comparison reads that tuple by position.

The report is five lines: the band with its three figures, how many applications were reviewed, how many fell outside, the list of the ones that fell outside sorted from highest to lowest, and the full original list to prove it came through untouched. It comes to 3 of 12, and the outside-the-band list is 18.80, 18.60 and 17.40.

Close with a line that tries to change the upper limit of the tuple to 19.00 and paste the full error it raises. Explain in one line why it suits the band to live in a tuple and not in a list.

---

## Week 13 · Unit 6 · Sets and dictionaries · Second midterm

### 13.1 · Recognise

**A catalogue that grows and a reason that does not exist**

Without running anything, write the eight lines this program prints and what happens on the last one.

```python
reasons = {"M01": "Bureau score too low",
           "M02": "Payment capacity exceeded",
           "M03": "Incomplete documentation"}

reasons["M02"] = "Payment capacity above 35 %"
reasons["M04"] = "Not enough time in the job"

print(len(reasons))
print(reasons["M02"])
print(reasons.get("M09"))
print(reasons.get("M09", "Reason not in the catalogue"))

batch_a = {"M01", "M02", "M01", "M03"}
batch_b = {"M02", "M03", "M05"}

print(len(batch_a))
print(sorted(batch_a & batch_b))
print(sorted(batch_a - batch_b))
print(sorted(batch_a ^ batch_b))
print(reasons["M09"])
```

Answer two more things. Why the dictionary ends up with four entries when two codes were assigned to it after it was created. And why `batch_a` holds three elements when the list it came from carries four.

### 13.2 · Apply

**The rejection reason catalogue**

Build the dictionary of the six reason codes the floor works with: M01 bureau score too low, M02 payment capacity above 35 %, M03 incomplete documentation, M04 not enough time in the job, M05 income cannot be verified, and M06 client already has an active loan.

The batch reported these eight codes, in this order: M01, M03, M01, M05, M01, M02, M03 and M09.

Write the program that prints the full catalogue walking it with `items`, then three labelled figures (reasons in the catalogue, rejections reported and distinct reasons reported), and at the end the sorted list of the distinct reasons, each one with its description.

Looking up the description has to use `get` with a default, because M09 is not in the catalogue and the program cannot stop there. It comes to 6 reasons in the catalogue, 8 rejections reported and 5 distinct reasons.

### 13.3 · Integrate

**Second midterm review: the batch board**

This exercise crosses everything the midterm covers: repetition, functions and collections. The data are these.

```python
desks = ["MC-01", "MC-02", "MC-03", "MC-04"]
hours = [86.4, 61.5, 112.8, 48.2]
applications = [1240, 984, 1512, 760]

reported_a = ["M01", "M03", "M01", "M05", "M01", "M02", "M03"]
reported_b = ["M02", "M02", "M06", "M03", "M01"]
```

First, build the dictionary that goes from desk to analyst-hours with a loop. It does not get typed by hand. Print it with `items`, get the total from `values` and find the costliest desk by walking the dictionary, not by eye. The total comes to 308.9 hours and the costliest desk is MC-03 with 112.8.

Second, count how many times each reason from batch A shows up using a dictionary as a counter, with `get` and a default of zero. Print it sorted by code.

Third, compare the reasons in the two batches with set operations, never with a loop and an `if`: the ones that showed up in both, the ones only in batch A, the ones that turned up new in batch B, and the ones in one but not in both.

Close with two lines: what origination decision you would take on the reason that turned up new in batch B, and why the count for batch A could not have been done with a set.

---

## Week 14 · Unit 7 · Text and CSV files

### 14.1 · Recognise

**What a CSV gives back, and of what type**

The four weeks that are left all work on the same file. Create it under the name `applications.csv`, saved in the same folder as your programs and encoded in UTF-8. It holds 30 rows of authorised applications from Financiera Altamar, exported exactly as they came out of the origination system, across three days of operation and three batches.

```text
date,desk,batch,rate_pct,resp_hours,commission_mxn
2026-01-08,MC-01,C-2601,18.10,44,"$1,240"
2026-01-08,MC-02,C-2601,17.80,39,$980
2026-01-08, MC-01,C-2601,18.60,46,"$1,310"
2026-01-08,MC-03,C-2601,18.00,51,"$1,505"
2026-01-08,mc-01,C-2601,17.40,,"$1,190"
2026-01-08,MC-04,C-2601,18.30,38,$760
2026-01-09,MC-01,C-2602,17.90,45,"$1,260"
2026-01-09,MC-02,C-2602,18.50,41,"$1,020"
2026-01-09,MC-03,C-2602,18.80,52,"$1,540"
2026-01-09,MC-01 ,C-2602,18.20,43,"$1,225"
2026-01-09,MC-04,C-2602,17.60,,$745
2026-01-09,MC-03,C-2602,17.70,50,"$1,480"
2026-01-12,MC-01,C-2603,18.40,44,"$1,255"
2026-01-12,mc-02,C-2603,18.70,40,"$1,005"
2026-01-12,MC-03,C-2603,17.50,49,"$1,460"
2026-01-12,MC-04,C-2603,18.00,37,$735
2026-01-12,MC-01,C-2603,17.30,47,"$1,330"
2026-01-12,MC-02,C-2603,18.10,,$995
2026-01-08,MC-02,C-2601,18.20,40,"$1,010"
2026-01-08,MC-03,C-2601,18.90,53,"$1,575"
2026-01-09,MC-01,C-2602,17.90,45,"$1,260"
2026-01-09,MC-04,C-2602,18.30,39,$755
2026-01-12,MC-03,C-2603,18.20,48,"$1,435"
2026-01-12,MC-04,C-2603,17.80,38,$742
2026-01-08,MC-04,C-2601,18.50,37,$730
2026-01-09,MC-02,C-2602,17.50,42,"$1,035"
2026-01-12,MC-01,C-2603,18.40,44,"$1,255"
2026-01-08,MC-03 ,C-2601,17.10,54,"$1,610"
2026-01-09,MC-03,C-2602,18.60,51,"$1,520"
2026-01-12,MC-02,C-2603,17.70,41,"$1,015"
```

Without running anything, write the six lines this program prints.

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent

with (DATA / "applications.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(len(rows))
print(rows[0]["desk"], rows[0]["rate_pct"])
print(type(rows[0]["rate_pct"]))
print(rows[0]["rate_pct"] + rows[1]["rate_pct"])
print(rows[4]["resp_hours"] == "")
print(rows[2]["desk"] == "MC-01")
```

Then answer three things, one line each. Why the fourth line raises no error at all despite adding things up wrong. Why the sixth line comes out false when that row says MC-01 in the file. And what would happen to the file if that same open call carried `"w"` instead of the default mode.

### 14.2 · Apply

**The summary by desk, reading by column name**

Write the program that reads `applications.csv` with `DictReader` and produces the batch summary. You need three short functions, each with its docstring: one that turns the commission into a decimal by stripping the peso sign and the thousands comma, one that turns the response hours into an integer and reports a missing value as `None` when the cell comes in empty, and one that normalises the desk name by trimming the ends and leaving a single spelling.

The program first prints four diagnostic lines: rows read, rows with no response hours, distinct spellings of the desk, and desks left after normalising. There are 30 rows, 3 with no response hours, and the 9 spellings come down to 4 desks.

Then it prints the table by desk, sorted by name, with applications authorised, total commission in pesos and average rate to four decimals, plus the row for the whole floor. With the file exactly as it comes, the floor adds up to 34,977 pesos of commission across 30 applications.

Paths are built from the location of the file, never typed by hand.

### 14.3 · Integrate

**Clean it, decide, and write the output file**

Now the same file gets processed with internal control criteria and the result is saved.

The program drops the rows that are exact duplicates by comparing the whole row and not a single column, normalises the desk, converts the commission, and marks each application as outside policy when its rate falls outside the band. Rows that carry no response hours are kept, because their rate was captured and that is the variable that decides whether the price complies; the program reports how many they are and leaves the decision written down.

It prints six log figures: 30 rows in the file, 2 exact duplicates removed, 28 rows left, 3 rows kept with no response hours, 8 applications outside policy and 32,462 pesos of floor commission.

Then it writes a new file called `desk_summary.csv`, with the header `desk,applications,outside_policy,commission_mxn` and one row per desk sorted by name. Writing a CSV on Windows means passing the parameter that avoids the blank row between records. At the end the program prints the contents of the file it has just written.

That commission is 2,515 pesos lower than the one from the previous exercise. Explain in two lines where the exact difference comes from and why a duplicate inflates the commission but barely moves the average rate.

---

## Week 15 · Unit 8.1 · Series, DataFrame, cleaning and grouping

### 15.1 · Recognise

**What pandas inferred from the file, and why**

Without running anything, say what each of the seven statements in this program prints, running over the same `applications.csv`.

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

applications = pd.read_csv(DATA / "applications.csv")

print(applications.shape)
print(applications.dtypes)
print(applications["resp_hours"].isna().sum())
print(applications.duplicated().sum())
print(applications["desk"].nunique())
print(applications["desk"].value_counts())
print(applications["rate_pct"].describe().round(3))
```

Then answer four things, one line each. Why `resp_hours` came out decimal and not integer, when every response time in the file is a round number. Why `commission_mxn` came out as text. Why two rows in the `value_counts` output look identical and are still separate entries. And which columns `describe` summarises and which it leaves out.

### 15.2 · Apply

**The four repairs, with their log**

Write the program that loads `applications.csv` with pandas and leaves it ready to analyse, printing the count before and after each repair.

The order is this: report the initial state, drop duplicates, normalise the desk with text methods, strip the peso sign and the thousands comma off the commission and convert it to a decimal, and convert the date to a date type. Print the types of all six columns when you are done.

The numbers it has to report are 30 rows on load, 2 duplicates, 9 spellings of the desk, 3 rows with no response hours, 28 rows without duplicates and 4 real desks.

Then add the `verdict` column, which holds "Within policy" everywhere and "Outside policy" wherever the rate falls outside the band, written in a single step with `loc`. It comes to 20 within and 8 outside.

Close with four more figures: how many MC-03 applications came out outside policy, which is 4; how many applications belong to MC-01 or MC-02, which is 14 and gets asked with `isin`; the total commission, which comes to 32,462 pesos; and the average response hours, which come to 44.36. Report as well how many rows you would be left with if you dropped the three without response hours, and explain in two lines why keeping them suits this file.

Combined conditions use the symbols and their brackets, never the words.

### 15.3 · Integrate

**The floor board, the grid by batch and the audited join**

Wrap all the cleaning from 15.2 into a `load_clean()` function with its docstring, so it does not have to be written again for the rest of the term.

First, group by desk and ask for four summaries in a single statement: applications authorised, commission, average response hours and average rate, rounded to three decimals and sorted by commission from highest to lowest. MC-03 leads with 12,125 pesos across 8 applications.

Second, print how many outside-policy applications each desk contributed. Look at how many rows that table carries and explain in one line why it is not four.

Third, build the grid of desk against batch with the commission summed, filling with zero where there is no record and adding the row and column totals. The most profitable cell is batch C-2601 at MC-03 with 4,690 pesos and the grand total comes to 32,462.

Fourth, build this catalogue as a DataFrame from a dictionary of columns and join it to the board.

```python
catalogue = pd.DataFrame({
    "desk": ["MC-01", "MC-02", "MC-03", "MC-04", "MC-05"],
    "city": ["Monterrey", "Guadalajara", "Leon", "Puebla", "Merida"],
    "target_hours": [42, 40, 48, 36, 30],
})
```

Audit the join in both directions before trusting it. It has to give 28 rows on both sides, 1 from the catalogue alone and 0 from the applications alone. Explain in two lines what each of those three numbers means for the lender.

Close with the response-time gap board: desk, city, applications, actual hours, target hours and gap as a fraction, rounded to three decimals. MC-01 runs 6.7 % above its target and MC-02 only 1.2 %. Write in two lines what you would report to the operations director with those figures.

---

## Week 16 · Unit 8.2 · Visualisation with matplotlib and seaborn

### 16.1 · Recognise

**The bar that says average when the subject line says total**

Somebody on the desk built this chart from the already-clean file and emailed it out with the subject line «commission on the batch by desk».

```python
sns.barplot(data=applications, x="desk", y="commission_mxn", ax=ax)
```

Without running anything, answer what number each bar is showing, what that bar is worth for MC-01 and what it would be worth if it showed what the subject line says, and what would have to be added to the call for it to show the total.

Then write the short program that prints the three tables backing your answer: the sum, the average and the count of commission by desk; the mean, the spread, the minimum and the maximum of the rate by desk, sorted by spread; and how many outside-policy applications each one contributed.

Close by choosing the right chart for each of these four questions, with one line of justification each.

- How the commission of the four desks compares.
- How the granted rates are spread inside each desk.
- How the average rate of the floor moved across the three days.
- Whether the applications that take longest to decide are also the ones that fall furthest outside the pricing band.

### 16.2 · Apply

**The floor commission, in a chart that travels on its own**

With the clean file, group the commission by desk and produce a bar chart saved as `commission_desk.png` at 150 dots per inch.

The chart carries five things: a title stating the finding and not the names of the axes, the vertical axis label with its unit, the vertical axis starting at zero, the vertical axis formatted in thousands so nobody has to count digits, and the source at the foot. The bar for the peak desk goes in strong blue and the other three in light blue.

MC-03 holds 37.4 % of the floor commission with 12,125 pesos, and that percentage is worked out inside the program, not typed by hand into the title.

The program prints the series by desk and one line proving the file was generated. Close the figure when you are done.

Write as well the alternative text for the chart, two or three lines, where every figure you mention can be checked against the printed series.

### 16.3 · Integrate

**Three seaborn charts and the story they tell together**

Set the seaborn theme once at the top and produce three images from the clean file.

The first is a bar chart of commission by desk, with the right estimator and without the error bar it draws by default. It is saved as `commission_bars.png`.

The second is a box plot of the granted rates by desk, with the desks ordered by spread from lowest to highest and two dashed horizontal lines at 17.50 and 18.50 marking the band. It is saved as `box_desk.png`.

The third is a heatmap of the desk against batch grid, with the commission in thousands of pesos, the value written inside each cell and one decimal. It is saved as `heatmap_desk_batch.png`.

All three carry a title stating the finding. The program prints the table of mean, median, spread and count of the rate by desk sorted by spread, and the grid in thousands.

In that table, MC-01 has the mean closest to the policy rate of the four desks and is still the second that falls outside the band most often. Write in three lines the conclusion that comes out of putting the three charts together, with at least three checkable figures, and say which of the three you would send to the operations director if you could only send one.

---

## Week 17 · Review and final exam

### 17.1 · Recognise

**The six expensive mistakes, all in the same file**

This program runs from start to finish and produces six results. Five of them are wrong.

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

applications = pd.read_csv(DATA / "applications.csv")

averages = applications.groupby("desk")["rate_pct"].mean()
print(len(averages))

applications[applications["desk"] == "MC-03"]["verdict"] = "Review"
print("verdict" in applications.columns)

rates = [18.10, 17.80, 18.60]
rates = rates.sort()
print(rates)

for hour in [86.4, 61.5, 112.8, 48.2]:
    total = 0.0
    total += hour
print(total)

print(applications["commission_mxn"][0] + applications["commission_mxn"][1])

print(applications["rate_pct"][1])
```

Without running anything, write the six lines it prints and, for each one, name the mistake from the list built up over the term, say what the correct result was, and explain in one line why the program did not stop. The last line prints a number that really does exist in the file and still answers the wrong question; say which question it was.

### 17.2 · Apply

**From file to finding, in a single run**

Write the program that goes from the raw file to a conclusion, in this order and without skipping a step: inspect, clean, group and conclude.

The inspection prints four figures: rows, duplicates, spellings of the desk and rows with no response hours. The cleaning drops duplicates, normalises the desk, converts the commission and marks the verdict on every application.

The board by desk carries six columns: applications, commission, average rate, spread, outside-policy applications and share outside policy, sorted by commission from highest to lowest. The outside-policy column has to hold zero on the desk that contributed none, not sit empty.

The last line is the conclusion, and it is assembled inside the program from the board, not typed by hand: which desk carries the highest share, what percentage of the floor commission it leaves and what percentage of the outside-policy applications it holds. It comes to 37.4 % of the commission and 50 % of the applications outside.

### 17.3 · Integrate

**The close: cleaning changes the answer, and you have to be able to say by how much**

Wrap the cleaning into `load_clean()` and the verdict marking into its own function, both with docstrings.

First, report the share of outside-policy applications on the unclean file and on the clean file: 8 of 30 against 8 of 28. Explain in two lines why the numerator does not change and the denominator does, and which of the two figures you would report to internal control.

Second, print the board by desk with applications, commission, average rate and spread, sorted by spread from highest to lowest.

Third, audit the join against the five-desk catalogue from 15.3 and report the three indicator counts.

Fourth, produce a single box plot of the rates by desk, ordered by spread, with the two band lines, a title stating the finding and the source at the foot, saved as `spread_desk.png`.

The checkable finding is that MC-03 is the only desk whose upper quartile, 18.65 %, clears the 18.50 % limit. Close with three lines: what you would ask the operations director for, which two figures back it up, and which value this file is missing before you could claim the cause.
