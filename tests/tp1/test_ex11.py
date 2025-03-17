import unittest
import io
import sys
from unittest.mock import patch


class TestEx11(unittest.TestCase):

    def test_prix_minimums(self):
        """Test de la création du dictionnaire avec les prix minimums"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp1/ex11.py').read())
        except SystemExit:
            pass

        # Restaurer stdout
        sys.stdout = sys.__stdout__

        # Analyser l'output
        output = captured_output.getvalue()

        # Vérifier les résultats attendus
        self.assertIn("Formation1: {'Python': 1500, 'Django': 3500, 'PHP': 1600, 'Java': 1800}", output)
        self.assertIn("Formation2: {'Python': 1200, 'Django': 3600, 'PHP': 1750, 'Java': 2000}", output)
        self.assertIn("Formation (prix minimums): {'Python': 1200, 'Django': 3500, 'PHP': 1600, 'Java': 1800}", output)

    def test_formation_modifiee(self):
        """Test avec des dictionnaires de formation modifiés"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Modifier le code pour utiliser des dictionnaires différents
        code = open('../../tp1/ex11.py').read()
        code_modifie = code.replace(
            "Formation1 = {\"Python\": 1500, \"Django\": 3500, \"PHP\": 1600, \"Java\": 1800}",
            "Formation1 = {\"Python\": 1000, \"JavaScript\": 2500, \"C++\": 1800, \"Ruby\": 2200}"
        ).replace(
            "Formation2 = {\"Python\": 1200, \"Django\": 3600, \"PHP\": 1750, \"Java\": 2000}",
            "Formation2 = {\"Python\": 1200, \"JavaScript\": 2000, \"C++\": 2000, \"Ruby\": 1900}"
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
        self.assertIn("Formation1: {'Python': 1000, 'JavaScript': 2500, 'C++': 1800, 'Ruby': 2200}", output)
        self.assertIn("Formation2: {'Python': 1200, 'JavaScript': 2000, 'C++': 2000, 'Ruby': 1900}", output)
        self.assertIn("Formation (prix minimums): {'Python': 1000, 'JavaScript': 2000, 'C++': 1800, 'Ruby': 1900}",
                      output)

    def test_formation1_toujours_mieux(self):
        """Test où Formation1 a toujours les meilleurs prix"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open('../../tp1/ex11.py').read()
        code_modifie = code.replace(
            "Formation1 = {\"Python\": 1500, \"Django\": 3500, \"PHP\": 1600, \"Java\": 1800}",
            "Formation1 = {\"Python\": 1000, \"Django\": 2000, \"PHP\": 1500, \"Java\": 1700}"
        ).replace(
            "Formation2 = {\"Python\": 1200, \"Django\": 3600, \"PHP\": 1750, \"Java\": 2000}",
            "Formation2 = {\"Python\": 1200, \"Django\": 3000, \"PHP\": 1750, \"Java\": 2000}"
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Vérifier les résultats attendus - Formation doit être identique à Formation1
        self.assertIn("Formation (prix minimums): {'Python': 1000, 'Django': 2000, 'PHP': 1500, 'Java': 1700}", output)

    def test_formation2_toujours_mieux(self):
        """Test où Formation2 a toujours les meilleurs prix"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open('../../tp1/ex11.py').read()
        code_modifie = code.replace(
            "Formation1 = {\"Python\": 1500, \"Django\": 3500, \"PHP\": 1600, \"Java\": 1800}",
            "Formation1 = {\"Python\": 1500, \"Django\": 3500, \"PHP\": 1800, \"Java\": 2200}"
        ).replace(
            "Formation2 = {\"Python\": 1200, \"Django\": 3600, \"PHP\": 1750, \"Java\": 2000}",
            "Formation2 = {\"Python\": 1200, \"Django\": 3000, \"PHP\": 1600, \"Java\": 1800}"
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Vérifier les résultats attendus - Formation doit être identique à Formation2
        self.assertIn("Formation (prix minimums): {'Python': 1200, 'Django': 3000, 'PHP': 1600, 'Java': 1800}", output)

    def test_prix_egaux(self):
        """Test où certains prix sont égaux dans les deux formations"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        code = open('../../tp1/ex11.py').read()
        code_modifie = code.replace(
            "Formation1 = {\"Python\": 1500, \"Django\": 3500, \"PHP\": 1600, \"Java\": 1800}",
            "Formation1 = {\"Python\": 1500, \"Django\": 3000, \"PHP\": 1600, \"Java\": 1800}"
        ).replace(
            "Formation2 = {\"Python\": 1200, \"Django\": 3600, \"PHP\": 1750, \"Java\": 2000}",
            "Formation2 = {\"Python\": 1200, \"Django\": 3000, \"PHP\": 1600, \"Java\": 2000}"
        )

        try:
            exec(code_modifie)
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Vérifier les résultats attendus - Formation doit prendre le prix qui est le même pour Django et PHP
        self.assertIn("Formation (prix minimums): {'Python': 1200, 'Django': 3000, 'PHP': 1600, 'Java': 1800}", output)