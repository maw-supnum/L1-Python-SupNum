# Programme pour vérifier si une chaîne contient la lettre 's' et indiquer sa position

# Demander à l'utilisateur de saisir une chaîne
ch = input("Veuillez saisir une chaîne de caractères : ")

# Rechercher la lettre 's' dans la chaîne
position = ch.find("s")

# Vérifier si 's' est présent et afficher le message approprié
if position != -1:
    print(f"La chaîne contient la lettre 's' à la position {position}.")

    # Rechercher les autres occurrences de 's'
    autres_positions = []
    for i in range(position + 1, len(ch)):
        if ch[i] == "s":
            autres_positions.append(i)

    # Afficher les autres occurrences si elles existent
    if autres_positions:
        print(
            f"La lettre 's' apparaît également aux positions : {', '.join(map(str, autres_positions))}"
        )
else:
    print("La chaîne ne contient pas la lettre 's'.")
