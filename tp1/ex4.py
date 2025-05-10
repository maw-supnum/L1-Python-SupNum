import random

# Générer un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

print("J'ai choisi un nombre entre 1 et 100. Essayez de le deviner!")

# Initialiser le compteur d'essais
nb_essais = 0

# Boucle jusqu'à ce que l'utilisateur devine correctement
while True:
    try:
        # Demander à l'utilisateur de deviner
        proposition = int(input("Votre proposition : "))
        nb_essais += 1

        # Donner des indications
        if proposition < nombre_secret:
            print("Trop bas! Essayez encore.")
        elif proposition > nombre_secret:
            print("Trop haut! Essayez encore.")
        else:
            print(
                f"Bravo! Vous avez trouvé le nombre {nombre_secret} en {nb_essais} essais."
            )
            break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
