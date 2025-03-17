# Consignes pour le TP3

## Exercice 1

demander le chemin d'un fichier à l'utilisateur (utiliser la fonction `input`):

```python
# Demander le chemin du fichier
chemin_fichier = ...
```

respecter les formats suivants pour l'affichage des resultats:

```python
print(f"Nombre de caractères: {nb_caracteres}")
print(f"Nombre de mots: {nb_mots}")
print(f"Nombre de lignes: {nb_lignes}")
```

En cas d'erreur, respecter le format suivant d'affichage:

```python
raison = ...
print(f"Erreur : {raison}")
```

## Exercice 2

demander le chemin d'un fichier à l'utilisateur (utiliser la fonction `input`):

```python
# le chemin du fichier
chemin_fichier = ...
```

demander le mot à rechercher dans le fichier à l'utilisateur (utiliser la fonction `input`):

```python
# le mot à rechercher
mot_recherche = ...
```

respecter les formats suivants pour l'affichage des resultats:

```python
print(f"Le mot '{mot_recherche}' a été trouvé {nombre_occurences} fois dans le fichier.")
```

En cas d'erreur, respecter le format suivant d'affichage:

```python
raison = ...
print(f"Erreur : {raison}")
```

## Exercice 3

demander le chemin d'un fichier à l'utilisateur (utiliser la fonction `input`):

```python
# le chemin du fichier
chemin_fichier = ...
```

demander le mot à remplacer dans le fichier à l'utilisateur (utiliser la fonction `input`):

```python
mot_original = ...
```

demander le mot de remplacement à l'utilisateur (utiliser la fonction `input`):

```python
nouveau_mot = ...
```

afficher les resultats en respectant les formats suivants:

```python
print(f"Nombre d'occurrences de '{mot_original}': {occurrences_avant}")
print(f"Nombre d'occurrences de '{nouveau_mot}': {occurrences_apres}")
```

En cas d'erreur, respecter le format suivant d'affichage:

```python
raison = ...
print(f"Erreur : {raison}")
```

si le mot original n'est pas trouvé, afficher le message suivant:

```python
print(f"Le mot '{mot_original}' n'existe pas dans le fichier.")
```

## Exercice 4

1. mettre le fichier `Liste_L1.txt` dans le dossier `tp3`.

2. la fonction `obtenir_nom_par_matricule` doit respecter la signature suivante et les formats d'affichage suivants:

signature:

```python
# le chemin du fichier
# 2. Fonction pour obtenir le nom complet à partir du matricule
def obtenir_nom_par_matricule(matricule, nom_fichier="Liste_L1.txt"):
    ...
```

si étudiant n'est pas trouvé, retouner `None` et afficher le message suivant:

```python
"Étudiant non trouvé"
```

gestion des erreurs (format d'affichage):

```python
raison = ...
print(f"Erreur : {raison}")
```

3. Afficher les membres d'un groupe TP

demander le numero du groupe TP à l'utilisateur (utiliser la fonction `input`):

```python
# le numero du groupe TP
numero_groupe = ...
```

respecter les formats suivants pour l'affichage des resultats:

```python
print(f"Membres du groupe TP{numero_groupe}:")
```

pour chaque membre, afficher le nom complet et le matricule:

```python
print(f"{prenom} {nom} ({matricule})")
```

En cas d'erreur, respecter le format suivant d'affichage:

```python
raison = ...
print(f"Erreur : {raison}")
```

4. Créer six fichiers pour les groupes TP

la fonction `creer_fichiers_groupes` doit respecter la signature suivante et les formats d'affichage et de naming suivants:

signature:

```python
def creer_fichiers_groupes(nom_fichier="Liste_L1.txt"):
    ...
```

En cas d'erreur, respecter le format suivant d'affichage:

```python
raison = ...
print(f"Erreur : {raison}")
```

chaque groupe doit être dans un fichier nommé `TPX.txt` où `X` est le numero du groupe TP.
