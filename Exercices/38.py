class Vecteur:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre):
        return Vecteur(self.x - autre.x, self.y - autre.y)

    def __str__(self):
        return f"Vecteur({self.x}, {self.y})"


v1 = Vecteur(3, 4)
v2 = Vecteur(1, 2)

# Addition de vecteurs
v3 = v1 + v2   # équivalent à v1.__add__(v2)
print(v3)

# Soustraction de vecteurs
v4 = v1 - v2
print(v4)