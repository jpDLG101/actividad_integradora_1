def naive_search(text: str, pattern: str) -> tuple[int, int]:
    """Devuelve (índice de la primera aparición, comparaciones realizadas)."""
    comparisons = 0

    for start in range(len(text) - len(pattern) + 1):
        matched = True
        for offset in range(len(pattern)):
            comparisons += 1
            if text[start + offset] != pattern[offset]:
                matched = False
                break
        if matched:
            return start, comparisons

    return -1, comparisons


text = "A" * 30 + "B"
pattern = "A" * 10 + "B"
index, comparisons = naive_search(text, pattern)
print(f"Índice de inicio (0-indexed): {index}")
print(f"Comparaciones: {comparisons}")
print(f"Longitud del texto: {len(text)}")
