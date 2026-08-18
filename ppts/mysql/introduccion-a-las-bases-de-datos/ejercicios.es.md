# Ejercicios · Introducción a las Bases de Datos · COM112

Cincuenta y un ejercicios, tres por sesión, para el grupo de Ingeniería que cursa las diecisiete semanas del temario. Cada semana abre con uno de lectura, donde se predice lo que va a contestar el servidor antes de correrlo; sigue con uno de escritura contra una especificación que trae sus cifras; y cierra con uno que amarra la sesión del día con las anteriores. La dificultad sube dos veces, dentro de la semana y a lo largo del semestre, así que el de reconocer de la semana 12 pide más trabajo que el de integrar de la semana 4. Se entrega un archivo `.sql` por ejercicio con la salida del servidor pegada tal como salió, sin recortar ni acomodar. Todo corre sobre el esquema del anexo, que es una planta de manufactura con sus líneas, sus equipos, sus sensores y su almacén de refacciones.

---

## Semana 01 · Por qué existe una base de datos

### 01.1 · Reconocer

El registrador de la línea de ensamble exporta sus lecturas a un archivo plano. Estos son cinco renglones de `mediciones.csv` de la mañana del 2 de marzo:

```
SN-101,2026-03-02 06:00,71.5,C
SN-101,2026-03-02 07:00,74.2,C
SN-101,2026-03-02 07:00,742,C
SN-101,2026-03-02 08:00,,c
SN-101,2026-03-02 09:00,78.9,C
```

Hay cinco fallas y ninguna produjo un mensaje. El tercer renglón repite la marca de tiempo del segundo. Ese mismo renglón trae 742 donde el sensor SN-101 mide de 0 a 120 grados. El cuarto viene sin valor y con la unidad en minúscula. La unidad se repite en los cinco renglones aunque pertenece al sensor y no a la lectura. Y la tarde anterior dos personas guardaron el archivo desde sus máquinas, así que la segunda en guardar se llevó el trabajo de la primera.

Escribe, para cada falla, cuál de las cinco presiones de la sesión es la que la resuelve. Después predice, sin correr nada, qué contestan los dos SELECT de esta corrida sobre la tabla `medicion` del anexo, que empieza con veinte renglones:

```sql
START TRANSACTION;
INSERT INTO medicion VALUES (21, 6, '2026-03-02 08:00:00', 9.40);
INSERT INTO medicion VALUES (22, 6, '2026-03-02 09:00:00', 9.65);
SELECT COUNT(*) AS mediciones_dentro FROM medicion;
ROLLBACK;
SELECT COUNT(*) AS mediciones_despues FROM medicion;
```

### 01.2 · Aplicar

Conéctate al servidor del curso y escribe `w01_servidor.sql`, que contesta cuatro cosas en este orden.

Primero la versión, el motor por omisión y el juego de caracteres del servidor, los tres en un solo renglón, con las columnas nombradas `version`, `motor` y `juego_caracteres`. Después el `sql_mode` completo, en su propia consulta. Al final una transacción que meta tres lecturas al sensor 3 con marcas de tiempo 10:00, 11:00 y 12:00 del 2 de marzo, cuente adentro de la transacción, deshaga y vuelva a contar. Las dos columnas de conteo se llaman `mediciones_dentro` y `mediciones_despues`.

Con las veinte lecturas del anexo, el primer conteo tiene que salir en 23 y el segundo en 20. Pega la salida literal debajo de cada sentencia.

### 01.3 · Integrar

Escribe la declaración que habría atajado el archivo plano de 01.1. La tabla se llama `medicion_plana` y tiene cinco columnas: un identificador entero que es la llave primaria, el sensor, la marca de tiempo, el valor con dos decimales y la unidad en cuatro caracteres. El sensor, la marca de tiempo y la unidad no aceptan vacío. El valor sí, porque un sensor desconectado es un caso real. Corre `SHOW CREATE TABLE medicion_plana` y pega lo que devolvió el servidor, incluido lo que escribió solo.

Después contesta con una corrida y no con una opinión. De las cinco fallas de 01.1, una sigue siendo posible con la tabla ya declarada. Di cuál. Luego demuestra con dos conteos alrededor de un ROLLBACK que este servidor sí sabe retirar una escritura, y explica en dos renglones por qué esa capacidad no resuelve la falla que quedó viva.

---

## Semana 02 · Tipos, elementos y clasificaciones

### 02.1 · Reconocer

El instructor entrega `taller.sql`, el guion que levanta el esquema del almacén de herramienta. Adentro hay tres `CREATE TABLE`, una vista, un trigger, un evento y ningún procedimiento. Las tres tablas son `herramienta`, con llave primaria y una columna `clave` declarada `NOT NULL UNIQUE`; `prestamo`, con llave primaria y una llave foránea a `herramienta`; y `prestamo_bitacora`, con llave primaria y nada más.

Antes de correr nada, predice los siete renglones que va a devolver el inventario de objetos del esquema `taller`: cuántas tablas, cuántas vistas, cuántos triggers, cuántos eventos, cuántas rutinas, cuántas restricciones y cuántos índices. Las restricciones se cuentan sobre `information_schema.TABLE_CONSTRAINTS` y los índices sobre `information_schema.STATISTICS`, contando nombres distintos por tabla.

Los dos renglones donde casi todo el grupo se equivoca son los dos últimos. Escribe al lado de cada uno de qué línea del guion salió cada restricción y cada índice, incluidos los que nadie declaró.

### 02.2 · Aplicar

Corre `taller.sql` y verifica tu predicción con la consulta al catálogo. Después crea la cuenta `ing_lector` en `localhost`, con contraseña, y haz dos cosas en este orden: pide sus privilegios antes de otorgarle nada, y pídelos otra vez después de darle `SELECT` sobre todo el esquema `planta`.

El punto del ejercicio son las dos salidas comparadas. Explica en un renglón qué es lo que ya tenía la cuenta recién creada, antes de que le concedieras nada, y por qué el servidor se lo escribió solo.

### 02.3 · Integrar

En el esquema `planta` está la tabla `lectura`, declarada con tres reglas que el servidor va a defender: el valor tiene que caer entre -50 y 500, el par sensor más marca de tiempo no se puede repetir, y el sensor tiene que existir en el catálogo. Ya trae un renglón, el del sensor 1 a las 06:00 con 71.50.

Escribe tres INSERT, uno por regla, cada uno diseñado para que reboten por una razón distinta. Pega los tres errores completos con su número y su SQLSTATE. Al final cuenta las filas de `lectura` y muestra que sigue habiendo una sola.

Después contesta por escrito: ninguno de los tres rechazos lo levantó un programa de aplicación. Nombra qué pieza los levantó y en qué se apoya cada uno para saber que el dato estaba mal.

---

## Semana 03 · El manejador y sus archivos

### 03.1 · Reconocer

Estas cuatro salidas vienen de la misma sesión contra el esquema `taller` y contestan la misma pregunta, «qué hay ahí», desde cuatro alturas distintas.

```
A)  prestamo_id  herramienta_id  salida
    1            1               2026-03-02 07:15:00

B)  @@innodb_page_size   16384
    @@innodb_buffer_pool_size   134217728

C)  TABLE_NAME          TABLE_TYPE   ENGINE
    herramienta         BASE TABLE   InnoDB
    v_prestamo_vigente  VIEW         NULL

D)  SPACE  NAME                     FILE_SIZE
    280    taller/herramienta       131072
```

