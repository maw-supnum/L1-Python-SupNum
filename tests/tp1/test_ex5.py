import io
import sys
import unittest
from unittest.mock import patch


class TestEx5(unittest.TestCase):

    @patch(
        "builtins.input",
        side_effect=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    )
    def test_calculs_entiers_positifs(self, mock_input):
        """Test avec 10 entiers positifs consécutifs"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open("../../tp1/ex5.py").read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("Liste des nombres    : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", output)
        self.assertIn("Somme des éléments   : 55", output)
        self.assertIn("Produit des éléments : 3628800", output)
        self.assertIn("Moyenne des éléments : 5.50", output)

    @patch(
        "builtins.input", side_effect=["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    )
    def test_calculs_tous_zeros(self, mock_input):
        """Test avec 10 zéros"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex5.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Liste des nombres    : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]", output)
        self.assertIn("Somme des éléments   : 0", output)
        self.assertIn("Produit des éléments : 0", output)
        self.assertIn("Moyenne des éléments : 0.00", output)

    @patch(
        "builtins.input",
        side_effect=["-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9", "-10"],
    )
    def test_calculs_entiers_negatifs(self, mock_input):
        """Test avec 10 entiers négatifs"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex5.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn(
            "Liste des nombres    : [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]", output
        )
        self.assertIn("Somme des éléments   : -55", output)
        self.assertIn("Produit des éléments : 3628800", output)
        self.assertIn("Moyenne des éléments : -5.50", output)

    @patch(
        "builtins.input",
        side_effect=["abc", "1", "xyz", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    )
    def test_calculs_avec_erreurs(self, mock_input):
        """Test avec des entrées invalides suivies d'entrées valides"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex5.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Erreur : Veuillez entrer un nombre entier valide.", output)
        self.assertIn("Liste des nombres    : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", output)
        self.assertIn("Somme des éléments   : 55", output)

    @patch(
        "builtins.input",
        side_effect=["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
    )
    def test_calculs_grands_nombres(self, mock_input):
        """Test avec des grands nombres"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex5.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn(
            "Liste des nombres    : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]", output
        )
        self.assertIn("Somme des éléments   : 550", output)
        # Le produit attendu est très grand
        produit_attendu = 10 * 20 * 30 * 40 * 50 * 60 * 70 * 80 * 90 * 100
        self.assertIn(f"Produit des éléments : {produit_attendu}", output)
        self.assertIn("Moyenne des éléments : 55.00", output)
