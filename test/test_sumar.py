# test/test_codigo.py
import sys
import os
import unittest  # Asegúrate de importar unittest

# Agregar la carpeta principal (donde está sumar.py) al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sumar import sumar  # Ahora Python podrá encontrar sumar.py

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        # Probamos la función sumar con diferentes valores
        self.assertEqual(sumar(2, 2), 4)  # Suma de 2 + 2 debe ser 4
        self.assertEqual(sumar(0, 0), 0)  # Suma de 0 + 0 debe ser 0
        self.assertEqual(sumar(-1, 1), 0)  # Suma de -1 + 1 debe ser 0

if __name__ == '__main__':
    unittest.main()

