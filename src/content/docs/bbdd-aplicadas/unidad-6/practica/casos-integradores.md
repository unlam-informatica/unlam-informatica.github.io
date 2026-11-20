---
title: Casos integradores — Calidad, privacidad y gobierno
slug: bbdd-aplicadas/unidad-6/practica/casos-integradores
sidebar:
  order: 3
---

[← Unidad 6](/bbdd-aplicadas/unidad-6/teoria/)

Cinco casos propios, con empresas y datos ficticios, que combinan normativa ([Ley 25.326](/bbdd-aplicadas/unidad-6/teoria/ley-25326/) y [RGPD](/bbdd-aplicadas/unidad-6/teoria/gdpr/)), características de [ISO/IEC 25012](/bbdd-aplicadas/unidad-6/teoria/iso-25012/) y medición. Son enunciados originales, no reconstruyen exámenes. Los casos 3 y 5 incluyen una comprobación en SQL Server; los otros se resuelven por razonamiento.

:::note[Contenido complementario]
La plantilla de análisis, las métricas y los umbrales son elaboración propia para practicar; ISO/IEC 25012 y las normas no los prescriben. Material académico: no sustituye asesoramiento jurídico.
:::

## Plantilla de análisis

Usá siempre este orden:

1. datos, sensibilidad y actores;
2. finalidad, jurisdicción y base;
3. principios legales comprometidos (con artículo);
4. características ISO afectadas;
5. regla, fórmula, población, frecuencia y umbral;
6. controles preventivos, detectivos y correctivos;
7. responsable, evidencia, derechos y retención.

## Caso 1 — Universidad

:::note[Enunciado]
Una universidad ficticia publica un CSV con nombre, DNI, nota y condición académica de sus estudiantes. Algunos DNI pertenecen a otras personas y las notas se actualizaron solo en el sistema interno. Analizá el caso con la plantilla.
:::

<details>
<summary>Resolución</summary>

1. **Datos y actores.** Nombre, DNI, nota y condición son datos personales (Ley art. 2; RGPD art. 4.1). No son sensibles (art. 2 y 7 de la Ley; art. 9.1 del RGPD), pero la publicación los expone a terceros indeterminados. Actores: la universidad (responsable), los estudiantes (titulares) y quien descarga el archivo.
2. **Finalidad y base.** Hay que identificar para qué se publica y con qué habilitación. Nombre y DNI figuran entre los datos que el art. 5.2.c de la Ley exceptúa de consentimiento al recabarlos, pero eso no habilita por sí solo difundirlos con la nota: la comunicación a terceros es una cesión que requiere habilitación (art. 11) y la finalidad debe ser compatible con la de origen (art. 4.3).
3. **Principios comprometidos.** Exactitud y actualización (art. 4, incisos 4 y 5): hay DNI de otras personas y notas desactualizadas. Datos no excesivos (art. 4.1): el DNI completo probablemente no es necesario para publicar una nota. Seguridad y confidencialidad (art. 9.1; art. 10). En el RGPD: exactitud (5.1.d), minimización (5.1.c) e integridad y confidencialidad (5.1.f), si fuera aplicable.
4. **ISO.** **Exactitud** (DNI y notas), **consistencia** entre las dos fuentes, **actualidad**, **confidencialidad** y **conformidad** con la norma de privacidad.
5. **Medición.** Calificaciones coincidentes entre el acta y la publicación ÷ calificaciones contrastadas × 100. Umbral propuesto (criterio del caso): 100 % antes de publicar; si hay menos, no se publica.
6. **Controles.** Correctivo: retirar o restringir el archivo, evaluar la exposición, corregir contra las actas autorizadas y propagar. Preventivo: publicar con un identificador que no identifique directamente (si la finalidad lo permite), generar el archivo desde la fuente oficial y exigir doble validación y aprobación. Detectivo: reconciliar acta y publicación en cada corte.
7. **Responsable y evidencia.** El owner de las calificaciones aprueba; se conserva el registro de la verificación. La rectificación de los titulares afectados corre en 5 días hábiles desde el reclamo (art. 16) y debe notificarse a quienes recibieron los datos.
</details>

