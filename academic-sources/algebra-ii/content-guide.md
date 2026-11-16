# Guía de producción — Álgebra y Geometría Analítica II

Contrato común para redactar, verificar e integrar las páginas de `src/content/docs/algebra-ii/`.
Toda página nueva lo cumple. Las decisiones están tomadas: no reabrirlas página por página.

## 1. Alcance y fuentes

- Asignatura 3645, Ingeniería en Informática, UNLaM. **Programa vigente: año académico 2023**
  (`raw/programa/661_3645_AlgebrayGeometriaAnaliticaII.pdf`, publicado por el DIIT; no hay versión
  posterior). La cobertura sale del programa, no de las fuentes viejas.
- **Fuera de programa** (no desarrollar): cónicas y cuádricas, diagonalización ortogonal como tema
  propio, transformaciones ortogonales, ecuaciones diferenciales, espacios de funciones continuas con
  producto integral, forma de Jordan. Se pueden mencionar en una línea como "para seguir".
- Las fuentes de cátedra (guías, parciales, apuntes) son **privadas**: sirven para alinear temas,
  notación, nivel y tipo de ejercicio. **Nunca** se copian enunciados, datos numéricos, figuras ni
  párrafos. Todos los ejercicios y ejemplos usan datos propios.
- Digestos de lectura (privados, no versionados): `academic-sources/algebra-ii/processed/digests/`.
  Las erratas que señalan **no** se heredan.
- Bibliografía que se puede citar con secciones verificadas: Poole, *Álgebra lineal. Una introducción
  moderna*, 3.ª ed. (Cengage, 2011); el programa pide la 4.ª ed. (2017), cuya numeración no se verificó.
  Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed. (Pearson, 2016) se cita **sin** números de sección
  o página (no está disponible localmente). Nakos y Joyner, *Álgebra lineal con aplicaciones*
  (Thomson, 1999) para códigos. Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.
  (Pearson, 2012) como complementaria. No inventar páginas ni ediciones.

## 2. Estructura y slugs

Cada archivo `.md` tiene `slug` explícito igual a su ruta sin extensión (sin `index`):

```text
algebra-ii/                         index.md          Presentación de la materia
algebra-ii/programa/                programa.md
algebra-ii/como-estudiar/           como-estudiar.md
algebra-ii/notacion/                notacion.md
algebra-ii/bibliografia/            bibliografia.md
algebra-ii/repaso/                  repaso/index.md + lecciones
algebra-ii/unidad-N/                unidad-N/index.md  Presentación de la unidad
algebra-ii/unidad-N/teoria/<tema>/  unidad-N/teoria/<tema>.md
algebra-ii/unidad-N/practica/<x>/   unidad-N/practica/{nivel-inicial,nivel-intermedio,nivel-avanzado,guia-integradora}.md
algebra-ii/integradores/            integradores/index.md + simulacro-1.md + simulacro-2.md
```

Lecciones previstas (slug final entre paréntesis; el orden es el de `sidebar.order`):

- **Repaso** (`repaso/`): 1 `vectores-y-matrices`, 2 `determinantes`, 3 `sistemas-lineales`,
  4 `polinomios`, 5 `rectas-y-planos`.
- **Unidad 1** (`unidad-1/teoria/`): 1 `cuerpos-y-z2`, 2 `espacios-vectoriales`, 3 `subespacios`,
  4 `combinaciones-lineales`, 5 `independencia-lineal`, 6 `subespacios-de-una-matriz`,
  7 `base-y-dimension`, 8 `coordenadas`, 9 `cambio-de-coordenadas`, 10 `codigos-lineales`.
- **Unidad 2** (`unidad-2/teoria/`): 1 `definicion-y-ejemplos`, 2 `nucleo-e-imagen`,
  3 `teorema-de-la-dimension`, 4 `clasificacion`, 5 `teorema-fundamental`, 6 `matriz-asociada`,
  7 `cambio-de-base`, 8 `composicion-e-inversa`.
- **Unidad 3** (`unidad-3/teoria/`): 1 `autovalores-y-autovectores`, 2 `polinomio-caracteristico`,
  3 `propiedades`, 4 `matrices-semejantes`, 5 `diagonalizacion`, 6 `potencias`,
  7 `relaciones-de-recurrencia`, 8 `cadenas-de-markov`.
- **Unidad 4** (`unidad-4/teoria/`): 1 `producto-interno`, 2 `norma-distancia-angulo`,
  3 `ortogonalidad`, 4 `gram-schmidt`, 5 `complemento-ortogonal`, 6 `proyeccion-y-distancia`,
  7 `cuadrados-minimos`, 8 `codigos-y-z2`.
