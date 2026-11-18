---
title: Práctica — Window Functions
slug: bbdd-aplicadas/unidad-1/practica/window-functions
sidebar:
  label: Window Functions
  order: 2
---

Doce ejercicios originales sobre funciones de ventana, con datos propios: una carrera por etapas. Presuponen la lección de [window functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/) y, para el ejercicio 4 y el 10, de [CTE](/bbdd-aplicadas/unidad-1/teoria/cte/). Objetivos: ranking, particiones, `LAG`/`LEAD`, marcos, acumulados, valores de borde y percentiles.

## Conjunto de datos

Ocho corredores en dos categorías, cinco etapas y un tiempo en minutos por corredor y etapa. Tito abandona antes de la etapa 4, y hay empates de tiempo a propósito. Creá una base de prueba (por ejemplo `CREATE DATABASE PracticaCarrera;`), cambiá a ella y ejecutá:

<!-- check: U1.42 -->
```sql
CREATE SCHEMA carrera;
GO

CREATE TABLE carrera.Corredor (
    CorredorId INT         NOT NULL,
    Nombre     VARCHAR(30) NOT NULL,
    Categoria  VARCHAR(10) NOT NULL,
    CONSTRAINT PK_Corredor PRIMARY KEY (CorredorId),
    CONSTRAINT CK_Corredor_Categoria CHECK (Categoria IN ('Elite', 'Amateur'))
);

CREATE TABLE carrera.Etapa (
    EtapaId INT         NOT NULL,
    Nombre  VARCHAR(30) NOT NULL,
    Km      INT         NOT NULL,
    CONSTRAINT PK_Etapa PRIMARY KEY (EtapaId),
    CONSTRAINT CK_Etapa_Km CHECK (Km > 0)
);

CREATE TABLE carrera.Tiempo (
    CorredorId INT NOT NULL,
    EtapaId    INT NOT NULL,
    Minutos    INT NOT NULL,
    CONSTRAINT PK_Tiempo PRIMARY KEY (CorredorId, EtapaId),
    CONSTRAINT FK_Tiempo_Corredor FOREIGN KEY (CorredorId) REFERENCES carrera.Corredor (CorredorId),
    CONSTRAINT FK_Tiempo_Etapa FOREIGN KEY (EtapaId) REFERENCES carrera.Etapa (EtapaId),
    CONSTRAINT CK_Tiempo_Minutos CHECK (Minutos > 0)
);

INSERT INTO carrera.Corredor (CorredorId, Nombre, Categoria)
VALUES
    (1, 'Lola',  'Elite'),
    (2, 'Mateo', 'Elite'),
    (3, 'Nora',  'Elite'),
    (4, 'Omar',  'Elite'),
    (5, 'Pia',   'Amateur'),
    (6, 'Rafa',  'Amateur'),
    (7, 'Sol',   'Amateur'),
    (8, 'Tito',  'Amateur');

INSERT INTO carrera.Etapa (EtapaId, Nombre, Km)
VALUES
    (1, 'Llano',        40),
    (2, 'Montana',      55),
    (3, 'Contrarreloj', 20),
    (4, 'Sierras',      65),
    (5, 'Final',        30);

-- Tito abandona antes de la etapa 4: no tiene tiempos en las etapas 4 y 5
INSERT INTO carrera.Tiempo (CorredorId, EtapaId, Minutos)
VALUES
    (1, 1, 62), (2, 1, 64), (3, 1, 64), (4, 1, 66), (5, 1, 70), (6, 1, 69), (7, 1, 72), (8, 1, 72),
    (1, 2, 90), (2, 2, 88), (3, 2, 91), (4, 2, 91), (5, 2, 99), (6, 2, 97), (7, 2, 97), (8, 2, 104),
    (1, 3, 30), (2, 3, 31), (3, 3, 29), (4, 3, 31), (5, 3, 36), (6, 3, 35), (7, 3, 33), (8, 3, 38),
    (1, 4, 98), (2, 4, 101), (3, 4, 96), (4, 4, 100), (5, 4, 112), (6, 4, 108), (7, 4, 110),
    (1, 5, 47), (2, 5, 45), (3, 5, 49), (4, 5, 48), (5, 5, 55), (6, 5, 52), (7, 5, 50);
GO

SELECT
    (SELECT COUNT(*) FROM carrera.Corredor) AS Corredores,
    (SELECT COUNT(*) FROM carrera.Etapa)    AS Etapas,
    (SELECT COUNT(*) FROM carrera.Tiempo)   AS Tiempos;
```

