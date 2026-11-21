# Análisis Matemático I — Auditoría pedagógica y de coherencia académica

Fecha: 2026-11-21. Rama de trabajo: `feat/analisis-matematico-i` (sin commits).
Esta auditoría parte de la reconstrucción documentada en `implementation-report.md` y de las comprobaciones
de `math-verification.json`. No repite la verificación simbólica de los 430 checks, que se corrieron una sola vez
al final como regresión.

## 1. Alcance y método

- **Páginas revisadas:** las 110 rutas de la materia: 4 presentaciones de unidad, 22 lecciones, 4 resúmenes
  integradores, prácticas, integradores, adicionales, 8 páginas de GeoGebra, portada y «Cómo estudiar».
- **Organización:**
  - Una coordinación (Opus) y tres auditores (Sonnet): U1+U4, U2, y U3+figuras.
  - Los auditores corrigieron directamente los hallazgos importantes o menores que no cambiaban matemática.
  - Todo hallazgo crítico o cambio matemático lo propuso el auditor y lo verificó la coordinación por separado,
    con cálculo propio, contraejemplo o consulta del material de la cátedra, antes de aplicarlo. Ningún cambio
    matemático crítico lo propuso y aprobó el mismo agente.
- **Fuentes de contraste:**
  - `content-guide.md`, el programa (`curriculum-map.yaml`) y las guías y apuntes de la cátedra (texto extraído
    en la etapa de ingesta, sin reprocesar con Docling);
  - el manual oficial de GeoGebra, para nombres de comandos y sintaxis.
- **Clasificación de hallazgos:**
  - **Crítico:** error matemático o conceptual que lleva a aprender algo falso.
  - **Importante:** laguna, incoherencia o error que obstaculiza el aprendizaje o hace fallar una herramienta.
  - **Menor:** redacción, notación o presentación.

## 2. Hallazgos por categoría

| Origen | Críticos | Importantes | Menores | Total |
|---|---|---|---|---|
| Coordinación (C-01 a C-10) | 0 | 5 | 5 | 10 |
| U1 + U4 (u1-u4-01 a 22) | 2 | 10 | 10 | 22 |
| U2 (u2-01 a 38) | 1 | 15 | 22 | 38 |
| U3 + figuras (u3figuras-01 a 28) | 1 | 8 | 19 | 28 |
| **Total** | **4** | **38** | **56** | **98** |

Estado:
- Corregidos: los 4 críticos y 34 de los 38 importantes.
- Importantes no corregidos: 4, todos por decisión editorial (sección 11).
- Descartados: 4 menores, con justificación.

### 2.1 Críticos (los cuatro verificados de forma independiente y corregidos)

| ID | Archivo · sección | Problema | Evidencia | Impacto | Corrección |
|---|---|---|---|---|---|
| u1-u4-01 | `unidad-1/teoria/inversa.md` · monotonía e inyectividad | Afirmaba que para funciones continuas «inyectiva ⇒ monótona» sin exigir que el dominio fuera un intervalo | La homográfica del ejemplo 1, en ℝ−{3}, es continua e inyectiva y no es monótona | Se aprende un teorema falso | Hipótesis «continuas definidas en un intervalo» y contraejemplo explícito |
| u1-u4-02 | `unidad-4/practica/integradores.md` · U4.16 b) | La explicación de un distractor decía que y = 3 − 2x vale −2 en x = 1 | 3 − 2·1 = 1 | Explicación errónea de opción múltiple | «da y = 1 en x = 1» |
| u2-01 | `unidad-2/teoria/unidad-2.md` §13 | Clasificación de discontinuidades distinta de la cátedra: «de salto (1ª especie)» y «esencial (2ª especie) si algún lateral no existe o es ±∞» | Apunte de la cátedra, U2 p. 47: las esenciales de 1ª especie son de salto finito o infinito; las de 2ª, cuando algún lateral no existe | Un salto infinito quedaba como de 2ª especie, contra lo que se evalúa | Tabla de cuatro filas alineada con la cátedra, también en la lección, en la tabla de GeoGebra y en `content-guide.md` |
| u3figuras-01 | `unidad-3/teoria/unidad-3.md` §10 | «Si f es biyectiva y derivable», la inversa es derivable con (f⁻¹)′ = 1/f′(f⁻¹) | f(x) = x³ es biyectiva y derivable, pero f⁻¹ = ∛x no es derivable en 0 porque f′(0) = 0 | Se aplica la fórmula donde no vale | Hipótesis completas: continua y estrictamente monótona en un intervalo, derivable en x₀, f′(x₀) ≠ 0 |

