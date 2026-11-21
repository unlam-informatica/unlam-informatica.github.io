---
title: Funciones y modelos
description: Definición de función como terna, dominio, imagen y registros de representación; modelado con funciones lineales, cuadráticas, exponenciales y periódicas, y razón de cambio media.
slug: analisis-matematico-i/unidad-1/teoria/funciones-y-modelos
sidebar:
  order: 1
---

## Qué vas a aprender

- Reconocer cuándo una relación entre conjuntos de números reales es una función y escribirla como una terna (dominio, codominio, regla).
- Determinar el dominio y la imagen a partir de la fórmula, de una tabla o de un gráfico, y pasar de un registro de representación a otro.
- Identificar variables, unidades y dominio **en contexto** al modelar un problema.
- Construir modelos lineales, cuadráticos, exponenciales y periódicos a partir de datos o de una descripción.
- Calcular e interpretar la **razón de cambio media** de un modelo en un intervalo.

## Antes de empezar

Necesitás manejar intervalos y valor absoluto, factorización, ecuaciones lineales y cuadráticas y desigualdades sencillas. Si querés un panorama de toda la unidad, está el [resumen de la Unidad 1](/analisis-matematico-i/unidad-1/teoria/unidad-1/). Esta lección es la puerta de entrada: las siguientes la usan todo el tiempo ([características](/analisis-matematico-i/unidad-1/teoria/caracteristicas/), [funciones elementales](/analisis-matematico-i/unidad-1/teoria/funciones-elementales/), [álgebra y transformaciones](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/) e [inversa](/analisis-matematico-i/unidad-1/teoria/inversa/)).

## Introducción: una relación entre dos magnitudes

Un tanque tiene 80 litros y se llena con una canilla que aporta 12 litros por minuto. Si $t$ es el tiempo transcurrido (en minutos) y $V$ el volumen (en litros), el volumen **depende** del tiempo: a cada valor de $t$ le corresponde **un único** valor de $V$, que se calcula con $V = 80 + 12\,t$. Esa dependencia, con la precisión de saber para qué valores de $t$ tiene sentido y a qué conjunto pertenecen los resultados, es lo que formalizamos como función.

## Definición de función

:::note[Definición]
Dados dos conjuntos $A$ y $B$ de números reales, una **función** de $A$ en $B$ es una regla que asigna a **cada** elemento $x \in A$ **uno y solo un** elemento $y \in B$. Se escribe

$$
f\colon A \to B \,/\, y = f(x)
$$

y se lee «$y$ es la imagen de $x$ a través de $f$».

- $A$ es el **dominio**, $D_f$.
- $B$ es el **codominio** o conjunto de llegada.
- La **imagen** es el conjunto de los valores efectivamente alcanzados: $\operatorname{Im} f = \{\, y \in B : y = f(x) \text{ para algún } x \in A \,\}$. Siempre $\operatorname{Im} f \subseteq B$.
:::

La definición tiene dos exigencias, y las dos importan:

1. **Existencia:** todo $x$ del dominio tiene imagen.
2. **Unicidad:** ningún $x$ tiene dos imágenes distintas.

Por eso la circunferencia $x^2 + y^2 = 1$ **no** define a $y$ como función de $x$: para $x = 0$ hay dos valores, $y = 1$ e $y = -1$. En un gráfico, la unicidad se reconoce con el **test de la recta vertical**: una curva es el gráfico de una función si y solo si toda recta vertical la corta **a lo sumo** una vez.

### La terna

Una función queda determinada por **tres** datos: el dominio, el codominio y la regla. A esa información completa se la llama **terna**. Cambiar cualquiera de los tres da, en general, **otra** función. Por ejemplo, $f_1\colon \mathbb{R} \to \mathbb{R} \,/\, f_1(x) = x^2$ y $f_2\colon \mathbb{R} \to [0, +\infty) \,/\, f_2(x) = x^2$ tienen la misma regla, pero tienen distinto codominio, así que formalmente son funciones diferentes (la segunda es sobreyectiva y la primera no, como vamos a ver en la lección de la [inversa](/analisis-matematico-i/unidad-1/teoria/inversa/)).

