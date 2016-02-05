import pygame
import random

pygame.init()

''' Colors '''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

WIDTH = 800
HEIGHT = 600
FPS = 10
gamedisplay = pygame.display.set_mode([WIDTH,HEIGHT])
pyClock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption('Othello')
gamedisplay.fill(white)

def start():
    global gameExit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    pygame.display.update()
    pyClock.tick(FPS)

gameExit = False

while not gameExit:
    start()

pygame.quit()
quit()

