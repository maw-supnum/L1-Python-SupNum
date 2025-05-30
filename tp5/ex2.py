class Voiture:
    _marque: str = "NotDefined"
    _couleur: str = "NotDefined"
    _prix: int = 100
    _puissance: int = 10000

    def __init__(self, marque:str | None = None, prix: int | None =None):
        if marque is not None:
            self._marque = marque
        if prix is not None:
            self._prix = prix
        # validation de puissance
        try:
            assert isinstance(self._puissance, int)
        except AssertionError:
            raise ValueError(f"Puissance must be an integer, got {self._puissance}")
        try:
            assert self._puissance >= 0
        except AssertionError:
            raise ValueError(f"Puissance must be a positive integer, got {self._puissance}")


    @classmethod
    def voiture(cls, marque=None, prix:int| None=None):
        ob = cls(marque, prix)
        if marque is not None:
            ob._marque = marque
        return ob

    def get_couleur(self):
        return self._couleur

    def get_prix(self):
        return self._prix

    def get_marque(self):
        return self._marque

    def set_marque(self, marque: str):
        if not isinstance(marque, str):
            raise ValueError(f"Marque must be a string, got {type(marque).__name__}")
        self._marque = marque

    def set_couleur(self, couleur:str):
        if not isinstance(couleur, str):
            raise ValueError(f"Couleur must be a string, got {type(couleur).__name__}")
        self._couleur = couleur

    def __str__(self):
        return (f"{self.__class__.__name__}(marque='{self._marque}'; "
                f"couleur='{self._couleur}'; prix={self._prix}; puissance={self._puissance})"
                )

    def __eq__(self, other: "Voiture"):
        return (self._marque == other._marque and self._prix == other._prix
                and self._puissance == other._puissance and self._couleur == other._couleur)