#Partie1:
def Valider(enregistrement):
    nom,matiere,note,groupe = enregistrement
    if nom == "" :
        return False , "Nom Vide"
    if matiere == "" :
        return False , "Matiere Vide"
    if groupe == "" :
        return False , "Groupe Vide"
    if not isinstance(note,(int,float)):
        return False , "Note non numerique"
    if note < 0 or note > 20 :
        return False , "Note Invalide"
    
    return True , ""

donnees = [
 ("Sara", "Math", 12, "G1"),
 ("Sara", "Info", 14, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Adam", "Chimie", 18, "G1"),
 ("Sara", "Math", 11, "G1"),
 ("Bouchra", "Info", "abc", "G2"),
 ("", "Math", 10, "G1"),
 ("Yassine", "Info", 22, "G2"),
 ("Ahmed", "Info", 13, "G2"),
 ("Adam", "Math", None, "G1"),
 ("Sara", "Chimie", 16, "G1"),
 ("Adam", "Info", 7, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Hana", "Physique", 15, "G3"),
 ("Hana", "Math", 8, "G3"),
]
print("Validite et raison: ")
for i in donnees :
    print(i,"->",Valider(i))
print("Liste des Tuples nettoyes: ")
valides = []
for i in donnees :
    if Valider(i)[0] == True :
        nom,matiere,note,groupe = i 
        valides += [(nom,matiere,float(note),groupe),]
print(valides)
print("Liste des Dictionnaires: ")
erreurs = [] 
for i in donnees:
    valide,raison = Valider(i)
    if valide is False :
        nom,matiere,note,groupe = i
        erreurs += [ {"ligne" : i , "raison" :  raison } ]
print(erreurs)
print("doublons_exact: ")
Unique = set()
doublons_exact = set()
for i in donnees:
    if i in Unique : 
        doublons_exact.add(i)
    else :
        Unique.add(i)
print(doublons_exact)
#Partie2
print("Matières enseignées")
Matieres = set()
for i in valides :
    nom,matiere,note,groupe = i
    Matieres.add(matiere)
print(Matieres)
print("Organisation des donnees: ")
MatieresNotes = {}
for i in valides :
    nom,matiere,note,groupe = i
    if nom not in MatieresNotes:
        MatieresNotes[nom] = {}
    if matiere not in MatieresNotes[nom]:
        MatieresNotes[nom][matiere] = []

    MatieresNotes[nom][matiere].append(note)
print(MatieresNotes)
print("Groupe : Etudiant")
GroupeEtu = {}
for i in valides:
    nom,matiere,note,groupe = i
    if groupe not in GroupeEtu:
        GroupeEtu[groupe] = set()
    if nom not in GroupeEtu[groupe]:
        GroupeEtu[groupe].add(nom)
print(GroupeEtu)
#partie3
# Mettre en place un calcul de somme basé sur la récursivité (une fonction qui s’appelle
# elle-même). À partir de cette somme récursive, définir un calcul de moyenne.
# • À partir de ces fonctions, calculer pour chaque étudiant sa moyenne générale ainsi que
# ses moyennes par matière.
print("somme basé sur la récursivité: ")
i = 0
Sum = 0
def somme (notes,i=0):
    if i == len(notes):
        return 0
    else:
        return notes[i] + somme(notes,i+1)
Notes = []
for i in valides:
    nom,matiere,note,groupe = i
    Notes.append(note)
print("La moyenne est :" ,somme(Notes)/len(Notes))
def moyenne(notes):
    if len(notes) == 0 :
        return 0
    else:
        return somme(notes) / len(notes)
for nom in MatieresNotes:
    print("Etudiant :",nom)
    AllNotes = []
    for matiere in MatieresNotes[nom]:
        notes = MatieresNotes[nom][matiere]
        print(matiere,":",moyenne(notes))
        AllNotes += notes
    print("LA moyenne generale est :",moyenne(AllNotes))
#Partie4
alertes = {
    "notes_multiples": [],
    "profil_incomplet": [],
    "groupe_faible": [],
    "ecart_important": []
}

for nom in MatieresNotes:
    for matiere in MatieresNotes[nom]:
        if len(MatieresNotes[nom][matiere]) > 1:
            alertes["notes_multiples"].append((nom, matiere, MatieresNotes[nom][matiere]))

for nom in MatieresNotes:
    if set(MatieresNotes[nom].keys()) != Matieres:
        alertes["profil_incomplet"].append(nom)

seuil = 10
for groupe in GroupeEtu:
    notes_groupe = []
    for nom in GroupeEtu[groupe]:
        for matiere in MatieresNotes[nom]:
            notes_groupe += MatieresNotes[nom][matiere]
    if len(notes_groupe) > 0:
        moy = moyenne(notes_groupe)
        if moy < seuil:
            alertes["groupe_faible"].append((groupe, moy))

seuil_ecart = 10
for nom in MatieresNotes:
    all_notes = []
    for matiere in MatieresNotes[nom]:
        all_notes += MatieresNotes[nom][matiere]
    if len(all_notes) > 0:
        ecart = max(all_notes) - min(all_notes)
        if ecart > seuil_ecart:
            alertes["ecart_important"].append((nom, ecart))

print(alertes)