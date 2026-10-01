def _transform(s: str) -> str:
    """Intercala '#' entre los caracteres de s (y en los extremos)."""
    return "#" + "#".join(s) + "#"


def longest_palindrome(s: str) -> tuple[int, int]:
    t = _transform(s)
    P = [0] * len(t)
    center = right = 0

    for i in range(len(t)):
        if i < right:
            P[i] = min(right - i, P[2 * center - i])

        while i - P[i] - 1 >= 0 and i + P[i] + 1 < len(t) and t[i - P[i] - 1] == t[i + P[i] + 1]:
            P[i] += 1

        if i + P[i] > right:
            center = i
            right = i + P[i]