## Caso 2 — Banco y puntaje automático

:::note[Enunciado]
Un banco ficticio rechaza automáticamente solicitudes de crédito por un domicilio desactualizado que compró a un tercero. No puede explicar qué versión del modelo produjo cada decisión. Analizá el caso con la plantilla.
:::

<details>
<summary>Resolución</summary>

1. **Datos.** Domicilio y perfil crediticio son datos personales; no sensibles según el art. 2 de la Ley. Actores: el banco, el tercero que vendió los datos y los solicitantes.
2. **Base y fuente.** Los datos obtenidos de un tercero exigen revisar la licitud de la fuente (art. 4.2: no se recolectan por medios desleales) y la cesión (art. 11: consentimiento y finalidad informada, con las excepciones de la ley). Si la solicitante está en la Unión, el RGPD agrega los deberes de información (arts. 13 y 14) y el derecho a no ser objeto de decisiones basadas únicamente en tratamiento automatizado con efectos jurídicos o similares (art. 22, con excepciones).
3. **Principios.** Exactitud y actualización (Ley art. 4, incisos 4 y 5; RGPD 5.1.d), rectificación a pedido (Ley art. 16, 5 días hábiles; RGPD art. 16) y, para el RGPD, responsabilidad proactiva (5.2): poder demostrar cómo se decidió.
4. **ISO.** **Actualidad** y **exactitud** del domicilio, **credibilidad** de la fuente, **trazabilidad** (qué versión del modelo y qué entradas), **comprensibilidad** de la explicación y **conformidad**.
5. **Medición.** Domicilios verificados dentro de la ventana ÷ domicilios evaluados; decisiones con versión del modelo, entradas y explicación registradas ÷ decisiones automatizadas. Umbrales: los fija el owner según el riesgo; para la segunda métrica, un valor inferior al 100 % indica decisiones que no se pueden reconstruir.
6. **Controles.** Preventivo: fuentes autorizadas, fecha y procedencia en cada dato, versionado del modelo. Detectivo: auditoría de una muestra de rechazos. Correctivo: revisión humana de las decisiones afectadas, canal de impugnación y propagación de las correcciones.
</details>

## Caso 3 — Pulsera deportiva

:::note[Enunciado]
Una pulsera ficticia registra pulso y ubicación cada segundo, aunque la función contratada solo cuenta pasos. Los datos se conservan cinco años y se venden "agregados", pero los grupos muy pequeños permiten identificar usuarios. Analizá el caso con la plantilla. Después, resolvé el ejercicio 29.
:::

<details>
<summary>Resolución</summary>

1. **Datos.** El pulso es información de salud (dato sensible, Ley art. 2 y 7; categoría especial, RGPD art. 9.1) y la ubicación es un dato personal. Con la función de contar pasos, esa granularidad parece excesiva (Ley art. 4.1: "no excesivos"; RGPD art. 5.1.c).
2. **Principios.** Finalidad (Ley art. 4.3; RGPD 5.1.b), conservación: los datos deben destruirse cuando dejan de ser necesarios (Ley art. 4.7; RGPD 5.1.e). Cinco años sin una finalidad que lo justifique no cumple ese estándar. La venta es una cesión (art. 11).
3. **Agregar no equivale a anonimizar.** La Ley habla de disociación (art. 2): que la información no pueda asociarse a una persona determinable. Un agregado con grupos chicos o combinaciones raras no la garantiza.
4. **ISO.** **Confidencialidad** y **conformidad**; también la **precisión** innecesaria, que aumenta el riesgo y el costo sin beneficio.
5. **Rediseño.** Frecuencia mínima de captura, función de salud como opcional y separada, procesamiento local, umbral de tamaño de grupo comprobado, retención corta y prohibición contractual de reidentificar.
</details>

