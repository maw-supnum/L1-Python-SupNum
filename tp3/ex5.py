from ex1 import ouvrir_fichier

def creer_fichier_avec_mots(fichier_source, fichier_destination):
    file = ouvrir_fichier(fichier_source, "r")
    mots = file.read().split(" ")
    file.close()
    contenu_destination = "\n".join(mots)
    file = ouvrir_fichier(fichier_destination, "w")
    file.write(contenu_destination)
    file.close()
    print(contenu_destination)

creer_fichier_avec_mots("toto.txt", "tata.txt")