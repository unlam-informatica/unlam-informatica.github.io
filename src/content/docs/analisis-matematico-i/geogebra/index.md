---
title: GeoGebra — Guía práctica
slug: analisis-matematico-i/geogebra
sidebar:
  order: 0
  label: Presentación
---


Guía de uso de **GeoGebra** orientada a las necesidades de Análisis Matemático I. No pretende ser exhaustiva: cubre los comandos y técnicas que más se usan en cada unidad de la cursada, con ejemplos directos de los ejercicios de las prácticas.

## ¿Por qué GeoGebra?

GeoGebra es una herramienta de matemática dinámica gratuita que combina geometría, álgebra, análisis y cálculo simbólico. En esta materia se usa para:

- **Verificar resoluciones analíticas**: graficar funciones, ver asíntotas, raíces y valores extremos sin tener que confiar en el cálculo "a mano".
- **Explorar transformaciones**: con deslizadores se puede visualizar cómo cambia una función al modificar parámetros.
- **Resolver problemas que serían tediosos a mano**: regresión sobre tablas de datos, máximos de funciones cúbicas, polinomios de Taylor de orden alto, etc.

## Cómo acceder

Tres opciones:

- **Online (recomendado para empezar):** [geogebra.org/calculator](https://www.geogebra.org/calculator). No requiere instalación, funciona en cualquier navegador.
- **Aplicación de escritorio:** descargar **GeoGebra Classic 6** desde [geogebra.org/download](https://www.geogebra.org/download). Lo mismo que la versión web pero offline.
- **App móvil:** disponible en Play Store y App Store, útil para consultas rápidas pero menos cómoda para ejercicios largos.

Para el trabajo de esta materia, usar **GeoGebra Classic** (web o escritorio) — es la versión que tiene todas las vistas (Algebraica, Gráfica, CAS, Hoja de Cálculo) integradas.

## Índice de la guía

| Sección | Contenido |
|---------|-----------|
| [Primeros pasos](/analisis-matematico-i/geogebra/basico/) | Interfaz, vistas, barra de entrada, deslizadores, configuración en español |
| [Funciones (Unidad 1)](/analisis-matematico-i/geogebra/funciones/) | Graficar, restringir dominio, raíces, transformaciones, función inversa, regresión |
| [Límites y continuidad (Unidad 2)](/analisis-matematico-i/geogebra/limites-continuidad/) | Comandos `Límite`, laterales, asíntotas, visualizar discontinuidades |
| [Derivada (Unidad 3)](/analisis-matematico-i/geogebra/derivada/) | Derivadas simbólicas, rectas tangentes, optimización, derivación implícita |
| [Polinomio de Taylor (Unidad 4)](/analisis-matematico-i/geogebra/taylor/) | `PolinomioTaylor`, Maclaurin, aproximaciones, comparación con la función |


## Convención de notación

A lo largo de la guía:

- Los **comandos** de GeoGebra van con tipografía monoespaciada: `Raíz(f)`, `Derivada(g, x, 2)`.
- Los nombres de comandos en GeoGebra en español **no llevan acentos** en la entrada (aunque en pantalla se muestren acentuados): por ejemplo, escribir `Raiz(f)` también funciona.
- Las **mayúsculas y minúsculas importan** en los nombres de objetos (`f` y `F` son objetos distintos), pero **no** en los comandos (`Derivada` y `derivada` son equivalentes en GeoGebra Classic).
- En GeoGebra el separador de argumentos es **coma** (`,`) salvo cuando el idioma está configurado en español y el separador decimal es coma — en ese caso el separador de argumentos cambia automáticamente a **punto y coma** (`;`). Ver la sección [Primeros pasos](/analisis-matematico-i/geogebra/basico/) para configurar esto.
