class Vecteur2D:
# constructeur par defult
    def __init__(self, x0=0, y0=0):

        self.x = x0
        self.y = y0
  # methode pour afficher les vecteurs
    def affiche(self):

       print("x = %.2f, y = %.2f" % (self.x, self.y))


# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
       vec1 = Vecteur2D();
       vec2 = Vecteur2D(-0.1, 2)
       print(" le vecteur  par defaut ")
       vec1.affiche()
        # --
       print(" le vecteur initialisee ".center(50, '-'))
       vec2.affiche()
