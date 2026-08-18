# Soluciones · Introducción a las Bases de Datos · COM112

Las cincuenta y una soluciones corrieron contra MySQL 9.7.2 con el `sql_mode` de fábrica del curso (`ONLY_FULL_GROUP_BY`, `STRICT_TRANS_TABLES`, `NO_ZERO_IN_DATE`, `NO_ZERO_DATE`, `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ENGINE_SUBSTITUTION`), motor InnoDB, colación `utf8mb4_0900_ai_ci`. Cada salida de este archivo es lo que devolvió el servidor, copiada sin editar. Los tiempos y los tamaños en disco se vuelven a medir en el aula y van a salir parecidos, no idénticos.

---

## Semana 01 · Por qué existe una base de datos

### 01.1 · Reconocer

**Solución**

```sql
-- La adjudicacion de las cinco fallas
-- 1. Marca de tiempo repetida ......... Proteger
--    Nadie se niega a aceptar el renglon que rompe la regla.
-- 2. 742 grados en un sensor de 0 a 120 ... Proteger
--    Misma presion, misma causa: no hay quien revise el dominio.
-- 3. Valor ausente y unidad en minuscula .. Organizar
--    No hay tipo declarado, asi que el archivo acepta cualquier cosa.
-- 4. La unidad repetida en los cinco renglones ... Relacionar
--    La unidad pertenece al sensor y se copia en cada lectura.
-- 5. Dos personas guardan y la ultima se lleva todo ... Administrar
--    Y buscar entre 8.6 millones de renglones ......... Manejar volumen

-- La prediccion de la traza
START TRANSACTION;
INSERT INTO medicion VALUES (21, 6, '2026-03-02 08:00:00', 9.40);
INSERT INTO medicion VALUES (22, 6, '2026-03-02 09:00:00', 9.65);
SELECT COUNT(*) AS mediciones_dentro FROM medicion;   -- 22
ROLLBACK;
SELECT COUNT(*) AS mediciones_despues FROM medicion;  -- 20
```

**Salida**

```
mediciones_dentro
22
mediciones_despues
20
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco fallas quedan adjudicadas a una presión cada una | 4 |
| Las dos que caen en Proteger se distinguen de la de Organizar | 2 |
| Los dos conteos predichos son 22 y 20 | 3 |
| Se dice que la transacción sí vio sus propias filas antes del ROLLBACK | 1 |

**Error que más se ve**

Predecir 20 en el primer conteo, por creer que la fila no existe hasta el COMMIT; se delata porque entonces el ROLLBACK no tendría nada que deshacer.

### 01.2 · Aplicar

**Solución**

```sql
USE planta;

SELECT VERSION() AS version,
       @@default_storage_engine AS motor,
       @@character_set_server   AS juego_caracteres;

SELECT @@sql_mode AS modo;

START TRANSACTION;
INSERT INTO medicion VALUES (21, 3, '2026-03-02 10:00:00', 39.20);
INSERT INTO medicion VALUES (22, 3, '2026-03-02 11:00:00', 40.05);
INSERT INTO medicion VALUES (23, 3, '2026-03-02 12:00:00', 43.70);
SELECT COUNT(*) AS mediciones_dentro FROM medicion;
ROLLBACK;
SELECT COUNT(*) AS mediciones_despues FROM medicion;
```

**Salida**

```
version	motor	juego_caracteres
9.7.2	InnoDB	utf8mb4

modo
ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION

mediciones_dentro
23

mediciones_despues
20
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres lecturas del servidor salen en un solo renglón con los alias pedidos | 3 |
| El `sql_mode` completo aparece en su propia consulta | 2 |
| La transacción deja 23 adentro y 20 después | 4 |
| La salida está pegada literal, sin recortar el `sql_mode` | 1 |

**Error que más se ve**

Pegar el `sql_mode` recortado a los primeros dos valores; se delata porque falta `STRICT_TRANS_TABLES`, que es el que produce cuatro de los errores del semestre.

### 01.3 · Integrar

**Solución**

```sql
USE planta;

CREATE TABLE medicion_plana (
  medicion_id INT          PRIMARY KEY,
  sensor_id   INT          NOT NULL,
  tomada_en   DATETIME     NOT NULL,
  valor       DECIMAL(7,2) NULL,
  unidad      CHAR(4)      NOT NULL
);
SHOW CREATE TABLE medicion_plana;

-- La falla que sigue viva es la 5: dos personas escribiendo a la vez.
-- Ninguna columna de esta declaracion la toca.
START TRANSACTION;
INSERT INTO medicion_plana VALUES (1, 1, '2026-03-02 07:00:00', 742.00, 'C');
SELECT COUNT(*) AS dentro FROM medicion_plana;
ROLLBACK;
SELECT COUNT(*) AS despues FROM medicion_plana;
```

**Salida**

```
Table	Create Table
medicion_plana	CREATE TABLE `medicion_plana` (
  `medicion_id` int NOT NULL,
  `sensor_id` int NOT NULL,
  `tomada_en` datetime NOT NULL,
  `valor` decimal(7,2) DEFAULT NULL,
  `unidad` char(4) NOT NULL,
  PRIMARY KEY (`medicion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

dentro
1

despues
0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco columnas con su tipo, y solo `valor` acepta vacío | 3 |
| `SHOW CREATE TABLE` pegado, incluido el motor y la colación que el servidor escribió solo | 2 |
| Se identifica la falla 5, la de las dos personas, como la que queda viva | 3 |
| Los dos conteos alrededor del ROLLBACK, y la explicación de por qué eso no la resuelve | 2 |

**Error que más se ve**

Declarar `valor` como `NOT NULL` para «que no falte ninguno»; se delata porque entonces un sensor desconectado tumba la carga entera en lugar de registrar la ausencia.

---

## Semana 02 · Tipos, elementos y clasificaciones

### 02.1 · Reconocer

**Solución**

```sql
-- Prediccion, renglon por renglon
-- TABLE               3   herramienta, prestamo, prestamo_bitacora
-- VIEW                1   v_prestamo_vigente
-- TRIGGER             1   trg_prestamo_after_insert_bitacora
-- EVENT               1   ev_purga_bitacora
-- PROCEDURE/FUNCTION  0   el guion no declara ninguna
-- CONSTRAINT          5   3 PRIMARY KEY + 1 UNIQUE + 1 FOREIGN KEY
-- INDEX               5   3 PRIMARY + 1 de la UNIQUE + 1 que escribio la FK
```

**Salida**

```
objeto	n
TABLE	3
VIEW	1
TRIGGER	1
EVENT	1
PROCEDURE/FUNCTION	0
CONSTRAINT	5
INDEX	5

TABLE_NAME	CONSTRAINT_NAME	CONSTRAINT_TYPE
herramienta	clave	UNIQUE
herramienta	PRIMARY	PRIMARY KEY
prestamo	prestamo_ibfk_1	FOREIGN KEY
prestamo	PRIMARY	PRIMARY KEY
prestamo_bitacora	PRIMARY	PRIMARY KEY
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco primeros renglones (3, 1, 1, 1, 0) | 3 |
| El conteo de restricciones es 5 y se desglosa por su origen | 3 |
| El conteo de índices es 5 | 2 |
| Se nombra el índice de la llave foránea como el que nadie declaró | 2 |

**Error que más se ve**

Contar 3 índices, uno por tabla; se delata porque olvida que un `UNIQUE` y una `FOREIGN KEY` traen cada uno su índice de regalo.

### 02.2 · Aplicar

**Solución**

```sql
CREATE USER 'ing_lector'@'localhost' IDENTIFIED BY 'Planta2026!';
SHOW GRANTS FOR 'ing_lector'@'localhost';

GRANT SELECT ON planta.* TO 'ing_lector'@'localhost';
SHOW GRANTS FOR 'ing_lector'@'localhost';
```

**Salida**

```
Grants for ing_lector@localhost
GRANT USAGE ON *.* TO `ing_lector`@`localhost`

Grants for ing_lector@localhost
GRANT USAGE ON *.* TO `ing_lector`@`localhost`
GRANT SELECT ON `planta`.* TO `ing_lector`@`localhost`
```

La cuenta recién creada ya traía `USAGE`, que no es un permiso sino el derecho a conectarse sin poder tocar nada. El servidor lo escribió solo, al crear la cuenta.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La cuenta se crea con contraseña y con host explícito | 3 |
| Los dos `SHOW GRANTS` aparecen, antes y después del `GRANT` | 4 |
| Se explica que `USAGE` es el derecho a conectarse y nada más | 3 |

**Error que más se ve**

Escribir `CREATE USER 'ing_lector'` sin host y suponer que eso crea una cuenta universal; se delata porque el servidor la registra como `'ing_lector'@'%'`, que es otra cuenta distinta de la de `localhost`.

### 02.3 · Integrar

**Solución**

```sql
USE planta;
-- Regla 1: el dominio del valor
INSERT INTO lectura VALUES (2, 1, '2026-03-02 07:00:00', 742.00);
-- Regla 2: el par sensor + marca de tiempo
INSERT INTO lectura VALUES (3, 1, '2026-03-02 06:00:00',  72.10);
-- Regla 3: el sensor tiene que existir
INSERT INTO lectura VALUES (4, 99,'2026-03-02 07:00:00',  72.10);

SELECT COUNT(*) AS filas_en_lectura FROM lectura;
```

**Salida**

```
ERROR 3819 (HY000) at line 14: Check constraint 'ck_lectura_valor' is violated.

ERROR 1062 (23000) at line 16: Duplicate entry '1-2026-03-02 06:00:00' for key 'lectura.uq_lectura_sensor_tiempo'

ERROR 1452 (23000) at line 18: Cannot add or update a child row: a foreign key constraint fails (`planta`.`lectura`, CONSTRAINT `fk_lectura_sensor` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))

filas_en_lectura
1
```

Los tres rechazos los levantó el manejador, sin un solo programa de aplicación conectado. El primero se apoya en el `CHECK`, el segundo en el índice único del par y el tercero en la existencia de la fila padre.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres INSERT rebotan, cada uno por una regla distinta | 4 |
| Los tres errores están pegados con su número y su SQLSTATE | 3 |
| El conteo final demuestra que la tabla no cambió | 1 |
| Se nombra al manejador como la pieza que levantó los tres | 2 |

**Error que más se ve**

Escribir el segundo INSERT con un `lectura_id` repetido en lugar de un par repetido; se delata porque el error nombra `PRIMARY` y no `uq_lectura_sensor_tiempo`, así que probó otra regla.

---

## Semana 03 · El manejador y sus archivos

### 03.1 · Reconocer

**Solución**

```sql
-- A) Nivel externo.    SELECT * FROM v_prestamo_vigente;
-- B) Nivel interno.    SELECT @@innodb_page_size; SELECT @@innodb_buffer_pool_size;
-- C) Nivel conceptual. SELECT TABLE_NAME, TABLE_TYPE, ENGINE
--                        FROM information_schema.TABLES WHERE TABLE_SCHEMA='taller';
-- D) El suelo.         SELECT SPACE, NAME, FILE_SIZE
--                        FROM information_schema.INNODB_TABLESPACES
--                       WHERE NAME LIKE 'taller/%';

-- Si alguien agrega una columna a herramienta, cambia C. A no, porque la vista
-- nombra sus columnas. B tampoco, porque la pagina sigue midiendo 16 KB.
-- D no menciona la vista porque una vista no tiene archivo: no guarda filas.
-- ENGINE viene vacio en el segundo renglon de C por la misma razon.
```

**Salida**

```
TABLE_NAME	TABLE_TYPE	ENGINE
herramienta	BASE TABLE	InnoDB
prestamo	BASE TABLE	InnoDB
prestamo_bitacora	BASE TABLE	InnoDB
v_prestamo_vigente	VIEW	NULL
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro salidas quedan asignadas a su nivel | 4 |
| Cada asignación trae la sentencia que la produjo | 2 |
| Se identifica C como la única que cambia al agregar una columna | 2 |
| Se explica el `ENGINE` vacío y la ausencia de la vista en D con la misma razón | 2 |

**Error que más se ve**

Poner la vista en el nivel conceptual porque «aparece en el catálogo»; se delata porque el catálogo también la lista, y lo que define el nivel externo es quién la consulta, no dónde está registrada.

### 03.2 · Aplicar

**Solución**

```sql
USE taller;

-- Nivel externo
SELECT * FROM v_prestamo_vigente;

-- Nivel conceptual
SELECT TABLE_NAME, TABLE_TYPE, ENGINE
  FROM information_schema.TABLES
 WHERE TABLE_SCHEMA = 'taller'
 ORDER BY TABLE_TYPE, TABLE_NAME;

-- Nivel interno
SELECT @@datadir AS donde_viven_los_bytes;
SELECT @@innodb_page_size AS tamano_pagina,
       @@innodb_buffer_pool_size AS gestor_de_buffers;

-- El suelo
SELECT SPACE, NAME, FILE_SIZE
  FROM information_schema.INNODB_TABLESPACES
 WHERE NAME LIKE 'taller/%'
 ORDER BY NAME;
```

**Salida**

```
prestamo_id	herramienta_id	salida
1	1	2026-03-02 07:15:00
2	3	2026-03-02 08:40:00

TABLE_NAME	TABLE_TYPE	ENGINE
herramienta	BASE TABLE	InnoDB
prestamo	BASE TABLE	InnoDB
prestamo_bitacora	BASE TABLE	InnoDB
v_prestamo_vigente	VIEW	NULL

donde_viven_los_bytes
...\scratchpad\mydb\data\

tamano_pagina	gestor_de_buffers
16384	134217728

SPACE	NAME	FILE_SIZE
280	taller/herramienta	131072
281	taller/prestamo	131072
282	taller/prestamo_bitacora	114688
```

El listado tiene tres entradas y el catálogo tenía cuatro porque `v_prestamo_vigente` no tiene archivo. Una vista guarda lógica, no filas.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Una consulta por nivel, en orden, cada una con su salida | 5 |
| El nivel conceptual trae tipo de objeto y motor | 2 |
| El listado de archivos aparece y trae los tres tamaños | 1 |
| Se explica la diferencia entre tres y cuatro | 2 |

**Error que más se ve**

Cambiar de base a media entrega, de modo que el listado de archivos ya no corresponde al catálogo; se delata porque los nombres de la columna `NAME` traen otro prefijo de esquema.

### 03.3 · Integrar

**Solución**

```sql
USE taller;
SELECT SUM(FILE_SIZE) AS bytes_en_disco
  FROM information_schema.INNODB_TABLESPACES
 WHERE NAME LIKE 'taller/%';
-- y desde la terminal:  wc -c taller.sql

SELECT @@explain_format AS formato_por_omision;
EXPLAIN SELECT prestamo_id, salida FROM prestamo WHERE herramienta_id = 3;
EXPLAIN FORMAT=TRADITIONAL
SELECT prestamo_id, salida FROM prestamo WHERE herramienta_id = 3;

SELEC prestamo_id FROM prestamo;
```

**Salida**

```
bytes_en_disco
376832

1200 taller.sql
```

376 832 bytes en disco contra 1 200 bytes de texto SQL. El cociente es 314. Esa diferencia es estructura, no desperdicio.

```
formato_por_omision
TREE

EXPLAIN
-> Index lookup on prestamo using herramienta_id (herramienta_id = 3)  (cost=0.35 rows=1)

id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	prestamo	NULL	ref	herramienta_id	herramienta_id	4	const	1	100.00	NULL

ERROR 1064 (42000) at line 28: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELEC prestamo_id FROM prestamo' at line 1
```

El error 1064 lo levantó el parser. El optimizador, el ejecutor, el gestor de archivos y el gestor de buffers no llegaron a enterarse, porque la cadena nunca se convirtió en una sentencia.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos números de la brecha y su cociente | 3 |
| Los dos `EXPLAIN` pegados, con `@@explain_format` para explicar la diferencia | 3 |
| El error 1064 provocado y pegado literal | 2 |
| Se atribuye el 1064 al parser y se dice por qué los otros cuatro no participaron | 2 |

**Error que más se ve**

Comparar el tamaño en disco contra el número de renglones de datos en lugar de contra el texto del guion; se delata porque el cociente sale en bytes por fila, que no es lo que la brecha mide.

---

## Semana 04 · Modelo entidad-relación

### 04.1 · Reconocer

**Solución**

```sql
-- 1. Equipo pertenece a Linea .............. 1:N
--    Llave foranea del lado muchos, en equipo.
-- 2. Orden consume Refaccion ............... N:M
--    Tabla nueva, llave primaria del par (orden_id, refaccion_id).
-- 3. Equipo tiene Certificado .............. 0:1
--    Llave foranea en certificado, mas UNIQUE. Acepta equipos sin certificado.
-- 4. Equipo se monta en Equipo ............. recursiva 1:N
--    Llave foranea a la propia tabla, y la columna acepta vacio para la raiz.
-- 5. Linea tiene equipo cabecera ........... relacion doble
--    Dos lineas entre las mismas dos entidades, en sentidos contrarios:
--    equipo.linea_id apunta a linea, y linea.equipo_cabecera_id apunta a equipo.
--    Se ve simetrica y no lo es. La 1 es una sola linea del dibujo; la 5 son dos,
--    y las dos juntas forman un ciclo que ningun CREATE TABLE resuelve de un golpe.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco cardinalidades correctas | 3 |
| Los cinco verbos, cada uno legible en voz alta como oración | 2 |
| Las cinco formas físicas | 3 |
| Se explica que la 5 son dos relaciones y que forman un ciclo | 2 |

**Error que más se ve**

Marcar la 3 como 1:1 en lugar de 0:1; se delata porque la frase dice «hay equipos sin certificado», y eso decide si la llave foránea acepta vacío.

### 04.2 · Aplicar

**Solución**

```sql
CREATE DATABASE modelo CHARACTER SET utf8mb4;
USE modelo;

