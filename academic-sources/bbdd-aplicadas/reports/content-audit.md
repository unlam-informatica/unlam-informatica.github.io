# Auditoría académica — Bases de Datos Aplicada (3641)

Fecha: 2026-11-17 · Fase: matriz curricular y auditoría. No se modificó ninguna página publicada.

Antecedentes: `ingest-audit.md` y `extraction-report.md`. La matriz está en `../curriculum-map.yaml` y
las convenciones de redacción en `../content-guide.md`. Este informe no reproduce texto de las
fuentes ni datos personales.

## 1. Alcance y método

- **Alcance.** Se revisaron completas las **79 páginas** de `src/content/docs/bbdd-aplicadas/`, más
  sus recursos referenciados. Se contrastaron con el programa 2024 y con los 51 documentos extraídos.
- **Corpus anonimizado.** La revisión usó una copia anonimizada del corpus, sin nombres, DNI, correos
  ni líneas de identificación. El documento excluido por credenciales no se usó.
- **División del trabajo.** Tres revisores trabajaron en paralelo (u1–u2, u3–u4, u5–u6 y la portada)
  con una lista fija de 53 temas, derivada ítem por ítem del programa 2024.
- **Verificación de la coordinación.**
  - Se validaron las 646 referencias de página propuestas: todas existen y las palabras clave del tema aparecen en ellas.
  - Se contrastaron a mano los hallazgos de mayor impacto (sección 2.2).
  - Se confirmó con la página renderizada que el programa 2024 incluye Data Mining y KDD en u4.
- **Controles automáticos.**
  - `content-pipeline validate` sobre la matriz: 0 errores. Los 53 temas resuelven su página
    actual; se corrigió `validate` para que resuelva por `slug`.
  - `content-pipeline qa` (línea de base): 23 errores. 17 son de `$` y 6 de enlaces; su lectura está en la sección 2.2.
- **Limitaciones.**
  - No había motor SQL Server ni MongoDB disponible: el código se revisó por inspección. Las
    observaciones marcadas "verificar en motor" quedan abiertas.
  - Las observaciones de la sección 9 son una lista de revisión. Las de la sección 2.2 están
    verificadas; las demás se confirman al corregir cada página.

## 2. Resumen ejecutivo

| Indicador | Valor |
|---|---|
| Temas del programa 2024 | 53 en 6 unidades |
| Cobertura actual | completo 29, parcial 15, superficial 7, ausente 2 |
| Acción por tema | corregir 19, ampliar 16, conservar 11, investigar 4, reorganizar 3 |
| Confianza del respaldo | alta 36, media 13, baja 4 |
| Temas sin fuente de cátedra | 4: `u4-poo`, `u6-ley-25326`, `u6-gdpr`, `u6-iso-25012` |
| Veredicto por página (79) | corregir 39, conservar 18, reorganizar 12, ampliar 5, investigar 4, reemplazar 1 |
| Observaciones por página | 219 faltantes, 21 de unidad, 120 solapamientos, 98 de ejercicios, 172 de código, 81 sin fuente, 92 afirmaciones dudosas |
| Temas fuera del programa o de su unidad | 28 (sección 10) |

### 2.1 Conclusiones

1. **El portal sigue el programa 2023, no el 2024.**
   - Los títulos de u2, u3 y u4 usan "transaccionales" y "no transaccionales".
   - Los índices hablan de "1er parcial" y "2do parcial".
   - La referencia provisional es 2024: "relacionales", un parcial sobre u1–u4, el TP integrador y el
     final con todas las unidades. Los contenidos de u3 a u6 no cambian entre versiones; cambian la
     ubicación de los formatos de intercambio (de u1 a u2), "Qué es una API" (nuevo en u2) y la evaluación.
2. **La base es aprovechable.**
   - 18 páginas se pueden conservar y la mayoría de los temas está cubierta.
   - Hay dos temas ausentes: `u2-bd-sistema` y `u4-poo`.
   - Hay siete superficiales: motores y licencias, despliegue, subconsultas, plan de ejecución,
     optimización, rowstore/columnstore y KDD. KDD además tiene confianza baja.
3. **Hay contenido fuera de su unidad.**
   - El índice clúster está en u1.
   - Aislamiento, MVCC, WAL y la práctica de transacciones están en u2.
   - Always On aparece en u2.
   - Data warehouse y data lake aparecen en u2. Ahí los pone la presentación de cátedra, pero el programa los ubica en u4.
4. **Hay redundancia alta.**
   - Los "apuntes completos" de u4, u5 y u6 duplican sus páginas temáticas.
   - En u3 hay dos páginas de transacciones y dos de índices, más métricas repetidas.
   - En u2 hay dos páginas de formatos casi idénticas.
5. **Muchos ejercicios no son confiables tal como están.**
   - El TP 1 tiene soluciones vacías en los ejercicios 6 y 10 a 20.
   - Hay errores en el TP 2, la práctica de PIVOT, la práctica de transacciones y la práctica de MongoDB.
   - Ningún laboratorio trae resultados esperados.
   - Dos prácticas de u4 dependen de archivos que no existen.
6. **El código requiere verificación sistemática.** Hay 172 observaciones de código, entre ellas:
   - sintaxis que no compila (`GO` que pierde variables, XML mal formado, `WITH ... AS JSON` inválido);
   - afirmaciones desactualizadas sobre In-Memory OLTP (FK, NULL y `ALTER TABLE` se admiten desde 2016/2017);
   - errores de lógica (`NULL = NULL` evalúa a UNKNOWN, no a FALSE; una tabla de `XACT_ABORT` invertida);
   - inconsistencias de esquema entre páginas (`wf`, `tablaswf`, `tablasWF`).
7. **Una parte importante del contenido no tiene fuente.**
   - **u6:** sin material de cátedra. El respaldo de los artículos de la Ley 25.326, las bases y
     plazos del GDPR y la clasificación de ISO/IEC 25012 viene solo de apuntes de alumnos o del
     conocimiento general; hay que contrastarlos con el texto oficial.
   - **Otros temas sin fuente en el corpus:** In-Memory OLTP en detalle, T-SQL de XML y JSON,
     llamadas HTTP con OLE Automation, deadlocks y DMVs, FCI, Always Encrypted, gobierno de datos y
     medición de calidad.
8. **Privacidad y seguridad.**
   - No se encontraron datos personales ni credenciales en las páginas publicadas: `instalacion-mongodb` no reproduce la credencial.
   - El laboratorio de inyección es defensivo, pero su Parte 5 llega a una conclusión incorrecta (ver 2.2).

### 2.2 Hallazgos verificados por la coordinación

| Página | Hallazgo | Evidencia |
|---|---|---|
| `unidad-5/practica/laboratorio-inyeccion` (Parte 5) | La conclusión es incorrecta. `BuscarSeguro` ejecuta SQL dinámico con `sp_executesql`, que no hereda el encadenamiento de propiedad. Con `DENY SELECT` sobre la tabla, el usuario de prueba **no** puede ejecutarlo; solo `BuscarEstatico` funciona | Código de la página: `GRANT EXECUTE` y `DENY SELECT` sobre `seguridad.UsuarioDemo` |
| `unidad-3/teoria/transacciones-y-concurrencia` | La tabla de `XACT_ABORT` dice que con `OFF` una violación de restricción cancela la transacción. En realidad solo termina la sentencia; la transacción sigue abierta | Tabla en la sección de `XACT_ABORT` |
| `unidad-4/practica/ejercicios` (consulta 20) | Filtra `dolar: true` en la raíz, pero en `datosventas_1.json` el campo está en `producto.dolar`, así que devuelve 0 documentos | `public/bbdd-aplicadas/unidad-4/practica/archivos/datosventas_1.json` |
| `unidad-5/teoria/apunte-completo` | Niega que una secundaria síncrona que excede el tiempo de espera pase a confirmación asíncrona. La cátedra (`5db2ce42f603` p.50) y la documentación de Microsoft lo afirman | Párrafo de modos de disponibilidad; contrastar con Microsoft Learn al corregir |
| `unidad-4/teoria/mongodb-agregacion` y `unidad-2/practica/transacciones` | KaTeX muestra como **fórmula** texto en prosa (`$addFields` … `$replaceRoot`; un tramo con montos en `$`). `npm run validate` no lo detecta porque no hay error de KaTeX | `<annotation encoding="application/x-tex">` en `dist/` |
| `unidad-4/practica/integrador-peliculas` y `laboratorio-tienda-online` | Usan `Peliculas.json`, `Prestamos.json`, `01_setup_datos.js` y `03_api_externa.js`, que no existen en el repositorio | `public/bbdd-aplicadas/unidad-4/practica/archivos/` solo tiene 4 archivos |
| Subpáginas de u5 y u6 | El enlace "← Unidad 5/6" lleva a la portada de la materia, no a la unidad. En u2–u4 funciona por redirección | 21 enlaces a `/bbdd-aplicadas/` |
| Línea de base de `qa` | Los 17 errores de `$` mezclan defectos reales (operadores MongoDB sin formato de código en títulos y prosa) con falsos positivos (montos). Los 6 "enlaces rotos" a `/unidad-N/` son falsos positivos: Astro genera esas redirecciones | `astro.config` y `dist/bbdd-aplicadas/unidad-3/index.html` |

## 3. Programa 2024 (referencia provisional) frente al 2023 (histórico)

| Aspecto | 2023 (público, DIIT) | 2024 (`3d9721081e14`) | Efecto en el portal |
|---|---|---|---|
| Título u2/u3 | BD transaccionales: aspectos básicos/avanzados | BD relacionales: aspectos básicos/avanzados | Hay que cambiar los títulos visibles (no las URL) |
| Título u4 | BD no transaccionales | BD no relacionales | Ídem; la página de u4 ya aclara la denominación |
| Formatos de intercambio | u1 | u2 | El portal ya los tiene en u2 |
| "Qué es una API" | No figura | u2 | Cubierto en u2 |
| Data Mining y KDD | u4 | u4 | Sin cambio; falta fuente de contenido |
| Contenidos mínimos | Incluyen KDD y Data Warehousing | Idénticos | Data warehouse va con data lakes en u4 |
| Evaluación | Dos parciales (u1–u3 en la semana 7; u4–u6 en la 13), recuperatorio no integrador, un TP por parcial | Un parcial (u1–u4, semana 9), TP integrador (semana 13), recuperatorio (semana 15), final con todo | Quitar "1er/2do parcial"; las guías de u5 y u6 se orientan al TP y al final |

Los exámenes del corpus (2C2023 a 2C2026) evalúan u1–u4 en el parcial, y los finales de 2025
agregan u5 y u6. Esto es coherente con el esquema 2024. El archivo de 2C2026 se llama "Parcial 1",
pero no hay evidencia de un segundo parcial: queda pendiente de confirmar (sección 7).

## 4. Matriz por tema

Fuentes: identificador corto del catálogo (`bbdd-aplicadas-<id>`) y páginas del PDF. Cobertura, calidad y confianza describen el estado **actual** del portal; la confianza es la del respaldo de fuentes. Detalle de cada tema en la sección 8.

### u1 · Conceptos básicos

| Tema | Fuentes de cátedra | Páginas actuales | Cobertura | Calidad | Confianza | Acción |
|---|---|---|---|---|---|---|
| `u1-bd-conceptos` Qué es una base de datos y su clasificación | `f740763a4b8b` p.3–12 | unidad-1/teoria/conceptos-basicos | parcial | alta | alta | **ampliar** |
| `u1-motores-licencias` Motores modernos y modelos de licenciamiento | `f740763a4b8b` p.8–11 | unidad-1/teoria/conceptos-basicos | superficial | media | alta | **ampliar** |
| `u1-dba` Tareas del administrador de bases de datos · 2 exámenes | `f740763a4b8b` p.13–14 | unidad-1/teoria/conceptos-basicos | completo | alta | alta | **conservar** |
| `u1-despliegue` Bases de datos embebidas, on premise y cloud | `f740763a4b8b` p.11–12; `d0b0a9b78ca8` p.10–17 | unidad-1/teoria/conceptos-basicos<br>unidad-2/teoria/bd-transaccionales | superficial | media | alta | **ampliar** |
| `u1-tipos-datos` Tipos de datos básicos | `9d5ab3349985` p.7–14 | unidad-1/teoria/repaso-sql | parcial | media | alta | **ampliar** |
| `u1-ddl-dml-esquemas` Repaso de SQL: DDL, DML y esquemas | `9d5ab3349985` p.4–13; `95d8b07bd5dd` p.2–3 | unidad-1/teoria/repaso-sql<br>unidad-1/practica/tp1 | completo | media | alta | **corregir** |
| `u1-integridad` Integridad referencial, claves y restricciones · 1 exámenes | `9d5ab3349985` p.5–21 | unidad-1/teoria/repaso-sql | parcial | media | alta | **corregir** |
| `u1-subconsultas` Subconsultas | `9d5ab3349985` p.28–29 | unidad-1/teoria/repaso-sql | superficial | media | media | **ampliar** |
| `u1-vistas-agregados` Vistas y funciones de agregado | `9d5ab3349985` p.29–33 | unidad-1/teoria/repaso-sql | parcial | media | alta | **corregir** |
| `u1-programabilidad` Procedimientos almacenados, triggers y funciones | `9d5ab3349985` p.34–41 | unidad-1/teoria/repaso-sql | parcial | media | alta | **corregir** |
| `u1-window` Window functions · 10 exámenes | `d275f59f2093` p.2–36; `9d5ab3349985` p.42–44; `7d43d771a356` p.2–26 | unidad-1/teoria/window-functions<br>unidad-1/practica/window-functions | completo | media | alta | **corregir** |
| `u1-cte` Common table expressions · 3 exámenes | `9d5ab3349985` p.45–47; `95d8b07bd5dd` p.3 | unidad-1/teoria/cte | completo | alta | alta | **corregir** |
| `u1-pivot` Pivot · 11 exámenes | `9d5ab3349985` p.50–51; `95d8b07bd5dd` p.4 | unidad-1/teoria/pivot<br>unidad-1/practica/pivot | completo | media | alta | **corregir** |
| `u1-null` El valor NULL | `9d5ab3349985` p.22 | unidad-1/teoria/repaso-sql | completo | media | alta | **corregir** |

### u2 · Bases de datos relacionales: aspectos básicos

| Tema | Fuentes de cátedra | Páginas actuales | Cobertura | Calidad | Confianza | Acción |
|---|---|---|---|---|---|---|
| `u2-arquitectura` Arquitectura de las bases de datos relacionales | `d0b0a9b78ca8` p.9–17 | unidad-2/teoria/bd-transaccionales | parcial | media | media | **ampliar** |
| `u2-bd-sistema` Bases de datos de usuario y de sistema | `d0b0a9b78ca8` p.18–19 | unidad-2/teoria/bd-en-memoria | ausente | sin-evaluar | media | **ampliar** |
| `u2-instalacion` Instalación de un motor de base de datos | `d0b0a9b78ca8` p.16–21; `242399d569be` p.2 | unidad-2/teoria/bd-transaccionales | parcial | media | alta | **ampliar** |
| `u2-collation` Intercalación (collation) · 1 exámenes | `d0b0a9b78ca8` p.19–23; `242399d569be` p.2–3 | unidad-2/teoria/collation<br>unidad-2/practica/tp2 | completo | alta | alta | **ampliar** |
| `u2-almacenamiento` Almacenamiento en disco y en memoria · 2 exámenes | `d0b0a9b78ca8` p.24–28 | unidad-2/teoria/bd-en-memoria<br>unidad-2/practica/practica-bd-en-memoria | completo | media | media | **corregir** |
| `u2-conexion-drivers` Configuración de conexión, drivers, ODBC y JDBC | `d0b0a9b78ca8` p.21–30 | unidad-2/teoria/formatos-conectividad<br>unidad-2/teoria/bd-transaccionales | completo | media | alta | **corregir** |
| `u2-formatos` Formatos de intercambio | `008193c9c082` p.4–22 | unidad-2/teoria/formatos-de-intercambio<br>unidad-2/teoria/formatos-conectividad<br>unidad-2/teoria/json-en-sql<br>unidad-2/teoria/xml-en-sql | completo | media | media | **reorganizar** |
| `u2-apis` Qué es una API · 1 exámenes | `008193c9c082` p.23–26 | unidad-2/teoria/formatos-conectividad<br>unidad-2/teoria/apis-desde-sql<br>unidad-2/practica/practica-apis | completo | media | media | **corregir** |
| `u2-importacion` Importación de datos de múltiples formatos | `242399d569be` p.2–3; `008193c9c082` p.8–11 | unidad-2/teoria/importacion-de-archivos<br>unidad-2/practica/importacion-archivos<br>unidad-2/practica/tp2 | parcial | media | media | **corregir** |

### u3 · Bases de datos relacionales: aspectos avanzados

| Tema | Fuentes de cátedra | Páginas actuales | Cobertura | Calidad | Confianza | Acción |
|---|---|---|---|---|---|---|
| `u3-concurrencia` Control de concurrencia y niveles de aislamiento · 5 exámenes | `17c2c97f736b` p.14–26 | unidad-3/teoria/transacciones-concurrencia<br>unidad-3/teoria/transacciones-y-concurrencia<br>unidad-3/practica/laboratorio-aislamiento | completo | media | alta | **reorganizar** |
| `u3-tcl` Transaction Control Language · 2 exámenes | `17c2c97f736b` p.4–13 | unidad-3/teoria/transacciones-concurrencia<br>unidad-3/teoria/transacciones-y-concurrencia<br>unidad-3/practica/laboratorio-tcl | completo | media | alta | **corregir** |
| `u3-bloqueos` Bloqueos y esperas | `17c2c97f736b` p.15–41 | unidad-3/teoria/transacciones-concurrencia<br>unidad-3/teoria/transacciones-y-concurrencia | completo | media | media | **conservar** |
| `u3-distribuidas` Transacciones distribuidas | `17c2c97f736b` p.27–44 | unidad-3/teoria/transacciones-concurrencia | parcial | media | alta | **ampliar** |
| `u3-monitoreo` Monitoreo y métricas de performance · 1 exámenes | `17c2c97f736b` p.31–42 | unidad-3/teoria/metricas-de-rendimiento<br>unidad-3/teoria/indices-optimizacion | parcial | media | alta | **corregir** |
| `u3-plan-ejecucion` Interpretación del plan de ejecución · 3 exámenes | `0d2ad822befa` p.4–10 | unidad-3/teoria/indices-y-planes<br>unidad-3/teoria/indices-optimizacion | superficial | media | alta | **ampliar** |
| `u3-indices` Índices clúster y no clúster · 9 exámenes | `0d2ad822befa` p.11–20 | unidad-3/teoria/indices-optimizacion<br>unidad-3/teoria/indices-y-planes | parcial | media | alta | **reorganizar** |
| `u3-estadisticas` Estadísticas · 1 exámenes | `0d2ad822befa` p.21–24 | unidad-3/teoria/indices-y-planes<br>unidad-3/teoria/indices-optimizacion | completo | media | alta | **corregir** |
| `u3-optimizacion` Optimización de consultas · 3 exámenes | `0d2ad822befa` p.8–29 | unidad-3/teoria/indices-y-planes | superficial | media | alta | **ampliar** |
| `u3-rowstore-columnstore` Rowstore y columnstore | `0d2ad822befa` p.30–31 | unidad-3/teoria/indices-optimizacion<br>unidad-3/teoria/indices-y-planes | superficial | media | alta | **ampliar** |

### u4 · Bases de datos no relacionales

| Tema | Fuentes de cátedra | Páginas actuales | Cobertura | Calidad | Confianza | Acción |
|---|---|---|---|---|---|---|
| `u4-modelos-datos` Modelos de datos heterogéneos y tipos de datos | `ed6885ded031` p.3–24 | unidad-4/teoria/nosql-conceptos<br>unidad-4/teoria/datos-data-lake-kdd<br>unidad-4/teoria/apunte-completo | parcial | alta | media | **ampliar** |
| `u4-base-acid` El modelo BASE y sus diferencias con ACID · 8 exámenes | `ed6885ded031` p.10–24 | unidad-4/teoria/nosql-conceptos<br>unidad-4/teoria/apunte-completo<br>unidad-4/teoria/guia-parcial | completo | alta | alta | **conservar** |
| `u4-tipos-nosql` Bases clave-valor, columnares y de documentos | `ed6885ded031` p.16–24 | unidad-4/teoria/nosql-conceptos<br>unidad-4/teoria/apunte-completo | completo | alta | alta | **conservar** |
| `u4-mql-crud` MongoDB Query Language: colecciones y CRUD · 8 exámenes | `4bd543391072` p.9–33; `f65cc231b1f0` p.5–19; `3df29cd152a2` p.1–2 | unidad-4/teoria/mongodb-crud<br>unidad-4/teoria/mongodb-introduccion<br>unidad-4/teoria/apunte-completo<br>unidad-4/practica/ejercicios | parcial | media | alta | **ampliar** |
| `u4-estadisticas-indices` Estadísticas de ejecución e índices en MongoDB · 2 exámenes | `9eb38199334b` p.1–13; `4bd543391072` p.40–51; `f65cc231b1f0` p.22–24 | unidad-4/teoria/mongodb-agregacion<br>unidad-4/practica/ejercicios<br>unidad-4/practica/laboratorio-tienda-online<br>unidad-4/practica/integrador-peliculas | parcial | media | media | **corregir** |
| `u4-agregacion` Agregación · 7 exámenes | `9a0d8e90ff05` p.1–33 | unidad-4/teoria/mongodb-agregacion<br>unidad-4/teoria/apunte-completo<br>unidad-4/practica/laboratorio-tienda-online<br>unidad-4/practica/integrador-peliculas | completo | media | alta | **corregir** |
| `u4-poo` Relación con la programación orientada a objetos | **sin fuente de cátedra** | unidad-4/teoria/nosql-conceptos | ausente | sin-evaluar | baja | **investigar** |
| `u4-data-lakes` Data lakes y data warehousing | `3d9721081e14` p.3; `ed6885ded031` p.8–9; `d0b0a9b78ca8` p.11–15 | unidad-4/teoria/datos-data-lake-kdd<br>unidad-4/teoria/apunte-completo | completo | media | media | **conservar** |
| `u4-kdd` Introducción al data mining y KDD | `3d9721081e14` p.3; `ed6885ded031` p.10 | unidad-4/teoria/datos-data-lake-kdd<br>unidad-4/teoria/apunte-completo | superficial | media | baja | **investigar** |

### u5 · Protección de los datos

| Tema | Fuentes de cátedra | Páginas actuales | Cobertura | Calidad | Confianza | Acción |
|---|---|---|---|---|---|---|
| `u5-minimo-privilegio` Principio del mínimo privilegio · 2 exámenes | `5db2ce42f603` p.3–8 | unidad-5/teoria/apunte-completo<br>unidad-5/teoria/seguridad-permisos<br>unidad-5/teoria/guia-parcial | completo | alta | alta | **conservar** |
| `u5-autenticacion` Autenticación y directivas de contraseñas · 1 exámenes | `5db2ce42f603` p.8–13 | unidad-5/teoria/apunte-completo<br>unidad-5/teoria/seguridad-permisos<br>unidad-5/practica/laboratorio-seguridad | parcial | media | alta | **ampliar** |
| `u5-permisos-dcl` Estructura de permisos y DCL · 3 exámenes | `5db2ce42f603` p.19–23 | unidad-5/teoria/apunte-completo<br>unidad-5/teoria/seguridad-permisos<br>unidad-5/practica/laboratorio-seguridad<br>unidad-5/teoria/guia-parcial | completo | alta | alta | **conservar** |
| `u5-propietarios-roles` Propietarios y roles · 1 exámenes | `5db2ce42f603` p.14–23 | unidad-5/teoria/apunte-completo<br>unidad-5/teoria/seguridad-permisos | completo | alta | alta | **conservar** |
| `u5-alta-disponibilidad` Alta disponibilidad y réplicas | `5db2ce42f603` p.49–58 | unidad-5/teoria/alta-disponibilidad<br>unidad-5/teoria/apunte-completo | completo | media | alta | **corregir** |
| `u5-backups` Backups: clasificación, metodología y buenas prácticas · 1 exámenes | `5db2ce42f603` p.35–45 | unidad-5/teoria/backup-restauracion<br>unidad-5/teoria/apunte-completo<br>unidad-5/practica/laboratorio-backup<br>unidad-5/teoria/guia-parcial | completo | alta | alta | **conservar** |
| `u5-recuperacion` Recuperación · 1 exámenes | `5db2ce42f603` p.24–48 | unidad-5/teoria/log-recuperacion<br>unidad-5/teoria/backup-restauracion<br>unidad-5/teoria/apunte-completo<br>unidad-5/practica/laboratorio-backup | completo | alta | alta | **conservar** |
| `u5-cifrado` Encriptación en tránsito y en almacenamiento | `5db2ce42f603` p.59–61 | unidad-5/teoria/cifrado<br>unidad-5/teoria/apunte-completo | completo | media | media | **corregir** |

### u6 · Calidad en bases de datos

| Tema | Fuentes de cátedra | Páginas actuales | Cobertura | Calidad | Confianza | Acción |
|---|---|---|---|---|---|---|
| `u6-ley-25326` Ley 25.326 de protección de datos personales · 2 exámenes | **sin fuente de cátedra** | unidad-6/teoria/ley-25326<br>unidad-6/teoria/apunte-completo<br>unidad-6/teoria/guia-parcial<br>unidad-6/practica/laboratorio-privacidad<br>unidad-6/practica/casos-integradores | completo | media | baja | **investigar** |
| `u6-gdpr` General Data Protection Regulation (GDPR) | **sin fuente de cátedra** | unidad-6/teoria/gdpr<br>unidad-6/teoria/apunte-completo<br>unidad-6/practica/laboratorio-privacidad<br>unidad-6/teoria/guia-parcial | completo | media | baja | **investigar** |
| `u6-iso-25012` Modelo de calidad de datos ISO/IEC 25012 · 1 exámenes | **sin fuente de cátedra** | unidad-6/teoria/iso-25012<br>unidad-6/teoria/apunte-completo<br>unidad-6/teoria/guia-parcial<br>unidad-6/practica/laboratorio-calidad<br>unidad-6/practica/casos-integradores | completo | alta | media | **conservar** |

## 5. Matriz por página

Veredictos: corregir 39, conservar 18, reorganizar 12, ampliar 5, investigar 4, reemplazar 1 (total 79).
Columnas: cantidad de observaciones por tipo (faltantes, unidad incorrecta, solapamientos, ejercicios, código, sin fuente, afirmaciones dudosas).

| Página | Temas | Veredicto | Falt. | Unidad | Solap. | Ejerc. | Código | S/fuente | Dudosas |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| portada |  | **corregir** | 6 | 2 | 0 | 0 | 0 | 2 | 1 |
| unidad-1/practica | u1-ddl-dml-esquemas | **conservar** | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| unidad-1/practica/pivot | u1-pivot | **corregir** | 1 | 0 | 1 | 3 | 2 | 1 | 1 |
| unidad-1/practica/tp1 | u1-ddl-dml-esquemas, u1-integridad, u1-programabilidad, u1-cte, u1-window, u1-pivot | **corregir** | 5 | 1 | 2 | 7 | 4 | 1 | 0 |
| unidad-1/practica/window-functions | u1-window | **corregir** | 3 | 0 | 1 | 3 | 3 | 0 | 0 |
| unidad-1/teoria | u1-bd-conceptos | **conservar** | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| unidad-1/teoria/conceptos-basicos | u1-bd-conceptos, u1-motores-licencias, u1-dba, u1-despliegue | **ampliar** | 5 | 0 | 1 | 0 | 0 | 1 | 2 |
| unidad-1/teoria/cte | u1-cte | **corregir** | 3 | 0 | 0 | 0 | 2 | 0 | 1 |
| unidad-1/teoria/indice-cluster | u1-indices-en-u1 | **reorganizar** | 1 | 1 | 3 | 0 | 1 | 2 | 3 |
| unidad-1/teoria/pivot | u1-pivot | **corregir** | 3 | 0 | 1 | 0 | 3 | 0 | 1 |
| unidad-1/teoria/repaso-sql | u1-tipos-datos, u1-ddl-dml-esquemas, u1-integridad, u1-subconsultas, u1-vistas-agregados, u1-programabilidad, u1-null | **corregir** | 7 | 1 | 1 | 0 | 5 | 1 | 5 |
| unidad-1/teoria/sql-dinamico | u1-programabilidad | **corregir** | 4 | 0 | 1 | 0 | 3 | 0 | 2 |
| unidad-1/teoria/window-functions | u1-window | **corregir** | 4 | 0 | 1 | 0 | 2 | 1 | 2 |
| unidad-2/practica | u2-importacion | **conservar** | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| unidad-2/practica/importacion-archivos | u2-importacion | **corregir** | 3 | 0 | 2 | 3 | 2 | 1 | 0 |
| unidad-2/practica/practica-apis | u2-apis | **corregir** | 2 | 0 | 1 | 3 | 3 | 1 | 0 |
| unidad-2/practica/practica-bd-en-memoria | u2-almacenamiento | **corregir** | 2 | 0 | 1 | 2 | 4 | 1 | 1 |
| unidad-2/practica/practica-json | u2-formatos, u2-importacion | **corregir** | 3 | 0 | 1 | 3 | 2 | 1 | 0 |
| unidad-2/practica/practica-transacciones | u2-fuera-de-unidad-transacciones | **reorganizar** | 3 | 1 | 2 | 3 | 2 | 1 | 0 |
| unidad-2/practica/practica-xml | u2-formatos, u2-importacion | **corregir** | 3 | 0 | 1 | 2 | 2 | 1 | 0 |
| unidad-2/practica/tp2 | u2-collation, u2-importacion, u1-cte, u2-almacenamiento | **corregir** | 4 | 1 | 2 | 8 | 4 | 1 | 1 |
| unidad-2/teoria | u2-formatos | **reorganizar** | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| unidad-2/teoria/apis-desde-sql | u2-apis | **corregir** | 4 | 0 | 1 | 0 | 5 | 1 | 1 |
| unidad-2/teoria/bd-en-memoria | u2-almacenamiento | **corregir** | 2 | 1 | 1 | 0 | 3 | 1 | 7 |
| unidad-2/teoria/bd-transaccionales | u2-arquitectura, u2-instalacion, u2-collation, u2-almacenamiento, u2-fuera-de-unidad-transacciones, u1-despliegue | **reorganizar** | 4 | 3 | 4 | 0 | 2 | 2 | 6 |
| unidad-2/teoria/collation | u2-collation | **ampliar** | 5 | 0 | 1 | 0 | 2 | 1 | 1 |
| unidad-2/teoria/formatos-conectividad | u2-conexion-drivers, u2-formatos, u2-apis | **reorganizar** | 2 | 0 | 3 | 0 | 2 | 1 | 3 |
| unidad-2/teoria/formatos-de-intercambio | u2-formatos, u2-importacion | **reorganizar** | 1 | 0 | 4 | 0 | 2 | 1 | 2 |
| unidad-2/teoria/importacion-de-archivos | u2-importacion | **ampliar** | 5 | 0 | 3 | 0 | 3 | 1 | 1 |
| unidad-2/teoria/json-en-sql | u2-formatos, u2-importacion | **conservar** | 3 | 0 | 3 | 0 | 3 | 1 | 0 |
| unidad-2/teoria/xml-en-sql | u2-formatos, u2-importacion | **corregir** | 3 | 0 | 2 | 0 | 3 | 1 | 1 |
| unidad-3/practica | u3-tcl, u3-concurrencia | **conservar** | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| unidad-3/practica/laboratorio-aislamiento | u3-concurrencia | **corregir** | 5 | 0 | 1 | 5 | 3 | 1 | 1 |
| unidad-3/practica/laboratorio-tcl | u3-tcl, u3-concurrencia | **corregir** | 4 | 0 | 1 | 7 | 3 | 1 | 0 |
| unidad-3/teoria | u3-concurrencia, u3-tcl, u3-indices, u3-monitoreo | **corregir** | 1 | 0 | 1 | 0 | 0 | 0 | 2 |
| unidad-3/teoria/indices-optimizacion | u3-indices, u3-plan-ejecucion, u3-estadisticas, u3-monitoreo, u3-rowstore-columnstore, u3-optimizacion | **reorganizar** | 5 | 1 | 2 | 0 | 4 | 2 | 4 |
| unidad-3/teoria/indices-y-planes | u3-plan-ejecucion, u3-estadisticas, u3-indices, u3-optimizacion, u3-rowstore-columnstore | **corregir** | 6 | 0 | 1 | 0 | 8 | 2 | 3 |
| unidad-3/teoria/metricas-de-rendimiento | u3-monitoreo | **corregir** | 5 | 0 | 1 | 0 | 7 | 2 | 1 |
| unidad-3/teoria/transacciones-concurrencia | u3-tcl, u3-concurrencia, u3-bloqueos, u3-distribuidas | **reorganizar** | 5 | 0 | 1 | 0 | 3 | 2 | 3 |
| unidad-3/teoria/transacciones-y-concurrencia | u3-tcl, u3-concurrencia, u3-bloqueos | **corregir** | 5 | 0 | 2 | 0 | 7 | 2 | 2 |
| unidad-4/practica | u4-mql-crud, u4-agregacion | **corregir** | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| unidad-4/practica/ejercicios | u4-mql-crud, u4-agregacion, u4-estadisticas-indices | **corregir** | 5 | 0 | 2 | 11 | 4 | 2 | 0 |
| unidad-4/practica/integrador-peliculas | u4-mql-crud, u4-agregacion, u4-estadisticas-indices | **investigar** | 3 | 0 | 1 | 6 | 2 | 2 | 1 |
| unidad-4/practica/laboratorio-tienda-online | u4-mql-crud, u4-agregacion, u4-estadisticas-indices | **reemplazar** | 3 | 0 | 1 | 8 | 2 | 2 | 1 |
| unidad-4/teoria | u4-base-acid, u4-modelos-datos, u4-data-lakes, u4-kdd-datamining | **corregir** | 2 | 1 | 1 | 0 | 0 | 1 | 1 |
| unidad-4/teoria/apunte-completo | u4-base-acid, u4-tipos-nosql, u4-mql-crud, u4-agregacion, u4-estadisticas-indices, u4-data-lakes, u4-kdd-datamining, u4-modelos-datos | **reorganizar** | 4 | 0 | 6 | 0 | 5 | 2 | 3 |
| unidad-4/teoria/datos-data-lake-kdd | u4-data-lakes, u4-kdd-datamining, u4-modelos-datos | **investigar** | 3 | 1 | 1 | 1 | 0 | 4 | 1 |
| unidad-4/teoria/guia-parcial | u4-base-acid, u4-mql-crud, u4-agregacion, u4-estadisticas-indices, u4-data-lakes | **corregir** | 4 | 1 | 1 | 2 | 2 | 1 | 1 |
| unidad-4/teoria/instalacion-mongodb | u4-mql-crud | **conservar** | 3 | 1 | 2 | 0 | 1 | 1 | 0 |
| unidad-4/teoria/mongodb-agregacion | u4-agregacion, u4-estadisticas-indices | **corregir** | 6 | 0 | 2 | 0 | 9 | 1 | 2 |
| unidad-4/teoria/mongodb-compass | u4-mql-crud, u4-estadisticas-indices | **conservar** | 2 | 0 | 2 | 0 | 2 | 1 | 1 |
| unidad-4/teoria/mongodb-crud | u4-mql-crud | **ampliar** | 5 | 0 | 2 | 0 | 5 | 1 | 1 |
| unidad-4/teoria/mongodb-introduccion | u4-mql-crud, u4-modelos-datos | **conservar** | 3 | 0 | 2 | 0 | 2 | 0 | 2 |
| unidad-4/teoria/nosql-conceptos | u4-base-acid, u4-tipos-nosql, u4-modelos-datos | **conservar** | 3 | 0 | 1 | 0 | 2 | 1 | 3 |
| unidad-5/practica |  | **conservar** | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| unidad-5/practica/laboratorio-backup | u5-backups, u5-recuperacion | **corregir** | 3 | 0 | 1 | 3 | 3 | 0 | 0 |
| unidad-5/practica/laboratorio-inyeccion |  | **corregir** | 2 | 0 | 1 | 2 | 3 | 0 | 0 |
| unidad-5/practica/laboratorio-seguridad | u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles, u5-minimo-privilegio | **corregir** | 3 | 0 | 1 | 4 | 3 | 0 | 0 |
| unidad-5/teoria | u5-minimo-privilegio, u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles, u5-alta-disponibilidad, u5-backups, u5-recuperacion, u5-cifrado | **corregir** | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| unidad-5/teoria/alta-disponibilidad | u5-alta-disponibilidad | **corregir** | 2 | 0 | 1 | 0 | 1 | 2 | 2 |
| unidad-5/teoria/apunte-completo | u5-minimo-privilegio, u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles, u5-alta-disponibilidad, u5-backups, u5-recuperacion, u5-cifrado | **reorganizar** | 1 | 0 | 7 | 0 | 2 | 1 | 1 |
| unidad-5/teoria/backup-restauracion | u5-backups, u5-recuperacion | **conservar** | 2 | 0 | 2 | 0 | 3 | 1 | 0 |
| unidad-5/teoria/cifrado | u5-cifrado | **corregir** | 1 | 0 | 1 | 1 | 5 | 1 | 1 |
| unidad-5/teoria/guia-parcial | u5-minimo-privilegio, u5-permisos-dcl, u5-backups, u5-recuperacion, u5-alta-disponibilidad, u5-cifrado | **corregir** | 3 | 0 | 1 | 2 | 0 | 0 | 1 |
| unidad-5/teoria/inyeccion-sql |  | **conservar** | 1 | 0 | 2 | 0 | 2 | 1 | 1 |
| unidad-5/teoria/log-recuperacion | u5-recuperacion | **conservar** | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
| unidad-5/teoria/seguridad-permisos | u5-minimo-privilegio, u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles | **conservar** | 1 | 0 | 2 | 1 | 4 | 0 | 1 |
| unidad-6/practica |  | **conservar** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| unidad-6/practica/casos-integradores | u6-iso-25012, u6-ley-25326, u6-gdpr | **conservar** | 1 | 0 | 1 | 1 | 0 | 1 | 1 |
| unidad-6/practica/laboratorio-calidad | u6-iso-25012 | **corregir** | 2 | 0 | 1 | 2 | 2 | 0 | 0 |
| unidad-6/practica/laboratorio-privacidad | u6-ley-25326, u6-gdpr | **ampliar** | 3 | 0 | 2 | 2 | 0 | 1 | 0 |
| unidad-6/teoria | u6-ley-25326, u6-gdpr, u6-iso-25012 | **corregir** | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| unidad-6/teoria/apunte-completo | u6-ley-25326, u6-gdpr, u6-iso-25012 | **reorganizar** | 1 | 0 | 6 | 0 | 0 | 4 | 1 |
| unidad-6/teoria/gdpr | u6-gdpr | **investigar** | 2 | 0 | 1 | 0 | 1 | 2 | 1 |
| unidad-6/teoria/gobierno-privacidad |  | **reorganizar** | 0 | 1 | 2 | 0 | 0 | 1 | 1 |
| unidad-6/teoria/guia-parcial | u6-ley-25326, u6-gdpr, u6-iso-25012 | **corregir** | 2 | 0 | 2 | 2 | 0 | 2 | 1 |
| unidad-6/teoria/iso-25012 | u6-iso-25012 | **conservar** | 0 | 0 | 2 | 0 | 0 | 1 | 1 |
| unidad-6/teoria/ley-25326 | u6-ley-25326 | **investigar** | 2 | 0 | 2 | 1 | 0 | 4 | 2 |
| unidad-6/teoria/medicion-calidad |  | **conservar** | 1 | 0 | 2 | 0 | 2 | 1 | 0 |

