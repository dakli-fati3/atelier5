class Etudiant:

    nom = ""
    prenom = ""
    age = 0
    cne = ""
    moyenne = 0

    def __init__(self, nom="", prenom="", age=0, cne="", moyenne=0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
    def display(self):
        print(self.nom, "\t""\t", self.prenom, "\t""\t", self.age, "\t""\t", self.cne, "\t""\t", self.moyenne)

if __name__ == '__main__':

  e1 = Etudiant("fati", "th", 29, "2001", 20)
  e2 = Etudiant("jaafar", "hi", 20, "2001", 12)
  e3 = Etudiant("monir", "tera", 17, "2001", 17.5)
  e4 = Etudiant("mohmed", "ahmed", 14, "2001", 14)


ListEtudiants = []
ListEtudiants.append(e1)
ListEtudiants.append(e2)
ListEtudiants.append(e3)
ListEtudiants.append(e4)


#sort selon l'age et la moyen :

def MySortAM(etudiant):
    return -etudiant.moyenne - etudiant.age

#sort selon la moyen :

def MySortm(etudiant):
    return -etudiant.moyenne

#sort selon l'age  :

def MySortA(etudiant):
    return -etudiant.age

#affichage:
#sort selon l'age et la moyen :
print("\nliste triee selon l'age et le moyenne\n")
ListEtudiants.sort(key=MySortAM)
for i in ListEtudiants:
    i.display()
print("\nliste triee selon le moyenne\n")
#sort selon la moyen :
ListEtudiants.sort(key=MySortm)
for i in ListEtudiants:
    i.display()
print("\nliste triee selon l'age\n")
#sort selon la l'age :
ListEtudiants.sort(key=MySortA)
for i in ListEtudiants:
    i.display()