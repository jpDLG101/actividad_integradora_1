## Ejemplo incluido (`transmission1.txt`, `transmission2.txt`, `mcode1.txt`, `mcode2.txt`, `mcode3.txt`)

### Archivos de entrada

Archivo: `transmission1.txt`

Entrada:
```
01234
56789
ABCDE
```
Limpio (sin saltos de línea): `0123456789ABCDE`, 15 caracteres.

Archivo: `transmission2.txt`

Entrada:
```
FEDCB
98765
43210
```
Limpio: `FEDCB9876543210`, 15 caracteres.

Archivo: `mcode1.txt`
```
56789
```
Archivo: `mcode2.txt`
```
FFFFF
```
Archivo: `mcode3.txt`
```
A1B2C
```

### Resultado esperado

```
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

### Por qué esa salida

**Parte 1 (líneas 1-6, orden t1×m1, t1×m2, t1×m3, t2×m1, t2×m2, t2×m3):** `mcode1` (`56789`) sí aparece dentro de `transmission1`, justo en las posiciones 6 a 10 (`...4[56789]ABCDE`), por eso `true 6`. `mcode2` (`FFFFF`) no aparece en ninguna transmisión: `transmission1` no tiene ninguna `F`, y `transmission2` solo tiene una. `mcode3` (`A1B2C`) tampoco aparece: ninguna de las dos transmisiones intercala letras y dígitos en ese orden. `mcode1` no aparece en `transmission2` porque ahí los dígitos van en orden descendente (`...98765...`), nunca como `56789`.

**Parte 2 (líneas 7-8, palíndromo más largo de cada transmisión):** ambas transmisiones son secuencias estrictamente crecientes (`transmission1`) o decrecientes (`transmission2`) de caracteres distintos, así que ningún par de caracteres vecinos se repite ni se refleja. El palíndromo más largo posible es un solo carácter, y como hay empate entre los 15 caracteres de cada una, se reporta el primero: posición `1 1` en ambas.

**Parte 3 (línea 9, substring común más largo entre las dos transmisiones):** `transmission1` siempre avanza hacia adelante (`01`, `12`, `9A`, `AB`, ...) y `transmission2` siempre avanza hacia atrás (`FE`, `DC`, `98`, ...), así que nunca coinciden dos caracteres consecutivos en el mismo orden entre ambas. Lo más largo que comparten es un solo carácter, y el primero que aparece así en `transmission1` es el `0` de la posición 1, que también existe en `transmission2` (al final). Por eso `1 1`.
