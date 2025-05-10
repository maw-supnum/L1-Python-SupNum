# Exercice 1 - Inverser un tableau
# Méthode 1: Avec une boucle
def inverser_tableau_boucle(tableau):
    inverse = []
    for i in range(len(tableau) - 1, -1, -1):
        inverse.append(tableau[i])
    return inverse


# Méthode 2: Avec la fonction reverse()
def inverser_tableau_reverse(tableau):
    tableau_copie = tableau.copy()  # Pour ne pas modifier l'original
    tableau_copie.reverse()
    return tableau_copie
