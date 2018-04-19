import pygame, sys
from pygame.locals import *

fpsClock = pygame.time.Clock()
pygame.init()
bluealien = pygame.image.load("C:/Users/Carlos/PycharmProjects/SpaceInvaders/sprites/alienblue.png")

window = pygame.display.set_mode((640, 480))
image = pygame.Surface((300, 300), pygame.SRCALPHA, 32)
image = image.convert_alpha()
image.set_colorkey((255, 0, 255))
image.blit(bluealien, (0, 0))
image2 = pygame.transform.scale(image, (80, 80))
image.blit(bluealien, (0, 0))
pygame.display.set_caption("Hello World!")
a = 0
b = 0
p = 0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.key.get_pressed()[K_UP]:
        b -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        b += 5
    if pygame.key.get_pressed()[K_LEFT]:
        a -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        a += 5
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (p, 20, 100, 50))
    window.blit(image2, (a, b))
    pygame.draw.rect(window, (255, 0, 0), (250, 250, 20, 20))
    if 250 in range(a-40, a + 39) and 250 in range(b-40, b+39): #LA HITBOX ES UN RECTÁNGULO ASÍ
        pygame.quit()
        sys.exit()
    p += 2
    if p == 300:
        p = 0
    pygame.display.update()
    fpsClock.tick(30)