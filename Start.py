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
gameExit = False

""" Game function variables """
main_matrix = []
white_places = []
black_places = []
for x in range(8):
    main_matrix.append([0,0,0,0,0,0,0,0])

''' Getting game display to work  '''
pygame.display.set_caption('Othello')
gamedisplay.fill(white)

''' Adding color to places '''
def add_place(x,y,color):
    global main_matrix
    main_matrix[y][x] = int(color)

''' Turning all the checks between (x1,y1) and (x2, y2) '''
def turn_all(x1, y1, x2, y2, color, stepx, stepy):
    nx1 = int(x1)
    ny1 = int(y1)
    print x1, y1, x2, y2, stepx, stepy
    while nx1 != x2 or ny1 != y2:
        nx1 += stepx
        ny1 += stepy
        add_place(nx1, ny1, color)

    add_place(x1, y1, color)
    pass


''' check if the given cell is valid or not '''

def check_cell(x, y, color):
    stepx = [0, 1, 1, 1, 0, -1, -1, -1]
    stepy = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(8):
        checkx = x + stepx[i]
        checky = y + stepy[i]
        if main_matrix[checky][checkx] == -color:
            while checkx >= 0 and checkx <= 8 and checky >= 0 and checky <= 8:
                if main_matrix[checky][checkx] == color:
                    turn_all(x, y, checkx, checky, color, stepx[i], stepy[i])
                    break
                elif main_matrix[checky][checkx] == 0:
                    break
                checkx += stepx[i]
                checky += stepy[i]
    pass

def draw_table():
    pass

''' Main gameloop function '''
def start():
    global gameExit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


    draw_table()
    pygame.display.update()
    pyClock.tick(FPS)


""" Init game """
add_place(3,3,1)
add_place(3,4,-1)
add_place(4,3,-1)
add_place(4,4,1)

add_place(2, 4, -1)

print main_matrix

check_cell(1, 4, 1)
print main_matrix

check_cell(4, 5, -1)
print main_matrix
while not gameExit:
    start()

pygame.quit()
quit()