## 6. Plan de reorganización propuesto (no ejecutado)

Se conservan todas las URL actuales. Una fusión o un traslado deja la ruta anterior como
redirección y se registra en `migration/` (ver `content-guide.md` §2).

| Unidad | Propuesta |
|---|---|
| u1 | `teoria/indice-cluster` pasa a `u3-indices`. En u1 queda, como mucho, una nota breve sobre PK clúster por defecto. Agregar a la teoría: clasificación transaccional/no transaccional, licencias por motor, despliegue, tipos de fecha y cadena, subconsultas correlacionadas, `EXISTS`, `ANY`/`ALL`, funciones de tabla y acciones referenciales. Unificar el esquema de ejemplos de window functions (`wf`, `tablaswf`, `tablasWF`) |
| u2 | `teoria/bd-transaccionales`: dejar OLTP, ACID conceptual, arquitectura e instalación. Trasladar aislamiento, MVCC y WAL a u3, Always On a u5 y DWH/DL a u4. Fusionar `formatos-conectividad` con `formatos-de-intercambio`; la conectividad (drivers, ODBC/JDBC, conexión remota) va a una página propia. `practica/transacciones` pasa a u3. Página nueva: bases de usuario y de sistema |
| u3 | Fusionar `transacciones-concurrencia` (`unidad-3.md`) con `transacciones-y-concurrencia`. Reorganizar `indices-optimizacion`, `indices-y-planes` y `metricas-de-rendimiento` en: plan de ejecución, índices, estadísticas, optimización (reescritura antes/después), rowstore/columnstore y monitoreo. Sacar el modelo de recuperación (va a u5) |
| u4 | Convertir `apunte-completo` en un resumen integrador que enlace las páginas temáticas; la versión con matices es `nosql-conceptos`. Agregar upsert, `bulkWrite` y `explain` completo. Decidir el alcance de POO y de KDD. Reescribir o reemplazar las dos prácticas sin datos |
| u5 | Convertir `apunte-completo` en resumen integrador. Ampliar autenticación y directivas de contraseña (cátedra p.9, 11–13). Corregir alta disponibilidad, cifrado y los laboratorios de inyección, seguridad y backup |
| u6 | Contrastar cada afirmación normativa con el texto oficial antes de conservarla. Convertir `apunte-completo` en resumen. Rotular `medicion-calidad` y `gobierno-privacidad` como complementarios o retirarlos de la navegación principal |
| Índices y portada | Títulos del programa 2024; sin "1er/2do parcial"; esquema de evaluación 2024; Gils Carbó en la bibliografía complementaria; enlaces "← Unidad" de u5 y u6 a su unidad |

## 7. Decisiones pendientes antes de reescribir

1. **Versión del programa.**
   - Confirmar con la cátedra si existe un programa 2025 o 2026.
   - Mientras tanto se usa el 2024, y el portal adopta su terminología y su esquema de evaluación.
   - El nombre "Parcial 1" del examen de 2C2026 no alcanza para suponer dos parciales.
2. **Títulos de las unidades.** Pasar a "relacionales" y "no relacionales" en los títulos visibles,
   conservando las URL. Propuesta: sí.
3. **Enunciados de cátedra.**
   - Decidir si se pueden seguir publicando los enunciados reproducidos (TP 1, TP 2, guía de window
     functions, guía de MongoDB), o si se reemplazan por ejercicios propios equivalentes.
   - La guía de contenido conserva identificadores al reproducir, pero no agrega enunciados nuevos hasta que esto se decida.
4. **Fuentes primarias de u6.** Definir las fuentes:
   - Ley 25.326 y su decreto reglamentario (InfoLEG).
   - GDPR (Reglamento UE 2016/679, EUR-Lex).
   - ISO/IEC 25012: la norma es paga; se puede usar la vista previa oficial o una fuente secundaria reconocida y declararlo.

   Sin esas fuentes, u6 no puede pasar de `investigar`.
5. **Alcance de `u4-poo` y `u4-kdd`.** No hay material que los desarrolle.
   - Propuesta para POO: desajuste de impedancia, mapeo objeto-documento y ODM.
   - Propuesta para KDD: formulación de Fayyad et al. (1996) en 5 etapas, con cita. No conservar las 7 etapas sin fuente.
6. **Temas extra** (sección 10): para cada uno, conservar como complementario y rotularlo, o retirarlo.
   - Inyección SQL.
   - Medición de calidad.
   - Gobierno de datos.
   - In-Memory OLTP en profundidad.
   - OLE Automation.
   - FCI.
   - Always Encrypted.
   - Variantes avanzadas de MongoDB.
7. **Verificación de código.**
   - Disponer de un entorno reproducible: un contenedor de SQL Server 2022 y MongoDB 7 con `mongosh`.
   - Extender el pipeline con una verificación de motor; hoy `qa` solo acepta `sympy | razonamiento`.
   - Sin esto, ningún ejercicio con código puede marcarse como verificado.
8. **Control de `$` en `qa` para esta materia.**
   - Decidir si se desactiva el control de fórmulas en BBDD.
   - Alternativa: se exige formato de código a los operadores y se escriben los montos sin `$` suelto, como dice la guía.
9. **Mínimos de ejercicios por unidad y niveles.** Propuesta: 15 por unidad (5 por nivel) en u1–u4 y
   8 en u5–u6. Además, una guía estilo parcial para u1–u4 y otra estilo final para u5–u6.
10. **Datos de práctica.** Publicar conjuntos de datos propios y sintéticos para las prácticas de u4
    (películas y préstamos, tienda), o reescribirlas sobre `datosventas_1.json`.
11. **Nombres pendientes.** Esquema propio para los ejemplos T-SQL y convención de colecciones y campos en MongoDB.
12. **Seguridad (de la fase anterior).**
    - Avisar a la titular de la credencial de `Instalación MongoDB.pdf`.
    - Autorizar el despliegue que retira los dos PDF de cátedra de producción.

## 8. Detalle por tema

### `u1-bd-conceptos` · Qué es una base de datos y su clasificación

- **Programa 2024:** Qué es una base de datos. Por qué necesitamos bases de datos. Clasificación de bases de datos en transaccionales y no transaccionales.
- **Fuentes de cátedra:** `f740763a4b8b` p.3–12
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.1–2; `6939322b728b` p.1–3
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad alta · confianza alta · acción **ampliar**
- **Observaciones:** Qué es una BD, por qué, DBMS y cuándo no usar uno están bien resumidos y fieles a f740763a4b8b p.4-7 y p.12. Falta la clasificación transaccionales / no transaccionales que fija el programa 2024 para u1 (hoy solo aparece OLTP en u2 y no existe una página que contraste ambos). Faltan rasgos de la p.5: naturaleza autodescriptiva, múltiples vistas de los datos, aislación programa-datos.

### `u1-motores-licencias` · Motores modernos y modelos de licenciamiento

- **Programa 2024:** Motores de bases de datos modernos. Modelos de licenciamiento pago vs código abierto.
- **Fuentes de cátedra:** `f740763a4b8b` p.8–11
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.1–34
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura superficial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** Se menciona el ranking (Oracle, MySQL, SQL Server, PostgreSQL, MongoDB) y el ranking argentino, fiel a p.8-9. Pero licenciamiento pago vs código abierto es una sola fila de tabla, sin ejemplos por motor (SQL Server Express/Developer/Standard/Enterprise aparece recién en u2/bd-transaccionales). Se cita la 'encuesta de sueldos de OpenQube 2025': ese nombre no figura en la diapositiva p.9-10 ni en ningún documento del corpus (requiere fuente). Los porcentajes de p.9-10 (31,79 % / 44,17 %) no se reproducen.

### `u1-dba` · Tareas del administrador de bases de datos

- **Programa 2024:** Tareas del administrador de la base de datos.
- **Fuentes de cátedra:** `f740763a4b8b` p.13–14
- **Referencias de alumnos (no verificadas):** `6939322b728b` p.1–3; `cd36d917c66c` p.4; `3a0d8f223fcf` p.2
- **Exámenes que lo evalúan:** 2
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Tabla DBA vs programador fiel a p.13-14. Menor: 'tareas del DBA' del programa (accesos, monitoreo, adquisición de HW/SW, disponibilidad) están condensadas; el portal agrega 'backups' que no figura textualmente en p.13.

### `u1-despliegue` · Bases de datos embebidas, on premise y cloud

- **Programa 2024:** Características y diferencias de las bases de datos embebidas, On Premise y Cloud.
- **Fuentes de cátedra:** `f740763a4b8b` p.11–12; `d0b0a9b78ca8` p.10–17
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.1
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura superficial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** La cátedra solo plantea la pregunta 'embebida, on premise, cloud' (p.11) y la retoma en u2 p.10 y p.17. El portal la reduce a una fila de tabla en u1 y a dos párrafos en u2 (modalidades de despliegue). No hay definición de BD embebida (SQLite, SQL Server Express LocalDB, etc.) ni comparación on-premise vs cloud (IaaS/PaaS/DBaaS) en ninguna página. Con la fuente actual no se puede ampliar más allá de lo que dice la cátedra sin material externo.

### `u1-tipos-datos` · Tipos de datos básicos

- **Programa 2024:** Tipos de datos básicos.
- **Fuentes de cátedra:** `9d5ab3349985` p.7–14
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.2–8; `cd36d917c66c` p.4–14
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** La p.14 cubre enteros, bit, decimal/numeric, fecha-hora (datetime, smalldatetime, date, time), punto flotante, char/nchar/varchar/nvarchar. El portal tiene una tabla numérica detallada (rangos y bytes correctos) y solo una nota sobre varchar/nvarchar. Faltan fecha y hora (date, time, datetime2, datetimeoffset), cadenas (char, varchar, nchar, nvarchar, max), uniqueidentifier, xml y la distinción tipos ANSI vs propios del RDBMS.

### `u1-ddl-dml-esquemas` · Repaso de SQL: DDL, DML y esquemas

- **Programa 2024:** Repaso de SQL: DDL, DML. Esquemas.
- **Fuentes de cátedra:** `9d5ab3349985` p.4–13; `95d8b07bd5dd` p.2–3
- **Referencias de alumnos (no verificadas):** `6939322b728b` p.1–4
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Abstracción, catálogo-esquema-objeto, CREATE/DROP/ALTER/TRUNCATE y DML cubiertos. Problemas: mezcla de esquemas de ejemplo (bbdda y ddbba) y de convenciones; en tp1 el ejercicio 2 junta USE y CREATE SCHEMA en un mismo lote (error: CREATE SCHEMA debe ser la primera sentencia del lote).

### `u1-integridad` · Integridad referencial, claves y restricciones

- **Programa 2024:** Integridad referencial, claves primarias y foráneas. Actualización y borrado en cascada. Constraints.
- **Fuentes de cátedra:** `9d5ab3349985` p.5–21
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.2–5; `cd36d917c66c` p.4–5
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **corregir**
- **Observaciones:** PK/FK/UNIQUE/CHECK/DEFAULT y clustered por defecto bien explicados. Falta detalle de ON DELETE/ON UPDATE (solo CASCADE; faltan NO ACTION, SET NULL, SET DEFAULT) y de integridad referencial con ejemplo de error. El ejemplo de FK compuesta (examen -> curso(id_curso, dni)) es incoherente. 'NULL = NULL siempre es FALSE' es impreciso: evalúa a UNKNOWN.

### `u1-subconsultas` · Subconsultas

- **Programa 2024:** Subconsultas en el where, en el from y en el select.
- **Fuentes de cátedra:** `9d5ab3349985` p.28–29
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.2
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura superficial · calidad media · confianza media · acción **ampliar**
- **Observaciones:** Solo hay subconsulta en WHERE (IN) y en FROM. El programa exige WHERE/FROM/SELECT: falta subconsulta escalar en SELECT, correlacionada, EXISTS/NOT EXISTS, ANY/ALL. También faltan CROSS/SELF JOIN y la variante 'LEFT JOIN sin intersección' que muestra la cátedra en p.25.

### `u1-vistas-agregados` · Vistas y funciones de agregado

- **Programa 2024:** Vistas. Funciones de agregado.
- **Fuentes de cátedra:** `9d5ab3349985` p.29–33
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.2
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Vistas con SCHEMABINDING y agregados con HAVING correctos. Dudoso: 'no puede incluir ... más de una tabla base' para DML sobre vistas es excesivo (una vista de varias tablas admite DML que afecte una sola tabla base). No se explica por qué SCHEMABINDING (ej. 12 del TP1) bloquea ALTER TABLE ni vistas indexadas.

### `u1-programabilidad` · Procedimientos almacenados, triggers y funciones

- **Programa 2024:** Procedimientos almacenados, triggers y funciones.
- **Fuentes de cátedra:** `9d5ab3349985` p.34–41
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.2–8; `cd36d917c66c` p.4–10
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **corregir**
- **Observaciones:** SP, triggers (AFTER, INSTEAD OF, DDL, logon) y funciones escalares cubiertos. Error de ejemplo: el SP inscribir_alumno inserta en bbdda.inscripcion(dni, id_curso, fecha) pero la tabla definida arriba en la misma página es inscripcion(id_alumno, id_materia, fecha_inscripcion). Faltan funciones de tabla (inline y multi-statement), pseudotablas inserted/deleted con ejemplo de UPDATE, y la advertencia de que el trigger se ejecuta por sentencia y no por fila.

### `u1-window` · Window functions

- **Programa 2024:** Window functions.
- **Fuentes de cátedra:** `d275f59f2093` p.2–36; `9d5ab3349985` p.42–44; `7d43d771a356` p.2–26
- **Referencias de alumnos (no verificadas):** `df183295a1ee` secc.s001; `3a0d8f223fcf` p.10–14
- **Exámenes que lo evalúan:** 10
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Es el tema más evaluado después de PIVOT. Cubre ranking, NTILE, LAG/LEAD, FIRST/LAST_VALUE, PERCENT_RANK/CUME_DIST, frames y agregados OVER. Correcciones: (1) el ejemplo 'SUM(...) OVER (PARTITION BY depto ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)' no tiene ORDER BY y SQL Server exige ORDER BY para usar ROWS/RANGE: verificar en motor; (2) CUME_DIST = filas con valor <= actual / total, no 'rank/total' (difiere con empates); (3) falta el frame por defecto (RANGE UNBOUNDED PRECEDING..CURRENT ROW cuando hay ORDER BY) que explica el problema clásico de LAST_VALUE; (4) la práctica no reproduce los 'Resultado esperado' de la guía. Ver detalle por página.

### `u1-cte` · Common table expressions

- **Programa 2024:** Common table expressions.
- **Fuentes de cátedra:** `9d5ab3349985` p.45–47; `95d8b07bd5dd` p.3
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.10–14; `cd36d917c66c` p.5–7
- **Exámenes que lo evalúan:** 3
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **corregir**
- **Observaciones:** CTE simple, múltiple, recursiva y DELETE sobre CTE (ej. 9 del TP1) correctos. Los ejemplos usan el esquema tablaswf, mientras la práctica de WF del portal creó el esquema wf: no corren juntos. Falta aclarar que la sentencia previa debe terminar en punto y coma y que la CTE no es reutilizable en otra sentencia.

### `u1-pivot` · Pivot

- **Programa 2024:** Pivot.
- **Fuentes de cátedra:** `9d5ab3349985` p.50–51; `95d8b07bd5dd` p.4
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.15; `cd36d917c66c` p.2–7; `6939322b728b` p.1–8
- **Exámenes que lo evalúan:** 11
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** PIVOT aparece en 11 de 14 exámenes del corpus; es el tema de u1 con mejor práctica en el portal (el integrador 1 está reelaborado a partir del parcial 047fcb3ca752, con datos propios; verifiqué sus resultados contra el setup y son correctos). Errores: ejercicio 5 de la práctica no ejecuta (GO separa el lote y se pierde @cols; además ORDER BY sobre columna no agregada en una consulta con STRING_AGG; usar WITHIN GROUP). Ver detalle.

### `u1-null` · El valor NULL

- **Programa 2024:** El valor null.
- **Fuentes de cátedra:** `9d5ab3349985` p.22
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.2
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Buen tratamiento de ISNULL vs COALESCE (el ejemplo del truncamiento a CHAR(3) es correcto). Corregir: 'NULL = NULL es FALSE' debería decir UNKNOWN (y por qué NOT IN con NULL devuelve vacío). Falta NULLIF (usado en el propio TP1/ej.4) y el efecto de ANSI_NULLS.

### `u2-arquitectura` · Arquitectura de las bases de datos relacionales

- **Programa 2024:** Arquitectura de las bases de datos relacionales. Bases de datos populares en el mercado.
- **Fuentes de cátedra:** `d0b0a9b78ca8` p.9–17
- **Referencias de alumnos (no verificadas):** `cd36d917c66c` p.2–8
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza media · acción **ampliar**
- **Observaciones:** La arquitectura distribuida/clúster (p.9-10) está cubierta, pero con material propio (Always On, failover) que la cátedra de u2 no menciona (Always On aparece solo en la cátedra de u5, 5db2ce42f603). No hay una explicación de la arquitectura interna de un motor (instancia, servicios, procesos, archivos de datos/log) ni de 'BD populares' como tema aparte: están dispersas entre u1/conceptos-basicos (ranking) y u2.

### `u2-bd-sistema` · Bases de datos de usuario y de sistema

- **Programa 2024:** Bases de datos de usuario y de sistema.
- **Fuentes de cátedra:** `d0b0a9b78ca8` p.18–19
- **Referencias de alumnos (no verificadas):** `1a42e094e00e` p.1–10; `3c6cac1c3ff5` p.24–32
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura ausente · calidad sin-evaluar · confianza media · acción **ampliar**
- **Observaciones:** No hay ninguna página sobre BD de usuario vs BD de sistema (master, model, msdb, tempdb, resource). Solo se menciona tempdb dentro de tablas temporales y la collation de tempdb. La cátedra (p.18) pide planificar ubicación de BD de usuario, de sistema y tempdb.

### `u2-instalacion` · Instalación de un motor de base de datos

- **Programa 2024:** Instalación de un motor de base de datos.
- **Fuentes de cátedra:** `d0b0a9b78ca8` p.16–21; `242399d569be` p.2
- **Referencias de alumnos (no verificadas):** `1a42e094e00e` p.1–10
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** El portal cubre componentes, ediciones, instancias, Configuration Manager, conexión remota y autenticación (la p.21 de la cátedra lista exactamente esos pasos). Faltan: análisis previo a la instalación (p.17: VM/bare metal, memoria, núcleos, réplicas, respaldos), ubicación de datos/tempdb/respaldos y RAID (p.18), memoria máxima por defecto (p.20, 'por default utiliza la totalidad'), características opcionales (p.16).

### `u2-collation` · Intercalación (collation)

- **Programa 2024:** Intercalación (collation).
- **Fuentes de cátedra:** `d0b0a9b78ca8` p.19–23; `242399d569be` p.2–3
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.18; `cd36d917c66c` p.2–8; `6939322b728b` p.9
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **ampliar**
- **Observaciones:** Tema muy bien cubierto y fiel a p.22-23. Falta lo que exige el TP2: COLLATE database_default, el conflicto de collation en UNION/INTERSECT, y que tempdb hereda la collation de la instancia (se menciona en bd-en-memoria y en el ej. 15 de tp2 pero no en esta página).

### `u2-almacenamiento` · Almacenamiento en disco y en memoria

- **Programa 2024:** Almacenamiento en disco vs en memoria.
- **Fuentes de cátedra:** `d0b0a9b78ca8` p.24–28
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.18–19; `cd36d917c66c` p.2–8
- **Exámenes que lo evalúan:** 2
- **Estado:** cobertura completo · calidad media · confianza media · acción **corregir**
- **Observaciones:** Cubre disco vs memoria con sobreabundancia respecto a la cátedra (p.24-28 son 5 diapositivas): NVRAM, snapshots, Hekaton, índices hash, compilación nativa y SCHEMA_ONLY no aparecen en ningún documento del corpus (requieren fuente: probablemente guías externas citadas en p.27 'Ver guía de Tablas en memoria'). Contiene afirmaciones desactualizadas sobre limitaciones de tablas en memoria (ver página).

### `u2-conexion-drivers` · Configuración de conexión, drivers, ODBC y JDBC

- **Programa 2024:** Configuración de conexión. Concepto de driver o controlador. Qué es y cómo se usan ODBC y JDBC.
- **Fuentes de cátedra:** `d0b0a9b78ca8` p.21–30
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.19; `cd36d917c66c` p.2–9
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** ODBC/JDBC y cadenas de conexión correctos y más completos que p.29-30. Dudoso: JDBC 'Sun/Oracle (Java EE)' (es parte de Java SE). La conexión local/remota está en bd-transaccionales, ODBC/JDBC en formatos-conectividad: dos páginas distintas para un mismo tema del programa. No se explica qué es un driver/proveedor ni la diferencia con OLE DB.

### `u2-formatos` · Formatos de intercambio

- **Programa 2024:** Formatos de intercambio (XML, JSON, YAML, CSV, etc.).
- **Fuentes de cátedra:** `008193c9c082` p.4–22
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.20–22; `cd36d917c66c` p.2–9; `6939322b728b` p.1–12
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza media · acción **reorganizar**
- **Observaciones:** EDI, CSV, ancho fijo, XML, JSON y YAML cubiertos, pero repartidos y duplicados en 4 páginas. formatos-de-intercambio y formatos-conectividad repiten casi textualmente EDI/CSV/ancho fijo/XML/JSON/YAML con ejemplos levemente distintos (dos versiones del XML de ejemplo, dos del JSON). El T-SQL de XML/JSON (OPENJSON, FOR XML, OPENXML) no tiene respaldo en el corpus: la cátedra p.12-21 solo presenta los formatos. Recomendación: una sola página de formatos (teoría) y dos guías T-SQL.

### `u2-apis` · Qué es una API

- **Programa 2024:** Qué es una API.
- **Fuentes de cátedra:** `008193c9c082` p.23–26
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.19–22; `6939322b728b` p.9–10
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad media · confianza media · acción **corregir**
- **Observaciones:** Qué es una API, tipos, REST/SOAP, Postman: respaldado por p.23-26 (aunque 'tipos de API' y SOAP/XML-RPC/JSON-RPC no aparecen en esas diapositivas). Llamadas HTTP desde T-SQL con Ole Automation: sin respaldo en el corpus; la teoría tiene una advertencia correcta pero falta sp_OADestroy y seguridad (superficie de ataque). Dependencias externas (worldtimeapi, mymemory, jsonplaceholder) pueden no estar disponibles: verificar.

### `u2-importacion` · Importación de datos de múltiples formatos

- **Programa 2024:** Importación de datos de múltiples formatos de origen.
- **Fuentes de cátedra:** `242399d569be` p.2–3; `008193c9c082` p.8–11
- **Referencias de alumnos (no verificadas):** `cd36d917c66c` p.10; `e694c5563d75` secc.s001
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza media · acción **corregir**
- **Observaciones:** BULK INSERT y OPENROWSET+OPENJSON/XML están en la teoría con ejemplos y en la práctica con 4 ejercicios; el TP2 (ej. 5-8) es la importación de cátedra. Faltan: BULK INSERT con FORMAT='CSV' y FIELDQUOTE (campos entrecomillados), archivos de formato, OPENROWSET con SINGLE_NCLOB / CODEPAGE para UTF-8 en JSON, importación de ancho fijo y de YAML, tratamiento de errores (ERRORFILE) y tablas de staging. El respaldo de BULK INSERT/OPENJSON en el corpus es solo un apunte de alumno (cd36d917c66c p.10).

### `u3-concurrencia` · Control de concurrencia y niveles de aislamiento

- **Programa 2024:** Control de concurrencia.
- **Fuentes de cátedra:** `17c2c97f736b` p.14–26
- **Referencias de alumnos (no verificadas):** `6939322b728b` p.2–16; `3c6cac1c3ff5` p.31–32; `42835aeae3f6` p.20–21; `e694c5563d75` p.1–5
- **Exámenes que lo evalúan:** 5
- **Estado:** cobertura completo · calidad media · confianza alta · acción **reorganizar**
- **Observaciones:** Cubre dirty/non-repeatable/phantom y los niveles (incl. SNAPSHOT y RCSI, que la catedra menciona SNAPSHOT en p.23 y RCSI en p.21). Falta de la catedra: planificaciones secuenciales/serializabilidad (p.14), regla de que el X-lock de escritura se mantiene siempre hasta fin de TX (p.18), comportamiento de SET ISOLATION LEVEL dentro de SP/trigger (p.25) y lock S/X en notacion de Silberschatz. Tabla de niveles duplicada en dos paginas. Los examenes piden 'nivel minimo para evitar lectura sucia', clasificar dirty/non-repeatable/phantom y listar los 4 niveles.

### `u3-tcl` · Transaction Control Language

- **Programa 2024:** Transaction Control Language (TCL).
- **Fuentes de cátedra:** `17c2c97f736b` p.4–13
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.16–27; `3c6cac1c3ff5` p.30; `42835aeae3f6` p.21; `e694c5563d75` p.2–8
- **Exámenes que lo evalúan:** 2
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** ACID, implicito/explicito/autocommit, BEGIN/COMMIT/ROLLBACK, SAVE, @@TRANCOUNT, TRY/CATCH y XACT_ABORT estan bien cubiertos (TRY/CATCH, SAVE y XACT_ABORT exceden a la catedra). Faltan: estados de una transaccion (activa, parcialmente comprometida, fallida, abortada; p.6), argumento de durabilidad via log en disco (p.9), verificar IMPLICIT_TRANSACTIONS con @@OPTIONS (p.11) y bulk-logged. Error de contenido en la tabla XACT_ABORT (ver pagina). El laboratorio TCL de la catedra (TCL_0..TCL_9, p.13) usa creditCard_info/Transaccion; el portal renombro identificadores (tarjeta_credito/transaccion). Los experimentos 2 y 3 del portal no son ejecutables como concurrencia (sin WAITFOR).

### `u3-bloqueos` · Bloqueos y esperas

- **Programa 2024:** Bloqueos y esperas.
- **Fuentes de cátedra:** `17c2c97f736b` p.15–41
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.29; `e694c5563d75` p.1–8
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza media · acción **conservar**
- **Observaciones:** La catedra solo tiene lock compartido/exclusivo (p.15) y 'Bloqueos/esperas' como metrica (p.41); deadlocks, prioridad de victima, system_health, U/intent locks, LOCK_TIMEOUT y DMVs son aporte del portal sin fuente de catedra en el corpus (respaldo en alumno e694c5563d75 y conocimiento general SQL Server). Deadlock: sin examenes que lo evaluen en el corpus. Falta un ejemplo ejecutable de bloqueo (SELECT bloqueado) con sp_who/dm_tran_locks y resultado esperado.