CREATE TABLE equipo (
  equipo_id       INT PRIMARY KEY,
  nombre          VARCHAR(60) NOT NULL,
  equipo_padre_id INT NULL,
  FOREIGN KEY (equipo_padre_id) REFERENCES equipo(equipo_id)
);
INSERT INTO equipo VALUES (1,'Cabina de pintura', NULL);
INSERT INTO equipo VALUES (2,'Bomba de recirculacion', 1);
INSERT INTO equipo VALUES (3,'Impulsor de la bomba', 2);
SELECT equipo_id, nombre, equipo_padre_id FROM equipo;

CREATE TABLE orden (
  orden_id  INT PRIMARY KEY,
  folio     CHAR(8) NOT NULL,
  equipo_id INT NOT NULL,
  FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);
CREATE TABLE refaccion (
  refaccion_id INT PRIMARY KEY,
  descripcion  VARCHAR(60) NOT NULL
);
CREATE TABLE consumo (
  orden_id     INT,
  refaccion_id INT,
  cantidad     INT NOT NULL,
  PRIMARY KEY (orden_id, refaccion_id),
  FOREIGN KEY (orden_id)     REFERENCES orden(orden_id),
  FOREIGN KEY (refaccion_id) REFERENCES refaccion(refaccion_id)
);
INSERT INTO orden     VALUES (1,'OT-26001',1);
INSERT INTO refaccion VALUES (1,'Balero rigido de bolas 50 mm');
INSERT INTO consumo   VALUES (1,1,4);
SHOW CREATE TABLE consumo;

INSERT INTO consumo VALUES (1,1,2);
```

**Salida**

```
equipo_id	nombre	equipo_padre_id
1	Cabina de pintura	NULL
2	Bomba de recirculacion	1
3	Impulsor de la bomba	2

Table	Create Table
consumo	CREATE TABLE `consumo` (
  `orden_id` int NOT NULL,
  `refaccion_id` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`orden_id`,`refaccion_id`),
  KEY `refaccion_id` (`refaccion_id`),
  CONSTRAINT `consumo_ibfk_1` FOREIGN KEY (`orden_id`) REFERENCES `orden` (`orden_id`),
  CONSTRAINT `consumo_ibfk_2` FOREIGN KEY (`refaccion_id`) REFERENCES `refaccion` (`refaccion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

ERROR 1062 (23000) at line 42: Duplicate entry '1-1' for key 'consumo.PRIMARY'
```

Lo que el servidor escribió solo: el `KEY refaccion_id`, que nadie pidió y que existe porque la segunda llave foránea no era la columna izquierda de la llave primaria; y los dos nombres `consumo_ibfk_1` y `consumo_ibfk_2`.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La recursiva se declara con la llave foránea a su propia tabla | 2 |
| La columna de padre acepta vacío y la raíz lo demuestra | 2 |
| La tabla del N:M tiene la llave primaria del par | 2 |
| Se señalan las tres cosas que el servidor escribió solo | 2 |
| El par repetido devuelve el 1062 y está pegado | 2 |

**Error que más se ve**

Declarar `equipo_padre_id INT NOT NULL` porque «todo equipo está montado en algo»; se delata porque el primer INSERT ya no tiene por dónde empezar y falla por la llave foránea.

### 04.3 · Integrar

**Solución**

```sql
CREATE DATABASE modelo2 CHARACTER SET utf8mb4;
USE modelo2;

-- Lo que el dibujo pide de forma literal
CREATE TABLE linea (
  linea_id           INT PRIMARY KEY,
  nombre             VARCHAR(40) NOT NULL,
  equipo_cabecera_id INT NOT NULL,
  FOREIGN KEY (equipo_cabecera_id) REFERENCES equipo(equipo_id)
);

-- Lo que si corre, en tres sentencias
CREATE TABLE linea (                       -- concesion 1: sin la llave foranea
  linea_id           INT PRIMARY KEY,
  nombre             VARCHAR(40) NOT NULL,
  equipo_cabecera_id INT NULL               -- concesion 2: acepta vacio
);
CREATE TABLE equipo (
  equipo_id       INT PRIMARY KEY,
  nombre          VARCHAR(60) NOT NULL,
  linea_id        INT NOT NULL,
  equipo_padre_id INT NULL,
  FOREIGN KEY (linea_id)        REFERENCES linea(linea_id),
  FOREIGN KEY (equipo_padre_id) REFERENCES equipo(equipo_id)
);
ALTER TABLE linea                          -- concesion 3: la FK llega despues
  ADD CONSTRAINT fk_linea_cabecera
  FOREIGN KEY (equipo_cabecera_id) REFERENCES equipo(equipo_id);

INSERT INTO linea  VALUES (1,'Pintura', NULL);
INSERT INTO equipo VALUES (5,'Cabina de pintura', 1, NULL);
UPDATE linea SET equipo_cabecera_id = 5 WHERE linea_id = 1;
SELECT linea_id, nombre, equipo_cabecera_id FROM linea;

INSERT INTO linea VALUES (2,'Empaque', NULL);
SELECT COUNT(*) AS equipos_en_la_linea_2 FROM equipo WHERE linea_id = 2;
```

**Salida**

```
ERROR 1824 (HY000) at line 6: Failed to open the referenced table 'equipo'

linea_id	nombre	equipo_cabecera_id
1	Pintura	5

equipos_en_la_linea_2
0
```

La promesa que queda sin quien la exija es la cardinalidad mínima. El diagrama dice que una línea tiene equipos, y MySQL no tiene ninguna construcción para obligarlo. La línea Empaque se queda con cero equipos para siempre y nadie protesta.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El primer intento se corre y devuelve el 1824 | 2 |
| La versión que sí corre son tres sentencias, con el ALTER al final | 3 |
| Las tres concesiones están escritas en los comentarios | 2 |
| La línea sin equipos se da de alta y se cuenta | 1 |
| Se nombra la cardinalidad mínima como lo que no se puede exigir | 2 |

**Error que más se ve**

Romper el ciclo quitando la llave foránea en lugar de aflojando el `NOT NULL`; se delata porque el modelo pierde la regla, mientras que la columna que acepta vacío la conserva y solo la aplaza.

---

## Semana 05 · Normalización

### 05.1 · Reconocer

**Solución**

```sql
-- Dependencias funcionales de lectura_ancha
-- (sensor_id, tomada_en) -> valor            llave completa, bien puesta
--  sensor_id             -> sensor_unidad    media llave: rompe la 2FN
--  sensor_id             -> equipo_id        media llave: rompe la 2FN
--  equipo_id             -> equipo_nombre    transitiva: rompe la 3FN
--  equipo_id             -> equipo_area      transitiva: rompe la 3FN

-- Prediccion de la primera corrida: las tres lecturas entran, sin error
-- y sin advertencia, y el sensor 103 queda con dos unidades distintas.

-- Prediccion de la segunda: la tabla sin llave primaria se crea sin problema;
-- con sql_require_primary_key encendida, el mismo CREATE TABLE devuelve 3750.
-- La unicidad no es parte de la primera forma normal: es otra regla.
```

**Salida**

```
sensor_id	tomada_en	sensor_unidad
103	2026-03-02 06:00:00	mm/s
103	2026-03-02 07:00:00	mm/s
103	2026-03-02 08:00:00	mm/seg

Table	Create Table
sin_llave	CREATE TABLE `sin_llave` (
  `sensor_id` int DEFAULT NULL,
  `valor` decimal(7,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

ERROR 3750 (HY000) at line 28: Unable to create or change a table without a primary key, when the system variable 'sql_require_primary_key' is set. Add a primary key to the table or unset this variable to avoid this message. Note that tables without a primary key can cause performance problems in row-based replication, so please consult your DBA before changing this setting.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco dependencias escritas como `A → B` | 4 |
| Se separan las de media llave de las transitivas y se nombra la forma que rompe cada grupo | 3 |
| Se predice que las tres lecturas entran sin error | 1 |
| El 3750 se predice y se usa para separar la 1FN de la unicidad | 2 |

**Error que más se ve**

Escribir `sensor_id → valor`; se delata porque el mismo sensor tiene varias lecturas, así que el valor depende del par completo y no de la mitad.

### 05.2 · Aplicar

**Solución**

```sql
-- Ataque 1: la lista en la celda
SELECT COUNT(*) AS ordenes_con_rf003 FROM orden_ancha WHERE refacciones = 'RF-003';
SELECT orden_id, refacciones FROM orden_ancha
 WHERE FIND_IN_SET('RF-003', REPLACE(refacciones,', ',',')) > 0;

-- Ataque 2: dos grafias del mismo equipo
INSERT INTO lectura_ancha VALUES
 (104,'2026-03-02 06:00:00','C',4,'Compresor de tornillo','Acabados',95.10),
 (104,'2026-03-02 07:00:00','C',4,'Compresor de Tornillo','Acabados',98.60);
SELECT equipo_id, equipo_nombre FROM lectura_ancha WHERE sensor_id = 104;

-- Ataque 3: el UPDATE que parte el area
UPDATE lectura_ancha SET equipo_area = 'Pintura'
 WHERE sensor_id = 104 AND tomada_en = '2026-03-02 06:00:00';
SELECT equipo_id, equipo_nombre, equipo_area FROM lectura_ancha WHERE sensor_id = 104;
```

**Salida**

```
ordenes_con_rf003
0

orden_id	refacciones
1	RF-001, RF-003
2	RF-006, RF-003

equipo_id	equipo_nombre
4	Compresor de tornillo
4	Compresor de Tornillo

equipo_id	equipo_nombre	equipo_area
4	Compresor de tornillo	Pintura
4	Compresor de Tornillo	Acabados
```

El dato estaba guardado y el `WHERE` con igual contestó cero. `FIND_IN_SET` lo encuentra y a cambio renuncia al índice: ninguna función encima de una columna puede apoyarse en uno, así que se lee la tabla entera.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El ataque de la lista devuelve 0 con igual y sí encuentra con `FIND_IN_SET` | 3 |
| Se dice que el parche renuncia al índice | 2 |
| Las dos grafías entran y se muestran juntas | 2 |
| El UPDATE deja el mismo equipo en dos áreas, sin error ni advertencia | 3 |

**Error que más se ve**

Usar `LIKE '%RF-003%'` en lugar de `FIND_IN_SET` y darlo por resuelto; se delata en cuanto exista una clave `RF-0031`, que el comodín atrapa y el conjunto no.

### 05.3 · Integrar

**Solución**

```sql
CREATE TABLE equipo (
  equipo_id INT PRIMARY KEY,
  nombre    VARCHAR(60) NOT NULL,
  area      VARCHAR(30) NOT NULL
);
CREATE TABLE sensor (
  sensor_id INT PRIMARY KEY,
  unidad    VARCHAR(10) NOT NULL,
  equipo_id INT NOT NULL,
  FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);
CREATE TABLE lectura (
  sensor_id INT,
  tomada_en DATETIME,
  valor     DECIMAL(7,2) NULL,
  PRIMARY KEY (sensor_id, tomada_en),
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);
-- los mismos datos, sin perder un renglon
INSERT INTO equipo VALUES (2,'Robot de soldadura','Manufactura'),
                          (4,'Compresor de tornillo','Acabados');
INSERT INTO sensor VALUES (103,'mm/s',2),(104,'C',4);
INSERT INTO lectura VALUES
 (103,'2026-03-02 06:00:00',12.30),(103,'2026-03-02 07:00:00',41.80),
 (103,'2026-03-02 08:00:00',44.90),
 (104,'2026-03-02 06:00:00',95.10),(104,'2026-03-02 07:00:00',98.60);

UPDATE equipo SET area = 'Pintura' WHERE equipo_id = 4;
SELECT equipo_id, nombre, area FROM equipo;

CREATE TABLE consumo_energia (
  orden_id    INT PRIMARY KEY,
  potencia_kw DECIMAL(6,2) NOT NULL,
  horas       DECIMAL(5,2) NOT NULL,
  energia_kwh DECIMAL(10,2) AS (potencia_kw * horas) STORED
);
INSERT INTO consumo_energia (orden_id, potencia_kw, horas) VALUES (1, 15.00, 4.00);
SELECT orden_id, potencia_kw, horas, energia_kwh FROM consumo_energia;
INSERT INTO consumo_energia (orden_id, potencia_kw, horas, energia_kwh)
VALUES (2, 15.00, 4.00, 1.00);
```

**Salida**

```
equipo_id	nombre	area
2	Robot de soldadura	Manufactura
4	Compresor de tornillo	Pintura

orden_id	potencia_kw	horas	energia_kwh
1	15.00	4.00	60.00

ERROR 3105 (HY000) at line 94: The value specified for generated column 'energia_kwh' in table 'consumo_energia' is not allowed.
```

Ataque por ataque sobre el modelo reparado: la lista en la celda ya no cabe, porque cada consumo es una fila. Las dos grafías del mismo equipo ya no son posibles, porque el nombre vive en un solo renglón de `equipo`. La anomalía de actualización tampoco, porque el `UPDATE` toca esa misma fila única y las cinco lecturas la ven cambiada a la vez.

Lo que se compró: un solo lugar donde vive cada hecho. Lo que se pagó: para leer una lectura con el nombre de su equipo ahora hacen falta dos JOIN, y esa factura llega completa en la semana 11.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres tablas con sus llaves foráneas, sin perder renglones | 3 |
| Los tres ataques se vuelven a intentar y se dice qué pasó con cada uno | 3 |
| La columna generada calcula 60.00 sola | 2 |
| El intento de escribirla a mano devuelve el 3105 | 1 |
| Se nombra el precio de normalizar en términos de JOIN | 1 |

**Error que más se ve**

Reparar borrando el renglón incómodo, el de la segunda grafía, en lugar de mudar la columna a su tabla; se delata porque el modelo reparado ya no acepta los mismos datos que el original.

---

## Semana 06 · Del modelo a las tablas y las llaves

### 06.1 · Reconocer

**Solución**

```sql
-- 1. medicion con valor 742.00 ........ rebota, ERROR 3819 (CHECK)
-- 2. medicion con valor vacio .......... PASA. El CHECK no evalua el desconocido.
-- 3. segundo certificado del equipo 1 .. rebota, ERROR 1062 (UNIQUE)
-- 4. sensor del equipo 77 .............. rebota, ERROR 1452 (FOREIGN KEY)
-- 5. equipo con estado 'reparacion' .... rebota, ERROR 1265 (fuera del ENUM)
-- 6. FK hacia una columna no unica ..... rebota, ERROR 6125
-- 7. FK entre VARCHAR(10) e INT ........ rebota, ERROR 3780

-- Los dos que comparten numero: ninguno. Los que comparten SQLSTATE son el 3
-- y el 4, los dos con 23000, porque para el servidor duplicado y llave foranea
-- rota son la misma clase, la de integridad.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los siete veredictos correctos | 4 |
| Los siete números de error | 3 |
| Se identifica el 2 como el único que pasa, y por qué | 2 |
| Se corrige la pregunta: lo que comparten el 3 y el 4 es el SQLSTATE 23000 | 1 |

**Error que más se ve**

Predecir que el valor vacío rebota porque «no está entre -50 y 500»; se delata porque una comparación contra el vacío no da falso, da desconocido, y el `CHECK` solo detiene lo que resultó falso.

### 06.2 · Aplicar

**Solución**

```sql
DROP DATABASE IF EXISTS planta_ddl;
CREATE DATABASE planta_ddl CHARACTER SET utf8mb4;
USE planta_ddl;

CREATE TABLE linea (
  linea_id INT PRIMARY KEY,
  nombre   VARCHAR(40) NOT NULL UNIQUE,
  area     VARCHAR(30) NOT NULL
);

CREATE TABLE equipo (
  equipo_id       INT PRIMARY KEY,
  codigo          CHAR(7)     NOT NULL UNIQUE,
  nombre          VARCHAR(60) NOT NULL,
  linea_id        INT         NOT NULL,
  equipo_padre_id INT         NULL,
  estado          ENUM('operando','paro','baja') NOT NULL,
  CONSTRAINT fk_equipo_linea FOREIGN KEY (linea_id)        REFERENCES linea(linea_id),
  CONSTRAINT fk_equipo_padre FOREIGN KEY (equipo_padre_id) REFERENCES equipo(equipo_id)
);

CREATE TABLE certificado (
  certificado_id INT PRIMARY KEY,
  equipo_id      INT     NOT NULL UNIQUE,
  folio          CHAR(9) NOT NULL,
  CONSTRAINT fk_cert_equipo FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);

CREATE TABLE sensor (
  sensor_id INT PRIMARY KEY,
  clave     CHAR(6) NOT NULL UNIQUE,
  equipo_id INT     NOT NULL,
  rango_min DECIMAL(7,2) NOT NULL,
  rango_max DECIMAL(7,2) NOT NULL,
  CONSTRAINT ck_sensor_rango  CHECK (rango_min < rango_max),
  CONSTRAINT fk_sensor_equipo FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);

CREATE TABLE medicion (
  medicion_id INT PRIMARY KEY,
  sensor_id   INT      NOT NULL,
  tomada_en   DATETIME NOT NULL,
  valor       DECIMAL(7,2) NULL,
  CONSTRAINT uq_medicion       UNIQUE (sensor_id, tomada_en),
  CONSTRAINT ck_medicion_valor CHECK (valor BETWEEN -50 AND 500),
  CONSTRAINT fk_medicion_sensor FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);

INSERT INTO linea  VALUES (1,'Ensamble A','Manufactura'),(2,'Pintura','Acabados');
INSERT INTO equipo VALUES (1,'EQ-0001','Prensa hidraulica 200 t',1,NULL,'operando'),
                          (2,'EQ-0002','Robot de soldadura',1,NULL,'operando');
INSERT INTO certificado VALUES (1,1,'CAL-24001');
INSERT INTO sensor      VALUES (1,'SN-101',1,0.00,120.00);
INSERT INTO medicion    VALUES (1,1,'2026-03-02 06:00:00',71.50);
```

**Salida**

El guion corre limpio dos veces seguidas y no imprime una sola línea. El `DROP DATABASE IF EXISTS` de la primera sentencia es lo que lo hace re-ejecutable.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco tablas en un orden que no necesita corrección manual | 3 |
| El 1:N, el 0:1 con UNIQUE y la recursiva están implementados | 3 |
| Aparecen al menos un CHECK, un UNIQUE y un ENUM propios | 2 |
| El guion corre dos veces seguidas sin editarlo | 2 |

**Error que más se ve**

Crear `equipo` antes que `linea` y arreglarlo moviendo bloques a mano cada vez; se delata en la segunda corrida, cuando el error vuelve a aparecer en el mismo renglón.

### 06.3 · Integrar

**Solución**

```sql
USE planta_ddl;
INSERT INTO medicion    VALUES (2,1,'2026-03-02 07:00:00',742.00);
INSERT INTO medicion    VALUES (3,1,'2026-03-02 07:00:00',NULL);
SELECT medicion_id, valor FROM medicion WHERE medicion_id = 3;
INSERT INTO certificado VALUES (2,1,'CAL-24099');
INSERT INTO sensor      VALUES (2,'SN-999',77,0.00,10.00);
INSERT INTO equipo      VALUES (3,'EQ-0003','Pinza del robot',1,2,'reparacion');

CREATE TABLE turno   (turno_id INT, nombre VARCHAR(20), INDEX ix_turno (turno_id));
CREATE TABLE orden_a (orden_id INT PRIMARY KEY, turno_id INT);
ALTER TABLE orden_a ADD FOREIGN KEY (turno_id) REFERENCES turno(turno_id);

CREATE TABLE orden_b (orden_id INT PRIMARY KEY, equipo_id VARCHAR(10));
ALTER TABLE orden_b ADD FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id);

-- El cierre del hueco. La fila 3 es la que entro vacia; se retira primero,
-- o el ALTER no puede convertir la columna.
DELETE FROM medicion WHERE medicion_id = 3;
ALTER TABLE medicion MODIFY valor DECIMAL(7,2) NOT NULL;
INSERT INTO medicion VALUES (5,1,'2026-03-02 09:00:00',NULL);

SHOW INDEX FROM sensor;
SELECT INDEX_NAME, SEQ_IN_INDEX, COLUMN_NAME, NON_UNIQUE
  FROM information_schema.STATISTICS
 WHERE TABLE_SCHEMA='planta_ddl' AND TABLE_NAME='medicion'
 ORDER BY INDEX_NAME, SEQ_IN_INDEX;
```

**Salida**

```
ERROR 3819 (HY000): Check constraint 'ck_medicion_valor' is violated.

medicion_id	valor
3	NULL

ERROR 1062 (23000): Duplicate entry '1' for key 'certificado.equipo_id'
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`planta_ddl`.`sensor`, CONSTRAINT `fk_sensor_equipo` FOREIGN KEY (`equipo_id`) REFERENCES `equipo` (`equipo_id`))
ERROR 1265 (01000): Data truncated for column 'estado' at row 1
ERROR 6125 (HY000): Failed to add the foreign key constraint. Missing unique key for constraint 'orden_a_ibfk_1' in the referenced table 'turno'
ERROR 3780 (HY000): Referencing column 'equipo_id' and referenced column 'equipo_id' in foreign key constraint 'orden_b_ibfk_1' are incompatible.

ERROR 1048 (23000): Column 'valor' cannot be null
```

```
Table	Non_unique	Key_name	Seq_in_index	Column_name
sensor	0	PRIMARY	1	sensor_id
sensor	0	clave	1	clave
sensor	1	fk_sensor_equipo	1	equipo_id

INDEX_NAME	SEQ_IN_INDEX	COLUMN_NAME	NON_UNIQUE
PRIMARY	1	medicion_id	0
uq_medicion	1	sensor_id	0
uq_medicion	2	tomada_en	0
```

`sensor` tiene un índice que nadie declaró, `fk_sensor_equipo`, escrito al declarar la llave foránea. `medicion` no lo tiene porque su llave foránea es `sensor_id`, y esa columna ya es la izquierda del índice único `uq_medicion`, así que el servidor reutilizó ese en lugar de escribir otro.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los siete intentos con su resultado real pegado | 3 |
| El hueco del `CHECK` se cierra con `NOT NULL` y se demuestra con el 1048 | 3 |
| Se muestra el índice que escribió la llave foránea en `sensor` | 2 |
| Se explica por qué `medicion` no lo necesitó | 2 |

**Error que más se ve**

Correr el `ALTER TABLE ... NOT NULL` sin borrar antes la fila vacía; se delata con `ERROR 1138 (22004) Invalid use of NULL value`, que es otra cosa: es el dato viejo estorbando, no la regla nueva funcionando.

---

## Semana 07 · Tipos de dato y DDL

### 07.1 · Reconocer

**Solución**

```sql
-- Comando          Familia   ¿Lo deshace el ROLLBACK?
-- TRUNCATE TABLE   DDL       no
-- INSERT           DML       si
-- GRANT            DCL       no
-- ROLLBACK         TCL       es el ROLLBACK
-- ALTER TABLE      DDL       no
-- DELETE           DML       si
-- REVOKE           DCL       no
-- CREATE INDEX     DDL       no

-- Las tres trazas
-- 1. TRUNCATE + ROLLBACK -> COUNT(*) = 0.  No se deshizo.
-- 2. CREATE   + ROLLBACK -> t_ddl sigue en la lista. No se deshizo.
-- 3. DELETE   + ROLLBACK -> 6, 5, 6.  Si se deshizo.
-- Lo que tienen en comun las dos primeras: las dos son DDL, y el DDL
-- confirma por su cuenta antes de que el ROLLBACK llegue.
```

**Salida**

```
tras_truncate_y_rollback
0

Tables_in_tipos (t_ddl)
t_ddl

antes
6
dentro
5
despues
6
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los ocho comandos en su familia | 3 |
| Las ocho respuestas sobre el ROLLBACK | 2 |
| Las tres trazas predichas correctamente | 3 |
| Se nombra el commit implícito del DDL como lo que comparten las dos primeras | 2 |

**Error que más se ve**

Clasificar `TRUNCATE` como DML porque «borra filas»; se delata con la pregunta de una línea, ya que en realidad tira la tabla y la vuelve a crear vacía.

### 07.2 · Aplicar

**Solución**

```sql
CREATE TABLE sensor (
  sensor_id INT AUTO_INCREMENT PRIMARY KEY,
  clave     CHAR(6)     NOT NULL UNIQUE,  -- siempre seis, CHAR se defiende aqui
  magnitud  VARCHAR(20) NOT NULL,         -- largo variable, de 7 a 11 letras
  instalado DATE        NOT NULL,         -- fecha, para poder compararla y restarla
  estado    ENUM('operando','paro','baja') NOT NULL  -- catalogo cerrado y corto
);
CREATE TABLE medicion (
  medicion_id INT PRIMARY KEY,
  sensor_id   INT NOT NULL,
  valor       DECIMAL(5,2) NOT NULL,      -- exacto; FLOAT es aproximado por diseño
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);

INSERT INTO sensor (clave, magnitud, instalado, estado)
VALUES ('SN-105','par','02/03/2026','operando');

INSERT INTO medicion VALUES (7,1,9999.9);

INSERT INTO sensor (clave, magnitud, instalado, estado)
VALUES ('SN-1060','par','2026-03-02','operando');

INSERT INTO sensor (clave, magnitud, instalado, estado)
VALUES ('SN-107', NULL,'2026-03-02','operando');
```

**Salida**

```
ERROR 1292 (22007) at line 50: Incorrect date value: '02/03/2026' for column 'instalado' at row 1
ERROR 1264 (22003) at line 54: Out of range value for column 'valor' at row 1
ERROR 1406 (22001) at line 57: Data too long for column 'clave' at row 1
ERROR 1048 (23000) at line 61: Column 'magnitud' cannot be null
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Cada columna trae su tipo y su razón en una línea | 4 |
| Los cuatro errores provocados, con su número | 4 |
| La razón del `DECIMAL` se defiende contra `FLOAT` | 1 |
| Ninguna fecha quedó en `VARCHAR` | 1 |

**Error que más se ve**

Justificar `CHAR(6)` diciendo que «ahorra memoria»; se delata en 07.3, donde la misma cadena con espacios al final se lee de vuelta distinta de como se guardó.

### 07.3 · Integrar

**Solución**

```sql
-- 1. El ENUM
SELECT sensor_id, clave, estado, estado + 0 AS valor_interno
  FROM sensor ORDER BY estado;

-- 2. La pareja que la fuente confunde
TRUNCATE TABLE sensor;
DELETE FROM sensor WHERE sensor_id = 1;

-- 3. El contador, sobre una tabla sin hijos
CREATE TABLE bitacora_paro (
  paro_id INT AUTO_INCREMENT PRIMARY KEY,
  motivo  VARCHAR(40) NOT NULL
);
INSERT INTO bitacora_paro (motivo)
VALUES ('Falla de sello'),('Sobrecarga'),('Cambio de herramental');
DELETE FROM bitacora_paro;
INSERT INTO bitacora_paro (motivo) VALUES ('Primera despues del DELETE');
SELECT paro_id, motivo FROM bitacora_paro;
TRUNCATE TABLE bitacora_paro;
INSERT INTO bitacora_paro (motivo) VALUES ('Primera despues del TRUNCATE');
SELECT paro_id, motivo FROM bitacora_paro;

-- El cierre
CREATE TABLE t_char    (v CHAR(6));
CREATE TABLE t_varchar (v VARCHAR(6));
INSERT INTO t_char    VALUES ('SN-1  ');
INSERT INTO t_varchar VALUES ('SN-1  ');
SELECT CONCAT('[',v,']') AS leido, LENGTH(v) AS bytes FROM t_char;
SELECT CONCAT('[',v,']') AS leido, LENGTH(v) AS bytes FROM t_varchar;
```

**Salida**

```
sensor_id	clave	estado	valor_interno
1	SN-101	operando	1
4	SN-104	operando	1
2	SN-102	paro	2
3	SN-103	baja	3

ERROR 1701 (42000) at line 69: Cannot truncate a table referenced in a foreign key constraint (`tipos`.`medicion`, CONSTRAINT `medicion_ibfk_1`)
ERROR 1451 (23000) at line 72: Cannot delete or update a parent row: a foreign key constraint fails (`tipos`.`medicion`, CONSTRAINT `medicion_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))

