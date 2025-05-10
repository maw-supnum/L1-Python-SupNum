from ex1 import ouvrir_fichier

def calculer_statistiques_fichier(nom_fichier):
    file = ouvrir_fichier(nom_fichier, "r")
    content = file.read()
    file.close()
    
    mots = content.split()
    lignes = content.split("\n")
    nombre_mots = len(mots)
    nombre_lignes = len(lignes)
    nombre_caracteres = len(content)

    # afficher nombre de caracteres
    print("nombre de caracteres: ", nombre_caracteres)
    # afficher nombre de lignes
    print("nombre de lignes: ", nombre_lignes)
    # afficher nombre de mots
    print("nombre de mots: ", nombre_mots)

calculer_statistiques_fichier("tata.txt")