---
title: Unidad 5
slug: bbdd-aplicadas/unidad-5
sidebar:
  order: 6
---

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

| Archivo | Tema |
|---------|------|
| [apunte-completo](/bbdd-aplicadas/unidad-5/teoria/apunte-completo/) | Desarrollo integral de todos los contenidos de la unidad |
| [seguridad-permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/) | POLP, principals, securables, login/usuario, roles, DCL, propietarios y ownership chaining |
| [log-recuperacion](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/) | WAL, LDF, VLF, LSN, truncamiento, crecimiento y modelos SIMPLE/FULL/BULK_LOGGED |
| [backup-restauracion](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/) | Full, diferencial, log, tail-log, copy-only, 3-2-1, RPO/RTO y secuencias de restore |
| [alta-disponibilidad](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/) | Availability Groups, FCI, replicación, log shipping, HA y DR |
| [cifrado](/bbdd-aplicadas/unidad-5/teoria/cifrado/) | Cifrado en reposo y tránsito, TDE, claves, certificados y cifrado de columnas |
| [inyeccion-sql](/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql/) | Vectores, impacto, consultas parametrizadas, `sp_executesql` y defensa en profundidad |
| [guia-parcial](/bbdd-aplicadas/unidad-5/teoria/guia-parcial/) | Comparaciones clave, preguntas de desarrollo, errores frecuentes y simulacro |

## Práctica

| Archivo | Tema |
|---------|------|
| [laboratorio-seguridad](/bbdd-aplicadas/unidad-5/practica/laboratorio-seguridad/) | Login, usuarios, roles, DCL, esquema, vista, procedimiento y permisos efectivos |
| [laboratorio-backup](/bbdd-aplicadas/unidad-5/practica/laboratorio-backup/) | Cadena full/diferencial/log, restore a otra base y recuperación a un punto en el tiempo |
| [laboratorio-inyeccion](/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion/) | Comparación controlada entre concatenación vulnerable y parametrización segura |

**Ruta sugerida:** apunte completo → guías temáticas → laboratorios → guía para el parcial.
