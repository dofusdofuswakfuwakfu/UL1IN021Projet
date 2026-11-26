from maths import *
class Player:
    def __init__(self):
        self.pos = Vector(0, 0)
        self.dir = Vector(0, 0)
        self.acc = Vector(0, 0)

    def jump(self):
        """ TODO: Prépare un saut en changant l'accélération"""
        pass

    def update(self, dt = 1 / 30):
        """ Calcule la position du joueur après {dt} secondes """
        self.dir += self.acc * dt
        self.pos += self.dir * dt
        return self.pos
