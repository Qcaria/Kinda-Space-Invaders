import pygame, sys
from pygame.locals import *
import functions.var


def quitter():
    for event in pygame.event.get():
        if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            pygame.quit()
            sys.exit()

def clocker():
    functions.var.clock += 1
    if functions.var.clock == 121:
        functions.var.clock = 1

def grider(inx, iny, sepx, sepy):
    grid = [[],[],[],[],[]]
    for i in range(5):
        for j in range(12):
            grid[i].append((inx + j * sepx, iny + i * sepy))
    return grid

def counter(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "N":
                count += 1
    return count

def move_ship(Ship):
    if pygame.key.get_pressed()[K_LEFT] and Ship.pos >= 0:
        Ship.pos -= 5
    if pygame.key.get_pressed()[K_RIGHT] and Ship.pos <= 1300:
        Ship.pos += 5