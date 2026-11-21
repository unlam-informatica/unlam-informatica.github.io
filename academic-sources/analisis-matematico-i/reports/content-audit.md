# Auditoría de los apuntes existentes — Análisis Matemático I

Fecha: 2026-11-21. Alcance: las 85 páginas que el portal tenía antes de esta etapa (teoría, presentaciones, prácticas
y GeoGebra), contrastadas con el programa 2C2026, los apuntes de la cátedra (Williner) y la Guía de Trabajos
Prácticos 2026, incluidas sus respuestas oficiales.

## Método

1. **Cobertura:** cada tema de `curriculum-map.yaml` se buscó en las páginas existentes y se calificó como completo,
   parcial, superficial o ausente (campo `audit` de la matriz; `coverage_after` es el estado después de las lecciones nuevas).
2. **Corrección matemática de las prácticas:** cada resultado calculable de las resoluciones existentes se recalculó
   con SymPy (comprobaciones `U<n>.A.*` en `checks/u<n>_auditoria.py`, 175 en total) y se contrastó con la respuesta
   oficial de la guía. Los límites se comprobaron por ambos laterales.
3. **Discrepancias con la respuesta oficial:** se verificaron mirando el enunciado en el **PDF renderizado** de la
   guía, no en su capa de texto (que pierde exponentes, índices de raíces y el alcance de raíces y potencias).
   Esta revisión mostró que dos de las «respuestas oficiales erróneas» que declaraban las páginas eran, en realidad,
   **errores de transcripción del enunciado en el portal**.

## Resumen

| Unidad | Cobertura antes | Errores corregidos en páginas existentes | Respuestas oficiales erróneas (con evidencia) |
|---|---|---|---|
| 1 · Funciones | 5 temas completos, 3 parciales, 1 superficial | Adicional 1c (dominio); 9l (enunciado mal transcripto; la oficial era correcta); adicionales 1a–1b (presentados como discrepancia sin serlo) | 9j y 9k (respuestas intercambiadas) |
| 2 · Límite y continuidad | Teoría resumida: la mayoría de los temas parciales | 25a y 25c (asíntotas con parámetros); 16e (enunciado mal transcripto: es una potencia; la oficial 1/4 era correcta) | 2b (raíz cuadrada; la oficial usa cúbica); 25c («no existe b con una sola AV»: falso para b = a²) |
| 3 · Derivada | Teoría resumida: temas parciales | Ej. 14 (ordenada de P₁); 42d (contraejemplo inválido); 42 (borrador a la vista); 5c (redacción precisada: cúspide con tangente vertical) | 6e (derivada de √(5x³)); 42k (la oficial da V; es F) |
| 4 · Taylor | Temas parciales; término complementario superficial | 15b (veredicto contradictorio con su justificación); 3b y Adicional 4 (discrepancias espurias) | 15b (la oficial omite una afirmación verdadera) |

Otros hallazgos transversales:

- **Residuos de la migración:** «## Tabla de contenidos / 1. TOC» (marcador de Jekyll que se publicaba como texto) en
  cuatro páginas; retirado. Un acento grave suelto en el índice de la Práctica 1; retirado.
- **Presentaciones de unidad:** la de la Unidad 2 decía que Continuidad se evalúa en el **segundo** parcial; según las
  consideraciones 2C2026 se evalúa en el **primero**. Corregido al reescribir las presentaciones (las tablas de temas se
  conservan, con la notación de entornos y la clasificación de discontinuidades de la cátedra).
- **Atribución:** las prácticas reproducen los enunciados de la Guía 2026 y decían «copiado literal del PDF» o citaban
  una ruta de archivo local. Se reemplazó por una nota de fuente con la atribución a la cátedra (decisión D2).
- **GeoGebra:** contenido correcto y vigente. La sección de optimización (máximos, mínimos, inflexiones) excede el
  programa 2026 y se rotuló como complementaria. Los comandos no se pudieron ejecutar en GeoGebra en este entorno.
- **Notación:** el resumen de la Unidad 2 usa $V(a,\delta)$ para el entorno y el de la Unidad 3 usa `\sin`; se conservan
  (son notaciones equivalentes) y las lecciones usan la notación de la cátedra ($E(a, r)$, $\operatorname{sen}$).

## Revisión de coordinación

