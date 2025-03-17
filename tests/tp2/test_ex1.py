import os
import sys
import unittest

sys.path.append("../../tp2")  # Ajouter le chemin vers les modules du TP2

# Importer les fonctions à tester
from tp2.ex1 import inverser_tableau_boucle, inverser_tableau_reverse


class TestEx1(unittest.TestCase):

    def test_inverser_tableau_boucle_standard(self):
        """Test d'inversion d'un tableau standard avec la méthode boucle"""
        tableau = [1, 2, 3, 4, 5]
        resultat = inverser_tableau_boucle(tableau)
        self.assertEqual(resultat, [5, 4, 3, 2, 1])
        # Vérifier que l'original n'a pas été modifié
        self.assertEqual(tableau, [1, 2, 3, 4, 5])

    def test_inverser_tableau_reverse_standard(self):
        """Test d'inversion d'un tableau standard avec la méthode reverse"""
        tableau = [1, 2, 3, 4, 5]
        resultat = inverser_tableau_reverse(tableau)
        self.assertEqual(resultat, [5, 4, 3, 2, 1])
        # Vérifier que l'original n'a pas été modifié
        self.assertEqual(tableau, [1, 2, 3, 4, 5])

    def test_inverser_tableau_boucle_vide(self):
        """Test d'inversion d'un tableau vide avec la méthode boucle"""
        tableau = []
        resultat = inverser_tableau_boucle(tableau)
        self.assertEqual(resultat, [])

    def test_inverser_tableau_reverse_vide(self):
        """Test d'inversion d'un tableau vide avec la méthode reverse"""
        tableau = []
        resultat = inverser_tableau_reverse(tableau)
        self.assertEqual(resultat, [])

    def test_inverser_tableau_boucle_un_element(self):
        """Test d'inversion d'un tableau avec un seul élément avec la méthode boucle"""
        tableau = [42]
        resultat = inverser_tableau_boucle(tableau)
        self.assertEqual(resultat, [42])

    def test_inverser_tableau_reverse_un_element(self):
        """Test d'inversion d'un tableau avec un seul élément avec la méthode reverse"""
        tableau = [42]
        resultat = inverser_tableau_reverse(tableau)
        self.assertEqual(resultat, [42])

    def test_inverser_tableau_boucle_strings(self):
        """Test d'inversion d'un tableau de chaînes avec la méthode boucle"""
        tableau = ["a", "b", "c", "d", "e"]
        resultat = inverser_tableau_boucle(tableau)
        self.assertEqual(resultat, ["e", "d", "c", "b", "a"])

    def test_inverser_tableau_reverse_strings(self):
        """Test d'inversion d'un tableau de chaînes avec la méthode reverse"""
        tableau = ["a", "b", "c", "d", "e"]
        resultat = inverser_tableau_reverse(tableau)
        self.assertEqual(resultat, ["e", "d", "c", "b", "a"])


if __name__ == "__main__":
    unittest.main()