- **Práctica** de cada unidad (`unidad-N/practica/`): 1 `nivel-inicial`, 2 `nivel-intermedio`,
  3 `nivel-avanzado`, 4 `guia-integradora`.

Enlaces internos: siempre absolutos con barra final, por ejemplo
`[coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/)`; con ancla, `.../coordenadas/#unicidad`.
Solo enlazar páginas de esta lista. No usar rutas relativas.

## 3. Frontmatter

```yaml
---
title: Subespacios
description: Criterio de subespacio, ejemplos en ℝⁿ, ℤ₂ⁿ y matrices, y errores frecuentes.
slug: algebra-ii/unidad-1/teoria/subespacios
sidebar:
  order: 3
  label: 1.3 Subespacios
---
```

- `title` corto, sin "Unidad N —" en lecciones. En las presentaciones: `Unidad 1 — Espacios vectoriales`.
- `description` de una oración (la usa la búsqueda y las tarjetas).
- `sidebar.label`: lecciones `N.k Título`; práctica `Nivel inicial`, `Nivel intermedio`,
  `Nivel avanzado`, `Guía integradora`; repaso `R.k Título`.
- No repetir el título como `# H1` en el cuerpo: Starlight lo muestra. El cuerpo empieza en `##`.

## 4. Notación de la cátedra (obligatoria)

