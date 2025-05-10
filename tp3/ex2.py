from ex1 import ouvrir_fichier

def afficher_mots_deux_caracteres(nom_fichier):
    file = ouvrir_fichier(nom_fichier, "r")
    content = file.read()
    file.close()
    words = content.replace('.', " ").replace("?", " ").split(" ")
    filtered_words = []
    for word in words:
        if len(word)==2:
            filtered_words.append(word)
    print(" ".join(filtered_words))

afficher_mots_deux_caracteres("test1.txt")