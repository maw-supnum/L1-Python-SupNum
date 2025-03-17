import unittest
import sys
import os

sys.path.append('../../tp2')  # Ajouter le chemin vers les modules du TP2

# Importer la fonction à tester
from tp2.ex2 import calcul


class TestEx2(unittest.TestCase):

    def test_calcul_standard(self):
        """Test de calcul avec une liste de nombres standard"""
        nombres = [1, 2, 3, 4, 5]
        moyenne, max_valeur, min_valeur = calcul(nombres)
        self.assertEqual(moyenne, 3.0)
        self.assertEqual(max_valeur, 5)
        self.assertEqual(min_valeur, 1)

    def test_calcul_liste_vide(self):
        """Test de calcul avec une liste vide"""
        nombres = []
        resultat = calcul(nombres)
        self.assertEqual(resultat, (None, None, None))

    def test_calcul_un_element(self):
        """Test de calcul avec une liste d'un seul élément"""
        nombres = [42]
        moyenne, max_valeur, min_valeur = calcul(nombres)
        self.assertEqual(moyenne, 42)
        self.assertEqual(max_valeur, 42)
        self.assertEqual(min_valeur, 42)

    def test_calcul_nombres_negatifs(self):
        """Test de calcul avec des nombres négatifs"""
        nombres = [-5, -4, -3, -2, -1]
        moyenne, max_valeur, min_valeur = calcul(nombres)
        self.assertEqual(moyenne, -3.0)
        self.assertEqual(max_valeur, -1)
        self.assertEqual(min_valeur, -5)

    def test_calcul_nombres_decimaux(self):
        """Test de calcul avec des nombres décimaux"""
        nombres = [1.5, 2.5, 3.5, 4.5, 5.5]
        moyenne, max_valeur, min_valeur = calcul(nombres)
        self.assertEqual(moyenne, 3.5)
        self.assertEqual(max_valeur, 5.5)
        self.assertEqual(min_valeur, 1.5)

    def test_calcul_nombres_mixtes(self):
        """Test de calcul avec des nombres mixtes (positifs, négatifs, décimaux)"""
        nombres = [-5, 0, 2.5, 10, -3.5]
        moyenne, max_valeur, min_valeur = calcul(nombres)
        self.assertEqual(moyenne, 0.8)
        self.assertEqual(max_valeur, 10)
        self.assertEqual(min_valeur, -5)