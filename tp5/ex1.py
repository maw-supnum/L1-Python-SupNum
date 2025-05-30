class Personne:
    # nom = None
    # prenom = None
    # age = None
    # adresse = None
    pass

#     def dummy_method(self):
#         pass
    
#     def __repr__(self):

#         return (
#             f"{self.__class__.__name__}("
#             f"nom={self.nom}, "
#             f"prenom={self.prenom}, "
#             f"age={self.age}, "
#             f"adresse={self.adresse}"
#             f")"
#         )

class Personne:
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    def __repr__(self):
        return (
                f"{self.__class__.__name__}("
                f"nom={self.nom}, "
                f"prenom={self.prenom}, "
                f"age={self.age}, "
                f"adresse={self.adresse}"
                f")"
        )

p1 = Personne("Mohamed", "sidi", 12, "Leksar")
p1.from_string("Mohamed, sidi, 12, Leksar")
p2 = Personne("Attik", "Khaled", 17, "Premier")

print(p1)
print(p2)