Asigna cada salida al nivel de la arquitectura que le corresponde y escribe la sentencia que la produjo. Después contesta tres preguntas. ¿Cuál de las cuatro cambia si alguien agrega una columna a `herramienta`? ¿Cuál de las cuatro no menciona nunca a `v_prestamo_vigente`, y por qué? ¿Por qué la columna `ENGINE` de la salida C viene vacía en el segundo renglón?

### 03.2 · Aplicar

Sobre `taller`, escribe una consulta por nivel y pega las tres salidas en orden, de arriba hacia abajo. El nivel externo se pregunta a la vista. El nivel conceptual se pregunta al catálogo, y tiene que traer el nombre del objeto, su tipo y su motor. El nivel interno se pregunta a tres variables del servidor: el directorio de datos, el tamaño de página y el tamaño del pool.

Después baja un escalón más y lista los archivos del esquema en `information_schema.INNODB_TABLESPACES`. Explica en un renglón por qué el listado tiene tres entradas y el catálogo del nivel conceptual tenía cuatro.

### 03.3 · Integrar

Mide la brecha. Suma el tamaño en disco de todos los archivos del esquema `taller` y compáralo con el tamaño en bytes del guion `taller.sql`, que es el texto SQL que produjo todo eso. Reporta los dos números y su cociente.

Después abre el optimizador. Corre `EXPLAIN` sobre una consulta que busque los préstamos de la herramienta 3, primero sin pedir formato y luego con `FORMAT=TRADITIONAL`. Pega las dos salidas y consulta `@@explain_format` para explicar por qué la primera no se parece a las capturas de los tutoriales.

Al final provoca un error de sintaxis a propósito, escribiendo `SELEC` en lugar de `SELECT`. De los cinco componentes de la sesión, di cuál levantó ese error y por qué los otros cuatro no llegaron a enterarse de tu consulta.

---

## Semana 04 · Modelo entidad-relación

### 04.1 · Reconocer

Cinco frases del área de mantenimiento, cada una tomada de una junta real:

1. Cada equipo pertenece a una línea de producción, y una línea tiene varios equipos.
2. Una orden de trabajo consume varias refacciones, y una refacción se consume en varias órdenes.
3. Un equipo tiene a lo más un certificado de calibración vigente, y cada certificado es de un solo equipo. Hay equipos sin certificado.
4. Una bomba puede estar montada dentro de otro equipo, y ese equipo dentro de otro.
5. Cada línea tiene un equipo cabecera, que además pertenece a esa misma línea.

Para cada frase escribe tres cosas: la cardinalidad, el verbo con el que nombrarías la relación, y la forma física en que se convierte cuando deja de ser dibujo. Las formas posibles son llave foránea sola, llave foránea más UNIQUE, llave foránea que apunta a la propia tabla, y tabla nueva con la llave primaria del par.

La cinco es la que separa al grupo. Di qué tiene de distinto respecto a la uno.

### 04.2 · Aplicar

En un esquema nuevo llamado `modelo`, construye dos de las cinco relaciones de 04.1.

Primero la recursiva. Una tabla `equipo` con identificador, nombre y una columna que apunta a la propia tabla, con su llave foránea declarada. Carga tres renglones que armen una cadena: la cabina de pintura, la bomba de recirculación montada en ella, y el impulsor montado en la bomba. Muestra los tres y señala cuál de las tres columnas de padre viene vacía y por qué tenía que aceptar vacío.

Después la de muchos a muchos. Tablas `orden`, `refaccion` y la tercera que sale de la relación, cuya llave primaria es el par. Corre `SHOW CREATE TABLE` sobre esa tercera tabla y marca en la salida las tres cosas que el servidor escribió sin que nadie las pidiera. Al final inserta dos veces el mismo par y pega el error.

### 04.3 · Integrar

La relación doble de la frase 5 no se puede construir de un golpe. Demuéstralo. En un esquema `modelo2` recién creado, intenta primero el `CREATE TABLE linea` que el dibujo pide de forma literal, con `equipo_cabecera_id INT NOT NULL` y su llave foránea a `equipo`. Pega el error.

Después escribe la versión que sí corre, en tres sentencias, y explica en el comentario de cada una qué concesión hiciste respecto al dibujo. Carga la línea Pintura con su cabina de pintura y deja el cabecera apuntando a ella.

Al final da de alta una segunda línea, Empaque, sin un solo equipo. Cuenta sus equipos y comprueba que el servidor no protesta. Escribe en dos renglones qué promesa del diagrama acaba de quedar sin quien la exija.

---

## Semana 05 · Normalización

### 05.1 · Reconocer

El área de confiabilidad guarda sus lecturas en una sola tabla ancha:

```sql
CREATE TABLE lectura_ancha (
  sensor_id     INT,
  tomada_en     DATETIME,
  sensor_unidad VARCHAR(10),
  equipo_id     INT,
  equipo_nombre VARCHAR(60),
  equipo_area   VARCHAR(30),
  valor         DECIMAL(7,2),
  PRIMARY KEY (sensor_id, tomada_en)
);
```

Escribe todas las dependencias funcionales de la tabla en la forma `A → B`, antes de nombrar una sola forma normal. Después marca cuáles de esas flechas no salen de la llave completa y di qué forma normal rompe cada grupo.

Predice también dos corridas. La primera mete tres lecturas del sensor 103 donde la tercera trae la unidad escrita `mm/seg` en lugar de `mm/s`; di cuántas entran y qué error sale. La segunda crea una tabla de dos columnas sin llave primaria y luego repite el mismo `CREATE TABLE` con `sql_require_primary_key` encendido; di qué pasa en cada caso y qué te dice eso sobre si la unicidad forma parte de la primera forma normal.

### 05.2 · Aplicar

Corre los tres ataques de la sesión contra la tabla ancha y contra una tabla `orden_ancha` que guarda las refacciones de cada orden en una sola celda, con valores como `'RF-001, RF-003'`.

El primer ataque es el de la lista en la celda: busca las órdenes que consumieron `RF-003` con un `WHERE` de igualdad y reporta el conteo. Luego encuéntralas con `FIND_IN_SET` sobre la misma columna y explica en un renglón qué acabas de renunciar a usar.

El segundo es la contradicción: mete dos lecturas del sensor 104 donde el nombre del equipo venga escrito de dos maneras, `Compresor de tornillo` y `Compresor de Tornillo`. Muestra las dos filas juntas.

El tercero es la anomalía de actualización: cambia el área de una sola de esas dos filas y vuelve a mostrarlas. El mismo equipo tiene que quedar en dos áreas a la vez, sin error y sin advertencia.

### 05.3 · Integrar

Repara el modelo. Tres tablas donde había una, con las llaves foráneas que las unen y con los mismos datos adentro, sin perder un solo renglón. Después vuelve a intentar los tres ataques de 05.2 sobre el modelo reparado y explica, ataque por ataque, si ahora es imposible o si simplemente cambió de lugar.

Al modelo reparado agrégale una tabla `consumo_energia` con la potencia en kilowatts, las horas de la orden y una tercera columna que sea el producto de las dos, calculada por el servidor y guardada. Mete una orden de 15.00 kW por 4.00 horas y muestra el resultado. Después intenta escribir esa tercera columna a mano con el valor 1.00 y pega el error.

Cierra con un renglón que diga qué acabas de comprar y qué acabas de pagar al partir la tabla en tres.

---

## Semana 06 · Del modelo a las tablas y las llaves

### 06.1 · Reconocer

