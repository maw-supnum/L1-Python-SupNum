# Programme qui vérifie si un nombre appartient à un intervalle

# Saisie des bornes de l'intervalle
borne_inf = float(input("Entrez la borne inférieure de l'intervalle : "))
borne_sup = float(input("Entrez la borne supérieure de l'intervalle : "))

# Saisie du nombre à vérifier
nombre = float(input("Entrez le nombre à vérifier : "))

# Vérification que l'intervalle est valide
if borne_inf > borne_sup:
    print("Erreur : la borne inférieure doit être plus petite que la borne supérieure")
else:
    # Vérification de l'appartenance à l'intervalle
    if borne_inf <= nombre <= borne_sup:
        print(
            f"Le nombre {nombre} appartient à l'intervalle [{borne_inf}, {borne_sup}]"
        )
    else:
        print(
            f"Le nombre {nombre} n'appartient pas à l'intervalle [{borne_inf}, {borne_sup}]"
        )