### 2.2 Importantes (selección; el detalle está en la sección 7)

- **Hipótesis matemáticas faltantes o imprecisas:**
  - u1-u4-03: contacto «al menos» de orden n.
  - u1-u4-06: hipótesis de la inversa de una composición.
  - u2-02: definición de continuidad que excluía los puntos fuera del dominio que la misma lección clasifica.
  - u2-04: faltaba el límite de una composición, usado en las demostraciones de límites notables y de $1^\infty$.
  - u2-05: faltaba $\lim f^{g}=L^{M}$, usado en cinco ejercicios.
  - u2-06: acotada / ∞ en el infinito.
  - u3figuras-02: derivadas laterales «finitas e iguales».
- **Contenido usado antes de enseñarse:**
  - u2-07: equivalentes de ln, exp, arcsen y arctan.
  - u2-13: «infinitésimo».
  - u1-u4-07: monotonía estricta.
  - u1-u4-11: Rolle, ahora declarado como resultado asumido.
  - u1-u4-13: producto de polinomios truncados.
- **Promesas no cumplidas:** u2-14, L'Hôpital anunciado «en la U3» sin lección que lo desarrolle. Se retiró la
  promesa.
- **Resultados mal leídos:**
  - u2-10: 20d escribía «2/0 = ∞» y «límite global ∞», cuando los laterales son −∞ y +∞, así que el límite
    bilateral no existe.
  - u2-11: formas indeterminadas escritas como igualdades.
  - u2-12: equivalentes sustituidos dentro de sumas.
- **Ejercicios mal planteados:**
  - u3figuras-07: el modelo del horno U3.01 daba T(40) = −20 °C y la respuesta caía en el extremo del dominio.
  - u3figuras-08: U3.12 repetía los puntos del ejemplo 5 resuelto.
- **GeoGebra (coordinación):**
  - C-01 a C-04: cinco comandos de regresión, `FunciónInversa`, `LímiteSuperior`/`LímiteInferior` e
    `Intersección` no existen.
  - C-09: toda la guía usaba `;` como separador de argumentos y afirmaba que en español el decimal es coma. Según
    el manual oficial, la entrada usa punto decimal y coma entre argumentos, y `(r; α)` es la notación de
    **coordenadas polares**. Por eso `A = (2; 3)` creaba otro punto.
- **Figuras:** u3figuras-20 a 22. Las etiquetas π no se mostraban, la figura de aproximación lineal no dejaba ver
  la diferencia que pretendía mostrar y las leyendas quedaban cortadas.

## 3. Coherencia

**Dentro de cada unidad.**
- Las rutas de estudio de cada presentación se contrastaron con las lecciones.
- Se reasignaron ejercicios mal ubicados:
  - el ejercicio 13 de la Práctica 2 pasó de la etapa 4 a la 5, porque necesita límites 0/0;
  - en U3 se reordenaron los pasos 1 a 3 para que cada ejercicio aparezca después de la regla que usa.
- Se agregaron los enlaces a prerrequisitos que faltaban: continuidad y cálculo de límites en U2, enlaces a U2
  desde las reglas de derivación.