Cuando solo se da la regla, se entiende que el dominio es el **dominio natural**: el conjunto más grande de reales para los que la regla tiene sentido. Cuando el problema viene de un contexto, el **dominio en contexto** es el subconjunto del natural que tiene sentido físico o económico: un volumen no puede ser negativo, un tiempo de vaciado no puede pasar del momento en que el tanque se vacía. El cálculo sistemático del dominio natural está en [álgebra de funciones](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/).

### Registros de representación

Una misma función se puede presentar de cuatro maneras:

| Registro | Qué muestra | Ventaja |
|---|---|---|
| Verbal | una descripción en palabras | contexto y unidades |
| Tabular | pares $(x, f(x))$ | datos medidos; permite detectar patrones |
| Gráfico | la curva en el plano | comportamiento global de un vistazo |
| Analítico | la fórmula | cálculo exacto y demostraciones |

Resolver un problema suele exigir **pasar de un registro a otro**: ajustar una fórmula a una tabla, o dibujar la curva de una fórmula.

### Ejemplo 1 · Imagen en un intervalo

Hallar la imagen de $g\colon [0, 5] \to \mathbb{R} \,/\, g(x) = x^2 - 4x + 7$.

**Estrategia.** Una parábola con ramas hacia arriba tiene su mínimo en el vértice; como el dominio es un intervalo **cerrado**, el máximo se alcanza en uno de los extremos.

**Desarrollo.** La abscisa del vértice es $x_v = -\dfrac{b}{2a} = 2$, que pertenece a $[0, 5]$, y $g(2) = 4 - 8 + 7 = 3$. En los extremos, $g(0) = 7$ y $g(5) = 25 - 20 + 7 = 12$. Entre $0$ y $2$ la función decrece de $7$ a $3$; entre $2$ y $5$ crece de $3$ a $12$. Como el gráfico es una parábola, un trazo continuo sin saltos, toma todos los valores entre $3$ y $12$.

<!-- check: U1.T.FUN.1 -->
$$
\operatorname{Im} g = [3, 12]
$$

Notá que si el dominio fuera todo $\mathbb{R}$ la imagen sería $[3, +\infty)$: la imagen depende del dominio.

### Ejemplo 2 · De la tabla a la fórmula

Un sensor registró estos datos de temperatura $T$ (en °C) a lo largo del tiempo $t$ (en minutos):

| $t$ | 0 | 1 | 3 |
|---|---|---|---|
| $T$ | 5 | 11 | 23 |

Suponemos que $T$ varía uniformemente. Los incrementos son $\dfrac{11 - 5}{1 - 0} = 6$ y $\dfrac{23 - 11}{3 - 1} = 6$: coinciden, lo que respalda la hipótesis. Entonces el modelo es lineal, $T(t) = 6\,t + b$, y con $T(0) = 5$ resulta $b = 5$:

<!-- check: U1.T.FUN.2 -->
$$
T(t) = 6t + 5.
$$

Comprobamos con el dato que no usamos para hallar la fórmula: $T(3) = 18 + 5 = 23$. Si el sensor se corta cuando llega a $41\,\text{°C}$, el dominio en contexto es $0 \le t \le 6$, porque $6t + 5 = 41$ cuando $t = 6$.

### Ejemplo 3 · Terna completa

Una pelota se lanza hacia arriba y su altura (en metros) a los $t$ segundos es $h(t) = 20t - 5t^2$ hasta que toca el piso. Escribir la terna.

**Dominio en contexto.** La pelota está en el aire mientras $h \ge 0$: $20t - 5t^2 = 5t(4 - t) \ge 0$ si $0 \le t \le 4$. El dominio es $[0, 4]$.

**Imagen.** El vértice está en $t = 2$ y $h(2) = 40 - 20 = 20$; en los extremos $h(0) = h(4) = 0$. Entonces $\operatorname{Im} h = [0, 20]$.

<!-- check: U1.T.FUN.3 -->
$$
h\colon [0, 4] \to [0, 20] \,/\, h(t) = 20t - 5t^2
$$

Con este codominio la función es sobreyectiva; si hubiésemos puesto $\mathbb{R}$ como codominio la regla y el dominio serían los mismos, pero la terna sería otra.