paro_id	motivo
4	Primera despues del DELETE

paro_id	motivo
1	Primera despues del TRUNCATE

leido	bytes
[SN-1]	4

leido	bytes
[SN-1  ]	6
```

El orden salió `operando`, `operando`, `paro`, `baja`, que es el orden en que se declaró el catálogo. Alfabéticamente habría salido `baja`, `operando`, `operando`, `paro`. El `estado + 0` muestra de dónde viene: cada valor guarda la posición que le tocó al escribirlo.

El contador arrancó en 4 después del `DELETE` y en 1 después del `TRUNCATE`. Ese salto es el argumento de que `TRUNCATE` no es un `DELETE` rápido.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El orden del ENUM se reporta y se explica con `estado + 0` | 3 |
| Los dos errores del padre, 1701 y 1451, con su número | 3 |
| Los dos identificadores del contador, 4 y 1 | 2 |
| `CHAR` devuelve `[SN-1]` con 4 bytes y `VARCHAR` devuelve `[SN-1  ]` con 6 | 2 |

**Error que más se ve**

Intentar la prueba del contador sobre `sensor`, que tiene hijos; se delata porque el `TRUNCATE` devuelve 1701 y el experimento se queda a medias sin que el alumno lo note.

---

## Semana 08 · DML y transacciones · Primer parcial

### 08.1 · Reconocer

**Solución**

```sql
-- al empezar                6
-- tras el primer DELETE     5
-- tras el segundo DELETE    4
-- tras ROLLBACK TO s1       5
-- tras el ROLLBACK final    6

-- Con COMMIT en lugar del ROLLBACK final, la tabla se queda en 5:
-- el ROLLBACK TO s1 solo retiro el segundo DELETE, no el primero.
-- Con autocommit en 1 y sin START TRANSACTION, cada DELETE ya se confirmo
-- solo; el ROLLBACK contesta Query OK y no cambia nada. La tabla queda en 4.
```

**Salida**

```
al_empezar
6
tras_el_primer_delete
5
tras_el_segundo_delete
4
tras_rollback_to_s1
5
tras_el_rollback_final
6
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco conteos en orden | 5 |
| La respuesta con `COMMIT` es 5, y se explica el alcance del `ROLLBACK TO` | 3 |
| La respuesta con autocommit es 4, y se dice que el `ROLLBACK` no protesta | 2 |

**Error que más se ve**

Creer que `ROLLBACK TO SAVEPOINT` cierra la transacción; se delata en el conteo final, que se predice en 5 en lugar de 6 porque se supone que el `ROLLBACK` de abajo ya no tenía nada que hacer.

### 08.2 · Aplicar

**Solución**

```sql
USE dml;
SELECT COUNT(*) AS antes FROM medicion;
INSERT INTO medicion (medicion_id, sensor_id, tomada_en, valor) VALUES
 (7,3,'2026-03-02 08:00:00', 44.90),
 (8,3,'2026-03-02 09:00:00',742.00),
 (9,3,'2026-03-02 10:00:00', 39.20);
SELECT COUNT(*) AS despues FROM medicion;

INSERT INTO medicion (medicion_id, sensor_id, tomada_en, valor) VALUES
 (7,3,'2026-03-02 08:00:00',44.90),
 (8,3,'2026-03-02 09:00:00',42.10),
 (9,3,'2026-03-02 10:00:00',39.20);
SELECT COUNT(*) AS despues FROM medicion;

INSERT INTO orden (equipo_id, tipo, fecha)
SELECT equipo_id, 'preventivo', '2026-04-01' FROM equipo WHERE linea_id = 1;
SELECT orden_id, equipo_id, tipo, fecha FROM orden;

SELECT equipo_id, ROUND(horas_operacion / paros, 2) AS horas_entre_paros
  FROM disponibilidad;
SHOW WARNINGS;

CREATE TABLE indicador (equipo_id INT PRIMARY KEY, mtbf DECIMAL(10,2));
INSERT INTO indicador (equipo_id, mtbf)
SELECT equipo_id, horas_operacion / paros FROM disponibilidad;
```

**Salida**

```
antes
6
ERROR 3819 (HY000) at line 73: Check constraint 'ck_medicion_valor' is violated.
despues
6

despues
9

orden_id	equipo_id	tipo	fecha
1	1	preventivo	2026-04-01
2	2	preventivo	2026-04-01

equipo_id	horas_entre_paros
1	120.00
2	230.17
4	NULL
Level	Code	Message
Warning	1365	Division by 0

ERROR 1365 (22012) at line 98: Division by 0
```

Antes 6 y después 6. La primera fila del `INSERT` de tres tampoco quedó: la sentencia entra completa o no entra, y esa garantía viene de fábrica.

La misma división contestó dos cosas distintas. En un `SELECT` devolvió vacío con una advertencia que nadie lee. Adentro de un `INSERT` levantó el error 1365 y tumbó la carga entera.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los conteos antes y después del `INSERT` malo son iguales | 3 |
| Se dice que la atomicidad de la sentencia no hubo que pedirla | 1 |
| El `INSERT ... SELECT` da de alta las órdenes sin teclear identificadores | 3 |
| La división aparece dos veces, con la advertencia y con el error 1365 | 3 |

**Error que más se ve**

Reparar la carga borrando la fila mala del guion y volver a correrlo sin verificar el conteo; se delata porque nunca se demuestra que la fila buena tampoco había entrado.

