import random
import string


def pwdGenerate():
    # Caractères disponibles
    lettres_maj = string.ascii_uppercase
    chiffres = string.digits
    symboles = string.punctuation
    tous_caracteres = string.ascii_letters + string.digits + string.punctuation

    password = []

    # Générer au moins 2 lettres majuscules
    for _ in range(2):
        letter = random.choice(lettres_maj)
        password.append(letter)

    # Ajouter au moins 1 chiffre
    chiffre = random.choice(chiffres)
    password.append(chiffre)

    # Ajouter au moins 1 symbole spécial
    symbole = random.choice(symboles)
    password.append(symbole)

    # Compléter jusqu'à 8 caractères
    while len(password) < 8:
        e_char = random.choice(tous_caracteres)
        password.append(e_char)

    # Mélanger le mot de passe
    random.shuffle(password)

    # Convertir la liste en chaîne
    return "".join(password)

print(pwdGenerate())
print(pwdGenerate())
print(pwdGenerate())