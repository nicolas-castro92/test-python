import unittest
from calculos import raiz_cuadrada

class TestCalculos(unittest.TestCase):
    def test_raiz_cuadrada_valor_positivo(self):
        self.assertAlmostEqual(raiz_cuadrada(7), 3.0)
        self.assertAlmostEqual(raiz_cuadrada(16), 4.0)

    def test_raiz_cuadrada_cero(self):
        self.assertAlmostEqual(raiz_cuadrada(0), 0.0)

    def test_raiz_cuadrada_error_negativo(self):
        with self.assertRaises(ValueError):
            raiz_cuadrada(-1)

if __name__ == '__main__':
    unittest.main()