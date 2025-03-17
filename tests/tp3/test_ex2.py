import io
import os
import sys
import unittest
from pathlib import Path

# Ajouter le chemin vers les modules du TP3
sys.path.append("../../tp3")


class TestEx2(unittest.TestCase):
    """Tests pour l'exercice 2: recherche de mots dans un fichier"""

    def setUp(self):
        """Préparation des tests - création des fichiers de test"""
        # Créer un dossier assets s'il n'existe pas
        self.assets_dir = Path("assets")
        self.assets_dir.mkdir(exist_ok=True)

        # Créer un fichier de test avec des occurrences de mots
        self.test_file = self.assets_dir / "test_ex2.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(
                "Python est un langage de programmation. Python est facile à apprendre.\n"
            )
            f.write(
                "Python est très populaire. On utilise Python pour différentes applications.\n"
            )
            f.write(
                "Python permet de faire du web, de l'analyse de données, de l'IA, etc."
            )

        # Fichier sans occurrence
        self.no_match_file = self.assets_dir / "no_match.txt"
        with open(self.no_match_file, "w", encoding="utf-8") as f:
            f.write("Ce fichier ne contient pas le mot recherché.\n")
            f.write("Il n'y a aucune occurrence du terme spécifique.")

    def tearDown(self):
        """Nettoyage après les tests"""
        # Supprimer les fichiers de test
        if self.test_file.exists():
            self.test_file.unlink()
        if self.no_match_file.exists():
            self.no_match_file.unlink()

    def test_recherche_mot_existant(self):
        """Test de recherche d'un mot existant dans le fichier"""
        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(f"{self.test_file}\nPython")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open("../../tp3/ex2.py").read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Le mot 'Python' a été trouvé 5 fois dans le fichier.", output)

    def test_recherche_mot_inexistant(self):
        """Test de recherche d'un mot inexistant dans le fichier"""
        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(f"{self.test_file}\nJava")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open("../../tp3/ex2.py").read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Le mot 'Java' a été trouvé 0 fois dans le fichier.", output)

    def test_recherche_insensible_a_la_casse(self):
        """Test de recherche insensible à la casse"""
        # Rediriger l'entrée standard
        sys.stdin = io.StringIO(f"{self.test_file}\npython")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open("../../tp3/ex2.py").read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Le mot 'python' a été trouvé 5 fois dans le fichier.", output)

    def test_fichier_inexistant(self):
        """Test avec un fichier inexistant"""
        # Rediriger l'entrée standard
        fichier_inexistant = self.assets_dir / "inexistant.txt"
        sys.stdin = io.StringIO(f"{fichier_inexistant}\nPython")

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script
        try:
            exec(open("../../tp3/ex2.py").read())
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn(
            f"Erreur : Le fichier '{fichier_inexistant}' n'existe pas.", output
        )


if __name__ == "__main__":
    unittest.main()
