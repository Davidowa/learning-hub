# Exercises · Introduction to Databases · COM112

Fifty-one exercises, three per session, for the Engineering group working through the seventeen weeks of the syllabus. Each week opens with a reading exercise, where you predict what the server will answer before you run it; then comes a writing exercise against a specification that carries its own figures; and it closes with one that ties the day's session to the earlier ones. Difficulty climbs twice, inside the week and along the term, so the recognise exercise of week 12 asks for more work than the integrate exercise of week 4. You hand in one `.sql` file per exercise with the server output pasted exactly as it came out, neither trimmed nor tidied. Everything runs against the schema in the annex, a manufacturing plant with its lines, its machines, its sensors and its spare parts store.

---

## Week 01 · Why a database exists

### 01.1 · Recognise

The assembly line logger exports its readings to a flat file. These are five rows of `readings.csv` from the morning of 2 March:

```
SN-101,2026-03-02 06:00,71.5,C
SN-101,2026-03-02 07:00,74.2,C
SN-101,2026-03-02 07:00,742,C
SN-101,2026-03-02 08:00,,c
SN-101,2026-03-02 09:00,78.9,C
```

There are five failures and not one of them produced a message. The third row repeats the timestamp of the second. That same row carries 742 where sensor SN-101 measures from 0 to 120 degrees. The fourth arrives with no value and with the unit in lower case. The unit repeats on all five rows even though it belongs to the sensor and not to the reading. And the afternoon before, two people saved the file from their own machines, so whoever saved second took the work of the first.

Write, for each failure, which of the five pressures from the session answers it. Then predict, without running anything, what the two SELECT statements of this trace answer against the `reading` table of the annex, which starts with twenty rows:

```sql
START TRANSACTION;
INSERT INTO reading VALUES (21, 6, '2026-03-02 08:00:00', 9.40);
INSERT INTO reading VALUES (22, 6, '2026-03-02 09:00:00', 9.65);
SELECT COUNT(*) AS readings_inside FROM reading;
ROLLBACK;
SELECT COUNT(*) AS readings_after FROM reading;
```

### 01.2 · Apply

Connect to the course server and write `w01_server.sql`, which answers four things in this order.

First the version, the default engine and the server character set, the three of them on a single row, with the columns named `version`, `engine` and `character_set`. Then the whole `sql_mode`, in its own query. Last, a transaction that puts three readings on sensor 3 with timestamps 10:00, 11:00 and 12:00 on 2 March, counts inside the transaction, undoes the work and counts again. The two count columns are called `readings_inside` and `readings_after`.

With the twenty readings of the annex, the first count has to come out at 23 and the second at 20. Paste the literal output under each statement.

### 01.3 · Integrate

Write the declaration that would have caught the flat file of 01.1. The table is called `flat_reading` and has five columns: an integer identifier that is the primary key, the sensor, the timestamp, the value with two decimals, and the unit in four characters. The sensor, the timestamp and the unit do not accept empty. The value does, because a disconnected sensor is a real case. Run `SHOW CREATE TABLE flat_reading` and paste what the server returned, including the parts it wrote by itself.

Then answer with a run and not with an opinion. Of the five failures in 01.1, one is still possible with the table already declared. Say which one. Then show with two counts around a ROLLBACK that this server does know how to withdraw a write, and explain in two lines why that ability does not solve the failure left standing.

---

## Week 02 · Types, elements and classifications

### 02.1 · Recognise

The instructor hands out `workshop.sql`, the script that raises the schema of the tool store. Inside there are three `CREATE TABLE` statements, a view, a trigger, an event and no procedures. The three tables are `tool`, with a primary key and a `code` column declared `NOT NULL UNIQUE`; `loan`, with a primary key and a foreign key to `tool`; and `loan_log`, with a primary key and nothing else.

Before running anything, predict the seven rows the object inventory of the `workshop` schema will return: how many tables, how many views, how many triggers, how many events, how many routines, how many constraints and how many indexes. Constraints are counted over `information_schema.TABLE_CONSTRAINTS` and indexes over `information_schema.STATISTICS`, counting distinct names per table.

The two rows where almost the whole group goes wrong are the last two. Write beside each one which line of the script produced every constraint and every index, including the ones nobody declared.

### 02.2 · Apply

Run `workshop.sql` and check your prediction with the catalogue query. Then create the account `eng_reader` on `localhost`, with a password, and do two things in this order: ask for its privileges before granting it anything, and ask again after giving it `SELECT` over the whole `plant` schema.

The point of the exercise is the two outputs side by side. Explain in one line what the freshly created account already had, before you granted it anything, and why the server wrote that by itself.

### 02.3 · Integrate

In the `plant` schema there is a table called `sample`, declared with three rules the server will defend: the value has to fall between -50 and 500, the sensor plus timestamp pair cannot repeat, and the sensor has to exist in the catalogue. It already carries one row, sensor 1 at 06:00 with 71.50.

Write three INSERT statements, one per rule, each designed to bounce for a different reason. Paste the three complete errors with their number and their SQLSTATE. At the end count the rows of `sample` and show there is still only one.

Then answer in writing: none of the three rejections was raised by an application program. Name the piece that raised them and what each one leans on to know the datum was wrong.

---

## Week 03 · The DBMS and its files

### 03.1 · Recognise

These four outputs come from the same session against the `workshop` schema and answer the same question, «what is in there», from four different heights.

```
A)  loan_id  tool_id  taken_out
    1        1        2026-03-02 07:15:00

B)  @@innodb_page_size   16384
    @@innodb_buffer_pool_size   134217728

C)  TABLE_NAME   TABLE_TYPE   ENGINE
    tool         BASE TABLE   InnoDB
    v_loan_open  VIEW         NULL

D)  SPACE  NAME            FILE_SIZE
    409    workshop/tool   131072
```

Assign each output to the level of the architecture it belongs to and write the statement that produced it. Then answer three questions. Which of the four changes if somebody adds a column to `tool`? Which of the four never mentions `v_loan_open`, and why? Why does the `ENGINE` column of output C come out empty on the second row?

### 03.2 · Apply

On `workshop`, write one query per level and paste the three outputs in order, from the top down. The external level is asked of the view. The conceptual level is asked of the catalogue, and it has to bring the name of the object, its type and its engine. The internal level is asked of three server variables: the data directory, the page size and the pool size.