Verificación de las «discrepancias con la respuesta oficial» declaradas en las páginas existentes, contra el PDF de la guía renderizado (pypdfium2):

| Página | Declarado | Hallazgo con el PDF | Acción |
|---|---|---|---|
| u1 ejercicio-9 (9j, 9k) | oficial errónea | Correcto: la guía publica las respuestas de j y k intercambiadas | Se mantiene la nota |
| u1 ejercicio-9 (9l) | oficial errónea | **Error de transcripción del portal**: el primer tramo es √(x−1)/(x−3), no √((x−1)/(x−3)); la oficial [1,5)−{3} es correcta | Enunciado y resolución corregidos; regresión U1.A.E09.l |
| u1 adicionales 1a, 1b | «discrepancia con el documento» | No hay discrepancia: son afirmaciones de V/F que resultan falsas | Reescrito como «Respuesta: Falso» con justificación |
| u2 ejercicio-2 (2b) | oficial errónea (raíz cúbica) | Correcto: el enunciado tiene raíz cuadrada | Se mantiene |
| u2 ejercicio-16 (16e) | oficial errónea (1/12 frente a 1/4) | **Error de transcripción del portal**: es una potencia (√((1−x)/(1−64x)))^((1+2x)/(3x−1)), no un producto; la oficial 1/4 es correcta | Enunciado y resolución corregidos; regresión U2.A.E16.e |
| u2 ejercicio-25 (25c) | oficial errónea («no existe b con una sola AV») | Correcto: con b = a² el numerador x(ax+1) y el denominador comparten la raíz −1/a, que queda como hueco | Se mantiene |
| u3 practica-3 (6e) | oficial errónea | Verificado por el agente de la unidad con el PDF renderizado | Se mantiene |
| u3 practica-3 (42k) | oficial errónea (dice V) | Correcto: «si f′(a) existe, f′ es continua en a» es falso (x² sen(1/x)) | Se mantiene |
| u3 practica-3 (5c) | corrección del agente: «cúspide, no hay recta tangente» | Discutible: las secantes por el origen tienden a la recta x = 0 desde ambos lados | Reescrito: cúspide (punto de retroceso) con tangente vertical x = 0, no derivable; la lección derivada-como-funcion ajustada igual |

Otras revisiones: correcciones de U3 ej. 14 y 42d y de U2 ej. 25a verificadas a mano (correctas).

## Unidad 1 · Funciones

Páginas leídas: `unidad-1/index.md`, `teoria/unidad-1.md` (925 líneas), `practica/practica-1.md`, `ejercicio-1` a `ejercicio-32`, `adicionales.md`. Resultados contrastados con las respuestas oficiales de la Guía de TP 2026 y recalculados con SymPy en `checks/u1_auditoria.py` (67 comprobaciones, IDs `U1.A.E<nn>.<k>`, todas pasan).

#### Hallazgos

