import io
import sys
import unittest
from unittest.mock import patch


class TestEx3(unittest.TestCase):

    @patch("builtins.input", side_effect=["5"])
    def test_fibonacci_cinq_termes(self, mock_input):
        """Test avec 5 termes de la suite de Fibonacci"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open("../../tp1/ex3.py").read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("Les 5 premiers termes de la suite de Fibonacci sont :", output)
        terms = output.split("Les 5 premiers termes de la suite de Fibonacci sont :")[1]
        self.assertIn("0", terms)
        self.assertIn("1", terms)
        self.assertIn("2", terms)
        self.assertIn("3", terms)

    @patch("builtins.input", side_effect=["1"])
    def test_fibonacci_un_terme(self, mock_input):
        """Test avec 1 terme de la suite de Fibonacci"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex3.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Les 1 premiers termes de la suite de Fibonacci sont :", output)
        terms = output.split("Les 1 premiers termes de la suite de Fibonacci sont :")[1]
        self.assertIn("0", terms)
        self.assertNotIn("1", terms)

    @patch("builtins.input", side_effect=["0"])
    def test_entree_zero(self, mock_input):
        """Test avec une entrée égale à zéro"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex3.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Erreur :", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = "Erreur : Veuillez entrer un entier positif."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")

    @patch("builtins.input", side_effect=["-3"])
    def test_entree_negative(self, mock_input):
        """Test avec une entrée négative"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex3.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Erreur :", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = "Erreur : Veuillez entrer un entier positif."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")

    @patch("builtins.input", side_effect=["8"])
    def test_fibonacci_dix_termes(self, mock_input):
        """Test avec 10 termes de la suite de Fibonacci"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex3.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Les 8 premiers termes de la suite de Fibonacci sont :", output)
        terms = output.split("Les 8 premiers termes de la suite de Fibonacci sont :")[1]
        self.assertIn("0", terms)
        self.assertIn("1", terms)
        self.assertIn("2", terms)
        self.assertIn("3", terms)
        self.assertIn("5", terms)
        self.assertIn("8", terms)
        self.assertIn("13", terms)
        self.assertNotIn("21", terms)
