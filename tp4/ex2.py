class Batiment:
    def __init__(self, adresse):
        self.adresse = adresse

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse

    def __str__(self):
        return f"Batiment: Adresse -> {self.adresse}"

class Maison(Batiment):
    def __init__(self, adresse, nbPieces):
        super().__init__(adresse)
        self.nbPieces = nbPieces

    def get_nbPieces(self):
        return self.nbPieces

    def set_nbPieces(self, nbPieces):
        self.nbPieces = nbPieces

    def __str__(self):
        return f"Maison: Adresse -> {self.adresse}, Nombre de pièces -> {self.nbPieces}"

class Immeuble(Batiment):
    def __init__(self, adresse, nbAppart):
        super().__init__(adresse)
        self.nbAppart = nbAppart

    def get_nbAppart(self):
        return self.nbAppart

    def set_nbAppart(self, nbAppart):
        self.nbAppart = nbAppart

    def __str__(self):
        return f"Immeuble: Adresse -> {self.adresse}, Nombre d'appartements -> {self.nbAppart}"


batiment1 = Batiment("123 Rue El massira")
print(batiment1)

maison1 = Maison("456 Avenue El waha", 5)
print(maison1)

immeuble1 = Immeuble("789 Boulevard d' Errachidia", 10)
print(immeuble1)
