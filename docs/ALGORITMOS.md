# Algoritmos

## 1. KMP (Parte 1)

**Problema:** encontrar la primera aparición de `pattern` (largo `m`) en `text` (largo `n`).

**Idea:** el método ingenuo reinicia la comparación cada vez que falla (O(n·m)). KMP precalcula, para cada posición del patrón, cuál es el **borde** más largo del prefijo hasta ahí (un borde es un trozo que es a la vez prefijo y sufijo). Al fallar, en vez de retroceder en `text`, se "salta" dentro del patrón usando ese borde.

**Tabla de prefijos** `pi[i]` = largo del borde propio más largo de `s[0..i]`.

```
pi = [0] * len(s)
k = 0
for i in 1..len(s)-1:
    while k > 0 and s[i] != s[k]: k = pi[k-1]
    if s[i] == s[k]: k += 1
    pi[i] = k
```

**Búsqueda:** recorrer `text` con un contador `k` (chars del patrón ya emparejados). Cuando `k == m`, hay match que inicia en `i - m + 1` (0-indexed).

**Complejidad:** O(n + m) tiempo, O(m) espacio.

## 2. Manacher (Parte 2)

**Problema:** palíndromo (substring que se lee igual al revés) más largo de `s`.

**Idea:** expandir desde cada centro es O(n²). Manacher reutiliza lo ya calculado: si un centro cae dentro de un palíndromo grande ya conocido, su radio inicial es el del centro **espejo** (limitado por el borde derecho).

**Pasos:**
1. Transformar `s` insertando un separador (ej. `#`) entre chars y en los extremos: `ABA` → `#A#B#A#`. Así todos los palíndromos son de largo impar.
2. Mantener `center` y `right` (borde derecho del palíndromo más a la derecha). Para cada `i`: si `i < right`, `P[i] = min(right - i, P[2*center - i])`; luego expandir mientras coincida; si `i + P[i] > right`, actualizar `center` y `right`.
3. El `i` con mayor `P[i]` da el mejor palíndromo. En `s` original: inicio = `(i - P[i]) // 2`, largo = `P[i]` (0-indexed).

**Complejidad:** O(n).

## 3. Substring común más largo con KMP (Parte 3)

**Problema:** substring más largo presente en `a` (transmission1) y `b` (transmission2).

**Idea:** para cada sufijo `a[i:]`, la tabla de prefijos de `a[i:] + '#' + b` dice, en la zona de `b`, cuánto del **prefijo** de `a[i:]` aparece terminando en cada posición de `b`. El máximo en esa zona es el match más largo que **empieza** en `a[i]`. Se toma el mejor sobre todos los `i`.

```
best_len = 0, best_start = 0
for i in 0..len(a)-1:
    pi = prefix_function(a[i:] + '#' + b)
    L = max(pi[len(a)-i+1:])          # solo la parte de b
    if L > best_len: best_len, best_start = L, i   # '>' estricto => primera aparición
resultado (1-indexed): best_start + 1, best_start + best_len
```

`#` no está en el alfabeto, así que ningún borde puede cruzarlo.

**Complejidad:** O(n · (n + m)). Aceptable para el tamaño de las pruebas de la actividad.

## Notas de posiciones
Internamente todo es 0-indexed; la conversión a 1-indexed se hace **solo** al devolver/imprimir (`+1`).
