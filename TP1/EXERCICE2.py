contacts = ["Ahmed","Yassine","Ali","Salma"]
while True :
    print("1.Ajouter")
    print("2.Afficher")
    print("3.Quitter")
    choix = int(input("Choix: "))
    if choix == 1 :
        new = input("Entrer le prenom de l'utilisateur : ")
        contacts.append(new)
    elif choix == 2 :
        for index , contact in enumerate(contacts,start=1):
            print(index , contact)
    elif choix == 3 :
        break
    else:
        print("Entrer une valeur valide !")