Un guion `planta_ddl.sql` declara cinco tablas de la planta. `linea` tiene llave primaria y su nombre en `NOT NULL UNIQUE`. `equipo` tiene llave primaria, un código en `NOT NULL UNIQUE`, una llave foránea a `linea`, otra a sí misma, y una columna `estado` declarada `ENUM('operando','paro','baja') NOT NULL`. `certificado` tiene una llave foránea a `equipo` declarada además `UNIQUE`. `sensor` tiene un `CHECK (rango_min < rango_max)`. `medicion` tiene `UNIQUE (sensor_id, tomada_en)`, un `CHECK (valor BETWEEN -50 AND 500)` y una llave foránea a `sensor`.

Predice, para cada uno de estos siete intentos, si pasa o si rebota, y con qué número de error:

1. Una medición del sensor 1 con valor 742.00.
2. Una medición del sensor 1 con valor vacío.
3. Un segundo certificado para el equipo 1.
4. Un sensor cuyo equipo es el 77, que no existe.
5. Un equipo con estado `'reparacion'`.
6. Un `ALTER TABLE` que agrega una llave foránea hacia una columna que tiene índice normal pero no único.
7. Un `ALTER TABLE` que agrega una llave foránea desde una columna `VARCHAR(10)` hacia una `INT`.

Dos de los siete devuelven el mismo número. Di cuáles y por qué el servidor no los distingue.

### 06.2 · Aplicar

Escribe el guion completo. Las cinco tablas del modelo de la semana 4, desde una base vacía, con las cuatro reglas de mapeo aplicadas y con las restricciones que la especificación de 06.1 describe. Carga dos líneas, dos equipos, un certificado, un sensor y una medición.

El guion tiene que correr dos veces seguidas sin que lo edites. El orden de creación es parte de la entrega, y si necesitas moverlo a mano hay una llave foránea mal puesta.

### 06.3 · Integrar

Ataca tu propio guion con los siete intentos de 06.1 y pega los siete resultados. El segundo no falla, y ese es el punto: el `CHECK` deja pasar el valor desconocido por en medio del rango. Cierra ese hueco con la sentencia que corresponde y demuestra con una corrida que ahora sí rebota, con otro número de error.

Después corre `SHOW INDEX FROM sensor` y `SHOW INDEX` sobre `medicion`. Una de las dos tablas tiene un índice que nadie declaró y la otra no. Explica de dónde salió el que sobra y por qué en la otra tabla el servidor no necesitó escribirlo.

---

## Semana 07 · Tipos de dato y DDL

### 07.1 · Reconocer

Clasifica estos ocho comandos en su familia, con la pregunta de una línea de la sesión: `TRUNCATE TABLE`, `INSERT`, `GRANT`, `ROLLBACK`, `ALTER TABLE`, `DELETE`, `REVOKE`, `CREATE INDEX`. Al lado de cada uno escribe si el ROLLBACK puede deshacerlo.

Después predice las tres corridas siguientes sobre una tabla `t_prueba` que empieza con seis renglones:

```sql
START TRANSACTION;  TRUNCATE TABLE t_prueba;         ROLLBACK;  SELECT COUNT(*) FROM t_prueba;
START TRANSACTION;  CREATE TABLE t_ddl (id INT);     ROLLBACK;  SHOW TABLES LIKE 't_ddl';
START TRANSACTION;  DELETE FROM t_prueba WHERE id=3; ROLLBACK;  SELECT COUNT(*) FROM t_prueba;
```

Las tres llevan la misma palabra al final y las tres contestan cosas distintas. Explica en un renglón qué tienen en común las dos que no se deshicieron.

### 07.2 · Aplicar

En un esquema `tipos`, declara `sensor` y `medicion` eligiendo el tipo de cada columna en lugar de heredarlo. La clave del sensor son siempre seis caracteres. La magnitud es texto de largo variable. La fecha de instalación es una fecha, no una cadena. El estado es un catálogo cerrado de tres valores. El valor de la medición lleva dos enteros y dos decimales.

Escribe al lado de cada columna, en un comentario, el tipo que elegiste y la razón en una línea. Después provoca a propósito estos cuatro rechazos y pega los cuatro errores con su número:

1. Una fecha escrita como se dice en voz alta, `'02/03/2026'`.
2. Un valor de 9999.9 en la columna de dos enteros.
3. Una clave de sensor de siete caracteres.
4. Un `NULL` en la columna de magnitud.

### 07.3 · Integrar

Tres mediciones sobre el mismo esquema, cada una contra una creencia común.

Primero el ENUM. Ordena los sensores por `estado` y muestra al lado `estado + 0`. Alfabéticamente el orden sería `baja`, `operando`, `paro`. Reporta el que salió y explica de dónde viene.

Segundo, la pareja que la fuente confunde. `sensor` es padre de `medicion`. Intenta vaciarla con `TRUNCATE` y luego borrar un renglón con `DELETE`, y pega los dos errores, que traen número distinto para el mismo obstáculo.

Tercero, el contador. Sobre una tabla `bitacora_paro` con `AUTO_INCREMENT` y sin hijos, carga tres renglones, vacíala con `DELETE`, mete uno nuevo y anota su identificador. Repite el ciclo con `TRUNCATE`. Los dos identificadores no son iguales, y esa diferencia es el argumento de por qué `TRUNCATE` es DDL.

Cierra guardando `'SN-1  '`, con dos espacios al final, en una columna `CHAR(6)` y en una `VARCHAR(6)`, y leyendo de vuelta las dos con su longitud.

---

## Semana 08 · DML y transacciones · Primer parcial

### 08.1 · Reconocer

La tabla `medicion` del esquema `dml` empieza con seis renglones. Predice los cinco conteos de esta corrida, en orden:

```sql
START TRANSACTION;
DELETE FROM medicion WHERE medicion_id = 6;
SAVEPOINT s1;
DELETE FROM medicion WHERE medicion_id = 5;
ROLLBACK TO SAVEPOINT s1;
ROLLBACK;
```

Después contesta dos preguntas sin correr nada. Si en lugar del `ROLLBACK` final hubiera un `COMMIT`, ¿con cuántos renglones se queda la tabla? Y si `@@autocommit` valiera 1 y alguien hubiera borrado el `START TRANSACTION`, ¿qué habría contestado el `ROLLBACK`?

### 08.2 · Aplicar

Tres cargas contra el esquema `dml`, que tiene un `CHECK` sobre `medicion.valor` entre -50 y 500.

La primera es un `INSERT` de tres lecturas en una sola sentencia, donde la de en medio trae 742.00. Cuenta antes y cuenta después. Los dos números tienen que ser el mismo, y ese es el punto: la sentencia ya es atómica sin que nadie lo pida.

La segunda es la misma carga corregida, con las tres lecturas dentro del rango.

La tercera saca las filas de una consulta en lugar de teclearlas: da de alta una orden preventiva con fecha 2026-04-01 para cada equipo de la línea 1, sin escribir un solo identificador a mano. Muestra las órdenes que quedaron.

Al final calcula las horas entre paros de cada equipo, dividiendo las horas de operación entre el número de paros. Uno de los equipos tiene cero paros. Corre la división primero en un `SELECT` y después adentro de un `INSERT` hacia una tabla `indicador`, y pega las dos salidas, que no son la misma.

### 08.3 · Integrar

Repaso del primer parcial, que cubre de la semana 1 a la 8. Un solo guion, cuatro partes.

Parte uno, del modelo al DDL. De la frase «cada sensor pertenece a un equipo y un equipo tiene varios sensores», escribe la cardinalidad, su forma física y el `CREATE TABLE` que la implementa con la restricción que la sostiene.

