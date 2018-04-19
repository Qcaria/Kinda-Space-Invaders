################################################################################
#       Carlos Munuera Javaloy                              23/11/2017         #
#                                 SPACE INVADERS                               #
################################################################################

import pygame, sys
from pygame.locals import *
from functions.ship import *
from functions.interfaz import *
from functions.control import *
import functions.var

pygame.init()
grid = grider(30, 80, 80, 50)
fpsClock = pygame.time.Clock()
screen = screener()

#imagen 3x3
Ship = SpaceShip(0)
mode = 0
speeds = [5, 12, 10, 8]
dir = "right"
cicle = 0
#######################################################################################
#GAME LOOP!
while True:
    while True:
        screen.fill(black)
        clocker()
        gifter()
        #################################################### Codigo del game loop aquí:
        move_ship(Ship)
        draw_aliens(grid, screen)
        screen.blit(functions.var.shipimg, (Ship.pos, 723))
        quitter()
        cicle, dir = move_aliens(grid, mode, speeds, dir, cicle)
        drawframe(screen, 4, 300, 3000, 1)
        #############################################################################
        pygame.display.update()
        fpsClock.tick(30)