### Ejercicio 29 · Tamaño mínimo de grupo en un agregado
<!-- ejercicio: U6.29 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con la tabla `pulsera.Usuario` (zona, rango de edad y pasos diarios), calculá el promedio de pasos por zona y rango de edad y decidí qué grupos se publican con un mínimo de tres personas por grupo (el umbral es un criterio del ejercicio). Los grupos que no alcancen el mínimo se suprimen.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Medir el tamaño de cada grupo del agregado: un grupo con pocos integrantes permite señalar a una persona aunque no figure su nombre. Se agrupa y se publica el promedio solo si `COUNT(*)` alcanza el mínimo. El bloque crea el esquema `pulsera` y los datos sintéticos, así que ejecutalo completo en una [base de práctica](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos).

<!-- check: U6.29 -->
```sql
CREATE SCHEMA pulsera;
GO

CREATE TABLE pulsera.Usuario (
    UsuarioId INT         NOT NULL,
    Zona      VARCHAR(10) NOT NULL,
    RangoEdad VARCHAR(10) NOT NULL,
    PasosDia  INT         NOT NULL,
    CONSTRAINT PK_Usuario PRIMARY KEY CLUSTERED (UsuarioId)
);

INSERT INTO pulsera.Usuario (UsuarioId, Zona, RangoEdad, PasosDia)
VALUES
    (1,  'Zona A', '20-29', 6000),
    (2,  'Zona A', '20-29', 8000),
    (3,  'Zona A', '20-29', 7000),
    (4,  'Zona A', '20-29', 9000),
    (5,  'Zona A', '30-39', 5000),
    (6,  'Zona A', '30-39', 6000),
    (7,  'Zona A', '30-39', 7000),
    (8,  'Zona B', '20-29', 4000),
    (9,  'Zona B', '20-29', 12000),
    (10, 'Zona B', '60-69', 3000);
GO

DECLARE @MinimoPorGrupo INT = 3;

SELECT
    Zona,
    RangoEdad,
    COUNT(*) AS Usuarios,
    CASE WHEN COUNT(*) >= @MinimoPorGrupo
         THEN CAST(AVG(1.0 * PasosDia) AS DECIMAL(8, 1)) END AS PasosPromedio,
    CASE WHEN COUNT(*) >= @MinimoPorGrupo THEN 'Publicar' ELSE 'Suprimir' END AS Decision
FROM pulsera.Usuario
GROUP BY Zona, RangoEdad
ORDER BY Zona, RangoEdad;
```

**Resultado esperado.**

| Zona | RangoEdad | Usuarios | PasosPromedio | Decision |
|---|---|---:|---:|---|
| Zona A | 20-29 | 4 | 7500.0 | Publicar |
| Zona A | 30-39 | 3 | 6000.0 | Publicar |
| Zona B | 20-29 | 2 | NULL | Suprimir |
| Zona B | 60-69 | 1 | NULL | Suprimir |

El grupo de "Zona B, 60-69" tiene un solo integrante: publicar su promedio equivale a publicar sus pasos. Suprimir los grupos de menos de tres es un **control preventivo** razonable, pero no una prueba de anonimato: otros atributos o datos externos pueden reidentificar aun con grupos grandes, de modo que el umbral se valida con un análisis de riesgo y se mantiene la prohibición contractual de reidentificar.
</details>

## Caso 4 — Migración a un lago de datos

:::note[Enunciado]
Después de migrar de SQL Server a un lago de datos, las fechas perdieron la zona horaria, los decimales se redondearon y no existe un mapa entre las columnas antiguas y las nuevas. El nuevo entorno tiene alta disponibilidad. Analizá el caso con la plantilla.
:::

<details>
<summary>Resolución</summary>

