class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Rectangle(Point):
    def __init__(self, x, y, longueur, largeur):
        super().__init__(x, y)
        self.longueur = longueur
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def get_largeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, Longueur: {self.longueur}, Largeur: {self.largeur})"

class Parallelepipede(Rectangle):
    def __init__(self, x, y, longueur, largeur, hauteur):
        super().__init__(x, y, longueur, largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    def aire(self):
        return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)

    def volume(self):
        return self.longueur * self.largeur * self.hauteur

    def __str__(self):
        return f"Parallelepipede({self.x}, {self.y}, Longueur: {self.longueur}, Largeur: {self.largeur}, Hauteur: {self.hauteur})"


point1 = Point(1, 2)
print(point1)

rectangle1 = Rectangle(1, 2, 3, 4)
print(rectangle1)
print("Aire du rectangle:", rectangle1.aire())

parallelepipede1 = Parallelepipede(1, 2, 3, 4, 5)
print(parallelepipede1)
print("Aire du parallelepiped:", parallelepipede1.aire())
print("Volume du parallelepiped:", parallelepipede1.volume())
