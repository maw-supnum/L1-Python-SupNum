# Définition des dictionnaires de formation
Formation1 = {"Python": 1500, "Django": 3500, "PHP": 1600, "Java": 1800}
Formation2 = {"Python": 1200, "Django": 3600, "PHP": 1750, "Java": 2000}

# Création du dictionnaire Formation avec les prix minimums
Formation = {}

# Parcourir les clés et trouver le prix minimum pour chaque formation
for module in Formation1:
    Formation[module] = min(Formation1[module], Formation2[module])

# Affichage des résultats
print("Formation1:", Formation1)
print("Formation2:", Formation2)
print("Formation (prix minimums):", Formation)
