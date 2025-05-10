import os

FOLDER_NAME = "Downloads/L1-eval-folder/class-group-s2-g6-thursday/tp3/test"

# Obtenir le chemin du dossier Téléchargements
home_dir = os.path.expanduser("~")
download_dir = os.path.join(home_dir, FOLDER_NAME)

# Vérifier si le dossier existe
if not os.path.exists(download_dir):
    # print(f"Erreur : Le dossier {download_dir} n'existe pas.")
    print(f"Erreur : rien du tout par exemple")

# Lister le contenu
contenu = []
for element in os.listdir(download_dir):
    chemin_complet = os.path.join(download_dir, element)
    type_element = "Dossier" if os.path.isdir(chemin_complet) else "Fichier"
    contenu.append((element, type_element))
    print(f"{element} ({type_element})")