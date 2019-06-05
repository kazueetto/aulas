x = 376
y= 324
BLACK = (0, 0, 0)
RESOL = [800, 600]
LOOP  = True
POS = (x,y)
SPRITE = "bolota.png"

import pygame
from serial import Serial
import time
 
ser = serial.Serial('/dev/ttyACM0', 9600)

pygame.init()


screen = pygame.display.set_mode(RESOL)
screen.fill (BLACK)
sprite = pygame.image.load (SPRITE)



while LOOP:
    porta =ser.read()
    time.sleep(0.2)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            LOOP = False
    screen.blit (sprite, POS)
   
    if porta == "E":
        x=x-10
        POS = (x,y)
        pygame.display.update()
        

    if porta == "D":
        x=x+10
        POS = (x,y)
        pygame.display.update()


    if porta == "C":
        y=y+10
        POS = (x,y)
        pygame.display.update()

    if porta == "B":
        y=y-10
        POS = (x,y)
        pygame.display.update()
