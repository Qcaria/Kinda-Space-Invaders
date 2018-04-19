import pygame, sys
from pygame.locals import *
import functions.var
from functions.var import white, black, red
from functions.control import *

def screener(): #Genera la pantalla
    screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
    pygame.display.set_caption("Space Invaders")
    pygame.mouse.set_visible(False)
    return screen

def drawframe(screen, lives, score, hscore, lvl):
    shipimg = pygame.image.load("C:/Users/Carlos/PycharmProjects/SpaceInvaders/sprites/shiplit.png")
    fontObj = pygame.font.Font('C:/Users/Carlos/PycharmProjects/SpaceInvaders/functions/PressStart2P.ttf', 20)
    scoretxt = fontObj.render('SCORE {}'.format(score), False, white)
    hscoretxt = fontObj.render("HIGH SCORE ", False, white)
    hscoretxt2 = fontObj.render(str(hscore), False, red)
    livestxt = fontObj.render("LIVES ", False, white)
    leveltxt = fontObj.render("LEVEL {}".format(lvl), False, white)

    screen.blit(scoretxt, (10, 15))
    screen.blit(hscoretxt, (350, 15))
    screen.blit(hscoretxt2, (570, 15))
    screen.blit(livestxt, (1100, 15))
    screen.blit(leveltxt, (800, 15))
    for i in range(lives - 1):
        screen.blit(shipimg, (1220 + 45*i, 10))

def gifter():   #Una función que tomando el clock anime los sprites
    if functions.var.clock % 3 == 0:
        aux = functions.var.shipimg
        functions.var.shipimg = functions.var.shipimg2
        functions.var.shipimg2 = aux
    if functions.var.clock % 30 == 0:
        aux = functions.var.bluealien
        functions.var.bluealien = functions.var.bluealien2
        functions.var.bluealien2 = aux
    if functions.var.clock % 30 == 0:
        aux = functions.var.alienred
        functions.var.alienred = functions.var.alienred2
        functions.var.alienred2 = aux
    if functions.var.clock % 30 == 0:
        aux = functions.var.aliengreen
        functions.var.aliengreen = functions.var.aliengreen2
        functions.var.aliengreen2 = aux

def mode(grid, cap1, cap2, cap3):   #devuelve el modo de juego
    count = counter(grid)
    if count >= cap1:
        mode = 0
    elif count >= cap2:
        mode = 1
    elif count >= cap3:
        mode = 2
    else:
        mode = 3
    return mode

def move_aliens(grid, mode, speeds, dir, cicler):
    speed = speeds[mode]
    a = 10
    if dir == "left":
        a = -a
    if dir == "down" and functions.var.clock % speed == 0:   #baja los marcianitos
        for k in range(len(grid[0])):
            grid[len(grid)-1-cicler][k] = (grid[len(grid)-1-cicler][k][0], grid[len(grid)-1-cicler][k][1] + 10)
        if cicler == len(grid)-1:
            if grid[len(grid)-1][(len(grid[0])//2)][0] > 700:
                dir = "left"
            else:
                dir = "right"
    elif functions.var.clock % speed == 0:       #Mueve los marcianitos lateralmente
        for i in range(len(grid[0])):
            grid[len(grid)-1-cicler][i] = (grid[len(grid)-1-cicler][i][0] + a, grid[len(grid)-1-cicler][i][1])
        if (grid[0][0][0] <= 29 and grid[len(grid)-1][0][0] <= 29) or (grid[0][len(grid[0])-1][0] >= 1280 and grid[len(grid)-1][len(grid[0])-1][0] >= 1280):
            dir = "down"

    if functions.var.clock % speed == 0:
        cicler += 1
        if cicler == len(grid):
            cicler = 0
    return cicler, dir

def draw_aliens(grid, screen):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i > 2:
                screen.blit(functions.var.alienred, grid[i][j])
            elif i > 0:
                screen.blit(functions.var.bluealien, grid[i][j])
            else:
                screen.blit(functions.var.aliengreen, grid[i][j])

