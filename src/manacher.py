def _transform(s: str) -> str:
    """Intercala '#' entre los caracteres de s (y en los extremos)."""
    return "#" + "#".join(s) + "#"


def longest_palindrome(s: str) -> tuple[int, int]:
    return (1,1)
