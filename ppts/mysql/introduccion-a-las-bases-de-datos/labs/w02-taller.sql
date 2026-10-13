-- Fictional practice data verified on MySQL 26.7.0, 2026-10-13.
-- Run in a fresh database. No original measured server data are included.
CREATE DATABASE taller_w02;
USE taller_w02;
CREATE TABLE alumno(matricula CHAR(9) PRIMARY KEY,nombre VARCHAR(80),correo VARCHAR(120) UNIQUE,creditos INT,CONSTRAINT ck_alumno_creditos CHECK(creditos BETWEEN 0 AND 500));

CREATE TABLE materia(clave CHAR(6) PRIMARY KEY,nombre VARCHAR(80));

CREATE TABLE inscripcion(matricula CHAR(9),clave CHAR(6),periodo CHAR(5),calificacion DECIMAL(4,2),PRIMARY KEY(matricula,clave,periodo),CONSTRAINT fk_ins_alumno FOREIGN KEY(matricula) REFERENCES alumno(matricula),CONSTRAINT fk_ins_materia FOREIGN KEY(clave) REFERENCES materia(clave));

CREATE TABLE bitacora_alumno(id INT PRIMARY KEY AUTO_INCREMENT,matricula CHAR(9),creditos_antes INT,creditos_despues INT,cuando DATETIME);

INSERT INTO alumno VALUES('A0000001','Ana','ana@up.edu.mx',135),('A0000002','Beto','beto@up.edu.mx',60),('A0000003','Carla','carla@up.edu.mx',30);

INSERT INTO materia VALUES('BD1001','Bases de Datos'),('FI1010','Fisica'),('MAT201','Calculo');

INSERT INTO inscripcion VALUES('A0000001','BD1001','26PRI',8),('A0000002','BD1001','26PRI',9),('A0000003','FI1010','26PRI',9),('A0000001','FI1010','26PRI',8),('A0000002','FI1010','26PRI',8),('A0000001','MAT201','26PRI',8),('A0000003','MAT201','26PRI',NULL);

CREATE VIEW v_alumno_activo AS SELECT matricula,nombre,correo,creditos FROM alumno WHERE creditos>0;

CREATE VIEW v_creditos_por_materia AS SELECT clave,COUNT(*) inscritos FROM inscripcion GROUP BY clave;

CREATE TRIGGER trg_alumno_after_update AFTER UPDATE ON alumno FOR EACH ROW INSERT INTO bitacora_alumno(matricula,creditos_antes,creditos_despues,cuando) VALUES(OLD.matricula,OLD.creditos,NEW.creditos,NOW());

CREATE EVENT ev_purga_inscripciones ON SCHEDULE EVERY 1 DAY DO DELETE FROM inscripcion WHERE periodo='00000';

SELECT 'TABLE' objeto,COUNT(*) n FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_TYPE='BASE TABLE';
SELECT 'VIEW' objeto,COUNT(*) n FROM information_schema.VIEWS WHERE TABLE_SCHEMA=DATABASE();
SELECT 'TRIGGER' objeto,COUNT(*) n FROM information_schema.TRIGGERS WHERE TRIGGER_SCHEMA=DATABASE();
SELECT 'EVENT' objeto,COUNT(*) n FROM information_schema.EVENTS WHERE EVENT_SCHEMA=DATABASE();
SELECT 'PROCEDURE/FUNCTION' objeto,COUNT(*) n FROM information_schema.ROUTINES WHERE ROUTINE_SCHEMA=DATABASE();
SELECT 'CONSTRAINT' objeto,COUNT(*) n FROM information_schema.TABLE_CONSTRAINTS WHERE CONSTRAINT_SCHEMA=DATABASE();
SELECT 'INDEX' objeto,COUNT(DISTINCT TABLE_NAME,INDEX_NAME) n FROM information_schema.STATISTICS WHERE TABLE_SCHEMA=DATABASE();
