# Programme qui calcule la somme, le produit et la moyenne de 10 entiers

# Initialisation de la liste vide
nombres = []

# Boucle pour saisir les 10 entiers
print("Veuillez saisir 10 entiers :")
for i in range(10):
    while True:
        try:
            entier = int(input(f"Entier {i+1}/10 : "))
            nombres.append(entier)
            break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

# Calcul de la somme
somme = sum(nombres)

# Calcul du produit
produit = 1
for nombre in nombres:
    produit *= nombre

# Calcul de la moyenne
moyenne = somme / len(nombres)

# Affichage des résultats
print("\nRésultats :")
print(f"Liste des nombres    : {nombres}")
print(f"Somme des éléments   : {somme}")
print(f"Produit des éléments : {produit}")
print(f"Moyenne des éléments : {moyenne:.2f}")