### `u3-distribuidas` · Transacciones distribuidas

- **Programa 2024:** Transacciones distribuidas.
- **Fuentes de cátedra:** `17c2c97f736b` p.27–44
- **Referencias de alumnos (no verificadas):** `6939322b728b` p.2–16; `cd36d917c66c` p.15; `42835aeae3f6` p.3–21
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** Cubierto solo en la seccion final de transacciones-concurrencia (unidad-3.md) y NO en transacciones-y-concurrencia. Falta: sintaxis y argumentos de BEGIN DISTRIBUTED (transaction_name <=32 caracteres, variable char/varchar; cat p.28), rol de MS DTC con mas detalle, requisito de linked server configurado (RPC/MSDTC habilitado), commit en dos fases (2PC) como concepto, y que la catedra cita el mismo link de bibliografia para ambos temas (p.44, enlace aparentemente erroneo). Ejemplo del portal usa pruebasDB.ddbba.candidatos sin DDL; el de la catedra usa AdventureWorks2022.HumanResources.JobCandidate.

### `u3-monitoreo` · Monitoreo y métricas de performance

- **Programa 2024:** Monitoreo y métricas de performance.
- **Fuentes de cátedra:** `17c2c97f736b` p.31–42
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.29; `3c6cac1c3ff5` p.33; `6939322b728b` p.2–16; `e694c5563d75` p.5–7
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Baseline, row count, file IO, tamano de backup de log, modelo de recuperacion y esperas estan cubiertos. Faltan: modelo BULK-LOGGED (cat. p.36), limitaciones del modelo SIMPLE (AlwaysOn, mirroring, log shipping; p.39), ventajas/limitaciones de cada metrica (cat. p.34-35, 40), metricas de HW (CPU/memoria), deadlocks como metrica (p.32) y Activity Monitor ('el ECG de SQL', p.31) con mas detalle que una mencion. La mitad de 'metricas de rendimiento' esta duplicada en indices-optimizacion y metricas-de-rendimiento (tabla Simple/Full textual repetida).

### `u3-plan-ejecucion` · Interpretación del plan de ejecución

- **Programa 2024:** Interpretación del plan de ejecución.
- **Fuentes de cátedra:** `0d2ad822befa` p.4–10
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.6–24; `3c6cac1c3ff5` p.27–29; `6939322b728b` p.6–13; `1a42e094e00e` p.11; `cd36d917c66c` p.11
- **Exámenes que lo evalúan:** 3
- **Estado:** cobertura superficial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** El portal describe operadores (table scan, seek, scan, key lookup), Ctrl+M/Ctrl+L y plan cache, pero omite lo central de la catedra: las dos fases (compilacion/ejecucion), Query Parser, Algebrizer, Optimizer, Execution Engine (p.5-8), reutilizacion por hash del query tree y causas de invalidacion (p.7), plan estimado vs real y que solo existe un plan por consulta (p.9), como leer un plan (derecha-izquierda, memory grant, warnings, nivel de optimizacion TRIVIAL/FULL/Timeout, p.10), SP posterga la resolucion de nombres (p.6). Un examen (04b9) presenta un plan con alto consumo de memoria.

### `u3-indices` · Índices clúster y no clúster

- **Programa 2024:** Índices clúster vs no clúster.
- **Fuentes de cátedra:** `0d2ad822befa` p.11–20
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.4–25; `3c6cac1c3ff5` p.28–29; `42835aeae3f6` p.18–19; `e694c5563d75` p.1–8
- **Exámenes que lo evalúan:** 9
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **reorganizar**
- **Observaciones:** Clustered/nonclustered, covering/INCLUDE, fill factor, page split y rebuild vs reorganize estan; el tema mas evaluado en examenes (crear indice de cobertura / cluster / no cluster para una consulta dada). Faltan: selectividad (cat. p.14), clave de cluster unica o uniquefier de 4 bytes (p.19), que la tabla sin cluster es heap, preguntas de optimizacion de indices (p.18-19: indices no usados, costo de mantenimiento, INCLUDE raros, UNIQUE), desventajas de fill factor bajo (p.17), aviso de mirroring en rebuild, ejercicios guiados con DDL+datos+plan esperado para 'proponer indice para esta consulta' (formato de examen). Contenido de indices triplicado: indices-optimizacion, indices-y-planes (seccion 'Tipos de indices') y, parcialmente, la teoria de la catedra.

### `u3-estadisticas` · Estadísticas

- **Programa 2024:** Estadísticas.
- **Fuentes de cátedra:** `0d2ad822befa` p.21–24
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.23–29; `cd36d917c66c` p.14; `1a42e094e00e` p.10; `e694c5563d75` p.1–8
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Bien cubierto: encabezado/densidad/histograma (hasta 200 pasos), DBCC SHOW_STATISTICS, sp_updatestats, UPDATE STATISTICS FULLSCAN/SAMPLE, sync vs async, columnas del histograma. Faltan: estadisticas filtradas y creacion manual de estadisticas (CREATE STATISTICS; cat. p.23, p.28), cardinalidad como concepto, cuando conviene crearlas a mano (columnas correlacionadas). Errores puntuales en el script sp_MSforeachdb y ejemplos de KEY LOOKUP (ver pagina).

### `u3-optimizacion` · Optimización de consultas

- **Programa 2024:** Optimización de consultas: reescritura de sentencias SQL, reconfiguración de tablas e índices.
- **Fuentes de cátedra:** `0d2ad822befa` p.8–29
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.4–24; `cd36d917c66c` p.9–14; `3c6cac1c3ff5` p.24; `e694c5563d75` p.5–7
- **Exámenes que lo evalúan:** 3
- **Estado:** cobertura superficial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** Hay solo una lista de 'consejos' (SELECT *, cursores, CHAR vs NCHAR, SP parametrizados, NOLOCK, variables de tabla). El programa pide 'reescritura de sentencias SQL, reconfiguracion de tablas e indices'. Faltan ejemplos antes/despues con plan y metricas: subconsultas -> JOIN/CTE, minimizar SELECT, sargabilidad de WHERE/JOIN (funciones sobre columnas, LIKE con comodin inicial), tipos de datos (abuso de float, CHAR vs VARCHAR con relleno de espacios, Unicode; cat. p.26), tablas temporales y las 8 reglas de uso (p.29), variables de tabla con indice cluster (p.25), checklist 'Mi consulta tarda mucho' (p.28: red, recursos, backups, estadisticas, FULLSAMPLE, estadistica filtrada, normalizacion, hardware, opciones SET). Un examen (efc4) pide reescribir un CREATE TABLE optimizando tipos de datos.

### `u3-rowstore-columnstore` · Rowstore y columnstore

- **Programa 2024:** Rowstore vs Columnstore.
- **Fuentes de cátedra:** `0d2ad822befa` p.30–31
- **Referencias de alumnos (no verificadas):** `68061c008f6a` secc.linea ~1427 (ROWSTORE VS COLUMNSTORE)
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura superficial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** Solo una tabla de 3 filas repetida en dos paginas, sin sintaxis ni ejemplo. Faltan: CREATE CLUSTERED/NONCLUSTERED COLUMNSTORE INDEX, ejemplo con consulta de agregacion/ventana y plan (Columnstore Index Scan, batch mode), compresion, delta store/tuple mover (para explicar el 'mejor si es solo de consulta' de la catedra p.30), relacion con data warehouse y con window functions de u1. Un cambio de lectura: el portal dice 'compresion muy alta' sin respaldo cuantitativo.

### `u4-modelos-datos` · Modelos de datos heterogéneos y tipos de datos

- **Programa 2024:** Modelos de datos heterogéneos: jerárquicos, texto, grafos. Datos estructurados y no estructurados.
- **Fuentes de cátedra:** `ed6885ded031` p.3–24
- **Referencias de alumnos (no verificadas):** `3c6cac1c3ff5` p.5–25; `3a0d8f223fcf` p.3–18; `6939322b728b` p.10–11
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura parcial · calidad alta · confianza media · acción **ampliar**
- **Observaciones:** Estructurados/semiestructurados/no estructurados + OCR/NLP bien cubiertos (datos-data-lake-kdd). Los modelos 'jerarquicos' (IMS, 1966; JSON/XML como estructura jerarquica) solo aparecen de forma indirecta en la linea de tiempo y como 'semiestructurado'; no hay seccion sobre modelo jerarquico ni sobre bases de datos de texto/busqueda de texto completo (ej. indice de texto, motores tipo Elasticsearch); grafos si (Gremlin, cat. p.20-21). El enunciado del programa 'modelos heterogeneos: jerarquicos, texto, grafos' queda cubierto solo en grafos.

### `u4-base-acid` · El modelo BASE y sus diferencias con ACID

- **Programa 2024:** El modelo BASE. Diferencias con ACID.
- **Fuentes de cátedra:** `ed6885ded031` p.10–24
- **Referencias de alumnos (no verificadas):** `6939322b728b` p.17–18; `3c6cac1c3ff5` p.22–24; `cd36d917c66c` p.17–19
- **Exámenes que lo evalúan:** 8
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Muy bien cubierto y de lo mas evaluado (CAP en 5 examenes recientes). Matiza correctamente la etiqueta CP de MongoDB. Observacion: la tabla CA/CP/AP con RDBMS=CA, MongoDB/HBase/Redis=CP viene de la catedra (ed6885ded031 p.24) pero es una simplificacion discutida; el portal ya lo marca en nosql-conceptos, no en apunte-completo (ahi se afirma 'MongoDB es CP' sin matiz). Un examen (1fbe) afirma que no se compromete C o A si la BD tiene un solo nodo: el portal explica que CAP solo importa ante particion (bien).

### `u4-tipos-nosql` · Bases clave-valor, columnares y de documentos

- **Programa 2024:** Bases de datos de pares clave-valor, columnares y de documentos.
- **Fuentes de cátedra:** `ed6885ded031` p.16–24
- **Referencias de alumnos (no verificadas):** `3c6cac1c3ff5` p.34–35; `6939322b728b` p.17; `cd36d917c66c` p.17–18
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Clave-valor, documentos, grafos y columnas con casos de uso y ejemplos de consulta (Gremlin, CQL). Falta la comparacion 'insert relacional vs documental/grafo/columnar' (cat. p.19, 21, 23-24) y ejemplos de INSERT en Cassandra/Cypher; las 'cargas de trabajo' por modelo si estan.

### `u4-mql-crud` · MongoDB Query Language: colecciones y CRUD

- **Programa 2024:** MongoDB Query Language. Clave primaria en MongoDB. Inserción bulk, actualización de colecciones, upsert, remove. Colecciones.
- **Fuentes de cátedra:** `4bd543391072` p.9–33; `f65cc231b1f0` p.5–19; `3df29cd152a2` p.1–2
- **Referencias de alumnos (no verificadas):** `19a1548ac204` p.1–12; `3c6cac1c3ff5` p.35–39; `6939322b728b` p.19–20
- **Exámenes que lo evalúan:** 8
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** CRUD, operadores y fechas BSON bien tratados. Faltan items que el programa nombra: upsert (solo se lo menciona como opcion; la catedra lo trae en 4bd p.31 y guia f65c p.15-16) sin ejemplo ni resultado (upsertedId), insercion bulk con opcion ordered, remove/deleteOne vs el legado remove() (cat. f65c p.19), replaceOne, bulkWrite, $push/$pull con ejemplos, findOne/countDocuments/distinct, sort/skip con ejemplos de salida, importacion con mongoimport. Los examenes evaluan: update de un documento por _id/campo, $inc/$set condicional (ej. 'Moroso' con multa > 1000), sumar y contar con aggregate, equivalencia entre consultas con coma/AND/IN.

### `u4-estadisticas-indices` · Estadísticas de ejecución e índices en MongoDB

- **Programa 2024:** Estadísticas de ejecución. Índices.
- **Fuentes de cátedra:** `9eb38199334b` p.1–13; `4bd543391072` p.40–51; `f65cc231b1f0` p.22–24
- **Referencias de alumnos (no verificadas):** `19a1548ac204` secc.indices (ver pag. 1-12); `6939322b728b` p.19–20
- **Exámenes que lo evalúan:** 2
- **Estado:** cobertura parcial · calidad media · confianza media · acción **corregir**
- **Observaciones:** Indices simple/embebido/compuesto/unico/array/sparse/parcial, COLLSCAN vs IXSCAN y explain('executionStats') cubiertos. 'Estadisticas de ejecucion' se reduce a 3 metricas; faltan nReturned vs totalKeysExamined/totalDocsExamined, winningPlan/stage, explain en aggregate, hint, TTL/hashed/texto/geoespaciales como tipos, orden ESR del indice compuesto, covered queries, y estadisticas de coleccion/indice ($collStats, $indexStats, db.collection.stats()). El ejemplo de dropIndex('cliente.localidad_hashed') proviene del OCR de la catedra (9eb3 p.13) y nunca se crea el indice hashed en el portal; los ejemplos de explain usan una coleccion 'pedidos' de 6 documentos no provista en teoria.

### `u4-agregacion` · Agregación

- **Programa 2024:** Agregado.
- **Fuentes de cátedra:** `9a0d8e90ff05` p.1–33
- **Referencias de alumnos (no verificadas):** `19a1548ac204` p.7–12; `6939322b728b` p.21–24; `cd36d917c66c` p.20–21
- **Exámenes que lo evalúan:** 7
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Cobertura amplia ($match, $project, $addFields, $replaceRoot+$mergeObjects, $lookup, $unwind, $group, $sort/$limit/$skip, $count, $sortByCount, $bucket, $facet, vistas). Error conceptual: $cmp, $multiply y $round figuran como 'operadores de acumulacion' (en realidad son operadores de expresion; los acumuladores de $group son $sum/$avg/$min/$max/$first/$last/$push/$addToSet...). Faltan $dateDiff con $$NOW y formateo de fechas con ejemplo completo (cat. 9a0d p.17), $addFields con fechas, $out/$merge con ejemplo y $setWindowFields (listados sin ejemplo), $addToSet. Los examenes piden completar un aggregate con $match/$group y razonar sobre la salida de un pipeline.

### `u4-poo` · Relación con la programación orientada a objetos

- **Programa 2024:** Relación con POO.
- **Fuentes de cátedra:** **sin fuente de cátedra**
- **Referencias de alumnos (no verificadas):** —
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura ausente · calidad sin-evaluar · confianza baja · acción **investigar**
- **Observaciones:** El programa 2024 (3d97 p.3) lista 'Relacion con POO' en la u4, pero no hay ningun material de catedra ni de alumno en el corpus que lo desarrolle (solo hay una mencion de bases orientadas a objetos en 4bd5 p.2 y el bullet del portal 'puede evitar el desajuste entre objetos de la aplicacion y filas relacionales'). Requiere definir el alcance con la catedra (desajuste de impedancia, mapeo objeto-documento, ODM como Mongoose, bases orientadas a objetos). No inventar contenido sin fuente.

### `u4-data-lakes` · Data lakes y data warehousing

- **Programa 2024:** Data Lakes. (Contenidos mínimos: Data Warehousing.)
- **Fuentes de cátedra:** `3d9721081e14` p.3; `ed6885ded031` p.8–9; `d0b0a9b78ca8` p.11–15
- **Referencias de alumnos (no verificadas):** `3c6cac1c3ff5` p.22–23; `1a42e094e00e` p.9; `3a0d8f223fcf` p.17; `42835aeae3f6` p.13; `6939322b728b` p.9
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza media · acción **conservar**
- **Observaciones:** Respaldo de catedra solo indirecto (programa y ed68 p.8-9, que mencionan datos no estructurados en NoSQL/Data Lake); no hay presentacion de catedra sobre data lakes, la fuente real son apuntes de alumno (DB vs DWH vs DL). El portal agrega gobierno (data swamp, lineage, zonas raw/depurada/consumo), que es correcto pero es aporte propio sin fuente en el corpus; conviene rotularlo. Data Warehousing esta en los contenidos minimos y solo tiene una tabla comparativa; no hay modelado dimensional (estrella, hechos/dimensiones) ni ETL/ELT.

### `u4-kdd` · Introducción al data mining y KDD

- **Programa 2024:** Introducción al Data Mining. Knowledge Discovery in Databases.
- **Fuentes de cátedra:** `3d9721081e14` p.3; `ed6885ded031` p.10
- **Referencias de alumnos (no verificadas):** `e40f44016a23` secc.mencion de mineria de datos; docx sin paginas
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura superficial · calidad media · confianza baja · acción **investigar**
- **Observaciones:** DISCREPANCIA con el brief: el programa 2024 del corpus incluye 'Introduccion al Data Mining. Knowledge Discovery in Databases' dentro de la u4 y tambien KDD y Data Warehousing en contenidos minimos. El portal desarrolla KDD en 7 etapas (la formulacion clasica de Fayyad es de 5: seleccion, preprocesamiento, transformacion, minería, interpretacion/evaluacion); las 7 etapas con 'integracion' y 'presentacion y decision' no tienen fuente de catedra en el corpus (requiere fuente primaria: Fayyad, Piatetsky-Shapiro y Smyth 1996). Ningun material de catedra desarrolla KDD y ningun examen del corpus lo evalua.

### `u5-minimo-privilegio` · Principio del mínimo privilegio

- **Programa 2024:** Principio del mínimo privilegio. Clasificación de usuarios.
- **Fuentes de cátedra:** `5db2ce42f603` p.3–8
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.31; `9a9e789db872` secc.s001; `e40f44016a23` secc.s001
- **Exámenes que lo evalúan:** 2
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Cátedra p.4-6: seguridad vs protección, POLP, reducción de superficie, medidas de protección. El portal reproduce y amplía (defensa en profundidad, separación de funciones). Final cf1a40d118d4 pide explicar el principio de menor privilegio (ítem 6). Definiciones del portal coinciden con p.4 (seguridad = ausencia de riesgo; protección = mecanismos).

### `u5-autenticacion` · Autenticación y directivas de contraseñas

- **Programa 2024:** Autenticación y directivas de contraseñas.
- **Fuentes de cátedra:** `5db2ce42f603` p.8–13
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.31–32; `9a9e789db872` secc.s001; `e40f44016a23` secc.s001
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura parcial · calidad media · confianza alta · acción **ampliar**
- **Observaciones:** Autenticación y directivas de contraseña SÍ figuran en el programa 2024 y en cátedra p.9 (sensible a mayúsculas, complejidad: largo mínimo y 3 de 4 categorías, CHECK_POLICY, regla del SO, CHECK_EXPIRATION, cambio en próximo login, cuidado con caracteres en ODBC) y p.11-12 (CREATE LOGIN, 6 formas de usuario). El portal (apunte-completo §3 «Directivas de contraseña») es una versión comprimida: omite sensibilidad a mayúsculas, regla de 3 de 4 categorías, largo mínimo y la salvedad de que con Windows rigen las políticas del SO. No hay sección propia de autenticación (Windows vs SQL; modo mixto) ni qué hace sa deshabilitado con código. El final 8d75a3b284ab (ítem 4) pide crear LOGIN con contraseña dada y otorgar permisos a un user: cubierto por seguridad-permisos y laboratorio-seguridad, pero sin ejercicio equivalente de examen. Falta mencionar CREATE USER ... WITHOUT LOGIN/certificado con ejemplo (cátedra p.12 lo muestra) aunque el portal lo enumera.

### `u5-permisos-dcl` · Estructura de permisos y DCL

- **Programa 2024:** Estructura de permisos. Data Control Language (DCL).
- **Fuentes de cátedra:** `5db2ce42f603` p.19–23
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.31–32; `9a9e789db872` secc.s001
- **Exámenes que lo evalúan:** 3
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Es el tema más evaluado de u5: los 3 finales traen un ejercicio de GRANT/DENY/REVOKE con SI/NO sobre consultas (d8ba ítem 1 con permisos contradictorios rol vs usuario; cf1a ítem 1; 8d75 ítem 4). El portal explica correctamente REVOKE vs DENY, jerarquía, CASCADE y GRANT OPTION (cátedra p.19-22). Falta un ejercicio tipo examen resuelto (secuencia de GRANT/DENY/REVOKE sobre rol y usuario + tabla de consultas SI/NO) que replique exactamente el formato de los finales; el laboratorio-seguridad Parte 5 lo aproxima.

### `u5-propietarios-roles` · Propietarios y roles

- **Programa 2024:** Configuración mediante propietarios y roles.
- **Fuentes de cátedra:** `5db2ce42f603` p.14–23
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.31–32; `9a9e789db872` secc.s001
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Roles fijos de servidor y de base, propietarios (irrevocables), ALTER AUTHORIZATION y ownership chaining (cátedra p.14-18, 23). Portal añade roles ##MS_*## de SQL Server 2022 (no está en cátedra; la cátedra p.14 solo dice «en la última versión se pueden crear roles definidos por el usuario»): verificar versión contra documentación de Microsoft.

### `u5-alta-disponibilidad` · Alta disponibilidad y réplicas

- **Programa 2024:** Alta disponibilidad. Réplicas de bases de datos.
- **Fuentes de cátedra:** `5db2ce42f603` p.49–58
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.34; `9a9e789db872` secc.s001
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza alta · acción **corregir**
- **Observaciones:** Cátedra: AG básico (BASIC), modos síncrono/asíncrono, réplicas (snapshot/transaccional/merge), log shipping, «¿cuál es la mejor herramienta?» (p.49-58). El portal agrega FCI/WSFC, tabla comparativa y escenarios; FCI no tiene desarrollo en cátedra (solo WSFC de pasada, p.51). Discrepancias: (1) cátedra p.50 afirma que si se excede el timeout el primario pasa a modo asíncrono para esa réplica y retoma el síncrono al restablecerse; el portal (apunte-completo §11) niega esa afirmación («no debe suponerse que ... se transforma mágicamente en modo async»). Según la documentación de SQL Server, el primario efectivamente deja de esperar a una secundaria que no responde dentro del session timeout, por lo que la redacción del portal contradice a la cátedra sin necesidad: verificar contra la documentación y alinear. (2) El DDL usa la opción BASIC (Basic AG = edición Standard, 1 base, 2 réplicas, sin lectura secundaria); la página dice que el AG «protege un conjunto de bases» y compara «Lectura secundaria: posible» sin aclarar que el ejemplo de cátedra es Basic AG (limitado). Ningún final u5 evaluó HA, pero el programa 2024 la incluye (semana 12).

### `u5-backups` · Backups: clasificación, metodología y buenas prácticas

- **Programa 2024:** Backups: Clasificación, metodología y buenas prácticas.
- **Fuentes de cátedra:** `5db2ce42f603` p.35–45
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.33; `9a9e789db872` secc.s001
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Clasificación (full, diferencial acumulativo, log incremental, tail-log, copy-only), estrategia 3-2-1, compresión/cifrado, RTO/RPO (cátedra p.35-45). El portal es fiel y más preciso (diferencial acumulativo; copy-only). Observación de terminología: cátedra p.37 titula «Diferencial o incremental», mientras la guía de parcial u5 lista como error llamar «incremental» al diferencial: conviene aclarar que la cátedra usa ambos términos. Cátedra p.44 dice que una de las 3 copias debe ser la nube; el portal generaliza a «externa, aislada o inmutable» (más correcto, pero difiere).

### `u5-recuperacion` · Recuperación

- **Programa 2024:** Recuperación.
- **Fuentes de cátedra:** `5db2ce42f603` p.24–48
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.32–33; `9a9e789db872` secc.s001
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad alta · confianza alta · acción **conservar**
- **Observaciones:** Log de transacciones, VLF, LSN/MinLSN, truncado, modelos SIMPLE/FULL/BULK_LOGGED (cátedra p.24-35) y restauración con RECOVERY/NORECOVERY/STOPATMARK/MOVE/REPLACE (p.46-48). El portal corrige errores de la cátedra: la consulta de VLF de p.30 usa el alias inexistente Total_VLF_count en ORDER BY y p.34 escribe DBCC SQLPREF (typo de SQLPERF). Final 8d75a3b284ab ítem 8 pide ordenar 7 pasos de recuperación (uno incorrecto): lo cubre la guía de parcial (¿Cómo restaurar a las 10:37?), aunque conviene un listado de 7 pasos con distractor explícito. BULK_LOGGED y tail-log con NO_TRUNCATE (base dañada) no están desarrollados en cátedra más allá de p.28/p.42; el portal los amplía (afirmaciones correctas según mi conocimiento, requieren documentación Microsoft).

### `u5-cifrado` · Encriptación en tránsito y en almacenamiento

- **Programa 2024:** Encriptación en tránsito y en almacenamiento.
- **Fuentes de cátedra:** `5db2ce42f603` p.59–61
- **Referencias de alumnos (no verificadas):** `3a0d8f223fcf` p.34–35; `9a9e789db872` secc.s001
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza media · acción **corregir**
- **Observaciones:** Cátedra: concepto, TDE (at rest), EncryptByPassPhrase con PK como autenticador, TLS con certificados. El portal añade jerarquía de claves, backup de certificado, backup cifrado, tabla de amenazas, Always Encrypted (solo mención) y HSM/Key Vault: sin respaldo de cátedra (conocimiento general correcto, requiere documentación Microsoft). Ver code_issues en la página. Ningún final evaluó cifrado.

### `u6-ley-25326` · Ley 25.326 de protección de datos personales

- **Programa 2024:** Ley nacional de protección de datos personales.
- **Fuentes de cátedra:** **sin fuente de cátedra**
- **Referencias de alumnos (no verificadas):** `7034e8ba7365` secc.s001; `e40f44016a23` secc.s001; `3a0d8f223fcf` p.35
- **Exámenes que lo evalúan:** 2
- **Estado:** cobertura completo · calidad media · confianza baja · acción **investigar**
- **Observaciones:** Respaldo del corpus (solo alumnos): definición de dato personal/sensible; arts. 4, 5, 6, 7, 9, 31 (multa de 1000 a 100 mil pesos), 32 (117 bis y 157 bis), registro nacional de bases (7034e8ba7365; 3a0d8f223fcf p.35). Finales: 8d75a3b284ab ítem 3 (clasificar dato personal/sensible/ninguno); cf1a40d118d4 ítem 7 («V/F de la ley de calidad», ambiguo: puede ser Ley 25.326 art. 4 o ISO 25012). NO respaldado por el corpus (requiere fuente primaria): arts. 1-3, 8, 10, 11, 12 (cesión y transferencia internacional), 13-20 (derechos y plazos de 10 días corridos y 5 días hábiles, gratuidad semestral), 21-30, 33-43 (hábeas data), la sanción de la ley el 4/10/2000, la AAIP como autoridad, la Resolución AAIP 47/2018 y los enlaces. Mi conocimiento coincide con lo que el portal afirma, pero debe marcarse «verificar contra el texto oficial». Observaciones: los apuntes de alumno dicen que dato sensible incluye «sexo»: no figura entre las categorías del art. 7 (el portal lo hace bien); y que una empresa no inscripta recibe «pena mayor»: no lo respalda el art. 32 tal como lo conozco (el portal no lo repite, bien).

### `u6-gdpr` · General Data Protection Regulation (GDPR)

- **Programa 2024:** General Data Protection Regulation (GDPR).
- **Fuentes de cátedra:** **sin fuente de cátedra**
- **Referencias de alumnos (no verificadas):** `7034e8ba7365` secc.s001; `e40f44016a23` secc.s001; `3a0d8f223fcf` p.35
- **Exámenes que lo evalúan:** 0
- **Estado:** cobertura completo · calidad media · confianza baja · acción **investigar**
- **Observaciones:** Corpus (alumnos): objetivo, exclusiones (fallecido, persona jurídica, fines personales), datos personales y categorías especiales, transferencia fuera de la UE con 3 condiciones, multa hasta 20 millones de euros (7034e8ba7365). Ningún final lo evaluó explícitamente. NO respaldado por el corpus: test del art. 3, principios del art. 5, las 6 bases del art. 6, DPO, DPIA, art. 25/32, plazo de notificación de 72 h, derechos del cap. III y plazo de un mes + 2, arts. 46/49, escalón 10 millones o 2 %, 20 millones o 4 % (cifras correctas según mi conocimiento del Reglamento 2016/679, art. 83.4 y 83.5; verificar contra el texto oficial). Los apuntes de alumno dicen que el GDPR se aplica a «cualquier empresa, sin importar ubicación o ciudadanía, que procese información dentro del EEE»; el portal lo corrige con el test del art. 3 (más preciso): una respuesta de examen basada en la fórmula de la cátedra/alumnos podría diferir de la guía-parcial. El portal omite las exclusiones que sí traen las fuentes (fallecidos, personas jurídicas, uso doméstico/personal).

### `u6-iso-25012` · Modelo de calidad de datos ISO/IEC 25012

- **Programa 2024:** Modelo de Calidad de datos (ISO/IEC 25012).
- **Fuentes de cátedra:** **sin fuente de cátedra**
- **Referencias de alumnos (no verificadas):** `7034e8ba7365` secc.s001; `e40f44016a23` secc.s001; `3a0d8f223fcf` p.35
- **Exámenes que lo evalúan:** 1
- **Estado:** cobertura completo · calidad alta · confianza media · acción **conservar**
- **Observaciones:** Las 15 características y su clasificación 5 inherentes (exactitud, completitud, consistencia, credibilidad, actualidad) + 7 inherentes y dependientes del sistema (accesibilidad, conformidad, confidencialidad, eficiencia, precisión, trazabilidad, comprensibilidad) + 3 dependientes (disponibilidad, portabilidad, recuperabilidad) COINCIDEN en 7034e8ba7365, e40f44016a23 y en el diagrama de 3a0d8f223fcf p.35 (cuyo texto OCR sale desordenado). Coinciden con lo que conozco de ISO/IEC 25012:2008: requiere fuente primaria para confirmar formalmente. Las definiciones de alumno son flojas/erróneas en varias (accesibilidad = «cualquier persona», conformidad = «usuario conforme», precisión = «qué tan entendibles»): el portal las corrige (accesibilidad para usuarios autorizados en un contexto, conformidad = cumplimiento de estándares, precisión = nivel de detalle). Las definiciones refinadas del portal (exactitud sintáctica/semántica, accesibilidad con tecnología de apoyo, etc.) no están en el corpus: verificar contra la norma. Que unicidad no sea una de las 15 es correcto.

## 9. Detalle por página

### portada — **corregir**

`src/content/docs/bbdd-aplicadas/index.md` · temas: —

**Conservar**

- Estructura por unidad, mapa de cursada, bibliografía obligatoria coincide con programa 2024 (Elmasri-Navathe 5ta 2007 Pearson; Silberschatz-Korth-Sudarshan 4ta 2002 McGraw-Hill; 3d9721081e14 p.6).

**Faltante o superficial**

- Esquema de evaluación vigente: UN parcial (u1-u4, semana 9) + TP integrador en entregas acumulativas con coloquio + recuperatorio + final con todas las unidades (3d9721081e14 p.5-6; 6538cbd089bd p.12-15). La portada no lo menciona y las portadas de u5/u6 dicen «2do parcial».
- Bibliografía complementaria del programa: Gils Carbó, A. M., «Régimen legal de las bases de datos y hábeas data», La Ley, 1ra ed., 2001 (3d9721081e14 p.6). Es la única referencia legal de cátedra y respalda la u6.
- Distinguir recursos obligatorios (los dos módulos de Microsoft Learn) de complementarios (MongoDB University) como hace el programa; hoy se listan juntos bajo «Recursos online».
- Lecturas recomendadas de u5 en cátedra p.62 (SQL Server security best practices; SQL injection en Microsoft Learn): no figuran.
- Descripción de u5 incompleta frente al programa: faltan autenticación y directivas de contraseña, recuperación y cifrado en tránsito/en almacenamiento; la de u6 omite la Ley nacional de protección de datos personales (Ley 25.326), que es el primer contenido del programa.
- Aviso de sitio personal y no oficial no se ve en esta página (AGENTS.md exige mantenerlo visible; verificar si lo aporta la home o la configuración del sitio).

**Unidad incorrecta**

- Descripción de u6 incluye «gobierno de datos»: no figura en el programa 2024 (ver extra_topics).
- Títulos de u2 y u4 usan el esquema 2023: «BD Transaccionales: aspectos básicos/avanzados» y «BD No Transaccionales (NoSQL)». El programa 2024 titula u2 y u3 «Bases de datos relacionales: aspectos básicos/avanzados» y u4 «Bases de datos no relacionales». Mezcla de esquemas.

**Sin fuente suficiente**

- Descripción de u2: solo «Arquitectura de SQL Server, instalación, ODBC/JDBC, collation»; el programa 2024 también incluye formatos de intercambio, qué es una API e importación de datos (fuera de mi grupo, pero visible en la portada).
- Descripción de u4 menciona KDD: el programa 2024 (3d9721081e14 p.3) también lo lista en u4 (contradice el brief); verificar con quien mantiene el programa de referencia.

**Afirmaciones dudosas**

- Enlaces a unidad-N/ dependen de redirects de astro.config.mjs (no existe unidad-N/index.md): funcionan, pero el enlace de retorno de las subpáginas apunta a la raíz de la materia.

**Estilo (guía de contenido)**

- La nota «Este sitio usa una estructura de documentación navegable...» describe la plataforma (Starlight), no la materia: no aporta al estudiante.
- El mapa Mermaid etiqueta u2 como «Aspectos transaccionales básicos» (terminología 2023).

