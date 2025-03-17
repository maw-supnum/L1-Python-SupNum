import io
import sys
import unittest
from unittest.mock import patch


class TestEx2(unittest.TestCase):

    @patch("builtins.input", side_effect=["10", "20", "15"])
    def test_nombre_dans_intervalle(self, mock_input):
        """Test avec un nombre appartenant à l'intervalle"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open("../../tp1/ex2.py").read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("Le nombre 15.0 appartient à l'intervalle [10.0, 20.0]", output)

    @patch("builtins.input", side_effect=["10", "20", "25"])
    def test_nombre_hors_intervalle(self, mock_input):
        """Test avec un nombre n'appartenant pas à l'intervalle"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex2.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn(
            "Le nombre 25.0 n'appartient pas à l'intervalle [10.0, 20.0]", output
        )

    @patch("builtins.input", side_effect=["20", "10", "15"])
    def test_intervalle_invalide(self, mock_input):
        """Test avec un intervalle invalide (borne inf > borne sup)"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex2.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Erreur :", output)

    @patch("builtins.input", side_effect=["10", "20", "10"])
    def test_nombre_egal_borne_inf(self, mock_input):
        """Test avec un nombre égal à la borne inférieure"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex2.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Le nombre 10.0 appartient à l'intervalle [10.0, 20.0]", output)

    @patch("builtins.input", side_effect=["10", "20", "20"])
    def test_nombre_egal_borne_sup(self, mock_input):
        """Test avec un nombre égal à la borne supérieure"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex2.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Le nombre 20.0 appartient à l'intervalle [10.0, 20.0]", output)

    @patch("builtins.input", side_effect=["1.5", "3.5", "2.5"])
    def test_valeurs_decimales(self, mock_input):
        """Test avec des valeurs décimales"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open("../../tp1/ex2.py").read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Le nombre 2.5 appartient à l'intervalle [1.5, 3.5]", output)
