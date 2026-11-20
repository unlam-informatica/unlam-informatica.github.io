---
title: Unidad 6 — Calidad en bases de datos
slug: bbdd-aplicadas/unidad-6/teoria
description: "Ley 25.326, RGPD e ISO/IEC 25012, con medición de calidad y gobierno de datos como complemento: ruta de estudio, prácticas y repaso."
sidebar:
  hidden: true
  label: Presentación y ruta
---

Esta unidad estudia dos preguntas sobre los datos: si sirven para el propósito previsto (calidad) y si es legítimo y seguro tratarlos (protección de datos personales). Retoma la [Unidad 5](/bbdd-aplicadas/unidad-5/teoria/): el mínimo privilegio, los roles y las copias de seguridad son los mecanismos técnicos con los que se cumplen las exigencias de seguridad de las normas.

La unidad se apoya en fuentes de distinto carácter:

- **Normas jurídicas (fuentes primarias):** la Ley 25.326 y su Decreto Reglamentario 1558/2001, y el Reglamento (UE) 2016/679 (RGPD).
- **Estándar técnico:** ISO/IEC 25012, un modelo de calidad de datos. Es una norma paga: estos apuntes usan un resumen público (fuente secundaria) y definiciones propias, y no la presentan como norma jurídica.
- **Prácticas recomendadas complementarias:** la medición de la calidad y el gobierno de datos. No figuran en el programa 2024 ni en las fuentes normativas de la unidad.

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- distinguir dato personal, dato sensible y dato anónimo, y explicar por qué se protegen;
- aplicar los principios, derechos, obligaciones y sanciones de la Ley 25.326 a un caso;
- determinar cuándo se aplica el GDPR y reconocer sus actores, bases jurídicas, derechos, transferencias y multas;
- clasificar las 15 características de ISO/IEC 25012 según su perspectiva inherente o dependiente del sistema;
- relacionar calidad, privacidad y seguridad de un dato con los artículos y características que corresponden.

*Complementario (no figura en las fuentes normativas de la unidad):* convertir una necesidad de calidad en una regla medible y gobernar los datos durante su ciclo de vida.

## Antes de comenzar