| Página | Fragmento | Tipo | Explicación | Acción | Prioridad |
|---|---|---|---|---|---|
| adicionales.md | Adicional 1c: «dominio $(-4,4)\setminus$… simétrico» | error-matematico | El dominio de $x^3/(16-x^2)$ es $\mathbb{R}-\{-4,4\}$, no un subconjunto de $(-4,4)$ (el texto estaba truncado). La conclusión (impar) era correcta. | **Corregido** (cambio mínimo) con regresión `U1.A.ADIC.1` | media |
| ejercicio-9 (9j) | página: $(-\infty,-1)\cup[4/3,\infty)$; oficial: $[4/3,\infty)$ | discrepancia: respuesta oficial errónea | Para $\sqrt{(3x-4)/(x+1)}$, $x=-2$ da cociente $10\ge0$. | No se cambia. Evidencia `U1.A.E09.j`, `U1.A.E09.j.oficial` | alta (informativa) |
| ejercicio-9 (9k) | página: $[4/3,\infty)$; oficial: $(-\infty,-1)\cup[4/3,\infty)$ | discrepancia: respuesta oficial errónea | Para $\sqrt{3x-4}/\sqrt{x+1}$ hace falta $3x-4\ge0$. Las oficiales de 9j y 9k parecen intercambiadas. | No se cambia. Evidencia `U1.A.E09.k` | alta (informativa) |
| ejercicio-9 (9l) | enunciado transcripto como $\sqrt{\frac{x-1}{x-3}}$; en la guía es $\frac{\sqrt{x-1}}{x-3}$ | error-matematico (transcripción) | La página resolvía otro enunciado y declaraba errónea la respuesta oficial $[1,5)-\{3\}$, que es correcta (revisión de coordinación con el PDF renderizado). | Enunciado y resolución corregidos; regresión U1.A.E09.l | alta | corregido |
| ejercicio-12 | Enunciado «miles de euros» vs. 11 250 000 € / oficial «millones» | otro | La guía es inconsistente en unidades; la página lo explica en 12c. | Sin cambios. | baja |
| ejercicio-10g | Enunciado de la guía pierde el exponente | otro | La respuesta oficial corresponde a $2^{x+1}$, que es lo que usa la página. | Sin cambios; `U1.A.E10.g`. | baja |
| ejercicio-20 | $-e^{2x+3}+1$: «compresión horiz., refl., 1 arriba» | incompleto | Omite el desplazamiento horizontal $3/2$ a la izquierda ($e^{2(x+3/2)}$). | Sin cambios (la coordinación decide; no es error de resultado). | baja |
| ejercicio-19 | «≈165 días» | redaccion | $0{,}4537\cdot365\approx165{,}6$: entre 165 y 166. | Sin cambios. | baja |
| teoria/unidad-1.md | §13 transformaciones | superficial | No trata $a\,f(b(x-c))+d$ ni el orden de los movimientos; §9.2 acotación sin ejemplos; §3 razón de cambio sin demostración. | Cubierto en las lecciones nuevas. | media |
| teoria/unidad-1.md | §15.2 propiedad gráfica sin demostración; trig inversas sin valores | superficial | | Cubierto en `inversa` y `funciones-elementales`. | media |
| practica-1.md | Texto «enunciado copiado literal del PDF»; fila con `` ` `` suelta tras la tabla (`|------|-----------|` + `` ` ``) | redaccion | Renderizado defectuoso de la tabla y mención al PDF. | No tocado (restricción: solo errores matemáticos). Aviso a la coordinación. | media |
| index.md | «1er parcial» | otro | El programa 2026 evalúa u1–u2 en el primer parcial. Coincide. | Sin cambios. | — |

Resultados verificados sin discrepancia (respuestas oficiales): 1a–g, 2a–d, 3, 4, 5, 6, 7, 8, 9a–i, 9m–ñ, 10a–g, 11a–d, 12, 13 (pares a,f,i,j; impares c,e,g), 16a–d, 17, 18, 19, 21, 24–31, 32 (V: a,j,k), 26a–g (incluidas ambas ramas de 26e), Adicionales 1–8.

#### Cobertura por tema de la matriz

| Tema | Antes (existente) | Después (lecciones) |
|---|---|---|
| u1-funcion | completo | completo (`funciones-y-modelos`) |
| u1-modelos | parcial | completo (lineal, cuadrático, exponencial, periódico, razón de cambio media según D5) |
| u1-ceros-signo | parcial | completo (`caracteristicas`) |
| u1-paridad | completo | completo, con propiedades y descomposición |
| u1-acotada | superficial | completo, con ejemplos y cotas |
| u1-elementales | completo | completo, con gráficos (`funciones-elementales`) |
| u1-algebra | completo | completo (`algebra-y-transformaciones`) |
| u1-transformaciones | parcial | completo ($a f(b(x-c))+d$, qué cambia) |
| u1-inversa | completo | completo, con demostraciones (`inversa`) |

#### Calidad y errores

Las prácticas existentes son matemáticamente correctas salvo el error de redacción del Adicional 1c (corregido). Las discrepancias 9j y 9k son errores de la respuesta oficial (respuestas intercambiadas). La de 9l era un error de transcripción del enunciado en el portal (ver «Revisión de coordinación»): se corrigió y la respuesta oficial es correcta. Dos errores corregidos (Adicional 1c, 9l); dos discrepancias con la respuesta oficial registradas.

## Unidad 2 · Límite funcional y continuidad

Comprobaciones: `academic-sources/analisis-matematico-i/checks/u2_auditoria.py` (33 comprobaciones, IDs `U2.A.<página>.<k>`).
Referencia: respuestas oficiales de la Guía de TP 2026 . Los límites se comprobaron con ambos laterales y contraste numérico.

