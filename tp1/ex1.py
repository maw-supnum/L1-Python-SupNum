# Programme qui calcule le maximum, minimum et la moyenne de trois nombres

# Saisie des trois nombres
a = float(input("Entrez le premier nombre (a): "))
b = float(input("Entrez le deuxième nombre (b): "))
c = float(input("Entrez le troisième nombre (c): "))

# Calcul du maximum, minimum et moyenne
maximum = max(a, b, c)
minimum = min(a, b, c)
moyenne = (a + b + c) / 3

# Affichage des résultats
print(f"Le maximum des trois nombres est: {maximum}")
print(f"Le minimum des trois nombres est: {minimum}")
print(f"La moyenne des trois nombres est: {moyenne:.2f}")