Parte dos, los tipos. Justifica en una línea por qué la marca de tiempo no puede quedar en `VARCHAR` y por qué el valor no puede quedar en `FLOAT`, citando cada uno un error medido en clase.

Parte tres, la carga. Envuelve una carga de tres lecturas en una transacción, verifica con un `SELECT` de conteo antes de confirmar, y confirma. Si el conteo no cuadra va un `ROLLBACK`, nunca un `DELETE` de reparación.

Parte cuatro, las tres condiciones. Demuestra con tres corridas separadas las tres situaciones en que un `ROLLBACK` no deshace nada: con un `CREATE TABLE` metido entre el `INSERT` y el `ROLLBACK`, sobre una tabla `ENGINE=MyISAM`, y sin transacción abierta. Pega las tres salidas y di cuál de las tres es la más peligrosa, con un argumento.

---

## Semana 09 · El SELECT de una tabla

### 09.1 · Reconocer

La tabla `equipo` del anexo tiene ocho renglones y una columna `criticidad` que acepta vacío. La tabla `medicion` tiene veinte.

Predice, sin correr nada, estos ocho conteos:

```sql
SELECT COUNT(*) FROM equipo;
SELECT COUNT(*) FROM equipo WHERE criticidad =  'alta';
SELECT COUNT(*) FROM equipo WHERE criticidad <> 'alta';
SELECT COUNT(*) FROM equipo WHERE criticidad =  NULL;
SELECT COUNT(*) FROM equipo WHERE criticidad IS NULL;
SELECT COUNT(*) FROM medicion;
SELECT COUNT(*) FROM medicion WHERE valor IS NOT NULL;
SELECT COUNT(*) FROM medicion WHERE valor IS NULL;
```

El segundo y el tercero no suman el primero. Explica en dos renglones por qué, con el nombre del tercer estado que contesta una condición en SQL.

Después predice cuántos equipos devuelve cada una de estas dos consultas, que difieren en un paréntesis:

```sql
SELECT codigo FROM equipo
 WHERE criticidad = 'alta' OR criticidad = 'media' AND estado = 'operando';

SELECT codigo FROM equipo
 WHERE (criticidad = 'alta' OR criticidad = 'media') AND estado = 'operando';
```

### 09.2 · Aplicar

Arma la pantalla de búsqueda de equipos del área de mantenimiento, sobre la tabla `equipo` y sin un solo JOIN. Son cinco consultas.

Una, el filtro exacto por estado, que devuelve los seis equipos operando.

Dos, la caja de texto. Busca `hidraulica` sin escribir el acento y encuentra la prensa. Busca `recirculacion` sin escribir el acento y encuentra la bomba. Busca `prensa` en minúscula y encuentra la prensa. Consulta `@@collation_database` y explica en un renglón por qué no tuviste que escribir nada de manejo de acentos.

Tres, el porcentaje que es dato y no comodín. Sobre `refaccion.descripcion`, busca `50` y luego busca el `50` seguido del signo de porcentaje literal. La primera devuelve tres refacciones y la segunda una.

Cuatro, listas y rangos. Cuenta los equipos cuya criticidad está en `('alta','baja')` y los que no están. Después cuenta las mediciones con valor entre 6.40 y 41.80, con los mismos límites escritos con mayor y menor estrictos, y con los dos límites invertidos. Los tres números son 6, 4 y 0.

Cinco, la rejilla. Los equipos ordenados por código, de tres en tres, página uno y página dos.

### 09.3 · Integrar

Tres errores callados, cada uno cruzado con una semana anterior.

El primero cruza con la semana 7. Ordena los sensores por su columna `canal`, que está declarada `VARCHAR(4)` y guarda `1`, `2`, `3`, `9`, `10` y `100`. Pega el orden que salió, corre `SELECT '10' < '9'` junto a `SELECT 10 < 9` para explicarlo, y escribe la sentencia DDL que lo arreglaría de raíz.

El segundo es el alias. Calcula la amplitud del rango de cada sensor como `rango_max - rango_min`, ponle alias, y úsalo primero en el `WHERE` y luego en el `ORDER BY`. Pega el error del primero y la salida del segundo, y explica la diferencia con la tabla del orden lógico de las cláusulas.

El tercero es el orden con vacíos. Muestra las tres mediciones más bajas. Con el orden ascendente simple, los vacíos salen primero. Escribe la versión que los manda al final, sin usar la cláusula del estándar que MySQL no tiene, y pega también el error que devuelve esa cláusula para que quede el registro.

Cierra con la coma que falta: corre `SELECT codigo, nombre FROM equipo LIMIT 3` y después el mismo `SELECT` sin la coma. Ninguno de los dos da error, y el reporte del segundo sale mal.

---

## Semana 10 · Agrupación y agregados

### 10.1 · Reconocer

Sobre las veinte mediciones del anexo, predice el renglón completo que devuelve esta consulta:

```sql
SELECT COUNT(*) AS n, COUNT(valor) AS c, AVG(valor) AS prom,
       MIN(valor) AS mn, MAX(valor) AS mx
FROM medicion;
```

Después predice los tres valores de esta otra, y di cuál de los dos cocientes es el promedio de verdad y cuál es el que alguien va a mandar en un reporte por equivocación:

```sql
SELECT SUM(valor) AS suma,
       SUM(valor)/COUNT(*)     AS entre_20,
       SUM(valor)/COUNT(valor) AS entre_15
FROM medicion;
```

Cierra escribiendo, en un renglón, con cuántas de las veinte lecturas se calculó el promedio y de dónde va a sacar ese dato quien reciba el reporte.

### 10.2 · Aplicar

El informe mensual de mantenimiento, sobre la tabla `orden`. Cinco consultas.

Una, provoca el error 1055 a propósito pidiendo el folio al lado de un conteo agrupado por tipo. Pega el error completo y escribe al lado la versión corregida.

Dos, las órdenes por equipo, con cuatro columnas: cuántas hay, cuántas traen horas capturadas, la suma de horas y el promedio. El equipo 2 tiene tres órdenes y solo dos con horas.

Tres, la diferencia entre los dos filtros. Pide los equipos con más de dos órdenes poniendo la condición en el `WHERE` y después en el `HAVING`. Uno de los dos falla; pega el error y explícalo con el orden lógico de la semana pasada.

Cuatro, el pivote. Una matriz con un renglón por equipo y tres columnas de conteo, una por tipo de orden, armada con agregado condicional.

Cinco, las órdenes por mes. Agrupa por año y mes con el nombre del mes, ordena cronológicamente y explica por qué un curso en español imprime `January`. Después cambia `lc_time_names` a `es_MX` y vuelve a pedir un nombre de mes.

### 10.3 · Integrar

La trampa más cara de la sesión, sobre la columna `equipo_padre_id` de la tabla `equipo`, que acepta vacío.

Pregunta cuántos equipos no son padres de ningún otro, escribiendo la misma pregunta de dos maneras: con `NOT IN` sobre una subconsulta y con `NOT EXISTS` correlacionado. Pega los dos conteos, que no coinciden, y el conteo de cuántos `equipo_padre_id` están vacíos, que es lo que explica la diferencia. Ninguna de las dos consultas dio error ni advertencia.

Después escribe la carga de órdenes por equipo con una `WITH`, y pídele las que están por encima del promedio del propio conjunto. Explica en un renglón qué te ahorró la cláusula frente a escribir la misma agrupación dos veces.