**Resultado esperado.**

| Corredores | Etapas | Tiempos |
|---:|---:|---:|
| 8 | 5 | 38 |

Todos los ejercicios siguen sobre este esquema. En cada uno, el script de la resolución se ejecuta después de este.

## Ejercicios

### Ejercicio 1 · Orden de llegada
<!-- ejercicio: U1.21 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Numerá a los corredores de la etapa 1 según su orden de llegada (el menor tiempo es el número 1). Si dos empatan, desempatá por `CorredorId`. Mostrá número, nombre y minutos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `ROW_NUMBER()` con `ORDER BY Minutos, CorredorId`; el desempate vuelve determinista la numeración.

<!-- check: U1.21 -->
```sql
SELECT
    ROW_NUMBER() OVER (ORDER BY t.Minutos, t.CorredorId) AS NroLlegada,
    c.Nombre,
    t.Minutos
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 1
ORDER BY NroLlegada;
```

**Resultado esperado.**

| NroLlegada | Nombre | Minutos |
|---:|---|---:|
| 1 | Lola | 62 |
| 2 | Mateo | 64 |
| 3 | Nora | 64 |
| 4 | Omar | 66 |
| 5 | Rafa | 69 |
| 6 | Pia | 70 |
| 7 | Sol | 72 |
| 8 | Tito | 72 |

Mateo y Nora empatan en 64 minutos: `ROW_NUMBER` igual les da 2 y 3, y el desempate por `CorredorId` decide quién es quién.

</details>

### Ejercicio 2 · Puestos con empates
<!-- ejercicio: U1.22 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
En la etapa 2, mostrá el puesto de cada corredor calculado con `RANK` y con `DENSE_RANK`. ¿Qué diferencia se ve a partir de los empates?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos columnas con la misma ventana `ORDER BY Minutos`; comparamos cómo cada función numera después de un empate.

<!-- check: U1.22 -->
```sql
SELECT
    c.Nombre,
    t.Minutos,
    RANK()       OVER (ORDER BY t.Minutos) AS PuestoRank,
    DENSE_RANK() OVER (ORDER BY t.Minutos) AS PuestoDenso
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 2
ORDER BY t.Minutos, c.Nombre;
```

**Resultado esperado.**

| Nombre | Minutos | PuestoRank | PuestoDenso |
|---|---:|---:|---:|
| Mateo | 88 | 1 | 1 |
| Lola | 90 | 2 | 2 |
| Nora | 91 | 3 | 3 |
| Omar | 91 | 3 | 3 |
| Rafa | 97 | 5 | 4 |
| Sol | 97 | 5 | 4 |
| Pia | 99 | 7 | 5 |
| Tito | 104 | 8 | 6 |

Nora y Omar empatan (91) y comparten el puesto 3. `RANK` salta al 5 porque cuatro corredores llegaron antes que Rafa y Sol, mientras que `DENSE_RANK` continúa con 4 sin dejar huecos.

</details>

### Ejercicio 3 · Diferencia con el promedio de la etapa
<!-- ejercicio: U1.23 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para la etapa 3, mostrá el tiempo de cada corredor, el promedio de la etapa (con dos decimales) y cuánto se aparta cada uno de ese promedio, sin usar `GROUP BY`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `AVG(...) OVER ()` sin partición calcula el promedio de todas las filas filtradas. Multiplicamos por `1.0` para evitar la división entera de `INT`.

<!-- check: U1.23 -->
```sql
SELECT
    c.Nombre,
    t.Minutos,
    CAST(AVG(t.Minutos * 1.0) OVER () AS DECIMAL(5,2))             AS PromedioEtapa,
    CAST(t.Minutos - AVG(t.Minutos * 1.0) OVER () AS DECIMAL(5,2)) AS DiferenciaConPromedio
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 3
ORDER BY t.Minutos, c.Nombre;
```

**Resultado esperado.**