| Concepto | Escribir | No escribir |
|---|---|---|
| Cuerpo | $K$, $\mathbb{R}$, $\mathbb{Z}_2=\{0,1\}$ | $\mathbb{F}_2$, GF(2) (se pueden mencionar una vez como sinónimos) |
| Espacios | $\mathbb{R}^n$, $\mathbb{Z}_2^n$, $\mathbb{R}^{m\times n}$, $P_n[\mathbb{R}]$ (polinomios de grado $\le n$ y el nulo, variable $x$) | $\mathcal P_n$, $M_{m\times n}$ |
| Vector nulo | $0_V$ (o $0$ si no hay ambigüedad) | |
| Generado | $\operatorname{gen}\{v_1,\dots,v_k\}$ | span, $\langle\ \rangle$ (reservado al producto interno) |
| Subespacios de $A$ | $\operatorname{fil}(A)$, $\operatorname{col}(A)$, $\operatorname{nul}(A)$; $\operatorname{rango}(A)$ | row, Col, rank |
| Rango–nulidad | $\operatorname{rango}(A)+\dim\operatorname{nul}(A)=n$ | |
| Base | $B=\{v_1,\dots,v_n\}$, **ordenada**; canónica $E$; $\dim(S)$ | |
| Coordenadas | $[v]_B$, **vector columna** | |
| Cambio de coordenadas | $C_{BB'}$: de $B$ a $B'$; columnas $[b_j]_{B'}$; $C_{BB'}[v]_B=[v]_{B'}$; $C_{B'B}=C_{BB'}^{-1}$; $C_{BB''}=C_{B'B''}\,C_{BB'}$ | $P_{B'\leftarrow B}$ (solo en la nota de equivalencias) |
| Transformación lineal | $T:V\to W$ (también $f$); "TL" | |
| Núcleo, imagen | $\operatorname{Nu}(T)$, $\operatorname{Im}(T)$ | Ker, ran, "rango" de una TL |
| Matriz de una TL | $M(T)_{BB'}$: salida $B$, llegada $B'$; columnas $[T(b_j)]_{B'}$; $M(T)_{BB'}[v]_B=[T(v)]_{B'}$; tamaño $\dim W\times\dim V$; si $V=W$ y una sola base, $M(T)_B$ | $[T]_{B'\leftarrow B}$ (solo en equivalencias) |
| Cambio de bases de la matriz | $M(T)_{B_1B_1'}=C_{B'B_1'}\,M(T)_{BB'}\,C_{B_1B}$ (se lee de derecha a izquierda) | |
| Clasificación | monomorfismo, epimorfismo, isomorfismo; endomorfismo | |
| Autovalores | $Av=\lambda v$, $v\neq 0$; $p_A(\lambda)=\det(\lambda I-A)$ (mónico); $E_\lambda(A)=\operatorname{nul}(\lambda I-A)$; $m_a(\lambda)$, $m_g(\lambda)$ | $\det(A-\lambda I)$ como definición (se aclara que tiene las mismas raíces) |
| Semejanza, diagonalización | $A=CBC^{-1}$; $A=CDC^{-1}$ con $C=(v_1\mid\cdots\mid v_n)$ columnas autovectores, $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ | $P$ para la matriz de autovectores |
| Transpuesta, traza | $A^t$, $\operatorname{tr}(A)$ | $A^T$ |
| Producto interno | $\langle u,v\rangle$; espacio euclídeo $(V,\langle\,,\rangle)$; usual en $\mathbb{R}^n$: $u\cdot v$ o $\langle u,v\rangle$ | |
| Norma, distancia, ángulo | $\lVert v\rVert$, $d(u,v)=\lVert u-v\rVert$, $\angle(u,v)$ | $\lvert v\rvert$ para norma |
| Ortogonalidad | $u\perp v$, $S^{\perp}$, $\operatorname{proy}_S(v)$, $d(v,S)$ | |
| Códigos | código lineal $(n,k)$; palabras código; **$G$ de $k\times n$ cuyas filas son una base del código** (codificar: $u=aG$, $a\in\mathbb{Z}_2^k$ fila); **$H$ matriz de control de paridad** con $\mathcal C=\operatorname{nul}(H)$, es decir $Hv^t=0$; síndrome $s=Hv^t$; peso $w(v)$; distancia de Hamming $d_H(u,v)=w(u+v)$; distancia mínima $d(\mathcal C)$; código dual $\mathcal C^{\perp}$; autodual $\mathcal C^{\perp}=\mathcal C$ | $G$ de $n\times k$ (convención de Poole: se explica en la nota de equivalencias) |

- Vectores de $K^n$ en el texto: $n$-uplas con comas $(1,-2,0)$; en cuentas matriciales, columnas.
- Base canónica de $P_2[\mathbb{R}]$: $E=\{1,x,x^2\}$ en ese orden (se dice explícitamente cada vez
  que importa el orden).
- Operaciones de fila: $F_2-2F_1\to F_2$; equivalencia por filas con $\sim$ o `\xrightarrow{}`.
- Cada lección que use $C_{BB'}$ o $M(T)_{BB'}$ incluye un aviso `:::caution[Notación de los libros]`
  con la equivalencia: Poole y Lay escriben $P_{B'\leftarrow B}$ y $[T]_{B'\leftarrow B}$
  (subíndices en orden inverso). La tabla completa vive en `/algebra-ii/notacion/`.

## 5. Fórmulas (KaTeX)

- Inline `$...$`. Bloques con `$$` **solos en su línea**, línea en blanco antes y después:

  ```markdown
  $$
  A=\begin{pmatrix}1&2\\0&1\end{pmatrix}
  $$
  ```

- Nunca `$$` en la misma línea que texto. Nunca `\(` `\)` ni `\[` `\]`. No usar `\newcommand`.
- Matriz ampliada: `\left(\begin{array}{cc|c} 1&2&3\\0&1&4 \end{array}\right)`.
- Operadores: `\operatorname{gen}`, `\operatorname{Nu}`, `\operatorname{Im}`, `\operatorname{nul}`,
  `\operatorname{col}`, `\operatorname{fil}`, `\operatorname{rango}`, `\operatorname{tr}`,
  `\operatorname{proy}`, `\operatorname{diag}`. Llaves de conjunto: `\{ \}`.
- **No poner fórmulas con `|` dentro de tablas Markdown** (rompe la tabla). En tablas, fórmulas simples.
- Sistemas: `\begin{cases} ... \end{cases}`. Alineación: `\begin{aligned} ... \end{aligned}`.
- Los `$` literales (precios) se escriben `\$`.

## 6. Estructura de una lección

No es una plantilla rígida; se usan las partes que el tema necesita, en este orden aproximado:

1. **Motivación** (sin título o `## Para qué sirve`): qué problema resuelve el concepto. Si existe,
   un vínculo concreto con la informática.
2. **Intuición** antes del formalismo, preferentemente con una figura o un ejemplo chico.
3. **Definiciones y resultados**: `:::note[Definición]`, `:::note[Teorema]`, `:::note[Propiedad]`
   (título en español, con nombre si lo tiene: `:::note[Teorema de la dimensión]`).
4. **Demostraciones** de los resultados centrales del programa (criterio de subespacio, unicidad de
   coordenadas, núcleo/imagen son subespacios, teorema de la dimensión, teorema fundamental,
   autovectores de autovalores distintos son LI, $m_g\le m_a$ cuando sea razonable, criterio de
   diagonalización, $A^k=CD^kC^{-1}$, Cauchy-Schwarz, ortogonales no nulos son LI, Gram-Schmidt,
   $\dim S+\dim S^\perp=n$, mejor aproximación, ecuaciones normales, distancia mínima y corrección
   de errores). Formato: `**Demostración.**` seguido del argumento y `$\blacksquare$` al final.
5. **Ejemplos resueltos** completos (`### Ejemplo k · título`), con cada paso justificado y una
   comprobación final ("Comprobación: ..."). Como mínimo dos por lección, uno de ellos no trivial.
   Cuando hay dos métodos, mostrar ambos y decir cuál conviene.
6. **Interpretación** geométrica, algebraica o computacional.
7. **Errores frecuentes** en `:::caution[Errores frecuentes]` con contraejemplos concretos.
8. **Autoevaluación** breve opcional (2–4 preguntas con respuesta en `<details>`).
9. **Resumen** en `:::tip[En resumen]` con los resultados esenciales.
10. **Para profundizar**: referencias bibliográficas (sección del libro) y enlaces a lecciones
    relacionadas (anteriores y siguientes) y al repaso que corresponda.

Extensión orientativa: lo que el tema necesite para estudiarse sin otra fuente (típicamente
1500–3500 palabras por lección). Nada de frases de relleno ("es muy importante", "como vimos").
Español de Argentina, registro académico claro. Explicaciones en primera persona del plural
("calculamos", "observemos"); si se interpela al lector, con voseo ("probá", "observá").
Enunciados de ejercicios en infinitivo, como la cátedra ("Hallar", "Probar", "Decidir si").

## 7. Ejercicios (páginas de práctica y simulacros)

Cada ejercicio:

```markdown
### Ejercicio 7 · Base de un subespacio de matrices
<!-- ejercicio: U1.07 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $S=\{A\in\mathbb{R}^{2\times 2}: \dots\}$. Hallar ...
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Qué método se usa y por qué.

Desarrollo paso a paso, justificando cada igualdad...

**Comprobación.** ...

:::tip[Resultado]
$B_S=\{\dots\}$, $\dim S=2$.
:::

</details>
```

- Identificadores: `U1.01`…`U1.nn` (unidad 1), `U2.01`…, `U3.`, `U4.`; repaso `R.01`…;
  simulacros `S1.1`…, `S2.1`…. Únicos en toda la materia; numeración continua dentro de la unidad
  a lo largo de las cuatro páginas de práctica (inicial 01–, intermedio sigue, etc.).
- `nivel`: `inicial`, `intermedio` o `avanzado`. `tipo`: `calculo`, `conceptual`, `demostracion`,
  `verdadero-falso`, `contraejemplo` o `aplicacion`. `verificacion`: `sympy` si la resolución contiene
  cuentas comprobables (se registra una comprobación con el mismo identificador) o `razonamiento`
  si es una demostración o argumento sin cuentas.
- Mínimos por unidad: **24 ejercicios** (≥ 7 iniciales, ≥ 9 intermedios, ≥ 6 avanzados) **más**
  la guía integradora (4–6 problemas de varios ítems estilo parcial, también con identificador).
  Cada unidad incluye al menos: 2 verdadero/falso justificados, 2 contraejemplos, 2 demostraciones,
  2 aplicaciones informáticas, 1 con parámetro.
- Resoluciones completas: estrategia, desarrollo, comprobación y resultado. En V/F, justificar con
  demostración o contraejemplo explícito.
- Al inicio de cada página de práctica: qué lecciones presupone (enlaces) y cómo usar la página.
- Datos "lindos" pero no triviales: enteros chicos, autovalores enteros, normas exactas.

## 8. Verificación matemática

- Toda cuenta de un ejercicio con `verificacion: sympy` y de cada ejemplo resuelto numérico se
  comprueba en `academic-sources/algebra-ii/checks/<archivo>.py` con el decorador
  `content_pipeline.mathcheck.check`. Un archivo por autor/sección para evitar conflictos:
  `repaso.py`, `u1_teoria.py`, `u1_practica.py`, `u2_teoria.py`, … `simulacros.py`.
- Identificadores de comprobación: el del ejercicio (`U1.07`) o, para ejemplos de teoría,
  `U1.T03.E2` (unidad 1, lección 3, ejemplo 2). En la página, junto al ejemplo, el comentario
  `<!-- check: U1.T03.E2 -->`.
- Cada comprobación **recalcula** el resultado desde los datos del enunciado (no solo compara
  con un número escrito a mano) y verifica también los pasos intermedios que se publican
  (escalonamientos, polinomios característicos, autovectores, proyecciones).
- Sobre $\mathbb{Z}_2$ usar `gf_rref`, `gf_rank`, `gf_nullspace`, `gf_matmul`, `gf_span`,
  `hamming`, `weight`, `min_distance`, `gf_dot` (aritmética modular exacta). Nunca reales.
- Plantilla:

  ```python
  import sympy as sp
  from content_pipeline.mathcheck import check, require, same, gf_rank

  @check("U1.07", "Base de un subespacio de matrices", page="/algebra-ii/unidad-1/practica/nivel-intermedio/")
  def _():
      A = sp.Matrix([[1, 2], [3, 4]])
      same(A.det(), -2, "determinante")
      require(gf_rank([[1, 1], [1, 1]], 2) == 1, "rango en Z2")
  ```

- Las demostraciones no se "verifican" con SymPy: se revisan hipótesis, casos borde y
  contraejemplos. Una afirmación V/F falsa se acompaña de un contraejemplo verificado.
- Mientras SymPy no esté instalado, las cuentas se comprueban con `fractions.Fraction` de la
  biblioteca estándar en un script temporal y se deja escrita la comprobación SymPy definitiva.

## 9. Figuras

- SVG en línea dentro de `<figure class="math-figure">`, sin líneas en blanco dentro del bloque
  (una línea en blanco corta el HTML en Markdown). Accesible: `role="img"`, `<title>` y `<desc>`
  con `aria-labelledby`, y `<figcaption>` que explique qué mirar.
- Colores **solo** por clase (definidas en `src/styles/custom.css`): `grid`, `axis`, `guide`,
  `vec-a`…`vec-d` / `line-a`…`line-d` (trazos), `head-a`…`head-d`, `head-muted` (puntas de flecha),
  `dot-a`…`dot-d`, `region-a`, `region-b`, y `text`, `text.math` (cursiva), `text.small`.
  Nunca colores fijos (`#000`, `black`, `red`) ni `style=`.
- Ids únicos por página (prefijo con el slug de la lección: `cb-arrow-a`).
- Coordenadas: el eje $y$ del SVG apunta hacia abajo; usar `transform="scale(1,-1)"` en un grupo para
  dibujar y escribir el texto fuera de ese grupo (si no, queda espejado). Verificar que cada vector
  dibujado corresponda exactamente a los datos del texto.
- Plantilla mínima:

  ```html
  <figure class="math-figure">
  <svg viewBox="-120 -120 240 240" role="img" aria-labelledby="cl-t cl-d" xmlns="http://www.w3.org/2000/svg">
  <title id="cl-t">Combinación lineal en el plano</title>
  <desc id="cl-d">Los vectores u=(2,1) y v=(1,2) y su suma u+v=(3,3), con el paralelogramo.</desc>
  <defs><marker id="cl-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker></defs>
  <g transform="scale(1,-1)">
  <line class="axis" x1="-110" y1="0" x2="110" y2="0"/>
  <line class="axis" x1="0" y1="-110" x2="0" y2="110"/>
  <line class="vec-a" x1="0" y1="0" x2="60" y2="30" marker-end="url(#cl-arrow-a)"/>
  </g>
  <text class="math" x="64" y="-30">u</text>
  </svg>
  <figcaption>Qué muestra la figura y qué hay que observar.</figcaption>
  </figure>
  ```

- Diagramas de flujo o mapas conceptuales: cercos ```` ```mermaid ````.
- Visualizaciones mínimas esperadas: combinación lineal y generado (U1), dependencia lineal en el
  plano (U1), base no canónica y coordenadas sobre una grilla oblicua (U1), cambio de coordenadas
  (U1), imagen de una grilla por una TL y núcleo (U2), autovectores como direcciones invariantes
  (U3), proyección ortogonal sobre una recta y un plano (U4), Gram-Schmidt en dos pasos (U4),
  recta de cuadrados mínimos con residuos (U4).

## 10. Avisos y callouts

Solo los nativos: `:::note`, `:::tip`, `:::caution`, `:::danger`, siempre con título en español.
Usos: `note` definiciones, teoremas, enunciados; `tip` resultados, resúmenes, consejos;
`caution` errores frecuentes y notación de libros; `danger` solo para errores graves de concepto.

## 11. Prohibido

- Texto provisional ("TODO", "en construcción", "próximamente", "completar").
- Enunciados presentados como de parciales oficiales. Los simulacros dicen que son **originales**.
- Imágenes decorativas, emojis, colores fijos, MathJax, HTML con `style=`.
- Afirmar que un resultado está verificado sin comprobación registrada.
- Cambiar archivos fuera de los asignados.
