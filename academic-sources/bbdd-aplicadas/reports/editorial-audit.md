# Auditoría editorial — Bases de Datos Aplicada (3641)

Fecha: 2026-11-19 · Etapa E11 (`implementation-plan.md`) · Rama de trabajo `feat/bbdd-aplicadas-editorial`, creada desde
`origin/main` con la PR #14 ya integrada.

**Objetivo.** Que los apuntes le hablen al estudiante y no a quien mantiene el sitio. Una persona que estudia la materia
tiene que entender las explicaciones y las instrucciones sin conocer el pipeline, los tests ni cómo se construyó el
portal. Las limitaciones reales siguen a la vista, pero contadas desde el estudiante. Es una tarea editorial: no cambian
temas, ejercicios, código ni resultados.

## 1. Alcance y método

- **Páginas revisadas: 83** (todas las de `src/content/docs/bbdd-aplicadas/`).
  - La portada y `como-estudiar`, a cargo de la coordinación.
  - Las 81 páginas de las seis unidades, repartidas entre tres revisores: u1–u2, u3–u4 y u5–u6.
  - Cada unidad incluye presentaciones, teoría, prácticas, ejercicios y resoluciones, resúmenes integradores, guías y avisos.
- **Fase A — Auditoría.**
  - Cada página se leyó completa, sin limitarse a buscar términos.
  - En las páginas largas, la segunda pasada de u1–u2 cubrió:
    - lectura completa: `repaso-sql`, `json-en-sql`, `xml-en-sql` y el resto de las lecciones de esas unidades;
    - lectura de la prosa, sin revisar cada celda de las tablas de resultados: `tp1`, `tp2`, `practica/window-functions` y `practica/pivot`.
  - Para saber qué bloques dependen de otros, se compararon los bloques de la página con su script en `checks/sql/` o `checks/mongo/`.
- **Fase B — Corrección.**
  - Orden de prioridad: primero lo que impedía ejecutar una práctica, después lo engañoso, el proceso interno, los términos sin explicar y la redacción.
  - Antes de corregir se fijó una **convención común** (ver §3), aplicada igual en las seis unidades.
- **Fase C — Revisión.**
  - La coordinación comparó cada cambio contra `origin/main`.
  - Revisó todas las líneas agregadas en busca de afirmaciones técnicas nuevas y corrigió dos (§4.3).
  - Verificó por script la preservación del contenido académico (§6).
- **Fase D — Validación:** ver §5.

## 2. Hallazgos

**81 hallazgos**: 70 de los revisores por unidad y 11 de la coordinación. Muchos agrupan varias apariciones del mismo
problema en una página o en páginas hermanas. Todos se corrigieron. El único que requería una decisión académica (U1.37) se resolvió el 2026-11-20 y se documenta aparte, en §4.1.

| Tipo | Hallazgos donde aparece* | Como tipo principal |
|---|---:|---:|
| A. Proceso interno a la vista (verificador, «entorno de verificación», rutas del repo, identificadores de comprobación) | 40 | 37 |
| B. Instrucciones que presuponen lo no explicado (base, datos, bloque previo, sesiones) | 32 | 27 |
| C. Limitación mal atribuida (motor, plataforma, permisos, entorno de pruebas) | 18 | 5 |
| D. Autorreferencias e historial del material («versión anterior», «reemplaza al laboratorio…») | 6 | 3 |
| E. Problemas pedagógicos (resultados armados sin explicar, ejemplos que alteran datos, redacción ambigua) | 15 | 9 |

\* Un hallazgo puede tener más de un tipo.

| Prioridad | Cantidad | Criterio |
|---|---:|---|
| Alta | 38 | Impedía reproducir una práctica o podía inducir a error |
| Media | 31 | Proceso interno a la vista o término sin explicar |
| Baja | 12 | Redacción |

Medido con la nueva regla `texto-interno` de `qa` (§7): `origin/main` tenía **65 apariciones en 27 páginas** y ahora hay **0**.

| Patrón | Antes | Después |
|---|---:|---:|
| «pendiente de verificación específica» | 20 | 0 |
| «el verificador» | 19 | 0 |
| Identificadores de comprobación en la prosa (`U4.T.CRUD.01`…) | 13 | 0 |
| «verificación automática» | 5 | 0 |
| Rutas internas (`academic-sources/`, `checks/mongo/`) | 4 | 0 |
| «entorno de verificación» | 3 | 0 |
| «registrado como revisado» | 1 | 0 |

### Hallazgos principales por unidad