### 08.3 · Integrar

**Solución**

```sql
-- Parte uno. 1:N, llave foranea del lado muchos.
CREATE TABLE sensor (
  sensor_id INT PRIMARY KEY,
  clave     CHAR(6) NOT NULL UNIQUE,
  equipo_id INT NOT NULL,
  FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);

-- Parte dos.
-- La marca de tiempo no puede ir en VARCHAR: el error 1292 de la semana 7 es
-- justo el que impide guardar '02/03/2026', y en texto no se puede restar ni
-- ordenar cronologicamente.
-- El valor no puede ir en FLOAT: FLOAT es aproximado por diseño, y el error
-- 1264 de la semana 7 solo aparece porque DECIMAL(5,2) cuenta los digitos.

-- Parte tres.
START TRANSACTION;
INSERT INTO medicion (medicion_id, sensor_id, tomada_en, valor) VALUES
 (10,3,'2026-03-02 11:00:00',40.05),
 (11,3,'2026-03-02 12:00:00',43.70),
 (12,3,'2026-03-02 13:00:00',38.15);
SELECT COUNT(*) AS verificacion FROM medicion;
COMMIT;

-- Parte cuatro, condicion 1: el DDL de por medio
START TRANSACTION;
INSERT INTO sensor VALUES (4,'SN-104',4);
CREATE TABLE tmp_implicito (id INT);
ROLLBACK;
SELECT sensor_id, clave FROM sensor WHERE sensor_id = 4;

-- Condicion 2: la tabla que no es InnoDB
CREATE TABLE t_myisam (id INT PRIMARY KEY, nota VARCHAR(30)) ENGINE=MyISAM;
START TRANSACTION;
INSERT INTO t_myisam VALUES (1,'lectura de prueba');
ROLLBACK;
SELECT id, nota FROM t_myisam;

-- Condicion 3: sin transaccion abierta. Con @@autocommit = 1 cada sentencia
-- se confirma sola y el ROLLBACK contesta Query OK sin cambiar nada.
```

**Salida**

```
sensor_id	clave
4	SN-104

id	nota
1	lectura de prueba
```

La fila del sensor 4 sigue ahí después del `ROLLBACK`, porque el `CREATE TABLE` de en medio la confirmó antes de que nadie pudiera retirarla. La fila de MyISAM también sigue ahí, y ahí el `ROLLBACK` ni siquiera tenía nada que hacer.

La más peligrosa de las tres es la de MyISAM, y el argumento es que las otras dos dejan huella. El `CREATE TABLE` está a la vista en el guion y el autocommit se consulta con `SELECT @@autocommit`. El motor de la tabla no aparece en ninguna parte de la sentencia que estás escribiendo, así que el `ROLLBACK` no hace nada y tampoco dice nada.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Parte uno: cardinalidad, forma física y DDL que la implementa | 2 |
| Parte dos: las dos justificaciones citan un error medido | 2 |
| Parte tres: el conteo de verificación va antes del `COMMIT` | 3 |
| Parte cuatro: las tres condiciones demostradas con su corrida | 2 |
| El juicio sobre la más peligrosa viene con argumento | 1 |

**Error que más se ve**

Poner el `COMMIT` antes del `SELECT` de verificación; se delata porque entonces la verificación ya no puede corregir nada y el único remedio que queda es un `DELETE` de reparación.

---

## Semana 09 · El SELECT de una tabla

### 09.1 · Reconocer

**Solución**

```sql
-- equipos                8
-- criticidad = 'alta'    3
-- criticidad <> 'alta'   4
-- criticidad = NULL      0
-- criticidad IS NULL     1
-- mediciones            20
-- valor IS NOT NULL     15
-- valor IS NULL          5

-- 3 + 4 = 7, no 8. El equipo 8 no aparece en ninguna de las dos listas porque
-- su criticidad esta vacia, y una comparacion contra el vacio no contesta
-- verdadero ni falso: contesta desconocido. El WHERE solo deja pasar lo
-- verdadero, asi que el desconocido se va con lo falso.

-- Sin parentesis:  6 equipos.  AND se resuelve antes que OR.
-- Con parentesis:  5 equipos.
```

**Salida**

```
equipos	8
criticidad_alta	3
criticidad_no_alta	4
comparada_con_null	0
sin_criticidad	1
mediciones	20
con_valor	15
sin_valor	5
```

```
codigo	nombre	criticidad	estado
EQ-0001	Prensa hidráulica 200 t	alta	operando
EQ-0002	Robot de soldadura	alta	operando
EQ-0003	Pinza del robot	media	operando
EQ-0004	Compresor de tornillo	alta	paro
EQ-0005	Cabina de pintura	media	operando
EQ-0006	Bomba de recirculación	media	operando

codigo	nombre	criticidad	estado
EQ-0001	Prensa hidráulica 200 t	alta	operando
EQ-0002	Robot de soldadura	alta	operando
EQ-0003	Pinza del robot	media	operando
EQ-0005	Cabina de pintura	media	operando
EQ-0006	Bomba de recirculación	media	operando
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los ocho conteos | 4 |
| Se nombra el desconocido como tercer estado y se explica el hueco de una fila | 3 |
| Los dos conteos de la precedencia, 6 y 5 | 2 |
| Se identifica al equipo 4, en paro, como el que sale sobrando sin paréntesis | 1 |

**Error que más se ve**

Predecir 5 para `criticidad <> 'alta'`, contando al equipo sin criticidad; se delata porque entonces el total cerraría en 8 y el ejercicio no tendría caso.

### 09.2 · Aplicar

**Solución**

```sql
USE planta;
-- 1
SELECT codigo, nombre, estado FROM equipo WHERE estado = 'operando';

-- 2
SELECT @@collation_database AS colacion;
SELECT codigo, nombre FROM equipo WHERE nombre LIKE '%hidraulica%';
SELECT codigo, nombre FROM equipo WHERE nombre LIKE '%recirculacion%';
SELECT codigo, nombre FROM equipo WHERE nombre LIKE 'prensa%';

-- 3
SELECT clave, descripcion FROM refaccion WHERE descripcion LIKE '%50%';
SELECT clave, descripcion FROM refaccion WHERE descripcion LIKE '%50\%%';

-- 4
SELECT COUNT(*) AS con_between FROM medicion WHERE valor BETWEEN 6.40 AND 41.80;
SELECT COUNT(*) AS estrictos   FROM medicion WHERE valor >  6.40 AND valor < 41.80;
SELECT COUNT(*) AS al_reves    FROM medicion WHERE valor BETWEEN 41.80 AND 6.40;

-- 5
SELECT codigo, nombre FROM equipo ORDER BY codigo LIMIT 3;
SELECT codigo, nombre FROM equipo ORDER BY codigo LIMIT 3 OFFSET 3;
```

**Salida**

```
codigo	nombre	estado
EQ-0001	Prensa hidráulica 200 t	operando
EQ-0002	Robot de soldadura	operando
EQ-0003	Pinza del robot	operando
EQ-0005	Cabina de pintura	operando
EQ-0006	Bomba de recirculación	operando
EQ-0007	Banda transportadora	operando

colacion
utf8mb4_0900_ai_ci

codigo	nombre
EQ-0001	Prensa hidráulica 200 t

codigo	nombre
EQ-0006	Bomba de recirculación

codigo	nombre
EQ-0001	Prensa hidráulica 200 t

clave	descripcion
RF-001	Filtro de aire 50% eficiencia
RF-002	Filtro de aceite 50 micras
RF-003	Balero rígido de bolas 50 mm

clave	descripcion
RF-001	Filtro de aire 50% eficiencia

con_between
6
estrictos
4
al_reves
0

codigo	nombre
EQ-0001	Prensa hidráulica 200 t
EQ-0002	Robot de soldadura
EQ-0003	Pinza del robot

codigo	nombre
EQ-0004	Compresor de tornillo
EQ-0005	Cabina de pintura
EQ-0006	Bomba de recirculación
```

Nadie escribió manejo de acentos ni de mayúsculas. La colación `utf8mb4_0900_ai_ci` ya viene puesta en el servidor: `ai` ignora acentos y `ci` ignora mayúsculas.

Los límites del `BETWEEN` entran, y por eso 6 contra 4. Las dos lecturas que hacen la diferencia son la de 6.40 y la de 41.80, que son exactamente los extremos.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El filtro exacto devuelve los seis equipos operando | 2 |
| Las tres búsquedas de texto funcionan y se cita la colación | 3 |
| El `50%` literal devuelve una sola refacción, con el comodín escapado | 2 |
| Los tres conteos del rango, 6, 4 y 0 | 2 |
| Las dos páginas de tres, con `ORDER BY` | 1 |

**Error que más se ve**

Escribir `LIKE '%50%%'` para buscar el porcentaje literal; se delata porque devuelve las mismas tres refacciones que sin escapar, ya que el segundo `%` se sigue leyendo como comodín.

### 09.3 · Integrar

**Solución**

```sql
-- 1. El canal que ordena como texto
SELECT clave, canal FROM sensor ORDER BY canal;
SELECT '10' < '9' AS como_texto, 10 < 9 AS como_numero;
-- La reparacion de raiz, con el tipo de la semana 7:
--   ALTER TABLE sensor MODIFY canal SMALLINT NOT NULL;

-- 2. El alias
SELECT clave, rango_max - rango_min AS amplitud FROM sensor WHERE amplitud > 100;
SELECT clave, rango_max - rango_min AS amplitud FROM sensor
 ORDER BY amplitud DESC LIMIT 3;

-- 3. Los NULL al final
SELECT medicion_id, valor FROM medicion ORDER BY valor ASC LIMIT 3;
SELECT medicion_id, valor FROM medicion ORDER BY valor IS NULL, valor ASC LIMIT 3;
SELECT medicion_id, valor FROM medicion ORDER BY valor ASC NULLS LAST;

-- El cierre
SELECT codigo, nombre FROM equipo LIMIT 3;
SELECT codigo  nombre FROM equipo LIMIT 3;
```

**Salida**

```
clave	canal
SN-101	1
SN-104	10
SN-105	100
SN-102	2
SN-106	3
SN-103	9

como_texto	como_numero
1	0

ERROR 1054 (42S22) at line 44: Unknown column 'amplitud' in 'where clause'

clave	amplitud
SN-105	250.00
SN-101	120.00
SN-104	120.00

medicion_id	valor
7	NULL
11	NULL
3	NULL

medicion_id	valor
5	6.40
6	6.55
19	8.75

ERROR 1064 (42000) at line 55: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'NULLS LAST' at line 1

codigo	nombre
EQ-0001	Prensa hidráulica 200 t
EQ-0002	Robot de soldadura
EQ-0003	Pinza del robot

nombre
EQ-0001
EQ-0002
EQ-0003
```

El alias nace en el `SELECT`, que corre en el paso 5. El `WHERE` corre en el paso 2, cuando todavía no existe, y por eso sale 1054. El `ORDER BY` corre en el paso 6 y sí lo alcanza a ver.

La segunda consulta del cierre no dio error y el reporte salió mal: sin la coma, `nombre` se leyó como alias de `codigo`, así que el encabezado dice `nombre` y debajo van los códigos.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El orden del canal se reporta y se explica con `'10' < '9'` | 2 |
| Se propone el cambio de tipo como reparación de raíz | 1 |
| El 1054 y la versión que sí funciona, explicados con el orden lógico | 3 |
| Los vacíos se mandan al final sin usar `NULLS LAST`, y el 1064 queda de registro | 2 |
| La coma que falta se corre y se explica el encabezado | 2 |

**Error que más se ve**

Mandar los vacíos al final con `ORDER BY valor DESC`; se delata porque eso también invierte el orden de los demás, y lo que se pedía era conservarlo.

---

## Semana 10 · Agrupación y agregados

### 10.1 · Reconocer

**Solución**

```sql
-- n      20      COUNT(*) cuenta todas las filas
-- c      15      COUNT(valor) se salta las cinco vacias
-- prom   73.050000
-- mn      6.40
-- mx    191.40

-- suma      1095.75
-- entre_20    54.787500   divide entre 20: no es el promedio
-- entre_15    73.050000   divide entre 15: este si, y coincide con AVG

-- El promedio se calculo con 15 de las 20 lecturas. Quien reciba el reporte
-- no lo va a sacar de ninguna parte: la cifra no trae la nota que lo diga.
```

**Salida**

```
n	c	prom	mn	mx
20	15	73.050000	6.40	191.40

suma	entre_20	entre_15
1095.75	54.787500	73.050000
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco valores del primer renglón | 4 |
| Los tres del segundo | 3 |
| Se identifica `entre_15` como el promedio de verdad, igual a `AVG` | 2 |
| Se dice que la cifra viaja sin la nota de cuántas filas se saltó | 1 |

**Error que más se ve**

Predecir `prom` como la suma entre 20; se delata porque no coincide con `AVG`, y `AVG` divide entre las filas que sí traen dato.

### 10.2 · Aplicar

**Solución**

```sql
USE planta;
-- 1
SELECT tipo, folio, COUNT(*) FROM orden GROUP BY tipo;           -- provoca el 1055
SELECT tipo, COUNT(*) AS ordenes FROM orden GROUP BY tipo;       -- corregida

-- 2
SELECT equipo_id, COUNT(*) AS ordenes, COUNT(horas) AS con_horas,
       SUM(horas) AS horas_totales, AVG(horas) AS promedio
  FROM orden GROUP BY equipo_id ORDER BY equipo_id;

-- 3
SELECT equipo_id, COUNT(*) AS ordenes FROM orden WHERE ordenes > 2 GROUP BY equipo_id;
SELECT equipo_id, COUNT(*) AS ordenes FROM orden GROUP BY equipo_id HAVING ordenes > 2;

-- 4
SELECT equipo_id,
  SUM(CASE WHEN tipo='preventivo' THEN 1 ELSE 0 END) AS prev,
  SUM(CASE WHEN tipo='correctivo' THEN 1 ELSE 0 END) AS corr,
  SUM(CASE WHEN tipo='predictivo' THEN 1 ELSE 0 END) AS pred
  FROM orden GROUP BY equipo_id ORDER BY equipo_id;

-- 5
SELECT @@lc_time_names AS idioma;
SELECT YEAR(fecha) AS anio, MONTHNAME(fecha) AS mes,
       COUNT(*) AS ordenes, SUM(horas) AS horas
  FROM orden
 GROUP BY YEAR(fecha), MONTH(fecha), MONTHNAME(fecha)
 ORDER BY anio, MONTH(fecha);
SET lc_time_names = 'es_MX';
SELECT MONTHNAME('2026-02-14') AS mes;
```

**Salida**

```
ERROR 1055 (42000) at line 23: Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'planta.orden.folio' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

tipo	ordenes
preventivo	5
correctivo	5
predictivo	2

equipo_id	ordenes	con_horas	horas_totales	promedio
1	2	2	9.50	4.750000
2	3	2	10.25	5.125000
4	2	2	21.50	10.750000
5	2	2	8.25	4.125000
6	1	1	5.00	5.000000
7	2	1	1.75	1.750000

ERROR 1054 (42S22) at line 38: Unknown column 'ordenes' in 'where clause'

equipo_id	ordenes
2	3

equipo_id	prev	corr	pred
1	1	1	0
2	1	1	1
4	0	2	0
5	2	0	0
6	0	1	0
7	1	0	1

idioma
en_US

anio	mes	ordenes	horas
2026	January	4	15.25
2026	February	6	31.50
2026	March	2	9.50

mes
febrero
```

El 1055 trae la regla en su propia redacción: si un renglón resume varias filas, cada columna que nombres tiene que valer lo mismo para todo el grupo, y `folio` no vale lo mismo para las cinco órdenes preventivas.

El alias no existe en el `WHERE` y sí en el `HAVING`. El `WHERE` corre en el paso 2, antes de que el `SELECT` cree el alias. El equipo 2 es el único con más de dos órdenes.

El mes sale en inglés porque `@@lc_time_names` vale `en_US` en el servidor, no porque el dato esté en inglés.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El 1055 provocado y corregido, con la explicación de la regla | 3 |
| Las órdenes por equipo con las cuatro columnas | 2 |
| El contraste `WHERE` contra `HAVING`, con el 1054 pegado | 2 |
| El pivote con agregado condicional | 2 |
| El mes en inglés explicado con `lc_time_names` | 1 |

**Error que más se ve**

Rellenar el `GROUP BY` con todas las columnas del `SELECT` para callar el 1055; se delata porque los grupos se parten y el conteo por tipo pasa de 3 renglones a 12.

### 10.3 · Integrar

**Solución**