Cierra clasificando las refacciones por su punto de reorden con un `CASE` de cuatro ramas, donde una rama es para el punto de reorden vacío. Después clasifica lo mismo con un `IF` de dos ramas. Una refacción tiene punto de reorden 0 y otra lo tiene vacío. Muestra las dos salidas y di en qué renglón exacto las dos versiones dejan de estar de acuerdo, y cuál de las dos está mal.

---

## Semana 11 · JOIN, UNION y UNION ALL

### 11.1 · Reconocer

Hay ocho equipos y doce órdenes de trabajo. Predice, sin correr nada, estos cuatro números:

1. Cuántas filas devuelve `equipo INNER JOIN orden` por `equipo_id`.
2. Cuántas devuelve el mismo par con `LEFT JOIN`.
3. Cuántos equipos salen si además filtras por `WHERE o.orden_id IS NULL`.
4. Para el equipo 3, que no tiene órdenes, cuánto vale `COUNT(*)` y cuánto vale `COUNT(o.orden_id)` en la misma fila del resultado agrupado.

El cuarto es el que hay que poder explicar. Escribe en dos renglones de dónde sale la fila que `COUNT(*)` está contando.

### 11.2 · Aplicar

Tres consultas sobre la planta.

Una, reensambla lo que la semana 5 partió. Trae el código del equipo, la clave del sensor, la marca de tiempo y el valor, uniendo `medicion`, `sensor` y `equipo`. Lee cada `ON` en voz alta como una frase antes de escribirlo, y déjala en el comentario.

Dos, el error más común que existe. Cuenta las filas de un `LEFT JOIN` de `equipo` con `orden` poniendo `o.tipo = 'correctivo'` primero en el `WHERE` y después en el `ON`. Los dos números son 5 y 9. Explica en dos renglones por qué el predicado en el `WHERE` convirtió tu `LEFT JOIN` en un `INNER JOIN`.

Tres, el producto cartesiano. Une `linea` con `equipo` sin escribir el `ON` y reporta cuántas filas salieron. La consulta es legal y nadie levanta la mano.

### 11.3 · Integrar

La junta de inventarios. El almacén central dice que tiene siete refacciones en la tabla `refaccion`. El sistema de la línea dice que tiene ocho en `inventario_linea`. Nadie sabe cuántas son en realidad.

Primero intenta la consulta que lo contestaría de un golpe, con `FULL OUTER JOIN`, y pega el error.

Después arma la receta que sí funciona: un `LEFT JOIN` unido con un `RIGHT JOIN`. Reporta los cuatro conteos, el del `LEFT`, el del `RIGHT`, el de las que coinciden y el de la unión, y muestra las diez filas del resultado leídas en tres bloques: las que están en los dos lados, las que solo están en el central y las que solo están en la línea. La proyección tiene que traer las dos claves, la del central y la de la línea, o dos refacciones distintas se te van a fundir en una.

Cierra con el costo de tres letras. Sobre `consumo_turno_a` y `consumo_turno_b`, cuenta las filas y suma las piezas, primero con `UNION ALL` y después con `UNION`. Los resultados son 7 filas con 18 piezas y 4 filas con 9 piezas. Di cuál de los dos números es el consumo real del almacén y por qué el otro salió sin una sola advertencia.

---

## Semana 12 · Vistas

### 12.1 · Reconocer

Cuatro vistas sobre el esquema `planta`:

- `v_medicion_completa`, un `INNER JOIN` de `medicion`, `sensor` y `equipo`.
- `v_medicion_izquierda`, un `LEFT JOIN` de `sensor` con `medicion`.
- `v_carga_sensor`, un `COUNT` y un `AVG` agrupados por sensor.
- `v_sensor_conteo`, los sensores con una subconsulta escalar que cuenta sus mediciones.

Predice para cada una qué va a decir la columna `IS_UPDATABLE` del catálogo. Después predice qué contesta el servidor a estos cinco intentos:

1. `UPDATE` del valor de una medición, que vive en una sola tabla base, a través de `v_medicion_completa`.
2. `UPDATE` que toca dos tablas base en la misma sentencia, también por `v_medicion_completa`.
3. `DELETE` a través de `v_medicion_completa`.
4. `UPDATE` a través de `v_medicion_izquierda`.
5. `UPDATE` a través de `v_sensor_conteo`, sobre una columna que no es la calculada.

Uno de los cinco es el desacuerdo del semestre: el catálogo dice una cosa y el servidor hace otra. Di cuál y qué regla operativa se lleva el grupo de ahí.

### 12.2 · Aplicar

Tres vistas en capas sobre `planta`. La primera limpia y renombra una sola tabla. La segunda aplica una regla del área sobre la primera, no sobre la tabla: los equipos de criticidad alta que están operando. La tercera agrega y aplana, contando equipos por línea.

Intenta un `UPDATE` a través de cada una de las tres y pega las tres respuestas. Dos pasan y una falla; explica en un renglón por qué la que falla no podía hacer otra cosa.

Después construye la vista del coordinador de la línea 1 y ciérrala. Sin `WITH CHECK OPTION`, inserta desde la vista un equipo de la línea 3, búscalo en la vista y no lo encuentres, y después búscalo en la tabla base y sí. Vuelve a crear la vista con la cláusula, repite el intento y pega el error.

### 12.3 · Integrar

Tres creencias, tres mediciones.

Primera, el asterisco. Crea una vista con `SELECT *` sobre `refaccion`, agrega una columna a la tabla base, y vuelve a consultar la vista y la tabla. Pega las dos salidas lado a lado y explica con `SHOW CREATE VIEW` por qué la vista no vio la columna nueva.

Segunda, el orden. Crea una vista con un `ORDER BY ... DESC` adentro. Consúltala directo y después consúltala desde un `JOIN`. Pega los dos órdenes, que no son el mismo, y di a quién pertenece el orden de un resultado.

Tercera, la velocidad. Corre `EXPLAIN` sobre `v_medicion_completa` sin filtro. Pega el plan y señala cuántas veces aparece el nombre de la vista en él. Con eso contesta si guardar una consulta la hace más rápida.

Cierra consultando el `DEFINER` y el `SECURITY_TYPE` de la vista que creaste. Escribe en dos renglones quién quedó ahí, si tú lo pediste, y en qué semana se va a cobrar eso.

---

## Semana 13 · Procedimientos y errores · Segundo parcial

### 13.1 · Reconocer

Este procedimiento se crea sin error y contesta mal:

```sql
CREATE PROCEDURE sp_malo(IN sensor_id INT)
BEGIN
  SELECT COUNT(*) AS filas_devueltas FROM medicion WHERE sensor_id = sensor_id;
END
```

La tabla `medicion` tiene veinte renglones y el sensor 1 tiene cuatro. Predice qué contesta `CALL sp_malo(1)` y explica en dos renglones qué comparó el `WHERE` en realidad. Escribe después el único cambio que lo arregla.

Predice también qué número de error sale de cada una de estas cuatro señales, todas levantadas desde adentro de un procedimiento:

```sql
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Operacion no permitida';
SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Integridad violada';
SIGNAL SQLSTATE '22012' SET MESSAGE_TEXT = 'Division entre cero';
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Valor fuera de escala', MYSQL_ERRNO = 3001;
```

Tres de las cuatro traen el mismo número. Di cuál es la única pieza que tu aplicación puede usar para distinguir un error tuyo de otro.

### 13.2 · Aplicar

