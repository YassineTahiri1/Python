class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."
    
personne1 = Personne("Ayoub", 20)
personne2 = Personne("Sara", 22)
personne3 = Personne("Mohamed", 30)

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())