| Nombre | Minutos | PromedioEtapa | DiferenciaConPromedio |
|---|---:|---:|---:|
| Nora | 29 | 32.88 | -3.88 |
| Lola | 30 | 32.88 | -2.88 |
| Mateo | 31 | 32.88 | -1.88 |
| Omar | 31 | 32.88 | -1.88 |
| Sol | 33 | 32.88 | 0.13 |
| Rafa | 35 | 32.88 | 2.13 |
| Pia | 36 | 32.88 | 3.13 |
| Tito | 38 | 32.88 | 5.13 |

Sin `1.0` el promedio de enteros se truncaría a 32. Las diferencias negativas son corredores más rápidos que el promedio.

</details>

### Ejercicio 4 · Podio por etapa
<!-- ejercicio: U1.24 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Listá los tres primeros puestos de cada etapa, incluyendo a todos los que empaten en un puesto del podio. Una función de ventana no puede ir en el `WHERE`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calculamos `RANK() OVER (PARTITION BY EtapaId ORDER BY Minutos)` en una CTE y filtramos `Puesto <= 3` afuera.

<!-- check: U1.24 -->
```sql
WITH Posicion AS (
    SELECT
        t.EtapaId,
        c.Nombre,
        t.Minutos,
        RANK() OVER (PARTITION BY t.EtapaId ORDER BY t.Minutos) AS Puesto
    FROM carrera.Tiempo AS t
    INNER JOIN carrera.Corredor AS c
        ON c.CorredorId = t.CorredorId
)
SELECT
    EtapaId,
    Puesto,
    Nombre,
    Minutos
FROM Posicion
WHERE Puesto <= 3
ORDER BY EtapaId, Puesto, Nombre;
```

**Resultado esperado.**

| EtapaId | Puesto | Nombre | Minutos |
|---:|---:|---|---:|
| 1 | 1 | Lola | 62 |
| 1 | 2 | Mateo | 64 |
| 1 | 2 | Nora | 64 |
| 2 | 1 | Mateo | 88 |
| 2 | 2 | Lola | 90 |
| 2 | 3 | Nora | 91 |
| 2 | 3 | Omar | 91 |
| 3 | 1 | Nora | 29 |
| 3 | 2 | Lola | 30 |
| 3 | 3 | Mateo | 31 |
| 3 | 3 | Omar | 31 |
| 4 | 1 | Nora | 96 |
| 4 | 2 | Lola | 98 |
| 4 | 3 | Omar | 100 |
| 5 | 1 | Mateo | 45 |
| 5 | 2 | Lola | 47 |
| 5 | 3 | Omar | 48 |

Con `RANK`, un empate por el segundo puesto (etapa 1) hace que el tercer puesto no exista: el podio de esa etapa tiene tres corredores y no cuatro. Con un empate por el tercero (etapa 2) el podio tiene cuatro. Con `ROW_NUMBER` se perdería a uno de los empatados.

</details>

### Ejercicio 5 · Variación respecto de la etapa anterior
<!-- ejercicio: U1.25 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para Lola (corredora 1) y Tito (corredor 8), mostrá el tiempo en cada etapa, el de la etapa anterior y la diferencia. En la primera etapa de cada uno no hay anterior.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `LAG(Minutos)` con `PARTITION BY CorredorId ORDER BY EtapaId`. Sin valor por defecto, la primera fila de cada partición queda en `NULL`.

<!-- check: U1.25 -->
```sql
SELECT
    c.Nombre,
    t.EtapaId,
    t.Minutos,
    LAG(t.Minutos) OVER (PARTITION BY t.CorredorId ORDER BY t.EtapaId) AS MinutosEtapaAnterior,
    t.Minutos - LAG(t.Minutos) OVER (PARTITION BY t.CorredorId ORDER BY t.EtapaId) AS Diferencia
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.CorredorId IN (1, 8)
ORDER BY c.Nombre, t.EtapaId;
```

**Resultado esperado.**

| Nombre | EtapaId | Minutos | MinutosEtapaAnterior | Diferencia |
|---|---:|---:|---:|---:|
| Lola | 1 | 62 | `NULL` | `NULL` |
| Lola | 2 | 90 | 62 | 28 |
| Lola | 3 | 30 | 90 | -60 |
| Lola | 4 | 98 | 30 | 68 |
| Lola | 5 | 47 | 98 | -51 |
| Tito | 1 | 72 | `NULL` | `NULL` |
| Tito | 2 | 104 | 72 | 32 |
| Tito | 3 | 38 | 104 | -66 |

