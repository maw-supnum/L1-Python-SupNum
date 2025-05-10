# Dictionnaire des étudiants avec leurs moyennes
etudiants = {"Salem": 12, "Ba": 15, "Mariem": 7, "Sidi": 9.5, "Med": 8.5, "Issa": 11}

# Création des dictionnaires pour les étudiants validés et non validés
V = {}  # Étudiants validés (moyenne >= 10)
NV = {}  # Étudiants non validés (moyenne < 10)

# Parcourir le dictionnaire des étudiants
for nom, moyenne in etudiants.items():
    if moyenne >= 10:
        V[nom] = moyenne
    else:
        NV[nom] = moyenne

# Affichage des résultats
print("Dictionnaire original des étudiants :")
print(etudiants)
print("\nÉtudiants validés (moyenne >= 10) :")
print(V)
print("\nÉtudiants non validés (moyenne < 10) :")
print(NV)
