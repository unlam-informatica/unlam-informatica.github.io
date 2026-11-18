---
title: Unidad 5 — Protección de los datos
slug: bbdd-aplicadas/unidad-5/teoria
description: "Seguridad y acceso, recuperación y disponibilidad en SQL Server: ruta de estudio, laboratorios y repaso para el trabajo práctico y el final."
sidebar:
  hidden: true
  label: Presentación y ruta
---

Esta unidad estudia cómo se protege una base de datos relacional frente a accesos indebidos, fallas y desastres: quién puede hacer qué, cómo se recupera un dato tras una caída o un error y cómo se reduce la interrupción del servicio. Continúa lo visto en la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/) sobre transacciones: el registro de transacciones que sostiene la atomicidad y la durabilidad es la base de los backups y de la alta disponibilidad. Los ejemplos se ejecutan en SQL Server.

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- reducir la superficie de ataque y diseñar accesos con el principio del mínimo privilegio;
- diferenciar login, usuario, rol, esquema, propietario, permiso y elemento protegible;
- diagnosticar el registro de transacciones y seleccionar un modelo de recuperación;
- definir y probar una estrategia de backup y restauración según RPO y RTO;
- elegir entre Availability Groups, Failover Cluster Instance, replicación y log shipping;
- proteger datos en reposo y en tránsito, y prevenir inyección SQL.

## Antes de comenzar

