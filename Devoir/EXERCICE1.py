try:
    age = int(input("Entrer votre age : "))

    if age >= 0 and age<=12 :
        print("Enfant")
    elif age >12 and age <=17 :
        print("Adolescent")
    elif age >17 and age <=64 :
        print("Adulte")
    elif age>64 : 
        print("Senior")

except ValueError:
    print("Entrer une valeur valide")
