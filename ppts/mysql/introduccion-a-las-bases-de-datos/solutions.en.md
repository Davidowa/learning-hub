# Solutions · Introduction to Databases · COM112

The fifty-one solutions were run against MySQL 9.7.2 with the course factory `sql_mode` (`ONLY_FULL_GROUP_BY`, `STRICT_TRANS_TABLES`, `NO_ZERO_IN_DATE`, `NO_ZERO_DATE`, `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ENGINE_SUBSTITUTION`), InnoDB engine, collation `utf8mb4_0900_ai_ci`. Every output in this file is what the server returned, copied without editing. The times and the sizes on disc get measured again in the classroom and will come out close, not identical.

---

## Week 01 · Why a database exists

### 01.1 · Recognise

**Solution**

```sql
-- Where the five failures belong
-- 1. Repeated timestamp .................... Protect
--    Nobody refuses the row that breaks the rule.
-- 2. 742 degrees on a sensor of 0 to 120 ... Protect
--    Same pressure, same cause: nobody checks the domain.
-- 3. Missing value and lower case unit ..... Organise
--    No declared type, so the file accepts anything.
-- 4. The unit repeated on all five rows .... Relate
--    The unit belongs to the sensor and gets copied onto every reading.
-- 5. Two people save and the last one wins . Administer
--    And searching 8.6 million rows ........ Handle volume

-- The prediction for the trace
START TRANSACTION;
INSERT INTO reading VALUES (21, 6, '2026-03-02 08:00:00', 9.40);
INSERT INTO reading VALUES (22, 6, '2026-03-02 09:00:00', 9.65);
SELECT COUNT(*) AS readings_inside FROM reading;   -- 22
ROLLBACK;
SELECT COUNT(*) AS readings_after FROM reading;    -- 20
```

**Output**

```
readings_inside
22
readings_after
20
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five failures are each assigned to one pressure | 4 |
| The two that land on Protect are told apart from the one on Organise | 2 |
| The two predicted counts are 22 and 20 | 3 |
| The answer says the transaction did see its own rows before the ROLLBACK | 1 |

**Most common mistake**

Predicting 20 for the first count, on the belief that the row does not exist until the COMMIT; it gives itself away because then the ROLLBACK would have nothing to undo.

### 01.2 · Apply

**Solution**

```sql
USE plant;

SELECT VERSION() AS version,
       @@default_storage_engine AS engine,
       @@character_set_server   AS character_set;

SELECT @@sql_mode AS mode;

START TRANSACTION;
INSERT INTO reading VALUES (21, 3, '2026-03-02 10:00:00', 39.20);
INSERT INTO reading VALUES (22, 3, '2026-03-02 11:00:00', 40.05);
INSERT INTO reading VALUES (23, 3, '2026-03-02 12:00:00', 43.70);
SELECT COUNT(*) AS readings_inside FROM reading;
ROLLBACK;
SELECT COUNT(*) AS readings_after FROM reading;
```

**Output**

```
version	engine	character_set
9.7.2	InnoDB	utf8mb4
mode
ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
readings_inside
23
readings_after
20
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three server readings come out on one row with the aliases asked for | 3 |
| The whole `sql_mode` appears in its own query | 2 |
| The transaction leaves 23 inside and 20 after | 4 |
| The output is pasted literally, with no trimming of the `sql_mode` | 1 |

**Most common mistake**

Pasting the `sql_mode` cut back to the first two values; it gives itself away because `STRICT_TRANS_TABLES` is missing, and that is the one producing four of the errors of the term.

### 01.3 · Integrate

**Solution**

```sql
USE plant;

CREATE TABLE flat_reading (
  reading_id INT          PRIMARY KEY,
  sensor_id  INT          NOT NULL,
  taken_at   DATETIME     NOT NULL,
  value      DECIMAL(7,2) NULL,
  unit       CHAR(4)      NOT NULL
);
SHOW CREATE TABLE flat_reading;

-- The failure still standing is number 5: two people writing at once.
-- No column of this declaration touches it.
START TRANSACTION;
INSERT INTO flat_reading VALUES (1, 1, '2026-03-02 07:00:00', 742.00, 'C');
SELECT COUNT(*) AS inside FROM flat_reading;
ROLLBACK;
SELECT COUNT(*) AS after_rollback FROM flat_reading;
```

**Output**

```
Table	Create Table
flat_reading	CREATE TABLE `flat_reading` (
  `reading_id` int NOT NULL,
  `sensor_id` int NOT NULL,
  `taken_at` datetime NOT NULL,
  `value` decimal(7,2) DEFAULT NULL,
  `unit` char(4) NOT NULL,
  PRIMARY KEY (`reading_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
inside
1
after_rollback
0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five columns with their type, and only `value` accepts empty | 3 |
| `SHOW CREATE TABLE` pasted, including the engine and the collation the server wrote by itself | 2 |
| Failure 5, the one with the two people, is identified as the one left standing | 3 |
| The two counts around the ROLLBACK, and the explanation of why that does not solve it | 2 |

**Most common mistake**

Declaring `value` as `NOT NULL` so that «none of them go missing»; it gives itself away because then a disconnected sensor brings down the whole load instead of recording the absence.

---

## Week 02 · Types, elements and classifications

### 02.1 · Recognise

**Solution**

```sql
-- Prediction, row by row
-- TABLE               3   tool, loan, loan_log
-- VIEW                1   v_loan_open
-- TRIGGER             1   trg_loan_after_insert_log
-- EVENT               1   ev_purge_log
-- PROCEDURE/FUNCTION  0   the script declares none
-- CONSTRAINT          5   3 PRIMARY KEY + 1 UNIQUE + 1 FOREIGN KEY
-- INDEX               5   3 PRIMARY + 1 from the UNIQUE + 1 the FK wrote

SELECT 'TABLE' AS object, COUNT(*) AS n
  FROM information_schema.TABLES
 WHERE TABLE_SCHEMA = 'workshop' AND TABLE_TYPE = 'BASE TABLE'
UNION ALL
SELECT 'VIEW', COUNT(*) FROM information_schema.VIEWS
 WHERE TABLE_SCHEMA = 'workshop'
UNION ALL
SELECT 'TRIGGER', COUNT(*) FROM information_schema.TRIGGERS
 WHERE TRIGGER_SCHEMA = 'workshop'
UNION ALL
SELECT 'EVENT', COUNT(*) FROM information_schema.EVENTS
 WHERE EVENT_SCHEMA = 'workshop'
UNION ALL
SELECT 'PROCEDURE/FUNCTION', COUNT(*) FROM information_schema.ROUTINES
 WHERE ROUTINE_SCHEMA = 'workshop'
UNION ALL
SELECT 'CONSTRAINT', COUNT(*) FROM information_schema.TABLE_CONSTRAINTS
 WHERE TABLE_SCHEMA = 'workshop'
UNION ALL
SELECT 'INDEX', COUNT(DISTINCT CONCAT(TABLE_NAME, '.', INDEX_NAME))
  FROM information_schema.STATISTICS
 WHERE TABLE_SCHEMA = 'workshop';

SELECT TABLE_NAME, CONSTRAINT_NAME, CONSTRAINT_TYPE
  FROM information_schema.TABLE_CONSTRAINTS
 WHERE TABLE_SCHEMA = 'workshop'
 ORDER BY TABLE_NAME, CONSTRAINT_NAME;
```

**Output**

```
object	n
TABLE	3
VIEW	1
TRIGGER	1
EVENT	1
PROCEDURE/FUNCTION	0
CONSTRAINT	5
INDEX	5
TABLE_NAME	CONSTRAINT_NAME	CONSTRAINT_TYPE
loan	loan_ibfk_1	FOREIGN KEY
loan	PRIMARY	PRIMARY KEY
loan_log	PRIMARY	PRIMARY KEY
tool	code	UNIQUE
tool	PRIMARY	PRIMARY KEY
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The first five rows (3, 1, 1, 1, 0) | 3 |
| The constraint count is 5 and it is broken down by where each one came from | 3 |
| The index count is 5 | 2 |
| The foreign key index is named as the one nobody declared | 2 |

**Most common mistake**

Counting 3 indexes, one per table; it gives itself away because it forgets that a `UNIQUE` and a `FOREIGN KEY` each bring an index as a gift.

### 02.2 · Apply

**Solution**

```sql
CREATE USER 'eng_reader'@'localhost' IDENTIFIED BY 'Plant2026!';
SHOW GRANTS FOR 'eng_reader'@'localhost';

GRANT SELECT ON plant.* TO 'eng_reader'@'localhost';
SHOW GRANTS FOR 'eng_reader'@'localhost';
```

**Output**

```
Grants for eng_reader@localhost
GRANT USAGE ON *.* TO `eng_reader`@`localhost`
Grants for eng_reader@localhost
GRANT USAGE ON *.* TO `eng_reader`@`localhost`
GRANT SELECT ON `plant`.* TO `eng_reader`@`localhost`
```

The freshly created account already carried `USAGE`, which is not a permission but the right to connect without being able to touch anything. The server wrote it by itself, on creating the account.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The account is created with a password and an explicit host | 3 |
| The two `SHOW GRANTS` appear, before and after the `GRANT` | 4 |
| The answer explains that `USAGE` is the right to connect and nothing else | 3 |

**Most common mistake**

Writing `CREATE USER 'eng_reader'` with no host and assuming that creates a universal account; it gives itself away because the server registers it as `'eng_reader'@'%'`, which is a different account from the `localhost` one.

### 02.3 · Integrate

**Solution**

```sql
USE plant;
-- Rule 1: the domain of the value
INSERT INTO sample VALUES (2, 1, '2026-03-02 07:00:00', 742.00);
-- Rule 2: the sensor plus timestamp pair
INSERT INTO sample VALUES (3, 1, '2026-03-02 06:00:00',  72.10);
-- Rule 3: the sensor has to exist
INSERT INTO sample VALUES (4, 99,'2026-03-02 07:00:00',  72.10);

SELECT COUNT(*) AS rows_in_sample FROM sample;
```

**Output**

```
ERROR 3819 (HY000) at line 3: Check constraint 'ck_sample_value' is violated.
ERROR 1062 (23000) at line 5: Duplicate entry '1-2026-03-02 06:00:00' for key 'sample.uq_sample_sensor_time'
ERROR 1452 (23000) at line 7: Cannot add or update a child row: a foreign key constraint fails (`plant`.`sample`, CONSTRAINT `fk_sample_sensor` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))
rows_in_sample
1
```

The three rejections were raised by the manager, with no application program connected. The first leans on the `CHECK`, the second on the unique index over the pair and the third on the existence of the parent row.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three INSERT statements bounce, each one on a different rule | 4 |
| The three errors are pasted with their number and their SQLSTATE | 3 |
| The final count shows the table did not change | 1 |
| The manager is named as the piece that raised all three | 2 |

**Most common mistake**

Writing the second INSERT with a repeated `sample_id` instead of a repeated pair; it gives itself away because the error names `PRIMARY` and not `uq_sample_sensor_time`, so it tested a different rule.

---

## Week 03 · The DBMS and its files

### 03.1 · Recognise

**Solution**

```sql
-- A) External level.    SELECT * FROM v_loan_open;
-- B) Internal level.    SELECT @@innodb_page_size; SELECT @@innodb_buffer_pool_size;
-- C) Conceptual level.  SELECT TABLE_NAME, TABLE_TYPE, ENGINE
--                         FROM information_schema.TABLES WHERE TABLE_SCHEMA='workshop';
-- D) The floor.         SELECT SPACE, NAME, FILE_SIZE
--                         FROM information_schema.INNODB_TABLESPACES
--                        WHERE NAME LIKE 'workshop/%';

-- If somebody adds a column to tool, C changes. A does not, because the view
-- names its columns. B does not either, because the page still measures 16 KB.
-- D never mentions the view because a view has no file: it stores no rows.
-- ENGINE comes out empty on the second row of C for that same reason.
```

**Output**

```
TABLE_NAME	TABLE_TYPE	ENGINE
loan	BASE TABLE	InnoDB
loan_log	BASE TABLE	InnoDB
tool	BASE TABLE	InnoDB
v_loan_open	VIEW	NULL
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four outputs are assigned to their level | 4 |
| Each assignment brings the statement that produced it | 2 |
| C is identified as the only one that changes when a column is added | 2 |
| The empty `ENGINE` and the absence of the view in D are explained by the same reason | 2 |

**Most common mistake**

Putting the view on the conceptual level because «it appears in the catalogue»; it gives itself away because the catalogue lists it too, and what defines the external level is who queries it, not where it is registered.

### 03.2 · Apply

**Solution**

```sql
USE workshop;

-- External level
SELECT * FROM v_loan_open;

-- Conceptual level
SELECT TABLE_NAME, TABLE_TYPE, ENGINE
  FROM information_schema.TABLES
 WHERE TABLE_SCHEMA = 'workshop'
 ORDER BY TABLE_TYPE, TABLE_NAME;

-- Internal level
SELECT @@datadir AS where_the_bytes_live;
SELECT @@innodb_page_size        AS page_size,
       @@innodb_buffer_pool_size AS buffer_manager;

-- The floor
SELECT SPACE, NAME, FILE_SIZE
  FROM information_schema.INNODB_TABLESPACES
 WHERE NAME LIKE 'workshop/%'
 ORDER BY NAME;
```

**Output**

```
loan_id	tool_id	taken_out
1	1	2026-03-02 07:15:00
2	3	2026-03-02 08:40:00
TABLE_NAME	TABLE_TYPE	ENGINE
loan	BASE TABLE	InnoDB
loan_log	BASE TABLE	InnoDB
tool	BASE TABLE	InnoDB
v_loan_open	VIEW	NULL
where_the_bytes_live
...\scratchpad\mydb\data\
page_size	buffer_manager
16384	134217728
SPACE	NAME	FILE_SIZE
410	workshop/loan	131072
411	workshop/loan_log	114688
409	workshop/tool	131072
```

The listing has three entries and the catalogue had four because `v_loan_open` has no file. A view stores logic, not rows.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| One query per level, in order, each with its output | 5 |
| The conceptual level brings the object type and the engine | 2 |
| The file listing appears and brings the three sizes | 1 |
| The difference between three and four is explained | 2 |

**Most common mistake**

Switching database halfway through, so the file listing no longer matches the catalogue; it gives itself away because the names in the `NAME` column carry a different schema prefix.

### 03.3 · Integrate

**Solution**

```sql
USE workshop;
SELECT SUM(FILE_SIZE) AS bytes_on_disc
  FROM information_schema.INNODB_TABLESPACES
 WHERE NAME LIKE 'workshop/%';

SELECT @@explain_format AS default_format;
EXPLAIN SELECT loan_id, taken_out FROM loan WHERE tool_id = 3;
EXPLAIN FORMAT=TRADITIONAL
SELECT loan_id, taken_out FROM loan WHERE tool_id = 3;

SELEC loan_id FROM loan;
```

**Output**

```
bytes_on_disc
376832
default_format
TREE
EXPLAIN
-> Index lookup on loan using tool_id (tool_id = 3)  (cost=0.35 rows=1)

id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	loan	NULL	ref	tool_id	tool_id	4	const	1	100.00	NULL
ERROR 1064 (42000) at line 11: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELEC loan_id FROM loan' at line 1
```

And from the terminal, `wc -c workshop.sql`:

```
1171 workshop.sql
```

376 832 bytes on disc against 1 171 bytes of SQL text. The ratio is 322. That difference is structure, not waste.

Error 1064 was raised by the parser. The optimiser, the executor, the file manager and the buffer manager never found out, because the string never became a statement.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two numbers of the gap and their ratio | 3 |
| The two `EXPLAIN` outputs pasted, with `@@explain_format` to explain the difference | 3 |
| The 1064 provoked and pasted literally | 2 |
| The 1064 is attributed to the parser and the other four are said not to have taken part | 2 |

**Most common mistake**

Comparing the size on disc against the number of data rows instead of against the text of the script; it gives itself away because the ratio comes out in bytes per row, which is not what the gap measures.

---

## Week 04 · Entity-relationship model

### 04.1 · Recognise

**Solution**

```sql
-- 1. Machine belongs to Line ............... 1:N
--    Foreign key on the many side, in machine.
-- 2. Work order consumes Part .............. N:M
--    New table, primary key of the pair (work_order_id, part_id).
-- 3. Machine has Certificate ............... 0:1
--    Foreign key in certificate, plus UNIQUE. It accepts machines with none.
-- 4. Machine is mounted in Machine ......... recursive 1:N
--    Foreign key to its own table, and the column accepts empty for the root.
-- 5. Line has a head machine ............... double relationship
--    Two lines between the same two entities, running opposite ways:
--    machine.line_id points at line, and line.head_machine_id points at machine.
--    It looks symmetric and it is not. Number 1 is one line of the drawing;
--    number 5 is two, and together they form a cycle no CREATE TABLE resolves
--    in one go.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five cardinalities correct | 3 |
| The five verbs, each one readable out loud as a sentence | 2 |
| The five physical forms | 3 |
| The answer explains that number 5 is two relationships and that they form a cycle | 2 |

**Most common mistake**

Marking number 3 as 1:1 instead of 0:1; it gives itself away because the sentence says «there are machines with no certificate», and that is what decides whether the foreign key accepts empty.

### 04.2 · Apply

**Solution**

```sql
CREATE DATABASE model CHARACTER SET utf8mb4;
USE model;