Escribe `sp_carga_equipo`, que recibe un identificador de equipo y devuelve dos cosas: un resultado en pantalla con el código, el nombre, cuántas órdenes tiene y la suma de sus horas, y un parámetro de salida con el número de órdenes. Por dentro reutiliza el `LEFT JOIN` de la semana 11 y la agrupación de la semana 10, sin cambiar una línea de ellas.

El guion arranca con `DROP PROCEDURE IF EXISTS` y usa `DELIMITER`, porque lo vas a correr veinte veces esta tarde. Los parámetros llevan prefijo, y en un comentario di qué pasaría si no lo llevaran.

Llámalo con el equipo 2, que tiene tres órdenes y 10.25 horas. Después llámalo pasando el número 5 donde va el parámetro de salida y pega el error. Al final agrégale un parámetro `INOUT` que acumule, inicialízalo en 100 y muestra que salió en 104.

### 13.3 · Integrar

Repaso del segundo parcial, que cubre de la semana 9 a la 12, envuelto en el tema de hoy.

Escribe `sp_dos_pasos`, que mete dos mediciones donde la segunda apunta a un sensor que no existe. Cuenta antes, llámalo, pega el error y cuenta después. Muestra que la primera fila se quedó adentro y explica en un renglón por qué el error llegó tarde.

Después escribe `sp_dos_pasos_seguro`, la versión que no deja trabajo a medias. Lleva un `DECLARE CONDITION` con nombre, un `EXIT HANDLER`, un `GET DIAGNOSTICS` que recupere las tres piezas del error, un `ROLLBACK` escrito por ti, y un parámetro de salida que devuelva el diagnóstico como texto legible. Cuenta antes y después de la llamada; los dos números tienen que ser el mismo.

Escribe una tercera versión que en lugar de devolver texto vuelva a lanzar el error con `RESIGNAL`, con el número 3101 y un mensaje que la oficina de mantenimiento pueda leer.

Cierra con dos renglones sobre el `SQLSTATE 23000`: nombra las tres situaciones distintas que lo producen y di qué atrapa de más el handler que acabas de escribir.

---

## Semana 14 · Triggers y eventos

### 14.1 · Reconocer

Completa la tabla de los seis momentos, diciendo para cada uno si `OLD` existe, si `NEW` existe y si `NEW` se puede escribir: `BEFORE INSERT`, `AFTER INSERT`, `BEFORE UPDATE`, `AFTER UPDATE`, `BEFORE DELETE`, `AFTER DELETE`.

Después predice tres cosas.

Una, qué contesta el servidor si intentas crear un trigger `BEFORE INSERT` cuyo cuerpo lee `OLD.valor`. Di además en qué momento aparece ese error, al crearlo o al dispararlo.

Dos, esta validación:

```sql
IF NEW.valor < 0 OR NEW.valor > 500 THEN
  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Valor fuera de la escala del sensor';
END IF;
```

Di qué pasa cuando llega una medición con 742.00 y qué pasa cuando llega una con el valor vacío. Explica la segunda con la lógica de tres valores de la semana 9 y escribe la guarda que la cierra.

Tres, la misma regla escrita como restricción declarativa en lugar de como trigger. Di qué número de error sale de cada una de las dos y en qué se diferencia lo que el usuario alcanza a leer.

### 14.2 · Aplicar

Sobre un esquema `auto` con `sensor`, `medicion` y `medicion_bitacora`, instala dos triggers.

El primero valida el valor contra la escala, con la guarda del vacío puesta. Nómbralo con la convención de tabla, momento, evento y propósito, para que un `SHOW TRIGGERS` se lea sin abrir el cuerpo. Prueba que rechaza 742.00 y que deja pasar el vacío.

El segundo escribe la bitácora en el `AFTER UPDATE`, dejando el valor viejo y el nuevo en el mismo renglón, junto con la acción y la marca de tiempo. Cambia una medición de 71.50 a 68.00 y muestra el renglón que quedó.

### 14.3 · Integrar

El agujero de la bitácora, medido en dos corridas.

La llave foránea de `medicion` está declarada con `ON DELETE CASCADE` y la tabla tiene además un trigger `BEFORE DELETE` que escribe la bitácora. Cuenta las mediciones del sensor 3 y los renglones de bitácora. Borra el sensor 3. Vuelve a contar las dos cosas. La medición desapareció y la bitácora no creció.

Repite el experimento con `TRUNCATE TABLE medicion`. Tres mediciones desaparecen y la bitácora sigue igual.

Escribe en tres renglones qué es lo que un trigger sí ve y qué es lo que no, y propón el mecanismo que sí registraría las dos desapariciones.

Cierra con los eventos. Crea uno con una fecha que ya pasó, corre `SHOW WARNINGS` justo después y busca el evento en el catálogo. El `CREATE` no dio error y el evento no está. Después crea el recurrente que purga la bitácora cada día y muéstralo en el catálogo con su tipo, su intervalo y su estado.

---

## Semana 15 · Índices y desempeño

### 15.1 · Reconocer

Sobre `medicion_big`, que tiene 200 000 renglones, existe un solo índice secundario, el compuesto `(equipo_id, tomada_en)`. Predice, para estas tres consultas, el valor de `type`, el de `key` y el de `rows` que va a devolver `EXPLAIN FORMAT=TRADITIONAL`:

```sql
SELECT medicion_id FROM medicion_big WHERE equipo_id = 42;
SELECT medicion_id FROM medicion_big WHERE equipo_id = 42 AND tomada_en = '2026-01-15';
SELECT medicion_id FROM medicion_big WHERE tomada_en = '2026-01-15';
```

La tercera es la que separa al grupo, porque el índice aparece en `key` y aun así no sirve de lo que parece. Explica con la regla del prefijo izquierdo qué está haciendo el servidor ahí.

Después predice qué pasa con un índice `(turno, valor)` cuando la consulta filtra solo por `valor` y `turno` tiene cuatro valores distintos. La respuesta no es la misma que la de la tercera consulta, y el nombre de lo que ocurre no aparece en ninguna fuente escrita para 5.7.

### 15.2 · Aplicar

Mide, indexa y vuelve a medir. La consulta es esta, sobre 200 000 mediciones y 50 000 equipos:

```sql
SELECT m.medicion_id, e.codigo
  FROM medicion_big m
  JOIN equipo_big e ON e.equipo_id = m.equipo_id
 WHERE e.codigo = 'EQ-000042';
```

Con las dos tablas sin un solo índice secundario, guarda el plan y el tiempo. Después construye los dos índices que la reparan, uno por tabla, y guarda el plan y el tiempo otra vez. Se entrega la comparación, no la opinión: los dos planes pegados uno junto al otro, el número de filas examinadas en cada caso y los dos tiempos.

Antes de cada medición corre la consulta una vez sin cronometrarla, para que el pool de la semana 3 no te mida el primer acceso a disco.

### 15.3 · Integrar

Auditoría del consejo heredado, en tres ramas y con evidencia.

Sobre `mensaje`, que tiene 60 000 renglones y un índice de prefijo en `titulo`, corre tres búsquedas de la misma palabra: anclada al inicio con `LIKE 'Paro por vibracion%'`, con el comodín al inicio, y con `REGEXP '^Paro por vibracion'`. Pega los tres planes con su `type`, su `key` y sus filas examinadas, y da un veredicto por rama: se sostiene, se matiza o se cae.

Después construye el índice de texto completo sobre `cuerpo` y mide dos cosas: lo que cuesta construirlo y lo que compra. Antes de construirlo, intenta la consulta con `MATCH ... AGAINST` y pega el error. Intenta también declararlo sobre una columna numérica y pega el otro error. Ya construido, compara el tiempo de `MATCH` contra el de `LIKE '%vibracion%'` sobre la misma columna.