1. **Idea central.** La alta disponibilidad no compensa una migración deficiente: asegura que los datos estén accesibles, no que sean correctos.
2. **ISO.** **Portabilidad** (los datos no se movieron preservando su significado), **precisión** y **exactitud** (decimales y zona horaria), **trazabilidad** (no hay linaje), **comprensibilidad** (no hay metadatos que expliquen las columnas) y **consistencia** con el sistema de origen. **Disponibilidad**, en cambio, no está afectada.
3. **Normativa.** Si los datos son personales, la exactitud (Ley art. 4.4; RGPD 5.1.d) y la seguridad (Ley art. 9; RGPD art. 32) se aplican también al destino, y los derechos de rectificación y acceso requieren poder ubicar cada dato.
4. **Medición.** Reconciliación por totales y por muestra: sumas de importes y recuentos por columna en origen y destino. Umbral propuesto: diferencia cero en los importes y cero fechas sin zona horaria.
5. **Controles.** Preventivos: contrato de esquema con tipos, precisión y zona horaria; catálogo de unidades. Detectivos: reconciliación y pruebas de ida y vuelta antes del corte. Correctivos: reprocesar desde el origen y criterios de aceptación previos al apagado del sistema anterior.
</details>

## Caso 5 — Backup restaurado

:::note[Enunciado]
Una empresa ficticia recibe un pedido de supresión válido, lo ejecuta en producción y seis meses después restaura una copia de seguridad antigua para investigar otra falla. El dato reaparece y vuelve a alimentar las campañas de marketing. Analizá el caso con la plantilla. Después, resolvé el ejercicio 30.
:::

<details>
<summary>Resolución</summary>

La copia de seguridad puede conservarse por continuidad operativa según la política, pero no debe reactivar usos incompatibles. Se necesita un **registro mínimo de supresiones** (solo el identificador interno y la fecha, sin datos personales adicionales), un procedimiento posterior a la restauración y un filtro que impida las campañas hasta reconciliar. Es una práctica propuesta aquí, no una obligación legal expresa.

1. **Normativa.** La supresión (Ley art. 16; RGPD art. 17) y la destrucción cuando los datos ya no son necesarios (Ley art. 4.7; RGPD art. 5.1.e). El RGPD pide además que el responsable pueda demostrar el cumplimiento (art. 5.2).
2. **ISO.** La **recuperabilidad** se logró, pero fallaron la **conformidad** (con la obligación de suprimir), la **actualidad** y la **consistencia** entre el estado jurídico y el estado restaurado.
3. **Controles.** Preventivo: la vista de destinatarios de campaña excluye siempre los identificadores del registro de supresiones. Correctivo: el procedimiento post-restauración reaplica las supresiones. Detectivo: un control que cuente "reaparecidos" y falle si es mayor que cero. Además, vencimiento de las copias por rotación.
</details>

### Ejercicio 30 · Reaplicar supresiones después de restaurar
<!-- ejercicio: U6.30 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Tras restaurar una copia antigua, la tabla `comercial.Cliente` contiene clientes que ya habían sido suprimidos; el registro mínimo `comercial.RegistroSupresion` conserva solo su identificador y la fecha. Creá una vista de destinatarios de campaña que excluya a los suprimidos, reaplicá las supresiones sobre la tabla restaurada y mostrá indicadores de control, incluyendo cuántos "reaparecidos" quedan.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Primero la defensa preventiva (la vista excluye siempre los identificadores del registro); luego el procedimiento correctivo (`DELETE ... OUTPUT` para contar lo reaplicado) y un control detectivo de reaparecidos que debe ser cero. El bloque crea el esquema `comercial` con los clientes restaurados y el registro de supresiones, así que ejecutalo completo en una base de práctica (puede ser la misma del ejercicio anterior).