:::caution[Errores frecuentes]
- Confundir **codominio** con **imagen**: el codominio se elige al definir la función; la imagen se calcula.
- Calcular la imagen sin mirar el dominio: la imagen de $x^2 - 4x + 7$ en $[0, 5]$ no es $[3, +\infty)$.
- Dar solo la fórmula cuando el enunciado pide la función: falta el dominio y el codominio.
- Olvidar que el dominio en contexto puede ser **más chico** que el natural.
:::

## Las funciones como modelos

Un **modelo matemático** es una descripción matemática de un fenómeno real. Sirve para entender el fenómeno y para predecir. Se construye así:

1. **Identificar las variables**: la **independiente** (la que se elige o controla; es la entrada $x$) y la **dependiente** (la que se calcula; la salida $y = f(x)$), cada una con su **unidad**.
2. **Establecer suposiciones** que simplifican (por ejemplo, «el agua entra a caudal constante»).
3. **Plantear la regla** $y = f(x)$.
4. **Determinar el dominio y la imagen en contexto.**
5. **Interpretar** el resultado en términos del problema original, con unidades.

Cuatro familias de modelos aparecen una y otra vez. Las estudiamos como modelos; sus gráficos y características completas están en [funciones elementales](/analisis-matematico-i/unidad-1/teoria/funciones-elementales/).

| Modelo | Cuándo se usa | Forma |
|---|---|---|
| Lineal | la magnitud cambia **por igual** en intervalos de igual longitud | $y = mx + b$ |
| Cuadrático | hay un máximo o un mínimo (áreas, alturas en tiro vertical) | $y = ax^2 + bx + c$ |
| Exponencial | la magnitud se multiplica por un factor fijo en intervalos de igual longitud | $y = C\,a^x$, $a > 0$, $a \ne 1$ |
| Periódico | el fenómeno se repite (mareas, ruedas, ondas) | $y = A\operatorname{sen}(Bx + \varphi) + D$ |

### Razón de cambio media

:::note[Definición · Razón de cambio media]
La **razón de cambio media** de $f$ en el intervalo $[x_0, x_1]$ (con $x_0 \ne x_1$ en el dominio) es

$$
\frac{\Delta y}{\Delta x} = \frac{f(x_1) - f(x_0)}{x_1 - x_0}.
$$
:::

Dice **cuánto cambia $y$, en promedio, por cada unidad que cambia $x$**; sus unidades son «unidades de $y$ por unidad de $x$» (litros por minuto, metros por segundo). Geométricamente es la **pendiente de la recta secante** que une los puntos $(x_0, f(x_0))$ y $(x_1, f(x_1))$.

![Altura h(t) = 20t − 5t² y la recta secante que une los puntos de abscisa 1 y 4; la pendiente de la secante es la razón de cambio media −5.](/analisis-matematico-i/figuras/u1-secante.svg)

*Observá que la secante une dos puntos de la curva y que su pendiente es negativa: en promedio, entre $t = 1$ y $t = 4$ la altura baja $5$ metros por segundo, aunque en parte de ese intervalo la pelota todavía sube.*

Esta es la herramienta de modelado que usamos aquí. En la [Unidad 3](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/) se formaliza al pasar de la secante a la tangente.

### Cambio uniforme y función lineal

:::note[Propiedad]
Una función $f$ definida en un intervalo tiene razón de cambio media **constante** en todos los subintervalos si y solo si es una función lineal $f(x) = mx + b$; esa constante es $m$.
:::

**Demostración (formal).** ($\Leftarrow$) Si $f(x) = mx + b$, entonces
$\dfrac{f(x_1) - f(x_0)}{x_1 - x_0} = \dfrac{m x_1 + b - m x_0 - b}{x_1 - x_0} = m$ para cualquier par $x_0 \ne x_1$.
($\Rightarrow$) Si la razón media vale siempre una constante $m$, fijamos un punto $x_0$ del intervalo y tomamos un $x \ne x_0$ cualquiera: $\dfrac{f(x) - f(x_0)}{x - x_0} = m$, es decir, $f(x) = f(x_0) + m(x - x_0)$ para todo $x$ (también para $x = x_0$). Es de la forma $mx + b$ con $b = f(x_0) - m x_0$. $\blacksquare$

