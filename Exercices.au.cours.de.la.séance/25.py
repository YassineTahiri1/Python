class Personne:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

personne1 = Personne("Alice", 28, "Alice@email.com")

print(f"Nom: {personne1.name}")
print(f"Âge: {personne1.age}")
print(f"Email: {personne1.mail}")

personne1.name = "Alice Dubois"
personne1.age += 1
personne1.mail = "alice.dubois@email.com"

print(f"Nouveau nom: {personne1.name}")
print(f"Nouvel âge: {personne1.age}")
print(f"Nouvel email: {personne1.mail}")