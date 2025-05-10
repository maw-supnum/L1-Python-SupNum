from ex1 import ouvrir_fichier

def compter_occurences_mangue_banane(nom_fichier):
    file = ouvrir_fichier(nom_fichier, "r")
    content = file.read()
    file.close()
    mots = content.split()
    mots_cibles = ["mangue", "banane"]
    return sum(mots.count(mot) for mot in mots_cibles)

print(compter_occurences_mangue_banane("toto.txt"))