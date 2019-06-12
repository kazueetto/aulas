x = 376
y= 324
BLACK = (0, 0, 0)
RESOL = [800, 600]
LOOP  = True
POS = (x,y)
SPRITE = "bolota.png"

import pygame
import serial
import time
 
ser = serial.Serial('COM8', 9600, timeout=0)

pygame.init()


screen = pygame.display.set_mode(RESOL)
screen.fill (BLACK)
sprite = pygame.image.load (SPRITE)



while LOOP:
    porta =ser.read()
    decodificado=porta.decode('utf-8')
    time.sleep(0.2)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            LOOP = False
    screen.blit (sprite, POS)
   
    if decodificado == "E":
        x=x-10
        POS = (x,y)
        pygame.display.update()
        

    if decodificado == "D":
        x=x+10
        POS = (x,y)
        pygame.display.update()


    if decodificado == "C":
        y=y+10
        POS = (x,y)
        pygame.display.update()

    if decodificado == "B":
        #print("teste1")
        y=y-10
        POS = (x,y)
        pygame.display.update()
        #print("teste2")
        
        
    print(decodificado)
