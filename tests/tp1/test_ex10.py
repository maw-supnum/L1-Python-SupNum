import unittest
import io
import sys
from unittest.mock import patch


class TestEx10(unittest.TestCase):

    def test_separation_etudiants(self):
        """Test de la séparation des étudiants en validés et non validés"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp1/ex10.py').read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()

        # Vérifier les résultats attendus
        self.assertIn("Dictionnaire original des étudiants :", output)
        self.assertIn("{'Salem': 12, 'Ba': 15, 'Mariem': 7, 'Sidi': 9.5, 'Med': 8.5, 'Issa': 11}", output)

        self.assertIn("Étudiants validés (moyenne >= 10) :", output)
        self.assertIn("{'Salem': 12, 'Ba': 15, 'Issa': 11}", output)

        self.assertIn("Étudiants non validés (moyenne < 10) :", output)
        self.assertIn("{'Mariem': 7, 'Sidi': 9.5, 'Med': 8.5}", output)

    def test_dictionnaire_modifie(self):
        """Test avec un dictionnaire modifié"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Modifier le code pour utiliser un dictionnaire différent
        code = open('../../tp1/ex10.py').read()
        code_modifie = code.replace(
            "etudiants = {\"Salem\": 12, \"Ba\": 15, \"Mariem\": 7, \"Sidi\": 9.5, \"Med\": 8.5, \"Issa\": 11}",
            "etudiants = {\"Alice\": 18, \"Bob\": 9, \"Charlie\": 15, \"David\": 7, \"Eve\": 10}"
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
        self.assertIn("Dictionnaire original des étudiants :", output)
        self.assertIn("{'Alice': 18, 'Bob': 9, 'Charlie': 15, 'David': 7, 'Eve': 10}", output)

        self.assertIn("Étudiants validés (moyenne >= 10) :", output)
        self.assertIn("{'Alice': 18, 'Charlie': 15, 'Eve': 10}", output)

        self.assertIn("Étudiants non validés (moyenne < 10) :", output)
        self.assertIn("{'Bob': 9, 'David': 7}", output)

    def test_tous_valides(self):
        """Test avec tous les étudiants validés"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open('../../tp1/ex10.py').read()
        code_modifie = code.replace(
            "etudiants = {\"Salem\": 12, \"Ba\": 15, \"Mariem\": 7, \"Sidi\": 9.5, \"Med\": 8.5, \"Issa\": 11}",
            "etudiants = {\"Alice\": 18, \"Bob\": 12, \"Charlie\": 15, \"David\": 10}"
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Étudiants validés (moyenne >= 10) :", output)
        self.assertIn("{'Alice': 18, 'Bob': 12, 'Charlie': 15, 'David': 10}", output)

        self.assertIn("Étudiants non validés (moyenne < 10) :", output)
        self.assertIn("{}", output)  # Dictionnaire vide pour les non validés

    def test_aucun_valide(self):
        """Test avec aucun étudiant validé"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open('../../tp1/ex10.py').read()
        code_modifie = code.replace(
            "etudiants = {\"Salem\": 12, \"Ba\": 15, \"Mariem\": 7, \"Sidi\": 9.5, \"Med\": 8.5, \"Issa\": 11}",
            "etudiants = {\"Alice\": 9, \"Bob\": 8, \"Charlie\": 7, \"David\": 5}"
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Étudiants validés (moyenne >= 10) :", output)
        self.assertIn("{}", output)  # Dictionnaire vide pour les validés

        self.assertIn("Étudiants non validés (moyenne < 10) :", output)
        self.assertIn("{'Alice': 9, 'Bob': 8, 'Charlie': 7, 'David': 5}", output)

    def test_dictionnaire_vide(self):
        """Test avec un dictionnaire vide"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open('../../tp1/ex10.py').read()
        code_modifie = code.replace(
            "etudiants = {\"Salem\": 12, \"Ba\": 15, \"Mariem\": 7, \"Sidi\": 9.5, \"Med\": 8.5, \"Issa\": 11}",
            "etudiants = {}"
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Dictionnaire original des étudiants :", output)
        self.assertIn("{}", output)

        self.assertIn("Étudiants validés (moyenne >= 10) :", output)
        self.assertIn("{}", output)

        self.assertIn("Étudiants non validés (moyenne < 10) :", output)
        self.assertIn("{}", output)