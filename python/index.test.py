# A partir de jest, je veux les tests unitaires
import unittest

def sommeChiffres(n):
    if isinstance(n, int) and n >= 0:
        if n < 10:
            return n
        else:
            return n % 10 + sommeChiffres(n // 10)
    else:
        raise ValueError("L'argument doit être un entier positif.")

try:
    result = sommeChiffres(12345)
    print(result) # Output : 15
except ValueError as e:
    print(e)

class TestSommeChiffres(unittest.TestCase):

    def test_sommeChiffres(self):
        self.assertEqual(sommeChiffres(12345), 15)

    def test_sommeChiffres_entier_negatif(self):
        with self.assertRaises(ValueError):
            sommeChiffres(-123)

    def test_sommeChiffres_chaine_caracteres(self):
        with self.assertRaises(ValueError):
            sommeChiffres('abc')

    def test_sommeChiffres_nombre_virgule(self):
        with self.assertRaises(ValueError):
            sommeChiffres(12.345)

if __name__ == '__main__':
    unittest.main()