Then go down one more step and list the files of the schema in `information_schema.INNODB_TABLESPACES`. Explain in one line why the listing has three entries and the catalogue of the conceptual level had four.

### 03.3 · Integrate

Measure the gap. Add up the size on disc of every file of the `workshop` schema and compare it with the size in bytes of the script `workshop.sql`, which is the SQL text that produced all of it. Report both numbers and their ratio.

Then open the optimiser. Run `EXPLAIN` over a query that looks for the loans of tool 3, first without asking for a format and then with `FORMAT=TRADITIONAL`. Paste the two outputs and consult `@@explain_format` to explain why the first one looks nothing like the screenshots in the tutorials.

At the end provoke a syntax error on purpose, writing `SELEC` instead of `SELECT`. Of the five components from the session, say which one raised that error and why the other four never found out about your query.

---

## Week 04 · Entity-relationship model

### 04.1 · Recognise

Five sentences from the maintenance department, each one taken from a real meeting:

1. Every machine belongs to a production line, and a line has several machines.
2. A work order consumes several spare parts, and a spare part is consumed on several orders.
3. A machine has at most one calibration certificate in force, and every certificate belongs to a single machine. There are machines with no certificate.
4. A pump can be mounted inside another machine, and that machine inside another.
5. Every line has a head machine, which also belongs to that same line.

For each sentence write three things: the cardinality, the verb you would name the relationship with, and the physical form it turns into when it stops being a drawing. The possible forms are a foreign key on its own, a foreign key plus UNIQUE, a foreign key pointing at its own table, and a new table whose primary key is the pair.

Number five is the one that splits the group. Say what makes it different from number one.

### 04.2 · Apply

In a new schema called `model`, build two of the five relationships from 04.1.

First the recursive one. A `machine` table with an identifier, a name and a column pointing at its own table, with the foreign key declared. Load three rows that form a chain: the paint booth, the recirculation pump mounted in it, and the impeller mounted in the pump. Show the three and point out which of the three parent columns comes out empty and why it had to accept empty.

Then the many to many one. Tables `work_order`, `part` and the third one that comes out of the relationship, whose primary key is the pair. Run `SHOW CREATE TABLE` over that third table and mark in the output the three things the server wrote without anybody asking for them. At the end insert the same pair twice and paste the error.

### 04.3 · Integrate

The double relationship of sentence 5 cannot be built in one go. Prove it. In a freshly created `model2` schema, first attempt the `CREATE TABLE line` the drawing asks for literally, with `head_machine_id INT NOT NULL` and its foreign key to `machine`. Paste the error.

Then write the version that does run, in three statements, and explain in the comment of each one what concession you made against the drawing. Load the Paint line with its paint booth and leave the head pointing at it.

At the end register a second line, Packing, with not a single machine. Count its machines and check that the server does not complain. Write in two lines which promise of the diagram has just been left with nobody to enforce it.

---

## Week 05 · Normalisation

### 05.1 · Recognise

The reliability department keeps its readings in a single wide table:

```sql
CREATE TABLE wide_reading (
  sensor_id    INT,
  taken_at     DATETIME,
  sensor_unit  VARCHAR(10),
  machine_id   INT,
  machine_name VARCHAR(60),
  machine_area VARCHAR(30),
  value        DECIMAL(7,2),
  PRIMARY KEY (sensor_id, taken_at)
);
```

Write every functional dependency of the table in the form `A → B`, before naming a single normal form. Then mark which of those arrows do not start from the full key and say which normal form each group breaks.

Predict two runs as well. The first one puts in three readings from sensor 103 where the third carries the unit written `mm/seg` instead of `mm/s`; say how many go in and what error comes out. The second one creates a two-column table with no primary key and then repeats the same `CREATE TABLE` with `sql_require_primary_key` switched on; say what happens in each case and what that tells you about whether uniqueness is part of the first normal form.

### 05.2 · Apply

Run the three attacks from the session against the wide table and against a `wide_order` table that keeps the parts of each order in a single cell, with values like `'RF-001, RF-003'`.

The first attack is the list inside the cell: look for the orders that consumed `RF-003` with an equality `WHERE` and report the count. Then find them with `FIND_IN_SET` over the same column and explain in one line what you have just given up using.

The second is the contradiction: put in two readings from sensor 104 where the machine name is written two different ways, `Screw compressor` and `Screw Compressor`. Show both rows together.

The third is the update anomaly: change the area of only one of those two rows and show them again. The same machine has to end up in two areas at once, with no error and no warning.

### 05.3 · Integrate

Repair the model. Three tables where there was one, with the foreign keys that join them and with the same data inside, without losing a single row. Then attempt the three attacks of 05.2 again over the repaired model and explain, attack by attack, whether it is now impossible or whether it simply moved somewhere else.

Add to the repaired model a table `energy_use` with the power in kilowatts, the hours of the order and a third column that is the product of the two, calculated by the server and stored. Put in one order of 15.00 kW over 4.00 hours and show the result. Then try to write that third column by hand with the value 1.00 and paste the error.

Close with one line saying what you have just bought and what you have just paid by splitting the table in three.

---

## Week 06 · From the model to tables and keys

### 06.1 · Recognise

A script `plant_ddl.sql` declares five tables of the plant. `line` has a primary key and its name in `NOT NULL UNIQUE`. `machine` has a primary key, a code in `NOT NULL UNIQUE`, a foreign key to `line`, another to itself, and a `status` column declared `ENUM('running','down','retired') NOT NULL`. `certificate` has a foreign key to `machine` that is also declared `UNIQUE`. `sensor` has a `CHECK (range_min < range_max)`. `reading` has `UNIQUE (sensor_id, taken_at)`, a `CHECK (value BETWEEN -50 AND 500)` and a foreign key to `sensor`.

Predict, for each of these seven attempts, whether it passes or bounces, and with which error number:

1. A reading from sensor 1 with the value 742.00.
2. A reading from sensor 1 with an empty value.
3. A second certificate for machine 1.
4. A sensor whose machine is 77, which does not exist.
5. A machine with the status `'repair'`.
6. An `ALTER TABLE` adding a foreign key towards a column that has a plain index but not a unique one.
7. An `ALTER TABLE` adding a foreign key from a `VARCHAR(10)` column towards an `INT`.