**Entre unidades (funciones → límites → continuidad → derivada → aproximación lineal → Taylor).**
- Las dependencias hacia atrás están enlazadas.
- Se corrigieron estas rupturas:
  - **Funciones → límites:** la recíproca de monotonía e inyectividad se apoya ahora en la continuidad en
    intervalos, que U2 desarrolla. El TVI de U1 se anuncia como «se estudia en la U2», no como «se demuestra».
  - **Límites → continuidad:** el límite de una composición se enuncia en Continuidad y se acepta con remisión
    explícita en Cálculo de límites. Antes se usaba sin enunciar.
  - **Continuidad → derivada:** el resumen de U3 recoge las tres formas de no derivabilidad (punta, tangente
    vertical, cúspide) que la lección ya enseñaba.
  - **Derivada → aproximación lineal → Taylor:** se agregó una oración en la definición de recta tangente que
    presenta la tangente como mejor aproximación lineal y enlaza a la U4. Antes U3 no anticipaba ese paso.
  - **Resúmenes integradores:** el de U2 contradecía a la lección en la clasificación de discontinuidades y
    prometía L'Hôpital. El de U3 tenía hipótesis incompletas en la inversa y en las derivadas laterales. Los
    cuatro resúmenes quedan alineados con sus lecciones.

## 4. Notación

Se unificó con `content-guide.md`:
- `\operatorname{sen}` y `\operatorname{arcsen}` en lugar de `\sin`/`\arcsin`: resúmenes de U1–U4, prácticas y
  dos páginas de GeoGebra (C-07);
- `E(a,r)` y `E^*(a,r)`;
- $D_f$;
- asíntota oblicua $y=mx+n$;
- «Mac Laurin», como el programa;
- coordenadas $(a, b)$ con coma en las figuras (cuatro etiquetas usaban `;`).

En la entrada de GeoGebra se usa la sintaxis real del programa: coma entre argumentos y punto decimal. En el
texto matemático se mantiene la coma decimal.

Un efecto colateral documentado: ocho encabezados de U3 y U4 cambiaron de texto al unificar la notación, por
ejemplo «Polinomio de Maclaurin» → «Mac Laurin», y con eso cambian sus anclas. Ningún enlace interno ni test las
usaba. Las URL de página no cambian.

## 5. Ejercicios

- **Revisión pedagógica:**
  - los 95 ejercicios originales de las lecciones: enunciado, nivel, estrategia, resolución y resultado;
  - un muestreo por riesgo de los ejercicios de la guía asignados en las rutas: al menos uno por etapa, y todos
    los marcados como de lectura de gráficos o de razonamiento.
- **Cambios con efecto matemático** (se actualizaron los checks correspondientes):
  - **U3.01:** el dominio pasa a $[0, 30]$ y c) pide $T'(t)=-8$, con respuesta $t=20$ y $T(20)=100$ °C. El check
    agrega $T(30)=30$ y que $T'$ no se anula en el dominio.
  - **U3.12:** se piden $(g\circ f)'(1)=12$, $(f\circ g)'(2)=12$ con tangente $y=2+12(x-2)$, y
    $(f/g)'(3)=\tfrac74$. El check comprueba además que los datos no repiten los del ejemplo 5.
  - **Ejercicio 20d de la guía:** se mantiene la respuesta oficial, pero la resolución explica que el límite
    bilateral no existe y que «∞» debe leerse como $\lvert f\rvert\to\infty$.
- **Justificaciones agregadas o corregidas, sin cambiar resultados:**
  - Práctica 1: ejercicio 26, inyectividad y biyectividad; ejercicio 32 k.
  - Práctica 2: ejercicio 20 a, dividir por $x$ en lugar de sustituir dentro de sumas; ejercicio 33 g,
    contraejemplo en lugar de «siguiendo la respuesta oficial»; ejercicio 28 i, conclusión; ejercicio 21, cifras
    intermedias; adicional 1 c, interpretación de $x\to\infty$.
  - Práctica 4: U4.09 c y U4.15 d.
- **Niveles:** U2.11 baja de avanzado a intermedio, porque repite la técnica del ejemplo 6.
- **Autoevaluaciones:**
  - la de Asíntotas tenía una respuesta que no cumplía lo pedido. Ahora usa $1+\frac{x}{1+e^x}$, con AH $y=1$ en
    $+\infty$ y AO $y=x+1$ en $-\infty$. Al verificarla, SymPy 1.14 devolvió un valor erróneo para
    $\lim_{x\to-\infty}(f-x)$, así que se comprobó a mano y numéricamente;
  - se agregó una tercera pregunta, porque la guía de contenido pide de 3 a 5.
