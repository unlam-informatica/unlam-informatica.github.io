# Informe de implementación — Bases de Datos Aplicada (3641)

Fecha: 2026-11-17/18 · Etapas E0–E9 de `../implementation-plan.md`.

El contrato de trabajo fue `content-audit.md`, más `../content-guide.md` (decisiones D1–D8) y
`../curriculum-map.yaml`. No se hicieron commits, push, merge ni despliegue. No se modificaron
`raw/`, los materiales privados ni Álgebra II.

## 1. Resultado global

| Indicador | Valor |
|---|---|
| Páginas de la materia | 82: 79 existentes, todas revisadas, y 3 nuevas (`unidad-2/teoria/bases-de-sistema`, `unidad-3/practica/rendimiento`, `unidad-4/teoria/poo-y-bases`). Ninguna URL cambió ni se eliminó |
| Temas del programa 2024 | 53, todos con `production: redactado`. `validation`: 36 `verificado`, 13 `con-observaciones` (tienen ítems pendientes de verificación específica), 4 `revisado` (conceptuales, sin código) |
| Comprobaciones de código | **454 ejecutadas, 454 aprobadas** (SQL Server 2022: 392; MongoDB 7: 62). 0 bloques sin verificar en las páginas |
| Pendientes de verificación específica | 30 (dos o tres sesiones concurrentes, clúster o alta disponibilidad, red externa, COM de Windows, SQL Server 2025, `CREATE DATABASE`, objetos de servidor que no se pueden limpiar de forma segura). **No cuentan como verificados** |
| Plantillas de sintaxis | 24 bloques `<!-- sintaxis -->`, ninguno sospechoso |
| Ejercicios | **235 con resolución completa**: 185 `motor`, 43 `razonamiento`, 7 `revisado`. Todas las unidades superan su mínimo y su mínimo por nivel |
| `content-pipeline qa` | 0 errores, 0 advertencias |
| `content-pipeline validate` | 0 errores |
| Tests Python (`pytest -m "not integration"`) | 107 aprobados (más el test de integración con Docker real del verificador) |
| `npm run build` / `npm run validate` / Playwright | Correcto / 0 errores (261 rutas, 139 revisiones encadenadas, 44 recursos publicados y 6 retirados) / 43 aprobados (incluye: los recursos retirados responden 404) |

## 2. Infraestructura y correcciones críticas (E1–E2)

### Motores detectados

| Motor | Imagen (digest fijado en `subject.yaml`) | Versión comprobada | Ejecución |
|---|---|---|---|
| SQL Server 2022 | `mcr.microsoft.com/mssql/server@sha256:4525e3ef…` | 16.0.4325.4 (RTM-CU28), Developer | Imagen **amd64 emulada** en el Mac arm64 (Docker Desktop). Arranca y responde; se comprobó con ejecución real, no se supuso |
| MongoDB 7 | `mongo@sha256:884c055b…` (multiarquitectura) | 7.0.48, mongosh 2.14.2 | Nativo arm64 |

- **Contenedores.** `bbdda-mssql` y `bbdda-mongo` no publican puertos. La contraseña de SA es aleatoria y vive solo en el entorno del contenedor.
- **Aislamiento.** Cada comprobación corre en una base de prueba nueva (`chk_<id>`) que se elimina al terminar. Los objetos de servidor (logins, certificados, backups) llevan nombres únicos y se limpian.
- **Contenedor del usuario.** El contenedor `mssql` preexistente no se tocó.
- **Conexiones externas.** No hubo conexiones a servidores de cátedra ni de producción.

### Herramientas

