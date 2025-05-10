liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5

# Chercher un élément dans une liste
is_in_list = False
for val in liste:
    if val == element:
        print(f"L'élément {element} est présent dans la liste.")
        is_in_list = True
        break
if not is_in_list:
    print(f"L'élément {element} n'est pas présent dans la liste.")


# Calcul du nombre d'occurrences d'un élément
compteur = 0
for val in liste:
    if val == element:
        compteur += 1
print(f"L'élément {element} apparaît {compteur} fois dans la liste.")


# Calcul de la moyenne et du minimum
if not liste:
    print("Erreur : La liste ne doit pas être vide.")

somme = 0
minimum = liste[0]

for valeur in liste:
    somme += valeur
    if valeur < minimum:
        minimum = valeur

moyenne = somme / len(liste)

print(f"La moyenne des éléments de la liste est {moyenne}.")
print(f"Le minimum de la liste est {minimum}.")

# Tri par ordre croissant sans utiliser sort()
liste_triee = liste.copy()  # Pour ne pas modifier la liste originale
n = len(liste_triee)

for i in range(n):
    # Trouver le minimum dans la partie non triée
    min_idx = i
    for j in range(i + 1, n):
        if liste_triee[j] < liste_triee[min_idx]:
            min_idx = j

    # Échanger le minimum trouvé avec le premier élément non trié
    liste_triee[i], liste_triee[min_idx] = liste_triee[min_idx], liste_triee[i]

print(f"La liste triée par ordre croissant est {liste_triee}.")


# Trouver les nombres uniques dans une liste
elements_uniques = []

for element in liste:
    if element not in elements_uniques:
        elements_uniques.append(element)

print(f"Les éléments uniques de la liste sont {elements_uniques}.")
