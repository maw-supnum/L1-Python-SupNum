import unittest
import sys
import os
from unittest.mock import patch, MagicMock
import io

sys.path.append('../../tp2')  # Ajouter le chemin vers les modules du TP2

from tp2 import ex6

class TestEx6(unittest.TestCase):

    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['fichier1.txt', 'dossier1'])
    @patch('os.path.isdir', side_effect=[False, True])
    def test_chemin_download_windows(self, mock_isdir, mock_listdir, mock_exists):
        """Test que le chemin du dossier Downloads est correctement défini sous Windows"""

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp2/ex6.py').read())
        except SystemExit:
            pass

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifier l'affichage des éléments
        output = captured_output.getvalue()
        self.assertIn('fichier1.txt (Fichier)', output)
        self.assertIn('dossier1 (Dossier)', output)
        

    @patch('os.path.exists')
    def test_dossier_inexistant(self, mock_exists):
        """Test du comportement quand le dossier Downloads n'existe pas"""
        # Configuration des mocks
        mock_exists.return_value = False

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Importer le module
        from tp2 import ex6
        importlib = __import__('importlib')
        importlib.reload(ex6)

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifier le message d'erreur
        output = captured_output.getvalue()
        self.assertIn("Erreur", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = f"Erreur : Le dossier n'existe pas."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")

if __name__ == '__main__':
    unittest.main()