| Componente | Qué hace |
|---|---|
| `content-pipeline engines up\|status\|down` y `verify-code` | Ejecuta `checks/sql/<ID>.sql` y `checks/mongo/<ID>.js` y compara con `<ID>.expected`. Admite archivos auxiliares `<ID>.files/` (`{{FIXTURES}}`) y la directiva `-- verify: ignorar-salida <regex>` para mensajes informativos no deterministas. Separa en tres registros los bloques ejecutados, los **pendientes de verificación específica** (`checks/reviewed.yaml`, nunca cuentan como verificados) y los pendientes, y cuenta aparte las plantillas `<!-- sintaxis -->` |
| `textscan.py` + `qa` | Distingue operadores MongoDB, montos y fórmulas KaTeX (`operador-mongodb-sin-codigo`, `monto-con-signo-pesos`, `formula-mal-delimitada`). QA de Álgebra II idéntico antes y después |
| `qa` (ejercicios) | `verificacion: motor\|revisado\|razonamiento`, resolución completa obligatoria, mínimos por unidad (`minimum_exercises`, `minimum_per_level`) |
| `migration/revisions.json` + `scripts/register-revisions.mjs` | Cadena de hashes por página (`from → to`, fecha, etapa, motivo). **`sources.json` queda intacto** como evidencia histórica, y `npm run validate` sigue fallando ante cualquier edición no registrada |
| `migration/withdrawn.json` | Retiro de seis recursos públicos con procedencia conservada: dos PDF de cátedra, `window-functions.sql` y `datosventas_1.json` (material de cátedra) y `cc_info.csv` y `transactions.csv` (procedencia no documentada). Sin dependencias activas |

### Errores críticos corregidos (content-audit §2.2)

| Hallazgo | Corrección | Evidencia |
|---|---|---|
| Laboratorio de inyección, Parte 5 | El SQL dinámico da error 229 sin `SELECT`; se remedia con firma de módulo; un `DENY` bloquea aun firmado | `U5.LI.P5` |
| Tabla de `XACT_ABORT` | Reemplazada por la medida: con `OFF`, una restricción o un desbordamiento solo terminan la sentencia; una conversión condena la transacción | `U3.XA.01` |
| Consulta MongoDB 20 | `producto.dolar` (0 → 4 documentos) | `U4.P.20` |
| Alta disponibilidad | `SESSION_TIMEOUT`: el primario pasa a confirmación asíncrona para esa réplica (cátedra y Microsoft) | Revisión documental |
| Fórmulas mal renderizadas | Operadores con formato de código y montos en pesos: 0 fórmulas espurias | `dist/` sin anotaciones TeX espurias |
| Datos de práctica inexistentes | Prácticas de u4 reescritas con datos propios publicados | 30 comprobaciones de u4 |
| Enlaces de u5 y u6 | 21 enlaces "← Unidad" y 23 enlaces a `/unidad-N/` corregidos | `qa` sin `enlace-roto` |

## 3. Informe por unidad

### Unidad 1 — Conceptos básicos (E3)

- **Temas:** los 14 temas de u1. 9 `verificado`, 1 `con-observaciones` (`CREATE DATABASE ... COLLATE`) y 4 `revisado` (conceptos, motores y licencias, DBA, despliegue: conceptuales).
- **Páginas:**
  - Reescritas: `conceptos-basicos`, `repaso-sql`, `window-functions`, `cte`, `pivot`, `sql-dinamico` (teoría) y `tp1`, `window-functions`, `pivot` (práctica).
  - `indice-cluster` pasa a ser puente hacia u3.
  - Se actualizaron los índices.
- **Errores corregidos:**
  - `NULL = NULL` evalúa a UNKNOWN, y `NOT IN` con NULL devuelve vacío.
  - La FK compuesta era incoherente.
  - El procedimiento no coincidía con su tabla.
  - DML sobre vistas de varias tablas.
  - Marcos `ROWS`/`RANGE` sin `ORDER BY` (errores 10756, 4112 y otros, medidos).
  - Fórmulas de `CUME_DIST` y `PERCENT_RANK`.
  - El `GO` que perdía variables en el PIVOT dinámico.
  - `STRING_AGG` sin `WITHIN GROUP`.
  - Tres nombres de esquema distintos para los mismos ejemplos.
  - Una cita sin fuente ("OpenQube 2025").