### unidad-1/practica — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-1/practica/index.md` · temas: u1-ddl-dml-esquemas

**Conservar**

- Índice con los tres laboratorios

**Faltante o superficial**

- No enlaza a la guía de cátedra ni indica que TP1 y WF son enunciados de cátedra mientras PIVOT es propio

### unidad-1/practica/pivot — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/practica/pivot.md` · temas: u1-pivot

**Conservar**

- Ejercicios 1-4, 6 y 7 correctos; resultado del ej. 1 verificado (Ana enero 1800 = 1500+300, Carlos NULL en enero/febrero/junio, Luis NULL en abril)
- Integrador 1: los resultados de la tabla coinciden con el setup (verifiqué las 25 filas: p.ej. Seattle/Online = 2*380 = 760, Austin/Marcelo = 2*45 = 90)
- UNPIVOT descarta RRHH Q3 (NULL): correcto

**Faltante o superficial**

- Soluciones de los exámenes originales del corpus (047fcb3ca752 y otros) no se reproducen; el enunciado del integrador está tomado del parcial 047fcb3ca752 con otros datos y ciudades (Seattle, Phoenix en lugar de Portland, Atlanta): documentar que es una adaptación

**Solapamientos**

- unidad-1/teoria/pivot: mismo escenario ventas/trimestre

**Ejercicios y soluciones**

- Ej. 5 (PIVOT dinámico) no ejecuta: (a) el GO entre la construcción de @cols y el SET @query hace perder las variables; (b) 'SELECT @cols = STRING_AGG(...) FROM (...) ORDER BY orden' es inválido porque orden no está en el agregado ni en GROUP BY: el orden cronológico se logra con STRING_AGG(...) WITHIN GROUP (ORDER BY orden)
- Ej. 4: AVG sobre DECIMAL(4,1) devuelve escala 6 (7.000000) y no 7.0 como en la tabla del resultado (cosmético)
- Ej. 3 y 7: sin tabla de resultado esperado

**Código a reconstruir o verificar**

- Ej. 5: DISTINCT mes, CASE... END AS orden dentro de subconsulta + STRING_AGG sin WITHIN GROUP
- Ej. 5: @query concatenado sin N (funciona porque el literal es ASCII)

**Sin fuente suficiente**

- Datos de ventas/notas son propios: sin problema, pero no hay referencia explícita a la guía de cátedra (no existe guía de PIVOT en el corpus salvo TP1 ej. 18)

**Afirmaciones dudosas**

- 'no se puede calcular dentro de la función de agregación de PIVOT': correcto (acepta solo una columna)

**Estilo (guía de contenido)**

- Columnas mezclan snake_case (venta_id) y alias en español con acentos sin delimitar (Matemáticas, Inglés, Física)

### unidad-1/practica/tp1 — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/practica/tp1.md` · temas: u1-ddl-dml-esquemas, u1-integridad, u1-programabilidad, u1-cte, u1-window, u1-pivot

**Conservar**

- Los 20 ejercicios siguen el orden y el contenido de 95d8b07bd5dd p.2-4 (ej. 1-5, 9-11, 13-20 prácticamente fieles)
- insertarLog con COALESCE(NULLIF(TRIM(...))) maneja 'en blanco' y NULL
- Ej. 9 elimina duplicados con CTE + ROW_NUMBER (DELETE sobre la CTE): válido
- Persona/curso/materia: PK, FK, patente con CHECK y comisión de 4 dígitos

**Faltante o superficial**

- Soluciones de los ejercicios 6, 10, 11, 12 (a-d), 13, 14, 15, 16, 17, 18, 19 y 20: todos los bloques sql están vacíos (la mayor parte del TP carece de solución)
- Ejercicio 6 'pruebas de restricciones' vacío
- Los incisos e) del ej. 5 y los ej. 7, 11 y 12 de la guía tienen líneas anonimizadas en el corpus (no verificable si 'DNI, teléfono, localidad, fecha de nacimiento, nombre y apellido' y 'vista SCHEMABINDING con comisión/código/nombre/apellido y nombre' son fieles)
- Pauta general y aclaración de que el TP es no obligatorio, 1 semana, y la instrucción final 'Genere un backup' no están (la pauta sí; el backup no)
- Parámetro de ejercicio 1: 'valores por defecto de crecimiento, ubicación de archivos' sin demostrarlo

**Unidad incorrecta**

- Ej. 18-20 (PIVOT, window functions) y ej. 12 (SCHEMABINDING) integran temas de u1: correcto

**Solapamientos**

- unidad-1/practica/pivot: ej. 18 de TP1 vs práctica PIVOT
- unidad-1/practica/window-functions: ej. 19-20 vs práctica WF

**Ejercicios y soluciones**

- Ej. 2: 'USE unlam; CREATE SCHEMA ddbba;' en un mismo lote falla (CREATE SCHEMA debe ser la única sentencia del lote); agregar GO
- Ej. 1: crea 'unlam' sin COLLATE ni opciones; la guía pide valores por defecto, correcto, pero TP2 ej. 1 depende de la collation de esta BD
- Ej. 5: la relación persona-materia-curso no impide que una persona esté en un curso de una materia donde su rol en persona_materia no existe (curso_persona no referencia a persona_materia): el modelo no garantiza 'un rol por materia' a nivel curso; 'persona_materia' y 'curso_persona' son dos tablas con rol solo en una
- Ej. 7: DNI aleatorio 10000000 + ABS(CHECKSUM(NEWID())) % 30000000 con UNIQUE: 1000 filas colisionan con probabilidad ~1,7 % y el SP fallaría con error de clave única (no cumple 'genere 1000 registros' de forma determinista)
- Ej. 7: no usa insertarLog (el ejercicio 4 exige registrar cada inserción en la bitácora); lo mismo ej. 9 solo lo llama una vez
- Ej. 9: elimina por nombre+apellido (cualquier coincidencia aleatoria de 2 nombres + 1 apellido) y reduce los 1000 alumnos; 'duplicado' no está definido en la guía (verificar con la guía completa)
- Texto suelto 't4' en la primera línea tras el frontmatter (artefacto)

**Código a reconstruir o verificar**

- Ej. 3: fecha_hora DATETIME DEFAULT GETDATE(): válido; se podría usar DATETIME2/SYSDATETIME (estilo)
- Ej. 5: UNIQUE y CHECK sin nombre; la guía pide 'restricciones de verificación', no nombrar impide documentar el error en ej. 6
- Ej. 5: patente VARCHAR(7) con CHECK LEN IN (6,7) y NOT LIKE '%[^A-Z0-9]%': válido, pero depende de la collation (con CI_AS el rango A-Z puede aceptar minúsculas): verificar en motor
- Ej. 7: SET NOCOUNT ON, WHILE con SELECT TOP 1 ... ORDER BY NEWID() por iteración (ineficiente pero válido)

**Sin fuente suficiente**

- Ej. 7 'tome al azar 2 valores de nombre y 1 de apellido': el corpus de la guía tiene esa línea anonimizada; verificar contra el original

**Estilo (guía de contenido)**

- Todas las tablas y columnas en snake_case (persona_id, numero_comision, fecha_nacimiento) en lugar de PascalCase singular; los identificadores de cátedra (registro, insertarLog, validaCursada, ddbba) sí están preservados

### unidad-1/practica/window-functions — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/practica/window-functions.md` · temas: u1-window

**Conservar**

- 9 ejercicios fieles a 7d43d771a356 (ROW_NUMBER, RANK, NTILE, LAG/LEAD con default 0, promedio por cliente, top 3 por país, LEAD diferencia, PERCENT_RANK por país, COUNT OVER + ROW_NUMBER)
- Soluciones verificadas a mano contra los resultados esperados de la guía: ej. 2 (empates 2-2-4 en IT), ej. 4 (SalarioAnterior/SiguienteSalario con 0), ej. 7 (5259.80 -> -3408.13) coinciden
- Nombres de columnas de salida preservados (OrdenEmpleadosSalario, Ranking, GrupoSalario, SalarioAnterior, SiguienteSalario, promedio_monto_cliente, posicion_rel_monto_cliente, monto_total_pedidos, ranking_por_pais, diferencia_monto, percentil_monto, total_pedidos_cliente, posicion_rel_pedidos_cliente)

**Faltante o superficial**

- Los 'Resultado esperado' de la guía (tablas) no se reproducen
- La guía agrega aclaración de que los datos aleatorios hacen variar el resultado (el portal sí la incluye)
- Ejercicio 1 de la guía se resuelve con 5 empleados y el resto con 20: el portal lo indica solo parcialmente (debe ejecutarse antes de insertar los 15)

**Solapamientos**

- unidad-1/teoria/window-functions: mismas funciones con otros datos

**Ejercicios y soluciones**

- No preserva identificadores: la guía crea esquema tablasWF (tablaswf.Empleados/Clientes/Pedidos) y el portal usa wf; la teoría CTE y SQL dinámico siguen usando tablaswf
- Ej. 2: la guía inserta los datos nuevos con departamento en minúsculas (ventas, marketing, it) y nombres en minúsculas; el portal los normaliza a Ventas/Marketing/IT y reemplaza un nombre anonimizado por otro nombre de ejemplo (no verificable)
- Ej. 6: RANK en lugar de DENSE_RANK/ROW_NUMBER puede devolver más de 3 por país con empates (aceptable, igual a la guía)

**Código a reconstruir o verificar**

- Setup: SELECT con RAND(CHECKSUM(NEWID())): válido; INSERT de Clientes repetido si se re-ejecuta (no idempotente, a diferencia de la tabla)
- Ej. 6, 8, 9: sin ORDER BY final en ej. 6 y 5; no afecta la corrección
- Ej. 5: posicion_rel_monto_cliente usa ROW_NUMBER ORDER BY monto (coincide con la guía p.18, que muestra 1..5 por monto ascendente)

**Estilo (guía de contenido)**

- Esquema wf en lugar de tablasWF; columnas snake_case y PascalCase mezcladas (heredado de la cátedra)

### unidad-1/teoria — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/index.md` · temas: u1-bd-conceptos

**Conservar**

- Índice claro con enlaces a todas las guías

**Faltante o superficial**

- No indica que indice-cluster excede la unidad
- No lista 'tipos de datos' ni 'BD de sistema' como tema

**Unidad incorrecta**

- Enlaza indice-cluster como parte de u1

### unidad-1/teoria/conceptos-basicos — **ampliar**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/unidad-1.md` · temas: u1-bd-conceptos, u1-motores-licencias, u1-dba, u1-despliegue

**Conservar**

- Qué es una BD y un DBMS: fiel a f740763a4b8b p.6-7
- ¿Siempre conviene usar un DBMS?: fiel a p.12
- Tabla DBA vs programador (p.13-14)
- Factores de decisión (p.11)

**Faltante o superficial**

- Clasificación transaccionales / no transaccionales (programa 2024)
- Embebida vs on premise vs cloud desarrollado (solo una fila de tabla)
- Licenciamiento: ejemplos concretos pago vs abierto
- Naturaleza autodescriptiva, múltiples vistas, aislación programa-datos (p.5)
- Tipos de datos (están en repaso-sql, solo numéricos)

**Solapamientos**

- unidad-2/teoria/bd-transaccionales: modalidades de despliegue on-cloud/on-premise y ediciones de SQL Server

**Sin fuente suficiente**

- Cita 'encuesta de sueldos de OpenQube 2025': la diapositiva p.9-10 no nombra la encuesta (requiere fuente primaria)

**Afirmaciones dudosas**

- 'SQL es el lenguaje más usado en Argentina ... por encima de JavaScript y Python': la diapositiva p.10 muestra SQL primero con 44,17 % pero el gráfico no es verificable aquí; mantener con cita de la fuente
- 'MariaDB' en 5.º puesto: p.9 la lista en ese orden pero sin porcentajes

**Estilo (guía de contenido)**

- Slug conceptos-basicos vs archivo unidad-1.md (inconsistencia de nombre de archivo, no de URL)

### unidad-1/teoria/cte — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/cte.md` · temas: u1-cte

**Conservar**

- CTE simple, encadenada, recursiva y DELETE sobre CTE
- MAXRECURSION 100 por defecto
- Comparativa CTE/subconsulta/tabla temporal

**Faltante o superficial**

- Punto y coma previo obligatorio
- UPDATE sobre CTE
- Recursión: ejemplo con datos de Empleados (la tabla Empleados del ejemplo no tiene JefeID en la práctica de WF)

**Código a reconstruir o verificar**

- Todos los ejemplos usan tablaswf.*, esquema que la práctica del portal renombró a wf: no ejecutan con el setup publicado
- CTE recursiva usa Empleados sin esquema y con JefeID inexistente en PracticaWF (no verificable)

**Afirmaciones dudosas**

- 'SQL Server la re-ejecuta cada vez': cierto en general pero depende del plan; presentarlo como comportamiento típico

**Estilo (guía de contenido)**

- Mezcla de tablas PascalCase (Empleados) y snake_case (id_cliente) heredada de la cátedra

### unidad-1/teoria/indice-cluster — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/indice-cluster.md` · temas: u1-indices-en-u1

**Conservar**

- Explicación clara de B+Tree, page splits, IDENTITY vs NEWID(), WAL y recuperación REDO/UNDO
- Tabla IDENTITY vs NEWID()

**Faltante o superficial**

- Referencia cruzada a /unidad-3/teoria/indices-y-planes/ e indices-optimizacion (ya tienen clustered, fill factor y page splits)

**Unidad incorrecta**

- El programa 2024 ubica índices clúster/no clúster, estadísticas y rowstore/columnstore en u3 (u3-indices); en u1 solo se menciona que la PK define el clúster por defecto. El transaction log, buffer pool, checkpoint y recuperación son u3 (concurrencia/TCL) o u5 (recuperación)

**Solapamientos**

- unidad-3/teoria/indices-y-planes: Clustered vs nonclustered, fill factor y page splits
- unidad-3/teoria/indices-optimizacion: Índice clustered, page splits
- unidad-2/teoria/bd-transaccionales: WAL, checkpoint, REDO/UNDO

**Código a reconstruir o verificar**

- Usa esquema bbdda con nombres snake_case (id_producto), contra la convención PascalCase

**Sin fuente suficiente**

- No hay respaldo en el corpus de cátedra de u1; el material de page split está en la cátedra de u3 (0d2ad822befa) y en apuntes (1a42e094e00e, 6939322b728b, 3a0d8f223fcf)
- Autoría/fuente desconocida: texto muy narrativo, parece generado/propio

**Afirmaciones dudosas**

- 'backups incrementales/diferenciales' en la lista del log: SQL Server no tiene backups 'incrementales' (sí diferenciales y de log)
- 'La tabla es el índice clustered': correcto solo si la PK es clustered; ya lo aclara
- Una transacción que lee con IDENTITY: 'se reinicia el servidor' causa saltos (cache de 1000 en 2012+, no es parámetro universal)

**Estilo (guía de contenido)**

- Bloques de texto como 'text' fences en lugar de listas; muy largo (19 secciones)

### unidad-1/teoria/pivot — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/pivot.md` · temas: u1-pivot

**Conservar**

- Estructura de PIVOT (agregación, FOR, IN)
- Advertencia de que PIVOT agrupa por todas las columnas no usadas (muy útil para el examen)
- UNPIVOT descarta NULL y alternativa con CROSS APPLY
- PIVOT dinámico en un solo lote (correcto)

**Faltante o superficial**

- Limitaciones: un único agregado, IN no admite subconsulta, nombres de columna con QUOTENAME en el dinámico
- Alternativa de pivot manual con CASE + GROUP BY
- UNPIVOT requiere columnas del mismo tipo

**Solapamientos**

- unidad-1/teoria/sql-dinamico: PIVOT dinámico repetido con otra tabla

**Código a reconstruir o verificar**

- Las dos tablas Markdown iniciales ('\| Departamento \| Trimestre \| Monto' sin fila separadora correcta) están mal formadas y no se renderizan como tabla
- Bloque ```` mal cerrado (cuatro acentos graves) tras 'Año \| Vendedor'
- PIVOT dinámico: @cols se arma sin QUOTENAME ('[' + Trimestre + ']') y @query sin prefijo N; funciona pero es inconsistente con sql-dinamico

**Afirmaciones dudosas**

- Tabla de errores: 'Columnas duplicadas en el resultado' no es un error real de PIVOT (lo que ocurre son filas repetidas por columnas extra en el origen)

**Estilo (guía de contenido)**

- Emoji en 'Regla práctica'

### unidad-1/teoria/repaso-sql — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/repaso-sql.md` · temas: u1-tipos-datos, u1-ddl-dml-esquemas, u1-integridad, u1-subconsultas, u1-vistas-agregados, u1-programabilidad, u1-null

**Conservar**

- Constraints implícitas/explícitas/semánticas (p.5-6)
- Catálogo-esquema-objeto en SQL Server
- Tabla numérica de tipos con rangos correctos
- PK clustered por defecto, un solo clustered por tabla, hasta 999 nonclustered
- ISNULL vs COALESCE con el ejemplo del truncamiento a CHAR(3)
- Triggers AFTER/INSTEAD OF/DDL/logon

**Faltante o superficial**

- Tipos de fecha/hora, cadenas, uniqueidentifier
- Subconsulta en SELECT, correlacionada, EXISTS
- CROSS/SELF JOIN y anti-joins
- Acciones referenciales SET NULL/SET DEFAULT/NO ACTION
- Funciones de tabla (inline y multi-statement)
- NULLIF y comportamiento de NOT IN con NULL
- Ejemplo con inserted/deleted en UPDATE

**Unidad incorrecta**

- Menciones a índices clúster/no clúster y 'Hasta 999' (u3-indices): aceptable como contexto de PK, no desarrollar más

**Solapamientos**

- unidad-1/teoria/indice-cluster: clustered vs nonclustered

**Código a reconstruir o verificar**

- Sección Procedimientos almacenados: bbdda.inscribir_alumno inserta en bbdda.inscripcion (dni, id_curso, fecha) pero la tabla se definió con (id_alumno, id_materia, fecha_inscripcion): incoherente
- FK compuesta bbdda.examen -> bbdda.curso(id_curso, dni): curso nunca se define y la clave referenciada debe ser PK/UNIQUE; ejemplo no verificable
- Vista cursos_copados referencia bbdda.curso, tabla no definida en la página
- DDL trigger tg_no_drop usa PRINT + ROLLBACK: correcto pero no se muestra la tabla afectada
- Ejemplos de CHECK de patente: correcto (Mercosur AA999AA y antiguo AAA999)

**Sin fuente suficiente**

- Límite de 999 índices nonclustered por tabla (dato correcto para SQL Server 2008+; la cátedra no lo cita)

**Afirmaciones dudosas**

- 'NULL = NULL siempre es FALSE': en lógica de tres valores es UNKNOWN
- 'UNIQUE admite un solo NULL': cierto en SQL Server, no en PostgreSQL/MySQL; aclarar el motor
- DML sobre vistas 'no puede incluir ... más de una tabla base': inexacto (vistas multi-tabla pueden actualizar columnas de una sola tabla base)
- 'Procedimientos: rutinas compiladas': en SQL Server se compilan y cachean en el primer uso, no en CREATE
- Tabla Función vs Procedimiento: usa íconos de verificación; 'Puede modificar datos ❌ (generalmente)' ambiguo (una función escalar no puede modificar tablas permanentes)

**Estilo (guía de contenido)**

- Mezcla esquemas bbdda y ddbba, y nombres snake_case vs PascalCase de la guía de contenido (tablas en singular PascalCase)
- Uso de emojis en tabla

### unidad-1/teoria/sql-dinamico — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/sql-dinamico.md` · temas: u1-programabilidad

**Conservar**

- Sí tiene respaldo de cátedra: 9d5ab3349985 p.48-49 (SQL dinámico, riesgo de inyección, ejemplo con QUOTENAME y COALESCE)
- EXEC vs sp_executesql, QUOTENAME e inyección: correcto
- PRINT del SQL antes de ejecutar

**Faltante o superficial**

- Ámbito: el código dinámico no ve variables del llamador (p.48)
- Ejemplo de la cátedra p.49 (conteo de filas por tabla con UNION ALL) no está
- OUTPUT en sp_executesql
- Contexto de permisos (ownership chaining no se aplica)

**Solapamientos**

- unidad-1/teoria/pivot: PIVOT dinámico duplicado

**Código a reconstruir o verificar**

- PIVOT dinámico: hay un GO entre SELECT @cols = ... y SET @query = ...; el GO termina el lote y @cols/@query dejan de existir (Must declare the scalar variable). Quitar el GO
- Ejemplos con tablaswf.Empleados: esquema distinto del de la práctica (wf)
- El ejemplo 'EXEC(@sql)' con '''' OR ''1''=''1''' devuelve la tabla completa: correcto

**Afirmaciones dudosas**

- 'EXEC no reutiliza plan de ejecución': EXEC con cadena también cachea planes ad hoc (solo por texto idéntico); la ventaja real es la parametrización
- 'PRINT muestra hasta 4000 caracteres': para NVARCHAR es 4000, para VARCHAR 8000

**Estilo (guía de contenido)**

- Comparación Markdown correcta

### unidad-1/teoria/window-functions — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-1/teoria/window-functions.md` · temas: u1-window

**Conservar**

- Problema que resuelven vs GROUP BY
- Anatomía de OVER y frames
- RANK/DENSE_RANK/ROW_NUMBER con empates (tabla Paint correcta)
- NTILE con reparto desigual (53 en 5 = 11,11,11,10,10 correcto)
- Fórmula de PERCENT_RANK
- Valores de porcentajes y acumulados verificados: 47,6 / 33,3 / 19,0 y 1000-3500-5300-8500-10600 son correctos

**Faltante o superficial**

- Frame por defecto (RANGE UNBOUNDED PRECEDING AND CURRENT ROW con ORDER BY) y por qué LAST_VALUE necesita el frame explícito
- Ejemplos con salida para FIRST_VALUE/LAST_VALUE, PERCENT_RANK y CUME_DIST (la cátedra tiene uno por función: d275f59f2093 p.14, 20, 23, 26, 29, 32, 35-36)
- Diferencia ROWS vs RANGE
- NTILE con PARTITION BY

**Solapamientos**

- unidad-1/practica/window-functions: ranking, LAG/LEAD y PERCENT_RANK se resuelven allí con otros datos

**Código a reconstruir o verificar**

- Sección 'Frames más usados', 3.er ejemplo: SUM(monto) OVER (PARTITION BY depto ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) sin ORDER BY: SQL Server rechaza ROWS/RANGE sin ORDER BY (verificar en motor); y la frase 'equivale a no poner frame' es cierta solo sin ORDER BY
- Ejemplos usan tablas ventas/resumen_mensual sin DDL ni datos (no verificables); la tabla de salida usa meses como texto en el ORDER BY fecha

**Sin fuente suficiente**

- Los ejemplos de ventas, vendedores y departamentos son propios, no de la cátedra (están bien como ejemplos originales pero no completos: faltan DDL+datos)

**Afirmaciones dudosas**

- CUME_DIST = rank/total: con empates cuenta todas las filas con valor menor o igual al actual
- 'PERCENT_RANK no incluye la fila actual en el conteo': descripción imprecisa; es (rank-1)/(n-1)

**Estilo (guía de contenido)**

- Columna 'rank' como alias (palabra reservada en T-SQL, requiere corchetes)
- Frase 'Podés ...' (voseo) válido en la guía

### unidad-2/practica — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/index.md` · temas: u2-importacion

**Conservar**

- Índice completo

**Faltante o superficial**

- Indicar qué prácticas pertenecen a la guía de cátedra (solo TP2)

**Unidad incorrecta**

- 'Práctica — Transacciones' pertenece a u3

### unidad-2/practica/importacion-archivos — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/importacion-archivos.md` · temas: u2-importacion

**Conservar**

- Tres CSV y un JSON con archivos publicados en public/ (viajerosgalicia.csv, SalarioMensualMedio.csv, starwars.json): verifiqué que son CSV UTF-8 con CRLF sin comillas, 466 y 17256 líneas y 25 objetos JSON con ids únicos; compatibles con BULK INSERT (ROWTERMINATOR '\n' = CRLF)
- Resultados esperados con nombres de columnas

**Faltante o superficial**

- Ej. 1: el archivo reclamos.csv no está en public/ ni hay enlace directo (solo 'descargar de datos.gob.ar')
- Resultado esperado (cantidad de filas) por ejercicio para verificar
- Ejercicio de importación de XML (la teoría cubre XML y no hay práctica)

**Solapamientos**

- unidad-2/teoria/importacion-de-archivos: mismos patrones; la teoría usa 'multas'
- unidad-2/practica/tp2: TP2 ej. 5-8 importa CSV de datos abiertos

**Ejercicios y soluciones**

- Ej. 3: la columna del CSV se llama clae2 (cabecera real) y la tabla usa clae; no es error pero el 'resultado esperado' dice clae
- Ej. 1: columnas NOT NULL: si el CSV real tiene campos vacíos o entrecomillados (BULK INSERT sin FORMAT='CSV' no los maneja), falla; verificar en motor
- Ej. 4: SINGLE_CLOB con JSON UTF-8 puede deformar acentos (los personajes tienen ':' y '-' pero no acentos en el archivo, por lo que funciona en este caso)

**Código a reconstruir o verificar**

- Base TestingDB no se crea en ningún lugar (USE TestingDB): ejercicio no autocontenido
- Falta el esquema/convención de la guía (tablas en minúscula snake_case)

**Sin fuente suficiente**

- Dataset 'Reclamos de Distribuidoras resueltos en 2022' y columnas esperadas: no verificables (sin copia local)

**Estilo (guía de contenido)**

- Tablas en minúscula (reclamos, viajeros, starwars) y columnas mixtas

### unidad-2/practica/practica-apis — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/practica-apis.md` · temas: u2-apis

**Conservar**

- Ejercicio 6 (verificar código HTTP) y 7 (persistir en tabla) agregan valor
- Verificación de sys.configurations para Ole Automation

**Faltante o superficial**

- sp_OADestroy y manejo de errores
- Respuestas esperadas a las preguntas del ej. 7

**Solapamientos**

- unidad-2/teoria/apis-desde-sql: ejemplos 1-4 de la teoría se repiten como ej. 2-5 con otras URL

**Ejercicios y soluciones**

- Ej. 3: URL con espacios y '\|' sin codificar: puede fallar con MSXML2.XMLHTTP (verificar en motor)
- Ej. 7: preguntas sin respuesta; ej. 5 repite el POST de la teoría
- Dependencias externas (worldtimeapi, mymemory, jsonplaceholder) no verificables sin red

**Código a reconstruir o verificar**

- Ej. 2: URL sin 'www' distinta de la teoría
- Ej. 4: SELECT TOP 10 con OPENJSON (cuerpo NVARCHAR(MAX)): válido
- Todos usan USE PracticaU2, base que se crea en practica-transacciones.md: dependencia entre prácticas no indicada

**Sin fuente suficiente**

- Sin respaldo en el corpus de cátedra

### unidad-2/practica/practica-bd-en-memoria — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/practica-bd-en-memoria.md` · temas: u2-almacenamiento

**Conservar**

- Estructura del setup, ejercicios 1-3 y 5
- Comparación disco vs memoria con medición de tiempos

**Faltante o superficial**

- Soluciones a las preguntas del ej. 6
- Nota de versión y de que el filegroup no se puede quitar sin descartar la BD

**Solapamientos**

- unidad-2/teoria/bd-en-memoria: mismas restricciones (aceptable)

**Ejercicios y soluciones**

- Ej. 6: afirma que ALTER TABLE no está soportado en tablas en memoria; desde SQL Server 2016 está soportado (ADD/ALTER/DROP COLUMN, offline); pregunta 'por qué no está soportado' parte de una premisa incorrecta
- Ej. 4: tiempos dependen del bucle; la nota ya lo advierte

**Código a reconstruir o verificar**

- Setup: SELECT 1 FROM sys.filegroups WHERE type = 'FX' AND database_id = DB_ID(): sys.filegroups no tiene la columna database_id (error 'Invalid column name'); eliminar la condición
- Ej. 2: columna llamada 'timestamp' (tipo de datos reservado): evitar o delimitar
- DEFAULT GETDATE() en tabla en memoria con DATETIME2: verificar en motor (tipo y función compatibles en el DEFAULT)
- Ej. 4: crea mem.SesionDisco sin esquema 'mem' garantizado (se crea en setup): ok

**Sin fuente suficiente**

- Todas las funcionalidades In-Memory carecen de fuente en corpus

**Afirmaciones dudosas**

- Ej. 6: 'FK hacia tabla en disco no soportado' es correcto; FK entre tablas en memoria sí se admite desde 2016

**Estilo (guía de contenido)**

- Esquema mem y tablas snake_case

### unidad-2/practica/practica-json — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/practica-json.md` · temas: u2-formatos, u2-importacion

**Conservar**

- Ejercicios 1-3, 5-7: sintaxis válida; JSON_MODIFY anidado y borrado con NULL correctos
- Datos propios y completos (DDL + datos)

**Faltante o superficial**

- Resultados esperados
- Respuesta a la pregunta del ej. 8
- Ejercicio con OPENROWSET de archivo (la teoría lo cubre)

**Solapamientos**

- unidad-2/teoria/json-en-sql: los mismos conceptos en forma de ejercicios (aceptable)

**Ejercicios y soluciones**

- Ej. 4: la primera consulta con 'subtotal AS JSON' dentro de WITH es inválida (AS JSON exige un tipo NVARCHAR(MAX) y una ruta); el propio comentario admite que no está soportado, pero deja un script con error
- Ej. 8: 'FOR JSON AUTO' sobre un CROSS APPLY OPENJSON ... AS linea: el comportamiento de jerarquía con una función de tabla no está garantizado (verificar en motor)
- El setup dice 'no requieren archivos externos' pero depende de PracticaU2 (se crea en practica-transacciones.md)

**Código a reconstruir o verificar**

- Ej. 1: inserta una fila inválida en una columna sin CHECK(ISJSON): demuestra ISJSON pero la columna debería llevar CHECK(ISJSON(atributos)=1)
- Ej. 7: alias [detalles.marca] con FOR JSON PATH: válido

**Sin fuente suficiente**

- Sin guía de cátedra de JSON T-SQL

**Estilo (guía de contenido)**

- Esquema js y columnas snake_case

### unidad-2/practica/practica-transacciones — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/practica-transacciones.md` · temas: u2-fuera-de-unidad-transacciones

**Conservar**

- Ejercicios 1, 2, 4, 5, 6 son técnicamente correctos (error 547 en CHECK, @@TRANCOUNT anidado, XACT_ABORT, patrón de SP con THROW)
- Base PracticaU2 se crea aquí y es reutilizada por otras prácticas

**Faltante o superficial**

- Ej. 1: el paso 2 (reemplazar COMMIT por ROLLBACK) no tiene código
- Respuestas a las preguntas de los ej. 2 y 5
- Ejemplo de deadlock y de SNAPSHOT (la teoría de u3 los trata)

**Unidad incorrecta**

- TCL, XACT_ABORT, SAVEPOINT y niveles de aislamiento son u3-tcl / u3-concurrencia / u3-bloqueos; el portal ya tiene /unidad-3/teoria/transacciones-y-concurrencia/ y su práctica pertenece junto con ella (el enlace de referencia de esta página apunta a u3)

**Solapamientos**

- unidad-3/teoria/transacciones-y-concurrencia: toda la teoría de la práctica
- unidad-2/teoria/bd-transaccionales: ejemplo de transferencia y aislamiento

**Ejercicios y soluciones**

- Ej. 3: la actualización de -9999 viola ck_saldo_positivo (error 547) y el UPDATE falla antes del IF; el saldo no cambia, la condición (saldo < 0) nunca se cumple y el ROLLBACK TO sp_antes_de_C no se ejecuta ni se imprime 'Mov C revertido': el resultado final coincide por casualidad pero la demostración del SAVEPOINT es incorrecta
- Ej. 7: el título 'Niveles de aislamiento' solo demuestra READ UNCOMMITTED/NOLOCK
- Ej. 5: tras el segundo bloque con XACT_ABORT ON el COMMIT nunca se ejecuta y la transacción se revierte: el comentario es correcto

**Código a reconstruir o verificar**

- Ej. 3: el datetime por defecto GETDATE() en DATETIME2 (estilo)
- Ej. 6: THROW 50001 dentro de TRY con XACT_ABORT ON: correcto

**Sin fuente suficiente**

- Sin guía de cátedra de transacciones en el corpus para u2; el material de u3 (0d2ad822befa, 17c2c97f736b) es de otra unidad

**Estilo (guía de contenido)**

- Esquema tx y columnas snake_case

### unidad-2/practica/practica-xml — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/practica-xml.md` · temas: u2-formatos, u2-importacion

**Conservar**

- Ejercicios 1-5 y 7 válidos
- Setup autocontenido

**Faltante o superficial**

- Resultados esperados
- Respuestas a las preguntas del ej. 2
- Importación de un archivo XML real con OPENROWSET (la teoría lo cubre)

**Solapamientos**

- unidad-2/teoria/xml-en-sql: mismos conceptos (aceptable)

**Ejercicios y soluciones**

- Ej. 6: el atributo Nombre="Monitor 27""" dentro de un literal T-SQL produce XML mal formado (Nombre="Monitor 27"""): el parser fallará; usar &quot;
- Ej. 7: dice 'parsear el XML del ejercicio 5' pero usa otro XML (P101/P102)

