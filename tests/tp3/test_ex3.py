import unittest
import sys
import os
from pathlib import Path
import io
import shutil

# Ajouter le chemin vers les modules du TP3
sys.path.append('../../tp3')


class TestEx3(unittest.TestCase):
    """Tests pour l'exercice 3: remplacement de mots dans un fichier"""

    def setUp(self):
        """Préparation des tests - création des fichiers de test"""
        # Créer un dossier assets s'il n'existe pas
        self.assets_dir = Path('assets')
        self.assets_dir.mkdir(exist_ok=True)

        # Créer un fichier de test
        self.test_file = self.assets_dir / 'test_ex3.txt'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("Python est un langage de programmation. Python est facile à apprendre.\n")
            f.write("Python est très populaire. On utilise Python pour différentes applications.\n")
            f.write("Python permet de faire du web, de l'analyse de données, de l'IA, etc.")

        # Fichier pour tester un mot inexistant
        self.no_match_file = self.assets_dir / 'no_match_ex3.txt'
        with open(self.no_match_file, 'w', encoding='utf-8') as f:
            f.write("Ce fichier ne contient pas le mot cherché.\n")
            f.write("Il n'y a aucune occurrence du terme spécifique.")

    def tearDown(self):
        """Nettoyage après les tests"""
        # Supprimer les fichiers de test
        if self.test_file.exists():
            self.test_file.unlink()
        if self.no_match_file.exists():
            self.no_match_file.unlink()

    def test_remplacement_mot_existant(self):
        """Test de remplacement d'un mot existant dans le fichier"""
        # Faire une copie du fichier original pour préserver le contenu
        test_file_copy = self.assets_dir / 'test_ex3_copy.txt'
        shutil.copy(self.test_file, test_file_copy)

        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(f"{test_file_copy}\nPython\nJava")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open('../../tp3/ex3.py').read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()

        # Vérifier que le mot a bien été remplacé
        with open(test_file_copy, 'r', encoding='utf-8') as f:
            new_content = f.read()

        self.assertIn("Nombre d'occurrences de 'Python': 5", output)
        self.assertIn("Nombre d'occurrences de 'Java': 5", output)
        self.assertIn("Java est un langage de programmation", new_content)
        self.assertNotIn("Python est un langage de programmation", new_content)

        # Nettoyer
        if test_file_copy.exists():
            test_file_copy.unlink()

    def test_remplacement_mot_inexistant(self):
        """Test de remplacement d'un mot inexistant dans le fichier"""
        # Faire une copie du fichier original pour préserver le contenu
        no_match_copy = self.assets_dir / 'no_match_ex3_copy.txt'
        shutil.copy(self.no_match_file, no_match_copy)

        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(f"{no_match_copy}\nPython\nJava")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open('../../tp3/ex3.py').read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Le mot 'Python' n'existe pas dans le fichier", output)

        # Nettoyer
        if no_match_copy.exists():
            no_match_copy.unlink()

    def test_fichier_inexistant(self):
        """Test avec un fichier inexistant"""
        # Rediriger l'entrée standard
        fichier_inexistant = self.assets_dir / 'inexistant.txt'
        sys.stdin = io.StringIO(f"{fichier_inexistant}\nPython\nJava")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open('../../tp3/ex3.py').read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn(f"Erreur : Le fichier '{fichier_inexistant}' n'existe pas.", output)


if __name__ == '__main__':
    unittest.main()