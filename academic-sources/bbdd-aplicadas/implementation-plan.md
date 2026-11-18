# Plan de implementación — Bases de Datos Aplicada (3641)

Contrato: `reports/content-audit.md` (hallazgos y acciones), `content-guide.md` (reglas y decisiones
D1–D8) y `curriculum-map.yaml` (temas, fuentes y estado). Cada etapa termina con sus criterios de
aceptación verificados y una entrada en el registro (§6).

Sin commits, push, merge ni despliegues sin autorización explícita.

## 1. Etapas

| Etapa | Alcance | Criterios de aceptación |
|---|---|---|
| **E0 · Decisiones** | Registrar D1–D8 en la guía, la matriz y este plan | Hecho (2026-11-17) |
| **E1 · Herramientas** | Verificador de motores (`engines`, `verify-code`) con SQL Server 2022 y MongoDB 7. QA que separa los operadores MongoDB de las fórmulas, con mínimos por unidad, `verificacion: motor\|revisado` y resoluciones completas | Tests del pipeline en verde; la prueba real contra los dos motores pasa; QA de Álgebra II sin cambios; `reports/code-verification.md` generado |
| **E2 · Correcciones transversales** | Portada e índices de unidad: títulos 2024, sin "1er/2do parcial", esquema de evaluación 2024, bibliografía completa. Enlaces "← Unidad" de u5 y u6. Operadores `$` y montos sin formato. Errores verificados de la auditoría §2.2 | `qa` sin `operador-mongodb-sin-codigo` ni `formula-mal-delimitada`; `npm run build`, `npm run validate` y `npm run test:browser` en verde; sin cambios de URL |
| **E3 · Unidad 1** | Reubicar el índice clúster a u3, ampliar los temas superficiales, corregir y verificar el código, ejercicios hasta el mínimo, reemplazar enunciados de cátedra (§3) | Las páginas reescritas no tienen ejemplos pendientes; mínimos de u1 cumplidos con resoluciones completas; `production: redactado` en la matriz; validaciones en verde |
| **E4 · Unidad 2** | Recortar `bd-transaccionales` (lo de u3, u4 y u5 sale de ahí), unificar formatos, conectividad propia, página de bases de sistema, mover la práctica de transacciones a u3 | Ídem; redirecciones y `migration/` actualizadas si una página cambia de ruta |
| **E5 · Unidad 3** | Fusionar las páginas de transacciones; reorganizar índices, plan, estadísticas, optimización, columnstore y monitoreo; corregir los laboratorios | Ídem; los laboratorios de concurrencia figuran como `revisado` (necesitan dos sesiones) con guion reproducible |
| **E6 · Unidad 4** | Resumen integrador en lugar del apunte completo; POO (D4); KDD con Fayyad (D4); upsert, `bulkWrite` y `explain`; prácticas con datos propios | Ídem; los datos de práctica están publicados y son de procedencia propia |
| **E7 · Unidad 5** | Resumen integrador; autenticación y directivas; corrección de alta disponibilidad, cifrado y laboratorios; inyección como complementario | Ídem; la alta disponibilidad (requiere clúster) figura como `revisado` |
| **E8 · Unidad 6** | Reescribir sobre fuentes primarias (D3); complementarios rotulados | Cada afirmación normativa tiene cita a InfoLEG, EUR-Lex o la ficha pública de ISO; las URL de EUR-Lex e iso.org están confirmadas a mano |
| **E9 · Integración** | Revisión cruzada de enlaces, navegación, guías de parcial (esquema 2024), informe final | Todas las validaciones en verde; `content-pipeline qa` sin errores para la materia; informe de cierre |

Orden: E1 → E2 → E3 → E4 → E5 → E6 → E7 → E8 → E9. E3–E5 van en secuencia porque los traslados
fluyen de u1 y u2 hacia u3. E6–E8 podrían paralelizarse.

## 2. Temas fuera del programa o de su unidad (D5)

Numeración de `reports/content-audit.md` §10.

