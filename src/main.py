import unittest
from utils import calculer_moyenne

class TestCalculerMoyenne(unittest.TestCase):
    def test_liste1(self):
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3)

    def test_liste2(self):
        self.assertAlmostEqual(calculer_moyenne([0, 0, 1]), 1/3)

    def test_liste3(self):
        self.assertIsNone(calculer_moyenne([]))

    def test_liste4(self):
        self.assertEqual(calculer_moyenne([0, 0, 0]), 0)

    def test_liste5(self):
        self.assertEqual(calculer_moyenne([1]*21), 1)

    def test_liste6(self):
        self.assertEqual(calculer_moyenne([1, -1]), 0)
        
    def test_liste6(self):
        self.assertEqual(calculer_moyenne([1, -1]), 1)

if __name__ == '__main__':
    unittest.main()