Cierra con el otro lado de la apuesta. Carga las mismas 200 000 filas en dos tablas idénticas, una sin índices secundarios y otra con ocho, y reporta los dos tiempos y las dos columnas `DATA_LENGTH` e `INDEX_LENGTH`. Escribe el cociente de cada uno.

---

## Semana 16 · Concurrencia y bloqueos · Proyecto

### 16.1 · Reconocer

Dos ventanillas del almacén corren el mismo guion sobre la refacción 3, que tiene 25 piezas. Cada una saca cinco.

```sql
START TRANSACTION;
SELECT existencia INTO @c FROM refaccion WHERE refaccion_id = 3;
-- aqui la persona teclea un momento
UPDATE refaccion SET existencia = @c - 5 WHERE refaccion_id = 3;
COMMIT;
```

La sesión A leyó a las 21:24:38.205676 y la B a las 21:24:38.387740. Predice tres números: qué leyó A, qué leyó B y con cuántas piezas se queda la refacción al final. Di cuántas piezas salieron del almacén de verdad y cuántas dice el sistema que salieron.

Después predice el resultado de las dos reparaciones, corriendo el mismo par de sesiones: una que agrega `FOR UPDATE` a la lectura, y otra que no lee y le pide al servidor que reste. Las dos llegan al mismo número final y no por el mismo camino. Explica la diferencia en dos renglones.

### 16.2 · Aplicar

Reproduce las tres corridas de 16.1 con dos sesiones de verdad, no con una sola. Cada sesión imprime `NOW(6)` al leer y al escribir, y se entregan las marcas de tiempo de las dos.

Después mide la distinción que parte la semana. Con `innodb_lock_wait_timeout` en 3 segundos, monta el caso en que la sesión B espera un candado que A no suelta, y pega el error con el tiempo que tardó en llegar. Monta después el caso en que A y B se piden mutuamente lo que la otra tiene, y pega el otro error.

Los dos errores tienen consecuencias distintas y ahí está el ejercicio. En la sesión que recibió la espera expirada, escribe algo en otra fila antes del error y confirma después de él. En la que recibió el interbloqueo, haz lo mismo. Reporta qué sobrevivió en cada caso.

### 16.3 · Integrar

El surtido con revisión de existencia, que es el error de diseño más común que hay.

Escribe `sp_surtir`, que recibe una refacción y una cantidad, lee la existencia, decide si alcanza, y si alcanza descuenta y registra la salida. Con 25 piezas en la refacción 3, llámalo desde dos sesiones a la vez, cada una pidiendo 20. Reporta lo que vio cada sesión, la existencia final y cuántas piezas salieron según la tabla `salida`.

Después escribe `sp_surtir_seguro`, que se diferencia en una sola cláusula, y repite el experimento desde el mismo estado. Reporta los mismos tres números.

Cierra con el reintento. Escribe `sp_ajustar`, que descuenta una pieza de dos refacciones en el orden que le digan, con un `CONTINUE HANDLER` para el `SQLSTATE '40001'`, un `ROLLBACK` adentro del handler y un `LOOP` que vuelva a intentar hasta cinco veces. Llámalo desde dos sesiones con los identificadores en orden invertido y reporta cuántos intentos necesitó cada una y en cuánto quedaron las dos refacciones. Las dos tienen que quedar con sus dos descuentos aplicados.

---

## Semana 17 · Usuarios, respaldo y cierre · Examen final

### 17.1 · Reconocer

Lee esta salida de `SHOW GRANTS` y di qué sentencias le van a ser negadas a la cuenta, con el número de error de cada una:

```
GRANT USAGE ON *.* TO `ing_tutor`@`localhost`
GRANT SELECT (`clave`, `descripcion`), UPDATE (`existencia`)
  ON `planta`.`refaccion` TO `ing_tutor`@`localhost`
```

Las cuatro sentencias a juzgar son: leer clave y descripción de `refaccion`; leer clave y existencia; actualizar existencia; actualizar descripción. Dos de las cuatro rebotan, y no con el mismo número que un permiso faltante de tabla completa.

Después lee este comando y di qué objetos del esquema no van a estar en el archivo que produce:

```
mysqldump -u root -p taller > taller.sql
```

El esquema `taller` tiene tres tablas, una vista, un trigger, un evento y un procedimiento. Di también qué imprime `mysqldump` en el error estándar mientras trabaja, y cuál es la última línea que un archivo completo tiene que traer.

### 17.2 · Aplicar

Del lado de las cuentas, cuatro corridas.

Una, intenta el `GRANT` sobre una cuenta que no creaste y pega el error. Después créala y pide sus privilegios antes y después de otorgarle lectura sobre `planta`.

Dos, ábrete una segunda ventana conectada como esa cuenta restringida y prueba tres cosas: una lectura que sí puede, un borrado que no puede, y una lectura de `mysql.user`. Pega los dos errores.

Tres, crea la cuenta con permisos por columna del ejercicio 17.1 y corre desde ella las cuatro sentencias que juzgaste. Verifica tus dos veredictos.

Cuatro, crea un rol de lectura, otórgaselo a una cuenta, conéctate con ella y consulta `CURRENT_ROLE()` antes de hacer nada. Explica con `@@activate_all_roles_on_login` por qué la cuenta con rol recibe el mismo error que una sin él, y arréglalo en la sesión.

Del lado del respaldo, produce tres archivos del esquema `taller`: el que sale por omisión, el completo, y el del esquema sin datos. Reporta los tres tamaños en bytes y cuántas veces aparece `PROCEDURE` y `EVENT` en cada uno.

### 17.3 · Integrar

Repaso final, que cruza los cinco bloques del semestre en una sola secuencia.

Primero restaura. Toma el respaldo completo, restáuralo en un esquema nuevo y reporta el código de salida y cuántas líneas imprimió el cliente. Después verifica la restauración de la única manera que existe: contando del otro lado. Los conteos de las tres tablas y la presencia del procedimiento, el evento y el trigger en el catálogo.

Segundo, restaura sobre una base viva. Agrega una herramienta, borra un préstamo y crea una tabla que el respaldo no conoce. Vuelve a restaurar el mismo archivo encima y reporta qué pasó con las tres cosas. Una de ellas sobrevive intacta; explica por qué.

Tercero, el archivo que miente. Corre un `mysqldump` que nombre una tabla que no existe, reporta el código de salida y el tamaño del archivo que dejó, y muestra su última línea. Di cuál es la señal de que ese archivo no sirve.

Cierra con tres párrafos cortos, uno por cada cosa que sobrevive al número de versión. Uno sobre `sql_mode`, nombrando cuatro errores del semestre que solo son errores porque el modo estricto está encendido. Uno sobre `EXPLAIN`, citando una afirmación de desempeño que mediste este semestre y que resultó estar al revés. Y uno sobre la contradicción entre la semana 6, que llama al índice un detalle agregado, y la semana 15, que lo midió. Resuélvela con tu propia medición, no con la autoridad de ninguna de las dos láminas.

---

## Anexo · La base de trabajo

Todos los ejercicios corren contra este esquema, una planta de manufactura con tres líneas. Se levanta desde una base vacía y se puede volver a correr cuantas veces haga falta.

