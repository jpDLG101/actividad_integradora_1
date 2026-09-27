# Arquitectura

```
.
├── README.md
├── docs/
├── src/
│   ├── main.py         # orquesta y imprime; sin lógica de algoritmos
│   ├── io_utils.py     # lectura de archivos
│   ├── kmp.py          # prefix_function, kmp_search
│   ├── manacher.py     # longest_palindrome
│   └── lcs.py          # longest_common_substring (usa kmp.prefix_function)
└── tests/
    ├── test_kmp.py
    ├── test_manacher.py
    ├── test_lcs.py
    └── test_main.py    # end-to-end con archivos de ejemplo
```

## Contratos (firmas acordadas)

| Módulo | Función | Contrato |
|---|---|---|
| `io_utils` | `read_clean(path: str) -> str` | Lee el archivo y quita `\n` y `\r`. |
| `kmp` | `prefix_function(s: str) -> list[int]` | Tabla de bordes. |
| `kmp` | `kmp_search(text: str, pattern: str) -> int \| None` | Posición **1-indexed** de la primera aparición, o `None`. |
| `manacher` | `longest_palindrome(s: str) -> tuple[int, int]` | `(inicio, fin)` 1-indexed, inclusivos. |
| `lcs` | `longest_common_substring(a: str, b: str) -> tuple[int, int]` | `(inicio, fin)` 1-indexed en `a`. |

`main.py` importa de los demás módulos e imprime en el orden de `ESPECIFICACION.md`. Si algo cambia en una firma, se actualiza este archivo en el mismo PR.

## Reglas
- Los módulos de algoritmos no leen archivos ni imprimen.
- Solo `main.py` imprime.
- Sin dependencias externas (solo biblioteca estándar; tests con `unittest`).
