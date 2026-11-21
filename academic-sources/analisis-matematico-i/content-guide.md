# Guía de producción — Análisis Matemático I (3622)

Contrato común para redactar, verificar e integrar las páginas de `src/content/docs/analisis-matematico-i/`.
Toda página nueva o reescrita lo cumple. Las decisiones D1–D5 están en `curriculum-map.yaml`.

## 1. Alcance y fuentes

- **Programa de referencia:** «Consideraciones generales 2C2026» de la cátedra (`analisis-matematico-i-5ccac17bb05e`).
  Cuatro unidades: Funciones; Límite funcional (incluye continuidad); Derivada; Polinomios de Taylor. No se
  agregan unidades. Lo que no figura en el programa se rotula como **complementario** (D4).
- **Jerarquía de fuentes:**
  1. Cátedra: programa, apuntes de clase (Williner, 2016), Guía de TP 2026, guía de autoaprendizaje de
     Continuidad, prácticas para parciales.
  2. Bibliografía recomendada por el programa (Stewart, Thomas, Purcell, Larson, Leithold, Piskunov,
     Sadosky-Guber, Apostol). **No está disponible localmente:** se cita sin número de página ni de sección.
- **Las fuentes de cátedra son privadas** (`raw/`, `processed/` no se versionan). Sirven para alinear temas,
  notación, nivel y tipo de ejercicio. **No se copian** párrafos, figuras ni enunciados nuevos (D2). Los
  ejemplos y ejercicios nuevos usan datos propios.
- Las páginas de práctica que ya reproducen la Guía de TP 2026 se conservan con atribución (D2):
  «Enunciado: Guía de Trabajos Prácticos 2026, Práctica N, ejercicio k (cátedra de AM I, DIIT-UNLaM)».
- Ninguna afirmación se atribuye a la cátedra sin fuente. No se inventan programas, fechas ni ediciones.

## 2. Estructura y slugs

- **URL existentes:** se conservan todas. Las páginas `unidad-N/teoria/unidad-N` pasan a ser el
  **resumen integrador** de la unidad sin perder contenido (D3). Las prácticas existentes conservan URL y numeración.
- **Lecciones nuevas** (`unidad-N/teoria/<tema>.md`, slug igual a la ruta):
  - u1: `funciones-y-modelos`, `caracteristicas`, `funciones-elementales`, `algebra-y-transformaciones`, `inversa`.
  - u2: `entornos-y-limite`, `limites-laterales-y-propiedades`, `infinitesimos`, `limites-infinitos`,
    `calculo-de-limites`, `asintotas`, `continuidad`.
  - u3: `razon-de-cambio-y-derivada`, `derivada-como-funcion`, `reglas-de-derivacion`,
    `regla-de-la-cadena-e-inversa`, `implicita-y-logaritmica`.
  - u4: `orden-de-contacto`, `polinomio-de-taylor`, `termino-complementario`.
- **Integradores** de cada unidad: `unidad-N/practica/integradores.md`, con ejercicios originales de estilo parcial.
- Enlaces internos absolutos con barra final: `[asíntotas](/analisis-matematico-i/unidad-2/teoria/asintotas/)`.

## 3. Frontmatter

```yaml
---
title: Asíntotas
description: Asíntotas verticales, horizontales y oblicuas, con el comportamiento en más y menos infinito.
slug: analisis-matematico-i/unidad-2/teoria/asintotas
sidebar:
  order: 6
---
```

`title` corto y sin «Unidad N —» en las lecciones. `description` de una oración.

## 4. Notación

Se prioriza la notación de los apuntes de la cátedra (Williner) cuando es válida.

| Concepto | Notación del sitio | Equivalencias en otras fuentes |
|---|---|---|
| Conjuntos | $\mathbb{R}$, $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ | $R$ (apunte) |
| Función como terna | $f\colon D_f \to \mathbb{R} \,/\, f(x) = \dots$ | $f: A \to B$ |
| Dominio e imagen | $D_f$, $\operatorname{Im} f$ | $\operatorname{Dom} f$, $I_f$, $\operatorname{Rec} f$ |
| Ceros, positividad, negatividad | $C_0$, $C^{+}$, $C^{-}$ | «intervalos de positividad y negatividad» |
| Entorno | $E(a, r) = \{x \in \mathbb{R} : \lvert x - a\rvert < r\} = (a - r, a + r)$ | $E_r(a)$, $(a-\delta, a+\delta)$ |
| Entorno reducido | $E^{*}(a, r) = E(a, r) - \{a\}$ | $E'(a,r)$, entorno perforado |
| Límite | $\lim\limits_{x \to a} f(x) = L$ | — |
| Límites laterales | $\lim\limits_{x \to a^{-}} f(x)$, $\lim\limits_{x \to a^{+}} f(x)$ | — |
| Límite infinito | $\lim\limits_{x \to a} f(x) = +\infty$ (el límite **no existe** como número; se dice que la función diverge) | — |
| Infinitésimos equivalentes | $\varphi(x) \sim \psi(x)$ si $x \to a$ | $\approx$ |
| Seno, tangente | $\operatorname{sen} x$, $\tan x$ | $\sin$, $\operatorname{tg}$ |
| Inversas trigonométricas | $\operatorname{arcsen} x$, $\arccos x$, $\arctan x$ (`\operatorname{arcsen}`, KaTeX no trae `\arcsen`) | $\sin^{-1}$, $\operatorname{arctg}$ |
| Logaritmos | $\ln x$ (natural), $\log x$ (decimal), $\log_a x$ | — |
| Derivada | $f'(a)$, $f'(x)$, $\dfrac{dy}{dx}$ | $Df$, $\dot{x}$ |
| Derivadas laterales | $f'_{-}(a)$, $f'_{+}(a)$ | $f'(a^-)$ |
| Polinomio de Taylor | $P_n(x)$ de orden $n$ centrado en $x = a$ | $T_n$ |
| Término complementario | $R_n(x) = \dfrac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$, con $c$ entre $a$ y $x$ | resto de Lagrange |

