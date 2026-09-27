# Especificación

## Entrada
No hay entrada del usuario. El programa lee 5 archivos de nombre fijo, ubicados en el directorio donde se ejecuta:

- `transmission1.txt`, `transmission2.txt`: datos enviados de un dispositivo a otro.
- `mcode1.txt`, `mcode2.txt`, `mcode3.txt`: código malicioso que puede aparecer dentro de una transmisión.

Alfabeto: `0-9`, `A-F` (mayúsculas) y saltos de línea.

## Salida (en este orden, una línea cada una)

### Parte 1 — 6 líneas
Orden: (t1,m1), (t1,m2), (t1,m3), (t2,m1), (t2,m2), (t2,m3).

- Si `mcodeY` está contenido en `transmissionX`: `true <pos>` (un solo espacio), donde `pos` es la posición 1-indexed donde inicia la **primera** aparición.
- Si no: `false`.

### Parte 2 — 2 líneas
`inicio fin` (1-indexed, inclusivos) del palíndromo más largo de transmission1, luego el de transmission2. Se asume que siempre existe.

### Parte 3 — 1 línea
`inicio fin` (1-indexed, inclusivos) del substring común más largo, **en transmission1**.

## Asunciones (confirmar con el profesor)
1. Cada archivo se lee como **una sola cadena** eliminando `\n` y `\r`; las posiciones se cuentan sobre esa cadena limpia.
2. Si hay varios palíndromos con la longitud máxima, se reporta el que inicia primero.
3. Si hay varios substrings comunes con la longitud máxima, se reporta el que inicia primero en transmission1.
4. Un `mcode` vacío (archivo vacío) se considera no contenido (`false`).
5. Si el palíndromo más largo tiene longitud 1 (no hay ninguno "real"), se reporta `1 1` por el primer caracter, aunque se asume que no ocurre.

## Restricciones
- Solo se usan **KMP** y **Manacher**. Nada de `str.find`, `in`, `re`, ni programación dinámica para resolver las partes.
- Sin librerías externas.
