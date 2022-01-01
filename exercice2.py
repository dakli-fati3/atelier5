class Vecteur2D:
# constructeur par defult
    def __init__(self, x0=0, y0=0):

        self.x = x0
        self.y = y0
  # methode pour afficher les vecteurs
    def affiche(self):

       print("x = %.2f, y = %.2f" % (self.x, self.y))
    def somme (self , x1 , y1,  x2 , y2):
        print("x = %.2f, y = %.2f" % (x1+x2, y2+y1))

# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
       vec1 = Vecteur2D(2,1);
       vec2 = Vecteur2D(-0.1, 2)
       vect3 = Vecteur2D();

       print(" le vecteur  par defaut ")
       vec1.affiche()
       print(" le vecteur initialisee ")
       vec2.affiche()
       print(" la somme des deux vecteur ")
       vect3.somme(2,1,-0.1,2)