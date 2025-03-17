# Consignes pour le TP1

## Exercice 1

definir les trois variables au début du programme (en utilisant la fonction `input`):

```python
a = ...
b = ...
c = ...
```

afficher les résultats en suivant le format suivant:

```python
print(f"Le maximum des trois nombres est: {maximum}")
print(f"Le minimum des trois nombres est: {minimum}")
print(f"La moyenne des trois nombres est: {moyenne:.2f}")
```

## Exercice 2

definir les trois variables au début du programme (en utilisant la fonction `input`):

```python
# Saisie des bornes de l'intervalle
borne_inf = ...
borne_sup = ...

# Saisie du nombre à vérifier
nombre = ...
```

afficher les résultats en suivant le format suivant:

si le nombre est dans l'intervalle:

```python
print(f"Le nombre {nombre} appartient à l'intervalle [{borne_inf}, {borne_sup}]")
```

si le nombre n'est pas dans l'intervalle:

```python
print(f"Le nombre {nombre} n'appartient pas à l'intervalle [{borne_inf}, {borne_sup}]")
```

si le cas n'est pas verifiable:

```python
# definir la raison de l'erreur
raison = ...
print(f"Erreur : {raison}")
```

## Exercice 3

definir la variable `n` au debut du programme (en utilisant la fonction `input`):

```python
# Demander à l'utilisateur d'entrer le nombre de termes
n = ...
```

afficher les résultats en suivant le format suivant:

```python
print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
```

suivi des `n` premiers termes de la suite de Fibonacci séparés par une virgule, espace ou un retour à la ligne.

s'il s'agit d'une erreur, afficher le message suivant:

```python
raison = ...
print(f"Erreur : {raison}")
```

## Exercice 4

respecter les formats suivants:

```python
# Générer un nombre aléatoire entre 1 et 100
nombre_secret = ...
```

```python
# Demander à l'utilisateur de deviner
proposition = ...
```

```python
print("Trop bas! Essayez encore.")
```

```python
print("Trop haut! Essayez encore.")
```

```python
print(f"Bravo! Vous avez trouvé le nombre {nombre_secret} en {nb_essais} essais.")
```

## Exercice 5

Pour l'affichage des resultats, respecter le format suivant:

```python
# Affichage des résultats
print("\nRésultats :")
print(f"Liste des nombres    : {nombres}")
print(f"Somme des éléments   : {somme}")
print(f"Produit des éléments : {produit}")
print(f"Moyenne des éléments : {moyenne:.2f}")
```

En cas d'erreur, afficher le message suivant:

```python
raison = ...
print(f"Erreur : {raison}")
```

## Exercice 6

definir les deux variables au début du programme (n'utilisez pas la fonction `input`):

```python
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5
```

afficher les résultats en suivant le format suivant:

1. recherche de l'élément dans la liste:

```python
print(f"L'élément {element} est présent dans la liste.")
```

```python
print(f"L'élément {element} n'est pas présent dans la liste.")
```

2. occurence de l'élément dans la liste:

```python
print(f"L'élément {element} apparaît {compteur} fois dans la liste.")
```

3. Calcul de la moyenne et du minimum

```python
# cas ingerable
raison = ...
print(f"Erreur : {raison}")
```

```python
print(f"La moyenne des éléments de la liste est {moyenne}.")
print(f"Le minimum de la liste est {minimum}.")
```

4. Tri par ordre croissant sans utiliser `sort`:

```python
print(f"La liste triée par ordre croissant est {liste_triee}.")
```

5. Trouver les nombres uniques dans une liste

```python
print(f"Les éléments uniques de la liste sont {elements_uniques}.")
```

## Exercice 7

definir la variable principale au début du programme (n'utilisez pas la fonction `input`):

```python
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

afficher les résultats en suivant le format suivant:

```python
print(liste_inverse)
```

## Exercice 8

definir la chaine de caractere (utilisez la fonction `input`):

```python
# Demander à l'utilisateur de saisir une chaîne
ch = ...
```

respecter les formats suivants pour l'affichage des résultats:

```python
print(f"La chaîne contient la lettre 's' à la position {position}.")
```

```python
print(f"La lettre 's' apparaît également aux positions : {', '.join(map(str, autres_positions))}")
```

```python
print("La chaîne ne contient pas la lettre 's'.")
```

## Exercice 9

Demander à l'utilisateur de saisir une chaîne de caractères a remplacer (utilisez la fonction `input`):

```python
# Demander à l'utilisateur de saisir une chaîne
chaine_originale = ...
```

respecter les formats suivants pour l'affichage des résultats:

```python
print("Chaîne originale :", chaine_originale)
print("Chaîne sans chiffres :", chaine_sans_chiffres)
```

## Exercice 10

respecter les formats suivants pour l'affichage des résultats:

```python
# Affichage des résultats
print("Dictionnaire original des étudiants :")
print(etudiants) # afficher le dictionnaire original
print("\nÉtudiants validés (moyenne >= 10) :")
print(V) # afficher les étudiants validés
print("\nÉtudiants non validés (moyenne < 10) :")
print(NV) # afficher les étudiants non validés
```

## Exercice 11

respecter les formats suivants pour l'affichage des résultats:

```python
# Affichage des résultats
print("Formation1:", Formation1) # afficher la formation1
print("Formation2:", Formation2) # afficher la formation2
print("Formation (prix minimums):", Formation) # afficher la formation avec le prix minimum
```
