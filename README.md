# Actividad Integradora 1 — Análisis de transmisiones

Programa en **Python** que analiza dos archivos de transmisión (`transmission1.txt`, `transmission2.txt`) en busca de código malicioso, código "espejeado" y similitud entre ellas.

Los archivos contienen únicamente caracteres `0-9`, `A-F` y saltos de línea. Los nombres son fijos y deben estar en la misma carpeta desde donde se ejecuta el programa:

```
transmission1.txt  transmission2.txt
mcode1.txt  mcode2.txt  mcode3.txt
```

## Qué hace

| Parte | Problema | Algoritmo |
|---|---|---|
| 1 | ¿Cada `mcodeY` está contenido en cada `transmissionX`? Si sí, en qué posición inicia | **KMP** |
| 2 | Palíndromo (a nivel de caracteres) más largo de cada transmisión | **Manacher** |
| 3 | Substring común más largo entre ambas transmisiones | **KMP** sobre cada sufijo |

## Salida esperada

```
true 15        <- transmission1 contiene mcode1, inicia en la posición 15
false          <- transmission1 no contiene mcode2
...            (6 líneas: t1×m1, t1×m2, t1×m3, t2×m1, t2×m2, t2×m3)
3 9            <- palíndromo más largo de transmission1 (inicio fin)
10 20          <- palíndromo más largo de transmission2
4 12           <- substring común más largo, posiciones en transmission1
```

Todas las posiciones inician en **1**.

## Cómo correrlo

```bash
python src/main.py
```

Tests:

```bash
python -m unittest discover tests
```

## Documentación

- [`docs/ESPECIFICACION.md`](docs/ESPECIFICACION.md) — formato exacto y asunciones
- [`docs/ALGORITMOS.md`](docs/ALGORITMOS.md) — KMP, Manacher y substring común con KMP
- [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md) — módulos y firmas
- [`docs/REPARTO.md`](docs/REPARTO.md) — reparto del trabajo y flujo de ramas/PR

## Equipo

Máximo 3 integrantes. Ver `docs/REPARTO.md` y los issues del repositorio.
