---
title: Cómo estudiar esta materia
description: Recorrido de las seis unidades, método de estudio, herramientas para las prácticas de SQL Server y MongoDB, evaluación y dos formas de usar los apuntes.
slug: bbdd-aplicadas/como-estudiar
---

Esta página explica cómo está organizada la materia y propone una forma de recorrerla, tanto si la
estudiás por primera vez como si la estás repasando para un examen. No agrega contenido: indica qué
leer, cuándo practicar y dónde comprobar lo aprendido.

## Cómo está organizada la materia

Los apuntes siguen el programa analítico 2024 de la asignatura (3641), en seis unidades que conviene
recorrer en orden, porque cada una usa lo anterior:

| Unidad | Qué estudia |
|---|---|
| [1 · Conceptos básicos](/bbdd-aplicadas/unidad-1/teoria/) | Bases de datos y DBMS; repaso de SQL; window functions, CTE, PIVOT y SQL dinámico |
| [2 · Relacionales: aspectos básicos](/bbdd-aplicadas/unidad-2/teoria/) | El motor por dentro: arquitectura, instalación, collation, conexión, formatos de intercambio e importación |
| [3 · Relacionales: aspectos avanzados](/bbdd-aplicadas/unidad-3/teoria/) | Transacciones, concurrencia y rendimiento: índices, planes, estadísticas y métricas |
| [4 · No relacionales](/bbdd-aplicadas/unidad-4/teoria/) | Modelos NoSQL, MongoDB, relación con la POO, data lakes y KDD |
| [5 · Protección de los datos](/bbdd-aplicadas/unidad-5/teoria/) | Seguridad y permisos, cifrado, backups, recuperación y alta disponibilidad |
| [6 · Calidad en bases de datos](/bbdd-aplicadas/unidad-6/teoria/) | Ley 25.326, RGPD e ISO/IEC 25012 |

Cada unidad tiene tres partes, que también ves en el menú lateral:

- **Presentación y ruta.** Objetivos, prerrequisitos y una **ruta de aprendizaje**: la secuencia de
  lecciones y prácticas recomendada. Es el punto de partida de cada unidad.
- **Teoría.** Una lección por tema, en el orden de la ruta. La mayoría termina con errores
  frecuentes, una autoevaluación con respuestas plegadas y un resumen.
- **Práctica.** Trabajos prácticos, ejercicios y laboratorios con resolución completa.