Two of the seven return the same number. Say which two and why the server does not tell them apart.

### 06.2 · Apply

Write the whole script. The five tables of the week 4 model, from an empty base, with the four mapping rules applied and with the constraints the specification in 06.1 describes. Load two lines, two machines, one certificate, one sensor and one reading.

The script has to run twice in a row without you editing it. The creation order is part of what you hand in, and if you need to move it by hand there is a foreign key in the wrong place.

### 06.3 · Integrate

Attack your own script with the seven attempts of 06.1 and paste the seven results. The second one does not fail, and that is the point: the `CHECK` lets the unknown value walk straight through the middle of the range. Close that hole with the statement that fits and prove with a run that it now does bounce, with a different error number.

Then list the indexes of `sensor` and of `reading` from the catalogue. One of the two tables has an index nobody declared and the other does not. Explain where the extra one came from and why on the other table the server did not need to write it.

---

## Week 07 · Data types and DDL

### 07.1 · Recognise

Classify these eight commands into their family, using the one-line question from the session: `TRUNCATE TABLE`, `INSERT`, `GRANT`, `ROLLBACK`, `ALTER TABLE`, `DELETE`, `REVOKE`, `CREATE INDEX`. Beside each one write whether ROLLBACK can undo it.

Then predict the following three runs over a `t_test` table that starts with six rows:

```sql
START TRANSACTION;  TRUNCATE TABLE t_test;         ROLLBACK;  SELECT COUNT(*) FROM t_test;
START TRANSACTION;  CREATE TABLE t_ddl (id INT);   ROLLBACK;  SHOW TABLES LIKE 't_ddl';
START TRANSACTION;  DELETE FROM t_test WHERE id=3; ROLLBACK;  SELECT COUNT(*) FROM t_test;
```

The three carry the same word at the end and the three answer different things. Explain in one line what the two that did not undo have in common.

### 07.2 · Apply

In a `types` schema, declare `sensor` and `reading` choosing the type of every column instead of inheriting it. The sensor tag is always six characters. The quantity is variable-length text. The installation date is a date, not a string. The status is a closed catalogue of three values. The reading value carries two integer digits and two decimals.

Write beside each column, in a comment, the type you chose and the reason in one line. Then provoke these four rejections on purpose and paste the four errors with their number:

1. A date written the way it is said out loud, `'02/03/2026'`.
2. A value of 9999.9 in the two-integer-digit column.
3. A sensor tag of seven characters.
4. A `NULL` in the quantity column.

### 07.3 · Integrate

Three measurements over the same schema, each one against a common belief.

First the ENUM. Sort the sensors by `status` and show `status + 0` beside it. Alphabetically the order would be `down`, `retired`, `running`. Report the one that came out and explain where it comes from.

Second, the pair the source material confuses. `sensor` is the parent of `reading`. Try to empty it with `TRUNCATE` and then to delete one row with `DELETE`, and paste the two errors, which carry different numbers for the same obstacle.

Third, the counter. Over a `stop_log` table with `AUTO_INCREMENT` and no children, load three rows, empty it with `DELETE`, put in a new one and note down its identifier. Repeat the cycle with `TRUNCATE`. The two identifiers are not the same, and that difference is the argument for why `TRUNCATE` is DDL.

Close by storing `'SN-1  '`, with two trailing spaces, in a `CHAR(6)` column and in a `VARCHAR(6)` one, and reading both back with their length.

---

## Week 08 · DML and transactions · First midterm

### 08.1 · Recognise

The `reading` table of the `dml` schema starts with six rows. Predict the five counts of this run, in order:

```sql
START TRANSACTION;
DELETE FROM reading WHERE reading_id = 6;
SAVEPOINT s1;
DELETE FROM reading WHERE reading_id = 5;
ROLLBACK TO SAVEPOINT s1;
ROLLBACK;
```

Then answer two questions without running anything. If instead of the final `ROLLBACK` there were a `COMMIT`, how many rows does the table keep? And if `@@autocommit` were 1 and somebody had removed the `START TRANSACTION`, what would the `ROLLBACK` have answered?

### 08.2 · Apply

Three loads against the `dml` schema, which has a `CHECK` over `reading.value` between -50 and 500.

The first is an `INSERT` of three readings in a single statement, where the middle one carries 742.00. Count before and count after. The two numbers have to be the same, and that is the point: the statement is already atomic without anybody asking for it.

The second is the same load corrected, with the three readings inside the range.

The third takes its rows from a query instead of typing them: register a preventive order dated 2026-04-01 for every machine on line 1, without writing a single identifier by hand. Show the orders that were created.

At the end calculate the hours between stops of each machine, dividing the running hours by the number of stops. One of the machines has zero stops. Run the division first in a `SELECT` and then inside an `INSERT` into an `indicator` table, and paste both outputs, which are not the same.

### 08.3 · Integrate

Review for the first midterm, covering weeks 1 to 8. One script, four parts.

Part one, from the model to the DDL. From the sentence «every sensor belongs to a machine and a machine has several sensors», write the cardinality, its physical form and the `CREATE TABLE` that implements it with the constraint that holds it up.

Part two, the types. Justify in one line why the timestamp cannot stay in `VARCHAR` and why the value cannot stay in `FLOAT`, each one citing an error measured in class.

Part three, the load. Wrap a load of three readings in a transaction, check with a counting `SELECT` before confirming, and confirm. If the count does not add up it is a `ROLLBACK`, never a repair `DELETE`.

Part four, the three conditions. Prove with three separate runs the three situations in which a `ROLLBACK` undoes nothing: with a `CREATE TABLE` slipped between the `INSERT` and the `ROLLBACK`, over an `ENGINE=MyISAM` table, and with no transaction open. Paste the three outputs and say which of the three is the most dangerous, with an argument.

---

## Week 09 · The single-table SELECT

### 09.1 · Recognise

The `machine` table of the annex has eight rows and a `criticality` column that accepts empty. The `reading` table has twenty.

Predict, without running anything, these eight counts:

```sql
SELECT COUNT(*) FROM machine;
SELECT COUNT(*) FROM machine WHERE criticality =  'high';
SELECT COUNT(*) FROM machine WHERE criticality <> 'high';
SELECT COUNT(*) FROM machine WHERE criticality =  NULL;
SELECT COUNT(*) FROM machine WHERE criticality IS NULL;
SELECT COUNT(*) FROM reading;
SELECT COUNT(*) FROM reading WHERE value IS NOT NULL;
SELECT COUNT(*) FROM reading WHERE value IS NULL;
```

The second and the third do not add up to the first. Explain in two lines why, with the name of the third state that answers a condition in SQL.

Then predict how many machines each of these two queries returns, which differ by one pair of brackets:

```sql
SELECT code FROM machine
 WHERE criticality = 'high' OR criticality = 'medium' AND status = 'running';

SELECT code FROM machine
 WHERE (criticality = 'high' OR criticality = 'medium') AND status = 'running';
```

### 09.2 · Apply

Build the machine search screen of the maintenance department, over the `machine` table and without a single JOIN. Five queries.

One, the exact filter by status, which returns the six running machines.

Two, the text box. The plant loaded its asset register from the supplier files, so two names carry diacritics. Search for `kuhn` without the umlaut and find the press. Search for `lindstrom` without the umlaut and find the pump. Search for `hydraulic` in lower case and find the press again. Consult `@@collation_database` and explain in one line why you did not have to write any diacritic handling.

Three, the percentage that is data and not a wildcard. Over `part.description`, search for `50` and then search for `50` followed by a literal percent sign. The first returns three parts and the second returns one.

Four, lists and ranges. Count the machines whose criticality is in `('high','low')` and the ones that are not. Then count the readings with a value between 6.40 and 41.80, with the same limits written with strict greater and less than, and with both limits swapped round. The three numbers are 6, 4 and 0.

Five, the grid. The machines sorted by code, three at a time, page one and page two.

### 09.3 · Integrate

Three quiet errors, each one crossed with an earlier week.

The first crosses with week 7. Sort the sensors by their `channel` column, which is declared `VARCHAR(4)` and holds `1`, `2`, `3`, `9`, `10` and `100`. Paste the order that came out, run `SELECT '10' < '9'` next to `SELECT 10 < 9` to explain it, and write the DDL statement that would fix it at the root.

The second is the alias. Calculate the span of each sensor range as `range_max - range_min`, give it an alias, and use it first in the `WHERE` and then in the `ORDER BY`. Paste the error of the first and the output of the second, and explain the difference with the table of the logical order of the clauses.

The third is sorting with empties. Show the three lowest readings. With a plain ascending sort the empties come out first. Write the version that sends them to the end, without using the standard clause MySQL does not have, and paste as well the error that clause returns so it is on the record.

Close with the missing comma: run `SELECT code, name FROM machine LIMIT 3` and then the same `SELECT` without the comma. Neither of the two gives an error, and the report of the second comes out wrong.

---

## Week 10 · Grouping and aggregates

### 10.1 · Recognise

Over the twenty readings of the annex, predict the complete row this query returns:

```sql
SELECT COUNT(*) AS n, COUNT(value) AS c, AVG(value) AS avg_value,
       MIN(value) AS mn, MAX(value) AS mx
FROM reading;
```

Then predict the three values of this other one, and say which of the two ratios is the real average and which is the one somebody is going to send in a report by mistake:

```sql
SELECT SUM(value) AS total,
       SUM(value)/COUNT(*)     AS over_20,
       SUM(value)/COUNT(value) AS over_15
FROM reading;
```

Close by writing, in one line, how many of the twenty readings the average was calculated with and where the person receiving the report is going to get that figure from.

### 10.2 · Apply

The monthly maintenance report, over the `work_order` table. Five queries.

One, provoke error 1055 on purpose by asking for the folio next to a count grouped by type. Paste the complete error and write the corrected version beside it.

Two, the orders per machine, with four columns: how many there are, how many carry hours captured, the sum of hours and the average. Machine 2 has three orders and only two with hours.

Three, the difference between the two filters. Ask for the machines with more than two orders putting the condition in the `WHERE` and then in the `HAVING`. One of the two fails; paste the error and explain it with the logical order from last week.

Four, the pivot. A matrix with one row per machine and three count columns, one per order type, built with conditional aggregation.

Five, the orders per month. Group by year and month with the month name, sort chronologically, and explain why the name of the month is a server setting and not a property of the date. Then change `lc_time_names` to `es_MX` and ask for a month name again.

### 10.3 · Integrate

The most expensive trap of the session, over the `parent_machine_id` column of the `machine` table, which accepts empty.

Ask how many machines are not the parent of any other, writing the same question two ways: with `NOT IN` over a subquery and with a correlated `NOT EXISTS`. Paste the two counts, which do not agree, and the count of how many `parent_machine_id` are empty, which is what explains the difference. Neither of the two queries gave an error or a warning.

Then write the load of orders per machine with a `WITH`, and ask it for the ones above the average of that same set. Explain in one line what the clause saved you against writing the same grouping twice.

Close by classifying the parts by their reorder point with a `CASE` of four branches, where one branch is for the empty reorder point. Then classify the same thing with an `IF` of two branches. One part has reorder point 0 and another has it empty. Show both outputs and say on which exact row the two versions stop agreeing, and which of the two is wrong.

---

## Week 11 · JOIN, UNION and UNION ALL

### 11.1 · Recognise

There are eight machines and twelve work orders. Predict, without running anything, these four numbers:

1. How many rows `machine INNER JOIN work_order` returns on `machine_id`.
2. How many the same pair returns with `LEFT JOIN`.
3. How many machines come out if you also filter with `WHERE o.work_order_id IS NULL`.
4. For machine 3, which has no orders, what `COUNT(*)` is worth and what `COUNT(o.work_order_id)` is worth on the same row of the grouped result.

The fourth is the one you have to be able to explain. Write in two lines where the row `COUNT(*)` is counting comes from.

### 11.2 · Apply

Three queries over the plant.

One, reassemble what week 5 split apart. Bring the machine code, the sensor tag, the timestamp and the value, joining `reading`, `sensor` and `machine`. Read each `ON` out loud as a sentence before writing it, and leave the sentence in the comment.

