"""Substring común más largo mediante KMP sobre cada sufijo de a.

Las entradas no deben contener '#', que se reserva como separador.
"""

from kmp import prefix_function


def _best_prefix_match(suffix: str, b: str) -> int:
    """Devuelve el largo del mayor prefijo de suffix que aparece en b."""
    pi = prefix_function(suffix + "#" + b)
    zone_start = len(suffix) + 1
    return max(pi[zone_start:], default=0)


def longest_common_substring(a: str, b: str) -> tuple[int, int]:
    """Devuelve inicio y fin inclusivos, desde 1, en a.

    En empate gana el inicio más temprano en a. Sin coincidencia devuelve
    (0, 0), también cuando una entrada está vacía.
    Tiempo O(n * (n + m)); espacio auxiliar O(n + m).
    """
    if not a or not b:
        return (0, 0)

    best_len = 0
    best_start = 0
    for i in range(len(a)):
        length = _best_prefix_match(a[i:], b)
        if length > best_len:
            best_len = length
            best_start = i

    if best_len == 0:
        return (0, 0)
    return (best_start + 1, best_start + best_len)
