import random

# Premier réel entre 0.1 et 1
reel1 = random.uniform(0.1, 1.0)

# Deuxième réel entre 3.5 et 33.5
reel2 = random.uniform(3.5, 33.5)

# Afficher la somme des deux réels
somme = reel1 + reel2
print(f"La somme de {reel1} et {reel2} est {somme}")