CREATE TABLE machine (
  machine_id        INT PRIMARY KEY,
  name              VARCHAR(60) NOT NULL,
  parent_machine_id INT NULL,
  FOREIGN KEY (parent_machine_id) REFERENCES machine(machine_id)
);
INSERT INTO machine VALUES (1,'Paint booth', NULL);
INSERT INTO machine VALUES (2,'Recirculation pump', 1);
INSERT INTO machine VALUES (3,'Pump impeller', 2);
SELECT machine_id, name, parent_machine_id FROM machine;

CREATE TABLE work_order (
  work_order_id INT PRIMARY KEY,
  folio         CHAR(8) NOT NULL,
  machine_id    INT NOT NULL,
  FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);
CREATE TABLE part (
  part_id     INT PRIMARY KEY,
  description VARCHAR(60) NOT NULL
);
CREATE TABLE part_usage (
  work_order_id INT,
  part_id       INT,
  quantity      INT NOT NULL,
  PRIMARY KEY (work_order_id, part_id),
  FOREIGN KEY (work_order_id) REFERENCES work_order(work_order_id),
  FOREIGN KEY (part_id)       REFERENCES part(part_id)
);
INSERT INTO work_order VALUES (1,'OT-26001',1);
INSERT INTO part       VALUES (1,'Deep groove ball bearing 50 mm');
INSERT INTO part_usage VALUES (1,1,4);
SHOW CREATE TABLE part_usage;

