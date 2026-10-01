def read_clean(path: str) -> str:
    """Lee un archivo de texto y elimina sus saltos de línea."""
    with open(path, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido.replace("\n", "").replace("\r", "")
