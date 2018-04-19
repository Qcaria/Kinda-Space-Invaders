from functions.var import *
import pygame

class SpaceShip:        #Objeto que carga la información de la nave
    lives = 3
    lasers = []

    def __init__(self, x):
        self.pos = x

    def shoot(self):
        self.lasers.append((self.pos))      #Estructurado muy básicamente