- **Conviene repasar:** [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/) y el [repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/); para la inyección SQL, [SQL dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/).
- **Herramientas:** una instancia de SQL Server de laboratorio (los ejemplos se ejecutaron en SQL Server 2022 sobre Linux) y un cliente como SSMS o Visual Studio Code con la extensión MSSQL. Más opciones en [Cómo estudiar · Herramientas](/bbdd-aplicadas/como-estudiar/#herramientas). Los laboratorios crean logins y restauran bases: usá solo instancias de laboratorio.

## Ruta de aprendizaje

Seguí las etapas en orden. Cada una indica qué leer y, cuando existe, qué practicar antes de pasar a la siguiente. El [resumen integrador](/bbdd-aplicadas/unidad-5/teoria/apunte-completo/) sirve como vista general antes de empezar. La unidad tiene tres bloques: seguridad y acceso, recuperación y disponibilidad.

### Bloque 1 · Seguridad y acceso

#### 1. Seguridad, usuarios y permisos

Mínimo privilegio, autenticación y directivas de contraseñas, permisos (`GRANT`, `DENY`, `REVOKE`), roles, propietarios y encadenamiento de propiedad.

- **Leé:** [Seguridad, usuarios y permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/)
- **Practicá:** [Laboratorio — Seguridad, roles y permisos](/bbdd-aplicadas/unidad-5/practica/laboratorio-seguridad/): partes 1 a 7 y ejercicios 1 a 8.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/#autoevaluación)

#### 2. Cifrado en reposo y en tránsito

Cifrado de columnas, jerarquía de claves, TDE y TLS; la custodia de las claves es el problema central.

- **Leé:** [Cifrado en reposo y en tránsito](/bbdd-aplicadas/unidad-5/teoria/cifrado/)
- **Practicá:** ejercicios 10 a 12, dentro de la misma lección.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-5/teoria/cifrado/#autoevaluación)

:::note[Cifrado y copias de seguridad]
La lección se puede leer sin haber estudiado backups. Las secciones [TDE](/bbdd-aplicadas/unidad-5/teoria/cifrado/#tde-cifrado-transparente-de-la-base) y [Cifrado de respaldo](/bbdd-aplicadas/unidad-5/teoria/cifrado/#cifrado-de-respaldo) hablan de respaldar el certificado y de cifrar un backup: conviene releerlas después de la etapa 5.
:::

#### 3. Inyección SQL y programación segura (complementario)

*Complementario: no forma parte del programa 2024; podés saltearlo en una primera lectura.* Cómo evitar que un dato se ejecute como código: parámetros, listas permitidas y mínimo privilegio.

- **Leé:** [Inyección SQL y programación segura](/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql/)
- **Practicá:** [Laboratorio defensivo — Inyección SQL](/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion/) (complementario): partes 1 a 6 y ejercicios 13 a 15.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql/#autoevaluación)

### Bloque 2 · Recuperación

#### 4. Registro de transacciones y modelos de recuperación

Cómo sobrevive un dato a una caída, por qué crece el log y qué diferencia hay entre los modelos `SIMPLE`, `FULL` y `BULK_LOGGED`.

- **Leé:** [Registro de transacciones y modelos de recuperación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/)
- **Practicá:** del [laboratorio de backup](/bbdd-aplicadas/unidad-5/practica/laboratorio-backup/), los ejercicios 21, 23 y 37.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/#autoevaluación)

#### 5. Backups, restauración, RPO y RTO

Tipos de backup, orden de restauración, recuperación a un punto en el tiempo y diseño de la estrategia desde el RPO y el RTO. Presupone la etapa anterior.

- **Leé:** [Backups, restauración, RPO y RTO](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/)
- **Practicá:** [Laboratorio — Cadena de backup y restauración](/bbdd-aplicadas/unidad-5/practica/laboratorio-backup/): los pasos 1 a 10 y los ejercicios 22, 26 a 33 y 36.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/#autoevaluación)

### Bloque 3 · Disponibilidad

#### 6. Alta disponibilidad, replicación y recuperación ante desastres

Grupos de disponibilidad, replicación, log shipping y FCI (complementario); qué falla tolera cada herramienta y por qué ninguna reemplaza al backup. Presupone los dos temas del bloque anterior.

- **Leé:** [Alta disponibilidad, replicación y recuperación ante desastres](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/)
- **Practicá:** del [laboratorio de backup](/bbdd-aplicadas/unidad-5/practica/laboratorio-backup/), los ejercicios 24, 25, 34 y 35.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/#autoevaluación)

:::caution[Lo que requiere un clúster]
El [laboratorio guiado de un grupo de disponibilidad de dos nodos](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/#laboratorio-guiado-grupo-de-disponibilidad-de-dos-nodos) necesita dos instancias que se vean entre sí: queda como pendiente de verificación específica del portal: está revisado, no verificado. Lo que sí se comprobó es lo que la lección indica en cada ejemplo.
:::

## Ejercicios y laboratorios

- **[Laboratorio — Seguridad, roles y permisos](/bbdd-aplicadas/unidad-5/practica/laboratorio-seguridad/)** · 8 ejercicios — logins, roles, vistas, procedimientos, `REVOKE` frente a `DENY` y delegación.
- **[Laboratorio defensivo — Inyección SQL](/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion/)** (complementario) · 3 ejercicios — concatenación frente a parámetros, listas permitidas y mínimo privilegio.
- **[Laboratorio — Cadena de backup y restauración](/bbdd-aplicadas/unidad-5/practica/laboratorio-backup/)** · 17 ejercicios — cadena completo, diferencial y log, restore a otra base, recuperación a un punto, log y alta disponibilidad.

Detalle en el [índice de prácticas](/bbdd-aplicadas/unidad-5/practica/).

## Autoevaluación y repaso

- Cada lección termina con una autoevaluación, enlazada en la ruta.
- El [resumen integrador](/bbdd-aplicadas/unidad-5/teoria/apunte-completo/) es una vista general antes de empezar y un repaso después; cada sección enlaza a su lección.
- La [guía de repaso](/bbdd-aplicadas/unidad-5/teoria/guia-parcial/) prepara el trabajo práctico integrador y el examen final: según el programa 2024, esta unidad no integra el parcial.

## Continuar

Cuando puedas diseñar los permisos de un escenario, explicar una restauración paso a paso y elegir una herramienta de disponibilidad según RPO y RTO sin mirar la resolución, seguí con la [Unidad 6 — Calidad en bases de datos](/bbdd-aplicadas/unidad-6/teoria/), que retoma el mínimo privilegio y la seguridad desde el punto de vista normativo.
