from abc import ABC , abstractmethod
from dataclasses import dataclass
class Boisson(ABC):
    @abstractmethod
    def prix(self):
        pass
    @abstractmethod
    def description(self):
        pass
    def __add__(self, other):
        return BoissonCombinee(self , other)
    def AfficherC(self):
        print("Commande: " , self.description())
        print("Prix: ",self.prix())

class Cafe(Boisson):
    def prix(self):
        return 12
    def description(self):
        return "Cafe simple"
    
class The(Boisson):
    def prix(self):
        return 8
    def description(self):
        return "The a la menthe"

C = Cafe()
T = The()
print(C.prix())
print(C.description())
print(T.prix())
print(T.description())
C.AfficherC()

class DecorateurBoisson(Boisson):

    def __init__(self , boisson):
        self._boisson = boisson

class Lait(DecorateurBoisson):
    def prix(self):
        return self._boisson.prix() + 0.5
    def description(self):
        return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def prix(self):
        return self._boisson.prix() + 0.2
    def description(self):
        return self._boisson.description() + "Sucre"
    
boisson = Cafe()
boisson = Lait(boisson)
boisson = Sucre(boisson)

print(boisson.description())
print(boisson.prix())

# Partie 4
class BoissonCombinee(Boisson):
    def __init__(self , b1 , b2):
        self.b1 = b1
        self.b2 = b2 
    def prix(self):
        return self.b1.prix() + self.b2.prix()
    def description(self):
        return self.b1.description() + self.b2.description()

Menu = C + T 
print(Menu.prix())        
print(Menu.description())
# Partie 5
@dataclass
class Client:
    nom = str
    numero = str
    point = int
# Partie 5
class Caramel(DecorateurBoisson):
    def prix(self):
        return self._boisson.prix() + 1
    def description(self):
        return self._boisson.description() + ",Caramel"
caramel = Caramel(C)
S = caramel + C
S.AfficherC()
# Partie 7
from abc import ABC, abstractmethod

class Boisson(ABC):
    @abstractmethod
    def prix(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def __add__(self, other):
        return BoissonCombinee(self, other)

class Cafe(Boisson):
    def prix(self):
        return 2

    def description(self):
        return "Cafe simple"

class The(Boisson):
    def prix(self):
        return 1.5

    def description(self):
        return "The a la menthe"

class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson

class Lait(DecorateurBoisson):
    def prix(self):
        return self._boisson.prix() + 0.5

    def description(self):
        return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def prix(self):
        return self._boisson.prix() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"

class Caramel(DecorateurBoisson):
    def prix(self):
        return self._boisson.prix() + 1

    def description(self):
        return self._boisson.description() + ", Caramel"

class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def prix(self):
        return self.b1.prix() + self.b2.prix()

    def description(self):
        return self.b1.description() + " + " + self.b2.description()

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.points = 0

class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        return sum(b.prix() for b in self.boissons)

    def afficher(self):
        print("Client :", self.client.nom)
        for b in self.boissons:
            print("-", b.description(), ":", b.prix(), "€")
        print("Total :", self.prix_total(), "€")

class CommandeSurPlace(Commande):
    def afficher(self):
        print("Commande sur place")
        super().afficher()

class CommandeEmporter(Commande):
    def afficher(self):
        print("Commande a emporter")
        super().afficher()

class Fidelite:
    def ajouter_points(self, client, montant):
        client.points += int(montant)

class CommandeFidele(Commande, Fidelite):
    def valider(self):
        total = self.prix_total()
        self.ajouter_points(self.client, total)

client = Client("Yassine")

cafe = Cafe()
cafe = Lait(cafe)
cafe = Sucre(cafe)

the = The()
the = Caramel(the)

menu = cafe + the

commande = CommandeFidele(client)

commande.ajouter_boisson(cafe)
commande.ajouter_boisson(the)
commande.ajouter_boisson(menu)

commande.afficher()

commande.valider()

print("Points fidelite :", client.points)

# Partie 8
print("1. Les ingrédients peuvent être ajoutés facilement grâce au Decorator Pattern avec la classe DecorateurBoisson.")

print("2. Pour ajouter une nouvelle boisson comme ChocolatChaud, il suffit de créer une nouvelle classe qui hérite de Boisson.")

print("3. Séparer les responsabilités rend le code plus clair, plus organisé et plus facile à modifier.")