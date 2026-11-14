---
title: Unidad 5 — Teoría
slug: bbdd-aplicadas/unidad-5/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 5.

## Protección de los datos · 2do parcial

Seguridad y protección, mínimo privilegio, principals y securables, DCL, roles, registro de transacciones, modelos de recuperación, backups, restauración, RPO/RTO, alta disponibilidad, replicación, log shipping, cifrado e inyección SQL.

### Resultados de aprendizaje

Al finalizar la unidad deberías poder:

- reducir la superficie de ataque y diseñar accesos con el principio del mínimo privilegio;
- diferenciar login, usuario, rol, esquema, propietario, permiso y elemento protegible;
- diagnosticar el registro de transacciones y seleccionar un modelo de recuperación;
- definir y probar una estrategia de backup y restauración según RPO y RTO;
- elegir entre Availability Groups, Failover Cluster Instance, replicación y log shipping;
- proteger datos en reposo y en tránsito, y prevenir inyección SQL.


## Teoría

| Apunte | Tema |
|---------|------|
| [Unidad 5 — Protección de los datos](/bbdd-aplicadas/unidad-5/teoria/apunte-completo/) | Desarrollo integral de todos los contenidos de la unidad |
| [Seguridad, usuarios y permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/) | POLP, principals, securables, login/usuario, roles, DCL, propietarios y ownership chaining |
| [Registro de transacciones y modelos de recuperación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/) | WAL, LDF, VLF, LSN, truncamiento, crecimiento y modelos SIMPLE/FULL/BULK_LOGGED |
| [Backups, restauración, RPO y RTO](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/) | Full, diferencial, log, tail-log, copy-only, 3-2-1, RPO/RTO y secuencias de restore |
| [Alta disponibilidad, replicación y recuperación ante desastres](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/) | Availability Groups, FCI, replicación, log shipping, HA y DR |
| [Cifrado en reposo y en tránsito](/bbdd-aplicadas/unidad-5/teoria/cifrado/) | Cifrado en reposo y tránsito, TDE, claves, certificados y cifrado de columnas |
| [Inyección SQL y programación segura](/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql/) | Vectores, impacto, consultas parametrizadas, `sp_executesql` y defensa en profundidad |
| [Guía para el parcial — Unidad 5](/bbdd-aplicadas/unidad-5/teoria/guia-parcial/) | Comparaciones clave, preguntas de desarrollo, errores frecuentes y simulacro |


## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-5/practica/).