<!-- check: U6.30 -->
```sql
CREATE SCHEMA comercial;
GO

CREATE TABLE comercial.Cliente (
    ClienteId      INT          NOT NULL,
    Email          VARCHAR(120) NOT NULL,
    AptoMarketing  BIT          NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE comercial.RegistroSupresion (
    ClienteId        INT  NOT NULL,
    FechaSupresion   DATE NOT NULL,
    CONSTRAINT PK_RegistroSupresion PRIMARY KEY CLUSTERED (ClienteId)
);

-- Estado "restaurado" desde una copia antigua: incluye clientes ya suprimidos
INSERT INTO comercial.Cliente (ClienteId, Email, AptoMarketing)
VALUES
    (1, 'cliente01@ejemplo.test', 1),
    (2, 'cliente02@ejemplo.test', 1),
    (3, 'cliente03@ejemplo.test', 1),
    (4, 'cliente04@ejemplo.test', 1),
    (5, 'cliente05@ejemplo.test', 0);

INSERT INTO comercial.RegistroSupresion (ClienteId, FechaSupresion)
VALUES (2, '2026-01-15'), (4, '2026-02-10');
GO

CREATE VIEW comercial.DestinatarioCampana
AS
SELECT c.ClienteId, c.Email
FROM comercial.Cliente AS c
WHERE c.AptoMarketing = 1
  AND NOT EXISTS (SELECT 1 FROM comercial.RegistroSupresion AS r WHERE r.ClienteId = c.ClienteId);
GO

DECLARE @Restaurados INT = (SELECT COUNT(*) FROM comercial.Cliente);
DECLARE @DestinatariosAntes INT = (SELECT COUNT(*) FROM comercial.DestinatarioCampana);
DECLARE @Aplicadas TABLE (ClienteId INT NOT NULL);

DELETE c
OUTPUT deleted.ClienteId INTO @Aplicadas
FROM comercial.Cliente AS c
WHERE EXISTS (SELECT 1 FROM comercial.RegistroSupresion AS r WHERE r.ClienteId = c.ClienteId);

SELECT Orden, Indicador, Valor
FROM (
    SELECT 1 AS Orden, 'Clientes restaurados' AS Indicador, @Restaurados AS Valor
    UNION ALL
    SELECT 2, 'Destinatarios de campaña con el filtro', @DestinatariosAntes
    UNION ALL
    SELECT 3, 'Supresiones reaplicadas', COUNT(*) FROM @Aplicadas
    UNION ALL
    SELECT 4, 'Clientes tras reaplicar', COUNT(*) FROM comercial.Cliente
    UNION ALL
    SELECT 5, 'Reaparecidos (debe ser 0)', COUNT(*)
    FROM comercial.Cliente AS c
    JOIN comercial.RegistroSupresion AS r ON r.ClienteId = c.ClienteId
) AS Control
ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Indicador | Valor |
|---:|---|---:|
| 1 | Clientes restaurados | 5 |
| 2 | Destinatarios de campaña con el filtro | 2 |
| 3 | Supresiones reaplicadas | 2 |
| 4 | Clientes tras reaplicar | 3 |
| 5 | Reaparecidos (debe ser 0) | 0 |

De los 5 clientes restaurados, solo 2 son destinatarios (los clientes 1 y 3): el 5 no es apto por su propia preferencia y el 2 y el 4 están suprimidos aunque tengan `AptoMarketing = 1`. Sin el filtro de la vista habría **4** destinatarios, dos de ellos suprimidos que reaparecieron con la restauración. Después de reaplicar, quedan 3 clientes y ninguno figura en el registro. El registro conserva solo `ClienteId` y fecha: es la información mínima para no repetir el error, y debe protegerse y documentarse como una excepción justificada.
</details>

## Actividad final

Elegí dos casos y escribí una respuesta de una carilla por caso. Cada afirmación debe identificar una norma o principio con su artículo, o una característica concreta de ISO/IEC 25012. No alcanza con decir "hay que mejorar la seguridad" o "los datos tienen mala calidad".

## Fuentes

- Ley 25.326: [InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm), consultada el 2026-11-17.
- Reglamento (UE) 2016/679: [EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679), consultado el 2026-11-17.
- Resumen público de ISO/IEC 25012: [iso25000.com](https://iso25000.com/index.php/normas-iso-25000/iso-25012).