Las unidades 4, 5 y 6 tienen además un **resumen integrador** y una **guía de repaso** (ver
[Resúmenes, guías y autoevaluaciones](#resúmenes-guías-y-autoevaluaciones)).

Algunos temas útiles que no figuran en el programa 2024 se conservan como **contenido
complementario**: llevan la marca «Complementario» (o «Parte complementaria» si solo una sección lo
es) y un aviso al comienzo. Podés dejarlos para una segunda lectura.

### Conocimientos previos

Conviene llegar con el modelo relacional (tablas, claves primarias y foráneas), consultas SQL con
`JOIN` y agrupamiento, y nociones de programación. Si alguno de esos temas está flojo, el
[repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/) de la Unidad 1 y su
[Trabajo Práctico 1](/bbdd-aplicadas/unidad-1/practica/tp1/) sirven para ponerse al día antes de
avanzar.

## Método de estudio

Para cada tema de la ruta:

1. **Identificá los objetivos.** Leé en la presentación de la unidad qué tenés que poder hacer al
   terminar el tema.
2. **Comprendé los conceptos.** Leé la lección completa una vez, sin detenerte en cada sentencia.
   Prestá atención a las definiciones y a las comparaciones con lo que ya conocés.
3. **Analizá un ejemplo resuelto.** Volvé a los ejemplos guiados y explicá con tus palabras qué hace
   cada parte y por qué el resultado es el que se muestra.
4. **Reproducilo cuando sea ejecutable.** Copiá el ejemplo en tu entorno y ejecutalo. Después cambiá
   un dato o una condición y anticipá el resultado antes de volver a ejecutar.
5. **Resolvé ejercicios sin mirar la solución.** Las resoluciones están plegadas: abrilas solo
   cuando tengas tu respuesta o después de haberlo intentado en serio.
6. **Contrastá y revisá los errores.** Compará tu resultado con el **resultado esperado** y tu
   razonamiento con la estrategia de la resolución. Si difieren, buscá la causa en la lección y en
   su sección de errores frecuentes.
7. **Avanzá o autoevaluate.** Respondé la autoevaluación de la lección. Si la resolvés sin ayuda,
   pasá al tema siguiente de la ruta; si no, volvé al paso 2 en la sección que falló.

:::tip[Cómo saber qué está comprobado]
Los ejemplos y resoluciones con código se ejecutaron en SQL Server 2022 o MongoDB 7.0, y el
resultado esperado que se muestra es el que devolvió el motor. Los experimentos que necesitan dos
sesiones simultáneas, un clúster o un servidor vinculado se presentan como **guiones paso a paso**
revisados pero no ejecutados automáticamente: cada página lo aclara. En esos casos, reproducilos
abriendo las sesiones que indica el guion.
:::

## Herramientas

Las unidades 1, 2, 3, 5 y 6 practican con **SQL Server**; la Unidad 4, con **MongoDB**. La teoría se
puede estudiar sin instalar nada, pero los ejercicios están pensados para ejecutarse.

### Para resolver los ejercicios

| Herramienta | Para qué |
|---|---|
| SQL Server 2019 o 2022, edición Developer o Express | Ejecutar los ejemplos y ejercicios de T-SQL. Developer es gratuita para desarrollo y pruebas e incluye funciones que Express no tiene |
| Un cliente SQL: SSMS (Windows) o Visual Studio Code con la extensión MSSQL (Windows, macOS y Linux) | Escribir y ejecutar consultas y ver planes de ejecución |
| MongoDB 7.0 o posterior y `mongosh` | Cargar los datos de práctica y ejecutar las consultas de la Unidad 4 |

Las diferencias entre ediciones y el proceso de instalación de SQL Server se estudian en
[Arquitectura e instalación de un motor relacional](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/#instalación-de-un-motor).
La instalación y conexión de MongoDB están en
[Instalación y conexión de MongoDB](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/).

### Opcionales

- **MongoDB Compass**: interfaz gráfica para explorar colecciones, armar pipelines e inspeccionar
  índices. Ayuda, pero todos los ejercicios se resuelven con `mongosh`. Ver
  [MongoDB Compass](/bbdd-aplicadas/unidad-4/teoria/mongodb-compass/).
- **MongoDB Atlas**: un clúster gratuito en la nube, si no querés instalar MongoDB localmente.
- **Docker**: para levantar SQL Server o MongoDB en contenedores descartables, sin instalarlos en el
  sistema.

Azure Data Studio dejó de tener soporte el 28 de febrero de 2026. Microsoft recomienda reemplazarlo
por Visual Studio Code con la extensión MSSQL.

### SQL Server en equipos con procesador ARM

SQL Server no tiene una versión para procesadores ARM64 (por ejemplo, Mac con Apple Silicon o
portátiles con Snapdragon). La documentación de Microsoft indica que sus imágenes de contenedor
solo están soportadas en hosts Linux con procesadores x86-64 de Intel o AMD, y que los entornos de
emulación o traducción (Rosetta 2, Prism, QEMU) no están probados ni soportados.

Alternativas, sin que ninguna sea obligatoria:

- **Emular la imagen x86-64 con Docker Desktop.** Los ejemplos de este sitio se verificaron así, en
  un Mac con Apple Silicon. Funciona para estudiar, pero es una configuración sin soporte oficial:
  puede ser más lenta o comportarse distinto en casos puntuales.
- **Usar un equipo o una máquina virtual x86-64** (Windows o Linux), propio o del laboratorio de la
  facultad.
- **Usar un servicio en la nube** con una oferta gratuita o para estudiantes. Algunas funciones de
  servidor (por ejemplo, ciertas opciones de backup o de seguridad de la instancia) difieren de las
  de una instalación local.

MongoDB sí publica versiones nativas para ARM64.

Consultá la [guía oficial de SQL Server en contenedores](https://learn.microsoft.com/es-es/sql/linux/install-upgrade/quickstart-install-docker)
antes de elegir, porque el soporte puede cambiar.

## Evaluación

Según el programa analítico 2024:

- **Examen parcial** teórico-práctico sobre las **unidades 1 a 4**, con recuperatorio.
- **Trabajo práctico integrador** grupal, con entregas acumulativas, coloquio y código en un
  repositorio.
- **Examen final** sobre los contenidos de **todas las unidades**.

:::caution[Confirmá la modalidad con la cátedra]
Este es un sitio personal y no oficial. Las fechas, condiciones y modalidades vigentes son las que
publica la cátedra en cada cuatrimestre.
:::

## Dos formas de recorrer la materia

### Aprender desde cero

1. Empezá por la [presentación de la Unidad 1](/bbdd-aplicadas/unidad-1/teoria/) y seguí su ruta
   de aprendizaje etapa por etapa.
2. En cada etapa aplicá el [método de estudio](#método-de-estudio): lección, ejemplo,
   reproducción, ejercicios y autoevaluación.
3. Cuando la ruta indique una práctica, resolvela antes de pasar a la etapa siguiente. Los temas
   complementarios pueden esperar a una segunda vuelta.
4. Al terminar la unidad, usá la sección **Autoevaluación y repaso** de su presentación y pasá a la
   siguiente con el enlace **Continuar**.

Los botones «Anterior» y «Siguiente» al pie de cada página siguen el mismo orden que el menú:
presentación, lecciones, prácticas y repaso de cada unidad.

### Repasar para un examen

1. **Ubicá el alcance.** El parcial abarca las unidades 1 a 4; el final, todas.
2. **Leé los resúmenes integradores** de las unidades que los tienen para recuperar el mapa de los
   temas, y las listas de objetivos de cada presentación para detectar qué no dominás.
3. **Hacé las autoevaluaciones** de las lecciones y las guías de repaso. Volvé a la lección solo en
   los temas donde fallaste.
4. **Rehacé ejercicios ya resueltos** sin mirar la solución, empezando por los de nivel intermedio y
   avanzado, y los trabajos prácticos integradores de cada unidad.

## Resúmenes, guías y autoevaluaciones

| Material | Para qué sirve |
|---|---|
| Resúmenes integradores: [Unidad 4](/bbdd-aplicadas/unidad-4/teoria/apunte-completo/), [Unidad 5](/bbdd-aplicadas/unidad-5/teoria/apunte-completo/) y [Unidad 6](/bbdd-aplicadas/unidad-6/teoria/apunte-completo/) | Ver el conjunto de la unidad antes de empezar y conectar los temas al repasar. Enlazan a cada lección; no la reemplazan |
| [Guía para el parcial (Unidad 4)](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/) | Comparaciones clave, preguntas con respuesta y simulacro sobre la Unidad 4 |
| Guías de repaso: [Unidad 5](/bbdd-aplicadas/unidad-5/teoria/guia-parcial/) y [Unidad 6](/bbdd-aplicadas/unidad-6/teoria/guia-parcial/) | Comparaciones, errores frecuentes y simulacro, orientados al trabajo práctico integrador y al final |
| Autoevaluaciones de cada lección | Comprobar la comprensión de un tema antes de seguir. La presentación de cada unidad las reúne |

Las unidades 1 a 3 no tienen resumen integrador: el repaso se hace con las autoevaluaciones de sus
lecciones y con sus prácticas, que la presentación de cada unidad enumera.