INSERT INTO part_usage VALUES (1,1,2);
```

**Output**

```
machine_id	name	parent_machine_id
1	Paint booth	NULL
2	Recirculation pump	1
3	Pump impeller	2
Table	Create Table
part_usage	CREATE TABLE `part_usage` (
  `work_order_id` int NOT NULL,
  `part_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`work_order_id`,`part_id`),
  KEY `part_id` (`part_id`),
  CONSTRAINT `part_usage_ibfk_1` FOREIGN KEY (`work_order_id`) REFERENCES `work_order` (`work_order_id`),
  CONSTRAINT `part_usage_ibfk_2` FOREIGN KEY (`part_id`) REFERENCES `part` (`part_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
ERROR 1062 (23000) at line 39: Duplicate entry '1-1' for key 'part_usage.PRIMARY'
```

What the server wrote by itself: the `KEY part_id`, which nobody asked for and which exists because the second foreign key was not the left column of the primary key; and the two names `part_usage_ibfk_1` and `part_usage_ibfk_2`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The recursive one is declared with the foreign key to its own table | 2 |
| The parent column accepts empty and the root proves it | 2 |
| The N:M table has the primary key of the pair | 2 |
| The three things the server wrote by itself are pointed out | 2 |
| The repeated pair returns 1062 and it is pasted | 2 |

**Most common mistake**

Declaring `parent_machine_id INT NOT NULL` because «every machine is mounted in something»; it gives itself away because the first INSERT then has nowhere to start and fails on the foreign key.

### 04.3 · Integrate

**Solution**

```sql
CREATE DATABASE model2 CHARACTER SET utf8mb4;
USE model2;

-- What the drawing asks for, taken literally
CREATE TABLE line (
  line_id         INT PRIMARY KEY,
  name            VARCHAR(40) NOT NULL,
  head_machine_id INT NOT NULL,
  FOREIGN KEY (head_machine_id) REFERENCES machine(machine_id)
);

-- What actually runs, in three statements
CREATE TABLE line (                        -- concession 1: no foreign key yet
  line_id         INT PRIMARY KEY,
  name            VARCHAR(40) NOT NULL,
  head_machine_id INT NULL                 -- concession 2: it accepts empty
);
CREATE TABLE machine (
  machine_id        INT PRIMARY KEY,
  name              VARCHAR(60) NOT NULL,
  line_id           INT NOT NULL,
  parent_machine_id INT NULL,
  FOREIGN KEY (line_id)           REFERENCES line(line_id),
  FOREIGN KEY (parent_machine_id) REFERENCES machine(machine_id)
);
ALTER TABLE line                           -- concession 3: the FK arrives later
  ADD CONSTRAINT fk_line_head
  FOREIGN KEY (head_machine_id) REFERENCES machine(machine_id);

INSERT INTO line    VALUES (1,'Paint', NULL);
INSERT INTO machine VALUES (5,'Paint booth', 1, NULL);
UPDATE line SET head_machine_id = 5 WHERE line_id = 1;
SELECT line_id, name, head_machine_id FROM line;

INSERT INTO line VALUES (2,'Packing', NULL);
SELECT COUNT(*) AS machines_on_line_2 FROM machine WHERE line_id = 2;
```

**Output**

```
ERROR 1824 (HY000) at line 6: Failed to open the referenced table 'machine'
line_id	name	head_machine_id
1	Paint	5
machines_on_line_2
0
```

The promise left with nobody to enforce it is the minimum cardinality. The diagram says a line has machines, and MySQL has no construct that forces it. The Packing line stays with zero machines forever and nobody complains.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The first attempt is run and returns 1824 | 2 |
| The version that runs is three statements, with the ALTER at the end | 3 |
| The three concessions are written in the comments | 2 |
| The line with no machines is registered and counted | 1 |
| Minimum cardinality is named as the thing that cannot be enforced | 2 |

**Most common mistake**

Breaking the cycle by removing the foreign key instead of loosening the `NOT NULL`; it gives itself away because the model loses the rule, while the column that accepts empty keeps it and only postpones it.

---

## Week 05 · Normalisation

### 05.1 · Recognise

**Solution**

```sql
-- Functional dependencies of wide_reading
-- (sensor_id, taken_at) -> value           full key, correctly placed
--  sensor_id            -> sensor_unit     half the key: breaks 2NF
--  sensor_id            -> machine_id      half the key: breaks 2NF
--  machine_id           -> machine_name    transitive: breaks 3NF
--  machine_id           -> machine_area    transitive: breaks 3NF

-- Prediction for the first run: the three readings go in, with no error
-- and no warning, and sensor 103 ends up with two different units.

-- Prediction for the second: the table with no primary key is created without
-- trouble; with sql_require_primary_key switched on, the same CREATE TABLE
-- returns 3750. Uniqueness is not part of the first normal form: it is
-- another rule.

USE norm;
INSERT INTO wide_reading VALUES
 (103,'2026-03-02 06:00:00','mm/s',  2,'Welding robot','Manufacturing',12.30),
 (103,'2026-03-02 07:00:00','mm/s',  2,'Welding robot','Manufacturing',41.80),
 (103,'2026-03-02 08:00:00','mm/seg',2,'Welding robot','Manufacturing',44.90);
SELECT sensor_id, taken_at, sensor_unit FROM wide_reading WHERE sensor_id = 103;

CREATE TABLE no_key (sensor_id INT, value DECIMAL(7,2));
SHOW CREATE TABLE no_key;
DROP TABLE no_key;

SET SESSION sql_require_primary_key = 1;
CREATE TABLE no_key (sensor_id INT, value DECIMAL(7,2));
```

**Output**

```
sensor_id	taken_at	sensor_unit
103	2026-03-02 06:00:00	mm/s
103	2026-03-02 07:00:00	mm/s
103	2026-03-02 08:00:00	mm/seg
Table	Create Table
no_key	CREATE TABLE `no_key` (
  `sensor_id` int DEFAULT NULL,
  `value` decimal(7,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
ERROR 3750 (HY000) at line 13: Unable to create or change a table without a primary key, when the system variable 'sql_require_primary_key' is set. Add a primary key to the table or unset this variable to avoid this message. Note that tables without a primary key can cause performance problems in row-based replication, so please consult your DBA before changing this setting.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five dependencies written as `A → B` | 4 |
| The half-key ones are separated from the transitive ones and the form each group breaks is named | 3 |
| The prediction says the three readings go in without an error | 1 |
| The 3750 is predicted and used to separate 1NF from uniqueness | 2 |

**Most common mistake**

Writing `sensor_id → value`; it gives itself away because the same sensor has several readings, so the value depends on the full pair and not on half of it.

### 05.2 · Apply

**Solution**

```sql
USE norm;
-- Attack 1: the list inside the cell
SELECT COUNT(*) AS orders_with_rf003 FROM wide_order WHERE parts = 'RF-003';
SELECT work_order_id, parts FROM wide_order
 WHERE FIND_IN_SET('RF-003', REPLACE(parts,', ',',')) > 0;

-- Attack 2: two spellings of the same machine
INSERT INTO wide_reading VALUES
 (104,'2026-03-02 06:00:00','C',4,'Screw compressor','Finishing',95.10),
 (104,'2026-03-02 07:00:00','C',4,'Screw Compressor','Finishing',98.60);
SELECT machine_id, machine_name FROM wide_reading WHERE sensor_id = 104;

-- Attack 3: the UPDATE that splits the area
UPDATE wide_reading SET machine_area = 'Paint'
 WHERE sensor_id = 104 AND taken_at = '2026-03-02 06:00:00';
SELECT machine_id, machine_name, machine_area FROM wide_reading WHERE sensor_id = 104;
```

**Output**

```
orders_with_rf003
0
work_order_id	parts
1	RF-001, RF-003
2	RF-006, RF-003
machine_id	machine_name
4	Screw compressor
4	Screw Compressor
machine_id	machine_name	machine_area
4	Screw compressor	Paint
4	Screw Compressor	Finishing
```

The datum was stored and the equality `WHERE` answered zero. `FIND_IN_SET` finds it and in exchange gives up the index: no function wrapped around a column can lean on one, so the whole table gets read.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The list attack returns 0 with equality and does find with `FIND_IN_SET` | 3 |
| The answer says the patch gives up the index | 2 |
| The two spellings go in and are shown together | 2 |
| The UPDATE leaves the same machine in two areas, with no error and no warning | 3 |

**Most common mistake**

Using `LIKE '%RF-003%'` instead of `FIND_IN_SET` and calling it solved; it gives itself away the moment a code `RF-0031` exists, which the wildcard catches and the set does not.

### 05.3 · Integrate

**Solution**

```sql
USE norm;
CREATE TABLE machine (
  machine_id INT PRIMARY KEY,
  name       VARCHAR(60) NOT NULL,
  area       VARCHAR(30) NOT NULL
);
CREATE TABLE sensor (
  sensor_id  INT PRIMARY KEY,
  unit       VARCHAR(10) NOT NULL,
  machine_id INT NOT NULL,
  FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);
CREATE TABLE reading (
  sensor_id INT,
  taken_at  DATETIME,
  value     DECIMAL(7,2) NULL,
  PRIMARY KEY (sensor_id, taken_at),
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);
-- the same data, without losing a row
INSERT INTO machine VALUES (2,'Welding robot','Manufacturing'),
                           (4,'Screw compressor','Finishing');
INSERT INTO sensor  VALUES (103,'mm/s',2),(104,'C',4);
INSERT INTO reading VALUES
 (103,'2026-03-02 06:00:00',12.30),(103,'2026-03-02 07:00:00',41.80),
 (103,'2026-03-02 08:00:00',44.90),
 (104,'2026-03-02 06:00:00',95.10),(104,'2026-03-02 07:00:00',98.60);

UPDATE machine SET area = 'Paint' WHERE machine_id = 4;
SELECT machine_id, name, area FROM machine;

CREATE TABLE energy_use (
  work_order_id INT PRIMARY KEY,
  power_kw      DECIMAL(6,2) NOT NULL,
  hours         DECIMAL(5,2) NOT NULL,
  energy_kwh    DECIMAL(10,2) AS (power_kw * hours) STORED
);
INSERT INTO energy_use (work_order_id, power_kw, hours) VALUES (1, 15.00, 4.00);
SELECT work_order_id, power_kw, hours, energy_kwh FROM energy_use;
INSERT INTO energy_use (work_order_id, power_kw, hours, energy_kwh)
VALUES (2, 15.00, 4.00, 1.00);
```

**Output**

```
machine_id	name	area
2	Welding robot	Manufacturing
4	Screw compressor	Paint
work_order_id	power_kw	hours	energy_kwh
1	15.00	4.00	60.00
ERROR 3105 (HY000) at line 41: The value specified for generated column 'energy_kwh' in table 'energy_use' is not allowed.
```

Attack by attack over the repaired model: the list inside the cell no longer fits, because each usage is a row. The two spellings of the same machine are no longer possible, because the name lives on a single row of `machine`. The update anomaly is gone too, because the `UPDATE` touches that same single row and all five readings see it changed at once.

What was bought: a single place where each fact lives. What was paid: reading one measurement with the name of its machine now takes two JOINs, and that bill arrives in full in week 11.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three tables with their foreign keys, without losing rows | 3 |
| The three attacks are attempted again and what happened to each is stated | 3 |
| The generated column works out 60.00 on its own | 2 |
| The attempt to write it by hand returns 3105 | 1 |
| The price of normalising is named in terms of JOINs | 1 |

**Most common mistake**

Repairing by deleting the awkward row, the one with the second spelling, instead of moving the column to its own table; it gives itself away because the repaired model no longer accepts the same data as the original.

---

## Week 06 · From the model to tables and keys

### 06.1 · Recognise

**Solution**

```sql
-- 1. reading with the value 742.00 ..... bounces, ERROR 3819 (CHECK)
-- 2. reading with an empty value ....... PASSES. The CHECK does not judge the unknown.
-- 3. second certificate for machine 1 .. bounces, ERROR 1062 (UNIQUE)
-- 4. sensor on machine 77 .............. bounces, ERROR 1452 (FOREIGN KEY)
-- 5. machine with the status 'repair' .. bounces, ERROR 1265 (outside the ENUM)
-- 6. FK towards a non-unique column .... bounces, ERROR 6125
-- 7. FK between VARCHAR(10) and INT .... bounces, ERROR 3780

-- The two that share a number: none of them. The two that share a SQLSTATE are
-- 3 and 4, both on 23000, because to the server a duplicate and a broken
-- foreign key are the same class, the integrity one.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven verdicts correct | 4 |
| The seven error numbers | 3 |
| Number 2 is identified as the only one that passes, and why | 2 |
| The question is corrected: what 3 and 4 share is SQLSTATE 23000 | 1 |

**Most common mistake**

Predicting that the empty value bounces because «it is not between -50 and 500»; it gives itself away because a comparison against the empty value does not give false, it gives unknown, and the `CHECK` only stops what came out false.

### 06.2 · Apply

**Solution**

```sql
DROP DATABASE IF EXISTS plant_ddl;
CREATE DATABASE plant_ddl CHARACTER SET utf8mb4;
USE plant_ddl;

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
  status            ENUM('running','down','retired') NOT NULL,
  CONSTRAINT fk_machine_line   FOREIGN KEY (line_id)           REFERENCES line(line_id),
  CONSTRAINT fk_machine_parent FOREIGN KEY (parent_machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE certificate (
  certificate_id INT PRIMARY KEY,
  machine_id     INT     NOT NULL UNIQUE,
  folio          CHAR(9) NOT NULL,
  CONSTRAINT fk_cert_machine FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE sensor (
  sensor_id  INT PRIMARY KEY,
  tag        CHAR(6) NOT NULL UNIQUE,
  machine_id INT     NOT NULL,
  range_min  DECIMAL(7,2) NOT NULL,
  range_max  DECIMAL(7,2) NOT NULL,
  CONSTRAINT ck_sensor_range   CHECK (range_min < range_max),
  CONSTRAINT fk_sensor_machine FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

CREATE TABLE reading (
  reading_id INT PRIMARY KEY,
  sensor_id  INT      NOT NULL,
  taken_at   DATETIME NOT NULL,
  value      DECIMAL(7,2) NULL,
  CONSTRAINT uq_reading        UNIQUE (sensor_id, taken_at),
  CONSTRAINT ck_reading_value  CHECK (value BETWEEN -50 AND 500),
  CONSTRAINT fk_reading_sensor FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);

INSERT INTO line    VALUES (1,'Assembly A','Manufacturing'),(2,'Paint','Finishing');
INSERT INTO machine VALUES (1,'EQ-0001','Hydraulic press 200 t',1,NULL,'running'),
                           (2,'EQ-0002','Welding robot',1,NULL,'running');
INSERT INTO certificate VALUES (1,1,'CAL-24001');
INSERT INTO sensor      VALUES (1,'SN-101',1,0.00,120.00);
INSERT INTO reading     VALUES (1,1,'2026-03-02 06:00:00',71.50);
```

**Output**

The script runs clean twice in a row and prints not one line. The `DROP DATABASE IF EXISTS` on the first statement is what makes it re-runnable.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five tables in an order that needs no manual correction | 3 |
| The 1:N, the 0:1 with UNIQUE and the recursive one are implemented | 3 |
| At least one CHECK, one UNIQUE and one ENUM of its own appear | 2 |
| The script runs twice in a row without being edited | 2 |

**Most common mistake**

Creating `machine` before `line` and fixing it by moving blocks by hand every time; it gives itself away on the second run, when the error comes back on the same line.

### 06.3 · Integrate

**Solution**

```sql
USE plant_ddl;
INSERT INTO reading     VALUES (2,1,'2026-03-02 07:00:00',742.00);
INSERT INTO reading     VALUES (3,1,'2026-03-02 07:00:00',NULL);
SELECT reading_id, value FROM reading WHERE reading_id = 3;
INSERT INTO certificate VALUES (2,1,'CAL-24099');
INSERT INTO sensor      VALUES (2,'SN-999',77,0.00,10.00);
INSERT INTO machine     VALUES (3,'EQ-0003','Robot gripper',1,2,'repair');

CREATE TABLE shift_cat (shift_id INT, name VARCHAR(20), INDEX ix_shift (shift_id));
CREATE TABLE order_a   (order_id INT PRIMARY KEY, shift_id INT);
ALTER TABLE order_a ADD FOREIGN KEY (shift_id) REFERENCES shift_cat(shift_id);

CREATE TABLE order_b (order_id INT PRIMARY KEY, machine_id VARCHAR(10));
ALTER TABLE order_b ADD FOREIGN KEY (machine_id) REFERENCES machine(machine_id);

-- Closing the hole. Row 3 is the one that went in empty; it comes out first,
-- or the ALTER cannot convert the column.
DELETE FROM reading WHERE reading_id = 3;
ALTER TABLE reading MODIFY value DECIMAL(7,2) NOT NULL;
INSERT INTO reading VALUES (5,1,'2026-03-02 09:00:00',NULL);

SELECT TABLE_NAME, NON_UNIQUE, INDEX_NAME, SEQ_IN_INDEX, COLUMN_NAME
  FROM information_schema.STATISTICS
 WHERE TABLE_SCHEMA='plant_ddl' AND TABLE_NAME='sensor'
 ORDER BY INDEX_NAME, SEQ_IN_INDEX;
SELECT INDEX_NAME, SEQ_IN_INDEX, COLUMN_NAME, NON_UNIQUE
  FROM information_schema.STATISTICS
 WHERE TABLE_SCHEMA='plant_ddl' AND TABLE_NAME='reading'
 ORDER BY INDEX_NAME, SEQ_IN_INDEX;
```

**Output**

```
ERROR 3819 (HY000) at line 2: Check constraint 'ck_reading_value' is violated.
reading_id	value
3	NULL
ERROR 1062 (23000) at line 5: Duplicate entry '1' for key 'certificate.machine_id'
ERROR 1452 (23000) at line 6: Cannot add or update a child row: a foreign key constraint fails (`plant_ddl`.`sensor`, CONSTRAINT `fk_sensor_machine` FOREIGN KEY (`machine_id`) REFERENCES `machine` (`machine_id`))
ERROR 1265 (01000) at line 7: Data truncated for column 'status' at row 1
ERROR 6125 (HY000) at line 11: Failed to add the foreign key constraint. Missing unique key for constraint 'order_a_ibfk_1' in the referenced table 'shift_cat'
ERROR 3780 (HY000) at line 14: Referencing column 'machine_id' and referenced column 'machine_id' in foreign key constraint 'order_b_ibfk_1' are incompatible.
ERROR 1048 (23000) at line 20: Column 'value' cannot be null
TABLE_NAME	NON_UNIQUE	INDEX_NAME	SEQ_IN_INDEX	COLUMN_NAME
sensor	1	fk_sensor_machine	1	machine_id
sensor	0	PRIMARY	1	sensor_id
sensor	0	tag	1	tag
INDEX_NAME	SEQ_IN_INDEX	COLUMN_NAME	NON_UNIQUE
PRIMARY	1	reading_id	0
uq_reading	1	sensor_id	0
uq_reading	2	taken_at	0
```

`sensor` has an index nobody declared, `fk_sensor_machine`, written when the foreign key was declared. `reading` does not have one because its foreign key is `sensor_id`, and that column is already the left column of the unique index `uq_reading`, so the server reused that one instead of writing another.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven attempts with their real result pasted | 3 |
| The `CHECK` hole is closed with `NOT NULL` and proved with the 1048 | 3 |
| The index the foreign key wrote on `sensor` is shown | 2 |
| The reason `reading` did not need one is explained | 2 |

**Most common mistake**

Running the `ALTER TABLE ... NOT NULL` without deleting the empty row first; it gives itself away with `ERROR 1138 (22004) Invalid use of NULL value`, which is a different thing: that is the old data getting in the way, not the new rule working.

---

## Week 07 · Data types and DDL

### 07.1 · Recognise

**Solution**

```sql
-- Command          Family   Does ROLLBACK undo it?
-- TRUNCATE TABLE   DDL      no
-- INSERT           DML      yes
-- GRANT            DCL      no
-- ROLLBACK         TCL      it is the ROLLBACK
-- ALTER TABLE      DDL      no
-- DELETE           DML      yes
-- REVOKE           DCL      no
-- CREATE INDEX     DDL      no

-- The three traces
-- 1. TRUNCATE + ROLLBACK -> COUNT(*) = 0.  It did not undo.
-- 2. CREATE   + ROLLBACK -> t_ddl is still on the list. It did not undo.
-- 3. DELETE   + ROLLBACK -> 6, 5, 6.  It did undo.
-- What the first two have in common: both are DDL, and DDL commits on its
-- own account before the ROLLBACK ever arrives.
```

**Output**

```
after_truncate_and_rollback
0
Tables_in_types (t_ddl)
t_ddl
before_it
6
inside
5
after_it
6
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight commands in their family | 3 |
| The eight answers about the ROLLBACK | 2 |
| The three traces predicted correctly | 3 |
| The implicit commit of DDL is named as what the first two share | 2 |

**Most common mistake**

Classifying `TRUNCATE` as DML because «it deletes rows»; it gives itself away with the one-line question, since what it really does is drop the table and create it again empty.

### 07.2 · Apply

**Solution**

```sql
CREATE TABLE sensor (
  sensor_id INT AUTO_INCREMENT PRIMARY KEY,
  tag       CHAR(6)     NOT NULL UNIQUE,  -- always six, CHAR defends that here
  quantity  VARCHAR(20) NOT NULL,         -- variable length, 4 to 11 letters
  installed DATE        NOT NULL,         -- a date, so it can be compared and subtracted
  status    ENUM('running','down','retired') NOT NULL  -- a short closed catalogue
);
CREATE TABLE reading (
  reading_id INT PRIMARY KEY,
  sensor_id  INT NOT NULL,
  value      DECIMAL(5,2) NOT NULL,       -- exact; FLOAT is approximate by design
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);

INSERT INTO sensor (tag, quantity, installed, status) VALUES
 ('SN-101','temperature','2019-03-11','running'),
 ('SN-102','pressure',   '2019-03-11','down'),
 ('SN-103','vibration',  '2020-07-01','retired'),
 ('SN-104','temperature','2018-05-20','running');
INSERT INTO reading VALUES (1, 1, 71.50);

INSERT INTO sensor (tag, quantity, installed, status)
VALUES ('SN-105','torque','02/03/2026','running');

INSERT INTO reading VALUES (7, 1, 9999.9);

INSERT INTO sensor (tag, quantity, installed, status)
VALUES ('SN-1060','torque','2026-03-02','running');

INSERT INTO sensor (tag, quantity, installed, status)
VALUES ('SN-107', NULL,'2026-03-02','running');
```

**Output**

```
ERROR 1292 (22007) at line 26: Incorrect date value: '02/03/2026' for column 'installed' at row 1
ERROR 1264 (22003) at line 29: Out of range value for column 'value' at row 1
ERROR 1406 (22001) at line 31: Data too long for column 'tag' at row 1
ERROR 1048 (23000) at line 34: Column 'quantity' cannot be null
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Every column brings its type and its reason in one line | 4 |
| The four rejections provoked, with their number | 4 |
| The reason for `DECIMAL` is defended against `FLOAT` | 1 |
| No date was left in `VARCHAR` | 1 |

**Most common mistake**

Justifying `CHAR(6)` by saying it «saves memory»; it gives itself away in 07.3, where the same string with trailing spaces reads back different from how it was stored.

### 07.3 · Integrate

**Solution**

```sql
-- 1. The ENUM
SELECT sensor_id, tag, status, status + 0 AS internal_value
  FROM sensor ORDER BY status;

-- 2. The pair the source material confuses
TRUNCATE TABLE sensor;
DELETE FROM sensor WHERE sensor_id = 1;

-- 3. The counter, on a table with no children
CREATE TABLE stop_log (
  stop_id INT AUTO_INCREMENT PRIMARY KEY,
  reason  VARCHAR(40) NOT NULL
);
INSERT INTO stop_log (reason)
VALUES ('Seal failure'),('Overload'),('Tooling change');
DELETE FROM stop_log;
INSERT INTO stop_log (reason) VALUES ('First one after the DELETE');
SELECT stop_id, reason FROM stop_log;
TRUNCATE TABLE stop_log;
INSERT INTO stop_log (reason) VALUES ('First one after the TRUNCATE');
SELECT stop_id, reason FROM stop_log;

-- The closing
CREATE TABLE t_char    (v CHAR(6));
CREATE TABLE t_varchar (v VARCHAR(6));
INSERT INTO t_char    VALUES ('SN-1  ');
INSERT INTO t_varchar VALUES ('SN-1  ');
SELECT CONCAT('[',v,']') AS read_back, LENGTH(v) AS bytes FROM t_char;
SELECT CONCAT('[',v,']') AS read_back, LENGTH(v) AS bytes FROM t_varchar;
```

**Output**

```
sensor_id	tag	status	internal_value
1	SN-101	running	1
4	SN-104	running	1
2	SN-102	down	2
3	SN-103	retired	3
ERROR 1701 (42000) at line 7: Cannot truncate a table referenced in a foreign key constraint (`types`.`reading`, CONSTRAINT `reading_ibfk_1`)
ERROR 1451 (23000) at line 8: Cannot delete or update a parent row: a foreign key constraint fails (`types`.`reading`, CONSTRAINT `reading_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))
stop_id	reason
4	First one after the DELETE
stop_id	reason
1	First one after the TRUNCATE
read_back	bytes
[SN-1]	4
read_back	bytes
[SN-1  ]	6
```

The order came out `running`, `running`, `down`, `retired`, which is the order the catalogue was declared in. Alphabetically it would have come out `down`, `retired`, `running`, `running`. The `status + 0` shows where that comes from: each value stores the position it was given when it was written.

The counter started at 4 after the `DELETE` and at 1 after the `TRUNCATE`. That jump is the argument for `TRUNCATE` not being a fast `DELETE`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The ENUM order is reported and explained with `status + 0` | 3 |
| The two parent errors, 1701 and 1451, with their number | 3 |
| The two counter identifiers, 4 and 1 | 2 |
| `CHAR` returns `[SN-1]` with 4 bytes and `VARCHAR` returns `[SN-1  ]` with 6 | 2 |

**Most common mistake**

Trying the counter test on `sensor`, which has children; it gives itself away because the `TRUNCATE` returns 1701 and the experiment stays half done without the student noticing.

---

## Week 08 · DML and transactions · First midterm

### 08.1 · Recognise

**Solution**

```sql
-- at the start              6
-- after the first DELETE    5
-- after the second DELETE   4
-- after ROLLBACK TO s1      5
-- after the final ROLLBACK  6

-- With a COMMIT instead of the final ROLLBACK, the table stays at 5:
-- the ROLLBACK TO s1 only withdrew the second DELETE, not the first.
-- With autocommit at 1 and no START TRANSACTION, each DELETE has already
-- committed on its own; the ROLLBACK answers Query OK and changes nothing.
-- The table stays at 4.

USE dml;
SELECT COUNT(*) AS at_the_start FROM reading;
START TRANSACTION;
DELETE FROM reading WHERE reading_id = 6;
SELECT COUNT(*) AS after_the_first_delete FROM reading;
SAVEPOINT s1;
DELETE FROM reading WHERE reading_id = 5;
SELECT COUNT(*) AS after_the_second_delete FROM reading;
ROLLBACK TO SAVEPOINT s1;
SELECT COUNT(*) AS after_rollback_to_s1 FROM reading;
ROLLBACK;
SELECT COUNT(*) AS after_the_final_rollback FROM reading;
```

**Output**

```
at_the_start
6
after_the_first_delete
5
after_the_second_delete
4
after_rollback_to_s1
5
after_the_final_rollback
6
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five counts in order | 5 |
| The answer with `COMMIT` is 5, and the reach of `ROLLBACK TO` is explained | 3 |
| The answer with autocommit is 4, and the `ROLLBACK` is said not to complain | 2 |

**Most common mistake**

Believing that `ROLLBACK TO SAVEPOINT` closes the transaction; it gives itself away in the final count, predicted at 5 instead of 6 because the `ROLLBACK` below is assumed to have nothing left to do.

### 08.2 · Apply

**Solution**

```sql
USE dml;
SELECT COUNT(*) AS before_load FROM reading;
INSERT INTO reading (reading_id, sensor_id, taken_at, value) VALUES
 (7,3,'2026-03-02 08:00:00', 44.90),
 (8,3,'2026-03-02 09:00:00',742.00),
 (9,3,'2026-03-02 10:00:00', 39.20);
SELECT COUNT(*) AS after_load FROM reading;

INSERT INTO reading (reading_id, sensor_id, taken_at, value) VALUES
 (7,3,'2026-03-02 08:00:00',44.90),
 (8,3,'2026-03-02 09:00:00',42.10),
 (9,3,'2026-03-02 10:00:00',39.20);
SELECT COUNT(*) AS after_the_fix FROM reading;

INSERT INTO work_order (machine_id, type, done_on)
SELECT machine_id, 'preventive', '2026-04-01' FROM machine WHERE line_id = 1;
SELECT work_order_id, machine_id, type, done_on FROM work_order;

SELECT machine_id, ROUND(run_hours / stops, 2) AS hours_between_stops
  FROM availability;
SHOW WARNINGS;

CREATE TABLE indicator (machine_id INT PRIMARY KEY, mtbf DECIMAL(10,2));
INSERT INTO indicator (machine_id, mtbf)
SELECT machine_id, run_hours / stops FROM availability;
```

**Output**

```
before_load
6
ERROR 3819 (HY000) at line 3: Check constraint 'ck_reading_value' is violated.
after_load
6
after_the_fix
9
work_order_id	machine_id	type	done_on
1	1	preventive	2026-04-01
2	2	preventive	2026-04-01
machine_id	hours_between_stops
1	120.00
2	230.17
4	NULL
Level	Code	Message
Warning	1365	Division by 0
ERROR 1365 (22012) at line 24: Division by 0
```

Before 6 and after 6. The first row of the three-row `INSERT` did not stay either: the statement goes in whole or it does not go in, and that guarantee comes as standard.

The same division answered two different things. In a `SELECT` it returned empty with a warning nobody reads. Inside an `INSERT` it raised error 1365 and brought down the whole load.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The counts before and after the bad `INSERT` are the same | 3 |
| The answer says the atomicity of the statement did not have to be asked for | 1 |
| The `INSERT ... SELECT` registers the orders without any identifier typed by hand | 3 |
| The division appears twice, with the warning and with error 1365 | 3 |

**Most common mistake**

Repairing the load by deleting the bad row from the script and running it again without checking the count; it gives itself away because it never shows that the good row had not gone in either.

### 08.3 · Integrate

**Solution**

```sql
USE dml;
-- Part one. 1:N, foreign key on the many side.
CREATE TABLE sensor (
  sensor_id  INT PRIMARY KEY,
  tag        CHAR(6) NOT NULL UNIQUE,
  machine_id INT NOT NULL,
  FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
);

-- Part two.
-- The timestamp cannot go in VARCHAR: error 1292 from week 7 is exactly the one
-- that refuses to store '02/03/2026', and in text it can neither be subtracted
-- nor sorted chronologically.
-- The value cannot go in FLOAT: FLOAT is approximate by design, and error 1264
-- from week 7 only appears because DECIMAL(5,2) counts the digits.

-- Part three.
START TRANSACTION;
INSERT INTO reading (reading_id, sensor_id, taken_at, value) VALUES
 (10,3,'2026-03-02 11:00:00',40.05),
 (11,3,'2026-03-02 12:00:00',43.70),
 (12,3,'2026-03-02 13:00:00',38.15);
SELECT COUNT(*) AS verification FROM reading;
COMMIT;

-- Part four, condition 1: DDL in the middle
START TRANSACTION;
INSERT INTO sensor VALUES (4,'SN-104',4);
CREATE TABLE tmp_implicit (id INT);
ROLLBACK;
SELECT sensor_id, tag FROM sensor WHERE sensor_id = 4;

-- Condition 2: the table that is not InnoDB
CREATE TABLE t_myisam (id INT PRIMARY KEY, note VARCHAR(30)) ENGINE=MyISAM;
START TRANSACTION;
INSERT INTO t_myisam VALUES (1,'test reading');
ROLLBACK;
SELECT id, note FROM t_myisam;

-- Condition 3: no transaction open. With @@autocommit = 1 every statement
-- commits by itself and the ROLLBACK answers Query OK without changing a thing.
```

**Output**

```
verification
12
sensor_id	tag
4	SN-104
id	note
1	test reading
```

The sensor 4 row is still there after the `ROLLBACK`, because the `CREATE TABLE` in the middle committed it before anybody could withdraw it. The MyISAM row is still there too, and there the `ROLLBACK` never had anything to do in the first place.

The most dangerous of the three is the MyISAM one, and the argument is that the other two leave a trace. The `CREATE TABLE` is in plain sight in the script and autocommit is one `SELECT @@autocommit` away. The engine of the table appears nowhere in the statement you are writing, so the `ROLLBACK` does nothing and says nothing either.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Part one: cardinality, physical form and the DDL that implements it | 2 |
| Part two: the two justifications cite a measured error | 2 |
| Part three: the verification count comes before the `COMMIT` | 3 |
| Part four: the three conditions demonstrated with their run | 2 |
| The judgement on the most dangerous one comes with an argument | 1 |

**Most common mistake**

Putting the `COMMIT` before the verification `SELECT`; it gives itself away because the check can no longer correct anything and the only remedy left is a repair `DELETE`.

---

## Week 09 · The single-table SELECT

### 09.1 · Recognise

**Solution**

```sql
-- machines               8
-- criticality = 'high'   3
-- criticality <> 'high'  4
-- criticality = NULL     0
-- criticality IS NULL    1
-- readings              20
-- value IS NOT NULL     15
-- value IS NULL          5

-- 3 + 4 = 7, not 8. Machine 8 appears on neither list because its criticality
-- is empty, and a comparison against the empty value answers neither true nor
-- false: it answers unknown. The WHERE only lets the true ones through, so the
-- unknown leaves with the false ones.

-- Without brackets:  6 machines.  AND is resolved before OR.
-- With brackets:     5 machines.

USE plant;
SELECT 'machines'            AS metric, COUNT(*) AS n FROM machine
UNION ALL SELECT 'criticality high',     COUNT(*) FROM machine WHERE criticality =  'high'
UNION ALL SELECT 'criticality not high', COUNT(*) FROM machine WHERE criticality <> 'high'
UNION ALL SELECT 'compared with NULL',   COUNT(*) FROM machine WHERE criticality =  NULL
UNION ALL SELECT 'no criticality',       COUNT(*) FROM machine WHERE criticality IS NULL
UNION ALL SELECT 'readings',             COUNT(*) FROM reading
UNION ALL SELECT 'with a value',         COUNT(*) FROM reading WHERE value IS NOT NULL
UNION ALL SELECT 'without a value',      COUNT(*) FROM reading WHERE value IS NULL;

SELECT code, name, criticality, status FROM machine
 WHERE criticality = 'high' OR criticality = 'medium' AND status = 'running';

SELECT code, name, criticality, status FROM machine
 WHERE (criticality = 'high' OR criticality = 'medium') AND status = 'running';
```

**Output**

```
metric	n
machines	8
criticality high	3
criticality not high	4
compared with NULL	0
no criticality	1
readings	20
with a value	15
without a value	5
code	name	criticality	status
EQ-0001	Hydraulic press 200 t Kühn	high	running
EQ-0002	Welding robot	high	running
EQ-0003	Robot gripper	medium	running
EQ-0004	Screw compressor	high	down
EQ-0005	Paint booth	medium	running
EQ-0006	Lindström recirculation pump	medium	running
code	name	criticality	status
EQ-0001	Hydraulic press 200 t Kühn	high	running
EQ-0002	Welding robot	high	running
EQ-0003	Robot gripper	medium	running
EQ-0005	Paint booth	medium	running
EQ-0006	Lindström recirculation pump	medium	running
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight counts | 4 |
| Unknown is named as the third state and the one-row gap is explained | 3 |
| The two precedence counts, 6 and 5 | 2 |
| Machine 4, which is down, is identified as the extra one without brackets | 1 |

**Most common mistake**

Predicting 5 for `criticality <> 'high'`, counting the machine with no criticality; it gives itself away because the total would then close at 8 and the exercise would have no point.

### 09.2 · Apply

**Solution**

```sql
USE plant;
-- 1
SELECT code, name, status FROM machine WHERE status = 'running';

-- 2
SELECT @@collation_database AS collation_in_force;
SELECT code, name FROM machine WHERE name LIKE '%kuhn%';
SELECT code, name FROM machine WHERE name LIKE '%lindstrom%';
SELECT code, name FROM machine WHERE name LIKE 'hydraulic%';

-- 3
SELECT code, description FROM part WHERE description LIKE '%50%';
SELECT code, description FROM part WHERE description LIKE '%50\%%';

-- 4
SELECT COUNT(*) AS in_the_list     FROM machine WHERE criticality IN ('high','low');
SELECT COUNT(*) AS out_of_the_list FROM machine WHERE criticality NOT IN ('high','low');
SELECT COUNT(*) AS with_between    FROM reading WHERE value BETWEEN 6.40 AND 41.80;
SELECT COUNT(*) AS strict_limits   FROM reading WHERE value >  6.40 AND value < 41.80;
SELECT COUNT(*) AS reversed        FROM reading WHERE value BETWEEN 41.80 AND 6.40;

-- 5
SELECT code, name FROM machine ORDER BY code LIMIT 3;
SELECT code, name FROM machine ORDER BY code LIMIT 3 OFFSET 3;
```

**Output**

```
code	name	status
EQ-0001	Hydraulic press 200 t Kühn	running
EQ-0002	Welding robot	running
EQ-0003	Robot gripper	running
EQ-0005	Paint booth	running
EQ-0006	Lindström recirculation pump	running
EQ-0007	Conveyor belt	running
collation_in_force
utf8mb4_0900_ai_ci
code	name
EQ-0001	Hydraulic press 200 t Kühn
code	name
EQ-0006	Lindström recirculation pump
code	name
EQ-0001	Hydraulic press 200 t Kühn
code	description
RF-001	Air filter 50% efficiency
RF-002	Oil filter 50 micron
RF-003	Deep groove ball bearing 50 mm
code	description
RF-001	Air filter 50% efficiency
in_the_list
4
out_of_the_list
3
with_between
6
strict_limits
4
reversed
0
code	name
EQ-0001	Hydraulic press 200 t Kühn
EQ-0002	Welding robot
EQ-0003	Robot gripper
code	name
EQ-0004	Screw compressor
EQ-0005	Paint booth
EQ-0006	Lindström recirculation pump
```

Nobody wrote any diacritic or case handling. The collation `utf8mb4_0900_ai_ci` already comes set on the server: `ai` ignores accents and `ci` ignores case.

The limits of the `BETWEEN` are included, and that is why 6 against 4. The two readings that make the difference are the one at 6.40 and the one at 41.80, which are exactly the ends.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The exact filter returns the six running machines | 2 |
| The three text searches work and the collation is cited | 3 |
| The literal `50%` returns a single part, with the wildcard escaped | 2 |
| The three range counts, 6, 4 and 0 | 2 |
| The two pages of three, with `ORDER BY` | 1 |

**Most common mistake**

Writing `LIKE '%50%%'` to search for the literal percent sign; it gives itself away because it returns the same three parts as the unescaped version, since the second `%` is still read as a wildcard.

### 09.3 · Integrate

**Solution**

```sql
USE plant;
-- 1. The channel that sorts as text
SELECT tag, channel FROM sensor ORDER BY channel;
SELECT '10' < '9' AS as_text, 10 < 9 AS as_number;
-- The repair at the root, with week 7's type:
--   ALTER TABLE sensor MODIFY channel SMALLINT NOT NULL;

-- 2. The alias
SELECT tag, range_max - range_min AS span FROM sensor WHERE span > 100;
SELECT tag, range_max - range_min AS span FROM sensor ORDER BY span DESC LIMIT 3;

-- 3. NULLs at the end
SELECT reading_id, value FROM reading ORDER BY value ASC LIMIT 3;
SELECT reading_id, value FROM reading ORDER BY value IS NULL, value ASC LIMIT 3;
SELECT reading_id, value FROM reading ORDER BY value ASC NULLS LAST;

-- The closing
SELECT code, name FROM machine LIMIT 3;
SELECT code  name FROM machine LIMIT 3;
```

**Output**

```
tag	channel
SN-101	1
SN-104	10
SN-105	100
SN-102	2
SN-106	3
SN-103	9
as_text	as_number
1	0
ERROR 1054 (42S22) at line 9: Unknown column 'span' in 'where clause'
tag	span
SN-105	250.00
SN-101	120.00
SN-104	120.00
reading_id	value
7	NULL
11	NULL
3	NULL
reading_id	value
5	6.40
6	6.55
19	8.75
ERROR 1064 (42000) at line 15: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'NULLS LAST' at line 1
code	name
EQ-0001	Hydraulic press 200 t Kühn
EQ-0002	Welding robot
EQ-0003	Robot gripper
name
EQ-0001
EQ-0002
EQ-0003
```

The alias is born in the `SELECT`, which runs at step 5. The `WHERE` runs at step 2, when it does not exist yet, and that is why 1054 comes out. The `ORDER BY` runs at step 6 and does get to see it.

The second query of the closing gave no error and the report came out wrong: with no comma, `name` was read as an alias for `code`, so the header says `name` and the codes are underneath it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The channel order is reported and explained with `'10' < '9'` | 2 |
| The type change is proposed as the repair at the root | 1 |
| The 1054 and the version that does work, explained with the logical order | 3 |
| The empties are sent to the end without `NULLS LAST`, and the 1064 is left on the record | 2 |
| The missing comma is run and the header is explained | 2 |

**Most common mistake**

Sending the empties to the end with `ORDER BY value DESC`; it gives itself away because that also reverses the order of everything else, and what was asked for was to keep it.

---

## Week 10 · Grouping and aggregates

### 10.1 · Recognise

**Solution**

```sql
-- n      20      COUNT(*) counts every row
-- c      15      COUNT(value) skips the five empty ones
-- avg    73.050000
-- mn      6.40
-- mx    191.40

-- total     1095.75
-- over_20     54.787500   divided by 20: not the average
-- over_15     73.050000   divided by 15: this one is, and it matches AVG

-- The average was worked out with 15 of the 20 readings. Whoever receives the
-- report has nowhere to get that from: the figure does not carry the note.

USE plant;
SELECT COUNT(*) AS n, COUNT(value) AS c, AVG(value) AS avg_value,
       MIN(value) AS mn, MAX(value) AS mx
FROM reading;

SELECT SUM(value) AS total,
       SUM(value)/COUNT(*)     AS over_20,
       SUM(value)/COUNT(value) AS over_15
FROM reading;
```

**Output**

```
n	c	avg_value	mn	mx
20	15	73.050000	6.40	191.40
total	over_20	over_15
1095.75	54.787500	73.050000
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five values of the first row | 4 |
| The three of the second | 3 |
| `over_15` is identified as the real average, equal to `AVG` | 2 |
| The answer says the figure travels without the note of how many rows were skipped | 1 |

**Most common mistake**

Predicting `avg` as the sum divided by 20; it gives itself away because it does not match `AVG`, and `AVG` divides by the rows that do carry a value.

### 10.2 · Apply

**Solution**

```sql
USE plant;
-- 1
SELECT type, folio, COUNT(*) FROM work_order GROUP BY type;        -- raises 1055
SELECT type, COUNT(*) AS orders FROM work_order GROUP BY type;     -- corrected

-- 2
SELECT machine_id, COUNT(*) AS orders, COUNT(hours) AS with_hours,
       SUM(hours) AS total_hours, AVG(hours) AS average
  FROM work_order GROUP BY machine_id ORDER BY machine_id;

-- 3
SELECT machine_id, COUNT(*) AS orders FROM work_order
 WHERE orders > 2 GROUP BY machine_id;
SELECT machine_id, COUNT(*) AS orders FROM work_order
 GROUP BY machine_id HAVING orders > 2;

-- 4
SELECT machine_id,
  SUM(CASE WHEN type='preventive' THEN 1 ELSE 0 END) AS prev,
  SUM(CASE WHEN type='corrective' THEN 1 ELSE 0 END) AS corr,
  SUM(CASE WHEN type='predictive' THEN 1 ELSE 0 END) AS pred
  FROM work_order GROUP BY machine_id ORDER BY machine_id;

-- 5
SELECT @@lc_time_names AS language;
SELECT YEAR(done_on) AS year, MONTHNAME(done_on) AS month,
       COUNT(*) AS orders, SUM(hours) AS hours
  FROM work_order
 GROUP BY YEAR(done_on), MONTH(done_on), MONTHNAME(done_on)
 ORDER BY year, MONTH(done_on);
SET lc_time_names = 'es_MX';
SELECT MONTHNAME('2026-02-14') AS month;
```

**Output**

```
ERROR 1055 (42000) at line 3: Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'plant.work_order.folio' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
type	orders
preventive	5
corrective	5
predictive	2
machine_id	orders	with_hours	total_hours	average
1	2	2	9.50	4.750000
2	3	2	10.25	5.125000
4	2	2	21.50	10.750000
5	2	2	8.25	4.125000
6	1	1	5.00	5.000000
7	2	1	1.75	1.750000
ERROR 1054 (42S22) at line 12: Unknown column 'orders' in 'where clause'
machine_id	orders
2	3
machine_id	prev	corr	pred
1	1	1	0
2	1	1	1
4	0	2	0
5	2	0	0
6	0	1	0
7	1	0	1
language
en_US
year	month	orders	hours
2026	January	4	15.25
2026	February	6	31.50
2026	March	2	9.50
month
febrero
```

The 1055 carries the rule in its own wording: if a row summarises several rows, every column you name has to be worth the same for the whole group, and `folio` is not the same for the five preventive orders.

The alias does not exist in the `WHERE` and does exist in the `HAVING`. The `WHERE` runs at step 2, before the `SELECT` creates the alias. Machine 2 is the only one with more than two orders.

The month comes out in English because `@@lc_time_names` is `en_US` on the server, not because the datum is in English. Switch the variable to `es_MX` and the same date answers `febrero`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The 1055 provoked and corrected, with the rule explained | 3 |
| The orders per machine with the four columns | 2 |
| The `WHERE` against `HAVING` contrast, with the 1054 pasted | 2 |
| The pivot with conditional aggregation | 2 |
| The month name explained with `lc_time_names` | 1 |

**Most common mistake**

Padding the `GROUP BY` with every column of the `SELECT` to silence the 1055; it gives itself away because the groups split and the count per type goes from 3 rows to 12.

### 10.3 · Integrate

**Solution**

```sql
USE plant;
SELECT COUNT(*) AS with_not_in FROM machine m
 WHERE m.machine_id NOT IN (SELECT parent_machine_id FROM machine);

SELECT COUNT(*) AS with_not_exists FROM machine m
 WHERE NOT EXISTS (SELECT 1 FROM machine c WHERE c.parent_machine_id = m.machine_id);

SELECT COUNT(*) AS empty_parents FROM machine WHERE parent_machine_id IS NULL;

WITH work_load AS (
  SELECT machine_id, COUNT(*) AS orders FROM work_order GROUP BY machine_id
)
SELECT machine_id, orders FROM work_load
 WHERE orders > (SELECT AVG(orders) FROM work_load)
 ORDER BY orders DESC;

SELECT code, reorder_point,
  CASE
    WHEN reorder_point >= 8    THEN 'high'
    WHEN reorder_point >= 3    THEN 'medium'
    WHEN reorder_point IS NULL THEN 'no point set'
    ELSE 'low'
  END AS band
  FROM part ORDER BY part_id;

SELECT code, reorder_point,
  IF(reorder_point >= 3, 'has a point', 'no point') AS band
  FROM part ORDER BY part_id;
```

**Output**

```
with_not_in
0
with_not_exists
6
empty_parents
6
machine_id	orders
2	3
code	reorder_point	band
RF-001	4	medium
RF-002	4	medium
RF-003	8	high
RF-004	2	low
RF-005	0	low
RF-006	NULL	no point set
RF-007	3	medium
code	reorder_point	band
RF-001	4	has a point
RF-002	4	has a point
RF-003	8	has a point
RF-004	2	no point
RF-005	0	no point
RF-006	NULL	no point
RF-007	3	has a point
```

The same question answered 0 and answered 6, with no error and no warning. `NOT IN` compares against a list carrying six empties, and the moment one element of the list is unknown the whole answer turns unknown. `NOT EXISTS` asks whether a row exists that meets the condition, and that question does have an answer.

The two classifications stop agreeing on `RF-006`. The `CASE` sends it to `no point set` and the `IF` sends it to `no point`, the same box where it put `RF-005`, which has a reorder point of 0. The `IF` is the wrong one: a reorder point of 0 is a decision somebody took and an empty reorder point is a decision nobody took.

The `WITH` saved writing the grouping twice, once for the set and once for its own average.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three counts, 0, 6 and 6 | 3 |
| The 0 is explained by the empty value inside the list | 2 |
| The `WITH` runs and what it saved is stated | 2 |
| Both classifications are shown in full | 1 |
| `RF-006` is pointed out as the row of the disagreement and which one is wrong is stated | 2 |

**Most common mistake**

Concluding that `NOT IN` is broken; it gives itself away because over a list with no empties it answers the same as `NOT EXISTS`, and what fails is not the operator but the assumption that the list carries no unknowns.

---

## Week 11 · JOIN, UNION and UNION ALL

### 11.1 · Recognise

**Solution**

```sql
-- 1. INNER JOIN                                 12 rows
-- 2. LEFT JOIN                                  14 rows
-- 3. LEFT JOIN + WHERE o.work_order_id IS NULL   2 machines: EQ-0003 and EQ-0008
-- 4. For machine 3: COUNT(*) = 1 and COUNT(o.work_order_id) = 0

-- The row COUNT(*) is counting exists in neither of the two tables. The LEFT
-- JOIN manufactured it: it brings machine 3 along even though it matched
-- nothing, and fills every column of the right side with empty. COUNT(*)
-- counts it because there is a row; COUNT(o.work_order_id) does not, because
-- that column arrived empty.

USE plant;
SELECT COUNT(*) AS with_inner FROM machine e
  JOIN work_order o ON o.machine_id = e.machine_id;
SELECT COUNT(*) AS with_left FROM machine e
  LEFT JOIN work_order o ON o.machine_id = e.machine_id;

SELECT e.machine_id, e.code FROM machine e
  LEFT JOIN work_order o ON o.machine_id = e.machine_id
 WHERE o.work_order_id IS NULL;

SELECT e.machine_id, COUNT(*) AS with_asterisk, COUNT(o.work_order_id) AS with_column
  FROM machine e
  LEFT JOIN work_order o ON o.machine_id = e.machine_id
 GROUP BY e.machine_id ORDER BY e.machine_id;
```

**Output**

```
with_inner
12
with_left
14
machine_id	code
3	EQ-0003
8	EQ-0008
machine_id	with_asterisk	with_column
1	2	2
2	3	3
3	1	0
4	2	2
5	2	2
6	1	1
7	2	2
8	1	0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four numbers: 12, 14, 2, and the pair 1 and 0 | 4 |
| Where the row `COUNT(*)` counts comes from is explained | 4 |
| The two machines with no orders are identified | 2 |

**Most common mistake**

Predicting 14 for the `INNER JOIN` and 12 for the `LEFT JOIN`; it gives itself away because a `LEFT JOIN` never returns fewer rows than the `INNER JOIN` over the same tables.

### 11.2 · Apply

**Solution**

```sql
USE plant;
-- «The reading whose sensor is this one, and the machine that sensor belongs to.»
SELECT e.code, s.tag, r.taken_at, r.value
  FROM reading r
  JOIN sensor  s ON s.sensor_id  = r.sensor_id
  JOIN machine e ON e.machine_id = s.machine_id
 WHERE r.value IS NOT NULL
 ORDER BY e.code, s.tag, r.taken_at
 LIMIT 6;

SELECT COUNT(*) AS rows_returned FROM machine e
  LEFT JOIN work_order o ON o.machine_id = e.machine_id
 WHERE o.type = 'corrective';

SELECT COUNT(*) AS rows_returned FROM machine e
  LEFT JOIN work_order o ON o.machine_id = e.machine_id AND o.type = 'corrective';

SELECT COUNT(*) AS cartesian_product FROM line, machine;
```

**Output**

```
code	tag	taken_at	value
EQ-0001	SN-101	2026-03-02 06:00:00	71.50
EQ-0001	SN-101	2026-03-02 07:00:00	74.20
EQ-0001	SN-101	2026-03-02 09:00:00	78.90
EQ-0001	SN-102	2026-03-02 06:00:00	6.40
EQ-0001	SN-102	2026-03-02 07:00:00	6.55
EQ-0002	SN-103	2026-03-02 06:00:00	12.30
rows_returned
5
rows_returned
9
cartesian_product
24
```

With the predicate in the `WHERE` there are 5 rows. The `LEFT JOIN` manufactured its rows of empties and the `WHERE` then discarded them, because `o.type` was empty on all of them and empty is never equal to `'corrective'`. The `LEFT JOIN` turned back into an `INNER JOIN`.

With the predicate in the `ON` there are 9. There it is applied earlier, when deciding what matches what, and the four machines with no corrective orders still appear with their right-hand columns empty.

The cartesian product is 3 lines by 8 machines. The query is legal and nobody puts their hand up.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three-table JOIN runs and joins by key, not by name | 3 |
| Each `ON` brings its sentence in the comment | 1 |
| The two counts, 5 and 9 | 3 |
| Why the `WHERE` turned the `LEFT` into an `INNER` is explained | 2 |
| The cartesian product is reported at 24 | 1 |

**Most common mistake**

Joining `sensor` with `machine` by name instead of by key; it gives itself away because it returns zero rows, since no sensor name matches any machine name.

### 11.3 · Integrate

**Solution**

```sql
USE plant;
SELECT p.code, i.code FROM part p
  FULL OUTER JOIN line_stock i ON i.code = p.code;

SELECT COUNT(*) AS from_left  FROM part p
  LEFT  JOIN line_stock i ON i.code = p.code;
SELECT COUNT(*) AS from_right FROM part p
  RIGHT JOIN line_stock i ON i.code = p.code;
SELECT COUNT(*) AS matching   FROM part p
  JOIN line_stock i ON i.code = p.code;

SELECT p.code AS central, i.code AS on_the_line FROM part p
  LEFT JOIN line_stock i ON i.code = p.code
UNION
SELECT p.code, i.code FROM part p
  RIGHT JOIN line_stock i ON i.code = p.code
ORDER BY central, on_the_line;

SELECT COUNT(*) AS rows_returned, SUM(quantity) AS pieces FROM (
  SELECT code, quantity FROM shift_use_a
  UNION ALL
  SELECT code, quantity FROM shift_use_b) t;

SELECT COUNT(*) AS rows_returned, SUM(quantity) AS pieces FROM (
  SELECT code, quantity FROM shift_use_a
  UNION
  SELECT code, quantity FROM shift_use_b) t;

SELECT COUNT(*) AS the_union FROM (
  SELECT p.code AS central, i.code AS on_the_line FROM part p
    LEFT JOIN line_stock i ON i.code = p.code
  UNION
  SELECT p.code, i.code FROM part p
    RIGHT JOIN line_stock i ON i.code = p.code) u;
```

**Output**

```
ERROR 1064 (42000) at line 2: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'FULL OUTER JOIN line_stock i ON i.code = p.code' at line 2
from_left
7
from_right
8
matching
5
central	on_the_line
NULL	RF-101
NULL	RF-102
NULL	RF-103
RF-001	RF-001
RF-002	RF-002
RF-003	RF-003
RF-004	RF-004
RF-005	RF-005
RF-006	NULL
RF-007	NULL
rows_returned	pieces
7	18
rows_returned	pieces
4	9
the_union
10
```

The three blocks: five parts are on both sides, two only in the central store (`RF-006` and `RF-007`) and three only on the line (`RF-101`, `RF-102`, `RF-103`). 5 + 2 + 3 = 10.

The real consumption of the store is 18 pieces over 7 issues. The `UNION` answered 9 because both shifts took out the same bearing `RF-003` in the same quantity, and a row identical to another looked like a duplicate to it. When rows stand for things that happened they get stacked with `UNION ALL`; `UNION` is for asking for the list of distinct values, and it charges a temporary table for doing so.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The 1064 from the `FULL OUTER JOIN` pasted | 1 |
| The four counts: 7, 8, 5 and 10 | 3 |
| The ten rows read in the three blocks | 2 |
| The projection brings both codes | 1 |
| The two pairs of consumption numbers, 7/18 and 4/9 | 2 |
| Which is the real consumption and why the other came out quiet | 1 |

**Most common mistake**

Projecting only the description instead of the code; it gives itself away because the descriptions in the two tables are written differently and the count of the union climbs instead of closing at 10.

---

## Week 12 · Views

### 12.1 · Recognise

**Solution**

```sql
-- IS_UPDATABLE according to the catalogue
-- v_reading_full    YES
-- v_reading_left    NO
-- v_sensor_load     NO
-- v_sensor_count    YES

-- The five attempts
-- 1. UPDATE of one base table through v_reading_full ... passes
-- 2. UPDATE touching two base tables .............. ERROR 1393
-- 3. DELETE through v_reading_full ................ ERROR 1395
-- 4. UPDATE through v_reading_left ................ ERROR 1288
-- 5. UPDATE through v_sensor_count ................ ERROR 1288

-- The disagreement is number 5. The catalogue says YES and the server answers
-- 1288, and the UPDATE was not even touching the calculated column. The working
-- rule: test the UPDATE, do not believe the IS_UPDATABLE column.

USE plant;
SELECT TABLE_NAME, IS_UPDATABLE FROM information_schema.VIEWS
 WHERE TABLE_SCHEMA = 'plant' AND TABLE_NAME LIKE 'v_%'
 ORDER BY TABLE_NAME;

UPDATE v_reading_full SET value = 79.90 WHERE reading_id = 4;
SELECT reading_id, value FROM reading WHERE reading_id = 4;

UPDATE v_reading_full SET value = 80.00, sensor = 'SN-999' WHERE reading_id = 4;
DELETE FROM v_reading_full WHERE reading_id = 4;
UPDATE v_reading_left SET value = 1.00 WHERE sensor_id = 1;
UPDATE v_sensor_load  SET readings = 9 WHERE sensor_id = 1;
UPDATE v_sensor_count SET unit = 'K' WHERE sensor_id = 1;
```

**Output**

```
TABLE_NAME	IS_UPDATABLE
v_reading_full	YES
v_reading_left	NO
v_sensor_count	YES
v_sensor_load	NO
reading_id	value
4	79.90
ERROR 1393 (HY000) at line 9: Can not modify more than one base table through a join view 'plant.v_reading_full'
ERROR 1395 (HY000) at line 10: Can not delete from join view 'plant.v_reading_full'
ERROR 1288 (HY000) at line 11: The target table v_reading_left of the UPDATE is not updatable
ERROR 1288 (HY000) at line 12: The target table v_sensor_load of the UPDATE is not updatable
ERROR 1288 (HY000) at line 13: The target table v_sensor_count of the UPDATE is not updatable
```

The real boundary is not the JOIN. A view with an `INNER JOIN` does accept writes, as long as it touches a single base table and it is not a `DELETE`. Where the boundary does fall is on the outer join, on the aggregation and on the scalar subquery.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four `IS_UPDATABLE` values | 3 |
| The five results with their error number | 4 |
| `v_sensor_count` is identified as the disagreement | 2 |
| The working rule of testing the UPDATE is stated | 1 |

**Most common mistake**

Predicting `NO` for `v_reading_full` by repeating that «a view with a JOIN is not updatable»; it gives itself away because the catalogue says `YES` and the single-base-table `UPDATE` did move the row.

### 12.2 · Apply

**Solution**

```sql
USE plant;
-- Layer 1: cleans and renames, one table only
CREATE OR REPLACE VIEW v_machine_base AS
SELECT machine_id, code, name, line_id, status, criticality FROM machine;

-- Layer 2: the maintenance rule, on layer 1
CREATE OR REPLACE VIEW v_machine_critical AS
SELECT machine_id, code, name, line_id FROM v_machine_base
 WHERE criticality = 'high' AND status = 'running';

-- Layer 3: aggregates and flattens
CREATE OR REPLACE VIEW v_load_by_line AS
SELECT line_id, COUNT(*) AS machines FROM v_machine_base GROUP BY line_id;

SELECT * FROM v_machine_critical;
SELECT * FROM v_load_by_line ORDER BY line_id;

UPDATE v_machine_base   SET criticality = 'high' WHERE machine_id = 3;
SELECT machine_id, criticality FROM machine WHERE machine_id = 3;
UPDATE v_load_by_line   SET machines = 9 WHERE line_id = 1;

-- The coordinator's view, left open
CREATE OR REPLACE VIEW v_machine_assembly_open AS
SELECT machine_id, code, name, line_id, installed_on, status
  FROM machine WHERE line_id = 1;
INSERT INTO v_machine_assembly_open
  (machine_id, code, name, line_id, installed_on, status)
VALUES (21,'EQ-0021','Inspection table', 3, '2026-03-01','running');
SELECT COUNT(*) AS the_coordinator_sees_it FROM v_machine_assembly_open WHERE machine_id = 21;
SELECT COUNT(*) AS it_is_in_the_table      FROM machine WHERE machine_id = 21;

-- Closed
CREATE OR REPLACE VIEW v_machine_assembly AS
SELECT machine_id, code, name, line_id, installed_on, status
  FROM machine WHERE line_id = 1
WITH CHECK OPTION;
INSERT INTO v_machine_assembly
  (machine_id, code, name, line_id, installed_on, status)
VALUES (20,'EQ-0020','Inspection table', 3, '2026-03-01','running');
SELECT CHECK_OPTION FROM information_schema.VIEWS
 WHERE TABLE_SCHEMA='plant' AND TABLE_NAME='v_machine_assembly';

DELETE FROM machine WHERE machine_id = 21;
```

**Output**

```
machine_id	code	name	line_id
1	EQ-0001	Hydraulic press 200 t Kühn	1
2	EQ-0002	Welding robot	1
line_id	machines
1	3
2	3
3	2
machine_id	criticality
3	high
ERROR 1288 (HY000) at line 20: The target table v_load_by_line of the UPDATE is not updatable
the_coordinator_sees_it
0
it_is_in_the_table
1
ERROR 1369 (HY000) at line 37: CHECK OPTION failed 'plant.v_machine_assembly'
CHECK_OPTION
CASCADED
```

Layer 2 is still updatable even though it is built on another view, because underneath there is a single base table. Layer 3 could not have done anything else: each of its rows summarises several from the table, so there is no row an `UPDATE` could go and modify. If the view looks like a report, it is read only.

Without `WITH CHECK OPTION` the row went into the table and disappeared from the screen of the person who wrote it: 0 in the view and 1 in the base table.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three layers, each one resting on the previous one and not on the table | 3 |
| The three `UPDATE` attempts, with their output | 3 |
| Why the report layer cannot accept writes is explained | 1 |
| The lost row is demonstrated with the two counts, 0 and 1 | 2 |
| The `WITH CHECK OPTION` stops it with the 1369 | 1 |

**Most common mistake**

Building layer 2 on the base table instead of on layer 1; it gives itself away because the script still works and the exercise loses its point, which was to measure whether stacking views breaks updatability.

### 12.3 · Integrate

**Solution**

```sql
USE plant;
-- 1. The asterisk
CREATE OR REPLACE VIEW v_part_star AS SELECT * FROM part;
ALTER TABLE part ADD COLUMN location VARCHAR(20) NULL;
SELECT * FROM v_part_star WHERE part_id = 1;
SELECT * FROM part       WHERE part_id = 1;
SHOW CREATE VIEW v_part_star;
ALTER TABLE part DROP COLUMN location;

-- 2. The order
CREATE OR REPLACE VIEW v_order_desc AS
SELECT work_order_id, folio, machine_id FROM work_order ORDER BY folio DESC;
SELECT folio FROM v_order_desc LIMIT 3;
SELECT v.folio FROM v_order_desc v JOIN machine e ON e.machine_id = v.machine_id LIMIT 3;

-- 3. The speed
EXPLAIN SELECT reading_id, sensor, machine, value FROM v_reading_full;

SELECT TABLE_NAME, DEFINER, SECURITY_TYPE FROM information_schema.VIEWS
 WHERE TABLE_SCHEMA='plant' AND TABLE_NAME='v_reading_full';
```

**Output**

```
part_id	code	description	on_hand	reorder_point
1	RF-001	Air filter 50% efficiency	12	4
part_id	code	description	on_hand	reorder_point	location
1	RF-001	Air filter 50% efficiency	12	4	NULL
View	Create View	character_set_client	collation_connection
v_part_star	CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_part_star` AS select `part`.`part_id` AS `part_id`,`part`.`code` AS `code`,`part`.`description` AS `description`,`part`.`on_hand` AS `on_hand`,`part`.`reorder_point` AS `reorder_point` from `part`	utf8mb4	utf8mb4_0900_ai_ci
folio
OT-26012
OT-26011
OT-26010
folio
OT-26001
OT-26002
OT-26003
EXPLAIN
-> Nested loop inner join  (cost=7.95 rows=20)
    -> Nested loop inner join  (cost=2.95 rows=6)
        -> Table scan on s  (cost=0.85 rows=6)
        -> Single-row index lookup on e using PRIMARY (machine_id = s.machine_id)  (cost=0.267 rows=1)
    -> Index lookup on r using sensor_id (sensor_id = s.sensor_id)  (cost=0.556 rows=3.33)

TABLE_NAME	DEFINER	SECURITY_TYPE
v_reading_full	root@localhost	DEFINER
```

The view returns five columns and the table six. `SHOW CREATE VIEW` explains why: MySQL expanded the asterisk when the view was created and stored the list of columns that existed that day. The new column will never appear, and there is no error or warning that says so.

The same view came out in two different orders depending on how it was queried. The order belongs to the final query, not to the object.

The plan names `r`, `s` and `e`. The name `v_reading_full` appears zero times, because the algorithm is `MERGE`: the view is replaced by its text and what gets optimised are the base tables. Saving a query does not speed it up.

The `DEFINER` ended up as `root@localhost` with `SQL SECURITY DEFINER`, and nobody asked for it. That gets charged in week 17, when the view runs with the permissions of whoever created it and not with those of whoever queries it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two asterisk outputs, of five and six columns, with `SHOW CREATE VIEW` | 3 |
| The two orders of the same view, and who the order belongs to | 3 |
| The plan pasted, with the count of how many times it names the view | 2 |
| The `DEFINER` reported and placed in week 17 | 2 |

**Most common mistake**

Running the `EXPLAIN` with a filter by key, which collapses the tree to a single row; it gives itself away because the three tables are no longer visible and the argument that the view does not appear is left with no evidence.

---

## Week 13 · Procedures and errors · Second midterm

### 13.1 · Recognise

**Solution**

```sql
-- CALL sp_bad(1) answers 20, which is every row of the table.
-- The WHERE compared the parameter with itself: sensor_id = sensor_id is true
-- on every row where it is not empty. The column was shadowed by the parameter,
-- which carries the same name and wins.
-- The only change that fixes it is renaming the parameter:  p_sensor_id.
-- With that name it answers 4.

-- The four SIGNAL statements
-- '45000' 'Operation not allowed' ............ ERROR 1644 (45000)
-- '23000' 'Integrity violated' ............... ERROR 1644 (23000)
-- '22012' 'Division by zero' ................. ERROR 1644 (22012)
-- '45000' + MYSQL_ERRNO = 3001 ............... ERROR 3001 (45000)
-- SIGNAL always comes out as 1644, whichever SQLSTATE you pick. The SQLSTATE is
-- a label the server carries along. MYSQL_ERRNO is the only thing your
-- application can use to tell an error of yours from another one.

USE plant;
DROP PROCEDURE IF EXISTS sp_bad;
DROP PROCEDURE IF EXISTS sp_good;
DELIMITER $$
CREATE PROCEDURE sp_bad(IN sensor_id INT)
BEGIN
  SELECT COUNT(*) AS rows_returned FROM reading WHERE sensor_id = sensor_id;
END$$
CREATE PROCEDURE sp_good(IN p_sensor_id INT)
BEGIN
  SELECT COUNT(*) AS rows_returned FROM reading WHERE sensor_id = p_sensor_id;
END$$
DELIMITER ;
CALL sp_bad(1);
CALL sp_good(1);
```

**Output**

```
rows_returned
20
rows_returned
4
ERROR 1644 (45000) at line 32: Operation not allowed
ERROR 1644 (23000) at line 33: Integrity violated
ERROR 1644 (22012) at line 34: Division by zero
ERROR 3001 (45000) at line 35: Value off the sensor scale
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| 20 is predicted and the `WHERE` is explained as comparing the parameter with itself | 4 |
| The fix is renaming the parameter, and with it the answer is 4 | 2 |
| The four error numbers: three 1644 and one 3001 | 3 |
| `MYSQL_ERRNO` is named as the only piece that tells them apart | 1 |

**Most common mistake**

Predicting 4 because «the procedure receives 1»; it gives itself away on running it, and the cause shows the moment the parameter name is changed and the answer changes without the `WHERE` being touched.

### 13.2 · Apply

**Solution**

```sql
USE plant;
DROP PROCEDURE IF EXISTS sp_machine_load;   -- without this the second run
DELIMITER $$                                -- dies with ERROR 1305
CREATE PROCEDURE sp_machine_load(IN p_machine_id INT, OUT p_orders INT)
BEGIN
  -- The p_ prefix is not style: without it, p_machine_id would shadow the
  -- machine_id column and the WHERE would compare with itself, as in 13.1.
  SELECT COUNT(*) INTO p_orders FROM work_order WHERE machine_id = p_machine_id;
  SELECT e.code, e.name, COUNT(o.work_order_id) AS orders, SUM(o.hours) AS hours
    FROM machine e
    LEFT JOIN work_order o ON o.machine_id = e.machine_id
   WHERE e.machine_id = p_machine_id
   GROUP BY e.machine_id, e.code, e.name;
END$$
DELIMITER ;

CALL sp_machine_load(2, @n);
SELECT @n AS orders_of_machine_2;

CALL sp_machine_load(2, 5);

DROP PROCEDURE IF EXISTS sp_accumulate;
DELIMITER $$
CREATE PROCEDURE sp_accumulate(IN p_sensor_id INT, OUT p_total INT, INOUT p_running INT)
BEGIN
  SELECT COUNT(*) INTO p_total FROM reading WHERE sensor_id = p_sensor_id;
  SET p_running = p_running + p_total;
END$$
DELIMITER ;
SET @running = 100;
CALL sp_accumulate(1, @tot, @running);
SELECT @tot AS total, @running AS accumulated;
```

**Output**

```
code	name	orders	hours
EQ-0002	Welding robot	3	10.25
orders_of_machine_2
3
ERROR 1414 (42000) at line 20: OUT or INOUT argument 2 for routine plant.sp_machine_load is not a variable or NEW pseudo-variable in BEFORE trigger
total	accumulated
4	104
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The procedure is created with `DELIMITER` and with `DROP ... IF EXISTS` | 2 |
| It returns the four columns on screen and the count through the output parameter | 3 |
| It reuses the `LEFT JOIN` and the grouping without rewriting them | 1 |
| The 1414 provoked and pasted | 2 |
| The `INOUT` goes in at 100 and comes out at 104 | 2 |

**Most common mistake**

Leaving out the `DROP PROCEDURE IF EXISTS`; it gives itself away on the second run of the script with `ERROR 1305 (42000) PROCEDURE already exists`, which is exactly when the student is debugging.

### 13.3 · Integrate

**Solution**

```sql
USE plant;
DROP PROCEDURE IF EXISTS sp_two_steps;
DELIMITER $$
CREATE PROCEDURE sp_two_steps()
BEGIN
  INSERT INTO reading VALUES (101, 6, '2026-03-03 06:00:00', 8.90);
  INSERT INTO reading VALUES (102, 99,'2026-03-03 07:00:00', 9.10);
END$$
DELIMITER ;
SELECT COUNT(*) AS before_call FROM reading;
CALL sp_two_steps();
SELECT COUNT(*) AS after_call FROM reading;
SELECT reading_id, sensor_id, value FROM reading WHERE reading_id = 101;
DELETE FROM reading WHERE reading_id = 101;

DROP PROCEDURE IF EXISTS sp_two_steps_safe;
DELIMITER $$
CREATE PROCEDURE sp_two_steps_safe(OUT p_result VARCHAR(600))
BEGIN
  DECLARE v_sqlstate CHAR(5);
  DECLARE v_errno    INT;
  DECLARE v_text     VARCHAR(400);
  DECLARE integrity_broken CONDITION FOR SQLSTATE '23000';
  DECLARE EXIT HANDLER FOR integrity_broken
  BEGIN
    GET DIAGNOSTICS CONDITION 1
      v_sqlstate = RETURNED_SQLSTATE,
      v_errno    = MYSQL_ERRNO,
      v_text     = MESSAGE_TEXT;
    ROLLBACK;                                  -- the handler does not bring one
    SET p_result = CONCAT('rejected [', v_sqlstate, '/', v_errno, '] ', v_text);
  END;
  START TRANSACTION;
  INSERT INTO reading VALUES (101, 6, '2026-03-03 06:00:00', 8.90);
  INSERT INTO reading VALUES (102, 99,'2026-03-03 07:00:00', 9.10);
  COMMIT;
  SET p_result = 'accepted';
END$$
DELIMITER ;
SELECT COUNT(*) AS before_call FROM reading;
CALL sp_two_steps_safe(@r);
SELECT @r AS result;
SELECT COUNT(*) AS after_call FROM reading;

DROP PROCEDURE IF EXISTS sp_two_steps_strict;
DELIMITER $$
CREATE PROCEDURE sp_two_steps_strict()
BEGIN
  DECLARE EXIT HANDLER FOR SQLSTATE '23000'
  BEGIN
    ROLLBACK;
    RESIGNAL SET MYSQL_ERRNO = 3101,
      MESSAGE_TEXT = 'That sensor is not in the plant catalogue';
  END;
  START TRANSACTION;
  INSERT INTO reading VALUES (101, 6, '2026-03-03 06:00:00', 8.90);
  INSERT INTO reading VALUES (102, 99,'2026-03-03 07:00:00', 9.10);
  COMMIT;
END$$
DELIMITER ;
CALL sp_two_steps_strict();
SELECT COUNT(*) AS at_the_end FROM reading;
```

**Output**

```
before_call
20
ERROR 1452 (23000) at line 11: Cannot add or update a child row: a foreign key constraint fails (`plant`.`reading`, CONSTRAINT `reading_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))
after_call
21
reading_id	sensor_id	value
101	6	8.90
before_call
20
result
rejected [23000/1452] Cannot add or update a child row: a foreign key constraint fails (`plant`.`reading`, CONSTRAINT `reading_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))
after_call
20
ERROR 3101 (23000) at line 61: That sensor is not in the plant catalogue
at_the_end
20
```

The error arrived late because the server checks the foreign key when it executes the second statement, not when it creates the procedure. By then the first row was already written, and with no transaction open it had already committed itself.

`SQLSTATE 23000` does not mean duplicate. It is produced by the duplicate (1062), the broken foreign key (1452) and the violated `NOT NULL` (1048). The handler above catches all three, even though its name promises only one.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The version with no handler leaves the first row and it is shown with the counts | 2 |
| The handler catches the error and the procedure ends without blowing up | 3 |
| `GET DIAGNOSTICS` recovers the three pieces and the `ROLLBACK` is written by hand | 2 |
| The counts before and after both come out at 20 | 1 |
| The `RESIGNAL` comes out as 3101 with a readable message | 1 |
| The three situations behind 23000 are named | 1 |

**Most common mistake**

Assuming the `EXIT HANDLER` undoes on its own; it gives itself away because the count afterwards stays at 21, since the handler stops the block but the `ROLLBACK` has to be written on the line below.

---

## Week 14 · Triggers and events

### 14.1 · Recognise

**Solution**

```sql
-- Moment           OLD           NEW
-- BEFORE INSERT    absent        read and written
-- AFTER  INSERT    absent        read
-- BEFORE UPDATE    read          read and written
-- AFTER  UPDATE    read          read
-- BEFORE DELETE    read          absent
-- AFTER  DELETE    read          absent

-- 1. OLD in an INSERT trigger: ERROR 1363 (HY000) There is no OLD row in on
--    INSERT trigger. It appears on CREATING it, not on firing it.
-- 2. With 742.00 the trigger raises 1644 and the row does not go in.
--    With the empty value, NEW.value < 0 does not answer false: it answers
--    unknown, and unknown is not true, so the IF is not entered and the row
--    passes. The guard:
--      IF NEW.value IS NOT NULL AND (NEW.value < 0 OR NEW.value > 500)
-- 3. The trigger raises 1644 with the message you wrote.
--    The CHECK raises 3819 with the name of the constraint and nothing else.

USE auto;
DELIMITER $$
CREATE TRIGGER trg_reading_before_insert_old
BEFORE INSERT ON reading FOR EACH ROW
BEGIN
  IF OLD.value > 500 THEN SET NEW.value = 500; END IF;
END$$

CREATE TRIGGER trg_reading_before_insert_raw
BEFORE INSERT ON reading FOR EACH ROW
BEGIN
  IF NEW.value < 0 OR NEW.value > 500 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Value off the sensor scale';
  END IF;
END$$
DELIMITER ;
INSERT INTO reading VALUES (4,1,'2026-03-02 08:00:00',742.00);
INSERT INTO reading VALUES (5,1,'2026-03-02 09:00:00',NULL);
SELECT reading_id, value FROM reading WHERE reading_id = 5;

CREATE TABLE reading_check (
  reading_id INT PRIMARY KEY,
  value      DECIMAL(7,2) NULL,
  CONSTRAINT ck_reading_scale CHECK (value BETWEEN 0 AND 500)
);
INSERT INTO reading_check VALUES (1, 742.00);
INSERT INTO reading       VALUES (6,1,'2026-03-02 10:00:00',742.00);
```

**Output**

```
ERROR 1363 (HY000) at line 4: There is no OLD row in on INSERT trigger
ERROR 1644 (45000) at line 19: Value off the sensor scale
reading_id	value
5	NULL
ERROR 3819 (HY000) at line 29: Check constraint 'ck_reading_scale' is violated.
ERROR 1644 (45000) at line 30: Value off the sensor scale
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The table of the six moments complete | 3 |
| The 1363 and the moment it appears, on creating the trigger | 2 |
| The two cases of the unguarded validation, and the guard written out | 3 |
| The two numbers, 1644 and 3819, and what the user gets to read in each | 2 |

**Most common mistake**

Saying the 1363 comes out on inserting; it gives itself away because the trigger never gets to exist, so there is nothing to fire.

### 14.2 · Apply

**Solution**

```sql
USE auto;
DELIMITER $$
CREATE TRIGGER trg_reading_before_insert_validate
BEFORE INSERT ON reading FOR EACH ROW
BEGIN
  IF NEW.value IS NOT NULL AND (NEW.value < 0 OR NEW.value > 500) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Value off the sensor scale';
  END IF;
END$$

CREATE TRIGGER trg_reading_after_update_log
AFTER UPDATE ON reading FOR EACH ROW
BEGIN
  INSERT INTO reading_log
    (reading_id, value_before, value_after, action, changed_at)
  VALUES (OLD.reading_id, OLD.value, NEW.value, 'UPDATE', NOW());
END$$
DELIMITER ;

INSERT INTO reading VALUES (4,1,'2026-03-02 08:00:00',742.00);
INSERT INTO reading VALUES (5,1,'2026-03-02 09:00:00',NULL);
SELECT reading_id, value FROM reading WHERE reading_id = 5;

UPDATE reading SET value = 68.00 WHERE reading_id = 1;
SELECT reading_id, value_before, value_after, action FROM reading_log;
```

**Output**

```
ERROR 1644 (45000) at line 20: Value off the sensor scale
reading_id	value
5	NULL
reading_id	value_before	value_after	action
1	71.50	68.00	UPDATE
```

The name `trg_reading_before_insert_validate` states the table, the moment, the event and the purpose, so a `SHOW TRIGGERS` reads without opening the body.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The validation trigger rejects 742.00 with the 1644 | 3 |
| The guard for the empty value is in place and the empty reading goes in | 3 |
| The log leaves `OLD` and `NEW` on the same row | 3 |
| The names follow the convention of table, moment, event and purpose | 1 |

**Most common mistake**

Writing the log trigger as `BEFORE UPDATE` and reading `NEW` expecting the confirmed value; it gives itself away when another trigger at the same moment changes `NEW` afterwards and the log records a value that was never stored.

### 14.3 · Integrate

**Solution**

```sql
USE auto;
-- The trigger that ought to see the disappearance
DELIMITER $$
CREATE TRIGGER trg_reading_before_delete_log
BEFORE DELETE ON reading FOR EACH ROW
BEGIN
  INSERT INTO reading_log
    (reading_id, value_before, value_after, action, changed_at)
  VALUES (OLD.reading_id, OLD.value, NULL, 'DELETE', NOW());
END$$
DELIMITER ;

SELECT COUNT(*) AS readings_of_sensor_3 FROM reading WHERE sensor_id = 3;
SELECT COUNT(*) AS log_before FROM reading_log;
DELETE FROM sensor WHERE sensor_id = 3;          -- the FK is ON DELETE CASCADE
SELECT COUNT(*) AS readings_of_sensor_3 FROM reading WHERE sensor_id = 3;
SELECT COUNT(*) AS log_after FROM reading_log;

SELECT COUNT(*) AS readings_before FROM reading;
TRUNCATE TABLE reading;
SELECT COUNT(*) AS readings_after FROM reading;
SELECT COUNT(*) AS log_at_the_end FROM reading_log;

-- The events
SHOW VARIABLES LIKE 'event_scheduler';
CREATE EVENT ev_shift_close
ON SCHEDULE AT '2026-03-20 08:00:00'
DO DELETE FROM reading_log WHERE action = 'DELETE';
SHOW WARNINGS;
SELECT COUNT(*) AS events_in_the_catalogue FROM information_schema.EVENTS
 WHERE EVENT_SCHEMA = 'auto';

CREATE EVENT ev_purge_log
ON SCHEDULE EVERY 1 DAY
DO DELETE FROM reading_log WHERE changed_at < NOW() - INTERVAL 30 DAY;
SELECT EVENT_NAME, EVENT_TYPE, INTERVAL_VALUE, INTERVAL_FIELD, STATUS
  FROM information_schema.EVENTS WHERE EVENT_SCHEMA = 'auto';
```

**Output**

```
readings_of_sensor_3
1
log_before
1
readings_of_sensor_3
0
log_after
1
readings_before
3
readings_after
0
log_at_the_end
1
Variable_name	Value
event_scheduler	ON
Level	Code	Message
Note	1588	Event execution time is in the past and ON COMPLETION NOT PRESERVE is set. The event was dropped immediately after creation.
events_in_the_catalogue
0
EVENT_NAME	EVENT_TYPE	INTERVAL_VALUE	INTERVAL_FIELD	STATUS
ev_purge_log	RECURRING	1	DAY	ENABLED
```

A trigger sees the statements somebody writes against its table. It does not see the cascading delete, which the foreign key engine carries out internally, and it does not see the `TRUNCATE`, which really drops the table and creates it again empty. Three readings disappeared and the log stayed at one row, the one from the `UPDATE` in 14.2.

The mechanism that does record both disappearances is not delegating the delete to the engine: remove the `ON DELETE CASCADE` and delete the children with an explicit `DELETE`, in a procedure or in a trigger on the parent. The `TRUNCATE` is closed off through permissions, by denying `DROP` on that table.

The event with a past date was created without an error and it is not in the catalogue. The `CREATE` succeeded, `SHOW WARNINGS` carries note 1588, and `information_schema.EVENTS` comes back empty.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four counts of the cascade, with the log that does not grow | 3 |
| The three counts of the `TRUNCATE`, with the same result | 2 |
| What a trigger sees and does not see is explained, and the mechanism that does is proposed | 2 |
| The event with a past date, with note 1588 and the empty catalogue | 2 |
| The recurring event appears with its type, interval and status | 1 |

**Most common mistake**

Reporting that «the log does work» because the `UPDATE` row is still there; it gives itself away on comparing the counts before and after the delete, which is the number the exercise asks for and not the contents of the table.

---

## Week 15 · Indexes and performance

### 15.1 · Recognise

**Solution**

```sql
-- WHERE machine_id = 42
--   type=ref  key=idx_eq_date  key_len=4  rows=4  Extra=Using index
-- WHERE machine_id = 42 AND taken_at = '2026-01-15'
--   type=ref  key=idx_eq_date  key_len=7  rows=1  Extra=Using index
-- WHERE taken_at = '2026-01-15'
--   type=index  key=idx_eq_date  key_len=7  rows=199655

-- The third one: the index appears in key and the type is index, not ref. That
-- is not a search, it is walking the whole index end to end. The leftmost
-- prefix rule says a composite index serves the first column, or the first
-- plus the second, but not the second on its own. All it gained is walking the
-- index instead of the table, which is narrower.

-- With (shift, value) and a filter on value alone, with shift holding four
-- distinct values, the server does a group jump: it walks the index once for
-- each value of shift. It is called a skip scan and it does not exist in
-- MySQL 5.7.

USE perf;
EXPLAIN FORMAT=TRADITIONAL
SELECT reading_id FROM reading_big WHERE machine_id = 42;
EXPLAIN FORMAT=TRADITIONAL
SELECT reading_id FROM reading_big WHERE machine_id = 42 AND taken_at = '2026-01-15';
EXPLAIN FORMAT=TRADITIONAL
SELECT reading_id FROM reading_big WHERE taken_at = '2026-01-15';

EXPLAIN SELECT reading_id FROM reading_big WHERE value = 9.50;
```

**Output**

```
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	reading_big	NULL	ref	idx_eq_date	idx_eq_date	4	const	4	100.00	Using index
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	reading_big	NULL	ref	idx_eq_date	idx_eq_date	7	const,const	1	100.00	Using index
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	reading_big	NULL	index	idx_eq_date	idx_eq_date	7	NULL	199655	10.00	Using where; Using index
EXPLAIN
-> Filter: (reading_big.`value` = 9.50)  (cost=8561 rows=33275)
    -> Covering index skip scan on reading_big using idx_shift_value over value = 9.50  (cost=8561 rows=33275)
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three `type` values: ref, ref, index | 3 |
| The three `rows` values: 4, 1 and close to 200 000 | 2 |
| The third one is explained with the leftmost prefix rule | 3 |
| The group jump is named and said not to be in 5.7 | 2 |

**Most common mistake**

Concluding that the third query uses the index because `key` names it; it gives itself away with `rows`, which comes close to the total of the table, and with `type=index`, which is a full walk and not a search.

### 15.2 · Apply

**Solution**

```sql
USE perf;
-- Starting point: no secondary index on either table
DROP INDEX idx_eq_date     ON reading_big;
DROP INDEX idx_shift_value ON reading_big;
ANALYZE TABLE reading_big, machine_big;

-- Warm-up, so the first trip to disc is not what gets timed
SELECT COUNT(*) INTO @n FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id WHERE e.code = 'EQ-000042';

EXPLAIN FORMAT=TRADITIONAL
SELECT r.reading_id, e.code FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id WHERE e.code = 'EQ-000042';
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id WHERE e.code = 'EQ-000042';
SELECT @n AS rows_returned, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_without_index;

CREATE INDEX idx_rb_machine ON reading_big (machine_id);
CREATE INDEX idx_mb_code    ON machine_big (code);
ANALYZE TABLE reading_big, machine_big;
SELECT COUNT(*) INTO @n FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id WHERE e.code = 'EQ-000042';

EXPLAIN FORMAT=TRADITIONAL
SELECT r.reading_id, e.code FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id WHERE e.code = 'EQ-000042';
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM reading_big r
  JOIN machine_big e ON e.machine_id = r.machine_id WHERE e.code = 'EQ-000042';
SELECT @n AS rows_returned, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_with_index;
```

**Output**

```
Table	Op	Msg_type	Msg_text
perf.reading_big	analyze	status	OK
perf.machine_big	analyze	status	OK
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	r	NULL	ALL	NULL	NULL	NULL	NULL	199655	100.00	NULL
1	SIMPLE	e	NULL	eq_ref	PRIMARY	PRIMARY	4	perf.r.machine_id	1	10.00	Using where
rows_returned	ms_without_index
4	150.4340
Table	Op	Msg_type	Msg_text
perf.reading_big	analyze	status	OK
perf.machine_big	analyze	status	OK
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	e	NULL	ref	PRIMARY,idx_mb_code	idx_mb_code	36	const	1	100.00	Using where; Using index
1	SIMPLE	r	NULL	ref	idx_rb_machine	idx_rb_machine	4	perf.e.machine_id	3	100.00	Using index
rows_returned	ms_with_index
4	0.1850
```

With no indexes the server walks the 199 655 estimated rows of `reading_big` and for each one goes off to find its machine, only to return 4 in the end. With the two indexes the order flips: first it finds the machine by its code, and from there it drops to its 3 estimated readings. From 199 655 rows examined down to 4, and from 150.434 ms down to 0.185 ms.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two plans pasted, before and after | 3 |
| The rows examined in each case, with the `type` that explains them | 3 |
| The two times, measured after the warm-up | 3 |
| The `CREATE INDEX` that goes in the middle is left in plain sight | 1 |

**Most common mistake**

Timing the first shot against a cold disc and reporting that figure as the starting point; it gives itself away because the improvement comes out exaggerated and does not reproduce when the two measurements are run again.

### 15.3 · Integrate

**Solution**

```sql
USE perf;
CREATE INDEX idx_title ON message (title(60));

EXPLAIN FORMAT=TRADITIONAL
SELECT message_id FROM message WHERE title LIKE 'Shutdown from vibration%';
EXPLAIN FORMAT=TRADITIONAL
SELECT message_id FROM message WHERE title LIKE '%vibration%';
EXPLAIN FORMAT=TRADITIONAL
SELECT message_id FROM message WHERE title REGEXP '^Shutdown from vibration';

SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM message WHERE title LIKE 'Shutdown from vibration%';
SELECT @n AS rows_returned, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_anchored;
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM message WHERE title LIKE '%vibration%';
SELECT @n AS rows_returned, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_leading_wildcard;

SELECT message_id FROM message WHERE MATCH(body) AGAINST ('vibration');
ALTER TABLE message ADD FULLTEXT (message_id);

SET @t0 = NOW(6);
ALTER TABLE message ADD FULLTEXT ft_body (body);
SHOW WARNINGS;
SELECT TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_to_build;

SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM message WHERE MATCH(body) AGAINST ('vibration');
SELECT @n AS rows_returned, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_match;
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM message WHERE body LIKE '%vibration%';
SELECT @n AS rows_returned, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_like;

-- The other side of the bet
CREATE TABLE load_without (
  reading_id INT PRIMARY KEY, machine_id INT, taken_at DATE,
  shift VARCHAR(12), value DECIMAL(7,2));
CREATE TABLE load_with (
  reading_id INT PRIMARY KEY, machine_id INT, taken_at DATE,
  shift VARCHAR(12), value DECIMAL(7,2),
  INDEX i1 (machine_id), INDEX i2 (taken_at), INDEX i3 (shift),
  INDEX i4 (value), INDEX i5 (machine_id, taken_at), INDEX i6 (shift, value),
  INDEX i7 (taken_at, value), INDEX i8 (machine_id, value));
SET @t0 = NOW(6);
INSERT INTO load_without SELECT * FROM reading_big;
SELECT TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_without_indexes;
SET @t0 = NOW(6);
INSERT INTO load_with SELECT * FROM reading_big;
SELECT TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_with_eight_indexes;
ANALYZE TABLE load_without, load_with;
SELECT TABLE_NAME, DATA_LENGTH, INDEX_LENGTH FROM information_schema.TABLES
 WHERE TABLE_SCHEMA='perf' AND TABLE_NAME LIKE 'load_%';
```

**Output**

```
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	message	NULL	range	idx_title	idx_title	242	NULL	14320	100.00	Using where; Using index
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	message	NULL	ALL	NULL	NULL	NULL	NULL	59478	11.11	Using where
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	message	NULL	ALL	NULL	NULL	NULL	NULL	59478	100.00	Using where
rows_returned	ms_anchored
7500	8.1890
rows_returned	ms_leading_wildcard
7500	12.3950
ERROR 1191 (HY000) at line 18: Can't find FULLTEXT index matching the column list
ERROR 1283 (HY000) at line 19: Column 'message_id' cannot be part of FULLTEXT index
Level	Code	Message
Warning	124	InnoDB rebuilding table to add column FTS_DOC_ID
ms_to_build
7576.7370
rows_returned	ms_match
7500	3.1850
rows_returned	ms_like
7500	40.6290
ms_without_indexes
793.1860
ms_with_eight_indexes
3796.9440
Table	Op	Msg_type	Msg_text
perf.load_without	analyze	status	OK
perf.load_with	analyze	status	OK
TABLE_NAME	DATA_LENGTH	INDEX_LENGTH
load_with	9977856	44171264
load_without	9977856	0
```

The three verdicts. The `LIKE` anchored at the start holds: `type=range` and 14 320 rows examined against 59 478. The `LIKE` with the wildcard at the start falls: `type=ALL`, the whole table. The anchored `REGEXP` falls too, and there the inherited advice was exactly backwards: it recommended `REGEXP` over `LIKE`, and not even with an anchor does it use the index.

Full text costs 7 576 ms to build, rewrites the table to add a hidden `FTS_DOC_ID` column, and in exchange answers the same question in 3.185 ms against 40.629 ms for the `LIKE`. That is 12.8 times, over the same column and the same 60 000 rows.

The other side of the bet: eight indexes too many cost 4.79 times the load (793.186 ms against 3 796.944 ms) and weigh 4.43 times what the data weighs (44 171 264 against 9 977 856). An index no query uses is pure cost.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three plans of the `LIKE` and the `REGEXP`, with their `type` and their rows | 3 |
| One verdict per branch, each with its evidence | 2 |
| The two full-text errors, 1191 and 1283 | 1 |
| The build cost and the time comparison against `LIKE` | 2 |
| The two load times and the two lengths, with their ratio | 2 |

**Most common mistake**

Reporting that `LIKE '%vibration%'` is not that bad because it took 12 ms; it gives itself away with the rows examined, 59 478 against 14 320, which is the number that scales when the table grows and the time does not.

---

## Week 16 · Concurrency and locking · Project

### 16.1 · Recognise

**Solution**

```sql
-- A read 25.  B read 25.  The part is left at 20.
-- Ten pieces left the store and the system says five did.
-- Nobody wrote anything wrong. The hole sits between reading and writing:
-- B read 211 ms after A, when A had not written anything yet.

-- With FOR UPDATE:  A reads 25 and writes 20.  B waits for A to COMMIT, reads
-- 20 and writes 15.  Final 15.
-- Without reading:  UPDATE ... SET on_hand = on_hand - 5.  Final 15.
-- The difference: FOR UPDATE keeps the read, so the application can decide with
-- the right value before writing. The second one reads nothing, so it settles
-- the count and is no use when something has to be checked before subtracting.

USE conc;
START TRANSACTION;
SELECT on_hand INTO @c FROM part WHERE part_id = 3;
SELECT 'A_read' AS session, @c AS on_hand, NOW(6) AS at_time;
SELECT SLEEP(1) INTO @z;
UPDATE part SET on_hand = @c - 5 WHERE part_id = 3;
SELECT 'A_wrote' AS session, @c - 5 AS left_behind, NOW(6) AS at_time;
COMMIT;
```

**Output**

```
--- session A ---
session	on_hand	at_time
A_read	25	2026-08-18 00:16:49.594981
session	left_behind	at_time
A_wrote	20	2026-08-18 00:16:50.609654
--- session B ---
session	on_hand	at_time
B_read	25	2026-08-18 00:16:49.806316
session	left_behind	at_time
B_wrote	20	2026-08-18 00:16:50.806691
--- afterwards ---
part_id	final_result
3	20
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three numbers: 25, 25 and 20 | 3 |
| The answer says ten pieces left and the system records five | 2 |
| The two repairs both reach 15 | 2 |
| The hole is placed between the read and the write | 2 |
| The difference between the two repairs is explained | 1 |

**Most common mistake**

Predicting 15 because «both of them subtracted five»; it gives itself away with the timestamps, which show that both read the same 25 before either one wrote.

### 16.2 · Apply

**Solution**

```sql
-- Both sessions run the same script, 200 ms apart.
-- Session A and session B, with no lock:
USE conc;
START TRANSACTION;
SELECT on_hand INTO @c FROM part WHERE part_id = 3;
SELECT 'A_read' AS session, @c AS on_hand, NOW(6) AS at_time;
SELECT SLEEP(1) INTO @z;
UPDATE part SET on_hand = @c - 5 WHERE part_id = 3;
SELECT 'A_wrote' AS session, @c - 5 AS left_behind, NOW(6) AS at_time;
COMMIT;

-- Repair 1, the same read with a lock:
SELECT on_hand INTO @c FROM part WHERE part_id = 3 FOR UPDATE;

-- Repair 2, let the server do the subtraction:
UPDATE part SET on_hand = on_hand - 5 WHERE part_id = 3;

-- The 1205. Session A takes the row and sleeps 6 s; session B, timeout 3 s:
SET SESSION innodb_lock_wait_timeout = 3;
START TRANSACTION;
UPDATE part SET on_hand = 7 WHERE part_id = 2;          -- work done before the wait
SELECT on_hand FROM part WHERE part_id = 3;             -- plain read
SELECT on_hand FROM part WHERE part_id = 3 FOR UPDATE;  -- this one waits
COMMIT;

-- The 1213. A takes row 1 and asks for row 3; B takes 3 and asks for 1, at once.
```

**Output**

```
--- no lock ---
session	on_hand	at_time
A_read	25	2026-08-18 00:16:49.594981
session	left_behind	at_time
A_wrote	20	2026-08-18 00:16:50.609654
session	on_hand	at_time
B_read	25	2026-08-18 00:16:49.806316
session	left_behind	at_time
B_wrote	20	2026-08-18 00:16:50.806691
part_id	final_result
3	20

--- with FOR UPDATE ---
session	on_hand	at_time
A_read	25	2026-08-18 00:17:08.861285
session	left_behind	at_time
A_wrote	20	2026-08-18 00:17:09.883774
session	on_hand	at_time
B_read	20	2026-08-18 00:17:09.889465
session	left_behind	at_time
B_wrote	15	2026-08-18 00:17:10.903339
part_id	final_result
3	15

--- letting the server subtract ---
session	at_time
A_wrote	2026-08-18 00:17:12.197197
session	at_time
B_wrote	2026-08-18 00:17:12.414438
part_id	final_result
3	15

--- the 1205 ---
session A
on_hand
25
note	at_time
A took row 3	2026-08-18 00:17:36.821143
session B
note	at_time
B asks for row 3	2026-08-18 00:17:37.130706
on_hand
25
ERROR 1205 (HY000) at line 8: Lock wait timeout exceeded; try restarting transaction
note	at_time
B reached the end	2026-08-18 00:17:40.177155
part_id	on_hand
1	12
2	7
3	25

--- the 1213 ---
session A
note	at_time
A took row 1	2026-08-18 00:17:43.138188
session B
note	at_time
B took row 3	2026-08-18 00:17:43.145409
ERROR 1213 (40001) at line 6: Deadlock found when trying to get lock; try restarting transaction
part_id	on_hand
1	11
2	3
3	24
```

What survived in each case. After the 1205, session B stayed inside its transaction and its `COMMIT` carried the half-done work away with it: part 2 was left at 7, written before the error, while part 3 stayed at 25 because that statement never ran. After the 1213, session B lost the whole transaction: its decrement on part 3 was undone, and the two decrements that remain (11 and 24) are the ones from session A.

The plain read did not wait. It returned 25 straight away, while A held the row, because a read with no lock never waits. The `FOR UPDATE` waited 3.05 s and expired.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three runs with two real sessions and their timestamps | 3 |
| The 1205 with the time it took to arrive | 2 |
| The 1213 provoked | 2 |
| What survived in each case is reported, and it is not the same | 3 |

**Most common mistake**

Retrying both errors the same way, with a `COMMIT` afterwards; it gives itself away in the 1205 case, where the `COMMIT` confirms half-done work nobody checked.

### 16.3 · Integrate

**Solution**

```sql
USE conc;
DELIMITER $$
CREATE PROCEDURE sp_issue(IN p_part_id INT, IN p_quantity INT,
                          OUT p_result VARCHAR(60))
BEGIN
  DECLARE v_have INT;
  START TRANSACTION;
  SELECT on_hand INTO v_have FROM part WHERE part_id = p_part_id;
  SELECT SLEEP(1) INTO @z;                    -- the other session fits in here
  IF v_have >= p_quantity THEN
    UPDATE part SET on_hand = on_hand - p_quantity WHERE part_id = p_part_id;
    INSERT INTO issue (part_id, quantity) VALUES (p_part_id, p_quantity);
    SET p_result = CONCAT('issued, it saw ', v_have);
  ELSE
    SET p_result = CONCAT('refused, it saw ', v_have);
  END IF;
  COMMIT;
END$$

CREATE PROCEDURE sp_issue_safe(IN p_part_id INT, IN p_quantity INT,
                               OUT p_result VARCHAR(60))
BEGIN
  DECLARE v_have INT;
  START TRANSACTION;
  SELECT on_hand INTO v_have FROM part
   WHERE part_id = p_part_id FOR UPDATE;      -- the only difference
  SELECT SLEEP(1) INTO @z;
  IF v_have >= p_quantity THEN
    UPDATE part SET on_hand = on_hand - p_quantity WHERE part_id = p_part_id;
    INSERT INTO issue (part_id, quantity) VALUES (p_part_id, p_quantity);
    SET p_result = CONCAT('issued, it saw ', v_have);
  ELSE
    SET p_result = CONCAT('refused, it saw ', v_have);
  END IF;
  COMMIT;
END$$

CREATE PROCEDURE sp_adjust(IN p_first INT, IN p_second INT, OUT p_attempts INT)
BEGIN
  DECLARE v_failed INT DEFAULT 0;
  DECLARE CONTINUE HANDLER FOR SQLSTATE '40001'
  BEGIN
    ROLLBACK;
    SET v_failed = 1;
  END;
  SET p_attempts = 0;
  retry: LOOP
    SET v_failed = 0;
    SET p_attempts = p_attempts + 1;
    START TRANSACTION;
    UPDATE part SET on_hand = on_hand - 1 WHERE part_id = p_first;
    SELECT SLEEP(1) INTO @z;
    UPDATE part SET on_hand = on_hand - 1 WHERE part_id = p_second;
    IF v_failed = 0 THEN
      COMMIT;
      LEAVE retry;
    END IF;
    IF p_attempts >= 5 THEN LEAVE retry; END IF;
  END LOOP;
END$$
DELIMITER ;
```

**Output**

```
=== without FOR UPDATE, both asking for 20 out of 25 ===
session	result
A	issued, it saw 25
session	result
B	issued, it saw 25
on_hand
-15
issues	pieces
2	40

=== with FOR UPDATE, from the same starting state ===
session	result
A	issued, it saw 25
session	result
B	refused, it saw 5
on_hand
5
issues	pieces
1	20

=== the retry, with the identifiers reversed ===
session	attempts
A	2
session	attempts
B	1
part_id	on_hand
1	10
2	3
3	23
```

Without the lock both sessions saw 25, both decided it was enough and both issued. The store handed out 40 pieces from a stock of 25 and the on-hand figure ended at minus fifteen, with no error and no warning.

With `FOR UPDATE` session B waited for A to commit, read 5 and refused itself. One single issue of 20 pieces and the stock at 5.

The retry recovered the lost work: this time B closed on the first attempt and A needed two, and both parts ended with their two decrements applied, 12 down to 10 and 25 down to 23.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three numbers with no lock: 25 and 25, negative stock and 40 pieces | 3 |
| The three numbers with the lock: 25 and 5, stock 5 and 20 pieces | 3 |
| The difference between the two procedures is a single clause | 1 |
| The retry reports attempts per session and both parts with their two decrements | 3 |

**Most common mistake**

Putting the `FOR UPDATE` with autocommit on, outside a transaction; it gives itself away because the lock is released at the end of the statement and the result goes back to being the one from the version with no lock.

---

## Week 17 · Users, backup and closing · Final exam

### 17.1 · Recognise

**Solution**

```sql
-- Read code and description ......... passes
-- Read code and on_hand ............. bounces, ERROR 1143 (not 1142)
-- Update on_hand .................... passes
-- Update description ................ bounces, ERROR 1143
-- 1143 is the column error. 1142 is the whole-table one. The account does have
-- permission on the part table, only on other columns.

-- What will NOT be in workshop.sql with the default command:
--   the procedure sp_loans_of   (it needs --routines)
--   the event ev_purge_log      (it needs --events)
-- What does go in: the three tables, their data, the view and the trigger.
-- On standard error it prints three warnings: the one about GTIDs, the one
-- saying a complete backup needs --all-databases --triggers --routines
-- --events, and the one saying a consistent backup needs --single-transaction
-- or --lock-all-tables or --source-data.
-- The last line of a complete file is «-- Dump completed on ...».
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four verdicts on the `SHOW GRANTS` | 3 |
| The 1143 of the column is told apart from the 1142 of the table | 2 |
| The procedure and the event are named as what the backup leaves out | 3 |
| The trigger is said to go in, and the last line of a complete file is given | 2 |

**Most common mistake**

Assuming the trigger is left out of the default backup too; it gives itself away with a `grep -c TRIGGER` over the file, which returns 1.

### 17.2 · Apply

**Solution**

```sql
-- 1. The GRANT with no account behind it
GRANT SELECT, INSERT ON plant.* TO 'eng_clerk'@'localhost';
CREATE USER 'eng_analyst'@'localhost' IDENTIFIED BY 'Plant2026!';
SHOW GRANTS FOR 'eng_analyst'@'localhost';
GRANT SELECT ON plant.* TO 'eng_analyst'@'localhost';
SHOW GRANTS FOR 'eng_analyst'@'localhost';

-- 3. Column privileges
CREATE USER 'eng_tutor'@'localhost' IDENTIFIED BY 'Plant2026!';
GRANT SELECT (code, description) ON plant.part TO 'eng_tutor'@'localhost';
GRANT UPDATE (on_hand)           ON plant.part TO 'eng_tutor'@'localhost';
SHOW GRANTS FOR 'eng_tutor'@'localhost';

-- 4. The role
CREATE ROLE 'role_plant_read';
GRANT SELECT ON plant.* TO 'role_plant_read';
CREATE USER 'eng_reports'@'localhost' IDENTIFIED BY 'Plant2026!';
GRANT 'role_plant_read' TO 'eng_reports'@'localhost';
SELECT @@activate_all_roles_on_login AS active_on_login;

-- 2. From the second window, connected as eng_analyst
SELECT COUNT(*) AS can_read FROM plant.machine;
DELETE FROM plant.part WHERE part_id = 7;
SELECT user, host FROM mysql.user LIMIT 1;

-- 3. From the third window, connected as eng_tutor
SELECT code, description FROM plant.part LIMIT 2;
SELECT code, on_hand    FROM plant.part LIMIT 2;
UPDATE plant.part SET on_hand = 12 WHERE code = 'RF-001';
UPDATE plant.part SET description = 'Air filter' WHERE code = 'RF-001';

-- 4. From the fourth window, connected as eng_reports
SELECT CURRENT_ROLE() AS active_role;
SELECT COUNT(*) FROM plant.machine;
SET ROLE 'role_plant_read';
SELECT CURRENT_ROLE() AS active_role;
SELECT COUNT(*) AS now_it_works FROM plant.machine;
```

```bash
# The backup, three files
mysqldump -u root -p --set-gtid-purged=OFF workshop > workshop_default.sql
mysqldump -u root -p --routines --events --set-gtid-purged=OFF workshop > workshop_full.sql
mysqldump -u root -p --no-data --set-gtid-purged=OFF workshop > workshop_schema.sql
grep -c PROCEDURE workshop_default.sql workshop_full.sql
grep -c EVENT     workshop_default.sql workshop_full.sql
wc -c workshop_default.sql workshop_full.sql workshop_schema.sql
```

**Output**

```
ERROR 1410 (42000) at line 2: You are not allowed to create a user with GRANT
Grants for eng_analyst@localhost
GRANT USAGE ON *.* TO `eng_analyst`@`localhost`
Grants for eng_analyst@localhost
GRANT USAGE ON *.* TO `eng_analyst`@`localhost`
GRANT SELECT ON `plant`.* TO `eng_analyst`@`localhost`
Grants for eng_tutor@localhost
GRANT USAGE ON *.* TO `eng_tutor`@`localhost`
GRANT SELECT (`code`, `description`), UPDATE (`on_hand`) ON `plant`.`part` TO `eng_tutor`@`localhost`
active_on_login
0

--- connected as eng_analyst ---
can_read
8
ERROR 1142 (42000) at line 2: DELETE command denied to user 'eng_analyst'@'localhost' for table 'part'
ERROR 1142 (42000) at line 3: SELECT command denied to user 'eng_analyst'@'localhost' for table 'user'

--- connected as eng_tutor ---
code	description
RF-001	Air filter 50% efficiency
RF-002	Oil filter 50 micron
ERROR 1143 (42000) at line 2: SELECT command denied to user 'eng_tutor'@'localhost' for column 'on_hand' in table 'part'
ERROR 1143 (42000) at line 4: UPDATE command denied to user 'eng_tutor'@'localhost' for column 'description' in table 'part'

--- connected as eng_reports ---
active_role
NONE
ERROR 1142 (42000) at line 2: SELECT command denied to user 'eng_reports'@'localhost' for table 'machine'
active_role
`role_plant_read`@`%`
now_it_works
8
```

```
workshop_default.sql:0
workshop_full.sql:2
workshop_default.sql:0
workshop_full.sql:2
 6244 workshop_default.sql
 8901 workshop_full.sql
 5348 workshop_schema.sql
20493 total
```

The role was granted and it was not activated. `@@activate_all_roles_on_login` is 0, so the account comes in with `CURRENT_ROLE()` at `NONE` and receives the same 1142 as an account with no permissions. It is fixed in the session with `SET ROLE 'role_plant_read'`, and permanently with `SET DEFAULT ROLE` or by switching the variable on.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The 1410 and the order the server demands | 2 |
| The two `SHOW GRANTS` and the two 1142 seen from the restricted account | 3 |
| The four column verdicts checked, with the 1143 | 2 |
| The role left unactivated, with `CURRENT_ROLE()` at `NONE` and its fix | 2 |
| The three sizes and the counts of `PROCEDURE` and `EVENT` | 1 |

**Most common mistake**

Testing the permissions from the root session and calling them good; it gives itself away because granting produces no output, and the only thing you see from the other side is the error the restricted account receives.

### 17.3 · Integrate

**Solution**

```bash
# 1. Restore and verify
mysql -u root -p -e "CREATE DATABASE workshop_restored;"
mysql -u root -p workshop_restored < workshop_full.sql
echo "exit=$?"
```

```sql
SELECT (SELECT COUNT(*) FROM workshop_restored.tool)     AS t,
       (SELECT COUNT(*) FROM workshop_restored.loan)     AS l,
       (SELECT COUNT(*) FROM workshop_restored.loan_log) AS g;
SELECT ROUTINE_NAME FROM information_schema.ROUTINES WHERE ROUTINE_SCHEMA='workshop_restored';
SELECT EVENT_NAME   FROM information_schema.EVENTS   WHERE EVENT_SCHEMA='workshop_restored';
SELECT TRIGGER_NAME FROM information_schema.TRIGGERS WHERE TRIGGER_SCHEMA='workshop_restored';

-- 2. Restore over a live database
USE workshop_restored;
INSERT INTO tool VALUES (9,'HT-09','Thermal camera');
DELETE FROM loan WHERE loan_id = 2;
CREATE TABLE local_log (id INT PRIMARY KEY);
SELECT COUNT(*) AS tools, (SELECT COUNT(*) FROM loan) AS loans FROM tool;
```

```bash
mysql -u root -p workshop_restored < workshop_full.sql
# 3. The file that lies
mysqldump -u root -p --set-gtid-purged=OFF workshop tool table_that_does_not_exist > broken.sql
echo "exit=$?"; wc -c broken.sql; tail -1 broken.sql
```

**Output**

```
exit=0
lines printed by the client: 0

t	l	g
3	2	2
ROUTINE_NAME
sp_loans_of
EVENT_NAME
ev_purge_log
TRIGGER_NAME
trg_loan_after_insert_log

--- before restoring on top ---
tools	loans
4	1
--- after ---
exit of the restore=0
tools	loans
3	2
Tables_in_workshop_restored
loan
loan_log
local_log
tool
v_loan_open

--- the broken dump ---
mysqldump: Couldn't find table: "table_that_does_not_exist"
exit=6
795 broken.sql
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
```

The successful restore printed not one line and exited with code 0. The only proof it worked is the count on the other side.

Restoring does not take you back to the day of the backup, it overwrites your today. The new tool went away, the deleted loan came back, and `local_log` survived intact because the file does not name it on any line: a backup only puts back what it knows and does not delete what it ignores.

The broken file came out with code 6 and left 795 bytes of believable header. The signal is the last line: it does not say `-- Dump completed on ...`, it says a `SET` from the header, so the file was cut off before a single datum was written.

The three closings.

`sql_mode`. The 1264 of a value out of range, the 1292 of a badly written date, the 1265 of a value outside the ENUM and the 1406 of an overlong string are errors because `STRICT_TRANS_TABLES` is switched on. With the mode off, the four INSERT statements pass in silence, truncating the datum, and that is where «it works on my machine» is born.

`EXPLAIN`. In week 15 the inherited advice recommended `REGEXP` over `LIKE` for searching text. The plan knocked it down: the anchored `LIKE` gave `type=range` with 14 320 rows and the anchored `REGEXP` gave `type=ALL` with 59 478 and `possible_keys=NULL`. The advice was exactly backwards, and no authority would have shown that.

The contradiction. Week 6 calls the index an added detail and week 15 measured it: eight indexes too many weighed 44 171 264 bytes against 9 977 856 of data, more than four times, and multiplied the load time by 4.79. A detail does not change the size of a table fourfold. It is settled by the measurement, not by the slide.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The restore is checked by counting on the other side, with the three objects | 3 |
| The restore over a live base reports the three things and explains the one that survives | 2 |
| The broken file, with code 6, size and last line | 2 |
| The three closing paragraphs, each with a figure or an error from the term | 3 |

**Most common mistake**

Taking the restore as good because the client printed no errors; it gives itself away because a restore that failed halfway also comes out quiet, and the only proof is the count afterwards.
