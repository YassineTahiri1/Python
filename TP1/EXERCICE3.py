motdepasse = "python123"
saisie = input("Entrer le mot de passe : ")
while motdepasse != saisie :
    print("Le mot de passe est inccorect !")
    saisie = input("Entrer le mot de passe a nouveau : ")
print("Le Mot de passe est correcte :) ")