Two, the most common error there is. Count the rows of a `LEFT JOIN` of `machine` with `work_order` putting `o.type = 'corrective'` first in the `WHERE` and then in the `ON`. The two numbers are 5 and 9. Explain in two lines why the predicate in the `WHERE` turned your `LEFT JOIN` into an `INNER JOIN`.

Three, the cartesian product. Join `line` with `machine` without writing the `ON` and report how many rows came out. The query is legal and nobody puts their hand up.

### 11.3 · Integrate

The inventory meeting. The central store says it has seven parts in the `part` table. The line system says it has eight in `line_stock`. Nobody knows how many there really are.

First attempt the query that would answer it in one go, with `FULL OUTER JOIN`, and paste the error.

Then build the recipe that does work: a `LEFT JOIN` unioned with a `RIGHT JOIN`. Report the four counts, the one from the `LEFT`, the one from the `RIGHT`, the one for the parts that match and the one for the union, and show the ten rows of the result read in three blocks: the ones on both sides, the ones only in the central store and the ones only on the line. The projection has to bring both codes, the central one and the line one, or two different parts will melt into one.

Close with the cost of three letters. Over `shift_use_a` and `shift_use_b`, count the rows and add up the pieces, first with `UNION ALL` and then with `UNION`. The results are 7 rows with 18 pieces and 4 rows with 9 pieces. Say which of the two numbers is the real consumption of the store and why the other came out without a single warning.

---

## Week 12 · Views

### 12.1 · Recognise

Four views over the `plant` schema:

- `v_reading_full`, an `INNER JOIN` of `reading`, `sensor` and `machine`.
- `v_reading_left`, a `LEFT JOIN` of `sensor` with `reading`.
- `v_sensor_load`, a `COUNT` and an `AVG` grouped by sensor.
- `v_sensor_count`, the sensors with a scalar subquery counting their readings.

Predict for each one what the `IS_UPDATABLE` column of the catalogue will say. Then predict what the server answers to these five attempts:

1. An `UPDATE` of a reading value, which lives in a single base table, through `v_reading_full`.
2. An `UPDATE` touching two base tables in the same statement, also through `v_reading_full`.
3. A `DELETE` through `v_reading_full`.
4. An `UPDATE` through `v_reading_left`.
5. An `UPDATE` through `v_sensor_count`, over a column that is not the calculated one.

One of the five is the disagreement of the term: the catalogue says one thing and the server does another. Say which one and what working rule the group takes away from it.

### 12.2 · Apply

Three layered views over `plant`. The first cleans and renames a single table. The second applies a department rule over the first one, not over the table: the high criticality machines that are running. The third aggregates and flattens, counting machines per line.

Attempt an `UPDATE` through each of the three and paste the three answers. Two pass and one fails; explain in one line why the one that fails could not have done anything else.

Then build the view of the line 1 coordinator and close it. Without `WITH CHECK OPTION`, insert from the view a machine belonging to line 3, look for it in the view and fail to find it, and then look for it in the base table and find it. Create the view again with the clause, repeat the attempt and paste the error.

### 12.3 · Integrate

Three beliefs, three measurements.

First, the asterisk. Create a view with `SELECT *` over `part`, add a column to the base table, and query the view and the table again. Paste both outputs side by side and explain with `SHOW CREATE VIEW` why the view did not see the new column.

Second, the order. Create a view with an `ORDER BY ... DESC` inside. Query it directly and then query it from a `JOIN`. Paste the two orders, which are not the same, and say who the order of a result belongs to.

Third, the speed. Run `EXPLAIN` over `v_reading_full` with no filter. Paste the plan and point out how many times the name of the view appears in it. With that, answer whether saving a query makes it faster.

Close by consulting the `DEFINER` and the `SECURITY_TYPE` of the view you created. Write in two lines who ended up there, whether you asked for it, and in which week that gets charged.

---

## Week 13 · Procedures and errors · Second midterm

### 13.1 · Recognise

This procedure is created without an error and answers wrongly:

```sql
CREATE PROCEDURE sp_bad(IN sensor_id INT)
BEGIN
  SELECT COUNT(*) AS rows_returned FROM reading WHERE sensor_id = sensor_id;
END
```

The `reading` table has twenty rows and sensor 1 has four. Predict what `CALL sp_bad(1)` answers and explain in two lines what the `WHERE` actually compared. Then write the single change that fixes it.

Predict as well which error number comes out of each of these four signals, all of them raised from inside a procedure:

```sql
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Operation not allowed';
SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Integrity violated';
SIGNAL SQLSTATE '22012' SET MESSAGE_TEXT = 'Division by zero';
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Value off the sensor scale', MYSQL_ERRNO = 3001;
```

Three of the four carry the same number. Say which is the only piece your application can use to tell an error of yours from another one.

### 13.2 · Apply

Write `sp_machine_load`, which receives a machine identifier and returns two things: a result on screen with the code, the name, how many orders it has and the sum of its hours, and an output parameter with the number of orders. Inside, reuse the `LEFT JOIN` of week 11 and the grouping of week 10, without changing a line of either.

The script starts with `DROP PROCEDURE IF EXISTS` and uses `DELIMITER`, because you are going to run it twenty times this afternoon. The parameters carry a prefix, and in a comment say what would happen if they did not.

Call it with machine 2, which has three orders and 10.25 hours. Then call it passing the number 5 where the output parameter goes and paste the error. At the end add an `INOUT` parameter that accumulates, initialise it at 100 and show that it came out at 104.

### 13.3 · Integrate

Review for the second midterm, covering weeks 9 to 12, wrapped in today's topic.

Write `sp_two_steps`, which puts in two readings where the second one points at a sensor that does not exist. Count before, call it, paste the error and count after. Show that the first row stayed inside and explain in one line why the error arrived late.

Then write `sp_two_steps_safe`, the version that leaves no half-done work. It carries a named `DECLARE CONDITION`, an `EXIT HANDLER`, a `GET DIAGNOSTICS` recovering the three pieces of the error, a `ROLLBACK` written by you, and an output parameter returning the diagnosis as readable text. Count before and after the call; the two numbers have to be the same.

Write a third version that instead of returning text throws the error again with `RESIGNAL`, with the number 3101 and a message the maintenance office can read.

