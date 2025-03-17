import unittest
import sys
import os
import re

sys.path.append('../../tp2')  # Ajouter le chemin vers les modules du TP2

# Importer la fonction à tester
from tp2.ex5 import pwdGenerate


class TestEx5(unittest.TestCase):

    def test_pwdGenerate_longueur(self):
        """Test que le mot de passe généré a une longueur d'au moins 8 caractères"""
        for _ in range(10):  # Tester plusieurs générations
            password = pwdGenerate()
            self.assertGreaterEqual(len(password), 8)

    def test_pwdGenerate_majuscules(self):
        """Test que le mot de passe contient au moins 2 lettres majuscules"""
        for _ in range(10):  # Tester plusieurs générations
            password = pwdGenerate()
            majuscules = re.findall(r'[A-Z]', password)
            self.assertGreaterEqual(len(majuscules), 2)

    def test_pwdGenerate_chiffres(self):
        """Test que le mot de passe contient au moins 1 chiffre"""
        for _ in range(10):  # Tester plusieurs générations
            password = pwdGenerate()
            chiffres = re.findall(r'[0-9]', password)
            self.assertGreaterEqual(len(chiffres), 1)

    def test_pwdGenerate_symboles(self):
        """Test que le mot de passe contient au moins 1 symbole spécial"""
        for _ in range(10):  # Tester plusieurs générations
            password = pwdGenerate()
            symboles = re.findall(r'[^\w\s]', password)
            self.assertGreaterEqual(len(symboles), 1)

    def test_pwdGenerate_aleatoire(self):
        """Test que la fonction génère des mots de passe différents à chaque appel"""
        passwords = [pwdGenerate() for _ in range(10)]
        # Vérifier que tous les mots de passe sont différents (très peu probable d'avoir des doublons)
        self.assertEqual(len(passwords), len(set(passwords)))
