import io
import sys
import unittest
from unittest.mock import patch


class TestEx6(unittest.TestCase):

    def test_liste_standard(self):
        """Test avec la liste standard [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] et l'élément 5"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Modification du code pour injecter des valeurs de test
        code = open("../../tp1/ex6.py").read()
        code_modifie = (
            "liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nelement = 5\n"
            + "\n".join(code.split("\n")[2:])
        )

        # Exécuter le code modifié
        try:
            exec(code_modifie)
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()

        # Vérifier les résultats attendus
        self.assertIn("L'élément 5 est présent dans la liste.", output)
        self.assertIn("L'élément 5 apparaît 1 fois dans la liste.", output)
        self.assertIn("La moyenne des éléments de la liste est 5.5.", output)
        self.assertIn("Le minimum de la liste est 1.", output)
        self.assertIn(
            "La liste triée par ordre croissant est [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].",
            output,
        )
        self.assertIn(
            "Les éléments uniques de la liste sont [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].",
            output,
        )

    def test_liste_avec_doublons(self):
        """Test avec une liste contenant des doublons"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex6.py").read()
        code_modifie = (
            "liste = [5, 2, 5, 4, 5, 6, 7, 8, 5, 10]\nelement = 5\n"
            + "\n".join(code.split("\n")[2:])
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("L'élément 5 est présent dans la liste.", output)
        self.assertIn("L'élément 5 apparaît 4 fois dans la liste.", output)
        self.assertIn(
            "La moyenne des éléments de la liste est 5.7", output
        )  # Arrondi possible
        self.assertIn("Le minimum de la liste est 2.", output)
        self.assertIn(
            "La liste triée par ordre croissant est [2, 4, 5, 5, 5, 5, 6, 7, 8, 10].",
            output,
        )
        self.assertIn(
            "Les éléments uniques de la liste sont [5, 2, 4, 6, 7, 8, 10].", output
        )

    def test_element_absent(self):
        """Test avec un élément qui n'est pas dans la liste"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex6.py").read()
        code_modifie = (
            "liste = [1, 2, 3, 4, 6, 7, 8, 9, 10]\nelement = 5\n"
            + "\n".join(code.split("\n")[2:])
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("L'élément 5 n'est pas présent dans la liste.", output)
        self.assertIn("L'élément 5 apparaît 0 fois dans la liste.", output)

    def test_liste_negative(self):
        """Test avec une liste de nombres négatifs"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex6.py").read()
        code_modifie = "liste = [-5, -4, -3, -2, -1]\nelement = -3\n" + "\n".join(
            code.split("\n")[2:]
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("L'élément -3 est présent dans la liste.", output)
        self.assertIn("L'élément -3 apparaît 1 fois dans la liste.", output)
        self.assertIn("La moyenne des éléments de la liste est -3.0.", output)
        self.assertIn("Le minimum de la liste est -5.", output)
        self.assertIn(
            "La liste triée par ordre croissant est [-5, -4, -3, -2, -1].", output
        )

    def test_liste_vide(self):
        """Test avec une liste vide"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex6.py").read()
        code_modifie = "liste = []\nelement = 5\n" + "\n".join(code.split("\n")[2:])

        try:
            exec(code_modifie)
        except Exception as e:
            error = str(e)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("L'élément 5 n'est pas présent dans la liste.", output)
        self.assertIn("L'élément 5 apparaît 0 fois dans la liste.", output)
        # On s'attend à une erreur pour le calcul de la moyenne d'une liste vide

    # tester le cas où la liste est vide et l'on cherche le minimum ou la moyenne
    def test_moyenne_min_liste_vide(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open("../../tp1/ex6.py").read()
        code_modifie = "liste = []\nelement = 5\n" + "\n".join(code.split("\n")[2:])

        try:
            exec(code_modifie)
        except Exception as e:
            error = str(e)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Erreur", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = "Erreur : Veuillez saisir une liste non vide."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")
