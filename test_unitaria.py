
import unittest

def preprocess(data):
    # Implementación de la función preprocess
    return data.strip().lower()

class TestPreprocess(unittest.TestCase):
    def test_preprocess(self):
        # Verifica que la función preprocess elimine los espacios en blanco y convierta a minúsculas
        self.assertEqual(preprocess("hay alguien aqui"), "hay alguien aqui")

    def test_preprocess_empty_string(self):
        # Verifica que la función preprocess devuelva una cadena vacía si se le pasa una cadena vacía
        self.assertEqual(preprocess(""), "")

if __name__ == '__main__':
    unittest.main() 
    
    