| # | Tema | Decisión | Etapa |
|---|---|---|---|
| 1 | Índice clúster en u1 | **Reubicar** a `u3-indices`. La página de u1 conserva su URL como puente breve (PK clúster por defecto) con enlace a u3 | E3/E5 |
| 2 | SQL dinámico | **Conservar** en u1 (respaldo de cátedra). Corregir el `GO` que pierde variables | E3 |
| 3 | ACID desarrollado, aislamiento, MVCC y WAL en u2 | **Reubicar**: aislamiento y MVCC a `u3-concurrencia`, TCL a `u3-tcl`, WAL a `u5-recuperacion`. En u2 quedan OLTP y ACID conceptual | E4 |
| 4 | Práctica de transacciones en u2 | **Reubicar** a la práctica de u3. La ruta anterior queda como redirección registrada en `migration/` | E4/E5 |
| 5 | Data warehouse, data lake y ETL/ELT en u2 | **Reubicar** a `u4-data-lakes`. En u2 queda una mención con enlace | E4/E6 |
| 6 | Always On en u2 | **Reubicar** a `u5-alta-disponibilidad`. En u2 queda el clúster como arquitectura | E4 |
| 7 | Tablas temporales y variables de tabla | **Conservar** (la presentación de cátedra de u2 las trata) en una sección propia | E4 |
| 8 | In-Memory OLTP en profundidad | **Complementario**, actualizado (FK, NULL y `ALTER TABLE` desde 2016/2017) | E4 |
| 9 | XML y JSON con T-SQL | **Conservar como programa** (`u2-importacion` y `u2-formatos`), con documentación de Microsoft como fuente | E4 |
| 10 | Llamadas HTTP con OLE Automation | **Complementario**, con advertencia de seguridad y `sp_OADestroy`. Figura como `revisado` (requiere red) | E4 |
| 11 | Formatos de intercambio en u2 | **Conservar**; unificar las dos páginas | E4 |
| 12 | Transacciones multidocumento y `readConcern` en MongoDB | **Complementario** | E6 |
| 13 | Gobierno de data lake (zonas, linaje) | **Complementario**, como sección rotulada | E6 |
| 14 | KDD en 7 etapas | **Reemplazar** por las 5 etapas de Fayyad (D4) | E6 |
| 15 | `$expr`, `$text`, `$where`, `$mod`, collation | **Conservar** | E6 |
| 16 | `$graphLookup`, `$redact`, `$setWindowFields`, `$merge` | **Complementario**: mención breve | E6 |
| 17 | `XACT_ABORT`, `THROW` y TRY/CATCH | **Conservar** dentro de `u3-tcl` | E5 |
| 18 | Deadlocks, `system_health` y DMVs | **Conservar**: el programa pide "bloqueos y esperas" | E5 |
| 19 | Modelo de recuperación dentro de u3 | **Conservar** la versión breve de métricas (cátedra u3 p.36–39) con enlace a u5; quitar la copia de `indices-optimizacion` | E5 |
| 20 | Laboratorio `tienda_online` | **Reemplazar**: faltan sus scripts y depende de una API externa | E6 |
| 21 | Integrador de películas y préstamos | **Reescribir** con datos propios publicados | E6 |
| 22 | Inyección SQL | **Complementario** en u5, con la Parte 5 corregida | E7 |
| 23 | Medición y mejora de la calidad | **Complementario** en u6 | E8 |
| 24 | Gobierno de datos y privacidad desde el diseño | **Complementario** en u6 | E8 |
| 25 | Failover Cluster Instance | **Complementario**: sección dentro de alta disponibilidad | E7 |
| 26 | Práctica de alta disponibilidad | **Ampliar**: laboratorio guiado `revisado` (requiere clúster) | E7 |
| 27 | Always Encrypted, HSM y Key Vault | **Complementario**: mención con documentación oficial | E7 |
| 28 | Rótulos "2do parcial" | **Corregir** al esquema 2024 | E2 |

## 3. Enunciados de cátedra ya publicados (D2)