Close with two lines about `SQLSTATE 23000`: name the three different situations that produce it and say what the handler you have just written catches beyond what it promises.

---

## Week 14 · Triggers and events

### 14.1 · Recognise

Complete the table of the six moments, saying for each one whether `OLD` exists, whether `NEW` exists and whether `NEW` can be written: `BEFORE INSERT`, `AFTER INSERT`, `BEFORE UPDATE`, `AFTER UPDATE`, `BEFORE DELETE`, `AFTER DELETE`.

Then predict three things.

One, what the server answers if you try to create a `BEFORE INSERT` trigger whose body reads `OLD.value`. Say as well at which moment that error appears, on creating it or on firing it.

Two, this validation:

```sql
IF NEW.value < 0 OR NEW.value > 500 THEN
  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Value off the sensor scale';
END IF;
```

Say what happens when a reading of 742.00 arrives and what happens when one with an empty value arrives. Explain the second with the three-valued logic of week 9 and write the guard that closes it.

Three, the same rule written as a declarative constraint instead of as a trigger. Say which error number each of the two produces and how what the user gets to read differs.

### 14.2 · Apply

Over an `auto` schema with `sensor`, `reading` and `reading_log`, install two triggers.

The first validates the value against the scale, with the guard for the empty value in place. Name it with the convention of table, moment, event and purpose, so that a `SHOW TRIGGERS` reads without opening the body. Prove that it rejects 742.00 and that it lets the empty value through.

The second writes the log on `AFTER UPDATE`, leaving the old value and the new one on the same row, together with the action and the timestamp. Change a reading from 71.50 to 68.00 and show the row that was written.

### 14.3 · Integrate

The hole in the log, measured in two runs.

The foreign key of `reading` is declared with `ON DELETE CASCADE` and the table also has a `BEFORE DELETE` trigger that writes the log. Count the readings of sensor 3 and the rows of the log. Delete sensor 3. Count both things again. The reading disappeared and the log did not grow.

Repeat the experiment with `TRUNCATE TABLE reading`. Three readings disappear and the log stays as it was.

Write in three lines what a trigger does see and what it does not, and propose the mechanism that would record both disappearances.

Close with the events. Create one with a date already past, run `SHOW WARNINGS` straight afterwards and look for the event in the catalogue. The `CREATE` gave no error and the event is not there. Then create the recurring one that purges the log every day and show it in the catalogue with its type, its interval and its status.

---

## Week 15 · Indexes and performance

### 15.1 · Recognise

Over `reading_big`, which has 200 000 rows, there is a single secondary index, the composite `(machine_id, taken_at)`. Predict, for these three queries, the value of `type`, of `key` and of `rows` that `EXPLAIN FORMAT=TRADITIONAL` will return:

```sql
SELECT reading_id FROM reading_big WHERE machine_id = 42;
SELECT reading_id FROM reading_big WHERE machine_id = 42 AND taken_at = '2026-01-15';
SELECT reading_id FROM reading_big WHERE taken_at = '2026-01-15';
```

The third is the one that splits the group, because the index appears in `key` and even so it is not doing what it looks like. Explain with the leftmost prefix rule what the server is doing there.

Then predict what happens with a `(shift, value)` index when the query filters only by `value` and `shift` has four distinct values. The answer is not the same as the one for the third query, and the name of what happens does not appear in any source written for 5.7.

### 15.2 · Apply

Measure, index and measure again. The query is this one, over 200 000 readings and 50 000 machines:

```sql
SELECT r.reading_id, e.code
  FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id
 WHERE e.code = 'EQ-000042';
```

With both tables carrying no secondary index at all, save the plan and the time. Then build the two indexes that repair it, one per table, and save the plan and the time again. What you hand in is the comparison, not the opinion: the two plans pasted next to each other, the number of rows examined in each case and the two times.

Before each measurement run the query once without timing it, so that the pool from week 3 does not measure your first trip to disc.

### 15.3 · Integrate

An audit of the inherited advice, in three branches and with evidence.

Over `message`, which has 60 000 rows and a prefix index on `title`, run three searches for the same phrase: anchored at the start with `LIKE 'Shutdown from vibration%'`, with the wildcard at the start, and with `REGEXP '^Shutdown from vibration'`. Paste the three plans with their `type`, their `key` and their rows examined, and give a verdict per branch: it holds, it needs qualifying, or it falls.

Then build the full-text index over `body` and measure two things: what it costs to build and what it buys. Before building it, attempt the query with `MATCH ... AGAINST` and paste the error. Try as well to declare it over a numeric column and paste the other error. Once built, compare the time of `MATCH` against that of `LIKE '%vibration%'` over the same column.

Close with the other side of the bet. Load the same 200 000 rows into two identical tables, one with no secondary indexes and one with eight, and report the two times and the two `DATA_LENGTH` and `INDEX_LENGTH` columns. Write the ratio of each.

---

## Week 16 · Concurrency and locking · Project

### 16.1 · Recognise

Two store counters run the same script over part 3, which has 25 pieces. Each one takes out five.

```sql
START TRANSACTION;
SELECT on_hand INTO @c FROM part WHERE part_id = 3;
-- here the person types for a moment
UPDATE part SET on_hand = @c - 5 WHERE part_id = 3;
COMMIT;
```

Session A read at 00:16:49.594981 and B at 00:16:49.806316. Predict three numbers: what A read, what B read and how many pieces the part is left with at the end. Say how many pieces really left the store and how many the system says left.

Then predict the result of the two repairs, running the same pair of sessions: one that adds `FOR UPDATE` to the read, and one that does not read at all and asks the server to do the subtraction. Both reach the same final number and not by the same road. Explain the difference in two lines.

### 16.2 · Apply

Reproduce the three runs of 16.1 with two real sessions, not with one. Each session prints `NOW(6)` when it reads and when it writes, and you hand in the timestamps of both.

Then measure the distinction that splits the week. With `innodb_lock_wait_timeout` at 3 seconds, set up the case where session B waits for a lock A does not release, and paste the error with the time it took to arrive. Then set up the case where A and B ask each other for what the other one holds, and paste the other error.