Cuando la razón de cambio **depende del intervalo**, el cambio es **no uniforme**, y el modelo no es lineal.

### Ejemplo 4 · Modelo lineal con dominio en contexto

El tanque de la introducción tiene capacidad de 600 litros, contiene 80 litros al abrir la canilla y recibe $12$ litros por minuto. Modelar el volumen y decir cuándo se llena.

- Variable independiente: $t$, tiempo desde que se abre la canilla (min). Dependiente: $V$, volumen (L).
- Suposición: el caudal es constante, así que la razón de cambio es constante: modelo lineal con pendiente $12$ L/min y ordenada al origen $80$ L: $V(t) = 80 + 12\,t$.
- Se llena cuando $V = 600$: $80 + 12 t = 600 \Rightarrow t = \dfrac{520}{12} = \dfrac{130}{3} \approx 43{,}3$ min.

<!-- check: U1.T.MOD.1 -->
$$
V\colon \left[0, \tfrac{130}{3}\right] \to [80, 600] \,/\, V(t) = 80 + 12t
$$

Interpretación: la pendiente $12$ es la razón de cambio media en **cualquier** intervalo: por ejemplo, entre $t = 5$ y $t = 7$ el volumen pasa de $140$ a $164$ litros, y $\dfrac{164 - 140}{2} = 12$ L/min.

### Ejemplo 5 · Modelo cuadrático: maximizar un área

Con $40$ metros de alambre se cerca un corral rectangular que usa una pared como uno de sus lados (ese lado no lleva alambre). Si los dos lados perpendiculares a la pared miden $x$ metros, expresar el área en función de $x$ y hallar su máximo.

El lado paralelo a la pared mide $40 - 2x$, así que $A(x) = x(40 - 2x) = 40x - 2x^2$. Para que existan ambos lados, $x > 0$ y $40 - 2x > 0$, es decir, $0 < x < 20$.

El vértice está en $x_v = -\dfrac{40}{2\cdot(-2)} = 10$, que está dentro del dominio, con $A(10) = 10 \cdot 20 = 200$ m². Las dimensiones óptimas son $10 \times 20$ metros.

<!-- check: U1.T.MOD.2 -->
$$
A\colon (0, 20) \to (0, 200] \,/\, A(x) = 40x - 2x^2
$$

Como el dominio es abierto, $A$ no toma el valor $0$; sí alcanza su máximo $200$.

### Ejemplo 6 · Modelo exponencial: ajustar a dos datos

Un cultivo tiene $200$ bacterias al comenzar y $3200$ cuatro horas después. Suponemos $N(t) = C\,a^t$ con $t$ en horas.

<!-- check: U1.T.MOD.3 -->
Con $t = 0$: $N(0) = C = 200$. Con $t = 4$: $200\,a^4 = 3200 \Rightarrow a^4 = 16 \Rightarrow a = 2$ (tomamos $a > 0$). Entonces $N(t) = 200 \cdot 2^t$: la población se **duplica cada hora**.

¿Cuándo llega a $10\,000$? $200 \cdot 2^t = 10\,000 \Rightarrow 2^t = 50 \Rightarrow t = \log_2 50 = \dfrac{\ln 50}{\ln 2} \approx 5{,}64$ horas.

### Ejemplo 7 · Razón de cambio media de un modelo exponencial

Con $N(t) = 200\cdot 2^t$ calculamos la razón media en tres intervalos de la misma longitud:

<!-- check: U1.T.MOD.4 -->
| Intervalo | $\Delta N$ | $\Delta N / \Delta t$ |
|---|---|---|
| $[0, 1]$ | $400 - 200 = 200$ | $200$ bact/h |
| $[1, 2]$ | $800 - 400 = 400$ | $400$ bact/h |
| $[2, 3]$ | $1600 - 800 = 800$ | $800$ bact/h |

No es constante, así que el cambio es **no uniforme** y $N$ no es lineal. Lo que sí es constante es el **cociente** $N(t+1)/N(t) = 2$: el modelo exponencial cambia por un **factor** fijo, el lineal cambia por una **cantidad** fija.

### Ejemplo 8 · Razón de cambio media de un modelo cuadrático

Para $h(t) = 20t - 5t^2$ del ejemplo 3, en $[1, 4]$ (la secante de la figura):