- **Estructura:** los 95 marcadores `<!-- ejercicio -->` se conservan con los mismos ID, y cada ejercicio
  conserva su resolución (comprobado por script).

## 6. Gráficos

Las 31 figuras SVG se revisaron en contenido matemático, en lectura y en los esquemas claro y oscuro. Todas son
matemáticamente correctas. Se corrigieron estos defectos comprobados en los scripts de `figures/`:

- **`svgplot.py`:**
  - las etiquetas de marcas personalizadas se buscaban por igualdad exacta de flotantes, así que las etiquetas π
    de `u1-trigonometricas` no aparecían;
  - la leyenda tenía posición fija y se cortaba con etiquetas largas;
  - los números de los ejes usaban punto decimal y guion. Esto cambia los 31 SVG.
- **Escalas:** `u3-tangente-normal` y `u3-implicita` pasan a escala 1:1, para que la normal se vea perpendicular.
- **Ventanas:**
  - `u1-signo`: el mínimo quedaba fuera de la ventana;
  - `u3-secantes`: el punto (3, 9) quedaba sobre el borde;
  - `u4-aprox-lineal`: la ventana [1, 3] no dejaba distinguir la curva de la tangente. Se probó un segmento de
    error, pero se descartó porque mide 0,01 y no se ve.
- **Detalles:**
  - el cero de `u1-transf-composicion` estaba dibujado como punto hueco aunque pertenece al gráfico;
  - el título de `u2-infinitesimos` decía «x² es de otro tamaño», aunque es del mismo orden;
  - el pie de `u1-inversa-reflejo` era impreciso.

Las figuras se regeneraron con los scripts y las afectadas se revisaron renderizadas en los dos esquemas. Los
PNG de revisión no se conservan.

## 7. Demostraciones (revisión selectiva)

Se revisaron las demostraciones con señales de riesgo: hipótesis, uso de resultados no enunciados y pasos al
límite.

| Demostración | Resultado |
|---|---|
| Unicidad del límite, suma, intercalación, límites laterales | Correctas |
| $\frac{\operatorname{sen}x}{x}\to1$ (geométrica) | Correcta; se declararon sus dos supuestos geométricos |
| Número $e$, $\frac{\ln(1+u)}{u}$, $\frac{e^u-1}{u}$, regla $1^\infty$ | Correctas, pero usaban el límite de una composición sin enunciarlo. Ahora se enuncia (u2-04) y se agrega el caso $f=1$ en $1^\infty$ |
| Valor intermedio a partir de Bolzano | Faltaba el caso $\varphi(a)=0$ o $\varphi(b)=0$; agregado |
| Derivada de la inversa (lección y resumen) | La lección era correcta; el resumen tenía hipótesis insuficientes (crítico u3figuras-01) |
| Paridad de los polinomios de Mac Laurin | Reescrita con la hipótesis «derivable n veces en un entorno simétrico de 0» y un argumento directo |
| Término complementario de Lagrange | Usa Rolle, que no está en el programa; se declara como resultado asumido en la parte opcional |
| Inyectividad y monotonía; inversa de la composición | Hipótesis corregidas (u1-u4-01 y u1-u4-06) |

## 8. Navegación y experiencia de estudio

- Las presentaciones de unidad y sus rutas por etapas son el punto de entrada. Se revisó que cada ejercicio
  asignado exista y esté en la etapa en que ya se enseñó lo que necesita.
- **Paginación:** después del resumen de U4, «Siguiente: Presentación» llevaba a GeoGebra (C-05). El índice de
  GeoGebra se rotula ahora «Introducción».
- **«Cómo estudiar»:** distingue lo que se recalculó con SymPy de lo que solo se revisó, como demostraciones y
  ejercicios conceptuales (C-06).
- **Lecciones de U2:** se señala en la ruta que los ejercicios 4, 22, 23 y 27 de la Práctica 2 piden leer
  gráficos que el sitio no reproduce.

## 9. Cambios (resumen por archivo)

