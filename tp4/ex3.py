class Employe:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def gains(self):
        pass

    def __str__(self):
        return f"Employe: {self.prenom} {self.nom}"

class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.salaire = salaire

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def gains(self):
        return self.salaire

    def __str__(self):
        return f"Patron: {self.prenom} {self.nom}, Salaire: {self.salaire}"

class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.salaire = salaire
        self.commission = commission
        self.quantite = quantite

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def get_commission(self):
        return self.commission

    def set_commission(self, commission):
        self.commission = commission

    def get_quantite(self):
        return self.quantite

    def set_quantite(self, quantite):
        self.quantite = quantite

    def gains(self):
        return self.salaire + self.commission * self.quantite

    def __str__(self):
        return f"Travailleur à la Commission: {self.prenom} {self.nom}, Salaire: {self.salaire}, Commission: {self.commission}, Quantité: {self.quantite}"

class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.retribution = retribution
        self.heures = heures

    def get_retribution(self):
        return self.retribution

    def set_retribution(self, retribution):
        self.retribution = retribution

    def get_heures(self):
        return self.heures

    def set_heures(self, heures):
        self.heures = heures

    def gains(self):
        return self.retribution * self.heures

    def __str__(self):
        return f"Travailleur Horaire: {self.prenom} {self.nom}, Rétribution: {self.retribution}, Heures: {self.heures}"


employes = [Patron("Alaoui", "Hassan", 5000),
            TravailleurCommission("Alaoui", "Houssin", 2000, 10, 100),
            TravailleurHoraire("Alaoui", "Anass", 15, 160)]

for employe in employes:
    print(employe)
    print("Gains:", employe.gains())
    print()
