# Comprobación de comandos de GeoGebra

Protocolo reproducible para comprobar, **ejecutándolos en GeoGebra**, los comandos que citan las guías de GeoGebra y
los integradores de Análisis Matemático I.

## Qué hace

`ejecutar.mjs`:
1. Abre GeoGebra Clásico en Chromium (Playwright), cargado desde la distribución oficial
   (`https://www.geogebra.org/apps/deployggb.js`), con la interfaz en español (`applet.html`).
2. Para cada caso de `casos.json`, pega el comando en el campo «Entrada…» de la vista algebraica y pulsa Enter, como
   lo haría un estudiante.
3. Lee con la API del applet los objetos que se crearon y los compara con el resultado esperado del caso.
4. Escribe el detalle en `resultado.json`.

No se usa `evalCommand` de la API: solo acepta los nombres internos en inglés (`Root`, `Derivative`…) y rechaza
`Raíz` o `Derivada`, así que no comprobaría la sintaxis en español de los apuntes.

## Cómo correrlo

Desde la raíz del repositorio, con las dependencias instaladas (`npm ci` y `npx playwright install chromium`) y
acceso a geogebra.org:

```sh
node academic-sources/analisis-matematico-i/geogebra/ejecutar.mjs
```

Termina con código 0 si todos los casos dan lo esperado.

## Muestra

52 casos sobre 28 comandos distintos. Cubren los comandos más citados (`Derivada`, `PolinomioTaylor`, `Tangente`,
`Límite` y sus laterales, `Si`, `Raíz`, `Extremo`, `Asíntota`, `Interseca`, `Máximo`, `Mínimo`, `Función`), los cinco
de ajuste (`AjusteLineal`, `AjustePolinómico`, `AjusteExp`, `AjusteBaseExp`, `AjustePotencia` y `AjusteLog`),
`Inversa`, `DerivadaImplícita`, `PuntoInflexión`, `Pendiente`, `Perpendicular`, `Recta`, `Secuencia` y `Deslizador`.

También incluye **casos negativos**, que documentan sintaxis que no funciona:
- `Raiz(f)` sin tilde;
- `Límite(f, infinito)`;
- `DerivadaImplícita` aplicada a una ecuación;
- `(2; 3)`, que es un punto en coordenadas polares.

## Último resultado

GeoGebra web 5.4.920.0, 21/11/2026: **52 de 52 casos** dieron el resultado esperado.

La ejecución encontró dos errores en las guías, que se corrigieron:
- **`Límite(f, infinito)` no funciona.** Hay que escribir `∞` (o `inf`). Con `Infinito` en mayúscula, GeoGebra crea en
  silencio un número llamado `Infinito`.
- **`DerivadaImplícita(c)` con `c: x^2 + y^2 = 25` no devuelve nada.** El comando recibe la expresión $F(x,y)$, como en
  `DerivadaImplícita(x^2 + y^2 - 25)`, y la forma `DerivadaImplícita(c)(3, 4)` no es válida. Para evaluar se define
  `m(x, y) = DerivadaImplícita(x^2 + y^2 - 25)` y se calcula `m(3, 4)`, que da $-0{,}75$.

Además confirmó que la entrada usa punto decimal y coma entre argumentos, que `Raiz` sin tilde no se reconoce y que
en español `tg` es el nombre de la tangente trigonométrica, por lo que no sirve como nombre de objeto.

## Límites

- Es una muestra. Los comandos y usos que no están en `casos.json` solo se revisaron contra el manual.
- Se probó una sola versión, la web vigente al día de la ejecución. Otras versiones, como la de escritorio o la
  calculadora gráfica, pueden diferir en detalles.
- La comprobación valida el valor que devuelve cada comando. No revisa cómo se ve el gráfico.