#### Hallazgos

| Página | Fragmento | Tipo | Explicación | Acción | Prioridad |
|---|---|---|---|---|---|
| practica/ejercicio-25 (25a) | «El "k" pedido suele ser el resto/parámetro asociado… (valor que cierra el sistema de la consigna original)» | error-matematico | $k$ es el punto excluido del dominio $\mathbb{R}-\{k\}$, es decir $-b/a=-8$; no es un resto ni un parámetro de «cierre». | **Corregido** (cambio mínimo). Regresión: `U2.A.E25.a`. | alta |
| practica/ejercicio-25 (25c) | «si $b=0$ … (parábola, sin AV ni AH, AO si $a\neq0$)» | error-matematico | Con $b=0$, $f(x)=-ax^2-x$ es una parábola: no tiene AO. La respuesta oficial lo dice («no tiene asíntotas»). Solo $a=0$ da la recta $y=-x$. | **Corregido**. Regresión: `U2.A.E25.c`. | alta |
| practica/ejercicio-25 (25c) | respuesta oficial «No existe valor de $b$ para el cual tenga una sola AV» | discrepancia: respuesta oficial errónea (incompleta) | Con $b=a^2$ ($a\neq0$): $f=\frac{x(ax+1)}{(ax-1)(ax+1)}=\frac{x}{ax-1}$, una sola AV ($x=1/a$) y hueco en $x=-1/a$. Ej.: $a=2$, $b=4$. | No se cambia la página (la página ya menciona la cancelación); registrado. Evidencia: `U2.A.E25.c`. | media |
| practica/ejercicio-25 (25b) | «…tomamos $x^2+bx+c=(x+1)^2$… pero verifiquemos con AO…» | redaccion | Resolución con un intento descartado a la vista; el resultado $a=-2,b=0,c=-1$ es correcto (`U2.A.E25.b`). | Registrado para la coordinación. | baja |
| practica/ejercicio-16 (16e) | «Discrepancia: resultado calculado $\frac1{12}$, respuesta oficial $\frac14$» | otro (fuente ilegible) | La capa de texto de la guía pierde el índice del radical. Con raíz cuadrada da $\frac1{12}$ (la página), la oficial $\frac14=\sqrt[3]{1/64}$ solo se obtiene si el índice es 3 y el resto tiende a 1; no se puede decidir sin ver el PDF. No se cambia. | Registrado; evidencia `U2.A.E16.e`. | media |
| practica/ejercicio-20 (20d) | «$\frac{2}{0}=\infty$» y «el límite global es $\infty$ en valor absoluto» | notacion | Se escribe una forma sin valor como igualdad y el límite bilateral **no existe** (laterales $-\infty$ y $+\infty$; `U2.A.E20.a`). La respuesta oficial dice «$\infty$». | Registrado. | media |
| practica/ejercicio-33 (33g) | justificación «el enunciado se considera falso… siguiendo la respuesta oficial» | incompleto | La respuesta (Falso) es correcta; falta el contraejemplo: $f(x)=1/\lvert x-1\rvert$ si $x\neq1$, $f(1)=0$ tiene AV en $1$ y $1\in D_f$ (`U2.A.E33.a`). | Registrado. | media |
| practica/adicionales (Adicional 4) | «Según la respuesta oficial… $a=\frac32$, $b=-\frac92$» | otro (atribución) | El texto de la guía no incluye respuestas de los adicionales. El valor es correcto si el tramo $x<1$ es $\frac{x^2+4x-5}{2x^2-6x+4}$ (lectura plausible; límite $-3$): `U2.A.ADI.4`. | Registrado: la atribución no se pudo contrastar. | media |
| practica/adicionales (A1c, A2, A5, A7) | resoluciones sin enunciado de opciones o con «discusión por casos» | superficial | A2, A5 y A7 no se resuelven (falta enunciado); A1c es VERDADERO interpretando $x\to\infty$ como ambos extremos. | Registrado. | baja |
| practica/ejercicio-4, 22 y 27 | «Como no disponemos de los gráficos…» | incompleto | Dependen de gráficos no reproducidos; solo se recuerda el método y la respuesta oficial. | Registrado (D2: sin material nuevo). | baja |
| teoria/unidad-2 | entornos $V(a,\delta)$, $\dot V$ | notacion | La matriz fija $E(a,r)$, $E^{*}(a,r)$. | Lo resuelve la coordinación (resumen integrador). | baja |
| teoria/unidad-2 §13 | tabla «De salto (1ª especie)» y «Esencial (2ª especie): algún lateral no existe o es $\pm\infty$» | notacion | La clasificación de la cátedra/matriz es evitable / esencial de salto finito / esencial de salto infinito. Un lateral infinito es salto infinito, no «2ª especie». | Las lecciones usan la clasificación de la matriz; el resumen lo resuelve la coordinación. | media |
| teoria/unidad-2 §12 | «TVI: $f$ toma todos los valores entre $f(a)$ y $f(b)$» | incompleto | Falta la hipótesis «continua en $[a,b]$» en la viñeta (está solo en el título); D4: los teoremas son complementarios. | Registrado. | baja |
| teoria/unidad-2 §11 | «L'Hôpital (U3)» | otro | Referencia adelantada; correcto pero no figura en el programa de la unidad. | Registrado. | baja |