**Unidades 1 y 2**
- **`repaso-sql` (caso prioritario).**
  - La afirmación «cada ejemplo es autocontenido: copiado en una base vacía produce el resultado» era engañosa. Cada bloque crea el esquema `academia` y sus datos, así que se puede ejecutar solo; pero dos bloques seguidos en la misma base fallan porque el esquema ya existe.
  - «Catálogos y esquemas» explica ahora:
    - qué hacen `CREATE DATABASE`, `COLLATE` y `USE`, y qué permiso hace falta;
    - que una base de práctica existente sirve sin crear otra;
    - qué es el esquema `academia` y por qué se usa;
    - qué ejecutar antes de seguir.
  - Se aclara que ese único bloque no se probó en un motor.
- **Datos que la página no creaba.**
  - El `UNPIVOT` leía `ventas.ResumenMensual`, que solo se creaba en el script de comprobación.
  - Los archivos de ejemplo de importación y de ancho fijo no se podían descargar.
  - Ahora se indica cómo obtener cada uno.
- **Ejemplos que alteran datos.** La CTE con `DELETE`/`UPDATE` y los ejercicios 5 y 13 del TP 1 cambian los resultados de los ejemplos siguientes. Ahora tienen aviso y se explica cómo volver a empezar.
- **Collation.** `ALTER DATABASE CURRENT COLLATE` va solo en una base de práctica, y el resultado depende de la collation de la instancia.
- **`CODEPAGE = '65001'`.** Se conserva como limitación real de SQL Server para Linux (error 16202), y ya no como limitación del «entorno de pruebas».

**Unidades 3 y 4**
- **Laboratorios de dos sesiones.** Ahora explican cómo crear la base, abrir dos ventanas de consulta y ejecutar `USE` en cada una, en qué orden ejecutar los bloques y cómo aprovechar el `WAITFOR`.
- **`indices-optimizacion`.**
  - «Developer, que es la del contenedor de estos ejemplos» pasó a ser la edición con la que se obtuvieron los resultados.
  - Se explica cómo ver lo mismo en SSMS: plan real con `Ctrl+M` y `SET STATISTICS IO`.
- **MongoDB.**
  - Se quitaron las rutas `academic-sources/…` y los identificadores de comprobación.
  - Las colecciones `pedidos`, `ordenes` y `catalogo`, que ningún bloque de la página creaba, ahora tienen instrucciones de carga. El código en línea es idéntico al de los scripts de comprobación `U4.T.IDX.01`, `.04` y `.05`.
  - La instalación y la autenticación se explican como dependientes del sistema operativo y de la versión.
- **`metricas-de-rendimiento`.** El ejemplo de backup del log supone la base en `FULL`, pero el ejemplo anterior la deja en `SIMPLE`. Se agregó la instrucción en la prosa.

**Unidades 5 y 6**
- **Resultados «armados por el verificador».** Afectaba a los ejercicios 30, 32, 33 y 34 del laboratorio de backup y a las lecciones de backup, log y alta disponibilidad. Ahora cada uno explica qué ve el estudiante si ejecuta el bloque tal cual y qué consulta o paso adicional produce la tabla mostrada. Se contrastó contra `checks/sql/`.
- **Ejemplos no probados, con su motivo real:**
  - TDE, respaldo del certificado y backup cifrado: escriben archivos, `tempdb` queda cifrada hasta reiniciar el servicio y requieren permisos en `master`.
  - Alta disponibilidad de dos nodos: requiere dos instancias en red.
  - `ALTER LOGIN sa DISABLE`: afecta a toda la instancia.
  - Autenticación de Windows y bases contenidas: requieren dominio o `CONTAINMENT = PARTIAL`.
- **Preparación.** Las bases de práctica (`LaboratorioU5`, `CalidadU6`, `PrivacidadU6`) tienen nombre, permiso necesario, dependencias entre ejercicios y la indicación de que el ejercicio 26 requiere el 25. Se avisa del choque del esquema `calidad` entre `iso-25012` y el laboratorio de calidad, y se agregaron instrucciones para borrar logins y roles de práctica.
- **Título.** `## Cómo se verificó` pasó a `## Qué resultados vas a obtener`. No tenía enlaces entrantes.

**Portada y guía general**
- **«Cómo estudiar».**
  - Nueva sección «Antes de ejecutar los ejemplos». Define base de práctica (crearla, usarla, borrarla y el permiso necesario), preparación, dos sesiones y cómo ver un plan. Las prácticas la enlazan en lugar de repetir la explicación.
  - El recuadro sobre qué está comprobado ahora habla de requisitos del estudiante y no de «verificación automática».