The two errors have different consequences and that is where the exercise lives. In the session that received the expired wait, write something on another row before the error and commit after it. In the one that received the deadlock, do the same. Report what survived in each case.

### 16.3 · Integrate

Issuing stock with a stock check, which is the most common design error there is.

Write `sp_issue`, which receives a part and a quantity, reads the stock on hand, decides whether it is enough, and if it is, subtracts it and records the issue. With 25 pieces on part 3, call it from two sessions at once, each one asking for 20. Report what each session saw, the final stock and how many pieces left according to the `issue` table.

Then write `sp_issue_safe`, which differs by a single clause, and repeat the experiment from the same starting state. Report the same three numbers.

Close with the retry. Write `sp_adjust`, which takes one piece off two parts in the order it is told, with a `CONTINUE HANDLER` for `SQLSTATE '40001'`, a `ROLLBACK` inside the handler and a `LOOP` that tries again up to five times. Call it from two sessions with the identifiers in reversed order and report how many attempts each one needed and where the two parts ended up. Both have to end with their two decrements applied.

---

## Week 17 · Users, backup and closing · Final exam

### 17.1 · Recognise

Read this `SHOW GRANTS` output and say which statements will be denied to the account, with the error number of each one:

```
GRANT USAGE ON *.* TO `eng_tutor`@`localhost`
GRANT SELECT (`code`, `description`), UPDATE (`on_hand`)
  ON `plant`.`part` TO `eng_tutor`@`localhost`
```

The four statements to judge are: read code and description from `part`; read code and on_hand; update on_hand; update description. Two of the four bounce, and not with the same number as a missing whole-table permission.

Then read this command and say which objects of the schema will not be in the file it produces:

```
mysqldump -u root -p workshop > workshop.sql
```

The `workshop` schema has three tables, a view, a trigger, an event and a procedure. Say as well what `mysqldump` prints on standard error while it works, and what the last line of a complete file has to be.

### 17.2 · Apply

On the accounts side, four runs.

One, attempt the `GRANT` over an account you did not create and paste the error. Then create it and ask for its privileges before and after granting it read access over `plant`.

Two, open a second window connected as that restricted account and try three things: a read it is allowed, a delete it is not allowed, and a read of `mysql.user`. Paste the two errors.

Three, create the account with column permissions from exercise 17.1 and run from it the four statements you judged. Check your two verdicts.

Four, create a read role, grant it to an account, connect with it and consult `CURRENT_ROLE()` before doing anything. Explain with `@@activate_all_roles_on_login` why the account with a role receives the same error as one without it, and fix it in the session.

On the backup side, produce three files of the `workshop` schema: the one that comes out by default, the complete one, and the one with the schema and no data. Report the three sizes in bytes and how many times `PROCEDURE` and `EVENT` appear in each one.

### 17.3 · Integrate

Final review, crossing the five blocks of the term in a single sequence.

First restore. Take the complete backup, restore it into a new schema and report the exit code and how many lines the client printed. Then check the restore the only way there is: by counting on the other side. The counts of the three tables and the presence of the procedure, the event and the trigger in the catalogue.

Second, restore over a live database. Add a tool, delete a loan and create a table the backup knows nothing about. Restore the same file on top and report what happened to the three things. One of them survives intact; explain why.

Third, the file that lies. Run a `mysqldump` naming a table that does not exist, report the exit code and the size of the file it left, and show its last line. Say what the signal is that the file is no good.

Close with three short paragraphs, one for each thing that outlives the version number. One about `sql_mode`, naming four errors from the term that are only errors because strict mode is switched on. One about `EXPLAIN`, citing a performance claim you measured this term that turned out to be backwards. And one about the contradiction between week 6, which calls the index an added detail, and week 15, which measured it. Settle it with your own measurement, not with the authority of either slide.

---

## Annex · The working database

Every exercise runs against this schema, a manufacturing plant with three lines. It is raised from an empty base and can be run again as many times as needed.

