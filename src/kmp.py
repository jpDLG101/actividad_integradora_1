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
