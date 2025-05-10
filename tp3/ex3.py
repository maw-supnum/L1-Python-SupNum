from ex1 import ouvrir_fichier

def compter_occurences_mots(nom_fichier):
    file = ouvrir_fichier(nom_fichier, "r")
    mots = file.read()
    file.close()
    mots = mots.split(" ")
    # list_mots_uniques = set(mots)
    occurences = {}
    # for mot in list_mots_uniques:
    for mot in mots:
        occurences[mot] = mots.count(mot)
    return occurences

print(compter_occurences_mots("toto.txt"))