```sql
SELECT COUNT(*) AS con_not_in FROM equipo e
 WHERE e.equipo_id NOT IN (SELECT equipo_padre_id FROM equipo);

SELECT COUNT(*) AS con_not_exists FROM equipo e
 WHERE NOT EXISTS (SELECT 1 FROM equipo h WHERE h.equipo_padre_id = e.equipo_id);

SELECT COUNT(*) AS padres_nulos FROM equipo WHERE equipo_padre_id IS NULL;

WITH carga AS (
  SELECT equipo_id, COUNT(*) AS ordenes FROM orden GROUP BY equipo_id
)
SELECT equipo_id, ordenes FROM carga
 WHERE ordenes > (SELECT AVG(ordenes) FROM carga)
 ORDER BY ordenes DESC;

SELECT clave, punto_reorden,
  CASE
    WHEN punto_reorden >= 8    THEN 'alto'
    WHEN punto_reorden >= 3    THEN 'medio'
    WHEN punto_reorden IS NULL THEN 'sin punto fijado'
    ELSE 'bajo'
  END AS tramo
  FROM refaccion ORDER BY refaccion_id;

SELECT clave, punto_reorden,
  IF(punto_reorden >= 3, 'con punto', 'sin punto') AS tramo
  FROM refaccion ORDER BY refaccion_id;
```

**Salida**

```
con_not_in
0
con_not_exists
6
padres_nulos
6

equipo_id	ordenes
2	3

clave	punto_reorden	tramo
RF-001	4	medio
RF-002	4	medio
RF-003	8	alto
RF-004	2	bajo
RF-005	0	bajo
RF-006	NULL	sin punto fijado
RF-007	3	medio

clave	punto_reorden	tramo
RF-001	4	con punto
RF-002	4	con punto
RF-003	8	con punto
RF-004	2	sin punto
RF-005	0	sin punto
RF-006	NULL	sin punto
RF-007	3	con punto
```

La misma pregunta contestó 0 y contestó 6, sin error y sin advertencia. `NOT IN` compara contra una lista que trae seis vacíos, y en cuanto un elemento de la lista es desconocido la respuesta entera se vuelve desconocida. `NOT EXISTS` pregunta si existe una fila que cumpla, y esa pregunta sí tiene respuesta.

Las dos clasificaciones dejan de estar de acuerdo en `RF-006`. El `CASE` la manda a `sin punto fijado` y el `IF` la manda a `sin punto`, la misma casilla donde puso a `RF-005`, que tiene punto de reorden 0. El `IF` está mal: un punto de reorden en 0 es una decisión tomada y un punto de reorden vacío es una decisión que nadie tomó.

La `WITH` ahorró escribir la agrupación dos veces, una para el conjunto y otra para su propio promedio.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres conteos, 0, 6 y 6 | 3 |
| Se explica el 0 con el vacío adentro de la lista | 2 |
| La `WITH` corre y se dice qué ahorró | 2 |
| Las dos clasificaciones se muestran completas | 1 |
| Se señala `RF-006` como el renglón del desacuerdo y se dice cuál está mal | 2 |

**Error que más se ve**

Concluir que `NOT IN` está roto; se delata porque sobre una lista sin vacíos contesta lo mismo que `NOT EXISTS`, y lo que falla no es el operador sino la suposición de que la lista no trae desconocidos.

---

## Semana 11 · JOIN, UNION y UNION ALL

### 11.1 · Reconocer

**Solución**

```sql
-- 1. INNER JOIN                            12 filas
-- 2. LEFT JOIN                             14 filas
-- 3. LEFT JOIN + WHERE o.orden_id IS NULL   2 equipos: EQ-0003 y EQ-0008
-- 4. Para el equipo 3: COUNT(*) = 1 y COUNT(o.orden_id) = 0

-- La fila que COUNT(*) esta contando no existe en ninguna de las dos tablas.
-- La fabrico el LEFT JOIN: trae al equipo 3 aunque no caso con nada, y rellena
-- con vacio todas las columnas del lado derecho. COUNT(*) la cuenta porque hay
-- una fila; COUNT(o.orden_id) no, porque esa columna llego vacia.
```

**Salida**

```
con_inner
12
con_left
14

equipo_id	codigo
3	EQ-0003
8	EQ-0008

equipo_id	con_asterisco	con_columna
1	2	2
2	3	3
3	1	0
4	2	2
5	2	2
6	1	1
7	2	2
8	1	0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro números: 12, 14, 2, y el par 1 y 0 | 4 |
| Se explica de dónde sale la fila que `COUNT(*)` cuenta | 4 |
| Se identifican los dos equipos sin órdenes | 2 |

**Error que más se ve**

Predecir 14 para el `INNER JOIN` y 12 para el `LEFT JOIN`; se delata porque el `LEFT JOIN` nunca devuelve menos filas que el `INNER JOIN` sobre las mismas tablas.

### 11.2 · Aplicar

**Solución**

```sql
USE planta;
-- «La medicion cuyo sensor es este, y el equipo al que pertenece ese sensor.»
SELECT e.codigo, s.clave, m.tomada_en, m.valor
  FROM medicion m
  JOIN sensor s ON s.sensor_id = m.sensor_id
  JOIN equipo e ON e.equipo_id = s.equipo_id
 WHERE m.valor IS NOT NULL
 ORDER BY e.codigo, s.clave, m.tomada_en
 LIMIT 6;

SELECT COUNT(*) AS filas FROM equipo e
  LEFT JOIN orden o ON o.equipo_id = e.equipo_id
 WHERE o.tipo = 'correctivo';

SELECT COUNT(*) AS filas FROM equipo e
  LEFT JOIN orden o ON o.equipo_id = e.equipo_id AND o.tipo = 'correctivo';

SELECT COUNT(*) AS producto_cartesiano FROM linea, equipo;
```

**Salida**

```
codigo	clave	tomada_en	valor
EQ-0001	SN-101	2026-03-02 06:00:00	71.50
EQ-0001	SN-101	2026-03-02 07:00:00	74.20
EQ-0001	SN-101	2026-03-02 09:00:00	78.90
EQ-0001	SN-102	2026-03-02 06:00:00	6.40
EQ-0001	SN-102	2026-03-02 07:00:00	6.55
EQ-0002	SN-103	2026-03-02 06:00:00	12.30

filas
5

filas
9

producto_cartesiano
24
```

Con el predicado en el `WHERE` salen 5 filas. El `LEFT JOIN` fabricó sus filas de vacíos y después el `WHERE` las descartó, porque `o.tipo` valía vacío en todas ellas y el vacío nunca es igual a `'correctivo'`. El `LEFT JOIN` volvió a ser un `INNER JOIN`.

Con el predicado en el `ON` salen 9. Ahí se aplica antes, al decidir qué casa con qué, y los cuatro equipos sin órdenes correctivas siguen apareciendo con sus columnas de la derecha vacías.

El producto cartesiano son 3 líneas por 8 equipos. La consulta es legal y nadie levanta la mano.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El JOIN de tres tablas corre y une por llave, no por nombre | 3 |
| Cada `ON` trae su frase en el comentario | 1 |
| Los dos conteos, 5 y 9 | 3 |
| Se explica por qué el `WHERE` convirtió el `LEFT` en `INNER` | 2 |
| El producto cartesiano se reporta en 24 | 1 |

**Error que más se ve**

Unir `sensor` con `equipo` por el nombre en lugar de por la llave; se delata porque devuelve cero filas, ya que ningún nombre de sensor coincide con ninguno de equipo.

### 11.3 · Integrar

**Solución**

```sql
SELECT r.clave, i.clave FROM refaccion r
  FULL OUTER JOIN inventario_linea i ON i.clave = r.clave;

SELECT COUNT(*) AS del_left  FROM refaccion r
  LEFT  JOIN inventario_linea i ON i.clave = r.clave;
SELECT COUNT(*) AS del_right FROM refaccion r
  RIGHT JOIN inventario_linea i ON i.clave = r.clave;
SELECT COUNT(*) AS coinciden FROM refaccion r
  JOIN inventario_linea i ON i.clave = r.clave;

SELECT r.clave AS central, i.clave AS linea FROM refaccion r
  LEFT JOIN inventario_linea i ON i.clave = r.clave
UNION
SELECT r.clave, i.clave FROM refaccion r
  RIGHT JOIN inventario_linea i ON i.clave = r.clave
ORDER BY central, linea;

SELECT COUNT(*) AS filas, SUM(cantidad) AS piezas FROM (
  SELECT clave, cantidad FROM consumo_turno_a
  UNION ALL
  SELECT clave, cantidad FROM consumo_turno_b) t;

SELECT COUNT(*) AS filas, SUM(cantidad) AS piezas FROM (
  SELECT clave, cantidad FROM consumo_turno_a
  UNION
  SELECT clave, cantidad FROM consumo_turno_b) t;
```

**Salida**

```
ERROR 1064 (42000) at line 59: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'FULL OUTER JOIN inventario_linea i ON i.clave = r.clave' at line 2

del_left
7
del_right
8
coinciden
5
la_union
10

central	linea
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

filas	piezas
7	18

filas	piezas
4	9
```

Los tres bloques: cinco refacciones están en los dos lados, dos solo en el almacén central (`RF-006` y `RF-007`) y tres solo en la línea (`RF-101`, `RF-102`, `RF-103`). 5 + 2 + 3 = 10.

El consumo real del almacén son 18 piezas en 7 salidas. El `UNION` contestó 9 porque los dos turnos sacaron el mismo balero `RF-003` con la misma cantidad, y una fila idéntica a otra le pareció un duplicado. Cuando las filas representan cosas que pasaron se apilan con `UNION ALL`; `UNION` es para pedir la lista de valores distintos, y cobra una tabla temporal por ello.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El 1064 del `FULL OUTER JOIN` pegado | 1 |
| Los cuatro conteos: 7, 8, 5 y 10 | 3 |
| Las diez filas leídas en los tres bloques | 2 |
| La proyección trae las dos claves | 1 |
| Los dos pares de números del consumo, 7/18 y 4/9 | 2 |
| Se dice cuál es el consumo real y por qué el otro salió callado | 1 |

**Error que más se ve**

Proyectar solo la descripción en lugar de la clave; se delata porque las descripciones de las dos tablas están escritas distinto y el conteo de la unión sube en lugar de cerrar en 10.

---

## Semana 12 · Vistas

### 12.1 · Reconocer

**Solución**

```sql
-- IS_UPDATABLE segun el catalogo
-- v_medicion_completa    YES
-- v_medicion_izquierda   NO
-- v_carga_sensor         NO
-- v_sensor_conteo        YES

-- Los cinco intentos
-- 1. UPDATE de una sola tabla base por v_medicion_completa ... pasa
-- 2. UPDATE que toca dos tablas base .............. ERROR 1393
-- 3. DELETE por v_medicion_completa ............... ERROR 1395
-- 4. UPDATE por v_medicion_izquierda .............. ERROR 1288
-- 5. UPDATE por v_sensor_conteo ................... ERROR 1288

-- El desacuerdo es el 5. El catalogo dice YES y el servidor contesta 1288,
-- y el UPDATE ni siquiera tocaba la columna calculada. La regla operativa:
-- se prueba el UPDATE, no se le cree a la columna IS_UPDATABLE.
```

**Salida**

```
TABLE_NAME	IS_UPDATABLE
v_carga_sensor	NO
v_medicion_completa	YES
v_medicion_izquierda	NO
v_sensor_conteo	YES

medicion_id	valor
4	79.90

ERROR 1393 (HY000) at line 33: Can not modify more than one base table through a join view 'planta.v_medicion_completa'
ERROR 1395 (HY000) at line 36: Can not delete from join view 'planta.v_medicion_completa'
ERROR 1288 (HY000) at line 39: The target table v_medicion_izquierda of the UPDATE is not updatable
ERROR 1288 (HY000) at line 42: The target table v_carga_sensor of the UPDATE is not updatable
ERROR 1288 (HY000) at line 45: The target table v_sensor_conteo of the UPDATE is not updatable
```

La frontera real no está en el JOIN. Una vista con `INNER JOIN` sí acepta escritura, mientras toque una sola tabla base y no sea un `DELETE`. Donde sí cae la frontera es en el outer join, en la agregación y en la subconsulta escalar.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro valores de `IS_UPDATABLE` | 3 |
| Los cinco resultados con su número de error | 4 |
| Se identifica `v_sensor_conteo` como el desacuerdo | 2 |
| Se enuncia la regla operativa de probar el UPDATE | 1 |

**Error que más se ve**

Predecir `NO` para `v_medicion_completa` repitiendo que «una vista con JOIN no es actualizable»; se delata porque el catálogo dice `YES` y el `UPDATE` de una sola tabla base sí movió la fila.

### 12.2 · Aplicar

**Solución**

```sql
USE planta;
-- Capa 1: limpia y renombra, una sola tabla
CREATE OR REPLACE VIEW v_equipo_base AS
SELECT equipo_id, codigo, nombre, linea_id, estado, criticidad FROM equipo;

-- Capa 2: la regla del area, sobre la capa 1
CREATE OR REPLACE VIEW v_equipo_critico AS
SELECT equipo_id, codigo, nombre, linea_id FROM v_equipo_base
 WHERE criticidad = 'alta' AND estado = 'operando';

-- Capa 3: agrega y aplana
CREATE OR REPLACE VIEW v_carga_por_linea AS
SELECT linea_id, COUNT(*) AS equipos FROM v_equipo_base GROUP BY linea_id;

SELECT * FROM v_equipo_critico;
SELECT * FROM v_carga_por_linea ORDER BY linea_id;

UPDATE v_equipo_base     SET criticidad = 'alta' WHERE equipo_id = 3;
UPDATE v_carga_por_linea SET equipos = 9 WHERE linea_id = 1;

-- La vista del coordinador, sin cerrar
CREATE OR REPLACE VIEW v_equipo_manufactura_sin AS
SELECT equipo_id, codigo, nombre, linea_id, fecha_instalacion, estado
  FROM equipo WHERE linea_id = 1;
INSERT INTO v_equipo_manufactura_sin
  (equipo_id, codigo, nombre, linea_id, fecha_instalacion, estado)
VALUES (21,'EQ-0021','Mesa de inspeccion', 3, '2026-03-01','operando');
SELECT COUNT(*) AS la_ve_el_coordinador FROM v_equipo_manufactura_sin WHERE equipo_id = 21;
SELECT COUNT(*) AS esta_en_la_tabla     FROM equipo WHERE equipo_id = 21;

-- Cerrada
CREATE OR REPLACE VIEW v_equipo_manufactura AS
SELECT equipo_id, codigo, nombre, linea_id, fecha_instalacion, estado
  FROM equipo WHERE linea_id = 1
WITH CHECK OPTION;
INSERT INTO v_equipo_manufactura
  (equipo_id, codigo, nombre, linea_id, fecha_instalacion, estado)
VALUES (20,'EQ-0020','Mesa de inspeccion', 3, '2026-03-01','operando');
SELECT CHECK_OPTION FROM information_schema.VIEWS
 WHERE TABLE_SCHEMA='planta' AND TABLE_NAME='v_equipo_manufactura';
```

**Salida**

```
equipo_id	codigo	nombre	linea_id
1	EQ-0001	Prensa hidráulica 200 t	1
2	EQ-0002	Robot de soldadura	1

linea_id	equipos
1	3
2	3
3	2

TABLE_NAME	IS_UPDATABLE
v_carga_por_linea	NO
v_equipo_base	YES
v_equipo_critico	YES

equipo_id	criticidad
3	alta

ERROR 1288 (HY000) at line 64: The target table v_carga_por_linea of the UPDATE is not updatable

la_ve_el_coordinador
0
esta_en_la_tabla
1

ERROR 1369 (HY000) at line 71: CHECK OPTION failed 'planta.v_equipo_manufactura'

CHECK_OPTION
CASCADED
```

La capa 2 sigue siendo actualizable aunque esté construida sobre otra vista, porque debajo hay una sola tabla base. La capa 3 no podía hacer otra cosa: cada renglón suyo resume varios de la tabla, así que no existe una fila que un `UPDATE` pueda ir a modificar. Si la vista parece un reporte, es de solo lectura.

Sin `WITH CHECK OPTION` la fila entró a la tabla y desapareció de la pantalla de quien la escribió: 0 en la vista y 1 en la tabla base.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres capas, cada una apoyada en la anterior y no en la tabla | 3 |
| Los tres `UPDATE` intentados, con su salida | 3 |
| Se explica por qué la capa de reporte no puede aceptar escritura | 1 |
| La fila que se pierde se demuestra con los dos conteos, 0 y 1 | 2 |
| El `WITH CHECK OPTION` la detiene con el 1369 | 1 |

**Error que más se ve**

Construir la capa 2 sobre la tabla base en lugar de sobre la capa 1; se delata porque el guion sigue funcionando y el ejercicio pierde su punto, que era medir si apilar vistas rompe la actualizabilidad.

### 12.3 · Integrar

**Solución**

```sql
USE planta;
-- 1. El asterisco
CREATE OR REPLACE VIEW v_refaccion_estrella AS SELECT * FROM refaccion;
ALTER TABLE refaccion ADD COLUMN ubicacion VARCHAR(20) NULL;
SELECT * FROM v_refaccion_estrella WHERE refaccion_id = 1;
SELECT * FROM refaccion            WHERE refaccion_id = 1;
SHOW CREATE VIEW v_refaccion_estrella;
ALTER TABLE refaccion DROP COLUMN ubicacion;

-- 2. El orden
CREATE OR REPLACE VIEW v_orden_desc AS
SELECT orden_id, folio, equipo_id FROM orden ORDER BY folio DESC;
SELECT folio FROM v_orden_desc LIMIT 3;
SELECT v.folio FROM v_orden_desc v JOIN equipo e ON e.equipo_id = v.equipo_id LIMIT 3;

