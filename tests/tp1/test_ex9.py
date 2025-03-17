import unittest
from unittest.mock import patch
import io
import sys


class TestEx9(unittest.TestCase):

    @patch('builtins.input', return_value="Hello123World")
    def test_suppression_chiffres_simple(self, mock_input):
        """Test avec une chaîne contenant des lettres et des chiffres"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp1/ex9.py').read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("Chaîne originale : Hello123World", output)
        self.assertIn("Chaîne sans chiffres : HelloWorld", output)

    @patch('builtins.input', return_value="12345")
    def test_suppression_tous_chiffres(self, mock_input):
        """Test avec une chaîne ne contenant que des chiffres"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex9.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Chaîne originale : 12345", output)
        self.assertIn("Chaîne sans chiffres : ", output)

    @patch('builtins.input', return_value="abcde")
    def test_sans_chiffres(self, mock_input):
        """Test avec une chaîne ne contenant pas de chiffres"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex9.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Chaîne originale : abcde", output)
        self.assertIn("Chaîne sans chiffres : abcde", output)

    @patch('builtins.input', return_value="")
    def test_chaine_vide(self, mock_input):
        """Test avec une chaîne vide"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex9.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Chaîne originale : ", output)
        self.assertIn("Chaîne sans chiffres : ", output)

    @patch('builtins.input', return_value="1a2b3c4d5e")
    def test_alternance_chiffres_lettres(self, mock_input):
        """Test avec une chaîne alternant chiffres et lettres"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex9.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Chaîne originale : 1a2b3c4d5e", output)
        self.assertIn("Chaîne sans chiffres : abcde", output)

    @patch('builtins.input', return_value="Hello 123 World!")
    def test_espaces_ponctuations(self, mock_input):
        """Test avec des espaces et de la ponctuation"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp1/ex9.py').read())
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Chaîne originale : Hello 123 World!", output)
        self.assertIn("Chaîne sans chiffres : Hello  World!", output)