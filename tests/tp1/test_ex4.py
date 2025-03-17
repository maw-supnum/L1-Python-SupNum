import io
import random
import sys
import unittest
from unittest.mock import patch


class TestEx4(unittest.TestCase):

    @patch("random.randint", return_value=42)
    @patch("builtins.input", side_effect=["20", "60", "50", "45", "42"])
    def test_jeu_devinette_plusieurs_essais(self, mock_input, mock_randint):
        """Test d'un jeu complet où l'utilisateur trouve en plusieurs essais"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open("../../tp1/ex4.py").read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("Trop bas! Essayez encore.", output)
        self.assertIn("Trop haut! Essayez encore.", output)
        self.assertIn("Bravo! Vous avez trouvé le nombre 42 en 5 essais.", output)

    @patch("random.randint", return_value=50)
    @patch("builtins.input", side_effect=["50"])
    def test_jeu_devinette_premier_essai(self, mock_input, mock_randint):
        """Test où l'utilisateur trouve dès le premier essai"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex4.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Bravo! Vous avez trouvé le nombre 50 en 1 essais.", output)
        self.assertNotIn("Trop bas!", output)
        self.assertNotIn("Trop haut!", output)

    @patch("random.randint", return_value=75)
    @patch("builtins.input", side_effect=["abc", "75"])
    def test_jeu_devinette_entree_invalide(self, mock_input, mock_randint):
        """Test où l'utilisateur entre d'abord une valeur invalide"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex4.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Veuillez entrer un nombre entier valide.", output)
        self.assertIn("Bravo! Vous avez trouvé le nombre 75 en 1 essais.", output)

    @patch("random.randint", return_value=30)
    @patch("builtins.input", side_effect=["1", "50", "25", "30"])
    def test_jeu_devinette_strategie_dichotomie(self, mock_input, mock_randint):
        """Test d'une stratégie de recherche par dichotomie"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex4.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Trop bas! Essayez encore.", output)
        self.assertIn("Trop haut! Essayez encore.", output)
        self.assertIn("Bravo! Vous avez trouvé le nombre 30 en 4 essais.", output)

        # Vérifier que le message de succès est affiché une seule fois
        success_count = output.count("Bravo!")
        self.assertEqual(
            success_count, 1, "Le message de succès devrait apparaître une seule fois"
        )


if __name__ == "__main__":
    unittest.main()
