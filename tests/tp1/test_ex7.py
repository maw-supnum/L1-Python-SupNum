import io
import sys
import unittest
from unittest.mock import patch


class TestEx7(unittest.TestCase):

    def test_inversion_liste_standard(self):
        """Test avec la liste standard [1, 2, 3, 4, 5]"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Modification du code pour injecter des valeurs de test
        code = open("../../tp1/ex7.py").read()
        code_modifie = "liste = [1, 2, 3, 4, 5]\n" + "\n".join(code.split("\n")[1:])

        # Exécuter le code modifié
        try:
            exec(code_modifie)
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue().strip()

        # Vérifier les résultats attendus
        self.assertEqual(output, "[5, 4, 3, 2, 1]")

    def test_inversion_liste_vide(self):
        """Test avec une liste vide"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex7.py").read()
        code_modifie = "liste = []\n" + "\n".join(code.split("\n")[1:])

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        self.assertEqual(output, "[]")

    def test_inversion_liste_un_element(self):
        """Test avec une liste contenant un seul élément"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex7.py").read()
        code_modifie = "liste = [42]\n" + "\n".join(code.split("\n")[1:])

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        self.assertEqual(output, "[42]")

    def test_inversion_liste_nombres_negatifs(self):
        """Test avec une liste de nombres négatifs"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex7.py").read()
        code_modifie = "liste = [-5, -4, -3, -2, -1]\n" + "\n".join(
            code.split("\n")[1:]
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        self.assertEqual(output, "[-1, -2, -3, -4, -5]")

    def test_inversion_liste_chaines(self):
        """Test avec une liste de chaînes de caractères"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex7.py").read()
        code_modifie = "liste = ['a', 'b', 'c', 'd', 'e']\n" + "\n".join(
            code.split("\n")[1:]
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        self.assertEqual(output, "['e', 'd', 'c', 'b', 'a']")
