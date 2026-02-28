print("1 : addition")
print("2 : soustraction")
print("3 : multiplication")
print("4 : division")
choix = int(input("Choix : "))
while True :
    if choix < 1 or choix > 4 :
        choix = int(input("Veuillez choisir un nombre compris entre 1 et 4 :"))
    else:
        break
value1 = int(input("Valeur 1 :"))
value2 = int(input("Valeur 2 :"))
match choix:
    case 1 :
        print(value1 + value2)
    case 2 :
        print(value1 - value2)
    case 3 :
        print(value1 * value2)
    case 4 : 
        try:
            print(value1/value2)
        except ZeroDivisionError :
            print("Impossible de diviser par 0 :)")