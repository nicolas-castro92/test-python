import math

def raiz_cuadrada(x):
    if x < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(x)