Tito solo tiene tres etapas: la partición termina donde terminan sus datos. Las etapas tienen distinta longitud, así que la diferencia en minutos no mide mejora de ritmo; para eso habría que dividir por `Km`.

</details>

### Ejercicio 6 · Tiempo acumulado
<!-- ejercicio: U1.26 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para Lola y Tito, mostrá el tiempo acumulado a medida que avanzan las etapas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `SUM(Minutos)` con partición por corredor, orden por etapa y marco `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

<!-- check: U1.26 -->
```sql
SELECT
    c.Nombre,
    t.EtapaId,
    t.Minutos,
    SUM(t.Minutos) OVER (
        PARTITION BY t.CorredorId
        ORDER BY t.EtapaId
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS MinutosAcumulados
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.CorredorId IN (1, 8)
ORDER BY c.Nombre, t.EtapaId;
```

**Resultado esperado.**

| Nombre | EtapaId | Minutos | MinutosAcumulados |
|---|---:|---:|---:|
| Lola | 1 | 62 | 62 |
| Lola | 2 | 90 | 152 |
| Lola | 3 | 30 | 182 |
| Lola | 4 | 98 | 280 |
| Lola | 5 | 47 | 327 |
| Tito | 1 | 72 | 72 |
| Tito | 2 | 104 | 176 |
| Tito | 3 | 38 | 214 |

El marco acumula desde la primera etapa hasta la actual. Como `EtapaId` es único dentro de cada corredor, `ROWS` y el marco por defecto darían lo mismo, pero `ROWS` es más claro y evita sorpresas con empates.

</details>

### Ejercicio 7 · Tres grupos por rendimiento
<!-- ejercicio: U1.27 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Dividí a los corredores de la etapa 1 en tres grupos según su tiempo: el grupo 1 son los más rápidos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `NTILE(3)` ordenado por tiempo, con el nombre como desempate para que el reparto sea determinista.

<!-- check: U1.27 -->
```sql
SELECT
    c.Nombre,
    t.Minutos,
    NTILE(3) OVER (ORDER BY t.Minutos, c.Nombre) AS Grupo
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 1
ORDER BY Grupo, t.Minutos, c.Nombre;
```

**Resultado esperado.**

| Nombre | Minutos | Grupo |
|---|---:|---:|
| Lola | 62 | 1 |
| Mateo | 64 | 1 |
| Nora | 64 | 1 |
| Omar | 66 | 2 |
| Rafa | 69 | 2 |
| Pia | 70 | 2 |
| Sol | 72 | 3 |
| Tito | 72 | 3 |

Son 8 corredores en 3 grupos: no se divide exacto, así que los grupos más grandes van primero (3, 3 y 2). Mateo y Nora, empatados, pueden caer en grupos distintos si el desempate lo decide.

</details>

### Ejercicio 8 · Diferencia con el ganador
<!-- ejercicio: U1.28 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para la etapa 4, mostrá el ganador y cuántos minutos de diferencia tiene cada corredor con él.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `FIRST_VALUE` sobre la ventana ordenada por tiempo devuelve la primera fila: el ganador, tanto su nombre como su tiempo.

<!-- check: U1.28 -->
```sql
SELECT
    c.Nombre,
    t.Minutos,
    FIRST_VALUE(c.Nombre) OVER (ORDER BY t.Minutos, c.Nombre) AS Ganador,
    t.Minutos - FIRST_VALUE(t.Minutos) OVER (ORDER BY t.Minutos, c.Nombre) AS MinutosDeDiferencia
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 4
ORDER BY t.Minutos, c.Nombre;
```

**Resultado esperado.**

| Nombre | Minutos | Ganador | MinutosDeDiferencia |
|---|---:|---|---:|
| Nora | 96 | Nora | 0 |
| Lola | 98 | Nora | 2 |
| Omar | 100 | Nora | 4 |
| Mateo | 101 | Nora | 5 |
| Rafa | 108 | Nora | 12 |
| Sol | 110 | Nora | 14 |
| Pia | 112 | Nora | 16 |

`FIRST_VALUE` no necesita un marco especial porque la primera fila siempre está dentro del marco por defecto. Tito no aparece: abandonó antes de la etapa 4.

</details>

### Ejercicio 9 · El más lento de cada categoría
<!-- ejercicio: U1.29 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
En la etapa 2, mostrá para cada corredor el nombre del más lento de su categoría. Probá primero sin marco explícito y comprobá qué devuelve `LAST_VALUE`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos `LAST_VALUE` con la misma partición y orden: uno con el marco por defecto y otro con `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.

<!-- check: U1.29 -->
```sql
SELECT
    c.Categoria,
    c.Nombre,
    t.Minutos,
    LAST_VALUE(c.Nombre) OVER (
        PARTITION BY c.Categoria
        ORDER BY t.Minutos, c.Nombre
    ) AS MasLentoMarcoPorDefecto,
    LAST_VALUE(c.Nombre) OVER (
        PARTITION BY c.Categoria
        ORDER BY t.Minutos, c.Nombre
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS MasLento
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 2
ORDER BY c.Categoria, t.Minutos, c.Nombre;
```

**Resultado esperado.**

| Categoria | Nombre | Minutos | MasLentoMarcoPorDefecto | MasLento |
|---|---|---:|---|---|
| Amateur | Rafa | 97 | Rafa | Tito |
| Amateur | Sol | 97 | Sol | Tito |
| Amateur | Pia | 99 | Pia | Tito |
| Amateur | Tito | 104 | Tito | Tito |
| Elite | Mateo | 88 | Mateo | Omar |
| Elite | Lola | 90 | Lola | Omar |
| Elite | Nora | 91 | Nora | Omar |
| Elite | Omar | 91 | Omar | Omar |

Con el marco por defecto la última fila del marco es la fila actual: la columna `MasLentoMarcoPorDefecto` repite el nombre de cada corredor. Con el marco completo se ve el final de la partición: Tito en Amateur y Omar en Elite.

</details>

### Ejercicio 10 · Clasificación general
<!-- ejercicio: U1.30 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Calculá la clasificación general (por tiempo acumulado, el menor es el mejor) al terminar las etapas 3 y 5. Mostrá etapa, puesto, nombre y total.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos pasos en CTE: primero el acumulado por corredor y etapa; después `RANK` por etapa sobre ese acumulado. Se unen los nombres al final.

<!-- check: U1.30 -->
```sql
WITH Acumulado AS (
    SELECT
        t.CorredorId,
        t.EtapaId,
        SUM(t.Minutos) OVER (
            PARTITION BY t.CorredorId
            ORDER BY t.EtapaId
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS Total
    FROM carrera.Tiempo AS t
),
General AS (
    SELECT
        EtapaId,
        CorredorId,
        Total,
        RANK() OVER (PARTITION BY EtapaId ORDER BY Total) AS PuestoGeneral
    FROM Acumulado
)
SELECT
    g.EtapaId,
    g.PuestoGeneral,
    c.Nombre,
    g.Total
FROM General AS g
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = g.CorredorId
WHERE g.EtapaId IN (3, 5)
ORDER BY g.EtapaId, g.PuestoGeneral, c.Nombre;
```

**Resultado esperado.**

| EtapaId | PuestoGeneral | Nombre | Total |
|---:|---:|---|---:|
| 3 | 1 | Lola | 182 |
| 3 | 2 | Mateo | 183 |
| 3 | 3 | Nora | 184 |
| 3 | 4 | Omar | 188 |
| 3 | 5 | Rafa | 201 |
| 3 | 6 | Sol | 202 |
| 3 | 7 | Pia | 205 |
| 3 | 8 | Tito | 214 |
| 5 | 1 | Lola | 327 |
| 5 | 2 | Mateo | 329 |
| 5 | 2 | Nora | 329 |
| 5 | 4 | Omar | 336 |
| 5 | 5 | Rafa | 361 |
| 5 | 6 | Sol | 362 |
| 5 | 7 | Pia | 372 |

Tito figura en la etapa 3 (octavo) pero no en la 5: abandonó. Mateo y Nora empatan con 329 minutos y comparten el puesto 2; el siguiente es el 4.

</details>

### Ejercicio 11 · Media móvil y mejor marca
<!-- ejercicio: U1.31 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para Nora (3) y Omar (4), mostrá el tiempo en cada etapa, el promedio de las últimas tres etapas (la actual y las dos anteriores) y su mejor marca hasta ese momento.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `AVG` con marco `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` y `MIN` con marco acumulado, ambos particionados por corredor.

<!-- check: U1.31 -->
```sql
SELECT
    c.Nombre,
    t.EtapaId,
    t.Minutos,
    CAST(AVG(t.Minutos * 1.0) OVER (
        PARTITION BY t.CorredorId
        ORDER BY t.EtapaId
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS DECIMAL(6,2)) AS MediaMovil3,
    MIN(t.Minutos) OVER (
        PARTITION BY t.CorredorId
        ORDER BY t.EtapaId
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS MejorMarcaHastaAhora
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.CorredorId IN (3, 4)
ORDER BY c.Nombre, t.EtapaId;
```

**Resultado esperado.**

| Nombre | EtapaId | Minutos | MediaMovil3 | MejorMarcaHastaAhora |
|---|---:|---:|---:|---:|
| Nora | 1 | 64 | 64.00 | 64 |
| Nora | 2 | 91 | 77.50 | 64 |
| Nora | 3 | 29 | 61.33 | 29 |
| Nora | 4 | 96 | 72.00 | 29 |
| Nora | 5 | 49 | 58.00 | 29 |
| Omar | 1 | 66 | 66.00 | 66 |
| Omar | 2 | 91 | 78.50 | 66 |
| Omar | 3 | 31 | 62.67 | 31 |
| Omar | 4 | 100 | 74.00 | 31 |
| Omar | 5 | 48 | 59.67 | 31 |

En las dos primeras etapas el marco tiene menos de tres filas, y el promedio se calcula con las que haya (64 y 77,50 en Nora). Las etapas tienen distinto largo, así que el promedio de minutos es solo ilustrativo.

</details>

### Ejercicio 12 · Percentiles de la etapa 1
<!-- ejercicio: U1.32 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Mostrá `PERCENT_RANK` y `CUME_DIST` del tiempo de cada corredor de la etapa 1, redondeados a tres decimales. ¿Quién está en el 25 % más rápido? ¿Por qué Mateo y Nora tienen el mismo valor?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Ambas funciones sobre `ORDER BY Minutos`. Interpretamos `CUME_DIST` como la proporción de corredores con tiempo menor o igual.

<!-- check: U1.32 -->
```sql
WITH Percentil AS (
    SELECT
        c.Nombre,
        t.Minutos,
        CAST(PERCENT_RANK() OVER (ORDER BY t.Minutos) AS DECIMAL(5,3)) AS PercentRank,
        CAST(CUME_DIST()    OVER (ORDER BY t.Minutos) AS DECIMAL(5,3)) AS CumeDist
    FROM carrera.Tiempo AS t
    INNER JOIN carrera.Corredor AS c
        ON c.CorredorId = t.CorredorId
    WHERE t.EtapaId = 1
)
SELECT Nombre, Minutos, PercentRank, CumeDist
FROM Percentil
ORDER BY Minutos, Nombre;
```

**Resultado esperado.**

| Nombre | Minutos | PercentRank | CumeDist |
|---|---:|---:|---:|
| Lola | 62 | 0.000 | 0.125 |
| Mateo | 64 | 0.143 | 0.375 |
| Nora | 64 | 0.143 | 0.375 |
| Omar | 66 | 0.429 | 0.500 |
| Rafa | 69 | 0.571 | 0.625 |
| Pia | 70 | 0.714 | 0.750 |
| Sol | 72 | 0.857 | 1.000 |
| Tito | 72 | 0.857 | 1.000 |

`PERCENT_RANK` es `(puesto - 1) / (8 - 1)`: Mateo y Nora comparten el puesto 2, por eso valen `1/7 = 0,143`. `CUME_DIST` cuenta las filas con valor menor o igual: Mateo y Nora tienen 3 de 8 (0,375). Solo Lola cumple `CUME_DIST <= 0,25`; `RANK / 8` daría 0,25 para Mateo y Nora, que no es la proporción de filas con valor menor o igual. Sol y Tito, empatados en el último lugar, llegan a 1,000.

</details>
