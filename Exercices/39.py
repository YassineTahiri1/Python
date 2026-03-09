class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    # Comparaison d'égalité
    def __eq__(self, other):
        if isinstance(other, Personne):
            return self.nom == other.nom
        return False

    # Comparaison pour le tri
    def __lt__(self, other):
        if isinstance(other, Personne):
            return self.age < other.age
        return NotImplemented


p1 = Personne("Alice", 25)
p2 = Personne("sqrq", 22)
p3 = Personne("Bob", 30)

print(p1 == p2)  # True
print(p1 == p3)  # False

personnes = [p1, p2, p3]

for n in personnes:
    print(n.nom)

personnes.sort()

print("breakkkk")

for n in personnes:
    print(n.nom)