import numpy as np

# creer un tableau qui ne contient que les nombres pairs
# entre 0 et 50
T1 = np.arange(0, 51, 2)
print(T1)
print(type(T1))
print("\n\n")

# calcul des carres de T1
print(T1**2)

# T2 contient que les cosinus des carres des elements de T1
T2 = np.cos(T1**2)
print("T2: ", T2)
print("\n\n")

# minimum de T2
print("min T2: ", float(np.min(T2)))
print("\n\n")

# nombre de fois le max
max_de_T2 = np.max(T2)
print("max de T2: ", max_de_T2)
print("nombre d'occurences du max de T2: ", np.sum(T2 == max_de_T2))

# generer T3 1x10 coefs aleatoires dans [0,9]
T3 = np.random.randint(0, 10, size=(1,10))
print("T3: ", T3)
