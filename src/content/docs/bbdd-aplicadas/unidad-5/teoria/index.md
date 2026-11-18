---
title: Unidad 5 — Teoría
slug: bbdd-aplicadas/unidad-5/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 5.

## Protección de los datos

Seguridad y protección, mínimo privilegio, autenticación y directivas de contraseña, principals y securables, DCL, roles, registro de transacciones, modelos de recuperación, backups, restauración, RPO/RTO, alta disponibilidad, replicación, log shipping, cifrado e inyección SQL.

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
| [Unidad 5 — Protección de los datos](/bbdd-aplicadas/unidad-5/teoria/apunte-completo/) | Resumen integrador con enlaces a cada tema |
| [Seguridad, usuarios y permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/) | Mínimo privilegio, autenticación y directivas de contraseñas, permisos (`GRANT`, `DENY`, `REVOKE`), roles, propietarios y encadenamiento de propiedad, con ejemplos verificados en SQL Server 2022 |
| [Registro de transacciones y modelos de recuperación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/) | WAL, REDO/UNDO, buffer pool, VLF, LSN, truncamiento, `log_reuse_wait_desc` y modelos SIMPLE/FULL/BULK_LOGGED |
| [Backups, restauración, RPO y RTO](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/) | Full, diferencial (acumulativo), log, tail-log, copy-only, `STOPAT` y marcas, 3-2-1, RPO/RTO y orden de restauración |
| [Alta disponibilidad, replicación y recuperación ante desastres](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/) | Grupos de disponibilidad (Always On), replicación, log shipping, FCI (complementario), HA y DR |
| [Cifrado en reposo y en tránsito](/bbdd-aplicadas/unidad-5/teoria/cifrado/) | Cifrado de columnas, jerarquía de claves, TDE y TLS; Always Encrypted y Key Vault como contenido complementario |
| [Inyección SQL y programación segura](/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql/) · Complementario | Parámetros, listas permitidas y mínimo privilegio (no está en el programa 2024) |
| [Guía de repaso — Unidad 5](/bbdd-aplicadas/unidad-5/teoria/guia-parcial/) | Comparaciones clave, ejercicios propios, errores frecuentes y simulacro con pauta |


## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-5/practica/).