- Intervalos con paréntesis y corchetes: $(a, b]$; $(-\infty, 3)$. Los infinitos van siempre con paréntesis.
- Decimales con coma en la prosa (0,5); dentro de fórmulas LaTeX, `0{,}5` para que la coma no agregue espacio.
- Fórmulas en línea `$...$`; bloques con `$$` en líneas separadas (remark-math). Sin `\begin{align}` dentro de
  `$...$`. `\dfrac` en bloques, `\frac` en línea.
- Funciones por tramos con `\begin{cases} … \end{cases}` y la condición con «si»: `x^2 & \text{si } x < 1`.

## 5. Convenciones matemáticas

- **Límites.** Antes de calcular, se indica el tipo de expresión que aparece al sustituir
  ($\frac{0}{0}$, $\frac{\infty}{\infty}$, $\infty - \infty$, $0 \cdot \infty$, $1^{\infty}$, $0^0$, $\infty^0$) o
  que no hay indeterminación. Nunca se escribe una igualdad con una expresión indefinida como si fuera un número
  (no «$= \frac{0}{0}$»: se escribe «al sustituir se obtiene la forma $\frac{0}{0}$»). Los límites laterales se
  calculan cuando la función cambia de expresión, hay valor absoluto o un cociente con denominador que se anula.
- **Continuidad.** Las tres condiciones (existe $f(a)$; existe el límite; son iguales). En un intervalo cerrado
  $[a, b]$: continua en $(a, b)$, por derecha en $a$ y por izquierda en $b$. Clasificación de la cátedra:
  **evitable** (existe el límite finito) y **esencial**: de **primera especie**, de **salto finito** (laterales
  finitos y distintos) o de **salto infinito** (algún lateral infinito), o de **segunda especie** (algún lateral no existe). El **salto** es $\lvert \lim_{x\to a^+} f - \lim_{x\to a^-} f \rvert$.
- **Derivación.** $f'(a) = \lim\limits_{h \to 0} \dfrac{f(a+h) - f(a)}{h}$, que tiene que existir y ser finito. Recta
  tangente $y = f(a) + f'(a)(x - a)$; normal $y = f(a) - \dfrac{1}{f'(a)}(x - a)$ si $f'(a) \neq 0$ (vertical si
  $f'(a) = 0$). Derivable implica continua; la recíproca es falsa ($\lvert x\rvert$ en 0).
- **Taylor.** $P_n(x) = \sum_{k=0}^{n} \dfrac{f^{(k)}(a)}{k!}(x-a)^k$. «Orden» y «grado» se distinguen: el polinomio
  de orden $n$ puede tener grado menor si alguna derivada se anula. El resto se acota con la cota de
  $\lvert f^{(n+1)}\rvert$ en el intervalo entre $a$ y $x$, explicitando ese intervalo.

## 6. Estructura pedagógica de una lección

Usar las partes que el tema necesite, en este orden:

1. **Qué vas a aprender** (objetivos de la matriz) y **antes de empezar** (prerrequisitos con enlaces).
2. **Introducción**: el problema que motiva el concepto (un modelo, una pregunta geométrica o física).
3. **Definiciones** en `:::note[Definición]`, con la notación de §4.
4. **Interpretación intuitiva y geométrica**, con una figura cuando aporte (§8).
5. **Propiedades y teoremas** en `:::note[Teorema]` o `:::note[Propiedad]`: hipótesis explícitas, enunciado y
   qué pasa si falla una hipótesis (contraejemplo). Las demostraciones se rotulan **Demostración** si son
   formales y **Idea de la demostración** o **Por qué funciona** si son intuitivas. No se presenta como
   demostración un argumento gráfico.
6. **Ejemplos resueltos**, progresivos, con todos los pasos y la justificación de cada uno. Cada ejemplo con
   resultado calculable lleva `<!-- check: U<n>.T.<TEMA>.<k> -->` (§7).
