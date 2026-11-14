---
title: Ejercicio 12 * — Costo $C(x)=5000+10x+0{,}05x^2$
slug: analisis-matematico-i/unidad-2/practica/ejercicio-12
sidebar:
  order: 12
  label: Ejercicio 12
---


## 12a
Razón de cambio media

$\dfrac{C(x_2)-C(x_1)}{x_2-x_1}$.

- $C(100)=5000+1000+0{,}05\cdot 10000=6500$.
- $C(105)=5000+1050+0{,}05\cdot 11025=5000+1050+551{,}25=6601{,}25$.
- $C(101)=5000+1010+0{,}05\cdot 10201=5000+1010+510{,}05=6520{,}05$.



$$
[100,105]:\ \dfrac{6601{,}25-6500}{5}=\dfrac{101{,}25}{5}=\mathbf{20{,}25\ \$/\text{artículo}};\qquad [100,101]:\ \dfrac{6520{,}05-6500}{1}=\mathbf{20{,}05\ \$/\text{artículo}}
$$



## 12b
Razón instantánea en $a=100$



$$
\lim_{h\to0}\dfrac{C(100+h)-C(100)}{h}
$$



$C(100+h)-C(100)=10h+0{,}05\big((100+h)^2-100^2\big)=10h+0{,}05(200h+h^2)=10h+10h+0{,}05h^2=20h+0{,}05h^2.$



$$
\lim_{h\to0}\dfrac{20h+0{,}05h^2}{h}=\lim_{h\to0}(20+0{,}05h)=\mathbf{20\ \$/\text{artículo}}
$$



**Interpretación.** Producir un artículo adicional alrededor del nivel $x=100$ cuesta aproximadamente $\text{\char36}20$ (costo marginal).

✓ Coincide con la respuesta oficial.