```sql
DROP DATABASE IF EXISTS plant;
CREATE DATABASE plant CHARACTER SET utf8mb4;
USE plant;

CREATE TABLE line (
  line_id INT PRIMARY KEY,
  name    VARCHAR(40) NOT NULL UNIQUE,
  area    VARCHAR(30) NOT NULL
);

CREATE TABLE machine (
  machine_id        INT PRIMARY KEY,
  code              CHAR(7)     NOT NULL UNIQUE,
  name              VARCHAR(60) NOT NULL,
  line_id           INT         NOT NULL,
  parent_machine_id INT         NULL,
  installed_on      DATE        NOT NULL,
  status            ENUM('running','down','retired') NOT NULL,
  criticality       VARCHAR(10) NULL,
  FOREIGN KEY (line_id)           REFERENCES line(line_id),
  FOREIGN KEY (parent_machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE sensor (
  sensor_id  INT PRIMARY KEY,
  tag        CHAR(6)     NOT NULL UNIQUE,
  machine_id INT         NOT NULL,
  quantity   VARCHAR(20) NOT NULL,
  unit       VARCHAR(10) NOT NULL,
  channel    VARCHAR(4)  NOT NULL,
  range_min  DECIMAL(7,2) NOT NULL,
  range_max  DECIMAL(7,2) NOT NULL,
  FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE reading (
  reading_id INT PRIMARY KEY,
  sensor_id  INT      NOT NULL,
  taken_at   DATETIME NOT NULL,
  value      DECIMAL(7,2) NULL,
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);

CREATE TABLE work_order (
  work_order_id INT PRIMARY KEY,
  folio         CHAR(8) NOT NULL UNIQUE,
  machine_id    INT     NOT NULL,
  type          ENUM('preventive','corrective','predictive') NOT NULL,
  shift         ENUM('morning','afternoon','night') NOT NULL,
  done_on       DATE    NOT NULL,
  hours         DECIMAL(5,2) NULL,
  FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE part (
  part_id       INT PRIMARY KEY,
  code          CHAR(6)     NOT NULL UNIQUE,
  description   VARCHAR(60) NOT NULL,
  on_hand       INT NOT NULL,
  reorder_point INT NULL
);

CREATE TABLE part_usage (
  work_order_id INT,
  part_id       INT,
  quantity      INT NOT NULL,
  PRIMARY KEY (work_order_id, part_id),
  FOREIGN KEY (work_order_id) REFERENCES work_order(work_order_id),
  FOREIGN KEY (part_id)       REFERENCES part(part_id)
);

CREATE TABLE certificate (
  certificate_id INT PRIMARY KEY,
  machine_id     INT  NOT NULL UNIQUE,
  folio          CHAR(9) NOT NULL,
  expires_on     DATE NOT NULL,
  FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

INSERT INTO line VALUES
 (1,'Assembly A','Manufacturing'),
 (2,'Paint','Finishing'),
 (3,'Packing','Internal logistics');

INSERT INTO machine VALUES
 (1,'EQ-0001','Hydraulic press 200 t Kühn', 1, NULL,'2019-03-11','running','high'),
 (2,'EQ-0002','Welding robot',              1, NULL,'2020-07-01','running','high'),
 (3,'EQ-0003','Robot gripper',              1, 2,   '2021-02-15','running','medium'),
 (4,'EQ-0004','Screw compressor',           2, NULL,'2018-05-20','down','high'),
 (5,'EQ-0005','Paint booth',                2, NULL,'2019-11-04','running','medium'),
 (6,'EQ-0006','Lindström recirculation pump',2, 5,  '2019-11-04','running','medium'),
 (7,'EQ-0007','Conveyor belt',              3, NULL,'2022-01-10','running','low'),
 (8,'EQ-0008','Stretch wrapper',            3, NULL,'2017-09-30','retired',NULL);

INSERT INTO sensor VALUES
 (1,'SN-101',1,'temperature','C',    '1',   0.00,120.00),
 (2,'SN-102',1,'pressure',   'bar',  '2',   0.00, 10.00),
 (3,'SN-103',2,'vibration',  'mm/s', '9',   0.00, 45.00),
 (4,'SN-104',4,'temperature','C',    '10',  0.00,120.00),
 (5,'SN-105',5,'flow',       'l/min','100', 0.00,250.00),
 (6,'SN-106',7,'vibration',  'mm/s', '3',   0.00, 45.00);

INSERT INTO reading VALUES
 ( 1,1,'2026-03-02 06:00:00', 71.50),
 ( 2,1,'2026-03-02 07:00:00', 74.20),
 ( 3,1,'2026-03-02 08:00:00', NULL),
 ( 4,1,'2026-03-02 09:00:00', 78.90),
 ( 5,2,'2026-03-02 06:00:00',  6.40),
 ( 6,2,'2026-03-02 07:00:00',  6.55),
 ( 7,2,'2026-03-02 08:00:00', NULL),
 ( 8,3,'2026-03-02 06:00:00', 12.30),
 ( 9,3,'2026-03-02 07:00:00', 41.80),
 (10,3,'2026-03-02 08:00:00', 44.90),
 (11,3,'2026-03-02 09:00:00', NULL),
 (12,4,'2026-03-02 06:00:00', 95.10),
 (13,4,'2026-03-02 07:00:00', 98.60),
 (14,4,'2026-03-02 08:00:00', NULL),
 (15,5,'2026-03-02 06:00:00',180.00),
 (16,5,'2026-03-02 07:00:00',176.25),
 (17,5,'2026-03-02 08:00:00',191.40),
 (18,5,'2026-03-02 09:00:00', NULL),
 (19,6,'2026-03-02 06:00:00',  8.75),
 (20,6,'2026-03-02 07:00:00',  9.10);

INSERT INTO work_order VALUES
 ( 1,'OT-26001',1,'preventive','morning',  '2026-01-12', 3.50),
 ( 2,'OT-26002',1,'corrective','night',    '2026-01-28', 6.00),
 ( 3,'OT-26003',2,'preventive','morning',  '2026-02-02', 2.25),
 ( 4,'OT-26004',2,'corrective','afternoon','2026-02-14', 8.00),
 ( 5,'OT-26005',2,'predictive','morning',  '2026-02-20', NULL),
 ( 6,'OT-26006',4,'corrective','night',    '2026-02-25',12.00),
 ( 7,'OT-26007',4,'corrective','night',    '2026-03-01', 9.50),
 ( 8,'OT-26008',5,'preventive','morning',  '2026-01-15', 4.00),
 ( 9,'OT-26009',5,'preventive','afternoon','2026-02-16', 4.25),
 (10,'OT-26010',6,'corrective','morning',  '2026-02-27', 5.00),
 (11,'OT-26011',7,'preventive','morning',  '2026-01-20', 1.75),
 (12,'OT-26012',7,'predictive','afternoon','2026-03-03', NULL);

INSERT INTO part VALUES
 (1,'RF-001','Air filter 50% efficiency',       12, 4),
 (2,'RF-002','Oil filter 50 micron',             3, 4),
 (3,'RF-003','Deep groove ball bearing 50 mm',  25, 8),
 (4,'RF-004','Timing belt 1200 mm',              0, 2),
 (5,'RF-005','Viton gasket',                    40, 0),
 (6,'RF-006','Hydraulic hose 3/8',               7, NULL),
 (7,'RF-007','Solenoid valve 24 V',              2, 3);

INSERT INTO part_usage VALUES
 ( 1,1,2),( 1,3,4),( 2,6,1),( 2,3,2),( 3,1,1),
 ( 4,3,6),( 4,7,1),( 6,2,2),( 6,6,3),( 7,7,1),
 ( 8,1,2),( 8,5,4),( 9,5,2),(10,4,1),(11,3,2);

INSERT INTO certificate VALUES
 (1,1,'CAL-24001','2026-06-30'),
 (2,4,'CAL-24002','2026-04-15'),
 (3,5,'CAL-24003','2026-09-01');
```

Eight machines, six sensors, twenty readings of which five arrive with no value, twelve work orders and seven spare parts. Machine 8 is retired and it is the only one with no criticality. Machines 3 and 6 are subassemblies mounted inside another machine. Sensors 3 and 6 measure the same quantity on different machines, and no sensor was left without readings. Two machine names carry diacritics, because the asset register was loaded from the supplier files, and exercise 09.2 lives off that.

The schemas `workshop`, `model`, `norm`, `plant_ddl`, `types`, `dml`, `auto`, `perf` and `conc` are built by each exercise where they are needed, and their scripts come inside the statement that asks for them.