- **Referencias a ejercicios.** Ocho remitían a un ejercicio por su identificador interno (`U3.10`, `U5.04`…) en lugar del número que ve el estudiante. Ahora dicen, por ejemplo, «ejercicio 10 del laboratorio TCL».

### Ejemplos representativos (antes → después)

1. `repaso-sql`:
   > Ese bloque no se ejecuta en el entorno de verificación (crear bases de datos está fuera de su alcance); está registrado como revisado. Los demás ejemplos asumen una base vacía y crean el esquema `academia`.

   →
   > Este bloque `CREATE DATABASE` **no se probó en un motor**: es la única parte de esta lección que no se ejecutó. Se comporta como documenta Microsoft; comprobalo en tu instalación. Si ya tenés una base de práctica, no hace falta crear otra: cambiá a ella con `USE NombreDeTuBase;`. […]

2. `laboratorio-backup`, ejercicio 33:
   > **Resultado esperado** (el verificador junta el aviso del `CATCH` y el orden correcto en una tabla; al final hay 2 filas).

   →
   > **Resultado esperado.** Si ejecutás el bloque tal cual, el `CATCH` devuelve solo la fila «Restaurar log2 sin log1»; la tabla siguiente reúne además el resultado del orden correcto, que se obtuvo anotando cada paso en una tabla temporal. Al final hay 2 filas recuperadas.

3. `laboratorio-tcl`:
   > Los experimentos 1 a 3 necesitan dos o tres ventanas de consulta […] y no se ejecutan en la verificación automática.

   →
   > Los experimentos 1 a 3 necesitan **dos o tres ventanas de consulta** (pestañas en SSMS o en VS Code, conectadas al mismo servidor, con `USE LabTransacciones;` ejecutado en cada una; cada una es una sesión independiente) y **no se probaron en un motor**: el «resultado esperado» es el comportamiento que describe la documentación de SQL Server; comprobalo en tu instalación.

4. `seguridad-permisos`:
   > Esa sentencia no se ejecuta en el verificador porque afectaría a la instancia compartida.

   →
   > Deshabilitar `sa` afecta a toda la instancia (y a cualquier aplicación que lo use), por eso conviene probarlo solo en una instancia propia de laboratorio. Esa sentencia no se probó en un motor.

5. `mongodb-crud`:
   > Los scripts completos están en `academic-sources/bbdd-aplicadas/checks/mongo/` (`U4.T.CRUD.01` a `U4.T.CRUD.07`).

   →
   > Para reproducirlos, abrí `mongosh`, elegí una base de práctica (por ejemplo, `use practica`; se crea al insertar el primer documento) y cargá los datos de la sección siguiente.

## 3. Convención adoptada (incorporada a `content-guide.md` §8, «Redacción dirigida al estudiante»)

- **Ejemplo ejecutado.** Basta una mención por página de la versión y la plataforma («Los resultados se obtuvieron con SQL Server 2022»).
- **Ejemplo no ejecutado** (sigue registrado en `checks/reviewed.yaml`, que no cambió):
  - se dice que **no se probó en un motor**;
  - se dice qué necesita el estudiante para ejecutarlo;
  - se aclara que el resultado descripto es el que indica la documentación oficial.
  
  Si la incertidumbre es material, va en `:::caution[No probado en un motor]`.
- **Limitaciones.** Se distingue la del motor o la plataforma de un requisito de permisos o de infraestructura. No se atribuye al motor lo que es solo del sistema de pruebas.
- **Resultados resumidos o reunidos.** Se explica qué se muestra y en qué difiere de la salida del bloque.
- **Términos operativos.** «Base de práctica», «preparación» y «dos sesiones» se explican o enlazan a la guía general.

## 4. Decisiones pendientes y observaciones técnicas

### 4.1 Resuelto: corrección académica y técnica de U1.37

Es el único hallazgo que no era editorial. Se registra aparte porque modifica un bloque ejecutable, su comprobación y
la matriz curricular. La decisión académica (2026-11-20) fue:
- mantener el enunciado: un PIVOT dinámico tiene que incorporar meses nuevos sin modificar la consulta;
- ampliar el `CASE` de ordenamiento a los doce meses;
- conservar la generación dinámica con `STRING_AGG`, `QUOTENAME` y `sp_executesql`.

- **Defecto.** La resolución ordenaba las columnas con un `CASE` que solo conocía enero a junio. Una venta de julio
  generaba su columna, pero con orden `NULL`, y la columna quedaba **primera**. La resolución no cumplía la condición
  «en orden cronológico» del enunciado.
