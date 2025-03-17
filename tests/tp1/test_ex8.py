import unittest
from unittest.mock import patch
import io
import sys


class TestEx8(unittest.TestCase):

    @patch('builtins.input', return_value="test")
    def test_presence_s_simple(self, mock_input):
        """Test avec une chaîne contenant une seule lettre 's'"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("La chaîne contient la lettre 's' à la position 2.", output)
        self.assertNotIn("La lettre 's' apparaît également aux positions", output)

    @patch('builtins.input', return_value="sas")
    def test_presence_s_debut(self, mock_input):
        """Test avec une chaîne commençant par 's'"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("La chaîne contient la lettre 's' à la position 0.", output)
        self.assertIn("La lettre 's' apparaît également aux positions : 2", output)

    @patch('builtins.input', return_value="assiette")
    def test_presence_s_multiple(self, mock_input):
        """Test avec une chaîne contenant plusieurs 's'"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("La chaîne contient la lettre 's' à la position 1.", output)
        self.assertIn("La lettre 's' apparaît également aux positions : 2", output)

    @patch('builtins.input', return_value="sassafras")
    def test_presence_s_multiple_disperses(self, mock_input):
        """Test avec une chaîne contenant plusieurs 's' dispersés"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("La chaîne contient la lettre 's' à la position 0.", output)
        self.assertIn("La lettre 's' apparaît également aux positions : 2, 3, 8", output)

    @patch('builtins.input', return_value="bonjour")
    def test_absence_s(self, mock_input):
        """Test avec une chaîne ne contenant pas de 's'"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("La chaîne ne contient pas la lettre 's'.", output)
        self.assertNotIn("La chaîne contient la lettre 's'", output)

    @patch('builtins.input', return_value="")
    def test_chaine_vide(self, mock_input):
        """Test avec une chaîne vide"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("La chaîne ne contient pas la lettre 's'.", output)

    @patch('builtins.input', return_value="TASSE")
    def test_s_majuscule(self, mock_input):
        """Test avec une chaîne contenant 'S' majuscule (pas 's' minuscule)"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex8.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Le programme cherche seulement 's' minuscule, pas 'S' majuscule
        self.assertIn("La chaîne ne contient pas la lettre 's'.", output)