- **Conviene repasar:** [Seguridad, usuarios y permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/) (mínimo privilegio, roles y permisos), [Backups, restauración, RPO y RTO](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/) y [Cifrado en reposo y en tránsito](/bbdd-aplicadas/unidad-5/teoria/cifrado/) (Unidad 5), y el [repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/) para las consultas de los laboratorios.
- **Herramientas:** una instancia de SQL Server de laboratorio para los laboratorios (datos sintéticos). La parte normativa no requiere herramientas. Más opciones en [Cómo estudiar · Herramientas](/bbdd-aplicadas/como-estudiar/#herramientas).

## Ruta de aprendizaje

Seguí las etapas en orden. Cada una indica qué leer y, cuando existe, qué practicar antes de pasar a la siguiente. El [resumen integrador](/bbdd-aplicadas/unidad-6/teoria/apunte-completo/) sirve como vista general antes de empezar.

### 1. Protección de datos personales en Argentina: Ley 25.326

Norma jurídica. Datos personales y sensibles, principios, consentimiento, derechos del titular, seguridad, registro, sanciones y hábeas data.

- **Leé:** [Ley 25.326 — Protección de los datos personales](/bbdd-aplicadas/unidad-6/teoria/ley-25326/)
- **Practicá:** los [ejercicios de la lección](/bbdd-aplicadas/unidad-6/teoria/ley-25326/#ejercicios).
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-6/teoria/ley-25326/#autoevaluación)

### 2. Reglamento General de Protección de Datos (RGPD)

Norma jurídica de la Unión Europea que puede alcanzar a una empresa argentina: ámbito de aplicación, principios, bases de licitud, derechos, actores, transferencias, brechas y multas, con una comparación con la ley argentina.

- **Leé:** [GDPR — Reglamento General de Protección de Datos](/bbdd-aplicadas/unidad-6/teoria/gdpr/)
- **Practicá:** los [ejercicios de la lección](/bbdd-aplicadas/unidad-6/teoria/gdpr/#ejercicios).
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-6/teoria/gdpr/#autoevaluación)

### 3. Calidad de los datos: ISO/IEC 25012

Estándar técnico, no norma jurídica. Las 15 características de calidad en tres grupos y las relaciones entre ellas; da el vocabulario para decir de qué manera están mal los datos.

- **Leé:** [ISO/IEC 25012 — Modelo de calidad de datos](/bbdd-aplicadas/unidad-6/teoria/iso-25012/)
- **Practicá:** los [ejercicios de la lección](/bbdd-aplicadas/unidad-6/teoria/iso-25012/#ejercicios).
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-6/teoria/iso-25012/#autoevaluación)

### 4. Medición y mejora de la calidad (complementario)

*Complementario: no forma parte del programa 2024; podés saltearlo en una primera lectura.* Práctica recomendada, no norma: cómo convertir una característica de ISO/IEC 25012 en una regla medible, con perfilado en T-SQL.

- **Leé:** [Medición y mejora de la calidad](/bbdd-aplicadas/unidad-6/teoria/medicion-calidad/)
- **Practicá:** [Laboratorio — Perfilado, reglas y métricas](/bbdd-aplicadas/unidad-6/practica/laboratorio-calidad/), ejercicios 16 a 22.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-6/teoria/medicion-calidad/#autoevaluación)

### 5. Gobierno, privacidad y calidad desde el diseño (complementario)

*Complementario: no forma parte del programa 2024; podés saltearlo en una primera lectura.* Prácticas recomendadas, no normas: roles, inventario, linaje, retención y privacidad desde el diseño, como forma de aplicar la ley y el RGPD.

- **Leé:** [Gobierno, privacidad y calidad desde el diseño](/bbdd-aplicadas/unidad-6/teoria/gobierno-privacidad/)
- **Practicá:** [Laboratorio — Inventario, minimización y derechos](/bbdd-aplicadas/unidad-6/practica/laboratorio-privacidad/), ejercicios 23 a 28. Presupone la Ley 25.326, el RGPD y esta lección.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-6/teoria/gobierno-privacidad/#autoevaluación)

### 6. Aplicación a casos integradores

Resolvé los [casos integradores](/bbdd-aplicadas/unidad-6/practica/casos-integradores/) combinando ley, RGPD, ISO/IEC 25012, medición y gobierno con la plantilla de análisis de la página. Presuponen las cinco etapas anteriores; los ejercicios 29 y 30 usan SQL Server.

### 7. Repaso y cierre integrador

- **Leé:** [Guía de repaso — Unidad 6](/bbdd-aplicadas/unidad-6/teoria/guia-parcial/): comparaciones, preguntas de desarrollo, casos resueltos, errores frecuentes y simulacro.

## Ejercicios y laboratorios

Los laboratorios y los casos son material de práctica propio: aplican contenidos del programa 2024 (Ley 25.326, GDPR e ISO/IEC 25012) con técnicas de SQL Server, métricas y plazos que son elaboración propia y no figuran en la norma.

- **[Laboratorio — Perfilado, reglas y métricas](/bbdd-aplicadas/unidad-6/practica/laboratorio-calidad/)** · 7 ejercicios — perfilado, reglas entre tablas, actualidad, restricciones y los límites de la medición con SQL.
- **[Laboratorio — Inventario, minimización y derechos](/bbdd-aplicadas/unidad-6/practica/laboratorio-privacidad/)** · 6 ejercicios — clasificación de datos, seudonimización, enmascaramiento, retención y derecho de acceso.
- **[Casos integradores — Calidad, privacidad y gobierno](/bbdd-aplicadas/unidad-6/practica/casos-integradores/)** · 2 ejercicios con SQL dentro de cinco casos resueltos.

Detalle en el [índice de prácticas](/bbdd-aplicadas/unidad-6/practica/).

## Autoevaluación y repaso

- Cada lección termina con una autoevaluación, enlazada en la ruta.
- El [resumen integrador](/bbdd-aplicadas/unidad-6/teoria/apunte-completo/) es una vista general antes de empezar y un repaso después; cada sección enlaza a su lección.
- La [guía de repaso](/bbdd-aplicadas/unidad-6/teoria/guia-parcial/) prepara el trabajo práctico integrador y el examen final: según el programa 2024, esta unidad no integra el parcial.

## Continuar

Con esta unidad se cierra el recorrido de la materia. Cuando puedas aplicar la ley, el RGPD e ISO/IEC 25012 a un caso nuevo sin mirar la resolución, pasá al repaso integrador de toda la materia: [Cómo estudiar · Repasar para un examen](/bbdd-aplicadas/como-estudiar/#repasar-para-un-examen). Después preparate para el examen final, que abarca todas las unidades, y para el trabajo práctico integrador.

## Fuentes de la unidad

La unidad se sustenta en fuentes primarias, consultadas el 2026-11-17: [Ley 25.326](https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm) y [Decreto 1558/2001](https://servicios.infoleg.gob.ar/infolegInternet/anexos/70000-74999/70368/norma.htm) en InfoLEG, [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679) en EUR-Lex y el [resumen público de ISO/IEC 25012](https://iso25000.com/index.php/normas-iso-25000/iso-25012). Sitio personal y no oficial; no sustituye asesoramiento jurídico.
