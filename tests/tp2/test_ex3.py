import unittest
import sys
import os

sys.path.append('../../tp2')  # Ajouter le chemin vers les modules du TP2

# Importer la fonction à tester
from tp2.ex3 import isValid


class TestEx3(unittest.TestCase):

    def test_isValid_cas_valides(self):
        """Test de validité avec des cas valides"""
        self.assertTrue(isValid("user123", "user@example.com"))
        self.assertTrue(isValid("johndoe", "john.doe@domain.fr"))
        self.assertTrue(isValid("test", "a@b.com"))
        self.assertTrue(isValid("user42", "user.name@subdomain.domain.co"))

    def test_isValid_login_invalide(self):
        """Test avec un login invalide (caractères spéciaux)"""
        self.assertFalse(isValid("user@123", "user@example.com"))
        self.assertFalse(isValid("john doe", "john@example.com"))
        self.assertFalse(isValid("user_name", "user@example.com"))
        self.assertFalse(isValid("user+name", "user@example.com"))

    def test_isValid_email_sans_at(self):
        """Test avec un email sans le symbole @"""
        self.assertFalse(isValid("user123", "userexample.com"))

    def test_isValid_email_plusieurs_at(self):
        """Test avec un email contenant plusieurs symboles @"""
        self.assertFalse(isValid("user123", "user@example@domain.com"))

    def test_isValid_email_sans_partie_locale(self):
        """Test avec un email sans partie locale (avant @)"""
        self.assertFalse(isValid("user123", "@example.com"))

    def test_isValid_email_sans_point(self):
        """Test avec un email sans point dans le domaine"""
        self.assertFalse(isValid("user123", "user@examplecom"))

    def test_isValid_email_domaine_incomplet(self):
        """Test avec un email dont le domaine est incomplet (avant le point)"""
        self.assertFalse(isValid("user123", "user@.com"))

    def test_isValid_longueur_excessive(self):
        """Test avec un login et email trop longs (>256 caractères)"""
        long_string = "a" * 257
        self.assertFalse(isValid(long_string, "user@example.com"))
        self.assertFalse(isValid("user123", long_string + "@example.com"))
