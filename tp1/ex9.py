# Programme pour supprimer les chiffres d'une chaîne de caractères

# Demander à l'utilisateur de saisir une chaîne
chaine_originale = input("Veuillez saisir une chaîne de caractères : ")

# Initialiser une chaîne vide pour le résultat
chaine_sans_chiffres = ""

# Parcourir chaque caractère de la chaîne originale
for caractere in chaine_originale:
    # Vérifier si le caractère n'est pas un chiffre
    if not caractere.isdigit():
        # Ajouter le caractère à la nouvelle chaîne
        chaine_sans_chiffres += caractere

# Afficher le résultat
print("Chaîne originale :", chaine_originale)
print("Chaîne sans chiffres :", chaine_sans_chiffres)