7. **Errores frecuentes** en `:::caution[Errores frecuentes]`.
8. **Ejercicios** (§9).
9. **Autoevaluación**: 3 a 5 preguntas cortas con respuesta en `<details>`.
10. **En resumen** en `:::tip[En resumen]` y **Para seguir** con el enlace al tema siguiente.

Español de Argentina, primera persona del plural, voseo al interpelar ("calculá", "observá"). Sin relleno.
Dirigido al estudiante: no se menciona el pipeline, las comprobaciones automáticas ni herramientas internas.

## 7. Verificación matemática

- Las comprobaciones viven en `academic-sources/analisis-matematico-i/checks/u<n>_*.py` con
  `@check("ID", page=...)` de `content_pipeline.mathcheck`, y se ejecutan con `content-pipeline verify-math`.
- Cada comprobación **recalcula** el resultado publicado desde los datos del enunciado (límite, derivada,
  coeficientes de Taylor, dominio, ceros, asíntotas) y verifica además los **pasos intermedios** publicados
  (factorizaciones, racionalizaciones, valores de los límites laterales).
- Estados, siempre diferenciados en el ejercicio con `verificacion:`:
  - `sympy`: resultado comprobado simbólicamente (exacto) con comprobación aprobada.
  - `razonamiento`: el ejercicio es conceptual o una demostración; se revisó matemáticamente pero no hay cálculo
    que comprobar. Una demostración escrita **no** se marca `sympy` aunque alguno de sus pasos se compruebe.
  - Las comprobaciones numéricas (cotas de error, aproximaciones decimales) se hacen con aritmética exacta o
    racional cuando es posible y, si no, con precisión explícita; se dejan registradas como numéricas en la
    descripción del check y nunca reemplazan un resultado exacto que el enunciado pida.
- `sympy.limit` puede fallar o devolver resultados laterales: para límites se comprueban **ambos laterales**
  (`dir="+"` y `dir="-"`) y se contrasta con evaluación numérica cerca del punto cuando la forma es delicada.
- Si una comprobación revela un error, se corrige el contenido y se deja la comprobación como regresión.

## 8. Gráficos

- Sin imágenes decorativas. Un gráfico se incluye cuando muestra algo que el texto no puede: el comportamiento
  cerca de un punto, una asíntota, la recta tangente, la aproximación de Taylor de distintos órdenes.
- Los gráficos nuevos son **SVG generados desde la fórmula** por los scripts de
  `academic-sources/analisis-matematico-i/figures/` (Python estándar, sin dependencias), con salida en
  `public/analisis-matematico-i/figuras/`. Así son reproducibles y matemáticamente fieles. Llevan texto
  alternativo descriptivo y un pie que dice qué observar.
- Los SVG existentes (`/analisis-matematico-i/unidad-1/images/`) se conservan.
- Mermaid solo para diagramas de decisión (por ejemplo, elegir la técnica para un límite).

## 9. Ejercicios

~~~markdown
### Ejercicio 3 · Límite con raíces
<!-- ejercicio: U2.03 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
…
:::

<details>
<summary>Resolución</summary>

**Estrategia.** …

**Desarrollo.** …

**Resultado.** …

</details>
~~~

- **Identificadores** `U1.01`… únicos en la materia; el ID es también el de su comprobación SymPy.
- **`nivel`**: `inicial`, `intermedio` o `avanzado`. Los integradores de estilo parcial llevan `nivel: avanzado` y
  `tipo: integrador`.
- **`tipo`**: `calculo`, `grafico`, `modelado`, `demostracion`, `verdadero-falso`, `opcion-multiple`, `integrador`.
- **Resolución completa**: estrategia, desarrollo con la justificación de cada paso y resultado. En V/F y opción
  múltiple, la justificación de cada opción. No se omiten pasos algebraicos no triviales.
- **Originales**: datos propios. Se pueden inspirar en el tipo de consigna de la guía o de los parciales, sin copiar.
- Mínimos por unidad en `curriculum-map.yaml`. No se agregan ejercicios de relleno.
- Cuando un ejercicio pide usar GeoGebra, se indican los comandos y qué comprobar en el gráfico, y la resolución
  analítica se da igual.

## 10. GeoGebra

La sección `/analisis-matematico-i/geogebra/` se conserva. Las lecciones enlazan su apartado cuando un ejercicio o
un concepto se explora mejor con el software (deslizadores para parámetros, recta tangente, polinomios de
Taylor de distinto orden). Los comandos se escriben como código en línea (`Tangente(1, f)`) y se indica la
versión (GeoGebra Clásico 6 o la calculadora en línea).

## 11. Prohibido

- Presentar un resultado como verificado sin su comprobación aprobada.
- Copiar enunciados o párrafos de la cátedra o de libros (fuera de las prácticas existentes, D2).
- Publicar PDF o material privado, o datos personales.
- Cambiar una URL sin redirección y sin registrar la migración.
- Escribir una forma indeterminada como si fuera un valor.