| Página | Origen | Estado | Veredicto |
|---|---|---|---|
| `unidad-1/practica/tp1` | Guía de cátedra TP 1 (2024), 20 consignas reproducidas | Soluciones vacías en 6 y 10–20; errores en 2 y 7 | **Reemplazar** por un TP original equivalente: mismos objetivos (DDL, DML, restricciones, vistas, procedimientos, triggers, CTE, pivot) y nivel, con esquema y datos propios |
| `unidad-1/practica/window-functions` | Guía de cátedra de window functions (v1.0, 2024-03): consignas y datos | Soluciones mayormente correctas; faltan resultados esperados; esquemas inconsistentes | **Reemplazar** por ejercicios originales con datos propios y resultados verificados en motor |
| `unidad-2/practica/tp2` | Guía de cátedra TP 2 (2024) | Contradice la guía en el ej. 2; errores en 8, 10 y 14; supuestos sobre los CSV | **Reemplazar** por un TP original (collation, importación, temporales) con archivos propios publicados |
| `unidad-4/practica/ejercicios` | Mezcla de consignas propias y conjuntos de datos (`datosventas_1.json`, `sample_airbnb`, `cc_info.csv`, `transactions.csv`) | Errores en las consultas 7, 8, 20 y la vista | **Investigar** la procedencia de cada conjunto de datos: `datosventas` coincide con la guía de cátedra 2 de u4 y `sample_airbnb` es el conjunto de ejemplo público de MongoDB. Reemplazar lo que sea de cátedra |
| `unidad-1/practica/pivot` (integrador 1) | Inspirado en un parcial, con datos propios | Resultados verificados a mano | **Conservar** (no es reproducción). Corregir el ej. 5 |

Mientras no se reemplacen, las páginas reproducidas llevan la atribución de `content-guide.md` §6.

## 4. Pista de seguridad (D8), independiente del contenido

| Ítem | Estado | Próximo paso |
|---|---|---|
| Retiro de `MongoDB-Agregaciones-2026.pdf` y `MongoDB-Indices.pdf` de `public/` (`migration/withdrawn.json`, validadores y importador) | Hecho en el árbol de trabajo, sin commit | Commit propio y despliegue **solo con autorización**. Tras desplegar, `node scripts/verify-production.mjs` debe dar 404 en ambas rutas |
| Credencial de Atlas en `Instalación MongoDB.pdf` (`raw/`, excluido con `skip`) | No reproducida en ningún archivo | **Pendiente (persona responsable)**: avisar a la docente titular de la credencial para que la revoque o la cambie. No se registra el valor |

## 5. Infraestructura de verificación (D6)

- **Motores.** SQL Server 2022 (`mcr.microsoft.com/mssql/server`, fijado por digest; amd64 emulado
  en arm64) y MongoDB 7.0 (`mongo`, fijado por digest). Configuración en `subject.yaml` → `engines`.
- **Contenedores.** `bbdda-mssql` y `bbdda-mongo`, sin puertos publicados. Hay un contenedor
  preexistente del usuario (`mssql`) que no se usa ni se modifica.
- **Registros.** `reports/code-verification.md` lista por separado los ejemplos ejecutados, los
  revisados sin ejecución y los pendientes.

## 6. Registro de etapas

