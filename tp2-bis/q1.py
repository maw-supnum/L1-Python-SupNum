from sys import prefix

codes = ("dev210", "dev211", "syr210", "syr211", "mai210", "mai211", "mai212")
noms = ("python", "lang. web", "systeme logic", "systeme d'exploitation", "algebre2", "proba et stat", "pix2")

# for i in range(len(codes)):
#     print(f"{codes[i]}: {noms[i]}")

# for code, nom in zip(codes, noms):
#     print(f"{code}: {nom}")

# print(list(zip(codes, noms)))

# print(dict(zip(codes, noms)))

dict_cours = dict(zip(codes, noms))
# print(dict_cours.get("fyuguifdxez"))
# code_a_tester = input("saisir le code: ")
# print(dict_cours.get(code_a_tester))

# prefix = input("saisir le prefix: ")
# prefix = "dev"
# for code, nom in dict_cours.items():
#     # if prefix in code: # ne marche pas
#     # if code[:len(prefix)] == prefix:
#     if code.startswith(prefix):
#         print(f"{code}: {nom}")

for code in sorted(codes):
    print(f"{code}: {dict_cours[code]}")

# for code, nom in sorted(zip(codes, noms), key = lambda x: x[0]):
#     print(f"{code}: {nom}")