**Código a reconstruir o verificar**

- Ej. 1: nombres de columna alineados a la teoría: ok
- Ej. 3: la inversión del orden en FOR XML AUTO produce el anidamiento inverso (comprobar en motor)

**Sin fuente suficiente**

- Sin guía de cátedra de XML T-SQL

**Estilo (guía de contenido)**

- Esquema xml_prac y columnas snake_case

### unidad-2/practica/tp2 — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/practica/tp2.md` · temas: u2-collation, u2-importacion, u1-cte, u2-almacenamiento

**Conservar**

- 16 ejercicios en el orden de 242399d569be p.2-3; ejercicio 16 y su tabla de resultados: correctos (consulta 2 devuelve fila con CI_AI; 3 y 4 no)
- Aclaración de que tempdb hereda la collation de la instancia (ej. 15)
- Ej. 9 con PERCENT_RANK, ej. 13 con CTE y RANK: sintaxis válida

**Faltante o superficial**

- Ejercicios completos en la guía que el portal cambia: ej. 2 pide TRES bases adicionales (la del TP1 es la cuarta), el portal crea cuatro nuevas y su enunciado dice 'tres' pero el código crea cuatro
- Ej. 4 de la guía recomienda 'la tabla y SP registro del TP1' (el portal dice 'tabla y procedimiento registro'; correcto, aunque el SP real es insertarLog)
- Ej. 12 no usa el mismo SP en las cuatro DB como pide la guía ('puede generar el mismo SP en las cuatro DB'): solo se muestra para nombres_ci_ai
- Backup final: sí incluido

**Unidad incorrecta**

- TP2 de cátedra incluye CTE, vistas y percentiles (repaso de u1) dentro de u2: está así en la guía

**Solapamientos**

- unidad-2/practica/importacion-archivos: BULK INSERT de CSV
- unidad-2/teoria/importacion-de-archivos: BULK INSERT y CODEPAGE

**Ejercicios y soluciones**

- Ej. 2: contradice la guía (tres bases adicionales + la del TP1) y el DDL crea cuatro BD nuevas; el enunciado interno dice 'tres' y el bloque crea cuatro
- Ej. 5-6: estructura 'nombre, cantidad, anio' y archivos 'nombres_2010.csv' son suposiciones del portal; el dataset real de datos.gob.ar tiene columnas propias (verificar contra el recurso)
- Ej. 7: BULK INSERT con CODEPAGE 65001 hacia columnas VARCHAR no produce el problema de acentos que el ej. 8 supone; el portal afirma 'UTF-8' y luego busca 'Ã³': inconsistente (la guía anticipa mal importación)
- Ej. 8: REPLACE(nombre, 'Ã³', 'ó') en una BD con collation AI/CI trata 'Ã' como equivalente a 'A'/'a': el UPDATE puede reemplazar coincidencias falsas (p.ej. 'ao'); la propia guía advierte sobre el comportamiento por BD pero el ejemplo no lo evita (usar COLLATE binario)
- Ej. 10: INTERSECT entre vistas de BD con collations distintas lanza 'Cannot resolve the collation conflict ... INTERSECT'; el ejemplo como está no ejecuta (necesita COLLATE explícito); contradice lo que luego pregunta el ej. 11
- Ej. 14: CREATE VIEW sobre ##percentiles_global es inválido: una vista no puede referenciar tablas temporales (error 4508)
- Ej. 12: depende del ej. 9 pero '##percentiles_global' queda poblada con datos duplicados si el SP se ejecuta dos veces (no hay TRUNCATE)
- Ej. 3: 'USE nombres_ci_ai; GO  CREATE SCHEMA ddbba; GO' en una línea: GO debe estar solo en su línea, el script como está no ejecuta en SSMS/sqlcmd

**Código a reconstruir o verificar**

- Ver exercise_issues 8, 10, 14
- Ej. 9: pct_rank con empates (muchos nombres con la misma cantidad) puede dejar ambos percentiles vacíos si hay pocos nombres distintos
- Ej. 16: correcto
- Ej. 13: RANK() OVER (ORDER BY SUM(cantidad) DESC) en consulta agrupada: válido; con empates puede devolver más de 100 filas

**Sin fuente suficiente**

- Ruta C:\\datos\\nombres\\ y nombres de archivos de ejemplo

**Afirmaciones dudosas**

- 'CODEPAGE 65001 soportado': cierto desde SQL Server 2016 en BULK INSERT (verificar en motor 2019/2022); convierte a la página de códigos de la columna VARCHAR, con posible pérdida de caracteres fuera de la collation

**Estilo (guía de contenido)**

- Tabla nombres con (nombre, cantidad, anio) en minúscula (guía de contenido: PascalCase)
- Vistas v_percentiles / v_top100 en snake_case

### unidad-2/teoria — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/index.md` · temas: u2-formatos

**Conservar**

- Resumen de contenidos fiel al programa

**Faltante o superficial**

- Indicar que 'transaccionales' mezcla contenido de u3/u4
- 'Instalación', 'BD de sistema' y 'arquitectura' sin página

**Unidad incorrecta**

- El título 'BD Transaccionales: aspectos básicos' y la inclusión de aislamiento/DWH mezclan u2, u3 y u4

**Solapamientos**

- unidad-2/teoria/formatos-conectividad: dos enlaces a formatos: formatos-conectividad y formatos-de-intercambio

### unidad-2/teoria/apis-desde-sql — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql.md` · temas: u2-apis

**Conservar**

- Advertencia de que no se recomienda en producción
- Patrón sp_OACreate / OPEN / SEND / RESPONSETEXT
- Diferencias GET vs POST

**Faltante o superficial**

- sp_OADestroy y manejo de errores (sp_OAGetErrorInfo) en todos los ejemplos
- Seguridad: Ole Automation amplía la superficie de ataque
- Alternativas modernas: sp_invoke_external_rest_endpoint (Azure SQL / SQL Server 2025), CLR, aplicaciones externas
- Codificación de URL (espacios, \| y ?)

**Solapamientos**

- unidad-2/practica/practica-apis: los mismos cuatro ejemplos con pequeñas variaciones

**Código a reconstruir o verificar**

- Ejemplo 2: columnas FechaHora (DATETIME2 '$.datetime') y FechaHoraISO ambas desde $.datetime: redundante; convertir un ISO 8601 con offset a DATETIME2 es posible pero descarta el offset (verificar en motor)
- Ejemplo 3: URL no codificada (espacios y '\|'): puede fallar con MSXML2.XMLHTTP (verificar en motor)
- Ejemplo 1 y 2: www.worldtimeapi.org vs la práctica worldtimeapi.org: dominio distinto; el servicio puede no estar disponible
- Patrón base usa @url sin declarar (esquema conceptual)
- sp_OAMethod RESPONSETEXT con @respuesta OUTPUT y luego INSERT ... EXEC sp_OAGetProperty: se lee dos veces la respuesta (redundante)

**Sin fuente suficiente**

- Sin respaldo de cátedra en el corpus (008193c9c082 p.23-26 solo muestra API y Postman)

**Afirmaciones dudosas**

- 'Esta configuración persiste hasta que se deshabilite': cierto con RECONFIGURE; pero 'show advanced options' queda habilitado también

### unidad-2/teoria/bd-en-memoria — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria.md` · temas: u2-almacenamiento

**Conservar**

- Disco vs memoria (d0b0a9b78ca8 p.26)
- Tablas temporales locales/globales: alcance y duración
- Comparativa variable de tabla / temporal / memoria (p.28)
- FILEGROUP MEMORY_OPTIMIZED_DATA y sintaxis básica de tabla en memoria
- Modos SCHEMA_AND_DATA / SCHEMA_ONLY
- Vista de monitoreo con sys.dm_db_xtp_table_memory_stats

**Faltante o superficial**

- Nota de versión: In-Memory OLTP existe desde SQL Server 2014 y disponible en todas las ediciones desde 2016 SP1
- Relación con almacenamiento en disco (E/S, buffer pool) de forma más gráfica

**Unidad incorrecta**

- Tablas temporales y variables de tabla pertenecen más a programabilidad (u1) que a almacenamiento

**Solapamientos**

- unidad-2/teoria/bd-transaccionales: sección Bases de datos en memoria (comparativa duplicada)

**Código a reconstruir o verificar**

- Procedimiento nativo insertar_log usa NEXT VALUE FOR seq_log: la secuencia seq_log no se define en la página (verificar en motor que NEXT VALUE FOR sea válido en el módulo nativo para la versión usada)
- Tabla pedidos_cache con 'INDEX idx_cliente HASH (cliente_id) WITH (BUCKET_COUNT = 500000)': válido; el comentario '2x el máximo de filas' es una heurística, no regla
- Ejemplo 'SELECT * FROM pruebasDB.dbo.#temporal' desde otra BD de la misma sesión: comportamiento no documentado de forma clara (verificar en motor)

**Sin fuente suficiente**

- NVRAM, Hekaton, índices hash/range, compilación nativa: sin respaldo en el corpus (la cátedra remite a una guía 'Tablas en memoria' no incluida)

**Afirmaciones dudosas**

- 'Sin claves foráneas' / tabla comparativa 'Permite FK: No' y restricción 'Sin FOREIGN KEY': desde SQL Server 2016 se admiten FK entre tablas en memoria (no hacia tablas en disco)
- 'Todas las columnas deben ser NOT NULL o tener valor por defecto': desde 2016 se admiten columnas NULL
- 'Sin columnas calculadas': soportadas desde SQL Server 2017
- 'No se admite VARCHAR(MAX) como columna de índice': ambiguo; desde 2016 hay soporte LOB (fuera de fila)
- 'Range index usa árbol B+': los índices nonclustered en memoria usan Bw-tree
- 'ACID completo con snapshots + logs o NVRAM': los snapshots solos no dan durabilidad (lo dice más arriba); redacción contradictoria
- 'Sin fragmentación': no hay fragmentación de páginas, pero sí necesidad de compactar (MERGE); correcto

**Estilo (guía de contenido)**

- Emojis ✅ ❌ en tabla de ventajas
- Mezcla tablas temporales dentro de una guía de BD en memoria

### unidad-2/teoria/bd-transaccionales — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/unidad-2.md` · temas: u2-arquitectura, u2-instalacion, u2-collation, u2-almacenamiento, u2-fuera-de-unidad-transacciones, u1-despliegue

**Conservar**

- OLTP, ejemplos y ventajas/desventajas (d0b0a9b78ca8 p.2-8)
- OLTP vs OLAP
- BD vs DWH vs Data Lake (p.11-15) con ETL/ELT
- Clúster, nube vs dedicado (p.9-10)
- Instalación, ediciones, instancias, Configuration Manager, puerto 1433, conexión remota y autenticación (p.16-21)

**Faltante o superficial**

- Análisis previo a la instalación y ubicación de datos/tempdb/respaldos (p.17-18)
- BD de sistema (master, model, msdb, tempdb)
- Memoria máxima por defecto 'utiliza la totalidad' (p.20)
- Características opcionales (p.16)

**Unidad incorrecta**

- ACID desarrollado en detalle (atomicidad/consistencia/isolation/durabilidad con WAL, lost update, MVCC, NVRAM, snapshots) y los niveles de aislamiento SQL: corresponden a u3-concurrencia (aislamiento) y u4-base-acid (ACID vs BASE); en u2 la cátedra solo menciona 'propiedades ACID' y commit/rollback
- Always On Availability Groups y SNAPSHOT ISOLATION: u3/u5 (alta disponibilidad es u5)
- DWH y Data Lake: la cátedra los incluye en el mismo PDF de u2 (d0b0a9b78ca8 p.11-15), pero el programa 2024 los trata en u4 (data lakes) y en 'contenidos mínimos' (DWH): reubicar o dejar con rótulo

**Solapamientos**

- unidad-3/teoria/transacciones-y-concurrencia: niveles de aislamiento, SNAPSHOT, deadlocks y TCL (u3)
- unidad-2/teoria/collation: sección Collation duplicada en resumen
- unidad-2/teoria/bd-en-memoria: sección BD en memoria duplicada (tabla de comparación de tipos de tabla repetida)
- unidad-1/teoria/indice-cluster: WAL, checkpoint y recuperación

**Código a reconstruir o verificar**

- Cadenas de conexión: 'Server=mi_servidor,1433;...Password=contraseña' ok
- No hay código SQL ejecutable salvo la transferencia (sin DDL de cuentas)

**Sin fuente suficiente**

- NVRAM, instantáneas, 'tres técnicas de durabilidad': sin respaldo en el corpus de cátedra de u2 (sí en la versión de BD en memoria, pero tampoco en el corpus)
- 'Costo storage: Medio/Alto/Bajo' en la tabla BD/DWH/DL y 'Usuarios: Miles/Decenas' en OLTP vs OLAP: sin fuente en el corpus

**Afirmaciones dudosas**

- Lost update descrito como 'uno de los tres problemas clásicos de concurrencia': los tres clásicos de la tabla siguiente son dirty read, non-repeatable read y phantom; lost update no es uno de ellos
- 'El proceso checkpoint sincroniza periódicamente el log con los datos en disco': checkpoint escribe páginas sucias al archivo de datos, no sincroniza el log
- Tabla de aislamiento marca READ COMMITTED 'bloqueado' para dirty read: correcto; pero en Azure SQL Database el default es READ_COMMITTED_SNAPSHOT (no solo en SQL Server)
- 'SQL Server ... Standard: funcionalidades parciales' y 'Enterprise: Always On': Standard tiene Availability Groups básicos; verificar por versión
- 'SQL define cuatro niveles' pero SQL Server agrega SNAPSHOT: aceptable
- 'Escalado costoso en volúmenes muy grandes' y otras afirmaciones de la tabla Ventajas/Desventajas no están en la cátedra

**Estilo (guía de contenido)**

