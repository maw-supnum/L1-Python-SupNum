# def f(n, x):
#     if x==0:
#         return 1
#     else:
#         return n*f(n,x-1)

# f(4,5)

def longueur_chaine_caracteres(s):
    if s == "":
        return 0
    else:
        return 1 + longueur_chaine_caracteres(s[1:])