class voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0

ma_voiture = voiture("Toyota", "Corolla", 2021)

print(f"marque: {ma_voiture.marque}")
print(f"modèle: {ma_voiture.modele}")
print(f"année: {ma_voiture.annee}")
print(f"kilométrage: {ma_voiture.kilometrage}")