- **U1:**
  - `inversa.md`: recíproca de monotonía, composición y pie de figura;
  - `funciones-elementales.md`: monotonía estricta;
  - `funciones-y-modelos.md`: U1.03 y ejemplo 1;
  - `caracteristicas.md` y `algebra-y-transformaciones.md`;
  - resumen;
  - prácticas: ejercicios 26 y 32, adicionales;
  - integradores: `Interseca` y coordenadas con coma.
- **U2:**
  - `continuidad.md`: definición, límite de una composición, clasificación, extremos en el valor intermedio,
    función signo;
  - `limites-laterales-y-propiedades.md`: potencia de exponente variable, infinitésimo, supuestos de
    $\operatorname{sen}x/x$;
  - `infinitesimos.md`: hipótesis $u\neq0$, equivalentes usados como dato, nivel de U2.11;
  - `limites-infinitos.md`: tabla con acotadas, sin L'Hôpital;
  - `calculo-de-limites.md`;
  - `asintotas.md`: autoevaluación;
  - resumen;
  - `index.md`: ruta y nota de gráficos;
  - ejercicios 1, 4, 8, 20, 21, 25, 28 y 33, adicionales.
- **U3:**
  - `razon-de-cambio-y-derivada.md`: U3.01 y puente a U4;
  - `derivada-como-funcion.md`;
  - `reglas-de-derivacion.md`;
  - `regla-de-la-cadena-e-inversa.md`: U3.12;
  - `implicita-y-logaritmica.md`;
  - integradores;
  - Práctica 3;
  - resumen: §5, §6, §8 y §10;
  - `index.md`: ruta.
- **U4:**
  - `polinomio-de-taylor.md`: ejemplo 7, U4.09 c y paridad;
  - `termino-complementario.md`;
  - resumen: orden de contacto;
  - integradores: U4.15 y U4.16;
  - Práctica 4 e `index.md`: Mac Laurin.
- **GeoGebra:**
  - `basico.md` e `index.md`: sintaxis real;
  - `funciones.md`: regresión e `Inversa`;
  - `limites-continuidad.md`: comandos y clasificación;
  - `derivada.md` y `taylor.md`: separadores.
  - En total, 151 separadores `;` reemplazados en 6 archivos.
- **Fuentes y herramientas:**
  - `content-guide.md`: clasificación de la cátedra;
  - `checks/u3_practica.py`: U3.01 y U3.12;
  - `figures/svgplot.py`, `u1_figuras.py`, `u2_figuras.py`, `u3_figuras.py` y `u4_figuras.py`.

No se tocaron otras materias, los `raw/`, `processed/`, los slugs ni los ID de ejercicios y checks.

## 10. Validaciones

| Validación | Resultado |
|---|---|
| `content-pipeline verify-math --subject analisis-matematico-i` (suite completa, solo como regresión final) | 430/430 |
| `content-pipeline qa --subject analisis-matematico-i` | 0 errores, 0 advertencias |
| `pytest` (tools/content-pipeline) | 108 aprobados, 1 omitido (contenedores de BBDD apagados) |
| `npm run build` | 288 páginas |
| `npm run validate` | Aprobado tras registrar la etapa AM2 en `migration/revisions.json` |
| `npx playwright test` | 56 aprobados, 6 omitidos (omitidos por la propia suite) |
| `git diff --check` | Sin problemas |
| Ejercicios con resolución (script) | 95/95 |

**Comparación con la línea base previa a la auditoría:**

| Elemento | Antes | Después | Comentario |
|---|---|---|---|
| Rutas | 110 | 110 | Ninguna ruta agregada ni quitada |
| ID de ejercicios | 95 | 95 | Idénticos |
| Imágenes | 34 | 34 | Mismas figuras |
| Bloques de resolución (`<details>`) | 168 | 169 | +1: una pregunta de autoevaluación nueva en Asíntotas |
| Fórmulas en bloque | 918 | 917 | 20d sin la igualdad «2/0 = ∞» |
| Enlaces internos | 363 | 378 | +15 enlaces a prerrequisitos y a lecciones relacionadas |
| Encabezados | 1155 | 1155 | 8 con texto (y ancla) distinto por la notación |

