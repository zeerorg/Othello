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
    global white_places, black_places, main_matrix
    main_matrix[x][y] = int(color)
    if color > 0:
        white_places.append([x,y])
        if [x,y] in black_places:
            ind = black_places.index([x,y])
            black_places.pop(ind)
    else:
        black_places.append([x,y])
        if [x,y] in white_places:
            ind = white_places.index([x,y])
            white_places.pop(ind)


''' check if the given cell is valid or not '''
"""
def check_cell(x, y, color):
    tracker = []
    if color > 0:
        same = list(white_places)
        differ = list(black_places)
    else:
        same = list(black_places)
        differ = list(white_places)

    for check in same:
        if check == [x,y]:
            return
        difference = [check[0] - x, check[1] - y]
        if difference[0] == difference[1]:
            if check[0] > x:
                for hell_stepper in range(1,check[0] - x):
                    try:
                        ind = differ.index([x + hell_stepper, y + hell_stepper])
                        tracker.append(differ[ind])
                    except:
                        tracker = []
                        break
            else:
                for hell_stepper in range(1, x - check[0]):
                    try:
                        ind = differ.index([check[0] + hell_stepper, check[1] + hell_stepper])
                        tracker.append(differ[ind])
                    except:
                        tracker = []
                        break
        if difference[0] == 0:
            if check[1] > y:
                for hell_stepper in range(1, check[1] - y):
                    try:
                        ind = differ.index([check[0], hell_stepper + y])
                        tracker.append(differ[ind])
                    except:
                        tracker = []
                        break
            else:
                for hell_stepper in range(1, y - check[1]):
                    try:
                        ind = differ.index([check[0], check[1] + hell_stepper])
                        tracker.append(differ[ind])
                    except:
                        tracker = []
                        break

        if difference[1] == 0:
            if check[0] > x:
                for hell_stepper in range(1, check[0] - x):
                    try:
                        ind = differ.index([x + hell_stepper, check[1]])
                        tracker.append(differ[ind])
                    except:
                        tracker = []
                        break
            else:
                for hell_stepper in range(1, x - check[0]):
                    try:
                        ind = differ.index([check[0] + hell_stepper, check[1]])
                        tracker.append(differ[ind])
                    except:
                        tracker = []
                        break

        if tracker != []:
            for something in tracker:
                add_place(something[0], something[1], -color)

        tracker = []
        
                
        # TODO
                    
    pass
"""
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
add_place(4,3,1)
add_place(4,4,-1)
add_place(4, 2, -1)

check_cell(4, 5, 1)
check_cell(4, 1, 1)
print main_matrix
while not gameExit:
    start()

pygame.quit()
quit()

