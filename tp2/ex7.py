from ex3 import isValid
from ex5 import pwdGenerate

comptes = {}

# Demander le nombre de comptes à créer
try:
    nombre_comptes = int(input("Entrez le nombre de comptes à créer: "))
except ValueError:
    print("Erreur : Veuillez entrer un nombre entier.")
    exit()

comptes_crees = 0
while comptes_crees < nombre_comptes:
    continuer = input(
        "Appuyez sur -1 pour terminer ou toute autre touche pour continuer: "
    )
    if continuer == "-1":
        break
    # Demander les informations du compte
    login = input(f"Compte {comptes_crees + 1} - Entrez le login: ")
    email = input(f"Compte {comptes_crees + 1} - Entrez l'email: ")

    # Vérifier la validité
    if isValid(login, email):
        # Générer un mot de passe
        password = pwdGenerate()

        # Ajouter le compte au dictionnaire
        comptes[login] = {"email": email, "password": password}

        print(f"Compte créé avec succès pour {login}")
        comptes_crees += 1
    else:
        print("Erreur : Login ou email invalide. Veuillez réessayer.")


print("\nListe des comptes créés:")
for login, details in comptes.items():
    print(
        f"Login: {login}, Email: {details['email']}, Mot de passe: {details['password']}"
    )