## 11. Limitaciones

- **Ejercicios de la guía:** se revisaron por muestreo de riesgo, no uno por uno. Los resultados ya se habían
  verificado con SymPy en la reconstrucción.
- **Resueltos en el seguimiento del 21/11/2026** (sección 13): u2-09 (gráficos de los ejercicios 4, 22, 23 y 27),
  u2-15 (adicionales 2, 4, 5 y 7), u2-34 (integrador de continuidad) y u2-35 (niveles de U2.21 y U2.27).
- **Descartados:**
  - u1-u4-19: renumerar «Ejercicio N», porque cambiaría anclas y las rutas ya distinguen «de la Práctica N»;
  - u1-u4-21 y u2-38: preferencias de estilo;
  - u2-37: cubierto por u2-05.
- **GeoGebra:** se ejecutó una muestra de 52 usos de 28 comandos (sección 13). El resto de los usos solo se revisó
  contra el manual.
- **Herramientas:** SymPy 1.14 calcula mal algunos límites (potencias con exponente $1/x$ y
  $x\,e^{x}/(1+e^{x})$ en $-\infty$); en esos casos se usa contraste numérico. Los checks de razonamiento
  verifican hechos de apoyo, no la argumentación.

## 12. Evaluación final crítica

Cada criterio se evalúa según si cumple o no un estándar explícito, con su evidencia. No hay puntuaciones
numéricas.

- **Corrección matemática.**
  - *Criterio:* ningún enunciado falso; los teoremas con todas sus hipótesis; resultados verificados.
  - *Estado:* se cumple, con las limitaciones de la sección 11. Se encontraron y corrigieron cuatro errores
    conceptuales, todos en enunciados con hipótesis incompletas o en un resumen que contradecía a su lección. Los
    cálculos no tenían errores (430/430 antes y después).
  - *Riesgo remanente:* los resúmenes son la parte más expuesta, porque condensan sin demostrar.
- **Coherencia.**
  - *Criterio:* ningún concepto usado antes de definirse ni promesa sin cumplir, y la misma clasificación y
    notación en todas las páginas.
  - *Estado:* se cumple tras las correcciones. Era el área más débil: la clasificación de discontinuidades tenía
    tres versiones (lección, resumen, GeoGebra), L'Hôpital estaba anunciado sin lección y la composición de
    límites se usaba sin enunciar.
- **Claridad pedagógica.**
  - *Criterio:* cada lección motiva, define, ejemplifica y advierte errores típicos.
  - *Estado:* se cumple en las 22 lecciones. Son fuertes «Continuidad», pensada para estudio autónomo, e
    «Infinitésimos» por el ejemplo sobre sumas. Son débiles los resúmenes, que funcionan como mapa pero no como
    material de estudio.
- **Ejercicios.**
  - *Criterio:* progresión de nivel, resolución con estrategia, sin duplicar ejemplos y con datos realistas.
  - *Estado:* se cumple en los 95 ejercicios propios tras corregir U3.01 y U3.12. En los ejercicios de la guía,
    la cobertura de lectura de gráficos y los adicionales de U2 siguen siendo parciales.
- **Figuras.**
  - *Criterio:* correctas, legibles en ambos esquemas, con escala adecuada a lo que muestran y sin elementos
    decorativos.
  - *Estado:* se cumple. Los defectos eran de presentación, no de contenido.
- **Estudio autónomo.**
  - *Criterio:* un estudiante puede recorrer cada unidad sin ayuda externa, sabiendo qué estudiar, en qué orden y
    cómo comprobarse.
  - *Estado:* se cumple, gracias a las rutas por etapas, las autoevaluaciones y las resoluciones plegadas.
  - *Límites:* ejercicios de la guía con gráficos no reproducidos y una guía de GeoGebra cuya sintaxis no se
    probó en la aplicación.

## 13. Seguimiento: resolución de los pendientes (21/11/2026)

Pedido posterior a la aprobación de la auditoría. No se reprocesaron documentos con Docling ni se repitieron las
auditorías.

