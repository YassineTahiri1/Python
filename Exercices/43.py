from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str


u1 = User(1, "Alice", "alice@mail.com")
u2 = User(1, "Alice", "alice@mail.com")

print(u1)
print(u1 == u2)