import unittest
import sys
import os
from pathlib import Path
import io

# Ajouter le chemin vers les modules du TP3
sys.path.append('../../tp3')


class TestEx1(unittest.TestCase):
    """Tests pour l'exercice 1: comptage de caractères, mots et lignes"""

    def setUp(self):
        """Préparation des tests - création des fichiers de test"""
        # Créer un dossier assets s'il n'existe pas
        self.assets_dir = Path('assets')
        self.assets_dir.mkdir(exist_ok=True)

        # Créer un fichier de test
        self.test_file = self.assets_dir / 'test_ex1.txt'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("Première ligne du fichier.\nDeuxième ligne avec des mots.\nTroisième ligne pour les tests.")

        # Créer un fichier vide
        self.empty_file = self.assets_dir / 'empty.txt'
        self.empty_file.touch()

    def tearDown(self):
        """Nettoyage après les tests"""
        # Supprimer les fichiers de test
        if self.test_file.exists():
            self.test_file.unlink()
        if self.empty_file.exists():
            self.empty_file.unlink()

    def test_comptage_fichier_existant(self):
        """Test du comptage sur un fichier existant"""
        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(str(self.test_file))

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open('../../tp3/ex1.py').read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Nombre de caractères: 88", output)
        self.assertIn("Nombre de mots: 14", output)
        self.assertIn("Nombre de lignes: 3", output)

    def test_comptage_fichier_vide(self):
        """Test du comptage sur un fichier vide"""
        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(str(self.empty_file))

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open('../../tp3/ex1.py').read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Nombre de caractères: 0", output)
        self.assertIn("Nombre de mots: 0", output)
        self.assertIn("Nombre de lignes: 0", output)

    def test_fichier_inexistant(self):
        """Test avec un fichier inexistant"""
        # Rediriger l'entrée standard
        fichier_inexistant = self.assets_dir / 'inexistant.txt'
        sys.stdin = io.StringIO(str(fichier_inexistant))

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open('../../tp3/ex1.py').read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn(f"Erreur", output)
        # print the claimed reason of the error
        claimed_reason = [x for x in output.split("\n") if "Erreur" in x][0]
        # expected reason
        expected_reason = "Erreur : Le fichier 'assets/inexistant.txt' n'existe pas."
        print("\n----------------------------------------------")
        print(f"claimed reason: {claimed_reason}")
        print(f"expected reason: {expected_reason}")
        print("----------------------------------------------")


if __name__ == '__main__':
    unittest.main()