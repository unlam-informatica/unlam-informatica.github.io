---
title: Unidad 1 — Conceptos básicos
description: "Fundamentos de bases de datos y DBMS, repaso de SQL y SQL avanzado de T-SQL (window functions, CTE, PIVOT y SQL dinámico)."
slug: bbdd-aplicadas/unidad-1/teoria
sidebar:
  hidden: true
  label: Presentación y ruta
---
Esta unidad fija qué es una base de datos y un DBMS, repasa el SQL que se trae de Bases de Datos y de programación (DDL, DML, restricciones, NULL, consultas, vistas, procedimientos, triggers y funciones) y lo extiende con window functions, CTE, PIVOT y SQL dinámico. Es la base de las unidades siguientes: todas suponen que manejás este SQL.

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- Definir base de datos y DBMS, justificar su uso frente a archivos y clasificar las bases de datos en transaccionales y no transaccionales con ejemplos.
- Elegir un motor según su licencia y su despliegue (embebido, on premise o cloud) y distinguir las tareas del DBA y del programador.
- Crear esquemas, tablas y restricciones, cargar y consultar datos, y razonar con NULL y lógica de tres valores.
- Escribir subconsultas, funciones de agregado y vistas, y encapsular lógica en procedimientos almacenados, triggers y funciones de usuario.
- Resolver con window functions, CTE y PIVOT/UNPIVOT problemas de ranking, acumulados, jerarquías y reportes.
- Armar sentencias con SQL dinámico sin exponerse a la inyección SQL.

## Antes de comenzar

- **Conviene repasar:** lo visto en Bases de Datos (modelo relacional, claves, `SELECT` y `JOIN`) y los conceptos básicos de programación. La lección [Repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/) cubre lo que haga falta.
- **Herramientas:** SQL Server 2019 o 2022 y una base de prueba vacía. Ver [Cómo estudiar · Herramientas](/bbdd-aplicadas/como-estudiar/#herramientas).

## Ruta de aprendizaje

Seguí las etapas en orden. Cada una indica qué leer y, cuando existe, qué practicar antes de pasar a la siguiente.

### 1. Fundamentos de bases de datos y DBMS

Fija el vocabulario de toda la materia: qué es una base de datos y un DBMS, cómo se clasifican, cuándo conviene usar un DBMS y cómo elegir un motor.

- **Leé:** [Conceptos básicos](/bbdd-aplicadas/unidad-1/teoria/conceptos-basicos/)
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-1/teoria/conceptos-basicos/#autoevaluación)

### 2. Repaso de SQL

Recorre DDL, DML, integridad referencial, NULL, consultas, subconsultas, vistas, procedimientos, triggers y funciones sobre un único dominio de ejemplo.

- **Leé:** [Repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/)
- **Practicá:** [Trabajo Práctico 1 — Repaso de SQL](/bbdd-aplicadas/unidad-1/practica/tp1/) (16 ejercicios). Resolvé los ejercicios 1 a 3, 5 a 10 y 12 a 14 ahora. Los ejercicios 4, 11, 15 y 16 usan CTE, PIVOT y window functions (según los presupuestos del propio TP): dejalos para las etapas 3, 4 y 5.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/#autoevaluación)

### 3. Window functions

Calculan un valor por fila a partir de un conjunto de filas relacionadas, sin colapsar el resultado como `GROUP BY`. La lección define el esquema `ventas` que usan también CTE, PIVOT y SQL dinámico.

- **Leé:** [Window Functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/)
- **Practicá:** [Práctica — Window Functions](/bbdd-aplicadas/unidad-1/practica/window-functions/) (12 ejercicios). Los ejercicios 4 y 10 presuponen CTE: volvé a ellos después de la etapa 4. Del TP 1, el ejercicio 16 combina CTE y ranking.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-1/teoria/window-functions/#autoevaluación)

### 4. Common Table Expressions

Dan nombre a un paso intermedio, permiten filtrar por el resultado de una función de ventana y recorrer jerarquías.

- **Leé:** [Common Table Expressions](/bbdd-aplicadas/unidad-1/teoria/cte/)
- **Practicá:** ejercicios 4, 15 y 16 del [TP 1](/bbdd-aplicadas/unidad-1/practica/tp1/), y los ejercicios 4 y 10 de la [Práctica — Window Functions](/bbdd-aplicadas/unidad-1/practica/window-functions/).
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-1/teoria/cte/#autoevaluación)

### 5. PIVOT y UNPIVOT

Convierten valores de una columna en columnas y el camino inverso, para reportes y comparaciones.

- **Leé:** [PIVOT](/bbdd-aplicadas/unidad-1/teoria/pivot/). La sección [PIVOT dinámico](/bbdd-aplicadas/unidad-1/teoria/pivot/#pivot-dinámico) se apoya en SQL dinámico: leela de corrido y volvé a ella después de la etapa 6.
- **Practicá:** [Práctica — PIVOT](/bbdd-aplicadas/unidad-1/practica/pivot/) (9 ejercicios). El ejercicio 5 (PIVOT dinámico) presupone SQL dinámico: resolvelo después de la etapa 6. Del TP 1, el ejercicio 11.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-1/teoria/pivot/#autoevaluación)

### 6. SQL dinámico

Arma una sentencia como cadena de texto y la ejecuta en tiempo de ejecución; es potente y abre la puerta a la inyección SQL si se arma con datos externos.

- **Leé:** [SQL Dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/)
- **Practicá:** ejercicio 5 de la [Práctica — PIVOT](/bbdd-aplicadas/unidad-1/practica/pivot/).
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/#autoevaluación)

### 7. Integración y autoevaluación

Volvé sobre los ejercicios que dejaste pendientes (TP 1: 4, 11, 15 y 16; Window Functions: 4 y 10; PIVOT: 5) y resolvelos sin mirar la resolución.

## Ejercicios y laboratorios

- **[Trabajo Práctico 1 — Repaso de SQL](/bbdd-aplicadas/unidad-1/practica/tp1/)** · 16 ejercicios — repaso integral sobre una biblioteca comunal.
- **[Práctica — Window Functions](/bbdd-aplicadas/unidad-1/practica/window-functions/)** · 12 ejercicios — ranking, particiones, `LAG`/`LEAD`, marcos y percentiles.
- **[Práctica — PIVOT](/bbdd-aplicadas/unidad-1/practica/pivot/)** · 9 ejercicios — PIVOT, UNPIVOT y PIVOT dinámico.

Ver el [índice de prácticas](/bbdd-aplicadas/unidad-1/practica/).

## Autoevaluación y repaso

Cada lección termina con una autoevaluación (enlazadas en la ruta) y un «En resumen» cuando corresponde. La unidad no tiene resumen integrador ni guía de examen: el repaso son esas autoevaluaciones y las prácticas.

## Continuar

Cuando puedas resolver las prácticas de la unidad sin mirar la resolución, seguí con la [Unidad 2 — Bases de datos relacionales: aspectos básicos](/bbdd-aplicadas/unidad-2/teoria/).

:::note[Páginas trasladadas]
[Índice Clustered](/bbdd-aplicadas/unidad-1/teoria/indice-cluster/) se conserva para no romper enlaces antiguos: el tema pertenece a la Unidad 3 y se estudia en [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/).
:::