- **Ampliaciones:** clasificación transaccional/no transaccional, licencias por motor, despliegue embebido/on premise/cloud, tipos de fecha y cadena, acciones referenciales, subconsultas correlacionadas y `EXISTS`/`ANY`/`ALL`, funciones de tabla, `MERGE`.
- **Ejercicios:** 37 (12 iniciales, 14 intermedios, 11 avanzados), todos `motor`. El TP 1 y la práctica de window functions son **originales**: reemplazan reproducciones de guías de cátedra (D2).
- **Verificación:** 95 comprobaciones en SQL Server 2022.
- **Fuentes:** presentaciones de cátedra de u1, parte 1 (p.3–14) y parte 2 (p.4–51); documentación de Microsoft.

### Unidad 2 — Bases de datos relacionales: aspectos básicos (E4)

- **Temas:** los 9 temas de u2. 6 `verificado` y 3 `con-observaciones`:
  - collation: bases con otra collation y dos sesiones;
  - importación: `CODEPAGE='65001'` no se admite en SQL Server sobre Linux;
  - APIs: red, COM de Windows y SQL Server 2025.
- **Páginas:**
  - `bd-transaccionales` pasa a ser "Arquitectura e instalación de un motor relacional", con la misma URL. Su contenido de u3, u4 y u5 se trasladó.
  - Página nueva `bases-de-sistema`.
  - `formatos-conectividad` pasa a conexión, drivers, ODBC y JDBC.
  - Formatos unificados.
  - JSON, XML, importación, `collation`, `bd-en-memoria` y APIs (complementario).
  - `tp2` original.
  - `practica-transacciones` queda como puente hacia u3.
- **Errores corregidos:**
  - JSON con `AS JSON` inválido.
  - XML mal formado.
  - `database_id` inexistente en `sys.filegroups`.
  - Limitaciones de In-Memory OLTP desactualizadas: FK, NULL y `ALTER TABLE` se admiten (medido en 2022).
  - JDBC se atribuía a "Java EE".
  - Conflictos de collation sin resolver.
  - Vista sobre `##temporal`.
  - `REPLACE` con mojibake bajo `CI_AI`.
- **Ejercicios:** 55 (18, 20 y 17 por nivel): 50 `motor`, 3 `razonamiento` y 2 `revisado`.
- **Verificación:** 113 comprobaciones, varias con archivos auxiliares (CSV, JSON y XML propios publicados en `public/bbdd-aplicadas/unidad-2/practica/archivos/`); 6 pendientes de verificación específica.
- **Fuentes:** cátedra de u2, parte 1 (p.2–30) y parte 2 (p.4–26); documentación de Microsoft.

### Unidad 3 — Bases de datos relacionales: aspectos avanzados (E5)

- **Temas:** los 10 temas de u3. 5 `verificado` (plan, índices, estadísticas, optimización, columnstore) y 5 `con-observaciones` (concurrencia, TCL, bloqueos, distribuidas y monitoreo: dos sesiones, MS DTC o salida de `BACKUP` no determinista).
- **Páginas:**
  - `transacciones-concurrencia` pasa a concurrencia, bloqueos y distribuidas.
  - `transacciones-y-concurrencia` pasa a TCL, sin duplicación entre ambas.
  - `indices-optimizacion`, `indices-y-planes` y `metricas-de-rendimiento` reorganizadas: cada tema en una sola página.
  - Laboratorios de TCL y aislamiento corregidos.
  - Práctica nueva `rendimiento`.
- **Errores corregidos:**
  - Tabla de `XACT_ABORT`.
  - Laboratorios sin `WAITFOR`, con IDs inconsistentes y con un fantasma no observable.
  - Faltaba el script del error 3960.
  - "Table Scan" en tablas con clúster.
  - Key Lookup que el ejemplo no producía.
  - Script con `sp_MSforeachdb`.
  - `REBUILD ONLINE` sin la aclaración de edición.
  - Triplicación de índices, estadísticas y columnstore.