### 13.1 Gráficos de la Práctica 2 (ejercicios 4, 22, 23 y 27)

- **Fuente.** Los 15 gráficos se inspeccionaron sobre las páginas 15, 19 y 20 de la guía, renderizadas desde el PDF de
  `raw/`. Son capturas de GeoGebra **sin fórmula**.
- **Método.** Se reconstruyeron por **digitalización**, sin inventar fórmulas ni valores (`figures/digitalizacion/`):
  - recorte de la página renderizada;
  - calibración de la escala con la cuadrícula o con las marcas de los ejes, verificada contra los puntos marcados;
  - extracción de cada curva por color;
  - una polilínea por rama, unida solo donde la extracción la había cortado.
- **Lo que se toma del original.** Los puntos llenos y huecos, las rectas punteadas y las guías.
- **Asíntotas punteadas.** Se midieron sobre la imagen; la tabla de medidas y lecturas está en la página del
  ejercicio 22. Las diferencias son de 0,08 o menos.
- **Datos y figuras.** Los datos quedan en `figures/datos/practica-2-digitalizado.json` y las figuras salen de
  `figures/u2_practica_graficos.py`. Cada SVG se comparó visualmente con su original.
- **Dos ajustes documentados en el código:**
  - en 4a, el tramo que coincide con el eje x se detectó por el grosor del trazo;
  - en 22d, las ramas que quedan bajo la asíntota punteada se prolongaron horizontalmente.
- **Resoluciones.** Las páginas de los cuatro ejercicios tienen ahora el gráfico y una resolución completa. Antes
  remitían al PDF.
- **Limitaciones honestas:**
  - la guía no da respuestas de los ejercicios 4, 22 y 23;
  - los valores que no caen en la cuadrícula se informan como aproximados: $g(5)\approx2{,}4$ y la AH de 23 en
    $-\infty$, cercana a $-2$;
  - en 22 d) y 23 hay asíntotas verticales que el original no marca. Se informa el intervalo que permite la imagen y
    no un valor inventado;
  - el ejercicio 27 coincide con las respuestas oficiales.
- **No hizo falta un ejercicio original sustituto:** los 15 gráficos se pudieron reconstruir.

### 13.2 Adicionales 2, 4, 5 y 7 de la Práctica 2

- **Recuperación.** Los cuatro enunciados se recuperaron completos de las páginas 22 y 23 renderizadas. Quedan
  transcriptos en la página, con dos notas fieles al original: la opción b) del adicional 6 está incompleta, y el
  adicional 7 llama $f$ a la función $g$.
- **Resoluciones.** Se rehicieron para esos enunciados:
  - adicional 2: discusión de AV según $b$ e inciso c) con $a=1$, $b=4$;
  - adicional 4: opción a);
  - adicional 5: opción b);
  - adicional 7: opción d);
  - adicional 6: se agregó el enunciado y la opción d).
- **Checks.** Nuevos `U2.A.ADI.2`, `U2.A.ADI.5` y `U2.A.ADI.7`. `U2.A.ADI.4` se mantiene.
- **Atribuciones falsas corregidas.** La guía **no publica respuestas** de los adicionales de ninguna práctica, y
  varias resoluciones decían «coincide con la respuesta oficial»: el adicional 4 lo decía antes de tener el
  enunciado. Esas frases se retiraron en U2 y en U1.
- **Hallazgo matemático.** El adicional 2 y el ejercicio 25 c) piden si existe un $b$ con una sola AV. La respuesta
  oficial del 25 c) dice que no, pero con $b=a^2$ el factor $ax+1$ se cancela y queda una única AV, $x=\frac1a$. El
  check `U2.A.E25.c` ya lo registraba sin que la página lo dijera. Ahora las dos páginas lo explican con un recuadro
  de diferencia con la respuesta oficial.

### 13.3 Integrador de continuidad (U2.32)

