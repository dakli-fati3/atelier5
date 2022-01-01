class Point:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Segment:
    orig = Point(0, 0)
    extrem = Point(0, 0)

    def __init__(self, Xo=0, Yo=0, Xe=0, Ye=0 ):
        self.orig.x = Xo
        self.orig.y = Yo
        self.extrem.x = Xe
        self.extrem.y = Ye

    def display(self):
        print("l’origine : (", self.orig.x, ", ", self.orig.y, ")  l’extrémité : (", self.extrem.x, ", ", self.extrem.y, ")")

s = Segment(1, 2, 3, 4)
s.display()