- **Evidencia que contradice a la cátedra:** un `UPDATE` con el mismo valor no generó registros de log en SQL Server 2022. Se documentó como medido.
- **Ejercicios:** 45 (14, 18 y 13 por nivel): 33 `motor`, 7 `razonamiento` y 5 `revisado`.
- **Verificación:**
  - 102 comprobaciones.
  - Los planes se verifican extrayendo operadores del XML, y las lecturas lógicas son deterministas.
  - 14 pendientes de verificación específica, con guiones por sesión. No se inventaron salidas de dos sesiones.
- **Fuentes:** cátedra de u3, parte 1 (p.4–31) y parte 2 (p.4–44); documentación de Microsoft.

### Unidad 4 — Bases de datos no relacionales (E6)

- **Temas:** los 9 temas de u4, todos `verificado`.
- **Páginas:**
  - Reescritas: `mongodb-introduccion`, `mongodb-crud`, `mongodb-agregacion` (con índices y estadísticas), `mongodb-compass`, `instalacion-mongodb`, `nosql-conceptos`, `datos-data-lake-kdd` y `guia-parcial`.
  - Página nueva `poo-y-bases` (D4).
  - `apunte-completo` pasa a resumen integrador.
  - Las tres prácticas se reescribieron con datos propios publicados en `public/bbdd-aplicadas/unidad-4/practica/archivos/{ventas,tienda,videoclub}/`.
- **Errores corregidos:**
  - `$cmp`, `$multiply` y `$round` figuraban como acumuladores.
  - `dropIndex` de un índice nunca creado.
  - Type bracketing de fechas.
  - Upsert sin ejemplo.
  - "MongoDB es CP" sin matiz.
  - KDD en 7 etapas, reemplazado por las 5 de Fayyad et al. (1996), distinguido de data mining (D4).
  - Prácticas sin datos.
  - Consultas 7, 8 y 20 de la práctica.
  - Vista con nombres distintos al crearla y al usarla.
- **Ejercicios:** 37 (12, 13 y 12 por nivel): 31 `motor` y 6 `razonamiento`.
- **Verificación:** 67 comprobaciones (62 en MongoDB 7 y 5 en SQL Server); 1 pendiente de verificación específica (creación de usuario y autenticación de `mongod`). Se eliminó `U4.P.20`, que embebía el dataset de cátedra retirado.
- **Fuentes:** cátedra de u4, partes 1–3 y apunte NoSQL; manual de MongoDB; Fayyad, Piatetsky-Shapiro y Smyth (1996).

### Unidad 5 — Protección de los datos (E7)

- **Temas:** los 8 temas de u5. 4 `verificado` y 4 `con-observaciones` (autenticación, cifrado, backups y alta disponibilidad: usuarios de Windows, TDE activo, archivos de certificado, AG de dos nodos).
- **Páginas:**
  - Reescritas: `seguridad-permisos` (con autenticación y directivas de contraseñas ampliadas), `cifrado`, `log-recuperacion`, `backup-restauracion` y `alta-disponibilidad`.
  - `inyeccion-sql` y su laboratorio, como complementarios.
  - Laboratorios de seguridad, inyección y backup.
  - `apunte-completo` pasa a resumen.
  - Guía de repaso con simulacro y pauta.
- **Errores corregidos:**
  - Parte 5 del laboratorio de inyección.
  - `GRANT` de esquema sin revertir.
  - Variable usada fuera de su lote y tipo sin definir en el cifrado.
  - Certificado de backup nunca creado.
  - `SESSION_TIMEOUT`.
  - Confusión de estados en el laboratorio de backup.
  - Terminología diferencial/incremental, explicada sin contradecir a la cátedra.
- **Hechos medidos:** política de contraseñas en Linux (errores 33062, 33064, 15122 y 15099); 10 roles `##MS_*##`; precedencia de `DENY`.
- **Ejercicios:** 31 (10, 11 y 10 por nivel): 21 `motor` y 10 `razonamiento`.
- **Verificación:** 57 comprobaciones, con backups y restauraciones reales en la base de prueba; 8 pendientes de verificación específica.
- **Fuentes:** cátedra de u5 (p.3–61); documentación de Microsoft.