- Título y slug bd-transaccionales pero archivo unidad-2.md; usa encabezados H1 (#) para secciones internas (BD, Data Warehouse y Data Lake / Arquitectura / Motor / Collation / Memoria) en lugar de H2

### unidad-2/teoria/collation — **ampliar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/collation.md` · temas: u2-collation

**Conservar**

- Definición dual (representación + comparación) fiel a p.22
- Niveles instancia > BD > columna
- Cláusula COLLATE para comparaciones (p.23)
- Procedimiento de cambio de collation de instancia con sqlservr -q (documentado)

**Faltante o superficial**

- COLLATE database_default / CATALOG_DEFAULT (lo usa tp2 ej. 14)
- Collation de tempdb y tablas temporales (lo pide tp2 ej. 15)
- Conflicto de collation en UNION/INTERSECT/EXCEPT además de JOIN (tp2 ej. 10)
- Collations binarios (_BIN, _BIN2) con explicación
- Collation UTF-8 (_UTF8) en SQL Server 2019+ (CODEPAGE 65001 en BULK INSERT)

**Solapamientos**

- unidad-2/teoria/bd-transaccionales: sección Collation resumida

**Código a reconstruir o verificar**

- Consulta INFORMATION_SCHEMA.COLUMNS: correcta
- Cambio de collation de columna con índices: advertencia correcta

**Sin fuente suficiente**

- 'Columna de contraseñas (hash): Latin1_General_BIN o CS_AS' y 'Integración con Linux: CS_AS': recomendaciones propias, sin respaldo de cátedra

**Afirmaciones dudosas**

- 'AI: a = á = â = à' correcto; 'collation por defecto de muchas instalaciones SQL_Latin1_General_CP1_CI_AS' es el default en en-US, no en todas

### unidad-2/teoria/formatos-conectividad — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/formatos-conectividad.md` · temas: u2-conexion-drivers, u2-formatos, u2-apis

**Conservar**

- ODBC/JDBC con flujo de conexión y cadenas de conexión
- APIs: REST, SOAP, JSON-RPC y ejemplos GET/POST
- Postman

**Faltante o superficial**

- Qué es un driver/proveedor y OLE DB
- Autenticación en APIs (API key, OAuth) más allá de un ejemplo Bearer

**Solapamientos**

- unidad-2/teoria/formatos-de-intercambio: EDI, CSV/TSV, ancho fijo, XML, JSON y YAML repetidos casi textualmente (dos versiones distintas del ejemplo XML y JSON)
- unidad-2/teoria/json-en-sql: sintaxis JSON
- unidad-2/teoria/xml-en-sql: sintaxis XML

**Código a reconstruir o verificar**

- Dependencia Maven mssql-jdbc versión 12.4.2.jre11: verificar versión vigente
- Cadena JDBC con trustServerCertificate=true: prácticas de desarrollo, advertir riesgo en producción

**Sin fuente suficiente**

- Tipos de API (abierta/interna/de socios) y protocolos XML-RPC/JSON-RPC: no figuran en 008193c9c082 p.23-26

**Afirmaciones dudosas**

- 'XML — eXtended Markup Language': el nombre correcto es eXtensible Markup Language (la diapositiva p.14 de 008193c9c082 dice 'eXtendedMarkup'; se hereda el error)
- JDBC: 'Sun/Oracle (Java EE)': JDBC es parte de Java SE
- 'Los formatos de intercambio son siempre de texto simple': EDI, CSV, JSON, XML, YAML sí; existen formatos binarios (Parquet, Avro)

**Estilo (guía de contenido)**

- Misma advertencia de formato duplicado

### unidad-2/teoria/formatos-de-intercambio — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio.md` · temas: u2-formatos, u2-importacion

**Conservar**

- Es la página de formatos más completa y fiel a 008193c9c082 p.4-22 (EDI, CSV, ancho fijo, XML, JSON, YAML)
- Tabla comparativa final
- YAML sin soporte nativo en SQL Server: correcto

**Faltante o superficial**

- Ejemplo de ancho fijo con BULK INSERT y archivo de formato real

**Solapamientos**

- unidad-2/teoria/formatos-conectividad: todo el bloque Formatos de intercambio de datos
- unidad-2/teoria/json-en-sql: sección JSON en SQL Server (FOR JSON, OPENJSON, JSON_VALUE...)
- unidad-2/teoria/xml-en-sql: sección XML en SQL Server (FOR XML, .nodes(), OPENROWSET)
- unidad-2/teoria/importacion-de-archivos: BULK INSERT y OPENROWSET con SINGLE_BLOB

**Código a reconstruir o verificar**

- Ancho fijo: la tabla tmp_ancho_fijo (linea CHAR(32)) con ROWTERMINATOR '\n' espera CRLF; con una línea de 32 caracteres + CR se trunca/da error (verificar en motor)
- BULK INSERT ... FORMATFILE en OPENROWSET: sintaxis correcta; falta el .fmt de ejemplo

**Sin fuente suficiente**

- Ejemplo T-SQL de XML y JSON sin respaldo en el corpus

**Afirmaciones dudosas**

- 'TDS*14400~' como 144.00 en centavos: asunción sin fuente (ANSI X12 810 TDS usa 2 decimales implícitos, es correcto pero no consta en p.5-7)
- 'XML — eXtended' (ver formatos-conectividad)

**Estilo (guía de contenido)**

- Ejemplos con nombres de tablas genéricos (clientes, ventas) minúsculas

### unidad-2/teoria/importacion-de-archivos — **ampliar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos.md` · temas: u2-importacion

**Conservar**

- BULK INSERT: sintaxis, opciones y ejemplo completo
- OPENROWSET + OPENJSON y XML
- Valores de CODEPAGE explicados

**Faltante o superficial**

- FORMAT = 'CSV' y FIELDQUOTE (SQL Server 2017+) para campos entrecomillados
- ERRORFILE, BATCHSIZE, CHECK_CONSTRAINTS
- SINGLE_NCLOB / CODEPAGE='65001' para JSON UTF-8 con acentos
- Tabla de staging + validación + INSERT final (patrón de TP2)
- Permisos (ADMINISTER BULK OPERATIONS) y ruta accesible por la cuenta de servicio

**Solapamientos**

- unidad-2/practica/importacion-archivos: teoría y práctica repiten el patrón; la práctica es la aplicación (aceptable)
- unidad-2/teoria/formatos-de-intercambio: BULK INSERT y OPENROWSET en la sección CSV
- unidad-2/practica/tp2: ej. 7 (BULK INSERT de CSV) repite el ejemplo

**Código a reconstruir o verificar**

- Tabla de opciones: 'CODEPAGE valor por defecto ACP' es dudoso (la documentación no fija ACP como default; verificar)
- Ejemplo JSON: SINGLE_CLOB lee como varchar con la collation de la BD; JSON UTF-8 con acentos puede corromperse (usar SINGLE_NCLOB y archivo UTF-16, o CODEPAGE)
- 'SINGLE_BLOB (a diferencia de SINGLE_CLOB) lee como bytes sin conversión': correcto

**Sin fuente suficiente**

- Opciones LASTROW/MAXERRORS/TABLOCK sin fuente en corpus

**Afirmaciones dudosas**

- 'ROWTERMINATOR \\n por defecto \\r\\n': se acerca; en BULK INSERT '\\n' implícitamente espera CRLF y falla con archivos LF puros (relevante para CSV de Linux)

### unidad-2/teoria/json-en-sql — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/json-en-sql.md` · temas: u2-formatos, u2-importacion

**Conservar**

- OPENJSON con y sin WITH, tabla de type 0-5 correcta
- AS JSON, CROSS APPLY y ruta como segundo argumento
- Modo lax vs strict
- Compatibilidad >= 130

**Faltante o superficial**

- JSON_VALUE devuelve NVARCHAR(4000); JSON_QUERY vs JSON_VALUE con tipos; ISJSON en CHECK
- JSON_ARRAY/JSON_OBJECT (SQL Server 2022)
- Indexar JSON mediante columnas calculadas

**Solapamientos**

- unidad-2/teoria/formatos-de-intercambio: FOR JSON y OPENJSON ya presentados
- unidad-2/practica/practica-json: la práctica retoma los mismos ejemplos con otros datos (aceptable)
- unidad-2/teoria/importacion-de-archivos: OPENROWSET + OPENJSON

**Código a reconstruir o verificar**

- En el ejemplo sin esquema, 'DT null' muestra value 'null': OPENJSON devuelve SQL NULL en la columna value (type 0)
- Ejemplo de CROSS APPLY declara Torneo '$.Categoria' pero el JSON no tiene Categoria: devuelve NULL (inocuo, incoherente)
- Id INT '$.id' sobre '02' pierde el cero inicial (ver 'Ciudad de Bs As'): considerar VARCHAR

**Sin fuente suficiente**

- Sin respaldo en el corpus de cátedra (solo apunte de alumno cd36d917c66c p.10 menciona OPENJSON)

### unidad-2/teoria/xml-en-sql — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-2/teoria/xml-en-sql.md` · temas: u2-formatos, u2-importacion

**Conservar**

- Importación con OPENROWSET + nodes()/value()
- OPENXML con sp_xml_preparedocument/removedocument
- FOR XML RAW/AUTO/ELEMENTS/XSINIL/XMLSCHEMA
- TYPE en subconsultas anidadas

**Faltante o superficial**

- Tabla ddbba.gol referenciada en 'Relaciones entre tablas' no está definida
- XML con namespaces y XQuery exist()/query()
- Validación contra XSD (XML SCHEMA COLLECTION)

**Solapamientos**

- unidad-2/teoria/formatos-de-intercambio: sección XML en SQL Server (FOR XML y nodes())
- unidad-2/practica/practica-xml: retoma FOR XML con otros datos

**Código a reconstruir o verificar**

- UPDATE ddbba.cliente ... WHERE Nombre LIKE 'Pipi%': el cliente 'Pipi' no existe en los datos del XML (Ponzio, JJ Lopez); no se vería el efecto
- Consulta con ddbba.gol/Jugador: tabla y datos inexistentes (no reproducible)
- '.query('Documento').value('.', ...)': válido pero ineficiente; usar .value('(Documento)[1]', ...)

**Sin fuente suficiente**

- Datos con nombres de jugadores de fútbol ('Ponzio', 'JJ Lopez', 'Pipi', 'Sufridor'): provienen de material de cátedra no incluido en el corpus

**Afirmaciones dudosas**

- 'Si no se libera, el documento queda cacheado hasta que termina la sesión': la memoria se libera al terminar el lote/sesión pero puede ocupar hasta 1/8 de memoria de SQL Server: documentarlo mejor

**Estilo (guía de contenido)**

- Ejemplo con documentos y direcciones ficticias; el XML de ejemplo no usa PascalCase de la guía para columnas (sí lo hace)

### unidad-3/practica — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-3/practica/index.md` · temas: u3-tcl, u3-concurrencia

**Conservar**

- Indice simple de los dos laboratorios

**Faltante o superficial**

- No hay ejercicios con enunciado y solucion para indices/planes/estadisticas/optimizacion/columnstore (la guia de practica de u3 de la catedra no esta en el corpus; solo hay demos en la teoria)
- No hay laboratorio de bloqueos/deadlocks ni de transacciones distribuidas

### unidad-3/practica/laboratorio-aislamiento — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento.md` · temas: u3-concurrencia

**Conservar**

- Cobertura completa de los niveles: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE, SNAPSHOT y RCSI con dos sesiones
- Entorno autocontenido con DDL y datos
- Tabla final SNAPSHOT vs RCSI

**Faltante o superficial**

- Resultados esperados explicitos (que devuelve la sesion B en cada paso)
- Experimento de conflicto de actualizacion SNAPSHOT (error 3960): solo hay un comentario, no hay script
- Script de limpieza entre laboratorios (el LAB 2 deja saldo 1111 y el LAB 3 saldo 50; los totales y filtros 'saldo > 1000' cambian)
- Aviso de que ALTER DATABASE ... READ_COMMITTED_SNAPSHOT ON espera a que no haya otras conexiones activas (con SSMS abierta puede quedar bloqueado; usar WITH ROLLBACK IMMEDIATE)
- Restauracion a RCSI OFF al terminar

**Solapamientos**

- unidad-3/practica/laboratorio-tcl: Dirty read, REPEATABLE READ y SERIALIZABLE vuelven a verse

**Ejercicios y soluciones**

- LAB 3 (phantom): la sesion A ejecuta INSERT y a continuacion DELETE en el mismo script; el DELETE corre inmediatamente (GO separa lotes pero no espera) y el INSERT queda confirmado solo unos milisegundos, de modo que B (a los 10 s) vuelve a contar 3 y no se observa el fantasma. Debe ejecutarse solo el INSERT durante la espera y recien despues la limpieza
- LAB 3 primera parte: la sesion A 'bloqueara hasta que B haga COMMIT' y luego fija saldo = 50 definitivamente; deja datos distintos para los labs siguientes
- LAB 4 (SERIALIZABLE): el INSERT de A tambien queda confirmado y borrado inmediatamente despues; aceptable porque el INSERT se bloquea hasta el COMMIT de B, pero no se muestra el resultado
- LAB 1/2/5/6: mezclan escenarios de rollback con WAITFOR fijo (15 s); si la sesion B se lanza tarde no se ve el efecto; sin resultado esperado impreso
- LAB 6 asume que el ALTER ... RCSI ON ya esta efectivo; si ALLOW_SNAPSHOT_ISOLATION estaba ON del LAB 5, el ALTER de RCSI puede quedar esperando por la sesion de lab 5

**Código a reconstruir o verificar**

- DROP TABLE IF EXISTS ddbba.cuentas antes de crear el esquema: si el esquema no existe, DROP TABLE IF EXISTS no falla, pero el orden confunde (crear esquema primero)
- INSERT INTO ddbba.cuentas VALUES (...) sin lista de columnas; con INSERT posteriores 'VALUES (4, ''Diana'', 3000)' funciona pero es fragil
- LAB 5: una transaccion SNAPSHOT sin acceso a datos previo no 'fija' su snapshot hasta el primer acceso a datos; el comentario 'snapshot al inicio de la TX' es correcto para el primer SELECT del ejemplo

**Sin fuente suficiente**

- Escenarios y datos (Alice, Bob, Charlie) son del portal; la catedra usa un caso de tarjeta de credito (TCL_1..TCL_9)

**Afirmaciones dudosas**

- 'RCSI es la opcion con mejor relacion costo/beneficio para sistemas OLTP existentes': opinion; omite el costo de tempdb/version store y el riesgo de logica que dependia de bloqueos

**Estilo (guía de contenido)**

- Tabla cuentas en minuscula y snake_case
- Un enlace de retorno apunta a la pagina de teoria equivalente (correcto)

### unidad-3/practica/laboratorio-tcl — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl.md` · temas: u3-tcl, u3-concurrencia

**Conservar**

- Entorno completo (DDL + datos); los datos de las 4 tarjetas coinciden con las primeras filas de cc_info.csv de la u4 (misma base de la catedra)
- Experimento 0 correcto como compra atomica (con IF por limite)
- Experimento 1: ejemplo claro de dirty read y 'READ COMMITTED lo evitaria'

**Faltante o superficial**

- Resultados esperados de cada experimento (sin salida esperada en ninguno)
- Experimento con READ COMMITTED (cat. TCL_3/TCL_4, 17c2 p.13) y el estado final de las tablas
- WAITFOR en las sesiones del Experimento 2 y 3
- Script de limpieza/reinicio para repetir cada experimento

**Solapamientos**

- unidad-3/practica/laboratorio-aislamiento: Ambos laboratorios practican dirty read, REPEATABLE READ y SERIALIZABLE con distinto escenario; el nombre 'Laboratorio TCL' pero demuestra niveles de aislamiento

**Ejercicios y soluciones**

- Experimento 1: B hace un UPDATE sobre la misma fila que A mantiene con X-lock; ese UPDATE queda bloqueado hasta el ROLLBACK de A y luego ejecuta limite_credito - 20000 sobre el valor original (6000), dejando limite negativo (-14000) y la venta registrada. El enunciado omite este desenlace (el cliente 'autoriza' una compra con dato inexistente: bien) pero no lo documenta; resultado esperado ausente
- Experimento 2: la conexion A (REPEATABLE READ) no tiene WAITFOR ni pausa antes del COMMIT, por lo que ejecuta todo de corrido y no da tiempo a lanzar B y C; el comentario 'ir a la conexion B' solo es posible ejecutando sentencia por sentencia. Agregar WAITFOR DELAY
- Experimento 2: B y C 'quedan bloqueados' pero el UPDATE de A (S-lock -> X) y B esperando X puede llevar a una espera ordenada; no se explica por que no hay deadlock de conversion
- Experimento 3: titulo 'READ UNCOMMITTED con reversion (SERIALIZABLE en otra sesion)' pero la conexion A no hace reversion; la reversion (con id 10007/10006) esta en B. Los ids no coinciden con el resto (1001..1007) y la reversion hace referencia a 10006 inexistente
- Experimento 3: B no tiene WAITFOR; ejecuta y confirma sin que A pueda interferir; no demuestra el range lock descrito. Ademas nro_tarjeta no tiene indice, por lo que el range lock abarca la tabla completa
- Tabla resumen: 'Experimento 0: Explicita (default)' — el default es autocommit/READ COMMITTED; confuso
- Experimento 0: 'IF (@limite_actual > @monto)' rechaza un monto igual al limite (disponibilidad)

**Código a reconstruir o verificar**

- Identificadores propios (tarjeta_credito, transaccion, id_transaccion) difieren de la catedra (creditCard_info, Transaccion): la guia de contenido exige preservar los de catedra al reproducir ejercicios
- DROP TABLE IF EXISTS ddbba.transaccion antes de que se garantice la existencia del esquema: funciona, pero conviene crear el esquema primero
- DECLARE dentro de BEGIN TRANSACTION sin GO: correcto; las variables sobreviven solo en el lote

**Sin fuente suficiente**

- Enunciado de 'dos empleados del banco' (Exp. 2) y el escenario del limite 76000 son del portal; la catedra solo presenta los scripts TCL_0..TCL_9 sin texto en el corpus (solo se leen nombres de archivo en 17c2 p.13)

**Estilo (guía de contenido)**

- snake_case en tablas y columnas en lugar de PascalCase singular (se reproducen nombres de catedra solo parcialmente)

### unidad-3/teoria — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-3/teoria/index.md` · temas: u3-concurrencia, u3-tcl, u3-indices, u3-monitoreo

**Conservar**

- Tabla de paginas con descripcion de cada apunte
- Enlace a la practica

**Faltante o superficial**

- Mapa de temas del programa 2024 (concurrencia, TCL, bloqueos, distribuidas, monitoreo, plan, indices, estadisticas, optimizacion, rowstore/columnstore) con la pagina que cubre cada uno

**Solapamientos**

- unidad-3/teoria/transacciones-y-concurrencia: Dos entradas de indice para casi el mismo tema (Transacciones y Concurrencia vs Transacciones y concurrencia en SQL Server) con titulos casi identicos que confunden al lector

**Afirmaciones dudosas**

- Encabezado 'BD Transaccionales: aspectos avanzados · 1er parcial': el programa 2024 tiene UN parcial (u1-u4) segun el cronograma 6538 p.~16; '1er parcial' es esquema 2023 (dos parciales)
- Titulo 'BD Transaccionales' no coincide con el programa 2024 ('Bases de datos relacionales: aspectos avanzados')

**Estilo (guía de contenido)**

- Los enlaces '[← Unidad 3](/bbdd-aplicadas/unidad-3/)' de otras paginas apuntan a un slug que no corresponde a ninguna pagina (la presentacion tiene slug /bbdd-aplicadas/unidad-3/teoria): verificar enlaces rotos

### unidad-3/teoria/indices-optimizacion — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion.md` · temas: u3-indices, u3-plan-ejecucion, u3-estadisticas, u3-monitoreo, u3-rowstore-columnstore, u3-optimizacion

**Conservar**

- Indices clustered/nonclustered/INCLUDE y fill factor con explicacion correcta y alineada con la catedra 0d2a p.12-17
- Rebuild vs reorganize con umbrales 10-30/>30 (la catedra usa <30/>30)
- Distincion filas estimadas vs reales y estadisticas (componentes) correcta

**Faltante o superficial**

- Selectividad y uniquefier (cat. 0d2a p.14, 19)
- CREATE STATISTICS/estadisticas filtradas
- Sintaxis y ejemplo de columnstore
- Reescritura de consultas (ver indices-y-planes)
- Ejemplo completo con DDL, datos, plan y resultado para el caso 'crear un indice de cobertura' (tipico de examen)

**Unidad incorrecta**

- La seccion 'Metricas de rendimiento' + 'Modelo de recuperacion' (baseline, SQL Agent jobs, Simple vs Full) pertenece a u3-monitoreo y duplica metricas-de-rendimiento; ademas el modelo de recuperacion se retoma en u5 (backups) segun la catedra (17c2 p.38 'veremos mas en la unidad 5')

**Solapamientos**

- unidad-3/teoria/indices-y-planes: Indices clustered/nonclustered, INCLUDE, fill factor, rebuild/reorganize, rowstore/columnstore, TABLE SCAN/SEEK/KEY LOOKUP, estadisticas y variables de tabla vs temporales aparecen en ambas
- unidad-3/teoria/metricas-de-rendimiento: Baseline, tabla de metricas, estrategia de obtencion y tabla Simple vs Full duplicadas

**Código a reconstruir o verificar**

- ALTER INDEX ... REBUILD 'puede hacerse online (WITH (ONLINE = ON))': solo en Enterprise/Developer (y Azure SQL); en Standard falla. Omitido el requisito; la catedra dice que el rebuild 'bloquea la tabla' (p.20)
- 'Una tabla puede tener hasta 999 indices nonclustered': correcto desde SQL Server 2008, pero sin fuente en el corpus
- Consulta sys.dm_db_index_physical_stats con modo 'LIMITED' no devuelve page_count; sin filtro por page_count ni nombre de indice (join con sys.indexes) los resultados son poco interpretables
- DBCC SHOW_STATISTICS ... WITH HISTOGRAM sobre ix_apellido: sin DDL de dbo.Clientes ni datos

**Sin fuente suficiente**

- 'compresion muy alta' en columnstore sin cifras
- Software de monitoreo (SolarWinds DPA, Redgate): cita de la catedra 17c2 p.42 solo como 'software especializado (3rd party)'

**Afirmaciones dudosas**

- 'Las variables de tabla no tienen estadisticas: el optimizador asume siempre 1 fila': la catedra dice 'segun la version' (0d2a p.27). Desde SQL Server 2019 (compat 150) la compilacion diferida usa la cardinalidad real; afirmacion a matizar
- 'Cada tabla puede tener solo un clustered: determina el orden fisico': la catedra lo dice asi (p.12); tecnicamente es orden logico/lista enlazada (matiz, no error)
- 'Fill factor 100 % ... tablas de solo lectura': correcto; la catedra recomienda 100% para claves siempre crecientes (p.17), no solo para solo lectura
- 'AUTO_UPDATE_STATISTICS activado por defecto': correcto en SQL Server

**Estilo (guía de contenido)**

- Mezcla dbo.Ventas/dbo.Clientes con ddbba.venta en otras paginas

### unidad-3/teoria/indices-y-planes — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-3/teoria/indices-y-planes.md` · temas: u3-plan-ejecucion, u3-estadisticas, u3-indices, u3-optimizacion, u3-rowstore-columnstore

**Conservar**

- Mejor desarrollo de estadisticas del portal: componentes, columnas del histograma, estadisticas automaticas, FULLSCAN, sync/async (fiel a 0d2a p.21-24)
- Consultas sys.stats/sys.stats_columns utiles
- Consulta de plan cache (dm_exec_cached_plans) correcta

**Faltante o superficial**

- Fases compilacion/ejecucion y componentes (Parser, Algebrizer, Optimizer, Execution Engine; cat. 0d2a p.5-8)
- Plan estimado vs real (p.9) y como leer un plan (p.10)
- Estadisticas filtradas y manuales
- Optimizacion de consultas con ejemplos antes/despues; solo hay lista de consejos
- Tablas temporales (8 reglas, p.29) y variables de tabla con indice
- Columnstore con sintaxis

**Solapamientos**

- unidad-3/teoria/indices-optimizacion: Indices, fill factor, rebuild/reorganize, rowstore/columnstore, scan/seek/key lookup y estadisticas duplicados; la propia pagina remite a esta

**Código a reconstruir o verificar**

- Seccion 'NONCLUSTERED INDEX SEEK + KEY LOOKUP': las tres consultas del ejemplo (SELECT Id, COUNT(1)) NO producen KEY LOOKUP porque el indice sobre DisplayName ya cubre Id (clave clustered); el comentario afirma que aparece el lookup. Para mostrarlo hay que pedir una columna fuera del indice (p. ej. SELECT * o Location)
- 'Sin indice en DisplayName: TABLE SCAN' sobre dbo.Users, que tiene clustered PK: el operador es CLUSTERED INDEX SCAN, no TABLE SCAN (esto se reserva para heaps); inconsistente con la propia definicion de la pagina
- 'CREATE CLUSTERED INDEX pk_users ON dbo.Users(Id)' 'si no existe': falla si ya existe PK clustered (ya hay un seek en PK_Users_Id); debe condicionarse o eliminarse
- Script de actualizacion masiva: 'IF DB_ID(''?'') > 4 USE [?]; EXEC sp_updatestats' - el IF solo gobierna el USE; EXEC sp_updatestats se ejecuta siempre (y USE dentro de EXEC dinamico no persiste); ademas sp_MSforeachdb es un procedimiento no documentado
- DBCC SHOW_STATISTICS ('dbo.Users', Reputation) con nombre de columna: acepta nombre de estadistica o indice; verificar en motor si resuelve por columna (las estadisticas automaticas se llaman _WA_Sys_...)
- 'Statistics Live Query' debe ser 'Include Live Query Statistics'
- Datos: depende de bases StackOverflow2013 y pruebasDB (ddbba.venta, venta2, cliente, indice ClientesPK) sin script ni enlace; los resultados esperados (EQ_ROWS, AVG_RANGE_ROWS, memoria reservada) no se muestran
- Consulta 'sys.stats/sys.stats_columns' final no filtra por tabla ni esquema (mezcla objetos de sistema)

**Sin fuente suficiente**

- 'Una consulta ad hoc con diferencias minimas (mayusculas, espacios) puede generar entradas duplicadas en versiones anteriores a SQL Server 2017': afirmacion de version sin fuente (el cache de ad hoc siempre distingue texto; 2017 no cambia eso)
- Datos de ejemplo StackOverflow2013 no estan en el corpus de catedra (aparecen solo en las demos del portal)

**Afirmaciones dudosas**

- Tabla 'Consejos de optimizacion': 'CHAR/VARCHAR en lugar de NCHAR/NVARCHAR: la mitad del almacenamiento' - la catedra lo dice (p.26) y es cierto en general, pero depende de la collation (UTF-8, compresion)
- Variables de tabla siempre 1 fila: ver doubtful_claims de indices-optimizacion
- 'Los cursores son costosos; preferir operaciones basadas en conjuntos': fiel a la catedra (p.27)

**Estilo (guía de contenido)**

- Esquema/nombres en minuscula (venta, cliente) y mezcla con dbo

### unidad-3/teoria/metricas-de-rendimiento — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento.md` · temas: u3-monitoreo

**Conservar**

- Cuenta de filas via dm_db_partition_stats (index_id 0/1), file IO acumulado desde el reinicio, tamano del backup de log, esperas activas con texto SQL: fiel a la catedra 17c2 p.34-41
- Concepto de baseline claro

**Faltante o superficial**

- Modelo BULK-LOGGED y limitaciones del modelo SIMPLE (17c2 p.36, 39)
- Ventajas y limitaciones de cada metrica (p.34, 35, 40)
- Metricas de hardware (CPU/memoria) y deadlocks como metrica (p.32)
- Activity Monitor y dashboards (p.31, 42)
- Ejemplos de resultado esperado de cada consulta

**Solapamientos**

- unidad-3/teoria/indices-optimizacion: Seccion 'Metricas de rendimiento' y tabla Simple vs Full repetidas

**Código a reconstruir o verificar**

- COUNT(*) 'requiere un INDEX SCAN': correcto si hay indice; en heap seria TABLE SCAN: matizar
- dm_db_partition_stats.row_count se presenta como 'basado en datos en memoria' y 'aproximado': es metadato de la particion, normalmente exacto salvo concurrencia/ghost records; la afirmacion es imprecisa
- Para tablas particionadas/con varios indices hay que sumar row_count de las particiones del indice 0/1; la consulta de todas las tablas devuelve una fila por particion
- Consulta del backup de log: JOIN con sys.master_files type 'ROWS' duplica filas si hay varios archivos de datos, y 'database_archivo_mbs' mide tamano del archivo, no de la base
- Consulta de esperas: select de columnas calificadas con nombres de vista completos pero la tabla 'Campos clave' menciona 'status' que no esta en el SELECT
- 'UPDATE que fija el mismo valor igual genera entrada en el log': afirmacion de la catedra (no verificada en corpus); verificar en motor
- Uso de CONVERT(VARCHAR(MAX), Query_Hash, 1) con alias de tabla ambiguo: Query_Hash sin calificar; funciona porque solo esta en dm_exec_requests

**Sin fuente suficiente**

- 'Los datos se retienen en msdb por un periodo acotado (tipicamente al menos un dia)': sin fuente; la retencion depende del mantenimiento (sp_delete_backuphistory)
- Alternativa por PowerShell: sin fuente

**Afirmaciones dudosas**

- 'La metrica util es la variacion respecto al estado normal': correcto (cat. p.33)

**Estilo (guía de contenido)**

- Alias como nombre completo de tabla (dm_exec_requests.session_id) en vez de alias cortos

### unidad-3/teoria/transacciones-concurrencia — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-3/teoria/unidad-3.md` · temas: u3-tcl, u3-concurrencia, u3-bloqueos, u3-distribuidas

**Conservar**

- Ejemplos claros de autocommit/explicito/implicito, SAVE TRANSACTION y anidamiento con @@TRANCOUNT (correctos)
- Tabla de niveles de aislamiento coherente con SQL Server (incluye RCSI y SNAPSHOT) y comparacion SNAPSHOT vs RCSI (error 3960 correcto)
- Seccion de transacciones distribuidas: unica de las dos paginas que la trata; fiel a la catedra 17c2 p.27-30
- Las '10 reglas' como cierre

**Faltante o superficial**

- Estados de una transaccion y argumento de durabilidad con log (cat. 17c2 p.6, 9)
- Planificaciones secuenciales/serializabilidad y bloqueo en notacion de la catedra (p.14-15)
- XACT_ABORT (se delega)
- Ejemplo con resultado esperado de dirty read ejecutable (se delega al laboratorio)
- Sintaxis completa de BEGIN DISTRIBUTED TRANSACTION y requisitos de MS DTC/linked server

**Solapamientos**

- unidad-3/teoria/transacciones-y-concurrencia: Repite modos de transaccion, BEGIN/COMMIT/ROLLBACK, SAVE TRANSACTION, @@TRANCOUNT anidado, TRY/CATCH, fenomenos, tabla de niveles y deadlocks (prevencion con la misma lista de 5 puntos). Se recomienda unir en una sola pagina de TCL y concurrencia y otra de bloqueos/deadlocks/distribuidas

**Código a reconstruir o verificar**

- Los ejemplos usan ddbba.Cuentas/CuentaID/AuditoriaTransacciones (PascalCase) mientras la pagina hermana y los laboratorios usan cuentas/cuenta_id en minuscula; ninguno de los dos define la tabla (DDL + datos) en la teoria: ejemplos no autocontenidos
- En 'Modos de transaccion' se dice que IMPLICIT_TRANSACTIONS abre TX ante 'cualquier DML/DDL'; en realidad tambien con SELECT (y otras sentencias como OPEN, FETCH, etc.): impreciso, no incorrecto para el caso comun
- TRY/CATCH: el ejemplo hace THROW 50001 dentro del TRY sin SET XACT_ABORT ni XACT_STATE(); funciona, pero no muestra el patron robusto con XACT_STATE() = -1 (verificar en motor si se quiere ilustrar)

**Sin fuente suficiente**

- Prevencion de deadlocks (5 puntos), DEADLOCK_PRIORITY, error 1205: sin fuente de catedra en el corpus (conocimiento general de SQL Server; consistente con Microsoft Learn)
- Guia de seleccion de nivel de aislamiento ('cuando usarlo'): sin fuente de catedra

**Afirmaciones dudosas**

- 'AUTOCOMMIT: cada sentencia DML es su propia transaccion': tambien aplica a DDL y SELECT; menor
- SNAPSHOT 'No (versionado)' en bloqueo de lectura: correcto, pero SNAPSHOT tambien necesita que ALLOW_SNAPSHOT_ISOLATION este ON (esta aclarado)
- 'READ COMMITTED (default)' correcto en SQL Server en instancia local; en Azure SQL Database el default es RCSI ON (la catedra lo indica en 17c2 p.21): el portal no lo aclara

**Estilo (guía de contenido)**

- Tablas en PascalCase pero sin singular (Cuentas)
- Nombre de archivo (unidad-3.md) no coincide con slug

### unidad-3/teoria/transacciones-y-concurrencia — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia.md` · temas: u3-tcl, u3-concurrencia, u3-bloqueos

**Conservar**

- Aporte propio util: XACT_ABORT, funciones ERROR_*, patron de SP con THROW, captura de error 1205, DMVs de diagnostico
- Savepoint y @@TRANCOUNT con explicacion del estado posterior
- Consulta system_health ring_buffer para xml_deadlock_report (sintaxis correcta; requiere VIEW SERVER STATE)

**Faltante o superficial**

- Definicion de las tablas cuentas/auditoria usadas en SP y ejemplos (DDL + datos + resultado esperado)
- XACT_STATE() para decidir COMMIT/ROLLBACK en CATCH con XACT_ABORT ON
- Resultado esperado de cada EXEC de transferir_saldo
- Bloqueo con ejemplo ejecutable y su observacion en dm_tran_locks
- Transacciones distribuidas (solo esta en unidad-3.md)

**Solapamientos**

- unidad-3/teoria/transacciones-concurrencia: Casi todo el contenido de TCL, fenomenos, niveles y deadlocks esta duplicado; la tabla de niveles aparece con formato distinto y el texto 'Los tres problemas' repite lo de unidad-3.md
- unidad-3/practica/laboratorio-aislamiento: La seccion de niveles remite al laboratorio; el diagnostico usa la BD LabTransacciones definida alli

**Código a reconstruir o verificar**

- Tabla XACT_ABORT: la fila 'Error grave (violacion de constraint)' dice que con XACT_ABORT OFF se cancela la transaccion. Incorrecto: una violacion de constraint (PK, NOT NULL, FK) es un error que termina la sentencia pero deja la transaccion abierta con XACT_ABORT OFF (solo errores de severidad alta/ruptura de conexion la abortan); es justamente la razon de ser de XACT_ABORT ON
- Misma tabla: 'overflow aritmetico' como ejemplo de error leve: con ARITHABORT/ANSI_WARNINGS por defecto el desbordamiento aritmetico termina la sentencia/lote segun configuracion; verificar en motor antes de afirmarlo
- Ejemplo XACT_ABORT: 'INSERT INTO tabla_b VALUES (NULL)' sin DDL de las tablas (tabla_a/b/c no definidas) y se afirma 'rollback automatico' sin mostrar @@TRANCOUNT
- Seccion 'Deadlocks': primera mitad usa ddbba.cuentas, ejemplo de captura usa pedidos/clientes, el resto usa cuentas sin esquema: mezcla de esquemas; el SP usa dbo.transferir_saldo sobre cuentas (sin ddbba)
- Seccion 'Autocommit' usa 'saldo = saldo + 0' (no demuestra nada y deja el estado sin cambio); sirve como control pero no ilustra el riesgo descripto
- Transferencia bancaria con IF EXISTS(... saldo<0) examina TODA la tabla en vez de la cuenta origen: cualquier otra cuenta en negativo cancela la transferencia
- Referencia rapida: SET LOCK_TIMEOUT -1 espera indefinida es correcto; 'SET LOCK_TIMEOUT 5000' mal caracterizado solo como comentario

**Sin fuente suficiente**

- Matriz de compatibilidad de bloqueos (S/X/U/Intent): fuera de la catedra del corpus
- DEADLOCK_PRIORITY y 'victima de menor costo de rollback' (correcto pero sin fuente)

**Afirmaciones dudosas**

- 'El BEGIN TRANSACTION va antes del TRY para que el ROLLBACK del CATCH pueda revertirla. Si lo ponés dentro del TRY y el propio BEGIN TRANSACTION falla...': razon de diseno debil; ambos patrones son validos, lo importante es evaluar @@TRANCOUNT/XACT_STATE en el CATCH
- 'THROW en lugar de RAISERROR': recomendacion de estilo valida desde SQL Server 2012, no una regla

**Estilo (guía de contenido)**

- cuentas/cuenta_id en minuscula vs convencion PascalCase singular
- Emoji en enlace a laboratorio

### unidad-4/practica — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-4/practica/index.md` · temas: u4-mql-crud, u4-agregacion

**Conservar**

- Indice de las tres practicas

**Faltante o superficial**

- Aclarar que los archivos referenciados por 'Integrador' y 'tienda_online' no estan publicados
- Enlace a la guia de TP de catedra (3df2: TP MongoDB con Atlas y entrega en PDF)

### unidad-4/practica/ejercicios — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-4/practica/practica.md` · temas: u4-mql-crud, u4-agregacion, u4-estadisticas-indices

**Conservar**

- Sigue la guia de ejercicios de la catedra (f65c): bases Astronomia, Clima, Airbnb, Deteccion_Fraude; indices, vista y agregaciones
- Laboratorio I sobre datosventas con consultas correctas en sintaxis
- Archivos cc_info.csv (984 filas), transactions.csv (294.588 filas) y datosventas_1.json (50 documentos, fecha como $date) existen en public/bbdd-aplicadas/unidad-4/practica/archivos/ y son coherentes con el texto

**Faltante o superficial**

- Soluciones/resultados esperados de las partes 1-9 (solo se muestran comandos)
- Resolucion de los 25 enunciados de la guia de TP de la catedra sobre datosventas (3df2 p.1: bulk insert, delete id_venta>50, aggregates por vendedor/localidad/mes, top 3 clientes, etc.): el portal tiene 20 consultas propias distintas
- Ejercicio de $lookup entre dos colecciones propias + vista de 7 etapas (3df2 p.2) y MongoDB Atlas
- Archivo de la coleccion datosvendedores usada en teoria ($lookup, indices)
- Solucion de la Practica adicional (BD Clima) y dataset de Open-Meteo

**Solapamientos**

- unidad-4/teoria/mongodb-crud: Las mismas operaciones se explican en la teoria
- unidad-4/practica/laboratorio-tienda-online: CRUD y aggregate sobre otra BD

**Ejercicios y soluciones**

- Ejercicio 7 reinserta 'Sirio', 'Canopus', 'Arturo' y 'Alfa Centauri A' ya insertados en los ejercicios 3 y 4: quedan documentos duplicados (con distinto _id); el ejercicio 9 (deleteOne Canopus) borra solo uno y deja el duplicado. Falta aclarar si se debe vaciar la coleccion (deleteMany({}) o drop) antes
- Ejercicio 2: pide 'crear la coleccion con los campos' (tabla de tipos) pero createCollection no define campos ni tipos; tampoco se menciona validator (en MongoDB no hay DDL de columnas)
- Ejercicio 8: updateOne para Canopus y luego updateMany({}) hacen redundante el primero; no esta claro si son alternativas
- Ejercicio 11: cita 'archivos/sample_airbnb.listingsAndReviews.json' pero en public/ solo existe sample_airbnb.listingsAndReviews.zip (contiene el JSON de ~112 MB): el nombre del archivo no coincide y no se aclara que hay que descomprimir
- Ejercicio 12/13: crea la vista 'Transacciones_Estado'; el ejercicio 14 usa 'Transacciones_Estado_1'. Una de las dos esta mal (proviene de capturas de la catedra); con el nombre del ejercicio 13 la vista de 14 no existe
- Ejercicio 13: $lookup de 294 mil transacciones contra cc_info sin indice en cc_info.credit_card es costoso (no se sugiere crear el indice, que seria la aplicacion natural del tema)
- Ejercicio 14 '$group _id: "idAux"' usa una cadena constante como clave; es valido pero conviene null; $cmp: el filtro usa date como String '2015-08-16 19:02:57' (solo coincide si el CSV se importo con fecha String); el valor credit_card 9383760568579492 excede 2^53 pero es par y exacto en mongosh; verificar en motor que Compass lo importa como Int64
- Laboratorio I, consulta 20: filtra 'dolar: true' al nivel raiz, pero en datosventas_1.json 'dolar' esta dentro de 'producto' (producto.dolar) y solo en algunos documentos; la consulta devuelve 0 resultados. Debe ser 'producto.dolar': true
- Laboratorio I, consulta 8: { cantidad: { $not: { $gt: 10 } } } devuelve los 50 documentos (cantidad maxima 5): no demuestra nada con estos datos; consulta 3 (> 4) devuelve 9, la 6 (>2 y Ramos Mejia) etc.: faltan resultados esperados
- Consultas 18/19: se actualizan id_venta 1 y 2 (tags/comentarios inexistentes) pero el segundo parametro usa tags/comentarios como condicion de ausencia; bien, aunque no se muestra la comprobacion
- Parte 9: 7 items de la BD Clima sin solucion; el item 3 pide descargar un CSV de Montevideo (fuente externa); el item 6 'fechas de temperatura diaria promedio maxima' requiere $dateToString que no se ensena en la teoria de forma completa

**Código a reconstruir o verificar**

- Ejercicio 10: instrucciones dependen de descarga externa (open-meteo.com): sin dataset publicado ni columnas esperadas (temperature_2m, rain, windspeed_100m)
- Ejercicio 5: 'campo_int32: 42' y verificacion de tipo en Compass dependen de que mongosh inserte Int32; correcto en mongosh actual, distinto en el shell antiguo (verificar)
- Consulta 4 '{ "cliente.nombre": 1, cantidad: 1, _id: 0 }': correcta
- Consulta 12/13/14: dependen de que 'fecha' se importe como Date; datosventas_1.json usa {'$date': ...} (Extended JSON) por lo que Compass/mongoimport lo convierten en Date: correcto

**Sin fuente suficiente**

- Laboratorio I: 20 consultas propias del portal, distintas de las 25 de la guia 2 de catedra (3df2)
- Ejercicios 1-14 siguen f65c; el resto (Clima) sigue f65c p.36 'Practica adicional'

**Estilo (guía de contenido)**

- Bases/colecciones con nombres mixtos: Astronomia/Estrella, Deteccion_Fraude, datosventas

### unidad-4/practica/integrador-peliculas — **investigar**

`src/content/docs/bbdd-aplicadas/unidad-4/practica/integrador-peliculas.md` · temas: u4-mql-crud, u4-agregacion, u4-estadisticas-indices

**Conservar**

- Consultas MQL bien formadas y didacticas: $dateFromString/$dateDiff en update con pipeline, $lookup + $unwind con preserveNullAndEmptyArrays, $group compuesto, $unwind de actores
- Diferencia entre campo ausente y nulo; conversion de fechas string a Date
- Indices multikey y vista 'vw_prestamos_detalle'; aclara que las vistas no se materializan

**Faltante o superficial**

- Los datasets Peliculas.json y Prestamos.json NO existen en el repositorio ni en public/ ('provistos con el material de la catedra'): sin ellos no hay datos ni resultados verificables; el corpus tampoco los contiene
- Resultados esperados; soluciones de los 'Desafios sin solucion inmediata' (6 items)
- Esquema real de los documentos (el diagrama ER es inferido: fechaPrestamo como string, importe double, director embebido); no verificable contra el dataset

**Solapamientos**

- unidad-4/practica/ejercicios: Practica similar a Laboratorio I (datosventas) con otro dominio

**Ejercicios y soluciones**

- Parte A.5: { calificacion: null } y { $exists:true, $type:'null' } dependen de un campo 'calificacion' cuya existencia en el dataset no consta
- Parte B: $dateFromString sobre 'AAAA-MM-DD' funciona en MongoDB; pero 'tipo: { $type: "$fechaPrestamo" }' en una proyeccion de find() es sintaxis valida desde 4.4 solo como expresion de agregacion ($type en $project de aggregate); en find() la proyeccion con $type como operador de agregacion requiere 4.4+: verificar en motor
- $dateDiff con unit 'day' requiere MongoDB 5.0+ (aunque la pagina no lo indica)
- Parte D: indice unico { idPelicula: 1 } sobre peliculas falla (E11000) si el dataset tiene duplicados; sin verificacion
- Parte C.6: el pipeline asume que 'diasPrestamo' fue creado en la Parte B (dependencia entre partes no aclarada)
- Consultas de la Parte A dependen de valores literales (Christopher Nolan, Al Pacino, Virrey del Pino) que no se pueden verificar sin el dataset

**Código a reconstruir o verificar**

- Para el update con pipeline ([ { $set: ... } ]) se requiere MongoDB 4.2+: correcto pero no aclarado
- La referencia 'no se enlazan mediante la etiqueta Liquid {% link %}' es un comentario de infraestructura de otra plataforma que no aplica a Starlight

**Sin fuente suficiente**

- Ambos datasets y el escenario 'Peliculas y Prestamos/videoclub' no tienen respaldo en el corpus de catedra (el corpus menciona prestamos de biblioteca en el parcial 2C2026, 1fbe p.4, y peliculas en un examen de alumno e694 p.1, sin dataset)
- Es una practica integradora elaborada por el portal, no de la catedra

**Afirmaciones dudosas**

- 'preserveNullAndEmptyArrays evita perder prestamos sin pelicula': correcto

**Estilo (guía de contenido)**

- Referencia a plantilla Liquid residual

### unidad-4/practica/laboratorio-tienda-online — **reemplazar**

`src/content/docs/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online.md` · temas: u4-mql-crud, u4-agregacion, u4-estadisticas-indices

**Conservar**

- Estructura por niveles (CRUD, consultas avanzadas, pipeline) y comparativa SQL vs MongoDB
- Consultas MQL sintacticamente correctas ($mul, $all, $facet, $map, $bucket, $round)
- Aviso honesto de 'Material no oficial'

**Faltante o superficial**

- Los scripts 01_setup_datos.js y 03_api_externa.js no estan en el repositorio (en public/ solo existe inputs/MongoDB-no-oficial/MongoDB no oficial.pdf); sin ellos el dataset (6 clientes, 8 productos, 6 pedidos, 4 resenas) no se puede reconstruir
- Resultados esperados de cada consulta (solo se da 'electronica $3,279 \| hogar $449 \| libros $149' en 3.2 y totalDocsExamined 6/3)
- Datos de ejemplo embebidos en la pagina

**Solapamientos**

- unidad-4/teoria/mongodb-agregacion: Pipeline de ventas por categoria, $bucket y $facet duplicados literalmente

**Ejercicios y soluciones**

- Archivos referenciados inexistentes: 'archivos/MongoDB-no-oficial/01_setup_datos.js' y '03_api_externa.js' (no estan; ni siquiera en public/bbdd-aplicadas/unidad-4/practica/archivos/): el laboratorio no es ejecutable; ademas el script de la API requiere red (Open Library) y Node
- 1.2 usa 'categoria: electronica' con tilde pero el dato real del dataset es desconocido
- 1.3: aplicar $mul 1.10 sobre un double produce errores de redondeo; mejor Decimal128
- 1.5 'DELETE ... WHERE stock = 0 AND activo = false': depende de que existan esos documentos; sin datos no hay resultado esperado
- 2.8: $type 'number' es alias valido de MongoDB
- 3.2: el resultado indicado (electronica $3,279...) no se puede verificar sin el dataset
- Bonus API: Math.random para precio vuelve no reproducible el resultado; la fuente externa puede cambiar
- 'Indices y performance': TTL en { fecha: 1 } con expireAfterSeconds requiere campo Date; podria borrar pedidos de verdad si se aplica sobre la coleccion real; falta advertencia

**Código a reconstruir o verificar**

- 'Transacciones ACID multi-documento (v4+)' en tabla SQL vs MongoDB: correcto desde 4.0 (replica set) y 4.2 (sharded); requiere replica set, no funciona en standalone
- El indice compuesto se muestra como { categoria: 1, precio: 1 } en el codigo y { categoria: 1, precio: -1 } en la tabla de tipos: inconsistencia

**Sin fuente suficiente**

- El laboratorio completo es 'material no oficial' propio sin fuente de catedra; el propio portal lo declara
- Cifras de totalDocsExamined (6 y 3) y executionTimeMillis: <1 dependen del dataset no disponible

**Afirmaciones dudosas**

- 'Horizontal (sharding nativo)' / 'Vertical' en la comparativa: simplificacion; los RDBMS tambien escalan horizontalmente con particionado/replicas

**Estilo (guía de contenido)**

- Mezcla de singular/plural y snake_case en colecciones (clientes, resenas)

### unidad-4/teoria — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/index.md` · temas: u4-base-acid, u4-modelos-datos, u4-data-lakes, u4-kdd-datamining

**Conservar**

- Resultados de aprendizaje claros
- Aclaracion de que 'no transaccionales' no significa sin transacciones (MongoDB admite ACID multidocumento)
- Ruta sugerida de estudio

**Faltante o superficial**

- Mencion explicita de la relacion con POO y de los modelos jerarquicos/texto del programa
- Aviso de que el tema KDD/Data Mining esta en el programa (3d97 p.3) pero sin material de catedra

**Unidad incorrecta**

- Encabezado 'BD No Transaccionales (NoSQL) · 2do parcial': esquema 2023 (dos parciales). En 2024 hay un unico parcial (u1-u4) segun el cronograma 6538 y el programa; la u4 se evalua en el mismo parcial que u1-u3

**Solapamientos**

- unidad-4/teoria/apunte-completo: Hay dos rutas (apunte completo y paginas tematicas) con la misma informacion; el indice las presenta como complementarias

**Sin fuente suficiente**

- 'Vistas' y 'KDD' en el resumen: las vistas tienen respaldo (9a0d p.21-23); KDD no tiene material de catedra en el corpus

**Afirmaciones dudosas**

- 'MongoDB moderno admite garantias ACID y transacciones multidocumento': correcto desde 4.0 (replica sets) y 4.2 (sharded); el portal las atribuye al apunte sin version (lab tienda_online dice 'v4+')

### unidad-4/teoria/apunte-completo — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/unidad-4.md` · temas: u4-base-acid, u4-tipos-nosql, u4-mql-crud, u4-agregacion, u4-estadisticas-indices, u4-data-lakes, u4-kdd-datamining, u4-modelos-datos

**Conservar**

- Resumen unificado util como pagina unica de repaso
- Fiel a la catedra en historia, ACID/BASE, CAP, modelos, BSON, tipos, ObjectId, schema/validator, CRUD basico
- Seccion de vistas con $lookup/$project/$unwind y aclaracion final de data lake gobernado

**Faltante o superficial**

- Upsert, $inc/$push/$mul, replaceOne, bulk ordered, findOne/count (cubiertos parcialmente en mongodb-crud)
- $sort/$limit/$skip con ejemplo, $addFields, $bucket, $facet, $replaceRoot (en mongodb-agregacion)
- Tipos de indices adicionales (compuesto, unico, sparse, parcial; solo hay un indice simple)
- explain('executionStats')

**Solapamientos**

- unidad-4/teoria/nosql-conceptos: Historia, tipos de datos, arquitectura de cluster, ACID/BASE, CAP y modelos NoSQL duplicados (con menos matices)
- unidad-4/teoria/mongodb-introduccion: BSON, terminologia, tipos, ObjectId, schema, mongosh y gestion de BD/colecciones duplicados
- unidad-4/teoria/mongodb-crud: CRUD y operadores duplicados (version resumida)
- unidad-4/teoria/mongodb-agregacion: Pipeline, indices y vistas duplicados (version resumida)
- unidad-4/teoria/mongodb-compass: Resumen de Compass
- unidad-4/teoria/datos-data-lake-kdd: Data lake y KDD duplicados (version resumida, sin diagramas)

**Código a reconstruir o verificar**

- Tabla 'Operadores de acumulacion' incluye $cmp, que no es acumulador sino operador de comparacion de expresiones
- Descripcion de $unwind: 'convierte un campo array en un valor escalar' es impreciso: genera un documento por elemento del array
- Linea de tiempo: '1967 COBOL / Codasyl' y '1982 PL/SQL / Oracle': datos copiados de la catedra (ed68 p.3) pero discutibles; PL/SQL aparece en 1991 (Oracle 6) y Oracle V2 es de 1979 (la pagina nosql-conceptos ya los corrigio con redaccion generica)
- createView: la vista 'Transacciones_Estado' se crea con $project antes de $unwind: correcto; en el resto del portal se usa 'Transacciones_Estado_1' (ver practica)
- getIndexes() sobre cc_info: la catedra usa city_indx como name; el comando createIndex({city:1},{name:'city_indx'}) es correcto

**Sin fuente suficiente**

- Los 7 pasos de KDD (integracion y presentacion/decision) sin fuente en el corpus
- Afirmacion 'CP: ... Redis' sin matices (proviene del diagrama de la catedra ed68 p.24 pero es discutible)

**Afirmaciones dudosas**

- 'CA: RDBMS (SQL Server, MySQL)': simplificacion de la catedra; en un sistema distribuido P no es opcional
- 'No se permiten claves duplicadas (MongoDB conserva el ultimo valor)': BSON tecnicamente permite claves repetidas; es el shell/parser JSON el que las colapsa; matizado en mongodb-introduccion pero no aqui
- 'El orden de los campos BSON importa' (afirmacion sin matiz): importa para comparar documentos embebidos y para igualdad exacta; en mongodb-introduccion ya esta matizado

**Estilo (guía de contenido)**

- Mezcla de bloques ```javascript para comandos de shell (use ...)
- Nombres de colecciones de ejemplo en minuscula o con mayuscula inicial sin criterio

### unidad-4/teoria/datos-data-lake-kdd — **investigar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd.md` · temas: u4-data-lakes, u4-kdd-datamining, u4-modelos-datos

**Conservar**

- Clasificacion de datos por estructura con aclaracion util (JSON es semiestructurado; EXIF)
- OCR/NLP con ejemplos
- Data Lake vs Data Warehouse (schema on read/write) y riesgo de data swamp
- Preguntas tipicas de parcial y autoevaluacion

**Faltante o superficial**

- Data Warehousing propiamente dicho (modelo dimensional, ETL/ELT, OLAP) que figura en los contenidos minimos
- Fuente de catedra: no hay material propio de catedra sobre data lakes/KDD en el corpus; solo apuntes de alumnos (3c6c p.22-23, 1a42 p.9, 3a0d p.17)
- Referencia a la formulacion original de KDD

**Unidad incorrecta**

- KDD y Data Mining: el brief indica que 'no estan en la u4 2024'; pero el programa 2024 del corpus (3d97 p.3) SI los lista en la u4 ('Introduccion al Data Mining. Knowledge Discovery in Databases'). Resolver con la catedra antes de reubicar o eliminar. Si el criterio es 2024 estricto segun el brief, es del programa 2023/contenidos minimos

**Solapamientos**

- unidad-4/teoria/apunte-completo: Secciones 'Data Lake' y 'KDD' duplicadas en forma resumida

**Ejercicios y soluciones**

- Autoevaluacion sin respuestas; ejercicio 5 pide 'una fuente por cada tipo de dato': enunciado abierto, sin solucion

**Sin fuente suficiente**

- KDD en 7 etapas (con 'integracion' y 'presentacion y decision'): el KDD clasico de Fayyad tiene 5; las 7 etapas no figuran en ninguna fuente del corpus. Requiere fuente primaria
- Tareas de mineria (clasificacion, regresion, clustering, asociacion, anomalias): conocimiento general sin fuente en el corpus
- Gobierno del data lake (catalogo, lineage, zonas raw/depurada/consumo): aporte del portal, no de la catedra
- Caso de abandono de clientes: el corpus lo trae en ed68 p.10 como ejemplo de minería; el desarrollo extenso es del portal

**Afirmaciones dudosas**

- 'KDD: proceso iterativo... conocimiento valido, novedoso, util y comprensible': definicion de Fayyad correcta pero sin cita

### unidad-4/teoria/guia-parcial — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/guia-parcial.md` · temas: u4-base-acid, u4-mql-crud, u4-agregacion, u4-estadisticas-indices, u4-data-lakes

**Conservar**

- Tabla de comparaciones que coincide con lo que los examenes preguntan (CAP, ACID/BASE, indices, find vs aggregate)
- Lista de errores frecuentes y cómo leer una consulta MQL
- Simulacro con consignas variadas

**Faltante o superficial**

- Ejercicios de u3 (indices de cobertura, cluster, niveles de aislamiento) que el MISMO parcial 2024 evalua junto con u4 (guia para el parcial de u1-u4)
- Soluciones/respuestas esperadas del simulacro
- Preguntas tipo 'son equivalentes estas consultas' (1fbe p.~4) y 'completar aggregate' (2547, d8ba)
- Preguntas de CAP en formato V/F que aparecen en 3 examenes recientes (cf1a, 8d75, 1fbe)

**Unidad incorrecta**

- Titulo/metadata de 'Guia para el parcial' hereda el esquema 2023 de '2do parcial' desde el index; en 2024 el parcial abarca u1-u4

**Solapamientos**

- unidad-4/teoria/apunte-completo: Reexplica comparaciones ya presentes

**Ejercicios y soluciones**

- Simulacro de 10 puntos sin respuestas ni criterios de correccion
- El simulacro no incluye consignas de modelado o de lectura de un pipeline, que aparecen en los examenes

**Código a reconstruir o verificar**

- La consulta de ejemplo con $or e ISODate es correcta; la lectura verbal tambien
- 'Crear { city_indx: 1 }' como error comun: correcto

**Sin fuente suficiente**

- Preguntas y 'respuestas esperadas': elaboradas por el portal (no de catedra); marcarlas como material de estudio no oficial

**Afirmaciones dudosas**

- 'Siempre describi la forma de los documentos despues de cada etapa': consejo valido, no de catedra

### unidad-4/teoria/instalacion-mongodb — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb.md` · temas: u4-mql-crud

**Conservar**

- Distingue servidor, shell, Compass y Atlas con diagrama
- Diagnostico rapido, checklist y advertencia de credenciales (el documento de catedra de instalacion esta excluido del corpus)
- Uso de marcadores en las URI

**Faltante o superficial**

- Instalacion en macOS/Linux (solo se menciona 'net start MongoDB' de Windows)
- Creacion de usuario y habilitacion de autenticacion en local
- Pasos para crear cluster gratuito de Atlas y cargar la base (pide la guia 3df2 p.2: cluster, usuario de solo lectura)

**Unidad incorrecta**

- La instalacion de MongoDB no figura como tema separado en el programa 2024 (u4); es soporte de laboratorio

**Solapamientos**

- unidad-4/teoria/mongodb-introduccion: Conexion con mongosh repetida
- unidad-4/teoria/mongodb-compass: Conexion con Compass repetida

**Código a reconstruir o verificar**

- 'net start MongoDB' depende de que el servicio se llame MongoDB (instalador por defecto); en macOS/Linux usar brew services/systemctl

**Sin fuente suficiente**

- Tabla de diagnostico y checklist: aporte del portal (no verificable contra el documento de instalacion, excluido)

### unidad-4/teoria/mongodb-agregacion — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion.md` · temas: u4-agregacion, u4-estadisticas-indices

**Conservar**

- Descripcion de etapas con ejemplos: $match, $project, $addFields, $replaceRoot+$mergeObjects, $lookup, $group, $unwind (con opciones), $count, $sortByCount, $bucket, $bucketAuto, $facet
- Indices: simple, embebido, compuesto (regla del prefijo), unico (E11000), array, sparse, parcial, dropIndex
- Aviso sobre reIndex() y vistas de solo lectura
- COLLSCAN vs IXSCAN con explain('executionStats')

**Faltante o superficial**

- Operadores de expresion vs acumuladores diferenciados
- $out/$merge/$setWindowFields con ejemplo (se listan pero no se desarrollan)
- $dateDiff con $$NOW y formateo de fechas con resultado (cat. 9a0d p.17)
- Indices TTL, hashed, texto y geoespaciales; indices de texto con $text
- Estadisticas de ejecucion detalladas (nReturned, totalKeysExamined, winningPlan) y explain de aggregate
- Resultado esperado de cada pipeline con datos concretos (las colecciones pedidos/productos no se proveen en la teoria)

**Solapamientos**

- unidad-4/practica/laboratorio-tienda-online: El pipeline 'ventas por categoria', $bucket y $facet se repiten literalmente en el laboratorio
- unidad-4/teoria/apunte-completo: Version resumida en el apunte completo

**Código a reconstruir o verificar**

- Tabla 'Operadores de acumulacion' lista $cmp, $multiply y $round: no son acumuladores de $group. Corregir clasificacion (son operadores de expresion aritmetica/comparacion)
- Seccion 'Eliminar indices': dropIndex('cliente.localidad_hashed') nunca se crea (viene del OCR de la catedra 9eb3 p.13); y 'nIndexesWas: 2' no es coherente con los indices listados antes (hay 6)
- '$facet: Imposible de replicar en SQL sin multiples CTEs': afirmacion exagerada
- $unwind en la vista Transacciones_Estado: 'convierte el array city en un valor escalar': impreciso (genera un documento por elemento)
- Indice sparse: se afirma que un campo existente con valor null forma parte del indice: correcto
- Sin datos reproducibles: $lookup 'datosvendedores' (campos Id, nombre, ciudad, pais) y los indices sobre datosvendedores/apellidos requieren una coleccion que NO esta en public/ (solo datosventas_1.json)
- El indice parcial muestra 'partialFilterExpression: { importe: { $exists: true, $gt: 500 } }': valido; $exists:true ya es implicito por $gt (redundante)
- El orden de la regla del prefijo se ejemplifica con { localidad, marca }; sin resultado de explain que lo demuestre
- reIndex(): la pagina lo marca como historico (correcto); en MongoDB 6+ esta deprecated/solo para standalone: verificar version

**Sin fuente suficiente**

- Seccion 'Categorias de etapas' ($redact, $graphLookup, $setWindowFields...): del portal, sin fuente de catedra completa

**Afirmaciones dudosas**

- 'El indice _id se crea al insertar el primer documento': se crea al crear la coleccion
- 'Si ya existe, no se sobreescribe' (createIndex idempotente con misma definicion): correcto

**Estilo (guía de contenido)**

- Emoji de advertencia en el texto

### unidad-4/teoria/mongodb-compass — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/mongodb-compass.md` · temas: u4-mql-crud, u4-estadisticas-indices

**Conservar**

- Guia completa de Compass alineada con la catedra 4bd5 p.35-58 y 9a0d p.5-27 (conexion, insercion, importacion, filtros, collation, edicion, clones, agregaciones, indices, explain)
- Opciones de collation explicadas

**Faltante o superficial**

- Captura o descripcion de las opciones de Explain Plan con los campos exactos
- Conexion a Atlas paso a paso (Network Access, usuario) como pide la guia de TP 3df2 p.2

**Solapamientos**

- unidad-4/teoria/apunte-completo: Resumen de Compass duplicado
- unidad-4/teoria/instalacion-mongodb: Conexion local/Atlas repetida

**Código a reconstruir o verificar**

- Filtro { 'cliente.localidad': 'Ramos Mejia' } sin tilde: en datosventas_1.json el valor es 'Ramos Mejía'; no devuelve resultados
- Importacion de CSV: se pide especificar el tipo por columna; para transactions.csv la fecha queda String (el ejercicio $cmp de la practica depende de ello); no se advierte

**Sin fuente suficiente**

- MongoDB Assistant: solo se lo describe; no hay fuente de catedra (aparece en capturas de 4bd5)

**Afirmaciones dudosas**

- 'Compass es de codigo abierto': su licencia es SSPL desde versiones recientes; verificar licencia actual

### unidad-4/teoria/mongodb-crud — **ampliar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/mongodb-crud.md` · temas: u4-mql-crud

**Conservar**

- Cobertura correcta de CRUD y operadores de comparacion, conjuntos, logicos, arrays y evaluacion
- Fechas BSON con ISODate y aviso sobre comparacion Date vs String
- Respuestas de update/delete con matchedCount/modifiedCount/deletedCount

**Faltante o superficial**

- Ejemplo de upsert con resultado (upsertedId/upsertedCount) pese a que el programa lo pide expresamente
- Insercion bulk: opcion ordered:false y manejo de errores parciales; bulkWrite
- replaceOne, findOneAndUpdate, remove legado
- findOne, countDocuments, distinct, skip con ejemplo de paginacion
- Ejemplos con $push/$pull/$addToSet con resultado antes/despues

**Solapamientos**

- unidad-4/teoria/apunte-completo: El apunte completo repite una version resumida
- unidad-4/practica/ejercicios: Los mismos ejemplos (datosventas, Estrella) aparecen en la practica

**Código a reconstruir o verificar**

- Respuesta de updateOne: el bloque muestra insertedId: null y upsertedCount: 0 pero el texto describe 'upsertedId'; en mongosh el campo es upsertedId solo cuando hay upsert (ver doc oficial)
- Comparar fecha con un string: la pagina afirma que 'compara Date contra String segun el orden de tipos BSON'; en operadores de consulta ($gt/$gte/$lt/$lte) rige el 'type bracketing': solo compara valores del mismo tipo, por lo que simplemente NO devuelve esos documentos. La conclusion (no sirve) es correcta; la explicacion no
- Fila 'Filtro + proyeccion' de la tabla SQL<->MongoDB usa SELECT id, status pero MongoDB proyecta user_id: inconsistencia
- $not con $gt: correcto; $where documentado con aviso (bien)
- Ejemplo de filtro 'cliente.localidad: Ramos Mejia' ya se usa 'Mejía' en datosventas; Compass usa 'Mejia' sin tilde (ver compass)

**Sin fuente suficiente**

- Operadores $expr/$text/$where: la catedra solo enumera ($where/$text aparecen en 4bd p.26, 49); los ejemplos son del portal (correctos)

**Afirmaciones dudosas**

- 'No requiere modificar la coleccion previamente' ($set): correcto

### unidad-4/teoria/mongodb-introduccion — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion.md` · temas: u4-mql-crud, u4-modelos-datos

**Conservar**

- BSON, terminologia, tipos (con Extended JSON), ObjectId de 12 bytes (4+5+3 correcto), 16 MiB, schema y validator $jsonSchema
- Aclaracion de mongod/mongosh/Compass y puerto 27017
- Advertencia de no publicar credenciales

**Faltante o superficial**

- Ejemplos de salida de 'show dbs' y estructura del validator con error de validacion detallado
- GridFS (solo mencionado)
- Nota de que mongosh trata numeros enteros como Int32/Double segun valor: relevante para validators bsonType int

**Solapamientos**

- unidad-4/teoria/apunte-completo: Duplicado en el apunte completo
- unidad-4/teoria/instalacion-mongodb: Seccion 'Shell mongosh' repite conexion local/Atlas

**Código a reconstruir o verificar**

- Validator: edad con bsonType 'int'; en mongosh un literal 30 se inserta como Int32 pero 30.0 o valores desde importaciones (CSV/JSON) quedan como Double y fallarian la validacion; mencionar NumberInt/$type o usar bsonType ['int','long','double'] con minimum/maximum
- Decimal128: NumberDecimal('1234.5678901234567890') tiene 20 cifras (<34 en limite): correcto; la tabla dice 'hasta 34 digitos de precision' correcto

**Afirmaciones dudosas**

- 'No se permiten claves duplicadas en un documento (MongoDB conserva el ultimo valor)': BSON no lo prohibe; es comportamiento del parser/driver
- 'Si un archivo excede ese limite se lo divide, se lo guarda fuera del documento o se evalua GridFS': correcto

### unidad-4/teoria/nosql-conceptos — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-4/teoria/nosql-conceptos.md` · temas: u4-base-acid, u4-tipos-nosql, u4-modelos-datos

**Conservar**

- Version mejor matizada del apunte: linea de tiempo corregida, CAP solo ante particion, diagrama mermaid, comparativa y 'metodo de eleccion'
- Cuatro modelos con caracteristicas, casos de uso y ejemplos Gremlin/CQL
- Nota sobre CP como simplificacion de la catedra y readPreference/readConcern/writeConcern

**Faltante o superficial**

- Comparacion de INSERT relacional vs documental/grafo/columnar (ed68 p.19, 21, 23)
- Modelos jerarquicos y de texto (programa 2024)
- Relacion con POO y desajuste de impedancia (solo el bullet 'puede evitar el desajuste')

**Solapamientos**

- unidad-4/teoria/apunte-completo: El apunte completo repite estos contenidos con menos matices

**Código a reconstruir o verificar**

- Ejemplo CQL 'SELECT time, value FROM events WHERE event_type...': copia del texto de catedra; requiere definicion de la tabla y clave de particion/clustering (sin DDL no es verificable; verificar en motor Cassandra)
- 'Soporta millones de columnas por tabla' para el modelo columnar: afirmacion sin matiz (Cassandra limita a 2 mil millones de celdas por particion)

**Sin fuente suficiente**

- 'Lecturas y escrituras O(1) con la clave' en clave-valor: aporte propio

**Afirmaciones dudosas**

- 'CP: MongoDB, HBase, Redis' y 'CA: RDBMS': simplificacion de la catedra (reconocida en la propia pagina)
- 'DynamoDB: AP': depende de configuracion de consistencia (lectura fuertemente consistente opcional)
- 'MongoDB: un unico nodo primario... durante la eleccion pueden interrumpirse escrituras': correcto

### unidad-5/practica — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-5/practica/index.md` · temas: —

**Conservar**

- Índice coherente con los tres laboratorios existentes.

**Faltante o superficial**

- No hay laboratorio de HA/réplicas ni de cifrado (programa 2024 semana 12: «Configuración de alta disponibilidad. Configuración de réplicas»).

### unidad-5/practica/laboratorio-backup — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/practica/laboratorio-backup.md` · temas: u5-backups, u5-recuperacion

**Conservar**

- Secuencia correcta: full → log → diferencial → logs → restore full + diferencial + logs con STOPAT. Es válido restaurar U5_log_02 tras el diferencial porque su rango de LSN cubre el LSN del diferencial.
- Preguntas conceptuales sobre qué contiene el diferencial y por qué no hace falta log_01.
- Nunca usa REPLACE sobre la base de origen.

**Faltante o superficial**

- Resultados esperados: filas finales en LaboratorioU5_Restore (A_FULL, B_LOG1, C_DIFF presentes; ERROR_LOGICO ausente), salida de HEADERONLY y de DBCC CHECKDB.
- Rutas de Windows (D:\SQLBackups, D:\SQLData): no válidas en SQL Server en Linux/contenedor; indicar alternativa.
- Prerrequisito: tablas ventas.Pedido y ventas.Cliente del laboratorio-seguridad (el INSERT usa ClienteId = 1 y columna Estado).

**Solapamientos**

- unidad-5/teoria/backup-restauracion: Comandos idénticos.

**Ejercicios y soluciones**

- Los estados se llaman A_FULL, B_LOG1, C_DIFF, pero A_FULL se inserta DESPUÉS del full (no está en el full, solo en log_01 y en el diferencial). El nombre induce a pensar que el full lo contiene. La respuesta correcta a la pregunta del paso 4 es «ambos: A_FULL y B_LOG1 (cambios desde el full)», lo cual vale aclarar.
- @momento_objetivo se declara y se pierde al terminar el lote (GO): el texto dice anotarlo a mano, pero conviene guardarlo en una tabla o variable de sqlcmd.
- STOPAT con datetime2 de SYSDATETIME(): usar hora del servidor; el placeholder REEMPLAZAR_POR_MOMENTO_ANTES_DEL_ERROR debe ser literal válido (p. ej. '2026-07-22T14:37:00.000').

**Código a reconstruir o verificar**

- WITH COMPRESSION no disponible en Express (verificar en motor).
- Nombres lógicos 'LaboratorioU5' y 'LaboratorioU5_log' son los que CREATE DATABASE genera por defecto: correctos salvo que cambien.
- RESTORE VERIFYONLY con CHECKSUM, FILELISTONLY, HEADERONLY: válidos. DBCC CHECKDB ... WITH NO_INFOMSGS: válido.

### unidad-5/practica/laboratorio-inyeccion — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion.md` · temas: —

**Conservar**

- Enfoque defensivo: base aislada, sin DDL ni borrados; el payload solo altera el filtro (OR 1=1--) y el lab pide observar el SQLGenerado.
- BuscarEstatico, BuscarSeguro y ListarSeguro con allowlist + QUOTENAME correctos sintácticamente.

**Faltante o superficial**

- Resultados esperados: BuscarVulnerable con la entrada normal devuelve 1 fila; con el payload devuelve las 3 filas; BuscarSeguro con el payload devuelve 0 filas.
- Prerrequisito: esquema seguridad no existe en el lab de seguridad; el script lo crea (falla si se re-ejecuta).

**Solapamientos**

- unidad-5/teoria/inyeccion-sql: Mismos procedimientos y cuestionario.

**Ejercicios y soluciones**

- ERROR en la Parte 5: app_demo (miembro de rol_consulta_usuario con DENY SELECT sobre seguridad.UsuarioDemo) ejecuta EXEC seguridad.BuscarSeguro. Ese procedimiento ejecuta el SELECT con sys.sp_executesql: el SQL dinámico rompe el ownership chain y se evalúa con los permisos del llamador, por lo que fallará con «permiso SELECT denegado». Solo BuscarEstatico (SQL estático) funciona con DENY. Esto contradice el texto («Esto demuestra que parametrización y POLP son capas complementarias»). Corregir: o probar solo BuscarEstatico, o conceder SELECT mínimo/firmar el módulo, y explicar la ruptura de la cadena (verificar en motor).
- Parte 1: ejecuta un procedimiento deliberadamente vulnerable. Es aceptable por ser un lab aislado con datos ficticios y payload no destructivo; mantener la advertencia.

**Código a reconstruir o verificar**

- Payload: N''' OR 1=1--' genera WHERE Nombre = '' OR 1=1--': correcto.
- UsuarioId int IDENTITY PRIMARY KEY, Nombre UNIQUE: válido.
- BuscarVulnerable devuelve dos conjuntos de resultados (SQLGenerado y la consulta): documentar.

**Estilo (guía de contenido)**

- Esquema seguridad y tabla seguridad.UsuarioDemo (teoría usa seguridad.Usuario): inconsistente entre páginas, sin impacto.

### unidad-5/practica/laboratorio-seguridad — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/practica/laboratorio-seguridad.md` · temas: u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles, u5-minimo-privilegio

**Conservar**

- T-SQL sintácticamente correcto en general; objetivos claros; uso de EXECUTE AS/REVERT y fn_my_permissions.
- Ownership chain por vista y procedimiento (Partes 3 y 4) funciona: mismo propietario dbo en esquemas ventas y operaciones.

**Faltante o superficial**

- Resultados esperados de cada prueba (qué devuelve SELECT, qué mensaje de error de permiso se obtiene).
- Script de limpieza/reinicio (DROP USER/LOGIN/ROLE/SCHEMA) y de idempotencia: CREATE SCHEMA/TABLE/LOGIN fallan al re-ejecutar.
- Mención del prerrequisito entre laboratorios: LaboratorioU5 es reutilizado por laboratorio-backup y laboratorio-inyeccion.

**Solapamientos**

- unidad-5/teoria/seguridad-permisos: Mismos objetos y consultas; el lab pide construir lo que la teoría ya entrega resuelto.

**Ejercicios y soluciones**

- Parte 5 deja un GRANT SELECT ON SCHEMA::ventas TO usr_auditor sin revertir. Al final (REVOKE del DENY) el auditor puede leer ventas.Cliente, lo que contradice el escenario y la prueba de la Parte 2 («SELECT * FROM ventas.Cliente debería fallar»). Falta REVOKE del permiso de esquema al terminar.
- Parte 1 pregunta 2 («¿Qué creó DEFAULT_SCHEMA?») es una pregunta trampa: la respuesta es que no crea nada ni otorga permisos (el esquema ya existe); conviene decirlo para no confundir.
- Parte 7: simular la delegación requiere un tercer usuario que no se crea en el laboratorio.
- Desafío 2 (vendedores no ven pedidos ajenos) requiere row-level security o vista con SUSER_SNAME: no está en cátedra ni en la teoría de la unidad.

**Código a reconstruir o verificar**

- Consultas con LIKE 'login_%_u5' y 'usr_%': el guion bajo es comodín de LIKE; funciona pero imprecisamente (usar ESCAPE o prefijo exacto).
- CREATE SCHEMA ... GO en lotes separados es correcto; CREATE TABLE sin GO intermedio con INSERT: ok.
- Contraseñas de ejemplo en el repositorio: marcadas como reemplazables; CHECK_POLICY = ON las exige complejas (cumplen).

**Estilo (guía de contenido)**

- Prefijos usr_/rol_/login_ y esquemas en minúscula: estilo.

### unidad-5/teoria — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/index.md` · temas: u5-minimo-privilegio, u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles, u5-alta-disponibilidad, u5-backups, u5-recuperacion, u5-cifrado

**Conservar**

- Resultados de aprendizaje alineados con cátedra p.3 («Al finalizar deberías ser capaz de…»).
- Tabla de índice completa y coherente con las páginas existentes.

**Faltante o superficial**

- Mención explícita de autenticación y directivas de contraseña en el resumen (sí figuran en el programa).

**Afirmaciones dudosas**

- Encabezado «Protección de los datos · 2do parcial»: esquema 2023 (parciales u1-u3 y u4-u6). Programa 2024 y cronograma 2025: un solo parcial u1-u4; la u5 se evalúa en TP y final.

### unidad-5/teoria/alta-disponibilidad — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad.md` · temas: u5-alta-disponibilidad

**Conservar**

- Distinción HA/DR/escala/backup; tabla síncrono vs asíncrono; condiciones del failover automático; log shipping y replicación fieles a cátedra p.53-58.
- DDL de AG idéntico en estructura al de cátedra p.52, con dominio de ejemplo example.test.

**Faltante o superficial**

- Indicar que el ejemplo de cátedra es BASIC AG (Standard, una base, dos réplicas, sin lectura secundaria).
- Database Mirroring deprecado reemplazado por Always On (cátedra p.50).

**Solapamientos**

- unidad-5/teoria/apunte-completo: §11-§14.

**Código a reconstruir o verificar**

- Réplicas escritas como N'SQLVM1' (cátedra: N'SQLVM1\MSSQLSERVER'): válido para instancia por defecto.

**Sin fuente suficiente**

- Sección FCI y tabla FCI vs AG: sin fuente de cátedra (solo WSFC en p.51). Contenido correcto según conocimiento general; requiere documentación de Microsoft.
- «Failover automático requiere ... quorum saludable»: correcto, pero no está en cátedra.

**Afirmaciones dudosas**

- Tabla comparativa: «Lectura secundaria: Posible» para AG sin acotar a edición Enterprise/Basic AG; y «Failover automático: Sí» para replicación «No como objetivo principal» está bien matizado.
- Ver nota sobre el timeout en u5-alta-disponibilidad (apunte-completo).

### unidad-5/teoria/apunte-completo — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/unidad-5.md` · temas: u5-minimo-privilegio, u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles, u5-alta-disponibilidad, u5-backups, u5-recuperacion, u5-cifrado

**Conservar**

- Fiel a la presentación de cátedra (secciones 1-15 siguen el orden de Unidad-5_1.pdf) y corrige sus errores de código.
- Síntesis para el parcial (§17) correcta.

**Faltante o superficial**

- Directivas de contraseña con el detalle de cátedra p.9 (ver u5-autenticacion).

**Solapamientos**

- unidad-5/teoria/seguridad-permisos: §2-§6 duplican login/user, roles, DCL, jerarquía, ownership chaining y vistas/procedimientos (mismo SQL en parte).
- unidad-5/teoria/log-recuperacion: §7-§8 (WAL, VLF, LSN, modelos de recuperación, mismo query de VLF).
- unidad-5/teoria/backup-restauracion: §9-§10 (tipos de backup, 3-2-1, RPO/RTO, secuencia de restore, opciones REPLACE/MOVE).
- unidad-5/teoria/alta-disponibilidad: §11-§14 (AG, FCI, replicación, log shipping, tabla de elección).
- unidad-5/teoria/cifrado: §15 (TDE, columnas, TLS).
- unidad-5/teoria/inyeccion-sql: §16 (patrón vulnerable/seguro, defensa en profundidad).
- unidad-5/teoria/guia-parcial: §17 síntesis repite las comparaciones obligatorias.

**Código a reconstruir o verificar**

- §11: la afirmación sobre el timeout de la secundaria síncrona contradice cátedra p.50 (ver u5-alta-disponibilidad).
- §6 vista ClientesPublicos incluye la columna NumeroCuenta en una vista llamada «Publicos» (dato financiero en una vista abierta): no es un error de sintaxis pero contradice el mensaje de POLP; viene del ejemplo de cátedra (verificar intención).

**Sin fuente suficiente**

- §16 inyección SQL: la cátedra solo la menciona (p.6) y recomienda lectura (p.62); el desarrollo es propio del portal.

**Afirmaciones dudosas**

- §4 «Las versiones recientes incorporan roles de servidor más granulares ##MS_*##»: SQL Server 2022; verificar versión.

**Estilo (guía de contenido)**

- Duplicación casi total con las 6 páginas temáticas: 25 KB que deberían ser índice/resumen o eliminarse. Es la página con mayor redundancia de la unidad.

### unidad-5/teoria/backup-restauracion — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/backup-restauracion.md` · temas: u5-backups, u5-recuperacion

**Conservar**

- Tipos de backup, diferencial acumulativo, tail-log con NORECOVERY, copy-only, secuencia de restore con MOVE/NORECOVERY/STOPAT/RECOVERY y tabla NORECOVERY/STANDBY/RECOVERY: correctos.
- Diseño desde RPO/RTO y checklist de restore.

**Faltante o superficial**

- Tail-log con NO_TRUNCATE cuando la base está dañada/offline (cátedra p.42 menciona «DB dañada u offline»).
- STOPATMARK con ejemplo (cátedra p.48).

**Solapamientos**

- unidad-5/teoria/apunte-completo: §9-§10.
- unidad-5/practica/laboratorio-backup: Mismos nombres lógicos y comandos; el lab es la aplicación.

**Código a reconstruir o verificar**

- COMPRESSION: no disponible en todas las ediciones (p. ej. Express) según versión; verificar en motor.
- Backup cifrado: SERVER CERTIFICATE = CertificadoBackup no se crea en la página; el certificado debe existir en master (verificar en motor/edición).
- Gantt Mermaid con milestones de duración 0d y barra de 4 días: legible pero poco convencional; verificar render.

**Sin fuente suficiente**

- Retención inmutable y ransomware: sin respaldo de cátedra (la cátedra solo dice 3-2-1 con una copia en la nube); correcto como buena práctica.

### unidad-5/teoria/cifrado — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/cifrado.md` · temas: u5-cifrado

**Conservar**

- Modelo de amenazas, jerarquía TDE, respaldo del certificado y advertencia sobre su custodia.
- Aclaraciones correctas: TDE no oculta datos a un usuario autorizado; WITH ENCRYPTION es ofuscación; TLS no protege el .bak; hash no es cifrado.

**Faltante o superficial**

- Sin ejemplo de configuración de TLS en el servidor (Configuration Manager/Force Encryption), solo la lista de requisitos.

**Solapamientos**

- unidad-5/teoria/apunte-completo: §15.

**Ejercicios y soluciones**

- Sin ejercicio ni laboratorio propio de cifrado (la unidad no tiene práctica de TDE/TLS).

**Código a reconstruir o verificar**

- Cifrado de columnas: @frase se declara en el primer bloque y se reutiliza en el SELECT del segundo bloque; ejecutado por separado falla con «variable no declarada». Declarar de nuevo o juntar los lotes.
- ventas.Tarjeta.Numero no está definida: si es nvarchar, DecryptByPassPhrase devuelve varbinary de nvarchar y CONVERT(varchar(30), ...) produce texto corrupto (deberían coincidir los tipos, p. ej. CONVERT(nvarchar(30), ...)). Verificar en motor.
- EncryptByPassPhrase(..., 1, CONVERT(varbinary(128), TarjetaId)): sintaxis correcta (add_authenticator = 1).
- BACKUP ... WITH ENCRYPTION usa CertificadoBackup que no se crea; disponibilidad según edición (verificar).
- TDE: disponible en Standard desde SQL Server 2019 (antes solo Enterprise); la página dice «edición/versión compatible» sin precisar.

**Sin fuente suficiente**

- Always Encrypted, HSM/Key Vault y rotación de claves: sin fuente de cátedra.

**Afirmaciones dudosas**

- «Encrypt=true;TrustServerCertificate=false expresa la intención correcta en drivers modernos»: correcto, pero depende del driver (ODBC 18 / Microsoft.Data.SqlClient lo usan por defecto): verificar.

**Estilo (guía de contenido)**

- Nombres de columna NumeroCifrado/Numero fine; variable @frase en minúscula: estilo.

### unidad-5/teoria/guia-parcial — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/guia-parcial.md` · temas: u5-minimo-privilegio, u5-permisos-dcl, u5-backups, u5-recuperacion, u5-alta-disponibilidad, u5-cifrado

**Conservar**

- Comparaciones obligatorias y errores frecuentes alineados con lo que piden los finales (GRANT/DENY/REVOKE, restore order, POLP).
- Método de respuesta de 5 pasos.

**Faltante o superficial**

- Simulacro de 10 puntos sin pauta ni resolución (la guía de u6 sí trae pauta).
- Ejercicio de ordenar 7 pasos de recuperación con un paso incorrecto (formato de 8d75a3b284ab ítem 8).
- Ejercicio SI/NO sobre permisos con GRANT a rol y REVOKE a usuario (formato de d8baa3d1630e ítem 1).

**Solapamientos**

- unidad-5/teoria/apunte-completo: §17 síntesis; las comparaciones se repiten.

**Ejercicios y soluciones**

- Título y marco «parcial»: en 2024/2025 u5 no entra en el parcial (u1-u4); se evalúa en TP/final. Revisar el rótulo.
- Error frecuente «llamar incremental al diferencial»: la cátedra (p.37) usa «Diferencial o incremental»; matizar.

**Afirmaciones dudosas**

- Mapa mental incluye «Código seguro / SQL injection» como parte central de la unidad: no está en el programa.

### unidad-5/teoria/inyeccion-sql — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql.md` · temas: —

**Conservar**

- Desarrollo defensivo correcto: parametrización con sp_executesql, allowlist + QUOTENAME para identificadores, POLP, segundo orden, hashing de contraseñas.
- El ejemplo vulnerable está marcado como incorrecto y no incluye payloads destructivos.

**Faltante o superficial**

- Mención a que sp_executesql con SQL dinámico rompe el ownership chain (relación con u5-permisos-dcl).

**Solapamientos**

- unidad-5/teoria/apunte-completo: §16.
- unidad-5/practica/laboratorio-inyeccion: Mismos ejemplos (BuscarVulnerable/BuscarSeguro, ORDER BY con allowlist).

**Código a reconstruir o verificar**

- Bloque de allowlist: IF @columna NOT IN (...) THROW ... seguido de DECLARE @sql: válido; @columna debe estar declarada (no se muestra el procedimiento envolvente).
- EXEC (@sql) y sp_executesql: correctos.

**Sin fuente suficiente**

- Tema sin respaldo propio en cátedra: solo p.6 («buenas prácticas de programación, p/e prevenir inyección SQL») y p.62 (lectura recomendada de Microsoft Learn). En u1 la cátedra advierte el riesgo de SQL injection en SQL dinámico (9d5ab3349985 p.48; apunte 3a0d8f223fcf p.15; 3c6cac1c3ff5 p.20). Ningún final lo evaluó.

**Afirmaciones dudosas**

- Lista de algoritmos de hashing (Argon2id, bcrypt, scrypt, PBKDF2): recomendación vigente, no es contenido de cátedra.

**Estilo (guía de contenido)**

- Tabla de «Respuesta esperada de parcial» presenta un texto de examen que no está en las fuentes.

### unidad-5/teoria/log-recuperacion — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/log-recuperacion.md` · temas: u5-recuperacion

**Conservar**

- Explicación correcta de WAL, checkpoint, truncado vs shrink, log_reuse_wait_desc, BULK_LOGGED y cambio de modelo.
- Consultas válidas: sys.dm_db_log_space_usage, sys.dm_db_log_info (SQL Server 2016 SP2+), DBCC SQLPERF, DBCC OPENTRAN.
- Mitos de parcial útiles.

**Faltante o superficial**

- Ejemplo con resultado esperado de log_reuse_wait_desc (LOG_BACKUP) tras un FULL sin backup de log.

**Solapamientos**

- unidad-5/teoria/apunte-completo: §7-§8.

**Código a reconstruir o verificar**

- sys.dm_db_log_info solo existe desde SQL Server 2016 SP2; no se indica la versión.

**Sin fuente suficiente**

- Estados del diagrama de VLF (Reutilizable/Activo/Inactivo) simplifican los estados reales (unused/active/recoverable/reusable): aceptable como esquema didáctico.

### unidad-5/teoria/seguridad-permisos — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos.md` · temas: u5-minimo-privilegio, u5-autenticacion, u5-permisos-dcl, u5-propietarios-roles

**Conservar**

- Matriz de autorización antes de los comandos.
- Consulta de permisos con LEFT lógica por clase (DATABASE/SCHEMA/OBJECT_OR_COLUMN) correcta: SCHEMA_NAME(major_id) para clase SCHEMA y OBJECT_SCHEMA_NAME/OBJECT_NAME para objetos.
- Aclaración correcta de que REVOKE directo no elimina lo heredado de roles y de que EXECUTE AS requiere REVERT.
- Ownership chaining y su ruptura con SQL dinámico.

**Faltante o superficial**

- Modos de autenticación (Windows vs SQL; modo mixto) y detalle de directivas (CHECK_POLICY: largo/complejidad/3 de 4; MUST_CHANGE).

**Solapamientos**

- unidad-5/teoria/apunte-completo: §2-§6 del apunte completo.
- unidad-5/practica/laboratorio-seguridad: Mismo escenario (vendedores, auditores) y consultas de auditoría; se espera como solución del lab.

**Ejercicios y soluciones**

- «Preguntas para razonar» sin respuestas ni pistas.

**Código a reconstruir o verificar**

- CREATE LOGIN ... DEFAULT_DATABASE = Ventas requiere que Ventas exista (no definido en la página).
- CREATE LOGIN [EMPRESA\Vendedores] FROM WINDOWS seguido de USE Ventas en el mismo lote sin GO: válido, pero CREATE USER debería ir en un lote propio por claridad (verificar en motor).
- CREATE OR ALTER VIEW requiere SQL Server 2016 SP1 o posterior (no se indica).
- GRANT ... WITH GRANT OPTION TO supervisor y REVOKE ... FROM supervisor CASCADE: el principal «supervisor» no está definido en la página (es un nombre genérico).

**Afirmaciones dudosas**

- La frase «La consulta del material que hace INNER JOIN sys.objects omite permisos de base y esquema; la versión anterior...» es metacomentario sobre el material de origen: confusa para un lector y sin referencia verificable.

**Estilo (guía de contenido)**

- Prefijos snake_case (login_vendedor, rol_vendedores, usr_vendedor, vw_ClienteVisible, @p_nombre) en vez de PascalCase de la guía de contenido: registrar como estilo, no como error. Esquemas ventas/operaciones en minúscula: estilo.

### unidad-6/practica — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-6/practica/index.md` · temas: —

**Conservar**

- Índice coherente con los tres recursos de práctica.

### unidad-6/practica/casos-integradores — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-6/practica/casos-integradores.md` · temas: u6-iso-25012, u6-ley-25326, u6-gdpr

**Conservar**

- Plantilla de 7 pasos y cinco casos con «resolución orientativa» concisa que vincula norma, característica ISO, métrica y controles.
- Caso 5 (backup restaurado) integra u5 y u6 de forma pertinente.

**Faltante o superficial**

- Resultados no contrastables con fuentes: ningún caso se apoya en un examen real del corpus.

**Solapamientos**

- unidad-6/teoria/guia-parcial: Casos 1-4 de la guía y simulacro.

**Ejercicios y soluciones**

- Caso 4 (migración a un lago) mezcla u4 (data lakes) con u6; no es error, pero el enunciado asume conocimientos de otra unidad.

**Sin fuente suficiente**

- Afirmaciones jurídicas (cesión, impugnación, decisiones automatizadas) sin respaldo en el corpus: requiere fuente primaria.

**Afirmaciones dudosas**

- Caso 3: «pulso es salud»: criterio razonable; matizar que depende del contexto (verificar con normativa).

### unidad-6/practica/laboratorio-calidad — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-6/practica/laboratorio-calidad.md` · temas: u6-iso-25012

**Conservar**

- T-SQL ejecutable: el INSERT tiene 9 valores por fila para las 9 columnas de calidad.Cliente; literales de fecha 'AAAA-MM-DD' válidos para date/datetime2 en cualquier idioma.
- Datos con defectos deliberados cuyos resultados son coherentes con las consultas: DNI repetido 30111222 (clientes 1 y 2); PaisCodigo inválido en clientes 3 ('AR ') y 5 ('XXX'); fecha 31/02/1995 no convertible; pedido 103 con cliente inexistente; pedido 101 con entrega anterior al pedido y total declarado 150 vs calculado 140; actualidad: 3 de 4 activos dentro de 365 días (75,00 %).
- Los ALTER TABLE ... WITH CHECK fallan a propósito (FK por pedido 103; CHECK por pedido 101), como se explica.

**Faltante o superficial**

- Resultados esperados escritos (los de arriba pueden agregarse).
- Script re-ejecutable (CREATE SCHEMA/TABLE fallan al repetir).

**Solapamientos**

- unidad-6/teoria/medicion-calidad: Perfilado y porcentajes idénticos.

**Ejercicios y soluciones**

- Parte 1 consulta de PaisCodigo: usa NOT IN y por tanto no detecta NULL (no hay NULL en los datos); si se agregan, no se detectarían. Mencionarlo.
- Parte 4: tabla de remediación sin ejemplo resuelto.

**Código a reconstruir o verificar**

- Parte 2 JOIN a ItemPedido omite pedidos sin ítems (INNER JOIN); aceptable aquí, pero un pedido sin renglones no se detectaría.
- Dependencia de SYSDATETIME(): resultados de actualidad cambian con el tiempo (los clientes 2 y 5 se calculan con DATEADD relativo: estable).

**Estilo (guía de contenido)**

- Aliases snake_case; INSERT sin lista de columnas (frágil): estilo.

### unidad-6/practica/laboratorio-privacidad — **ampliar**

`src/content/docs/bbdd-aplicadas/unidad-6/practica/laboratorio-privacidad.md` · temas: u6-ley-25326, u6-gdpr

**Conservar**

- Escenario realista y ficticio (SaludEnCasa); no pide datos reales; incluye relación con ISO 25012.
- Preguntas sobre artículo 3 del GDPR y encargado vs responsable.

**Faltante o superficial**

- No contiene T-SQL (es ejercicio de diseño): falta una parte práctica en SQL Server (p. ej. enmascaramiento dinámico, roles que impidan leer diagnóstico a recepción, seudonimización) que conecte con la unidad 5.
- No trae pauta ni solución.
- Plazos pedidos (Ley 25.326 y GDPR) no figuran en el corpus.

**Solapamientos**

- unidad-6/practica/casos-integradores: Escenarios similares (salud, proveedor, retención, backups).
- unidad-6/teoria/gobierno-privacidad: Inventario, retención.

**Ejercicios y soluciones**

- Parte 4: «Indicá los plazos de Ley 25.326 y el plazo general GDPR»: requiere fuente primaria; sin solución no puede validarse.
- Diagrama ER: la entidad TRATAMIENTO/EVIDENCIA_BASE queda desconectada del resto del modelo.

**Sin fuente suficiente**

- Todo el laboratorio depende de normativa fuera del corpus.

### unidad-6/teoria — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/index.md` · temas: u6-ley-25326, u6-gdpr, u6-iso-25012

**Conservar**

- Resultados de aprendizaje coherentes con el programa 2024 (Ley, GDPR, ISO/IEC 25012).

**Unidad incorrecta**

- «medición y gobierno de datos» en el resumen: contenidos extra (no figuran en el programa).

**Afirmaciones dudosas**

- Encabezado «Calidad en bases de datos · 2do parcial»: esquema 2023. En 2024/2025 u6 no se evalúa en parcial (parcial = u1-u4); entra en el TP (entrega de la semana 13 en el programa) y en el final. Además el cronograma 2025 (6538cbd089bd p.17) no asigna clases a u6.

### unidad-6/teoria/apunte-completo — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/unidad-6.md` · temas: u6-ley-25326, u6-gdpr, u6-iso-25012

**Conservar**

- Estructura clara; las 15 características y su clasificación coinciden con los apuntes de alumno.
- Distinción seudonimización/anonimización, calidad ≠ privacidad ≠ seguridad.

**Faltante o superficial**

- Exclusiones del GDPR que figuran en las fuentes de alumno (fallecidos, personas jurídicas, uso personal/doméstico).

**Solapamientos**

- unidad-6/teoria/ley-25326: §2 duplica la Ley 25.326.
- unidad-6/teoria/gdpr: §3 duplica GDPR.
- unidad-6/teoria/iso-25012: §4 duplica ISO 25012.
- unidad-6/teoria/medicion-calidad: §5 duplica métricas y controles.
- unidad-6/teoria/gobierno-privacidad: §6-§7 duplican gobierno y ciclo de vida.
- unidad-6/teoria/guia-parcial: §8 método de casos duplica la guía.

**Sin fuente suficiente**

- La frase atribuida a Henry Ford «que abre el material»: el corpus (7034e8ba7365) solo dice «Calidad → hacer las cosas bien, incluso cuando nadie te está mirando» sin atribuir a Ford; la atribución es popular y dudosa. Sin fuente.
- Ley 25.326 «sancionada el 4 de octubre de 2000», AAIP/DNPDP, Resolución 47/2018: requiere fuente primaria (verificar contra el texto oficial).
- GDPR: fechas (25/05/2018), art. 3, 72 h, 10M/2 % y 20M/4 %: requiere fuente primaria; correctas según mi conocimiento.
- §6 Gobierno de datos y §5 métricas: sin ninguna fuente de cátedra ni de alumnos (ver extra_topics).

**Afirmaciones dudosas**

- §2.1 dato personal «referida a una persona humana o jurídica»: la ley define persona de existencia ideal en el art. 2 (verificar).

**Estilo (guía de contenido)**

- Duplicación masiva con las páginas temáticas (24 KB).

### unidad-6/teoria/gdpr — **investigar**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/gdpr.md` · temas: u6-gdpr

**Conservar**

- Test de aplicabilidad del art. 3 y aclaración de que ciudadanía/accesibilidad no bastan.
- Principios, bases, derechos, brechas y transferencias consistentes con el Reglamento según mi conocimiento.

**Faltante o superficial**

- Exclusiones de aplicación presentes en las fuentes de alumno (fallecidos, personas jurídicas, actividad personal/doméstica).
- Cláusulas/condiciones de transferencia en el lenguaje simple de las fuentes (adecuación, cláusulas específicas, consentimiento): el portal lo cubre con art. 46/49 pero no lo alinea con los apuntes.

**Solapamientos**

- unidad-6/teoria/apunte-completo: §3.

**Código a reconstruir o verificar**

- Mermaid de brechas: el nodo E está definido dos veces con etiquetas distintas («Documentar fundamento» y «Remediar y conservar evidencia»); la última etiqueta pisa a la primera y el diagrama pierde la rama «no hay riesgo → documentar fundamento». Corregir con dos IDs distintos.

**Sin fuente suficiente**

- Cifras: 72 h, un mes + dos, €10M/2 %, €20M/4 %, arts. 3, 5, 6, 9, 25, 32, 33, 37, 46, 49: requiere fuente primaria; verificar contra el texto oficial (EUR-Lex, enlace del portal).
- Tabla comparativa Ley 25.326 vs GDPR («Multas máximas: régimen local y reglamentación»): vaga y sin respaldo.

**Afirmaciones dudosas**

- Fórmula de alcance distinta a la de cátedra/alumnos («cualquier empresa que procese información personal dentro del EEE»): la del portal es más precisa; documentar la diferencia para quien rinda con el criterio de cátedra.

### unidad-6/teoria/gobierno-privacidad — **reorganizar**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/gobierno-privacidad.md` · temas: —

**Conservar**

- Contenido conceptualmente sensato (roles, RACI, inventario, linaje, retención).

**Unidad incorrecta**

- Gobierno de datos y privacidad desde el diseño no están en el programa 2024 de u6 (solo Ley, GDPR, ISO 25012).

**Solapamientos**

- unidad-6/teoria/apunte-completo: §6-§7 y ciclo de vida.
- unidad-6/practica/laboratorio-privacidad: Inventario, retención y derechos.

**Sin fuente suficiente**

- Sin ninguna fuente del corpus: RACI, niveles de clasificación, catálogo/linaje, tabla de retención. Sin referencias bibliográficas (p. ej. DAMA-DMBOK) ni normativas.

**Afirmaciones dudosas**

- Retención en backups inmutables («re-aplicar supresiones si se restaura»): práctica aceptada, no norma; presentarlo como buena práctica y no como obligación legal.

### unidad-6/teoria/guia-parcial — **corregir**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/guia-parcial.md` · temas: u6-ley-25326, u6-gdpr, u6-iso-25012

**Conservar**

- Lista 5+7+3, tabla de artículos y comparaciones correctos y consistentes con las fuentes de alumno.
- Pauta de corrección del simulacro.

**Faltante o superficial**

- Ejercicio tipo examen de clasificar datos como personal / sensible / ninguno (final 8d75a3b284ab ítem 3).
- Verdadero/falso sobre Ley 25.326 y calidad (final cf1a40d118d4 ítem 7).

**Solapamientos**

- unidad-6/teoria/apunte-completo: §8 método de casos.
- unidad-6/practica/casos-integradores: Casos cortos resueltos y simulacro.

**Ejercicios y soluciones**

- Marco de «parcial»: u6 no se evalúa en parcial en 2024/2025 (ver nota transversal).
- Simulacro: la métrica de la pauta (resultados con versión de algoritmo / emitidos) es razonable; el umbral del 100 % se deja a criterio.

**Sin fuente suficiente**

- Artículos y plazos de la tabla (14: 10 días corridos; 16: 5 días hábiles; 21 inscripción; 33 hábeas data): requiere fuente primaria; arts. 4, 5, 6, 7, 9, 31, 32 respaldados por alumnos.
- «citar a la DNPDP como autoridad autónoma actual sin mencionar AAIP» como error: dato no respaldado en el corpus.

**Afirmaciones dudosas**

- La respuesta modelo «GDPR alcanza a cualquier empresa...? No con esa formulación» difiere de lo que las fuentes de alumno afirman.

### unidad-6/teoria/iso-25012 — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/iso-25012.md` · temas: u6-iso-25012

**Conservar**

- Clasificación 5 + 7 + 3 = 15 respaldada por tres documentos de alumno y consistente con la norma según mi conocimiento.
- Distinciones útiles: exactitud vs precisión, accesibilidad vs permiso universal, backup vs recuperabilidad, unicidad no es de las 15.
- Matriz de diagnóstico síntoma → característica.

**Solapamientos**

- unidad-6/teoria/apunte-completo: §4 (tablas y diagrama de las 15 características).
- unidad-6/teoria/guia-parcial: Lista 5+7+3 repetida.

**Sin fuente suficiente**

- Definiciones y ejemplos de cada característica: no están en el corpus más allá de las definiciones de alumno; requiere fuente primaria (ISO/IEC 25012:2008). Credibilidad «aumenta con firma, certificación...»: interpretación propia.

**Afirmaciones dudosas**

- «Exactitud sintáctica/semántica» y «accesibilidad con tecnología de apoyo»: provienen de la norma, pero no del corpus: verificar contra el texto oficial.

### unidad-6/teoria/ley-25326 — **investigar**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/ley-25326.md` · temas: u6-ley-25326

**Conservar**

- Arts. 4, 5, 6, 7, 9, 31 y 32 coinciden con las fuentes de alumno (7034e8ba7365) en lo esencial; correcta la lista de excepciones del art. 5 (alumnos citan fuentes públicas, función estatal/obligación legal, listados limitados a nombre/DNI/ocupación/fecha de nacimiento/domicilio).
- Aclaración de que no toda falla de calidad es delito.

**Faltante o superficial**

- La multa del art. 31 (1000 a 100 mil pesos en el texto original, según 7034e8ba7365): el portal no cita cifra; verificar montos vigentes antes de agregarla.
- Art. 8 (datos de salud) y art. 11 (cesión) solo de pasada.

**Solapamientos**

- unidad-6/teoria/apunte-completo: §2.
- unidad-6/teoria/gdpr: Tabla comparativa final repite lo ya dicho en cada página.

**Ejercicios y soluciones**

- Preguntas de autoevaluación sin respuesta; el caso resuelto sí tiene pauta.

**Sin fuente suficiente**

- Derechos arts. 13-20 y plazos (10 días corridos acceso, 5 días hábiles rectificación/supresión/actualización, acceso gratuito semestral): requiere fuente primaria; coinciden con mi conocimiento de los arts. 14 y 16 (verificar contra el texto oficial).
- Mapa de estudio por rangos de artículos (1-2, 3-12, 13-20, 21-28, 29-30, 31-32, 33-43): requiere fuente primaria; coincide con mi conocimiento de la estructura de la ley.
- Resolución AAIP 47/2018 como medidas de seguridad recomendadas y trámite ante la AAIP: requiere fuente primaria (verificar vigencia; la normativa de protección de datos argentina está en proceso de actualización).
- Cesión y transferencia internacional (arts. 11 y 12): sin respaldo en el corpus.

**Afirmaciones dudosas**

- «Varias disposiciones también alcanzan, cuando corresponde, datos de personas jurídicas»: verificar contra el texto oficial.
- Enlaces externos (argentina.gob.ar/normativa/nacional/64790) no verificables sin red.

### unidad-6/teoria/medicion-calidad — **conservar**

`src/content/docs/bbdd-aplicadas/unidad-6/teoria/medicion-calidad.md` · temas: —

**Conservar**

- SQL correcto: COUNT_BIG, NULLIF contra división por cero, 100.0 para evitar división entera, TRY_CONVERT(date, ..., 23), índice único filtrado, CHECK constraint.
- Distinción preventivo/detectivo/correctivo y advertencia sobre NOCHECK.

**Faltante o superficial**

- Resultados esperados de las consultas (no hay datos de ejemplo en la página; el lab de calidad los provee).

**Solapamientos**

- unidad-6/teoria/apunte-completo: §5 «De la característica a una métrica».
- unidad-6/practica/laboratorio-calidad: Mismas consultas de perfilado.

**Código a reconstruir o verificar**

- CK_Cliente_Pais admite ('ARG','BRA','URY') mientras el laboratorio usa ('ARG','URY','BRA'): equivalente. Con los datos del laboratorio, ambos comandos (CHECK y UNIQUE INDEX sobre DNI) fallarían (hay PaisCodigo 'AR ' y 'XXX', y DNI repetido), como advierte el texto.
- COUNT(DISTINCT PaisCodigo) en perfilado: correcto.

**Sin fuente suficiente**

- Todo el tema (perfilado, métricas, umbrales, indicadores de proceso, 10 pasos de evaluación): sin fuente de cátedra ni de alumnos. Contenido de conocimiento general.

**Estilo (guía de contenido)**

- Alias en snake_case (email_faltante, completitud_email_pct) frente a PascalCase de la guía de contenido: estilo.

## 10. Temas del portal fuera del programa 2024 o fuera de su unidad

| Tema | Páginas | Respaldo | Recomendación |
|---|---|---|---|
| Índice clustered (inserción, page splits, WAL/REDO/UNDO) | unidad-1/teoria/indice-cluster | sin-fuente | Mover a u3 (u3-indices) y fusionar con indices-y-planes / indices-optimizacion, que ya cubren clustered, fill factor y page splits; la parte de log y recuperación puede ir a u3-tcl o u5-recuperacion. No hay respaldo en cátedra de u1 (9d5ab3349985 no trata índices; el material de page split está en la cátedra de u3, 0d2ad822befa). |
| SQL dinámico | unidad-1/teoria/sql-dinamico | catedra:bbdd-aplicadas-9d5ab3349985 p.48-49 | Conservar en u1 (tiene respaldo de cátedra y aparece en el parcial f12df9e4e498); corregir el GO en el PIVOT dinámico y sumar el ejemplo de la cátedra (conteo de filas por tabla). |
| ACID desarrollado, aislamiento, MVCC, SNAPSHOT, WAL | unidad-2/teoria/bd-transaccionales | catedra:bbdd-aplicadas-d0b0a9b78ca8 p.2-8 (solo OLTP/ACID descriptivo y commit/rollback) | Mantener en u2 solo OLTP, ACID a nivel conceptual y commit/rollback; trasladar aislamiento, MVCC y WAL a u3 (u3-concurrencia) y la comparación ACID vs BASE a u4 (u4-base-acid). |
| Práctica de transacciones (BEGIN/COMMIT/SAVE/XACT_ABORT/aislamiento) | unidad-2/practica/practica-transacciones | sin-fuente | Reubicar en u3 (u3-tcl); corregir el ej. 3 (CHECK antes del IF) y agregar el paso ROLLBACK del ej. 1. PracticaU2 se usa en otras prácticas de u2: mover el setup a una página común. |
| Data Warehouse, Data Lake, ETL/ELT | unidad-2/teoria/bd-transaccionales | catedra:bbdd-aplicadas-d0b0a9b78ca8 p.11-15 | Tema del programa 2024 en u4 (data lakes) y contenidos mínimos (DWH); respaldado por la cátedra pero en el PDF de u2. Dejar visible el respaldo, evaluar reubicar a una página propia. |
| Always On y alta disponibilidad | unidad-2/teoria/bd-transaccionales | catedra:bbdd-aplicadas-5db2ce42f603 (u5) | Pertenece a u5-alta-disponibilidad; en u2 dejar solo clúster como arquitectura distribuida (p.9-10). |
| Tablas temporales y variables de tabla | unidad-2/teoria/bd-en-memoria<br>unidad-2/practica/tp2 | catedra:bbdd-aplicadas-d0b0a9b78ca8 p.27-28; bbdd-aplicadas-242399d569be p.3 (tabla temporal global) | Conservar; separar en una sección propia (programabilidad) y aclarar que son distintas de las tablas en memoria. |
| In-Memory OLTP (Hekaton), hash/range index, NATIVE_COMPILATION, NVRAM, snapshots | unidad-2/teoria/bd-en-memoria<br>unidad-2/practica/practica-bd-en-memoria | sin-fuente (la cátedra p.24-28 solo presenta el concepto y remite a una guía no incluida) | Conservar como ampliación opcional si el equipo posee la guía externa; actualizar las restricciones (FK, ALTER TABLE, NULL, computed columns) por versión de SQL Server. |
| Importación de XML y JSON con T-SQL (OPENJSON, FOR XML, OPENXML, nodes()) | unidad-2/teoria/json-en-sql<br>unidad-2/teoria/xml-en-sql<br>unidad-2/practica/practica-json<br>unidad-2/practica/practica-xml | sin-fuente (solo apunte de alumno cd36d917c66c p.10 menciona OPENJSON/BULK INSERT); el programa 2024 pide 'importación desde múltiples formatos' | Mantener (soporta u2-importacion), marcar como material complementario y buscar la guía de cátedra de origen. |
| Llamadas HTTP desde T-SQL con Ole Automation | unidad-2/teoria/apis-desde-sql<br>unidad-2/practica/practica-apis | sin-fuente (cátedra p.23-26 solo presenta APIs y Postman) | Mantener solo como ejercicio ilustrativo con las salvedades de seguridad; no está en el programa 2024 más que como 'qué es una API' (2023 no la listaba). |
| Formatos de intercambio en u2 (2024) vs u1 (2023) | unidad-2/teoria/formatos-de-intercambio<br>unidad-2/teoria/formatos-conectividad | catedra:bbdd-aplicadas-008193c9c082 p.4-22 | Correcto en u2 (esquema 2024). Unificar las dos páginas duplicadas. |
| Variantes de MongoDB: transacciones multidocumento, readConcern/writeConcern, replica sets | unidad-4/teoria/nosql-conceptos<br>unidad-4/teoria/index | sin-fuente | Aporte valioso y correcto, pero no esta en el programa 2024; mantener como nota marcada 'ampliacion' con referencia a la documentacion oficial (requiere fuente primaria) |
| Gobierno de data lake (catalogo, lineage, zonas, data swamp) y DW vs DL con schema on read/write | unidad-4/teoria/datos-data-lake-kdd | catedra:bbdd-aplicadas-3d9721081e14 p.3 (solo el titulo del tema); contenido de alumnos bbdd-aplicadas-3c6cac1c3ff5 p.22-23 | Conservar como resumen; rotular como sintesis propia y citar apuntes de alumno |
| KDD en 7 etapas y tareas de data mining | unidad-4/teoria/datos-data-lake-kdd<br>unidad-4/teoria/apunte-completo | catedra:bbdd-aplicadas-3d9721081e14 p.3 (solo titulo en la unidad 4 del programa); programa-2023 (contenidos minimos) | Verificar con la catedra si se evalua; si se conserva, sustentar con Fayyad et al. 1996 (requiere fuente primaria) y alinear numero de etapas |
| Operadores $expr, $text, $where, $mod, collation y Extended JSON | unidad-4/teoria/mongodb-crud<br>unidad-4/teoria/mongodb-compass<br>unidad-4/teoria/mongodb-introduccion | catedra:bbdd-aplicadas-4bd543391072 p.26, 49-51 (enumeran $text/$where, collation en Compass) | Conservar; son extensiones correctas con respaldo parcial |
| Etapas $graphLookup, $redact, $setWindowFields, $merge | unidad-4/teoria/mongodb-agregacion | sin-fuente (Compass las lista en 9a0d p.6) | Mantener como mencion; o quitar si no se desarrollan |
| XACT_ABORT, THROW/RAISERROR, ERROR_* y patron de SP con TRY/CATCH | unidad-3/teoria/transacciones-y-concurrencia | sin-fuente (la catedra 17c2 no trata TRY/CATCH ni XACT_ABORT) | Conservar como ampliacion de u3-tcl; marcar como 'no figura en las diapositivas de catedra' |
| Deadlocks, system_health, DMVs y bloqueos U/Intent | unidad-3/teoria/transacciones-y-concurrencia<br>unidad-3/teoria/transacciones-concurrencia | sin-fuente (catedra solo trata bloqueos S/X y 'bloqueos/esperas' como metrica, 17c2 p.15, 41) | Conservar; el programa 2024 pide 'bloqueos y esperas', pero no hay material de catedra en el corpus que desarrolle deadlocks |
| Modelo de recuperacion Simple/Full dentro de u3 | unidad-3/teoria/indices-optimizacion<br>unidad-3/teoria/metricas-de-rendimiento | catedra:bbdd-aplicadas-17c2c97f736b p.36-39 | Tiene respaldo en u3 (metricas) y se amplia en u5; eliminar la copia de indices-optimizacion y agregar BULK-LOGGED |
| Laboratorio tienda_online y bonus de API externa (Open Library) | unidad-4/practica/laboratorio-tienda-online | sin-fuente | No reproducible por falta de scripts; reemplazar por ejercicios con datos publicados en public/ o incluir los scripts |
| Integrador Peliculas y Prestamos (videoclub) | unidad-4/practica/integrador-peliculas | sin-fuente (datasets ausentes del repo y del corpus) | Publicar los JSON o reescribir con datos propios completos (DDL equivalente + documentos + resultado esperado) |
| Inyección SQL y programación segura | unidad-5/teoria/inyeccion-sql<br>unidad-5/practica/laboratorio-inyeccion | catedra:bbdd-aplicadas-5db2ce42f603 p.6 (medida de protección «prevenir inyección SQL») y p.62 (lectura recomendada); riesgo en SQL dinámico: bbdd-aplicadas-9d5ab3349985 p.48 y 3c6cac1c3ff5 p.20 | No figura como tema en el programa 2024 pero sí se menciona en la presentación de u5 y en u1 (SQL dinámico). Conservar como material complementario (marcar «ampliación») y corregir el error de la Parte 5 del laboratorio. No fue evaluado en los 3 finales del corpus. |
| Medición y mejora de la calidad (perfilado, métricas, umbrales) | unidad-6/teoria/medicion-calidad<br>unidad-6/practica/laboratorio-calidad | sin-fuente (el programa dice «Modelo de Calidad de datos (ISO/IEC 25012)»; en cátedra no hay presentación de u6) | Extra: no está en el programa ni en el corpus. Mantener como complemento práctico señalado como tal; el SQL es correcto. |
| Gobierno de datos, privacidad desde el diseño, retención | unidad-6/teoria/gobierno-privacidad<br>unidad-6/practica/laboratorio-privacidad | sin-fuente | Extra: no figura en el programa 2024 ni en el 2023. Marcar como material complementario o eliminar del resumen de u6; no debe presentarse como contenido evaluable. |
| Failover Cluster Instance (FCI) y comparación AG vs FCI | unidad-5/teoria/alta-disponibilidad<br>unidad-5/teoria/apunte-completo | catedra:bbdd-aplicadas-5db2ce42f603 p.51 (solo WSFC, sin FCI) | Ampliación razonable, pero sin respaldo de cátedra; contrastar con documentación de Microsoft y marcarla como complemento. |
| Alta disponibilidad y réplicas: contenidos de u5 sin laboratorio | unidad-5/practica | programa 2024 semana 12 («Configuración de alta disponibilidad. Configuración de réplicas») | Brecha de práctica: el programa prevé configuración de HA y réplicas; la práctica de u5 solo tiene seguridad, backup e inyección. |
| Cifrado de columnas con Always Encrypted, HSM/Key Vault y rotación de claves | unidad-5/teoria/cifrado | sin-fuente (cátedra p.59-61 solo TDE, EncryptByPassPhrase y TLS) | Mencionar como lectura complementaria. |
| Esquema de evaluación «2do parcial» para u5 y u6 | unidad-5/teoria<br>unidad-6/teoria | programa-2023 (dos parciales: u1-u3 y u4-u6) | Reemplazar por el esquema vigente: un parcial u1-u4, TP integrador y final con todas las unidades; u5 y u6 se evalúan en TP/final. |
