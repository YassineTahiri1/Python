class Vehicule:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse

    def accelerer(self):
        print(f"{self.marque} accelere")

    def freiner(self):
        print(f"{self.marque} freine")


class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nb_portes):
        super().__init__(marque, vitesse)
        self.nb_portes = nb_portes

    # Heriter de fnct accelerer
    # Heriter de fnct freiner

    def klaxonner(self):
        print(f"{self.marque} klaxonne")


unevoiture = Voiture("Peugeot", 0, 5)

unevoiture.accelerer()
unevoiture.freiner()
unevoiture.klaxonner()