#### Resultados de la práctica contra las respuestas oficiales

Recalculado con SymPy y coincide con la guía: ej. 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 (salvo 16e), 17, 18, 19, 20, 21, 24, 25a-b, 26, 28, 29, 31, 32, 33 (f, j, l y contraejemplos).
Notas: 1, 4, 22, 23 y 27 dependen de gráficos (no recalculables). 30 y adicionales 2, 5, 7 no tienen resultado único.

**Alerta SymPy.** `sp.limit(3**(1/x), x, 0, dir="-")` devuelve `oo` (correcto: `0`) y `sp.limit(Rational(1,3)**(1/x), x, 0, dir="+")`/`"-"` devuelve `0` en ambos lados (correcto: `0` y `+oo`). Se reescriben las potencias como `exp(log(base)*exponente)` en todas las comprobaciones (`U2.A.E17.a`).

#### Cobertura por tema de la matriz (antes → después de las lecciones)

| Tema | Antes | Después |
|---|---|---|
| u2-entorno | completo | completo (`entornos-y-limite`) |
| u2-limite-finito | superficial | completo (ε-δ, 5 ejemplos, refutación) |
| u2-laterales-propiedades | completo | completo (unicidad y suma demostradas, intercalación demostrada, sen x/x) |
| u2-infinitesimos | parcial | completo (órdenes, equivalencias, principio de sustitución con contraejemplo) |
| u2-limites-infinitos | parcial | completo (3 definiciones, operaciones, jerarquía) |
| u2-calculo | parcial | completo (diagrama de decisión, número e, regla $1^\infty$ demostrada) |
| u2-asintotas | parcial | completo (AV/AH/AO por extremo, modelos) |
| u2-continuidad | parcial | completo (autocontenida; Bolzano/VI/Weierstrass con contraejemplos, D4) |
| u2-discontinuidades | parcial | completo (clasificación, salto, redefinición) |

Calidad de las páginas existentes: buena (resoluciones paso a paso y verificadas), con dos errores matemáticos corregidos (ej. 25) y varios puntos de redacción/notación.

## Unidad 3 · Derivada

Comprobaciones: `academic-sources/analisis-matematico-i/checks/u3_auditoria.py` (50, IDs `U3.A.E<kk>` / `U3.A.AD<k>`), todas aprobadas.

