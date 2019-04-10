x = 376
y= 324
BLACK = (255, 255, 255)
RESOL = [800, 600]
LOOP  = True
POS = (x,y)
SPRITE = "rosa.png"

import pygame
pygame.init()

screen = pygame.display.set_mode(RESOL)
screen.fill (BLACK)
sprite = pygame.image.load (SPRITE)

while LOOP:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            LOOP = False
    screen.blit (sprite, POS)
    if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                x=x-1
                POS = (x,y)
                pygame.display.update()
            if e.key == pygame.K_RIGHT:
                x=x+1
                POS = (x,y)
                pygame.display.update()
            if e.key == pygame.K_DOWN:
                y=y+1
                POS = (x,y)
                pygame.display.update()
            if e.key == pygame.K_UP:
                y=y-1
                POS = (x,y)
                pygame.display.update()
    

pygame.quit()
