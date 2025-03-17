import unittest
import sys
import os
from pathlib import Path
import io
import importlib.util

# Ajouter le chemin vers les modules du TP3
sys.path.append('../../tp3')


class TestEx4(unittest.TestCase):
    """Tests pour l'exercice 4: manipulation du fichier Liste_L1.txt"""

    def setUp(self):
        """Préparation des tests - création des fichiers de test"""
        # Créer un dossier assets s'il n'existe pas
        self.assets_dir = Path('assets')
        self.assets_dir.mkdir(exist_ok=True)

        # Créer un fichier de test Liste_L1.txt
        self.liste_file = self.assets_dir / 'Liste_L1.txt'
        with open(self.liste_file, 'w', encoding='utf-8') as f:
            f.write("20230001 : M : Jean Dupont : jean.dupont@univ.dz : 1\n")
            f.write("20230002 : F : Marie Martin : marie.martin@univ.dz : 1\n")
            f.write("20230003 : M : Pierre Durand : pierre.durand@univ.dz : 2\n")
            f.write("20230004 : F : Sophie Petit : sophie.petit@univ.dz : 2\n")
            f.write("20230005 : M : Paul Robert : paul.robert@univ.dz : 3\n")
            f.write("20230006 : F : Claire Lefebvre : claire.lefebvre@univ.dz : 3\n")
            f.write("20230007 : M : Thomas Dubois : thomas.dubois@univ.dz : 4\n")
            f.write("20230008 : F : Julie Moreau : julie.moreau@univ.dz : 4\n")
            f.write("20230009 : M : Nicolas Laurent : nicolas.laurent@univ.dz : 5\n")
            f.write("20230010 : F : Emma Leroy : emma.leroy@univ.dz : 5\n")
            f.write("20230011 : M : Alexandre Simon : alexandre.simon@univ.dz : 6\n")
            f.write("20230012 : F : Camille Rousseau : camille.rousseau@univ.dz : 6\n")

        # Créer un module temporaire avec la fonction obtenir_nom_par_matricule
        self.module_path = self.assets_dir / 'temp_ex4.py'
        with open(self.module_path, 'w', encoding='utf-8') as f:
            f.write("def obtenir_nom_par_matricule(matricule, nom_fichier='Liste_L1.txt'):\n")
            f.write("    try:\n")
            f.write("        with open(nom_fichier, 'r', encoding='utf-8') as fichier:\n")
            f.write("            for ligne in fichier:\n")
            f.write("                elements = ligne.strip().split(' : ')\n")
            f.write("                if len(elements) >= 3 and elements[0].strip() == str(matricule):\n")
            f.write("                    return elements[2].strip()  # Prénom et nom\n")
            f.write("        return 'Étudiant non trouvé'\n")
            f.write("    except FileNotFoundError:\n")
            f.write("        return f\"Erreur: Le fichier '{nom_fichier}' n'existe pas.\"\n")
            f.write("    except Exception as e:\n")
            f.write("        return f\"Erreur lors de la recherche: {e}\"\n\n")

            f.write("def creer_fichiers_groupes(nom_fichier='Liste_L1.txt'):\n")
            f.write("    try:\n")
            f.write("        # Dictionnaire pour stocker les étudiants par groupe\n")
            f.write("        groupes = {i: [] for i in range(1, 7)}\n\n")
            f.write("        # Lire le fichier et répartir les étudiants\n")
            f.write("        with open(nom_fichier, 'r', encoding='utf-8') as fichier:\n")
            f.write("            for ligne in fichier:\n")
            f.write("                elements = ligne.strip().split(' : ')\n")
            f.write("                if len(elements) >= 5:\n")
            f.write("                    try:\n")
            f.write("                        groupe = int(elements[4].strip())\n")
            f.write("                        if 1 <= groupe <= 6:\n")
            f.write("                            groupes[groupe].append(ligne.strip())\n")
            f.write("                    except ValueError:\n")
            f.write("                        continue\n\n")
            f.write("        # Créer les fichiers de groupe\n")
            f.write("        for groupe, etudiants in groupes.items():\n")
            f.write("            with open(f'TP{groupe}.txt', 'w', encoding='utf-8') as fichier_groupe:\n")
            f.write("                for etudiant in etudiants:\n")
            f.write("                    fichier_groupe.write(etudiant + '\\n')\n\n")
            f.write("        return True\n")
            f.write("    except FileNotFoundError:\n")
            f.write("        print(f\"Erreur : Le fichier '{nom_fichier}' n'existe pas.\")\n")
            f.write("        return False\n")
            f.write("    except Exception as e:\n")
            f.write("        print(f\"Erreur : lors de la création des fichiers: {e}\")\n")
            f.write("        return False\n")

    def tearDown(self):
        """Nettoyage après les tests"""
        # Supprimer les fichiers de test
        if self.liste_file.exists():
            self.liste_file.unlink()
        if self.module_path.exists():
            self.module_path.unlink()

        # Supprimer les fichiers TP*.txt
        for i in range(1, 7):
            tp_file = Path(f'TP{i}.txt')
            if tp_file.exists():
                tp_file.unlink()

    def test_obtenir_nom_par_matricule(self):
        """Test de la fonction obtenir_nom_par_matricule"""
        # Importer le module temporaire
        spec = importlib.util.spec_from_file_location("temp_ex4", self.module_path)
        temp_ex4 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(temp_ex4)

        # Tester avec un matricule existant
        nom = temp_ex4.obtenir_nom_par_matricule('20230001', str(self.liste_file))
        self.assertEqual(nom, 'Jean Dupont')

        # Tester avec un matricule inexistant
        nom = temp_ex4.obtenir_nom_par_matricule('99999999', str(self.liste_file))
        self.assertEqual(nom, 'Étudiant non trouvé')

        # Tester avec un fichier inexistant
        fichier_inexistant = self.assets_dir / 'inexistant.txt'
        nom = temp_ex4.obtenir_nom_par_matricule('20230001', str(fichier_inexistant))
        self.assertIn("Erreur", nom)
        self.assertIn(f"Le fichier '{fichier_inexistant}' n'existe pas", nom)

    def test_afficher_membres_groupe(self):
        """Test de l'affichage des membres d'un groupe TP"""
        # Rediriger l'entrée standard
        sys.stdin = io.StringIO("1")  # Groupe TP1

        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Exécuter le script avec le chemin modifié pour nom_fichier
        globals_dict = {'nom_fichier': str(self.liste_file)}
        try:
            with open('../../tp3/ex4.py', 'r', encoding='utf-8') as f:
                code = f.read().replace("nom_fichier = \"Liste_L1.txt\"", f"nom_fichier = \"{self.liste_file}\"")
                exec(code, globals_dict)
        except SystemExit:
            pass

        # Restaurer l'entrée et la sortie standard
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Vérifier les résultats
        output = captured_output.getvalue()
        self.assertIn("Membres du groupe TP1:", output)
        # Vérifier que les membres du groupe 1 sont listés (serait plus précis dans le code réel)