- **Evidencia en el motor** (SQL Server 2022 RTM-CU28, 16.0.4325.4, contenedor del proyecto):

  | Prueba | Consulta original (`CASE` de enero a junio) | Consulta corregida (`CASE` de doce meses) |
  |---|---|---|
  | Datos de enero a junio (`U1.37`) | aprobada | aprobada, sin cambios en el resultado esperado |
  | Con dos ventas de julio, lista que arma `STRING_AGG` | `[Julio], [Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio]` | `[Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio], [Julio]` |
  | Con julio, primera fila del resultado | `Ana\|3100.00\|1800.00\|…\|2500.00` (julio primero) | `Ana\|1800.00\|…\|2500.00\|3100.00` (julio último) |
- **Cambios.**
  - `unidad-1/practica/pivot.md`, ejercicio 5. El bloque de la resolución tiene el `CASE` de doce meses, idéntico a `checks/sql/U1.37.sql`. La explicación dice por qué el `CASE` tiene que cubrir los doce meses y por qué un mes desconocido quedaría primero. Hay un bloque nuevo de comprobación («llegan ventas de julio»), con su resultado esperado y la indicación de borrar esas filas antes de seguir.
  - `checks/sql/U1.37.sql`: `CASE` ampliado. Su `.expected` no cambia.
  - **Prueba de regresión** `checks/sql/U1.37.JUL.sql` y `.expected`. Carga los mismos datos, agrega dos ventas de julio y ejecuta la consulta **idéntica** a la de `U1.37` (se compara textualmente). El resultado esperado fija `Julio` en la última columna. Con el `CASE` anterior, la salida no coincide con ese `.expected` y la comprobación falla. Está enlazada al bloque nuevo de la página con `<!-- check: U1.37.JUL -->`.
  - `curriculum-map.yaml`: `u1-pivot` pasa de `verified_checks` 27 a 28.
  - `reports/code-verification.{md,json}`: regenerados con la corrida completa (§5).
- **Límite.** `verify-code` necesita los contenedores de los motores, así que la regresión se ejecuta con
  `content-pipeline verify-code` y no en la integración continua del sitio.

### 4.2 A considerar, sin urgencia

- **Código de preparación en línea.** El de `ventas.ResumenMensual` (PIVOT) y el de las colecciones `ordenes` y `catalogo` (MongoDB) quedó como código en línea dentro de la prosa, idéntico al de los scripts de comprobación. Convertirlo en un bloque propio con su marcador `<!-- check -->` lo haría más cómodo de copiar, pero exige tocar bloques y checks.
- **`metricas-de-rendimiento`.** La instrucción de poner la base en `FULL` antes del ejemplo de backup del log está en la prosa. Podría incorporarse al bloque si se repite su comprobación.
- **Esquemas repetidos.** `indices-optimizacion` e `indices-y-planes` crean los mismos esquemas (`ventas`, `diag`); ya se avisa que van en bases distintas.
- **Fuentes de U6.** Las citas normativas no se volvieron a contrastar con las fuentes primarias, que no formaban parte de esta auditoría. Se conservaron sin cambios.

### 4.3 Errores técnicos detectados y corregidos

- **`laboratorio-backup`, ejercicio 32 (`STOPAT`).**
  - El texto afirmaba que el valor «debe estar en el literal del `RESTORE`», y una primera reescritura agregó «no se puede pasar una variable». Es falso: la sintaxis de `RESTORE` admite `STOPAT = @variable`, y en ese bloque la variable está en el mismo lote.
  - La versión final explica que la fecha del literal es un ejemplo que hay que reemplazar, menciona la alternativa con `STOPAT = @Momento` y aclara que esa variante no se ejecutó.
- **`importacion-de-archivos`.** Una primera reescritura agregó que «en Linux se usa `CODEPAGE = 'RAW'`», una afirmación nueva sin probar. Se reemplazó por la alternativa que la página ya muestra y que sí se probó: `SINGLE_BLOB` con collation UTF-8.

## 5. Validaciones