<!-- check: U1.T.MOD.5 -->
$$
\frac{h(4) - h(1)}{4 - 1} = \frac{0 - 15}{3} = -5 \ \text{m/s}.
$$

En $[0, 2]$ vale $\dfrac{20 - 0}{2} = 10$ m/s y en $[2, 4]$ vale $\dfrac{0 - 20}{2} = -10$ m/s: la razón de cambio media cambia de signo porque la pelota sube y luego baja. Un valor $0$ no significa que la función sea constante: en $[1, 3]$ vale $\dfrac{15 - 15}{2} = 0$ aunque $h$ cambia (sube y baja).

### Ejemplo 9 · Modelo periódico

Una rueda de $8$ metros de radio gira con su eje a $10$ metros del suelo y da una vuelta cada $24$ minutos. Una cabina parte del punto más bajo. Su altura es de la forma $h(t) = 10 - 8\cos(Bt)$: parte de $10 - 8 = 2$ m (punto más bajo), la amplitud es $8$ y el valor medio $10$. El período es $\dfrac{2\pi}{B} = 24$, así que $B = \dfrac{\pi}{12}$:

<!-- check: U1.T.MOD.6 -->
$$
h(t) = 10 - 8\cos\left(\frac{\pi}{12}\,t\right), \qquad \operatorname{Im} h = [2, 18].
$$

Comprobaciones: $h(0) = 2$; $h(12) = 10 - 8\cos\pi = 18$ (punto más alto, media vuelta); $h(6) = 10 - 8\cos\frac{\pi}{2} = 10$ (a la altura del eje).

## Ejercicios

### Ejercicio 1 · Tarifa de alquiler
<!-- ejercicio: U1.01 | nivel: inicial | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
Un club alquila bicicletas con una cuota fija de $150$ pesos más $40$ pesos por hora, con un máximo de $8$ horas.
a) Escribir la función $C$ que da el costo según las horas $h$, con su terna.
b) ¿Cuántas horas se alquiló si se pagaron $350$ pesos?
c) Calcular la razón de cambio media entre $h = 2$ y $h = 6$ e interpretarla.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Hay un costo fijo y un costo que crece por igual cada hora: modelo lineal.

**Desarrollo.** a) $C(h) = 150 + 40h$. El dominio en contexto es $[0, 8]$ y $C(0) = 150$, $C(8) = 470$, así que la imagen es $[150, 470]$:

$$
C\colon [0, 8] \to [150, 470] \,/\, C(h) = 150 + 40h.
$$

b) $150 + 40h = 350 \Rightarrow h = 5$.

c) $\dfrac{C(6) - C(2)}{6 - 2} = \dfrac{390 - 230}{4} = 40$.

**Resultado.** a) la terna anterior; b) $5$ horas; c) $40$ pesos por hora: es la pendiente, el precio de cada hora adicional, y es igual en todos los intervalos porque el modelo es lineal.

</details>

### Ejercicio 2 · Verdadero o falso sobre funciones
<!-- ejercicio: U1.02 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa y justificar.
a) La relación que a cada $x \ge 0$ le asigna los $y$ tales que $y^2 = x$ es una función.
b) Si dos funciones tienen la misma regla, son iguales.
c) La imagen de una función siempre está incluida en su codominio.
d) Si la razón de cambio media de $f$ es la misma en $[0, 1]$ y en $[1, 2]$, entonces $f$ es lineal.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Volver a la definición (unicidad, terna) y buscar contraejemplos.

**Desarrollo.**
a) **Falso.** Para $x = 4$ hay dos valores, $y = 2$ e $y = -2$: falla la unicidad. Sí es función $y = \sqrt{x}$ (solo la raíz no negativa).
b) **Falso.** Dos funciones son iguales cuando coinciden dominio, codominio y regla. $f_1\colon \mathbb{R} \to \mathbb{R}$ y $f_2\colon [0,+\infty) \to \mathbb{R}$, ambas con regla $x^2$, tienen distinto dominio.
c) **Verdadero.** Por definición $\operatorname{Im} f = \{y \in B : \dots\} \subseteq B$.
d) **Falso.** La propiedad pide la misma razón en **todos** los subintervalos, no solo en dos. Contraejemplo: $f(x) = x(x-1)(x-2)$ vale $0$ en $x = 0, 1, 2$, así que su razón media es $0$ tanto en $[0, 1]$ como en $[1, 2]$; sin embargo no es lineal, porque $f\left(\tfrac12\right) = \tfrac38 \ne 0$ y la razón media en $\left[0, \tfrac12\right]$ es $\tfrac34 \ne 0$.