- **Ejercicio.** Es original, sobre una función de cuatro tramos. Evalúa:
  - límites laterales con equivalentes y con valor absoluto;
  - existencia del límite y continuidad en los empalmes, con un parámetro;
  - salto infinito en un punto que **pertenece** al dominio;
  - salto finito con cálculo del salto;
  - imposibilidad de redefinir;
  - una variante con $\operatorname{sen}\frac{1}{x+1}$, que da una discontinuidad de segunda especie.
- **Requisitos.** Usa solo contenidos de las lecciones de U2.
- **Resolución.** Incluye estrategia, desarrollo, resultado e interpretación conceptual.
- **Comprobación.** Check `U2.32`: parámetros, laterales y contraste numérico; para la segunda especie, valores $\pm1$
  arbitrariamente cerca de $-1$.
- **Registros.** Se agregó a la ruta de la unidad (etapa 8) y a la matriz curricular (tema `u2-discontinuidades`).

### 13.4 Dificultad de U2.21 y U2.27

Criterio: «avanzado» se reserva para lo que integra temas, usa parámetros o casos, o pide demostrar.
- **U2.21:** evalúa un modelo logístico, calcula el límite de $e^{-kt}$ y resuelve una ecuación exponencial. Son tres
  pasos breves de un solo tema.
- **U2.27:** calcula dos laterales triviales y discrimina continuidad lateral, evitable y salto. No usa parámetros ni
  combina temas.

Las dos pasan a `intermedio`. Enunciados y resoluciones no cambian. U2 conserva 10 ejercicios avanzados (el mínimo
por nivel es 4).

### 13.5 Anclas de compatibilidad

Para los 13 encabezados cuyo texto cambió (8 de la auditoría y 5 de los adicionales), se insertó antes de cada
encabezado un `<div id="…" aria-hidden="true"></div>` con el identificador antiguo. Esos identificadores se
calcularon con `github-slugger`, el mismo algoritmo del sitio, que reproduce exactamente los identificadores
actuales. No se duplica contenido y las URL no cambian. El build contiene los dos identificadores de cada
encabezado.

### 13.6 GeoGebra: comprobación ejecutada

- **Protocolo.** `geogebra/` contiene un protocolo reproducible (`ejecutar.mjs`, `casos.json`, `README.md`). Abre
  GeoGebra web, de la distribución oficial, en Chromium con interfaz en español y **pega cada comando en la barra de
  entrada**. La API `evalCommand` no sirve para esto porque solo acepta nombres en inglés.
- **Resultado.** **52/52** casos, sobre 28 comandos, dieron lo esperado en GeoGebra 5.4.920.0. Incluye casos
  negativos.
- **Errores encontrados y corregidos:**
  - `Límite(f, infinito)` no funciona: se usa `∞` o `inf`. Con `Infinito` en mayúscula, GeoGebra crea en silencio
    un número de ese nombre;
  - `DerivadaImplícita(c)` con una cónica y `DerivadaImplícita(c)(3, 4)` no funcionan: el argumento es la expresión
    $F(x,y)$, y para evaluar se define `m(x, y) = …`.
- **Confirmado:**
  - punto decimal, coma entre argumentos y `;` como coordenadas polares;
  - `Raiz` sin tilde no se reconoce;
  - la regresión del resorte da $y\approx0{,}8749x+0{,}0018$, como afirma la guía.
- **Límites.** Es una muestra, sobre una sola versión de GeoGebra. Los demás usos siguen revisados solo contra el
  manual, y así se aclara en `geogebra/index`.

### 13.7 Validación

| Validación | Resultado |
|---|---|
| `verify-math` (suite completa) | 434/434 (430 anteriores y 4 nuevas) |
| `qa --subject analisis-matematico-i` | 0 errores, 0 advertencias; 110 páginas, 96 ejercicios |
| `pytest` | 108 aprobados, 1 omitido |
| `npm run build` | 288 páginas |
| `npm run validate` | Aprobado tras registrar la etapa AM3 (14 páginas) |
| `npx playwright test` | 56 aprobados, 6 omitidos |
| Protocolo de GeoGebra | 52/52 |
| Línea base | 110 rutas (sin cambios); IDs de ejercicios previos sin cambios, más U2.32; imágenes 34 → 49 (15 nuevas); ninguna figura previa eliminada |
