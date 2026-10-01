# Actividad Integradora 1 — Análisis de transmisiones

Programa en Python que analiza dos transmisiones para encontrar código malicioso, palíndromos y el substring común más largo. Usa solo la biblioteca estándar.

| Parte | Resultado | Algoritmo |
|---|---|---|
| 1 | Primera aparición de cada uno de los tres códigos en cada transmisión | KMP |
| 2 | Mayor palíndromo de cada transmisión | Manacher |
| 3 | Mayor substring común, con posiciones en transmission1 | KMP sobre cada sufijo |

## Requisitos y ejecución

Python **3.10 o superior**, por las anotaciones `int | None`. Si tu instalación usa `python` en vez de `python3`, sustituye el nombre en los comandos.

Desde la raíz del repositorio, coloca los cinco archivos con estos nombres:

```text
transmission1.txt
transmission2.txt
mcode1.txt
mcode2.txt
mcode3.txt
```

Para probar con los ejemplos incluidos:

```bash
cp examples/*.txt .
python3 src/main.py
```

Los archivos contienen `0-9`, `A-F` y saltos de línea. `read_clean` elimina `\n` y `\r`; las posiciones se cuentan en la cadena limpia. `main.py` busca los archivos en el directorio de ejecución.

## Salida

Se imprimen exactamente nueve líneas:

1. Seis búsquedas, en orden `(t1,m1)`, `(t1,m2)`, `(t1,m3)`, `(t2,m1)`, `(t2,m2)`, `(t2,m3)`: `true <posición>` o `false`.
2. Dos palíndromos: `inicio fin` de transmission1, luego de transmission2.
3. El substring común: `inicio fin` en transmission1.

Las posiciones empiezan en 1 y los extremos son inclusivos. Los empates se resuelven con el primer inicio en la transmisión correspondiente. Sin substring común se imprime `0 0`. Un código vacío se considera ausente.

Con `examples/`, el resultado calculado a mano es:

```text
true 6
false
false
false
false
false
1 1
1 1
1 1
```

Las transmisiones limpias son `0123456789ABCDE` y `FEDCB9876543210`. Solo la primera contiene `56789`, desde la posición 6. No hay palíndromos ni substrings comunes de más de un carácter; se elige el primer inicio.

## Pruebas

Desde la raíz:

```bash
python3 -m unittest discover -s tests -v
python3 -m unittest tests.test_lcs -v
python3 -m unittest tests.test_main -v
```

Las pruebas de LCS usan `kmp.prefix_function` real y cubren coincidencias, empates, cadenas vacías, archivos limpiados y 2000 caracteres en menos de 10 segundos.

Las pruebas end-to-end ejecutan `src/main.py` con `subprocess`, tanto sobre `examples/` como sobre `tests/fixtures/integration/`, y comparan las nueve líneas exactas. Las expectativas son constantes calculadas a mano, sin usar los algoritmos del programa para generarlas.

La segunda colección contiene `0ABACDEF` y `9ABAFDEF`, con patrones `ABA`, `DEF` y `123`. `ABA` y `DEF` empatan en longitud 3; gana `ABA`, posiciones `2 4` en la primera transmisión. La salida es:

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

## Complejidad

KMP requiere O(n + m), Manacher O(n), y el substring común con KMP sobre sufijos O(n · (n + m)) tiempo y O(n + m) espacio auxiliar. La Parte 3 no usa programación dinámica ni búsquedas con `str.find`, `in` o expresiones regulares.

## Documentación

- [ESPECIFICACION](docs/ESPECIFICACION.md): entrada, salida y asunciones.
- [ALGORITMOS](docs/ALGORITMOS.md): explicación de los tres algoritmos.
- [ARQUITECTURA](docs/ARQUITECTURA.md): módulos y contratos.
- [REPARTO](docs/REPARTO.md): responsabilidades, ramas y revisiones del equipo.