-- 3. La velocidad
EXPLAIN SELECT medicion_id, sensor, equipo, valor FROM v_medicion_completa;

SELECT TABLE_NAME, DEFINER, SECURITY_TYPE FROM information_schema.VIEWS
 WHERE TABLE_SCHEMA='planta' AND TABLE_NAME='v_medicion_completa';
```

**Salida**

```
refaccion_id	clave	descripcion	existencia	punto_reorden
1	RF-001	Filtro de aire 50% eficiencia	12	4

refaccion_id	clave	descripcion	existencia	punto_reorden	ubicacion
1	RF-001	Filtro de aire 50% eficiencia	12	4	NULL

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
        -> Single-row index lookup on e using PRIMARY (equipo_id = s.equipo_id)  (cost=0.267 rows=1)
    -> Index lookup on m using sensor_id (sensor_id = s.sensor_id)  (cost=0.556 rows=3.33)

TABLE_NAME	DEFINER	SECURITY_TYPE
v_medicion_completa	root@localhost	DEFINER
```

La vista devuelve cinco columnas y la tabla seis. `SHOW CREATE VIEW` explica por qué: MySQL expandió el asterisco al crearla y guardó la lista de columnas que existían ese día. La columna nueva no va a aparecer nunca, y no hay error ni advertencia que lo diga.

La misma vista salió en dos órdenes distintos según cómo se la consultó. El orden pertenece a la consulta final, no al objeto.

El plan nombra a `m`, a `s` y a `e`. El nombre `v_medicion_completa` aparece cero veces, porque el algoritmo es `MERGE`: la vista se sustituye por su texto y lo que se optimiza son las tablas base. Guardar una consulta no la acelera.

El `DEFINER` quedó en `root@localhost` con `SQL SECURITY DEFINER`, y nadie lo pidió. Eso se cobra en la semana 17, cuando la vista corra con los permisos de quien la creó y no con los de quien la consulta.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos salidas del asterisco, de cinco y seis columnas, con `SHOW CREATE VIEW` | 3 |
| Los dos órdenes de la misma vista, y a quién pertenece el orden | 3 |
| El plan pegado, con el conteo de veces que nombra a la vista | 2 |
| El `DEFINER` reportado y ubicado en la semana 17 | 2 |

**Error que más se ve**

Correr el `EXPLAIN` con un filtro por llave, que colapsa el árbol a un solo renglón; se delata porque ya no se ven las tres tablas y el argumento de que la vista no aparece se queda sin evidencia.

---

## Semana 13 · Procedimientos y errores · Segundo parcial

### 13.1 · Reconocer

**Solución**

```sql
-- CALL sp_malo(1) contesta 20, que son todas las filas de la tabla.
-- El WHERE comparo el parametro contra si mismo: sensor_id = sensor_id es
-- verdadero en toda fila donde no sea vacio. La columna quedo tapada por el
-- parametro, que tiene el mismo nombre y gana.
-- El unico cambio que lo arregla es renombrar el parametro:  p_sensor_id.
-- Con ese nombre contesta 4.

-- Los cuatro SIGNAL
-- '45000' 'Operacion no permitida' ......... ERROR 1644 (45000)
-- '23000' 'Integridad violada' ............. ERROR 1644 (23000)
-- '22012' 'Division entre cero' ............ ERROR 1644 (22012)
-- '45000' + MYSQL_ERRNO = 3001 ............. ERROR 3001 (45000)
-- SIGNAL siempre sale con 1644, elijas el SQLSTATE que elijas. El SQLSTATE es
-- una etiqueta que el servidor transporta. MYSQL_ERRNO es lo unico que tu
-- aplicacion puede usar para distinguir un error tuyo de otro.
```

**Salida**

```
filas_devueltas
20

filas_devueltas
4

ERROR 1644 (45000) at line 39: Operacion no permitida
ERROR 1644 (23000) at line 40: Integridad violada
ERROR 1644 (22012) at line 41: Division entre cero
ERROR 3001 (45000) at line 42: Valor fuera de la escala del sensor
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Se predice 20 y se explica que el `WHERE` comparó el parámetro consigo mismo | 4 |
| El arreglo es renombrar el parámetro, y con él contesta 4 | 2 |
| Los cuatro números de error: tres 1644 y un 3001 | 3 |
| Se nombra `MYSQL_ERRNO` como la única pieza que distingue | 1 |

**Error que más se ve**

Predecir 4 porque «el procedimiento recibe 1»; se delata al correrlo, y la causa se ve en cuanto se cambia el nombre del parámetro y la respuesta cambia sin tocar el `WHERE`.

### 13.2 · Aplicar

**Solución**

```sql
USE planta;
DROP PROCEDURE IF EXISTS sp_carga_equipo;   -- sin esto, la segunda corrida
DELIMITER $$                                 -- muere con ERROR 1305
CREATE PROCEDURE sp_carga_equipo(IN p_equipo_id INT, OUT p_ordenes INT)
BEGIN
  -- El prefijo p_ no es estilo: sin el, p_equipo_id taparia a la columna
  -- equipo_id y el WHERE se compararia consigo mismo, como en 13.1.
  SELECT COUNT(*) INTO p_ordenes FROM orden WHERE equipo_id = p_equipo_id;
  SELECT e.codigo, e.nombre, COUNT(o.orden_id) AS ordenes, SUM(o.horas) AS horas
    FROM equipo e
    LEFT JOIN orden o ON o.equipo_id = e.equipo_id
   WHERE e.equipo_id = p_equipo_id
   GROUP BY e.equipo_id, e.codigo, e.nombre;
END$$
DELIMITER ;

CALL sp_carga_equipo(2, @n);
SELECT @n AS ordenes_del_equipo_2;

CALL sp_carga_equipo(2, 5);

DROP PROCEDURE IF EXISTS sp_acumula;
DELIMITER $$
CREATE PROCEDURE sp_acumula(IN p_sensor_id INT, OUT p_total INT, INOUT p_acum INT)
BEGIN
  SELECT COUNT(*) INTO p_total FROM medicion WHERE sensor_id = p_sensor_id;
  SET p_acum = p_acum + p_total;
END$$
DELIMITER ;
SET @acum = 100;
CALL sp_acumula(1, @tot, @acum);
SELECT @tot AS total, @acum AS acumulado;
```

**Salida**

```
codigo	nombre	ordenes	horas
EQ-0002	Robot de soldadura	3	10.25

ordenes_del_equipo_2
3

ERROR 1414 (42000) at line 71: OUT or INOUT argument 2 for routine planta.sp_carga_equipo is not a variable or NEW pseudo-variable in BEFORE trigger

total	acumulado
4	104
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El procedimiento se crea con `DELIMITER` y con `DROP ... IF EXISTS` | 2 |
| Devuelve las cuatro columnas en pantalla y el conteo por el parámetro de salida | 3 |
| Reutiliza el `LEFT JOIN` y la agrupación sin reescribirlos | 1 |
| El 1414 provocado y pegado | 2 |
| El `INOUT` entra en 100 y sale en 104 | 2 |

**Error que más se ve**

Omitir el `DROP PROCEDURE IF EXISTS`; se delata en la segunda corrida del guion con `ERROR 1305 (42000) PROCEDURE ya existe`, que es exactamente cuando el alumno está depurando.

### 13.3 · Integrar

**Solución**

```sql
USE planta;
DROP PROCEDURE IF EXISTS sp_dos_pasos;
DELIMITER $$
CREATE PROCEDURE sp_dos_pasos()
BEGIN
  INSERT INTO medicion VALUES (101, 6, '2026-03-03 06:00:00', 8.90);
  INSERT INTO medicion VALUES (102, 99,'2026-03-03 07:00:00', 9.10);
END$$
DELIMITER ;
SELECT COUNT(*) AS antes FROM medicion;
CALL sp_dos_pasos();
SELECT COUNT(*) AS despues FROM medicion;
SELECT medicion_id, sensor_id, valor FROM medicion WHERE medicion_id = 101;
DELETE FROM medicion WHERE medicion_id = 101;

DROP PROCEDURE IF EXISTS sp_dos_pasos_seguro;
DELIMITER $$
CREATE PROCEDURE sp_dos_pasos_seguro(OUT p_resultado VARCHAR(600))
BEGIN
  DECLARE v_sqlstate CHAR(5);
  DECLARE v_errno    INT;
  DECLARE v_texto    VARCHAR(400);
  DECLARE integridad_rota CONDITION FOR SQLSTATE '23000';
  DECLARE EXIT HANDLER FOR integridad_rota
  BEGIN
    GET DIAGNOSTICS CONDITION 1
      v_sqlstate = RETURNED_SQLSTATE,
      v_errno    = MYSQL_ERRNO,
      v_texto    = MESSAGE_TEXT;
    ROLLBACK;                                  -- no viene incluido en el handler
    SET p_resultado = CONCAT('rechazado [', v_sqlstate, '/', v_errno, '] ', v_texto);
  END;
  START TRANSACTION;
  INSERT INTO medicion VALUES (101, 6, '2026-03-03 06:00:00', 8.90);
  INSERT INTO medicion VALUES (102, 99,'2026-03-03 07:00:00', 9.10);
  COMMIT;
  SET p_resultado = 'aceptado';
END$$
DELIMITER ;
SELECT COUNT(*) AS antes FROM medicion;
CALL sp_dos_pasos_seguro(@r);
SELECT @r AS resultado;
SELECT COUNT(*) AS despues FROM medicion;

DROP PROCEDURE IF EXISTS sp_dos_pasos_estricto;
DELIMITER $$
CREATE PROCEDURE sp_dos_pasos_estricto()
BEGIN
  DECLARE EXIT HANDLER FOR SQLSTATE '23000'
  BEGIN
    ROLLBACK;
    RESIGNAL SET MYSQL_ERRNO = 3101,
      MESSAGE_TEXT = 'El sensor no existe en el catalogo de la planta';
  END;
  START TRANSACTION;
  INSERT INTO medicion VALUES (101, 6, '2026-03-03 06:00:00', 8.90);
  INSERT INTO medicion VALUES (102, 99,'2026-03-03 07:00:00', 9.10);
  COMMIT;
END$$
DELIMITER ;
CALL sp_dos_pasos_estricto();
SELECT COUNT(*) AS al_final FROM medicion;
```

**Salida**

```
antes
20
ERROR 1452 (23000) at line 96: Cannot add or update a child row: a foreign key constraint fails (`planta`.`medicion`, CONSTRAINT `medicion_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))
despues
21
medicion_id	sensor_id	valor
101	6	8.90

antes
20
resultado
rechazado [23000/1452] Cannot add or update a child row: a foreign key constraint fails (`planta`.`medicion`, CONSTRAINT `medicion_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`sensor_id`))
despues
20

ERROR 3101 (23000): El sensor no existe en el catalogo de la planta
al_final
20
```

El error llegó tarde porque el servidor revisa la llave foránea al ejecutar la segunda sentencia, no al crear el procedimiento. Para entonces la primera fila ya estaba escrita, y sin transacción abierta ya se había confirmado sola.

El `SQLSTATE 23000` no quiere decir duplicado. Lo producen el duplicado (1062), la llave foránea rota (1452) y el `NOT NULL` violado (1048). El handler de arriba atrapa las tres, aunque su nombre solo prometa una.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La versión sin handler deja la primera fila y se demuestra con los conteos | 2 |
| El handler atrapa el error y el procedimiento termina sin reventar | 3 |
| `GET DIAGNOSTICS` recupera las tres piezas y el `ROLLBACK` está escrito a mano | 2 |
| Los conteos antes y después coinciden en 20 | 1 |
| El `RESIGNAL` sale con 3101 y mensaje legible | 1 |
| Se nombran las tres situaciones del 23000 | 1 |

**Error que más se ve**

Suponer que el `EXIT HANDLER` deshace por su cuenta; se delata porque el conteo de después queda en 21, ya que el handler detiene el bloque pero el `ROLLBACK` hay que escribirlo en la línea de abajo.

---

## Semana 14 · Triggers y eventos

### 14.1 · Reconocer

**Solución**

```sql
-- Momento          OLD          NEW
-- BEFORE INSERT    no existe    se lee y se escribe
-- AFTER  INSERT    no existe    se lee
-- BEFORE UPDATE    se lee       se lee y se escribe
-- AFTER  UPDATE    se lee       se lee
-- BEFORE DELETE    se lee       no existe
-- AFTER  DELETE    se lee       no existe

-- 1. OLD en un trigger de INSERT: ERROR 1363 (HY000) There is no OLD row in
--    on INSERT trigger. Aparece al CREARLO, no al dispararlo.
-- 2. Con 742.00 el trigger levanta 1644 y la fila no entra.
--    Con el valor vacio, NEW.valor < 0 no contesta falso: contesta desconocido,
--    y desconocido no es verdadero, asi que el IF no entra y la fila pasa.
--    La guarda:  IF NEW.valor IS NOT NULL AND (NEW.valor < 0 OR NEW.valor > 500)
-- 3. El trigger levanta 1644 con el mensaje que tu escribiste.
--    El CHECK levanta 3819 con el nombre de la restriccion y nada mas.
```

**Salida**

```
ERROR 1363 (HY000) at line 33: There is no OLD row in on INSERT trigger

ERROR 1644 (45000) at line 50: Valor fuera de la escala del sensor

medicion_id	valor
5	NULL

ERROR 3819 (HY000) at line 89: Check constraint 'ck_sensor_rango' is violated.
ERROR 1644 (45000) at line 90: Valor fuera de la escala del sensor
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La tabla de los seis momentos completa | 3 |
| El 1363 y el momento en que aparece, al crear el trigger | 2 |
| Los dos casos de la validación sin guarda, y la guarda escrita | 3 |
| Los dos números, 1644 y 3819, y qué alcanza a leer el usuario en cada uno | 2 |

**Error que más se ve**

Decir que el 1363 sale al insertar; se delata porque el trigger ni siquiera llega a existir, así que no hay nada que disparar.

### 14.2 · Aplicar

**Solución**

```sql
USE auto;
DELIMITER $$
CREATE TRIGGER trg_medicion_before_insert_valida
BEFORE INSERT ON medicion FOR EACH ROW
BEGIN
  IF NEW.valor IS NOT NULL AND (NEW.valor < 0 OR NEW.valor > 500) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Valor fuera de la escala del sensor';
  END IF;
END$$

CREATE TRIGGER trg_medicion_after_update_bitacora
AFTER UPDATE ON medicion FOR EACH ROW
BEGIN
  INSERT INTO medicion_bitacora
    (medicion_id, valor_antes, valor_nuevo, accion, cambiado_en)
  VALUES (OLD.medicion_id, OLD.valor, NEW.valor, 'UPDATE', NOW());
END$$
DELIMITER ;

INSERT INTO medicion VALUES (4,1,'2026-03-02 08:00:00',742.00);
INSERT INTO medicion VALUES (5,1,'2026-03-02 09:00:00',NULL);
SELECT medicion_id, valor FROM medicion WHERE medicion_id = 5;

UPDATE medicion SET valor = 68.00 WHERE medicion_id = 1;
SELECT medicion_id, valor_antes, valor_nuevo, accion FROM medicion_bitacora;
```

**Salida**

```
ERROR 1644 (45000) at line 50: Valor fuera de la escala del sensor

medicion_id	valor
5	NULL

medicion_id	valor_antes	valor_nuevo	accion
1	71.50	68.00	UPDATE
```

El nombre `trg_medicion_before_insert_valida` dice la tabla, el momento, el evento y el propósito, así que un `SHOW TRIGGERS` se lee sin abrir el cuerpo.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El trigger de validación rechaza 742.00 con el 1644 | 3 |
| La guarda del vacío está puesta y la lectura vacía entra | 3 |
| La bitácora deja `OLD` y `NEW` en el mismo renglón | 3 |
| Los nombres siguen la convención de tabla, momento, evento y propósito | 1 |

**Error que más se ve**

Escribir el trigger de bitácora como `BEFORE UPDATE` y leer `NEW` esperando el valor confirmado; se delata cuando otro trigger del mismo momento cambia `NEW` después y la bitácora registra un valor que nunca se guardó.

### 14.3 · Integrar

**Solución**

