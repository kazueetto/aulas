x = 376
y= 324
BLACK = (0, 0, 0)
RESOL = [800, 600]
LOOP  = True
POS = (x,y)
SPRITE = "BATEMAN.png"

import pygame
import serial
import time

CIDADE = pygame.image.load("cidade.jpg")
 
ser = serial.Serial('COM8', 9600, timeout=0)

pygame.init()


screen = pygame.display.set_mode(RESOL)
screen.fill (BLACK)
sprite = pygame.image.load (SPRITE)
screen.blit (CIDADE, (0,0))

while LOOP:
    porta =ser.read()
    decodificado=porta.decode('utf-8')
    time.sleep(0.2)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            LOOP = False
    screen.blit (sprite, POS)
   
    if (decodificado == "E" and x>0):
        x=x-10
        POS = (x,y)
        pygame.display.flip()
        

    if (decodificado == "D" and x<800):
        x=x+10
        POS = (x,y)
        pygame.display.update()


    if (decodificado == "C" and y<600):
        y=y+10
        POS = (x,y)
        pygame.display.update()

    if (decodificado == "B" and y>0):
        #print("teste1")
        y=y-10
        POS = (x,y)
        pygame.display.update()
        #print("teste2")
        
    if decodificado == "P":
        pygame.mixer.music.load('musica.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        
    print(decodificado)
