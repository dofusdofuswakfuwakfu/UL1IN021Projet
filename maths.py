# "I'm old!" (this file is like 6 months old now. i'm not kiddin. i'm not kidding)
import math

class Matrix2:
    def __init__(self, m = None):
        """ Initialise une matrice 'vide' """
        self.mat = [0, 0, 0, 0] if m is None else m
    def identity(self):
        """ Met la matrice en 'identité' """
        self.mat = [1, 0, 0, 1]
        return self
    def rotation(self, theta):
        self[0,0] = +math.cos(theta)
        self[0,1] = +math.sin(theta)
        self[1,0] = -math.sin(theta)
        self[1,1] = +math.cos(theta)
        return self
    def scale(self, kx = 1, ky = 1):
        """ Remplace la matrice par une matrice d'"homothétie" (enfin, pas vraiment) """
        self[0,0] = kx
        self[1,1] = ky
        self[0,1] = 0
        self[1,0] = 0
        return self
    def hshear(self, t):
        """ i dont know how to explain this one right """
        self[0,0] = 1
        self[1,1] = 1
        self[0,1] = t
        self[1,0] = 0
        return self
    def __getitem__(self, key):
        line, column = key
        return self.mat[line + column * 2]
    def __setitem__(self, key, v):
        line, column = key
        self.mat[line + column * 2] = v
    def __mul__(self, other):
        if type(other) == Matrix2:
            ret = Matrix2()
            for y in range(2):
                for x in range(2):
                    summa = 0
                    for i in range(2):
                        summa += self[y,i] * other[i,x]
                    ret[y,x] = summa
            return ret
        elif type(other) == Vector:
            return Vector(other.x * self[0,0] + other.y * self[0,1], other.x * self[1,0] + other.y * self[1,1])
        else:
            raise TypeError("erm... what the sigma?")


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def length(self):
        return ((self.x ** 2) + (self.y ** 2))**0.5
    def normalised(self):
        return Vector(self.x, self.y) / self.length()
    def as_tuple(self):
        """ Convertit notre vecteur en tuple ordinaire """
        return self.x, self.y
    def angle(self, screenspace=True):
        """ Calcule l'angle d'un vecteur en radians (dans la rangée 0 à 2pi). 
        Si screenspace est False, alors ceci calculera sur un plan où Y pointe 
        vers le haut (comme dans un plan orthonormé), avec le Y et sinus inversé. """
        t = 0
        if screenspace:
            t = math.atan2(-self.y, +self.x)
        else:
            t = math.atan2(+self.y, +self.x)
        if t < 0:
            t += math.tau   # NB: math.tau = 2pi, et 2pi=0 [2pi]
        return t
    def __add__(self, other):
        """ Calcule la somme de deux vecteurs
        Usage: vecteur_a + vecteur_b """
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        """ Calcule le produit scalaire entre deux vecteurs si 
        nous multiplions par un vecteur, OU calcule other*self si 
        other est un nombre (int|float) """
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        elif type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("erm... what the sigma?")
    def __repr__(self) -> str:
        return f'<vector:{str(self.as_tuple())}>'

def lerp(a: Vector, b: Vector, t: float) -> Vector:
    """ Retourne la position à t unités entre a et b.
    Par exemple, si t=0, cette fonction retournera a, 
    si t=1, cette fonction retourne b, et si t=0.5, 
    cette fonction retournera le milieu du segment [ab] """
    return a + (b - a) * t

