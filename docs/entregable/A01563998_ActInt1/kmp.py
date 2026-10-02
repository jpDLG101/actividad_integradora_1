def prefix_function(s: str) -> list[int]:
    """Calcula el largo del borde propio más largo para cada prefijo de s."""
    pi = [0] * len(s)
    k = 0  # Largo del borde que intentamos extender.

    for i in range(1, len(s)):
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]

        if s[i] == s[k]:
            k += 1

        pi[i] = k

    return pi


def kmp_search(text: str, pattern: str) -> int | None:
    """Devuelve la primera posición 1-index de pattern en text, si existe."""
    if not pattern or len(pattern) > len(text):
        return None

    pi = prefix_function(pattern)
    k = 0  # Cantidad de caracteres del patrón emparejados.

    for i in range(len(text)):
        while k > 0 and text[i] != pattern[k]:
            k = pi[k - 1]

        if text[i] == pattern[k]:
            k += 1

        if k == len(pattern):
            return i - len(pattern) + 2  # +1 para 1-index

    return None


def format_result(pos: int | None) -> str:
    """Formatea el resultado de búsqueda sin imprimirlo."""
    if pos is None:
        return "false"
    return f"true {pos}"
