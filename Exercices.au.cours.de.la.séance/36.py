class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Salarie(Personne):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.salaire = salaire


class Etudiant(Personne):
    def __init__(self, nom, prenom, niveau):
        super().__init__(nom, prenom)
        self.niveau = niveau


class Doctorant(Etudiant, Salarie):
    def __init__(self, nom, prenom, niveau, salaire):
        Etudiant.__init__(self, nom, prenom, niveau)
        Salarie.__init__(self, nom, prenom, salaire)