```sql
USE auto;
-- El trigger que deberia ver la desaparicion
DELIMITER $$
CREATE TRIGGER trg_medicion_before_delete_bitacora
BEFORE DELETE ON medicion FOR EACH ROW
BEGIN
  INSERT INTO medicion_bitacora
    (medicion_id, valor_antes, valor_nuevo, accion, cambiado_en)
  VALUES (OLD.medicion_id, OLD.valor, NULL, 'DELETE', NOW());
END$$
DELIMITER ;

SELECT COUNT(*) AS mediciones_del_sensor_3 FROM medicion WHERE sensor_id = 3;
SELECT COUNT(*) AS bitacora_antes FROM medicion_bitacora;
DELETE FROM sensor WHERE sensor_id = 3;          -- la FK es ON DELETE CASCADE
SELECT COUNT(*) AS mediciones_del_sensor_3 FROM medicion WHERE sensor_id = 3;
SELECT COUNT(*) AS bitacora_despues FROM medicion_bitacora;

SELECT COUNT(*) AS mediciones_antes FROM medicion;
TRUNCATE TABLE medicion;
SELECT COUNT(*) AS mediciones_despues FROM medicion;
SELECT COUNT(*) AS bitacora_al_final  FROM medicion_bitacora;

-- Los eventos
SHOW VARIABLES LIKE 'event_scheduler';
CREATE EVENT ev_cierre_turno
ON SCHEDULE AT '2026-03-20 08:00:00'
DO DELETE FROM medicion_bitacora WHERE accion = 'DELETE';
SHOW WARNINGS;
SELECT COUNT(*) AS eventos_en_el_catalogo FROM information_schema.EVENTS
 WHERE EVENT_SCHEMA = 'auto';

CREATE EVENT ev_purga_bitacora
ON SCHEDULE EVERY 1 DAY
DO DELETE FROM medicion_bitacora WHERE cambiado_en < NOW() - INTERVAL 30 DAY;
SELECT EVENT_NAME, EVENT_TYPE, INTERVAL_VALUE, INTERVAL_FIELD, STATUS
  FROM information_schema.EVENTS WHERE EVENT_SCHEMA = 'auto';
```

**Salida**

```
mediciones_del_sensor_3
1
bitacora_antes
1
mediciones_del_sensor_3
0
bitacora_despues
1

mediciones_antes
3
mediciones_despues
0
bitacora_al_final
1

Variable_name	Value
event_scheduler	ON

Level	Code	Message
Note	1588	Event execution time is in the past and ON COMPLETION NOT PRESERVE is set. The event was dropped immediately after creation.

eventos_en_el_catalogo
0

EVENT_NAME	EVENT_TYPE	INTERVAL_VALUE	INTERVAL_FIELD	STATUS
ev_purga_bitacora	RECURRING	1	DAY	ENABLED
```

Un trigger ve las sentencias que alguien escribe contra su tabla. No ve el borrado en cascada, que lo ejecuta el motor de llaves foráneas por dentro, y no ve el `TRUNCATE`, que en realidad tira la tabla y la vuelve a crear vacía. Tres mediciones desaparecieron y la bitácora se quedó en un renglón, el del `UPDATE` de 14.2.

El mecanismo que sí registra las dos desapariciones es no delegar el borrado al motor: quitar el `ON DELETE CASCADE` y borrar las hijas con un `DELETE` explícito, en un procedimiento o en un trigger sobre el padre. El `TRUNCATE` se cierra por permisos, negando `DROP` sobre esa tabla.

El evento con fecha pasada se creó sin error y no está en el catálogo. El `CREATE` tuvo éxito, `SHOW WARNINGS` trae la nota 1588, y `information_schema.EVENTS` viene vacío.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro conteos de la cascada, con la bitácora que no crece | 3 |
| Los tres conteos del `TRUNCATE`, con el mismo resultado | 2 |
| Se explica qué ve y qué no ve un trigger, y se propone el mecanismo que sí | 2 |
| El evento con fecha pasada, con la nota 1588 y el catálogo vacío | 2 |
| El evento recurrente aparece con su tipo, intervalo y estado | 1 |

**Error que más se ve**

Reportar que «la bitácora sí funciona» porque el renglón del `UPDATE` sigue ahí; se delata al comparar los conteos antes y después del borrado, que es el número que el ejercicio pide y no el contenido de la tabla.

---

## Semana 15 · Índices y desempeño

### 15.1 · Reconocer

**Solución**

```sql
-- WHERE equipo_id = 42
--   type=ref  key=idx_eq_fecha  key_len=4  rows=4  Extra=Using index
-- WHERE equipo_id = 42 AND tomada_en = '2026-01-15'
--   type=ref  key=idx_eq_fecha  key_len=7  rows=1  Extra=Using index
-- WHERE tomada_en = '2026-01-15'
--   type=index  key=idx_eq_fecha  key_len=7  rows=199963

-- La tercera: el indice aparece en key y el type es index, no ref. Eso no es
-- una busqueda, es recorrer el indice completo de punta a punta. La regla del
-- prefijo izquierdo dice que un indice compuesto sirve para la primera columna,
-- o para la primera mas la segunda, pero no para la segunda sola. Lo unico que
-- gano es que recorre el indice en lugar de la tabla, que es mas angosto.

-- Con (turno, valor) y un filtro solo por valor, con turno de cuatro valores
-- distintos, el servidor hace un salto de grupo: recorre el indice una vez por
-- cada valor de turno. Se llama skip scan y no existe en MySQL 5.7.
```

**Salida**

```
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	medicion_big	NULL	ref	idx_eq_fecha	idx_eq_fecha	4	const	4	100.00	Using index

id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	medicion_big	NULL	ref	idx_eq_fecha	idx_eq_fecha	7	const,const	1	100.00	Using index

id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	medicion_big	NULL	index	idx_eq_fecha	idx_eq_fecha	7	NULL	199963	10.00	Using where; Using index
```

```
EXPLAIN
-> Filter: (medicion_big.valor = 9.50)  (cost=5148 rows=19996)
    -> Covering index skip scan on medicion_big using idx_turno_valor over valor = 9.50  (cost=5148 rows=19996)
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres `type`: ref, ref, index | 3 |
| Los tres `rows`: 4, 1 y cerca de 200 000 | 2 |
| Se explica la tercera con la regla del prefijo izquierdo | 3 |
| Se nombra el salto de grupo y se dice que no está en 5.7 | 2 |

**Error que más se ve**

Concluir que la tercera consulta usa el índice porque `key` lo nombra; se delata con `rows`, que se acerca al total de la tabla, y con `type=index`, que es un recorrido completo y no una búsqueda.

### 15.2 · Aplicar

**Solución**

```sql
USE desempeno;
-- Estado de partida: sin indices secundarios en ninguna de las dos tablas
DROP INDEX idx_eq_fecha    ON medicion_big;
DROP INDEX idx_turno_valor ON medicion_big;
ANALYZE TABLE medicion_big, equipo_big;

-- Calentamiento, para no medir el primer acceso a disco
SELECT COUNT(*) INTO @n FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id WHERE e.codigo = 'EQ-000042';

EXPLAIN FORMAT=TRADITIONAL
SELECT m.medicion_id, e.codigo FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id WHERE e.codigo = 'EQ-000042';
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id WHERE e.codigo = 'EQ-000042';
SELECT @n AS filas, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_sin_indice;

CREATE INDEX idx_mb_equipo ON medicion_big (equipo_id);
CREATE INDEX idx_eb_codigo ON equipo_big   (codigo);
ANALYZE TABLE medicion_big, equipo_big;
SELECT COUNT(*) INTO @n FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id WHERE e.codigo = 'EQ-000042';

EXPLAIN FORMAT=TRADITIONAL
SELECT m.medicion_id, e.codigo FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id WHERE e.codigo = 'EQ-000042';
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id WHERE e.codigo = 'EQ-000042';
SELECT @n AS filas, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_con_indice;
```

**Salida**

```
id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	m	NULL	ALL	NULL	NULL	NULL	NULL	199963	100.00	NULL
1	SIMPLE	e	NULL	eq_ref	PRIMARY	PRIMARY	4	desempeno.m.equipo_id	1	10.00	Using where

filas	ms_sin_indice
4	144.7550

id	select_type	table	partitions	type	possible_keys	key	key_len	ref	rows	filtered	Extra
1	SIMPLE	e	NULL	ref	PRIMARY,idx_eb_codigo	idx_eb_codigo	36	const	1	100.00	Using where; Using index
1	SIMPLE	m	NULL	ref	idx_mb_equipo	idx_mb_equipo	4	desempeno.e.equipo_id	3	100.00	Using index

filas	ms_con_indice
4	0.1350
```

Sin índices el servidor recorre las 199 963 filas de `medicion_big` y para cada una va a buscar su equipo, para acabar devolviendo 4. Con los dos índices el orden se invierte: primero encuentra el equipo por su código, y de ahí baja a sus 3 mediciones estimadas. De 199 963 filas examinadas a 4, y de 144.755 ms a 0.135 ms.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos planes pegados, antes y después | 3 |
| Las filas examinadas en cada caso, con el `type` que las explica | 3 |
| Los dos tiempos, medidos después del calentamiento | 3 |
| El `CREATE INDEX` que va en medio queda a la vista | 1 |

**Error que más se ve**

Medir el primer tiro contra disco frío y reportar esa cifra como el «antes»; se delata porque la mejora sale exagerada y no se reproduce al volver a correr las dos mediciones.

### 15.3 · Integrar

**Solución**

```sql
USE desempeno;
CREATE INDEX idx_titulo ON mensaje (titulo(60));

EXPLAIN FORMAT=TRADITIONAL
SELECT mensaje_id FROM mensaje WHERE titulo LIKE 'Paro por vibracion%';
EXPLAIN FORMAT=TRADITIONAL
SELECT mensaje_id FROM mensaje WHERE titulo LIKE '%vibracion%';
EXPLAIN FORMAT=TRADITIONAL
SELECT mensaje_id FROM mensaje WHERE titulo REGEXP '^Paro por vibracion';

SELECT mensaje_id FROM mensaje WHERE MATCH(cuerpo) AGAINST ('vibracion');
ALTER TABLE mensaje ADD FULLTEXT (mensaje_id);

SET @t0 = NOW(6);
ALTER TABLE mensaje ADD FULLTEXT ft_cuerpo (cuerpo);
SELECT TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_de_construccion;
SHOW WARNINGS;

SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM mensaje WHERE MATCH(cuerpo) AGAINST ('vibracion');
SELECT @n AS filas, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms;
SET @t0 = NOW(6);
SELECT COUNT(*) INTO @n FROM mensaje WHERE cuerpo LIKE '%vibracion%';
SELECT @n AS filas, TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms;

-- El otro lado de la apuesta
CREATE TABLE carga_sin (
  medicion_id INT PRIMARY KEY, equipo_id INT, tomada_en DATE,
  turno VARCHAR(12), valor DECIMAL(7,2));
CREATE TABLE carga_con (
  medicion_id INT PRIMARY KEY, equipo_id INT, tomada_en DATE,
  turno VARCHAR(12), valor DECIMAL(7,2),
  INDEX i1 (equipo_id), INDEX i2 (tomada_en), INDEX i3 (turno),
  INDEX i4 (valor), INDEX i5 (equipo_id, tomada_en), INDEX i6 (turno, valor),
  INDEX i7 (tomada_en, valor), INDEX i8 (equipo_id, valor));
SET @t0 = NOW(6);
INSERT INTO carga_sin SELECT * FROM medicion_big;
SELECT TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_sin_indices;
SET @t0 = NOW(6);
INSERT INTO carga_con SELECT * FROM medicion_big;
SELECT TIMESTAMPDIFF(MICROSECOND,@t0,NOW(6))/1000 AS ms_con_ocho_indices;
ANALYZE TABLE carga_sin, carga_con;
SELECT TABLE_NAME, DATA_LENGTH, INDEX_LENGTH FROM information_schema.TABLES
 WHERE TABLE_SCHEMA='desempeno' AND TABLE_NAME LIKE 'carga_%';
```

**Salida**

```
LIKE anclado al inicio
1	SIMPLE	mensaje	NULL	range	idx_titulo	idx_titulo	242	NULL	14560	100.00	Using where; Using index
filas 7500   ms 6.6330

LIKE con comodin al inicio
1	SIMPLE	mensaje	NULL	ALL	NULL	NULL	NULL	NULL	59855	11.11	Using where
filas 7500   ms 8.6120

REGEXP anclado
1	SIMPLE	mensaje	NULL	ALL	NULL	NULL	NULL	NULL	59855	100.00	Using where

ERROR 1191 (HY000) at line 62: Can't find FULLTEXT index matching the column list
ERROR 1283 (HY000) at line 64: Column 'mensaje_id' cannot be part of FULLTEXT index

ms_de_construccion
6923.8340
Level	Code	Message
Warning	124	InnoDB rebuilding table to add column FTS_DOC_ID

filas	ms
7500	3.0510
filas	ms
7500	49.9370

token_minimo
3
palabras_vacias
36

ms_sin_indices
695.5480
ms_con_ocho_indices
2654.6830

TABLE_NAME	DATA_LENGTH	INDEX_LENGTH
carga_con	9977856	49414144
carga_sin	9977856	0
```

Los tres veredictos. El `LIKE` anclado al inicio se sostiene: `type=range` y 14 560 filas examinadas contra 59 855. El `LIKE` con comodín al inicio se cae: `type=ALL`, la tabla entera. El `REGEXP` anclado también se cae, y ahí el consejo heredado estaba exactamente al revés: recomendaba `REGEXP` en lugar de `LIKE`, y ni con ancla usa el índice.

El texto completo cuesta 6 923 ms de construcción, reescribe la tabla para agregarle una columna escondida `FTS_DOC_ID`, y a cambio contesta la misma pregunta en 3.05 ms contra 49.94 ms del `LIKE`. Son 16 veces, sobre la misma columna y las mismas 60 000 filas.

El otro lado de la apuesta: ocho índices de más cuestan 3.8 veces la carga (695.548 ms contra 2 654.683 ms) y pesan 4.95 veces lo que pesan los datos (49 414 144 contra 9 977 856). Un índice que ninguna consulta usa es puro costo.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres planes del `LIKE` y el `REGEXP`, con su `type` y sus filas | 3 |
| Un veredicto por rama, cada uno con su evidencia | 2 |
| Los dos errores del texto completo, 1191 y 1283 | 1 |
| El costo de construcción y la comparación de tiempos contra `LIKE` | 2 |
| Los dos tiempos de carga y las dos longitudes, con su cociente | 2 |

**Error que más se ve**

Reportar que el `LIKE '%vibracion%'` «no está tan mal» porque tardó 8.6 ms; se delata con las filas examinadas, 59 855 contra 14 560, que es el número que escala cuando la tabla crece y el tiempo no.

---

## Semana 16 · Concurrencia y bloqueos · Proyecto

### 16.1 · Reconocer

**Solución**

```sql
-- A leyo 25.  B leyo 25.  La refaccion queda en 20.
-- Salieron 10 piezas del almacen y el sistema dice que salieron 5.
-- Nadie escribio mal. El hueco esta entre leer y escribir: B leyo 182 ms
-- despues que A, cuando A todavia no habia escrito nada.

-- Con FOR UPDATE:  A lee 25 y escribe 20.  B espera el COMMIT de A, lee 20
-- y escribe 15.  Final 15.
-- Sin leer:  UPDATE ... SET existencia = existencia - 5.  Final 15.
-- La diferencia: FOR UPDATE conserva la lectura, asi que la aplicacion puede
-- decidir con el valor correcto antes de escribir. La segunda no lee nada,
-- asi que resuelve el conteo y no sirve si hay que revisar antes de restar.
```

**Salida**

```
sesion	existencia	cuando
A_leyo	25	2026-08-17 21:24:38.205676
sesion	existencia	cuando
B_leyo	25	2026-08-17 21:24:38.387740

sesion	dejo	cuando
A_escribio	20	2026-08-17 21:24:39.216723
sesion	dejo	cuando
B_escribio	20	2026-08-17 21:24:39.396654

refaccion_id	resultado_final
3	20
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres números: 25, 25 y 20 | 3 |
| Se dice que salieron 10 piezas y el sistema registra 5 | 2 |
| Las dos reparaciones llegan a 15 | 2 |
| Se ubica el hueco entre la lectura y la escritura | 2 |
| Se explica en qué se diferencian las dos reparaciones | 1 |

**Error que más se ve**

Predecir 15 porque «las dos restaron cinco»; se delata con las marcas de tiempo, que muestran que las dos leyeron el mismo 25 antes de que ninguna escribiera.

### 16.2 · Aplicar

**Solución**

```sql
-- Las dos sesiones corren el mismo guion, con 150 ms de diferencia.
-- Sesion A y sesion B, sin candado:
START TRANSACTION;
SELECT existencia INTO @c FROM refaccion WHERE refaccion_id = 3;
SELECT 'A_leyo' AS sesion, @c AS existencia, NOW(6) AS cuando;
SELECT SLEEP(1) INTO @z;
UPDATE refaccion SET existencia = @c - 5 WHERE refaccion_id = 3;
COMMIT;

-- Reparacion 1, la misma lectura con candado:
SELECT existencia INTO @c FROM refaccion WHERE refaccion_id = 3 FOR UPDATE;

-- Reparacion 2, que lo reste el servidor:
UPDATE refaccion SET existencia = existencia - 5 WHERE refaccion_id = 3;

-- El 1205. Sesion A toma la fila y duerme 6 s; sesion B, con timeout de 3 s:
SET SESSION innodb_lock_wait_timeout = 3;
START TRANSACTION;
UPDATE refaccion SET existencia = 7 WHERE refaccion_id = 2;   -- trabajo previo
SELECT existencia FROM refaccion WHERE refaccion_id = 3;      -- lectura simple
SELECT existencia FROM refaccion WHERE refaccion_id = 3 FOR UPDATE;
COMMIT;

-- El 1213. A toma la 1 y pide la 3; B toma la 3 y pide la 1, a la vez.
```

**Salida**

