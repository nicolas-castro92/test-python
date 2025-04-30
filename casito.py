def resta(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos argumentos deben ser números (enteros o flotantes).")
    return a - b