| Control | Resultado |
|---|---|
| `content-pipeline qa --subject bbdd-aplicadas` | 0 errores, 0 advertencias (incluida la regla nueva `texto-interno`); 235 ejercicios completos: 185 motor, 43 razonamiento, 7 revisado, igual que la línea base |
| `content-pipeline qa --subject algebra-ii` | 0 errores, 10 advertencias, las mismas que antes (la regla nueva no produce hallazgos). Su reporte se restauró para no incluir cambios ajenos |
| `content-pipeline verify-code` (completo, SQL Server 2022 RTM-CU28 y MongoDB 7.0.48) | 455 de 455 aprobadas (las 454 previas más la regresión `U1.37.JUL`); 30 pendientes de verificación específica, sin cambios; 0 bloques sin verificar; 24 plantillas de sintaxis |
| `pytest` (pipeline) | 111 pasan (3 tests nuevos de `texto-interno`), 1 omitido porque requiere los contenedores de los motores |
| `npm run build` | correcto |
| `npm run validate` | 0 errores: 262 páginas, todas alcanzables; enlaces, anclas y compatibilidad correctos; 271 revisiones encadenadas |
| `npm run test:browser` | 50 pasan, 6 omitidos |
| `git diff --check` | limpio |

Las correcciones editoriales no tocaron bloques de código, datos ni scripts de comprobación. La única corrección
que los modifica, U1.37 (§4.1), se verificó en el motor con la corrida completa de `verify-code`.

## 6. Preservación del contenido académico

Comparación contra la línea base tomada en `origin/main` antes de editar:

| Elemento | Base | Ahora | Diferencia |
|---|---:|---:|---|
| Rutas (slugs) | 83 | 83 | ninguna |
| Ejercicios (`<!-- ejercicio -->`) | 235 | 235 | ninguna; mismos estados de verificación |
| Marcadores `<!-- check -->` | 483 | 484 | uno nuevo: `U1.37.JUL` (§4.1) |
| Bloques de código (hash del bloque completo) | 789 | 790 | por la corrección editorial, ninguno; por U1.37 (§4.1), el bloque de la resolución cambia (`CASE` de doce meses) y se agrega el de julio |
| Resoluciones (`<details>`) | 387 | 387 | ninguna eliminada; 22 con prosa editada (estrategia o nota del resultado esperado), sin tocar su código |
| Asociación marcador → bloque (`scan_docs`) | 0 pendientes, 0 huérfanos, 24 plantillas | igual | ninguna |
| Tablas Markdown fuera de código | — | — | una celda: se quitó «(verificado)» en `importacion-de-archivos` |
| Títulos y anclas explícitas | — | — | un título renombrado sin enlaces entrantes (`laboratorio-backup`) y una sección nueva en `como-estudiar` |

Tampoco cambiaron las unidades, la asignación de los 53 temas, las fuentes ni las rutas de aprendizaje.
Por la corrección editorial no se modificaron `checks/`, `reviewed.yaml` ni `migration/sources.json`; los cambios en
`checks/sql/U1.37*` y en `code-verification.*` corresponden solo a U1.37. Las 61 páginas migradas editadas se registraron
en `migration/revisions.json` con la etapa E11, y la corrección de U1.37 por separado, con la etapa E11-U1.37.

## 7. QA editorial automatizado

Se agregó a `qa.py` la regla **`texto-interno`**, de severidad advertencia.

- **Qué detecta, en la prosa publicada:**
  - frases que solo describen el proceso interno: «entorno de verificación», «el verificador», «verificación automática», «pendiente de verificación específica», «registrado como revisado»;
  - rutas y herramientas del repositorio: `academic-sources/`, `checks/sql|mongo/`, `reviewed.yaml`, `content-pipeline`, `code-verification.*`;
  - identificadores de comprobación con forma `U4.T.CRUD.01`.
- **Qué no se considera:**
  - los bloques de código y los comentarios HTML, porque los marcadores son metadatos;
  - palabras sueltas, para evitar falsos positivos con usos legítimos como «verificá el resultado», «pipeline de agregación», el «contenedor» de un filegroup o Docker.
- **Excepciones:** una materia las declara en `subject.yaml` → `qa.internal_text_allow` como lista de `{pattern, reason}`.
- **Tests:** detección de cada patrón, exclusión de código, comentarios y usos legítimos, y funcionamiento de las excepciones.
- **Resultado en las demás materias:** no hay hallazgos en Álgebra II, Análisis Matemático I ni Diseño de Software.

**Mejoras futuras posibles** (no implementadas):
- avisar cuando se cita un ejercicio por su identificador interno (`U3.10`) en lugar de su número visible; hoy se corrigió a mano;
- detectar bloques que usan tablas o colecciones que ningún bloque anterior de la página crea, como `ResumenMensual`, `ordenes` o `catalogo`;
- comprobar que cada práctica enlace su preparación o sus datos descargables.

Todas requieren un análisis más fino que una expresión regular.