| Fecha | Etapa | Resultado |
|---|---|---|
| 2026-11-17 | E1 | Nuevos comandos `content-pipeline engines up\|status\|down` y `verify-code` (`codecheck.py`). Entorno: SQL Server 2022 RTM-CU28 (16.0.4325.4) y MongoDB 7.0.48 en `bbdda-mssql` y `bbdda-mongo`, sin puertos publicados. QA: `textscan.py` separa operadores MongoDB y montos de las fórmulas (`operador-mongodb-sin-codigo`, `monto-con-signo-pesos`); mínimos por unidad; `verificacion: motor\|revisado`; `resolucion-incompleta`; los marcadores `check:` de ejemplos se respaldan con el informe de código o con `reviewed.yaml`. Correcciones: el verificador antepone `SET NOCOUNT ON` en un lote propio, y `validate` resuelve las páginas por `slug`. Tests: 103 aprobados; QA de Álgebra II idéntico antes y después |
| 2026-11-17 | E4 | **Unidad 2.** `bd-transaccionales` pasa a ser "Arquitectura e instalación de un motor relacional" (misma URL). OLTP y ACID conceptual; arquitectura e instalación según cátedra p.9–21. Aislamiento, MVCC y WAL, DWH/data lake y Always On trasladados con puentes y handoffs para E5–E7. Página nueva `bases-de-sistema` (tema ausente). `formatos-conectividad` pasa a conexión, drivers, ODBC y JDBC (misma URL); formatos unificados en `formatos-de-intercambio`. JSON, XML e importación reescritos y verificados con archivos auxiliares. Limitaciones reales de SQL Server 2022 sobre Linux documentadas: `CODEPAGE='65001'` da el error 16202, alternativa `CODEPAGE='RAW'` hacia collation UTF-8. In-Memory OLTP actualizado y verificado en 2022 (FK, NULL, `ALTER TABLE`; `NEXT VALUE FOR` no se admite en módulos nativos), con la parte avanzada como complementaria. APIs como complementario con aviso de seguridad. TP 2 reemplazado por un TP original con CSV propios publicados en `public/.../unidad-2/practica/archivos/tp2/`. **55 ejercicios completos** (18 iniciales, 20 intermedios, 17 avanzados; 50 `motor`, 3 `razonamiento`, 2 `revisado`). 6 pendientes de verificación específica (red, COM de Windows, SQL Server 2025, `CODEPAGE` en Linux, creación de bases y dos sesiones). Validaciones: `verify-code` 211/211, `qa` sin hallazgos en u1–u2, `validate` 0 errores (83 revisiones), build y Playwright 41 en verde. **Archivos nuevos en `public/`** (no registrados en `migration/`, que solo registra lo migrado): `unidad-2/practica/archivos/tp2/*.csv` y cuatro archivos de práctica de importación |
| 2026-11-18 | Publicación | Auditoría de privacidad de los 1.217 cambios: sin credenciales reales (solo contraseñas didácticas o marcadores), sin correos reales y sin documentos privados; los números con forma de DNI son hashes, identificadores o datos sintéticos; se quitó del informe de auditoría un nombre de ejemplo que coincidía con el de un autor. Se retiraron además `window-functions.sql`, `datosventas_1.json`, `cc_info.csv` y `transactions.csv` (6 recursos en `withdrawn.json`), y se eliminó la comprobación `U4.P.20`, que embebía el dataset de cátedra. Se resolvió la advertencia de párrafo duplicado. Playwright verifica que los recursos retirados respondan 404. Validaciones: 454/454, `qa` 0/0, `validate` 0 errores (139 revisiones), build, Playwright 43 y pytest 107. Se consolida todo en una única PR en borrador |
| 2026-11-18 | E5–E9 | **Unidades 3 a 6 e integración.** u3: concurrencia y TCL separadas, rendimiento reorganizado, práctica nueva `rendimiento`, puentes en `unidad-1/teoria/indice-cluster` y `unidad-2/practica/transacciones`. u4: MongoDB reescrito, POO (página nueva), KDD con las 5 etapas de Fayyad, resumen integrador, prácticas con datos propios publicados. u5: autenticación ampliada, permisos, cifrado, log, backups y alta disponibilidad verificados; inyección como complementario. u6: Ley 25.326, RGPD e ISO/IEC 25012 sobre fuentes primarias (InfoLEG, EUR-Lex; ISO solo con atribución a la fuente pública consultada); medición y gobierno como complementarios. Verificador: directiva `-- verify: ignorar-salida` para mensajes informativos no deterministas (`U3.T.CC.19` y `.20` fallaban de forma intermitente). Detalle por unidad en `reports/implementation-report.md`. **Cierre:** 455/455 comprobaciones aprobadas, 0 bloques sin verificar, 30 pendientes de verificación específica, 235 ejercicios completos, `qa` y `validate` sin errores, 137 revisiones encadenadas, build, Playwright 41 y pytest 107 en verde |
| 2026-11-17 | E5 (criterio) | Las dos páginas que cambian de unidad (práctica de transacciones de u2 e índice clúster de u1) se resuelven con **páginas puente**: el contenido pasa a u3 y la URL de origen se conserva con un párrafo y un enlace (content-guide §2). No se cambian slugs ni la matriz de compatibilidad |
| 2026-11-17 | E3 | **Unidad 1.** Reescritas `conceptos-basicos` (clasificación transaccional/no transaccional, características, licencias por motor, despliegue embebido/on premise/cloud; se retiró la cita sin fuente "OpenQube 2025"), `repaso-sql` (NULL como UNKNOWN y `NOT IN` con NULL, tipos de fecha y cadena, FK compuesta coherente, acciones referenciales, subconsultas correlacionadas/EXISTS/ANY/ALL, DML sobre vistas, SCHEMABINDING, procedimientos y triggers coherentes, funciones de tabla), `window-functions` (marcos y ORDER BY, CUME_DIST y PERCENT_RANK correctos, errores del motor documentados), `cte`, `pivot` y `sql-dinamico` (sin el `GO` que perdía variables). Esquema de ejemplo único `ventas`. Prácticas: TP 1 reemplazado por un TP original (biblioteca, U1.01–U1.16), práctica de window functions reemplazada (U1.21–U1.32), práctica de PIVOT corregida (U1.33–U1.41). **37 ejercicios completos, todos `motor`** (12 iniciales, 14 intermedios, 11 avanzados; mínimo 15). 96 comprobaciones de u1 aprobadas; 1 pendiente de verificación específica (`CREATE DATABASE`); 4 plantillas de sintaxis marcadas. Herramientas: archivos auxiliares `ID.files/` con `{{FIXTURES}}`, marcador `<!-- sintaxis -->`, registro de revisiones encadenadas `migration/revisions.json` (`sources.json` restaurado intacto) y `scripts/register-revisions.mjs`. Prueba de Playwright de descargas adaptada: `window-functions.sql` ya no se enlaza (D2), pero su URL sigue sirviendo los bytes originales. Validaciones: pytest 106, `verify-code` 98/98, `qa` sin hallazgos en u1, `validate` 0 errores (66 revisiones encadenadas), build y Playwright 41 en verde. **Pendiente de decisión:** `public/bbdd-aplicadas/unidad-1/practica/window-functions.sql` contiene datos de la práctica de cátedra reemplazada (¿retirarlo como los PDF?); 4 imágenes de u1 (`wf-*.png`, `pivot*.png`) quedaron sin referencia (se conservan) |
| 2026-11-17 | E2 | Portada e índices con títulos y evaluación 2024, sin "1er/2do parcial" y con bibliografía completa (Gils Carbó; recursos obligatorios y complementarios separados). Guías de u5 y u6 rebautizadas "de repaso", con nota de evaluación. 21 enlaces "← Unidad" de u5 y u6 y 23 enlaces a `/unidad-N/` apuntan ahora a la teoría de la unidad. Operadores `$` con formato de código y montos en pesos: 0 fórmulas espurias en `dist/`. Errores verificados de la auditoría §2.2: Parte 5 de inyección reescrita con evidencia (`U5.LI.P5`: el procedimiento dinámico da error 229 y se remedia con firma de módulo; un `DENY` lo bloquea igual); tabla de `XACT_ABORT` reemplazada por la medida (`U3.XA.01`); consulta 20 de MongoDB corregida (`U4.P.20`: 0 → 4 documentos; el bloque de la página sigue pendiente porque tiene 20 consultas); alta disponibilidad (`SESSION_TIMEOUT`) en dos páginas; avisos en las dos prácticas de u4 sin datos. `migratedSha256` actualizado para 64 salidas de BBDD. Validaciones: `qa` sin errores de fórmulas ni operadores (solo mínimos y temas sin redactar, esperables); `npm run build`, `npm run validate` (0 errores) y `npm run test:browser` (41 aprobados) en verde. Código: 3 comprobaciones ejecutadas y aprobadas; 574 bloques pendientes (línea de base) |
| 2026-11-17 | E0 | Decisiones D1–D8 registradas en `content-guide.md` §0, `curriculum-map.yaml` → `decisions` y este plan. Mínimos por unidad y alcance de POO y KDD en la matriz. Fuentes de u6: InfoLEG y el resumen de iso25000.com verificados; EUR-Lex e iso.org pendientes de confirmación manual (bloquean clientes automatizados) |