```
con FOR UPDATE
A_leyo	25	2026-03-... 21:25:06.998582
A_escribio	20	2026-03-... 21:25:08.027399
B_leyo	20	2026-03-... 21:25:08.027539
B_escribio	15	2026-03-... 21:25:09.047092
resultado_con_for_update	15

sin leer primero
resultado_sin_leer	15
```

```
--- el 1205 ---
nota	cuando
A tomo la fila 3	2026-08-17 21:25:24.852434
nota	cuando
B pide la fila 3	2026-08-17 21:25:25.178225
existencia
25
ERROR 1205 (HY000) at line 6: Lock wait timeout exceeded; try restarting transaction
nota	cuando
B llego al final	2026-08-17 21:25:28.208733

--- el 1213 ---
nota	cuando
A tomo la 1	2026-08-17 21:25:42.700644
nota	cuando
B tomo la 3	2026-08-17 21:25:42.713913
ERROR 1213 (40001) at line 6: Deadlock found when trying to get lock; try restarting transaction
refaccion_id	existencia
1	11
3	24
```

Lo que sobrevivió en cada caso. Tras el 1205, la sesión B siguió adentro de su transacción y su `COMMIT` se llevó el trabajo a medias: la refacción 2 quedó en 7, escrita antes del error, mientras que la 3 se quedó en 25 porque esa sentencia nunca corrió. Tras el 1213, la sesión B perdió la transacción completa: su descuento a la refacción 3 se deshizo, y los dos descuentos que quedaron (11 y 24) son los de la sesión A.

La lectura simple no esperó. Devolvió 25 al instante, mientras A tenía la fila, porque una lectura sin candado nunca espera. El `FOR UPDATE` esperó 3.03 s y expiró.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres corridas con dos sesiones de verdad y sus marcas de tiempo | 3 |
| El 1205 con el tiempo que tardó en llegar | 2 |
| El 1213 provocado | 2 |
| Se reporta qué sobrevivió en cada caso, y no es lo mismo | 3 |

**Error que más se ve**

Reintentar los dos errores igual, con un `COMMIT` después; se delata en el caso del 1205, donde el `COMMIT` confirma trabajo a medias que nadie revisó.

### 16.3 · Integrar

**Solución**

```sql
USE conc;
DELIMITER $$
CREATE PROCEDURE sp_surtir(IN p_refaccion_id INT, IN p_cantidad INT,
                           OUT p_resultado VARCHAR(60))
BEGIN
  DECLARE v_hay INT;
  START TRANSACTION;
  SELECT existencia INTO v_hay FROM refaccion WHERE refaccion_id = p_refaccion_id;
  SELECT SLEEP(1) INTO @z;                    -- aqui cabe la otra sesion
  IF v_hay >= p_cantidad THEN
    UPDATE refaccion SET existencia = existencia - p_cantidad
     WHERE refaccion_id = p_refaccion_id;
    INSERT INTO salida (refaccion_id, cantidad) VALUES (p_refaccion_id, p_cantidad);
    SET p_resultado = CONCAT('surtido, vio ', v_hay);
  ELSE
    SET p_resultado = CONCAT('rechazado, vio ', v_hay);
  END IF;
  COMMIT;
END$$

CREATE PROCEDURE sp_surtir_seguro(IN p_refaccion_id INT, IN p_cantidad INT,
                                  OUT p_resultado VARCHAR(60))
BEGIN
  DECLARE v_hay INT;
  START TRANSACTION;
  SELECT existencia INTO v_hay FROM refaccion
   WHERE refaccion_id = p_refaccion_id FOR UPDATE;    -- la unica diferencia
  SELECT SLEEP(1) INTO @z;
  IF v_hay >= p_cantidad THEN
    UPDATE refaccion SET existencia = existencia - p_cantidad
     WHERE refaccion_id = p_refaccion_id;
    INSERT INTO salida (refaccion_id, cantidad) VALUES (p_refaccion_id, p_cantidad);
    SET p_resultado = CONCAT('surtido, vio ', v_hay);
  ELSE
    SET p_resultado = CONCAT('rechazado, vio ', v_hay);
  END IF;
  COMMIT;
END$$

CREATE PROCEDURE sp_ajustar(IN p_primera INT, IN p_segunda INT, OUT p_intentos INT)
BEGIN
  DECLARE v_falla INT DEFAULT 0;
  DECLARE CONTINUE HANDLER FOR SQLSTATE '40001'
  BEGIN
    ROLLBACK;
    SET v_falla = 1;
  END;
  SET p_intentos = 0;
  reintenta: LOOP
    SET v_falla = 0;
    SET p_intentos = p_intentos + 1;
    START TRANSACTION;
    UPDATE refaccion SET existencia = existencia - 1 WHERE refaccion_id = p_primera;
    SELECT SLEEP(1) INTO @z;
    UPDATE refaccion SET existencia = existencia - 1 WHERE refaccion_id = p_segunda;
    IF v_falla = 0 THEN
      COMMIT;
      LEAVE reintenta;
    END IF;
    IF p_intentos >= 5 THEN LEAVE reintenta; END IF;
  END LOOP;
END$$
DELIMITER ;
```

**Salida**

```
=== sin FOR UPDATE, las dos piden 20 de 25 ===
sesion	resultado
A	surtido, vio 25
sesion	resultado
B	surtido, vio 25
existencia
-15
salidas	piezas
2	40

=== con FOR UPDATE, desde el mismo estado ===
sesion	resultado
A	surtido, vio 25
sesion	resultado
B	rechazado, vio 5
existencia
5
salidas	piezas
1	20

=== el reintento, con los identificadores invertidos ===
sesion	intentos
A	1
sesion	intentos
B	2
refaccion_id	existencia
1	10
3	23
```

Sin el candado las dos sesiones vieron 25, las dos decidieron que alcanzaba y las dos surtieron. El almacén entregó 40 piezas de un inventario de 25 y la existencia quedó en menos quince, sin un solo error ni advertencia.

Con `FOR UPDATE` la sesión B esperó el `COMMIT` de A, leyó 5 y se rechazó sola. Una sola salida de 20 piezas y la existencia en 5.

El reintento recuperó el trabajo perdido: A cerró al primer intento y B necesitó dos, y las dos refacciones quedaron con sus dos descuentos aplicados, 12 a 10 y 25 a 23.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres números sin candado: 25 y 25, existencia negativa y 40 piezas | 3 |
| Los tres números con candado: 25 y 5, existencia 5 y 20 piezas | 3 |
| La diferencia entre los dos procedimientos es una sola cláusula | 1 |
| El reintento reporta intentos por sesión y las dos refacciones con sus dos descuentos | 3 |

**Error que más se ve**

Poner el `FOR UPDATE` con autocommit encendido, fuera de una transacción; se delata porque el candado se suelta al terminar la sentencia y el resultado vuelve a ser el de la versión sin candado.

---

## Semana 17 · Usuarios, respaldo y cierre · Examen final

### 17.1 · Reconocer

**Solución**

```sql
-- Leer clave y descripcion .......... pasa
-- Leer clave y existencia ........... rebota, ERROR 1143 (no 1142)
-- Actualizar existencia ............. pasa
-- Actualizar descripcion ............ rebota, ERROR 1143
-- El 1143 es el error de columna. El 1142 es el de tabla completa. La cuenta
-- si tiene permiso sobre la tabla refaccion, solo que sobre otras columnas.

-- Lo que NO va a estar en taller.sql con el comando por omision:
--   el procedimiento sp_prestamos_de   (hace falta --routines)
--   el evento ev_purga_bitacora        (hace falta --events)
-- Lo que si va: las tres tablas, sus datos, la vista y el trigger.
-- En el error estandar imprime tres advertencias: la de los GTID, la de que
-- para un respaldo completo hay que pasar --all-databases --triggers
-- --routines --events, y la de que para un respaldo consistente hay que pasar
-- --single-transaction o --lock-all-tables o --source-data.
-- La ultima linea de un archivo completo es «-- Dump completed on ...».
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro veredictos sobre el `SHOW GRANTS` | 3 |
| Se distingue el 1143 de columna del 1142 de tabla | 2 |
| Se nombran el procedimiento y el evento como lo que falta en el respaldo | 3 |
| Se dice que el trigger sí va, y cuál es la última línea de un archivo completo | 2 |

**Error que más se ve**

Suponer que el trigger tampoco va en el respaldo por omisión; se delata con un `grep -c TRIGGER` sobre el archivo, que devuelve 1.

### 17.2 · Aplicar

**Solución**

```sql
-- 1. El GRANT sin cuenta
GRANT SELECT, INSERT ON planta.* TO 'ing_capturista'@'localhost';
CREATE USER 'ing_analista'@'localhost' IDENTIFIED BY 'Planta2026!';
SHOW GRANTS FOR 'ing_analista'@'localhost';
GRANT SELECT ON planta.* TO 'ing_analista'@'localhost';
SHOW GRANTS FOR 'ing_analista'@'localhost';

-- 3. Permisos por columna
CREATE USER 'ing_tutor'@'localhost' IDENTIFIED BY 'Planta2026!';
GRANT SELECT (clave, descripcion) ON planta.refaccion TO 'ing_tutor'@'localhost';
GRANT UPDATE (existencia)         ON planta.refaccion TO 'ing_tutor'@'localhost';

-- 4. El rol
CREATE ROLE 'rol_lectura_planta';
GRANT SELECT ON planta.* TO 'rol_lectura_planta';
CREATE USER 'ing_reportes'@'%' IDENTIFIED BY 'Planta2026!';
GRANT 'rol_lectura_planta' TO 'ing_reportes'@'%';
SELECT @@activate_all_roles_on_login AS activa_al_entrar;
```

```bash
# El respaldo, tres archivos
mysqldump -u root -p --set-gtid-purged=OFF taller > taller_omision.sql
mysqldump -u root -p --routines --events --set-gtid-purged=OFF taller > taller_completo.sql
mysqldump -u root -p --no-data --set-gtid-purged=OFF taller > taller_esquema.sql
grep -c PROCEDURE taller_omision.sql taller_completo.sql
grep -c EVENT     taller_omision.sql taller_completo.sql
wc -c taller_omision.sql taller_completo.sql taller_esquema.sql
```

**Salida**

```
ERROR 1410 (42000) at line 7: You are not allowed to create a user with GRANT

Grants for ing_analista@localhost
GRANT USAGE ON *.* TO `ing_analista`@`localhost`

Grants for ing_analista@localhost
GRANT USAGE ON *.* TO `ing_analista`@`localhost`
GRANT SELECT ON `planta`.* TO `ing_analista`@`localhost`
```

```
--- conectado como ing_analista ---
puede_leer
8
ERROR 1142 (42000) at line 2: DELETE command denied to user 'ing_analista'@'localhost' for table 'refaccion'
ERROR 1142 (42000) at line 3: SELECT command denied to user 'ing_analista'@'localhost' for table 'user'

--- conectado como ing_tutor ---
clave	descripcion
RF-001	Filtro de aire 50% eficiencia
RF-002	Filtro de aceite 50 micras
ERROR 1143 (42000) at line 2: SELECT command denied to user 'ing_tutor'@'localhost' for column 'existencia' in table 'refaccion'
ERROR 1143 (42000) at line 4: UPDATE command denied to user 'ing_tutor'@'localhost' for column 'descripcion' in table 'refaccion'

--- conectado como ing_reportes ---
rol_activo
NONE
ERROR 1142 (42000) at line 2: SELECT command denied to user 'ing_reportes'@'localhost' for table 'equipo'
rol_activo
`rol_lectura_planta`@`%`
ahora_si
8
```

```
taller_omision.sql:0
taller_completo.sql:2
taller_omision.sql:0
taller_completo.sql:2
 6456 taller_omision.sql
 9097 taller_completo.sql
 5497 taller_esquema.sql
```

El rol se otorgó y no se activó. `@@activate_all_roles_on_login` vale 0, así que la cuenta entra con `CURRENT_ROLE()` en `NONE` y recibe el mismo 1142 que una cuenta sin permisos. Se arregla en la sesión con `SET ROLE 'rol_lectura_planta'`, y de forma permanente con `SET DEFAULT ROLE` o encendiendo la variable.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El 1410 y el orden que el servidor exige | 2 |
| Los dos `SHOW GRANTS` y los dos 1142 vistos desde la cuenta restringida | 3 |
| Los cuatro veredictos por columna verificados, con el 1143 | 2 |
| El rol sin activar, con `CURRENT_ROLE()` en `NONE` y su arreglo | 2 |
| Los tres tamaños y los conteos de `PROCEDURE` y `EVENT` | 1 |

**Error que más se ve**

Probar los permisos desde la sesión de root y darlos por buenos; se delata porque otorgar no produce salida, y lo único que se ve del otro lado es el error que recibe la cuenta restringida.

### 17.3 · Integrar

**Solución**

```bash
# 1. Restaurar y verificar
mysql -u root -p -e "CREATE DATABASE taller_restaurado;"
mysql -u root -p taller_restaurado < taller_completo.sql
echo "exit=$?"
```

```sql
SELECT (SELECT COUNT(*) FROM taller_restaurado.herramienta)       AS h,
       (SELECT COUNT(*) FROM taller_restaurado.prestamo)          AS p,
       (SELECT COUNT(*) FROM taller_restaurado.prestamo_bitacora) AS b;
SELECT ROUTINE_NAME FROM information_schema.ROUTINES WHERE ROUTINE_SCHEMA='taller_restaurado';
SELECT EVENT_NAME   FROM information_schema.EVENTS   WHERE EVENT_SCHEMA='taller_restaurado';
SELECT TRIGGER_NAME FROM information_schema.TRIGGERS WHERE TRIGGER_SCHEMA='taller_restaurado';

-- 2. Restaurar sobre una base viva
USE taller_restaurado;
INSERT INTO herramienta VALUES (9,'HT-09','Camara termografica');
DELETE FROM prestamo WHERE prestamo_id = 2;
CREATE TABLE bitacora_local (id INT PRIMARY KEY);
```

```bash
mysql -u root -p taller_restaurado < taller_completo.sql
# 3. El archivo que miente
mysqldump -u root -p --set-gtid-purged=OFF taller herramienta tabla_que_no_existe > roto.sql
echo "exit=$?"; wc -c roto.sql; tail -1 roto.sql
```

**Salida**

```
exit=0

h	p	b
3	2	2

ROUTINE_NAME
sp_prestamos_de
EVENT_NAME
ev_purga_bitacora
TRIGGER_NAME
trg_prestamo_after_insert_bitacora
```

```
--- antes de restaurar encima ---
herramientas	prestamos
4	1
--- despues ---
exit del restore=0
herramientas	prestamos
3	2

Tables_in_taller_restaurado
bitacora_local
herramienta
prestamo
prestamo_bitacora
v_prestamo_vigente
```

```
mysqldump: Couldn't find table: "tabla_que_no_existe"
exit=6
793 roto.sql
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
```

La restauración exitosa no imprimió una sola línea y salió con código 0. La única prueba de que funcionó es el conteo del otro lado.

Restaurar no te devuelve al día del respaldo, te sobrescribe el hoy. La herramienta nueva se fue, el préstamo borrado volvió, y `bitacora_local` sobrevivió intacta porque el archivo no la nombra en ninguna línea: el respaldo solo repone lo que conoce y no borra lo que ignora.

El archivo roto salió con código 6 y dejó 793 bytes de cabecera creíble. La señal es la última línea: no dice `-- Dump completed on ...`, dice un `SET` de la cabecera, así que el archivo se cortó antes de escribir un solo dato.

Los tres cierres.

`sql_mode`. El 1264 de un valor fuera de rango, el 1292 de una fecha mal escrita, el 1265 de un valor fuera del ENUM y el 1406 de un texto muy largo son errores porque `STRICT_TRANS_TABLES` está encendido. Con el modo apagado los cuatro `INSERT` pasan callados, truncando el dato, y ahí nace el «en mi máquina sí sirve».

`EXPLAIN`. En la semana 15 el consejo heredado recomendaba `REGEXP` en lugar de `LIKE` para buscar texto. El plan lo tumbó: el `LIKE` anclado dio `type=range` con 14 560 filas y el `REGEXP` anclado dio `type=ALL` con 59 855 y `possible_keys=NULL`. El consejo estaba exactamente al revés, y ninguna autoridad lo habría mostrado.

La contradicción. La semana 6 llama al índice un detalle agregado y la semana 15 lo midió: ocho índices de más pesaron 49 414 144 bytes contra 9 977 856 de datos, casi cinco veces, y multiplicaron por 3.8 el tiempo de carga. Un detalle no cambia el tamaño de una tabla por cinco. Se resuelve con la medición, no con la lámina.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La restauración se verifica contando del otro lado, con los tres objetos | 3 |
| El restore sobre base viva reporta las tres cosas y explica la que sobrevive | 2 |
| El archivo roto, con código 6, tamaño y última línea | 2 |
| Los tres párrafos de cierre, cada uno con una cifra o un error del semestre | 3 |

**Error que más se ve**

Dar por buena la restauración porque el cliente no imprimió errores; se delata porque una restauración fallida a la mitad también sale sin ruido, y la única prueba es el conteo posterior.
