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

## Estado de la implementación

La rama `parte-3-lcs` agrega `src/lcs.py`, sus pruebas y una prueba de integración preparada. Aún faltan las entregas de Parte 1 (`kmp.py`, `io_utils.py`, `examples/`) y Parte 2 (`manacher.py`, `main.py`). Por eso el programa completo todavía no se puede ejecutar.

`lcs.py` importa `kmp.prefix_function` con la firma acordada; no incluye una implementación alternativa. Las pruebas se omiten explícitamente cuando falta su dependencia. Una prueba omitida no cuenta como aprobada.

## Cómo correrlo

Python 3.9 o superior. Los siguientes comandos usan `python3`; si tu instalación usa `python`, sustituye el nombre.

Una vez integradas las Partes 1 y 2, coloca los cinco archivos en el directorio actual y ejecuta:

```bash
python3 src/main.py
```

Tests:

```bash
python3 -m unittest discover -s tests -v
```

Pruebas de esta parte:

```bash
python3 -m unittest tests.test_lcs -v
python3 -m unittest tests.test_main -v
```

La prueba de integración ejecuta `src/main.py` desde `tests/fixtures/integration/` y compara exactamente nueve líneas. Esa carpeta contiene datos propios de prueba, sin sustituir los futuros archivos `examples/` de Parte 1. Las transmisiones limpias son `0ABACDEF` y `9ABAFDEF`; los patrones son `ABA`, `DEF` y `123`. La salida calculada a mano es:

```text
true 2
true 6
false
true 2
true 6
false
2 4
2 4
2 4
```

`ABA` y `DEF` tienen longitud 3; el desempate elige `ABA`, que empieza en la posición 2 de la primera transmisión. En ambas transmisiones, el mayor palíndromo también es `ABA`.

## Pendientes para cerrar #3

- Integrar KMP y `read_clean` de Ricky y repetir las pruebas con esas funciones reales.
- Añadir el caso de `examples/` leído con `read_clean`, con posiciones verificadas a mano sobre los ejemplos definitivos.
- Integrar `main.py` y Manacher de Jp, ejecutar la prueba end-to-end y comprobar que el principal llama al algoritmo real de LCS, sin stubs.
- Medir con KMP real el caso de aproximadamente 2000 caracteres (menos de 10 segundos).
- Revisar el PR de Ricky con dos comentarios útiles; abrir el PR de esta rama con `Closes #3`, obtener una aprobación e integrar.

## Documentación

- [`docs/ESPECIFICACION.md`](docs/ESPECIFICACION.md) — formato exacto y asunciones
- [`docs/ALGORITMOS.md`](docs/ALGORITMOS.md) — KMP, Manacher y substring común con KMP
- [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md) — módulos y firmas
- [`docs/REPARTO.md`](docs/REPARTO.md) — reparto del trabajo y flujo de ramas/PR

## Equipo

Máximo 3 integrantes. Ver `docs/REPARTO.md` y los issues del repositorio.