```sql
DROP DATABASE IF EXISTS planta;
CREATE DATABASE planta CHARACTER SET utf8mb4;
USE planta;

CREATE TABLE linea (
  linea_id INT PRIMARY KEY,
  nombre   VARCHAR(40) NOT NULL UNIQUE,
  area     VARCHAR(30) NOT NULL
);

CREATE TABLE equipo (
  equipo_id         INT PRIMARY KEY,
  codigo            CHAR(7)     NOT NULL UNIQUE,
  nombre            VARCHAR(60) NOT NULL,
  linea_id          INT         NOT NULL,
  equipo_padre_id   INT         NULL,
  fecha_instalacion DATE        NOT NULL,
  estado            ENUM('operando','paro','baja') NOT NULL,
  criticidad        VARCHAR(10) NULL,
  FOREIGN KEY (linea_id)        REFERENCES linea(linea_id),
  FOREIGN KEY (equipo_padre_id) REFERENCES equipo(equipo_id)
);

CREATE TABLE sensor (
  sensor_id INT PRIMARY KEY,
  clave     CHAR(6)     NOT NULL UNIQUE,
  equipo_id INT         NOT NULL,
  magnitud  VARCHAR(20) NOT NULL,
  unidad    VARCHAR(10) NOT NULL,
  canal     VARCHAR(4)  NOT NULL,
  rango_min DECIMAL(7,2) NOT NULL,
  rango_max DECIMAL(7,2) NOT NULL,
  FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);

CREATE TABLE medicion (
  medicion_id INT PRIMARY KEY,
  sensor_id   INT      NOT NULL,
  tomada_en   DATETIME NOT NULL,
  valor       DECIMAL(7,2) NULL,
  FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id)
);

CREATE TABLE orden (
  orden_id  INT PRIMARY KEY,
  folio     CHAR(8) NOT NULL UNIQUE,
  equipo_id INT     NOT NULL,
  tipo      ENUM('preventivo','correctivo','predictivo') NOT NULL,
  turno     ENUM('matutino','vespertino','nocturno') NOT NULL,
  fecha     DATE    NOT NULL,
  horas     DECIMAL(5,2) NULL,
  FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);

CREATE TABLE refaccion (
  refaccion_id  INT PRIMARY KEY,
  clave         CHAR(6)     NOT NULL UNIQUE,
  descripcion   VARCHAR(60) NOT NULL,
  existencia    INT NOT NULL,
  punto_reorden INT NULL
);

CREATE TABLE consumo (
  orden_id     INT,
  refaccion_id INT,
  cantidad     INT NOT NULL,
  PRIMARY KEY (orden_id, refaccion_id),
  FOREIGN KEY (orden_id)     REFERENCES orden(orden_id),
  FOREIGN KEY (refaccion_id) REFERENCES refaccion(refaccion_id)
);

CREATE TABLE certificado (
  certificado_id INT PRIMARY KEY,
  equipo_id      INT  NOT NULL UNIQUE,
  folio          CHAR(9) NOT NULL,
  vigencia       DATE NOT NULL,
  FOREIGN KEY (equipo_id) REFERENCES equipo(equipo_id)
);

INSERT INTO linea VALUES
 (1,'Ensamble A','Manufactura'),
 (2,'Pintura','Acabados'),
 (3,'Empaque','Logistica interna');

INSERT INTO equipo VALUES
 (1,'EQ-0001','Prensa hidráulica 200 t', 1, NULL,'2019-03-11','operando','alta'),
 (2,'EQ-0002','Robot de soldadura',      1, NULL,'2020-07-01','operando','alta'),
 (3,'EQ-0003','Pinza del robot',         1, 2,   '2021-02-15','operando','media'),
 (4,'EQ-0004','Compresor de tornillo',   2, NULL,'2018-05-20','paro','alta'),
 (5,'EQ-0005','Cabina de pintura',       2, NULL,'2019-11-04','operando','media'),
 (6,'EQ-0006','Bomba de recirculación',  2, 5,   '2019-11-04','operando','media'),
 (7,'EQ-0007','Banda transportadora',    3, NULL,'2022-01-10','operando','baja'),
 (8,'EQ-0008','Enfardadora',             3, NULL,'2017-09-30','baja',NULL);

INSERT INTO sensor VALUES
 (1,'SN-101',1,'temperatura','C',   '1',   0.00,120.00),
 (2,'SN-102',1,'presion',    'bar', '2',   0.00, 10.00),
 (3,'SN-103',2,'vibracion',  'mm/s','9',   0.00, 45.00),
 (4,'SN-104',4,'temperatura','C',   '10',  0.00,120.00),
 (5,'SN-105',5,'flujo',      'l/min','100',0.00,250.00),
 (6,'SN-106',7,'vibracion',  'mm/s','3',   0.00, 45.00);

INSERT INTO medicion VALUES
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

INSERT INTO orden VALUES
 ( 1,'OT-26001',1,'preventivo','matutino',  '2026-01-12', 3.50),
 ( 2,'OT-26002',1,'correctivo','nocturno',  '2026-01-28', 6.00),
 ( 3,'OT-26003',2,'preventivo','matutino',  '2026-02-02', 2.25),
 ( 4,'OT-26004',2,'correctivo','vespertino','2026-02-14', 8.00),
 ( 5,'OT-26005',2,'predictivo','matutino',  '2026-02-20', NULL),
 ( 6,'OT-26006',4,'correctivo','nocturno',  '2026-02-25',12.00),
 ( 7,'OT-26007',4,'correctivo','nocturno',  '2026-03-01', 9.50),
 ( 8,'OT-26008',5,'preventivo','matutino',  '2026-01-15', 4.00),
 ( 9,'OT-26009',5,'preventivo','vespertino','2026-02-16', 4.25),
 (10,'OT-26010',6,'correctivo','matutino',  '2026-02-27', 5.00),
 (11,'OT-26011',7,'preventivo','matutino',  '2026-01-20', 1.75),
 (12,'OT-26012',7,'predictivo','vespertino','2026-03-03', NULL);

INSERT INTO refaccion VALUES
 (1,'RF-001','Filtro de aire 50% eficiencia', 12, 4),
 (2,'RF-002','Filtro de aceite 50 micras',     3, 4),
 (3,'RF-003','Balero rígido de bolas 50 mm',  25, 8),
 (4,'RF-004','Banda dentada 1200 mm',          0, 2),
 (5,'RF-005','Empaque de vitón',              40, 0),
 (6,'RF-006','Manguera hidráulica 3/8',        7, NULL),
 (7,'RF-007','Válvula solenoide 24 V',         2, 3);

INSERT INTO consumo VALUES
 ( 1,1,2),( 1,3,4),( 2,6,1),( 2,3,2),( 3,1,1),
 ( 4,3,6),( 4,7,1),( 6,2,2),( 6,6,3),( 7,7,1),
 ( 8,1,2),( 8,5,4),( 9,5,2),(10,4,1),(11,3,2);

INSERT INTO certificado VALUES
 (1,1,'CAL-24001','2026-06-30'),
 (2,4,'CAL-24002','2026-04-15'),
 (3,5,'CAL-24003','2026-09-01');
```

Ocho equipos, seis sensores, veinte mediciones de las cuales cinco vienen sin valor, doce órdenes de trabajo y siete refacciones. El equipo 8 está dado de baja y es el único sin criticidad. Los equipos 3 y 6 son subensambles montados dentro de otro equipo. Los sensores 3 y 6 miden la misma magnitud en equipos distintos, y ningún sensor se quedó sin lecturas.

Los esquemas `taller`, `modelo`, `norma`, `planta_ddl`, `tipos`, `dml`, `auto`, `desempeno` y `conc` los construye cada ejercicio donde se necesitan, y sus guiones vienen dentro del enunciado que los pide.