**Resultado.** a) F, b) F, c) V, d) F.

</details>

### Ejercicio 3 · El corral dividido
<!-- ejercicio: U1.03 | nivel: intermedio | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
Un productor dispone de $120$ metros de alambre para armar un corral rectangular dividido en dos por un alambre paralelo a uno de los lados (queda con tres tramos de alambre del mismo largo $x$ y dos tramos de largo $y$, sin exigir cuál de los dos lados es el menor).
a) Expresar el área $A$ en función de $x$ y hallar el dominio en contexto.
b) Hallar las dimensiones que maximizan el área y el área máxima.
c) Calcular la razón de cambio media de $A$ entre $x = 10$ y $x = 30$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Usar el alambre total para despejar $y$ en función de $x$ y reducir el área a una variable.

**Desarrollo.** a) El alambre total es $3x + 2y = 120$, de donde $y = 60 - \tfrac{3}{2}x$. El área es $A(x) = x\,y = 60x - \tfrac{3}{2}x^2$. Hace falta $x > 0$ e $y > 0$, es decir, $x < 40$: el dominio es $(0, 40)$.

b) Es una parábola con ramas hacia abajo; su vértice está en $x_v = -\dfrac{60}{2\cdot(-3/2)} = 20 \in (0, 40)$. Entonces $y = 60 - 30 = 30$ y $A(20) = 20 \cdot 30 = 600$.

c) $A(10) = 600 - 150 = 450$ y $A(30) = 1800 - 1350 = 450$, así que la razón de cambio media es $\dfrac{450 - 450}{20} = 0$.

**Resultado.** a) $A(x) = 60x - \tfrac32 x^2$ con $x \in (0, 40)$; b) $20 \text{ m} \times 30 \text{ m}$, área máxima $600\ \text{m}^2$; c) $0$: los dos puntos están a igual distancia del vértice $x = 20$, por eso tienen igual área.

</details>

### Ejercicio 4 · Ajuste exponencial
<!-- ejercicio: U1.04 | nivel: intermedio | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
El número de usuarios de una aplicación sigue un modelo $N(t) = C\,a^t$ ($t$ en meses). A los $2$ meses hay $90$ usuarios y a los $5$ meses hay $720$.
a) Hallar $C$ y $a$.
b) ¿En qué mes se llegan a $5760$ usuarios?
c) Calcular la razón de cambio media entre $t = 2$ y $t = 5$ y comparar con la de $[5, 8]$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos datos para dos parámetros: dividir las ecuaciones para eliminar $C$.

**Desarrollo.** a) De $C a^2 = 90$ y $C a^5 = 720$, dividiendo: $a^3 = 8$, entonces $a = 2$ y $C = \dfrac{90}{4} = 22{,}5$. Por lo tanto $N(t) = 22{,}5 \cdot 2^t$.

b) $22{,}5 \cdot 2^t = 5760 \Rightarrow 2^t = 256 \Rightarrow t = 8$.

c) En $[2, 5]$: $\dfrac{720 - 90}{3} = 210$ usuarios por mes. En $[5, 8]$: $\dfrac{5760 - 720}{3} = 1680$ usuarios por mes.

**Resultado.** a) $C = 22{,}5$, $a = 2$; b) a los $8$ meses; c) $210$ y $1680$ usuarios/mes: la razón media crece ocho veces porque el crecimiento es exponencial (no uniforme).

</details>

### Ejercicio 5 · La noria
<!-- ejercicio: U1.05 | nivel: avanzado | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
Una rueda gigante tiene $12$ m de radio, su eje está a $14$ m del suelo y completa una vuelta cada $30$ minutos. Una persona sube en el punto más bajo en $t = 0$.
a) Hallar la altura $h(t)$ como $h(t) = D - A\cos(Bt)$ y su imagen.
b) ¿En qué instantes de la primera vuelta la altura es de $20$ m?
c) Calcular la razón de cambio media en $[0, 5]$, $[5, 10]$ y $[10, 15]$ y explicar por qué no es la misma.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Amplitud, nivel medio y período fijan los tres parámetros; después se resuelve $\cos(\cdot) = k$ en una vuelta.

