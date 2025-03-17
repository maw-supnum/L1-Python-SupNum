import unittest
import sys
import os
from unittest.mock import patch, MagicMock
import io

sys.path.append('../../tp2')  # Ajouter le chemin vers les modules du TP2


# Nous devons mocker les fonctions isValid et pwdGenerate car elles sont importées
# depuis d'autres modules dans ex7.py

class TestEx7(unittest.TestCase):

    @patch('ex3.isValid')
    @patch('ex5.pwdGenerate')
    @patch('builtins.input')
    def test_creation_compte_valide(self, mock_input, mock_pwdGenerate, mock_isValid):
        """Test de création d'un compte avec des informations valides"""
        # Configuration des mocks
        mock_input.side_effect = ['1', 'user123', 'user@example.com']
        mock_isValid.return_value = True
        mock_pwdGenerate.return_value = 'P@ssw0rd'

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        # Nous utilisons un bloc try-except car le code de ex7.py peut tenter de se terminer avec exit()
        try:
            exec(open('../../tp2/ex7.py').read())
        except SystemExit:
            pass

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifications
        output = captured_output.getvalue()
        self.assertIn("Compte créé avec succès pour user123", output)
        self.assertIn("Login: user123, Email: user@example.com, Mot de passe: P@ssw0rd", output)

    @patch('ex3.isValid')
    @patch('ex5.pwdGenerate')
    @patch('builtins.input')
    def test_creation_multiple_comptes(self, mock_input, mock_pwdGenerate, mock_isValid):
        """Test de création de plusieurs comptes"""
        # Configuration des mocks
        mock_input.side_effect = [
            '2',  # nombre de comptes
            'user1', 'user1@example.com',  # premier compte
            'autre',  # continuer
            'user2', 'user2@example.com'  # deuxième compte
        ]
        mock_isValid.return_value = True
        mock_pwdGenerate.side_effect = ['P@ssw0rd1', 'P@ssw0rd2']

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp2/ex7.py').read())
        except SystemExit:
            pass

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifications
        output = captured_output.getvalue()
        self.assertIn("Compte créé avec succès pour user1", output)
        self.assertIn("Compte créé avec succès pour user2", output)
        self.assertIn("Login: user1, Email: user1@example.com, Mot de passe: P@ssw0rd1", output)
        self.assertIn("Login: user2, Email: user2@example.com, Mot de passe: P@ssw0rd2", output)

    @patch('ex3.isValid')
    @patch('ex5.pwdGenerate')
    @patch('builtins.input')
    def test_informations_invalides(self, mock_input, mock_pwdGenerate, mock_isValid):
        """Test avec des informations de compte invalides"""
        # Configuration des mocks
        mock_input.side_effect = [
            '3',  # nombre de comptes
            'user@invalid', 'user@example.com',  # première tentative invalide
            '1', # pour continuer
            'user123', 'user@example.com'  # deuxième tentative valide
            '-1' # pour ne pas continuer
            'user456', 'user2@example.com'  # deuxième tentative valide
        ]
        # La première tentative est invalide, la deuxième est valide
        mock_isValid.side_effect = [False, True, True]
        mock_pwdGenerate.return_value = 'P@ssw0rd'

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp2/ex7.py').read())
        except:
            # Restaurer la sortie standard
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            print(output)

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifications
        output = captured_output.getvalue()
        self.assertIn("Erreur", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = "Erreur : Login ou email invalide. Veuillez réessayer."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")
        self.assertIn("Compte créé avec succès pour user123", output)
        self.assertNotIn("Compte créé avec succès pour user456", output)

    @patch('ex3.isValid')
    @patch('ex5.pwdGenerate')
    @patch('builtins.input')
    def test_terminer_prematurement(self, mock_input, mock_pwdGenerate, mock_isValid):
        """Test de l'arrêt prématuré de la création de comptes"""
        # Configuration des mocks
        mock_input.side_effect = [
            '3',  # nombre de comptes
            'user1', 'user1@example.com',  # premier compte
            '-1',  # terminer
        ]
        mock_isValid.return_value = True
        mock_pwdGenerate.return_value = 'P@ssw0rd'

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp2/ex7.py').read())
        except SystemExit:
            pass

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifications
        output = captured_output.getvalue()
        self.assertIn("Compte créé avec succès pour user1", output)
        self.assertNotIn("Compte 2", output)  # Pas de deuxième compte
        self.assertIn("Liste des comptes créés:", output)
        self.assertIn("Login: user1, Email: user1@example.com, Mot de passe: P@ssw0rd", output)

    @patch('builtins.input')
    def test_nombre_invalide(self, mock_input):
        """Test avec un nombre de comptes invalide"""
        # Configuration des mocks
        mock_input.return_value = 'abc'  # Entrée non numérique

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le code
        try:
            exec(open('../../tp2/ex7.py').read())
        except SystemExit:
            pass

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifications
        output = captured_output.getvalue()
        self.assertIn("Erreur", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = "Erreur : Veuillez entrer un nombre entier."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")