### Unidad 6 — Calidad en bases de datos (E8)

- **Temas:** los 3 temas de u6, todos `verificado` (casos y laboratorios con SQL ejecutado; el resto, razonamiento con artículo citado).
- **Páginas:**
  - `ley-25326`, `gdpr` e `iso-25012` reescritas **sobre fuentes primarias** (D3).
  - `apunte-completo` pasa a resumen.
  - Guía de repaso.
  - `medicion-calidad` y `gobierno-privacidad` rotuladas como complementarias.
  - Laboratorios de calidad y privacidad, y casos integradores propios.
- **Fuentes verificadas:**
  - InfoLEG: Ley 25.326, Decreto 1558/2001 y Resolución AAIP 47/2018.
  - Boletín Oficial: Resolución AAIP 332/2020.
  - EUR-Lex: RGPD (CELEX 32016R0679), con artículos y considerandos citados.
- **ISO/IEC 25012:** iso.org bloquea los clientes automatizados. No se atribuye a la norma nada no verificado: la clasificación en tres grupos se atribuye explícitamente al resumen público de iso25000.com.
- **Errores corregidos:**
  - Cita atribuida a Henry Ford, eliminada por no tener origen verificable.
  - Diagrama con un nodo duplicado.
  - Exclusiones del RGPD omitidas.
  - Persona jurídica en la ley.
  - Autoevaluaciones sin respuesta.
- **Ejercicios:** 30 (9, 12 y 9 por nivel): 13 `motor` y 17 `razonamiento`, con artículo.
- **Verificación:** 20 comprobaciones (incluido Dynamic Data Masking con `EXECUTE AS`).

## 4. Pendientes que requieren decisión o acción humana

1. **Despliegue.** No se desplegó nada. Los seis recursos retirados siguen publicados en producción hasta el próximo despliegue autorizado. Después hay que correr `node scripts/verify-production.mjs`, que espera 404 en esas rutas.
2. **Credencial expuesta.** La docente titular debe revocar o cambiar la credencial de Atlas de `Instalación MongoDB.pdf`. No se registró su valor.
3. **Recursos retirados (resuelto).** `window-functions.sql`, `datosventas_1.json`, `cc_info.csv` y `transactions.csv` se retiraron junto con los dos PDF (`migration/withdrawn.json`). Ninguna página dependía de ellos.
4. **Imágenes sin referencia.** `public/bbdd-aplicadas/unidad-1/images/wf-*.png` y `pivot*.png` quedaron sin uso y se conservan. ¿Se retiran?
5. **ISO/IEC 25012.** Hay que confirmar a mano la ficha de iso.org (año y estado de la norma) y la figura de iso25000.com con las 15 características en tres grupos, para retirar la atribución a la fuente secundaria.
6. **Programa vigente.** Hay que confirmar con la cátedra si existe un programa posterior a 2024. No se supuso ninguno (D1).
7. **Pendientes de verificación específica (30).** Para pasarlos a verificados se necesita infraestructura adicional: un segundo cliente concurrente automatizado, una segunda instancia con MS DTC o un grupo de disponibilidad, Windows para Ole Automation y SQL Server 2025.
8. **Montos de multas de la Ley 25.326.** Son los nominales del art. 31. No se verificaron actualizaciones posteriores del régimen sancionatorio.

## 5. Cómo reproducir

```sh
cd tools/content-pipeline
.venv/bin/content-pipeline engines up --subject bbdd-aplicadas
.venv/bin/content-pipeline verify-code --subject bbdd-aplicadas   # 454 comprobaciones
.venv/bin/content-pipeline qa --subject bbdd-aplicadas
.venv/bin/content-pipeline validate --subject bbdd-aplicadas --docs-root ../../src/content/docs
.venv/bin/pytest -m "not integration"
cd ../.. && npm run build && npm run validate && npm run test:browser
```