**Desarrollo.** a) El nivel medio es la altura del eje, $D = 14$; la amplitud es el radio, $A = 12$; el punto más bajo es $14 - 12 = 2$ m. El período es $\dfrac{2\pi}{B} = 30$, entonces $B = \dfrac{\pi}{15}$:

$$
h(t) = 14 - 12\cos\left(\frac{\pi}{15} t\right), \qquad \operatorname{Im} h = [2, 26].
$$

b) $14 - 12\cos\theta = 20 \Rightarrow \cos\theta = -\tfrac12$ con $\theta = \dfrac{\pi t}{15} \in [0, 2\pi]$. Las soluciones son $\theta = \dfrac{2\pi}{3}$ y $\theta = \dfrac{4\pi}{3}$, es decir, $t = 10$ y $t = 20$.

c) Evaluamos en los extremos de cada tercio de vuelta: $h(0) = 2$; $h(5) = 14 - 12\cos\frac{\pi}{3} = 8$; $h(10) = 14 - 12\cos\frac{2\pi}{3} = 20$; $h(15) = 14 - 12\cos\pi = 26$. Entonces

$$
\frac{h(5) - h(0)}{5} = \frac{6}{5} = 1{,}2, \qquad \frac{h(10) - h(5)}{5} = \frac{12}{5} = 2{,}4, \qquad \frac{h(15) - h(10)}{5} = \frac{6}{5} = 1{,}2.
$$

**Resultado.** a) $h(t) = 14 - 12\cos\left(\frac{\pi}{15}t\right)$, imagen $[2, 26]$; b) $t = 10$ min y $t = 20$ min; c) $1{,}2$; $2{,}4$ y $1{,}2$ m/min. La razón media es mayor en el tramo central porque cerca del punto más bajo y del más alto la cabina casi no cambia de altura, mientras que a mitad de camino sube mucho más por minuto: el cambio no es uniforme.

</details>

## Autoevaluación

<details>
<summary>1. ¿Qué dos condiciones exige la definición de función?</summary>

Existencia (todo elemento del dominio tiene imagen) y unicidad (esa imagen es única).
</details>

**2. Un modelo da una razón de cambio media de $3$ en $[0, 1]$ y de $5$ en $[1, 2]$. ¿Puede ser lineal?**

<details>
<summary>Respuesta</summary>

No. En un modelo lineal la razón media es la misma en cualquier intervalo.
</details>

<details>
<summary>3. ¿Qué diferencia hay entre dominio natural y dominio en contexto?</summary>

El natural depende solo de la regla (donde la fórmula tiene sentido); el de contexto incluye además las restricciones físicas o económicas del problema, y es un subconjunto del natural.
</details>

<details>
<summary>4. ¿Cómo se reconoce en un gráfico que una curva no es una función?</summary>

Con el test de la recta vertical: si alguna recta vertical la corta en más de un punto, hay un $x$ con dos imágenes.
</details>

:::tip[En resumen]
- Una función es una **terna** (dominio, codominio, regla) donde cada $x$ tiene una **única** imagen; la imagen se calcula y está incluida en el codominio.
- Se la representa en cuatro registros (verbal, tabular, gráfico, analítico) y hay que saber pasar de uno a otro.
- Modelar es identificar variables con unidades, plantear la regla y acotar dominio e imagen **en contexto**.
- La razón de cambio media $\frac{\Delta y}{\Delta x}$ es la pendiente de la secante; es constante en todos los intervalos exactamente cuando el modelo es lineal.
:::

**Para seguir.** Con las funciones definidas, el próximo paso es estudiar sus propiedades: [ceros, signo, paridad y acotación](/analisis-matematico-i/unidad-1/teoria/caracteristicas/). Si querés explorar las funciones con un software, mirá la [guía de GeoGebra para funciones](/analisis-matematico-i/geogebra/funciones/).
