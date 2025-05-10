# Programme pour générer les n premiers termes de la suite de Fibonacci

# Demander à l'utilisateur d'entrer le nombre de termes
n = int(input("Entrez le nombre de termes n de la suite de Fibonacci à afficher : "))

# Vérifier que n est positif
if n <= 0:
    print("Erreur : Veuillez entrer un entier positif.")
else:
    # Initialisation des deux premiers termes
    fibonacci = [0, 1]

    # Générer les termes suivants si n > 2
    if n > 2:
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    elif n == 1:
        fibonacci = [0]  # Si n=1, on n'affiche que le premier terme

    # Afficher les n premiers termes
    print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
    for i in range(n):
        print(f"F({i}) = {fibonacci[i]}")
