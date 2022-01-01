class Rectangle:
   #constructeur du class rectangle initialise par default
    def __init__(self, longueur=30, largeur=15):

        self.lon = longueur
        self.lar = largeur
        self.nom = "rectangle"

    def surface(self): # methode calcul serface d'un rectangle

        return self.lon * self.lar

    def __str__(self):#methode d'affichage

        return ("\nLe {0} de côtes {1} et {2} a une surface de {3}"
                .format(self.nom, self.lon, self.lar, self.surface())+"m²")


class Carre(Rectangle): #class caree herit du class de base reclangle


    def __init__(self, cote=2):

        Rectangle.__init__(self, cote, cote)
        self.nom = "carre"  # surchage d'attribut d'instance

if __name__ == '__main__':
    r1 = Rectangle(1,3)
    print(r1)
    c1 = Carre(3)
    print(c1)