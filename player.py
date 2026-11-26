from maths import *

# Paramètres de la gravité / saut (à trouver)
FORCE_GRAVITY           = +2.5
FORCE_JUMP              = -10
TERMINAL_VELOCITY       = 10000000

class Player:
    def __init__(self):
        self.pos = Vector(0, 0)
        self.dir = Vector(0, 0)
        self.acc = Vector(0, 0)

    def jump(self):
        """ Prépare un saut en changant l'accélération"""
        self.acc.y = FORCE_JUMP

    def move(self, joystick: tuple[float,float]):
        """ Applique un changement du joystick au joueur """
        pass # TODO

    def update(self, dt = 1 / 30):
        """ Calcule la position du joueur après {dt} secondes """
        self.dir += self.acc * dt
        if self.dir.length() > TERMINAL_VELOCITY:
            self.dir = self.dir.normalised() * TERMINAL_VELOCITY

        self.pos += self.dir * dt
        return self.pos