| Página | Fragmento | Tipo | Explicación | Acción | Prio |
|---|---|---|---|---|---|
| practica-3 | Ej. 14, P1 ≈ (−2,861; 3,303) | error-matematico | La ordenada exacta (2+⁴√12)/(−⁴√12) vale −2,075, no 3,303 (U3.A.E14) | CORREGIDO a −2,075 | alta |
| practica-3 | Ej. 42d, contraejemplo y=x³ en 0 | error-matematico | La tangente a x³ en 0 (y=0) solo corta en 0: no es contraejemplo | CORREGIDO: tangente a 1/x² en (1,1), corta en (−1/2,4) (Ej. 13b) | alta |
| practica-3 | Ej. 42, línea «Verdaderas: c, e, h, j, k... ¡revisar!» | error-matematico/redaccion | Contradice la lista final (k es falsa) y deja texto de borrador | ELIMINADA | media |
| practica-3 | Ej. 5c, «tangente vertical» para x^(2/3) | error-matematico | Laterales −∞ y +∞: cúspide, sin tangente (la respuesta oficial también dice «tangente vertical») | CORREGIDO en la página (cúspide) | media |
| practica-3 | Resumen de discrepancias, 6e | — | Confirmada: la guía imprime 3√5·x² (verificado en el PDF), la derivada de √(5x³) es (3√5/2)√x | «discrepancia: respuesta oficial errónea», página sin cambios | — |
| practica-3 | Resumen de discrepancias, 42k | — | Confirmada: k es Falsa (x² sen(1/x)); la oficial la marca Verdadera | «discrepancia: respuesta oficial errónea», sin cambios | — |
| practica-3 | Ej. 1–42 y adicionales 1–6 restantes | — | Recalculados con SymPy (derivadas, tangentes, parámetros, implícitas, logarítmicas, movimiento) | sin hallazgos | — |
| practica-3 / unidad-3 | «## Tabla de contenidos / 1. TOC» | redaccion | Residuo de la importación | coordinación | baja |
| teoria/unidad-3 | `\sin`, `\arcsin` en vez de `\operatorname{sen}` | notacion | No sigue la guía §4 | coordinación (resumen integrador) | baja |
| teoria/unidad-3 | Sin demostraciones, hipótesis de la inversa, ni condición f>0 en derivación logarítmica | incompleto/superficial | Cubierto por las lecciones nuevas | coordinación enlaza | media |
| unidad-3/index | Tabla de temas sin enlaces a las lecciones | enlace | Falta navegación | coordinación | media |

Cobertura por tema (antes → ahora): razón de cambio, derivada en un punto, función derivada, reglas, cadena, inversa, implícita, logarítmica: parcial/superficial → completo (lecciones nuevas). Diferencial: complementario (nota breve).

## Unidad 4 · Polinomios de Taylor

| Página | Fragmento | Tipo | Explicación | Acción | Prioridad |
|---|---|---|---|---|---|
| practica-4, Ej. 3b | «Discrepancia» sobre ln(0,4) | redaccion | No era una discrepancia: la oficial da solo P3 y coincide | Reemplazada por nota | media |
| practica-4, Ej. 15b | «Falso» con justificación que dice que lo verdadero es falso, y supone error de transcripción | error-matematico | El PDF dice f^(6)(0)/6!: es verdadero; la oficial marca falso | Corregido a Verdadero y registrado «discrepancia: respuesta oficial errónea» (U4.A.E15.b) | alta |
| practica-4, Adicional 4 | «Discrepancia», «pista S={1±√13}», «no puede verificarse la opción e)» | redaccion | El enunciado impreso trae las opciones; S={-1±√13} es la e); la d) es {1±√13}. La lista de respuestas oficiales no incluye los adicionales 4 y 5 | Reemplazada por nota (U4.A.A4) | media |
| practica-4, nota final | Citaba las tres discrepancias | redaccion | Actualizada | corregida | baja |
| teoria/unidad-4 §1, §3 | «único polinomio con contacto de orden n» | notacion | El Taylor de orden n tiene contacto al menos n (exacto n solo si f^(n+1)(a)≠0) | Corregido en las lecciones; resumen sin tocar | media |
| teoria/unidad-4 §1 | equivalencia por límites sin hipótesis | incompleto | Requiere n+1 derivadas en a | Tratado en orden-de-contacto | baja |
| geogebra/taylor | `PolinomioTaylor(f; a; n)` con punto y coma | otro | Fuera de mi alcance | Avisar a coordinación | baja |
| unidad-4/index | Sin lecciones ni integradores | enlace | Navegación a cargo de coordinación | — | media |
| Ej. 1–15 resto | Resultados | — | Los 15 ejercicios y 5 adicionales recalculados con SymPy (24+ checks), coinciden salvo lo anterior | — | — |

Cobertura por tema de la matriz (antes -> ahora): u4-orden-de-contacto parcial -> completo; u4-polinomio-derivadas parcial -> completo; u4-taylor-maclaurin parcial -> completo; u4-aproximacion-lineal parcial -> completo; u4-termino-complementario superficial -> completo.
Calidad: práctica correcta salvo los tres bloques de «discrepancia» (no justificados) y la 15b.
Errores matemáticos corregidos: 15b. Discrepancias con oficial: 15b (oficial errónea).
