class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def se_presenter(self): 
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int) or valeur < 0:
            raise ValueError("Entrer une valeur INT")
        if valeur < 0:
            raise ValueError("La valeur doit être positive")
        if valeur > 140:
            raise ValueError("L'age est irrealiste")
        self._age = valeur
        
personne1 = Personne("Ayoub", 20)
print(personne1.se_presenter())
personne1.age = 25
print(personne1.se_presenter())

try:personne1.age = -20
except ValueError as e:   print(e)
try:    personne1.age = 200
except ValueError as e:    print(e)
try:    personne1.age = "trente"    
except ValueError as e:    print(e)