# Exercice 3 - Validation de login et email
def isValid(login, email):
    # Vérification de la longueur
    if len(login) > 256 or len(email) > 256:
        return False

    # Vérification du login (lettres et chiffres uniquement)
    if not login.isalnum():
        return False

    # Vérification de l'email
    # 1. Un seul symbole @
    if email.count("@") != 1:
        return False

    # 2. Diviser en parties avant et après @
    parties = email.split("@")
    avant_at, apres_at = parties[0], parties[1]

    # 3. Au moins un caractère avant @
    if len(avant_at) == 0:
        return False

    # 4. Au moins un caractère après @ et avant le point
    if "." not in apres_at:
        return False

    domaine = apres_at.split(".")
    if len(domaine[0]) < 1:
        return False

    return True


login = "3myname"
email = "l@g.c"
print(isValid(login, email))