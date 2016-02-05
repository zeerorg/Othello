# Othello game using Python and Pygame

import pygame

pygame.init()

''' Colors '''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

""" Initial Setup variables """
WIDTH = 800
HEIGHT = 600
FPS = 10
gamedisplay = pygame.display.set_mode([WIDTH,HEIGHT])
pyClock = pygame.time.Clock()
FPS = 60

""" Game function variables """
main_matrix = []
for x in range(8):
    main_matrix.append([0,0,0,0,0,0,0,0])

''' Getting game display to work  '''
pygame.display.set_caption('Othello')
gamedisplay.fill(white)

def create_table():
    pass

''' Main gameloop function '''
def start():
    global gameExit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


    create_table()
    pygame.display.update()
    pyClock.tick(FPS)

gameExit = False

while not gameExit:
    start()

pygame.quit()
quit()

