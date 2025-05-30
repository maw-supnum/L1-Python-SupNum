import pytest

from tp5.ex2 import Voiture

class TestVoiture:
    def test1(self):
        v1 = Voiture.voiture()
        assert v1.get_marque() == "NotDefined"
        assert v1.get_couleur() == "NotDefined"
        assert v1.get_prix() == 100

        v2 = Voiture.voiture("marque")
        assert v2.get_couleur() == "NotDefined"
        assert v2.get_prix() == 100
        assert v2.get_marque() == "marque"

    def test2(self):
        v3 = Voiture(marque="Toyota", prix=10000)
        assert v3.get_marque() == "Toyota"
        assert v3.get_prix() == 10000
        assert v3.get_couleur() == "NotDefined"

    def test3(self):
        _ = Voiture.voiture(marque="Honda", prix=15000)

    def test4(self):
        v4 = Voiture.voiture(marque="SNIM", prix=20000)
        assert v4.get_marque() == "SNIM"
        assert v4.get_couleur() == "NotDefined"
        assert v4.get_prix() == 20000

        v4.set_marque("ASTON")
        v4.set_couleur("rouge")

        assert v4.get_marque() == "ASTON"
        assert v4.get_couleur() == "rouge"

        with pytest.raises(ValueError):
            v4.set_marque(1)

        with pytest.raises(ValueError):
            v4.set_couleur(3)

    def test5(self):
        v5 = Voiture(marque="GM", prix=12000)
        v5.set_couleur("jaune")

        assert str(v5) == "Voiture(marque='GM'; couleur='jaune'; prix=12000; puissance=10000)"

    def test6(self):
        v6 = Voiture(marque="GM", prix=12000)
        v6.set_couleur("gris")

        v7 = Voiture(marque="Honda", prix=12000)
        v7.set_couleur("gris")

        v8 = Voiture(marque="GM", prix=12030)
        v8.set_couleur("gris")

        v9 = Voiture(marque="GM", prix=12000)
        v9.set_couleur("jaune")

        v10 = Voiture(marque="GM", prix=12000)
        v10.set_couleur("gris")

        assert v6 != v7
        assert v6 != v8
        assert v6 != v9
        assert v6 == v10









