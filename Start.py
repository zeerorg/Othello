# Othello game using Python and Pygame

import pygame
import time

pygame.init()

''' Colors '''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 0)

""" Initial Setup variables """
WIDTH = 800
HEIGHT = 400
FPS = 10
gamedisplay = pygame.display.set_mode([WIDTH,HEIGHT])
pyClock = pygame.time.Clock()
FPS = 60
gameExit = False
font = pygame.font.SysFont(None, 25)

''' Getting game display to work  '''
pygame.display.set_caption('Othello')
gamedisplay.fill(yellow)

''' Adding color to places '''
def add_place(x,y,color):
    global main_matrix
    main_matrix[y][x] = int(color)

''' Turning all the checks between (x1,y1) and (x2, y2) '''
def turn_all(x1, y1, x2, y2, color, stepx, stepy):
    nx1 = int(x1)
    ny1 = int(y1)
    while nx1 != x2 or ny1 != y2:
        nx1 += stepx
        ny1 += stepy
        add_place(nx1, ny1, color)

    add_place(x1, y1, color)
    pass


''' check if the given cell is valid or not '''

def check_cell(x, y, color2, doturn = True):
    global color
    if main_matrix[y][x] != 0:
        return -1
    stepx = [0, 1, 1, 1, 0, -1, -1, -1]
    stepy = [1, 1, 0, -1, -1, -1, 0, 1]
    flag = False
    for i in range(8):
        checkx = x + stepx[i]
        checky = y + stepy[i]
        if checkx >= 0 and checkx <= 7 and checky >= 0 and checky <= 7 and main_matrix[checky][checkx] == -color2:
            while checkx >= 0 and checkx <= 7 and checky >= 0 and checky <= 7:
                if main_matrix[checky][checkx] == color2:
                    if doturn:
                        turn_all(x, y, checkx, checky, color2, stepx[i], stepy[i])
                    flag = True
                    break
                elif main_matrix[checky][checkx] == 0:
                    break
                checkx += stepx[i]
                checky += stepy[i]
    if flag:
        if doturn:
            color = -color
        return 1
    else:
        return -1


""" Check the whole table """
def check_whole_table():
    global color
    flag = False
    for iter_x in range(8):
        for iter_y in range(8):
            if check_cell(iter_x, iter_y, color, False) == 1:
                flag = True
                break
    if not flag:
        color = -color
    pass

""" Draw Table on canvas """

def draw_table():
    for y in range(8):
        for x in range(8):
            pygame.draw.rect(gamedisplay, red, [x*50, y*50, 50, 50], 2)
            if main_matrix[y][x] == 1:
                pygame.draw.circle(gamedisplay, white, [x*50 + 25, y*50 + 25], 25)
            elif main_matrix[y][x] == -1:
                pygame.draw.circle(gamedisplay, black, [x*50 + 25, y*50 + 25], 25)


""" Mouse position check """
def mouse_pos():
    global x, y, newx, newy, color
    co_ord = pygame.mouse.get_pos()
    if color == -1:
        _c_ = black
    else:
        _c_ = white
    if co_ord[0] < 400 and co_ord[1] < 400:
        x = int(co_ord[0]/50)
        y = int(co_ord[1]/50)

        if main_matrix[y][x] == 0:
            draw_table()
            pygame.draw.circle(gamedisplay, _c_, [x*50 + 25, y*50 + 25], 25, 3)


""" Display Score and check if game is finished """

def disp_score():
    global font, ctr_white, ctr_black, gameExit
    ctr_white = 0
    ctr_black = 0
    for x in range(8):
        for y in range(8):
            if main_matrix[y][x] == -1:
                ctr_black += 1
            elif main_matrix[y][x] == 1:
                ctr_white += 1

    
    msg = "White:"+str(ctr_white)+ "    Black:" + str(ctr_black)
    score_disp = font.render(msg, True, black)
    gamedisplay.blit(score_disp, [500, 200])

    if ctr_white + ctr_black == 64:
        gameExit = True
        if ctr_white > ctr_black:
            quit_game(False, 1)
        else:
            quit_game(False, -1)
    pass

""" If player wants to quit the game """
def quit_game(cont=True, winner=None):
    global gameExit, font
    gameExit = False
    gamedisplay.fill(yellow)
    if cont:
        msg = "Press SPACE to continue"
        msg2 = "ESC to quit"
    else:
        msg = "Winner is "
        if winner is 1:
            msg += "WHITE: "+str(ctr_white)
        else:
            msg += "BLACK: "+str(ctr_black)

        msg2 = "Press SPACE to continue"

    draw_table()
    quit_disp = font.render(msg, True, black)
    quit_disp2 = font.render(msg2, True, black)
    gamedisplay.blit(quit_disp, [500, 200])
    gamedisplay.blit(quit_disp2, [500, 300])
    pygame.display.update()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not cont:
                        reset()
                    start()
                elif event.key == pygame.K_ESCAPE:
                    gameExit = True

    if not cont:
        pygame.display.quit()
        pygame.quit()
        quit()                
    pass


''' Main gameloop function '''
def start():
    global gameExit, color
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 400 and pos[1] < 400:
                    x = int(pos[0]/50)
                    y = int(pos[1]/50)
                    check_cell(x, y, color)

        gamedisplay.fill(yellow)
        check_whole_table()
        draw_table()
        mouse_pos()
        disp_score()
        pygame.display.update()
        pyClock.tick(FPS)

    quit_game()
    pygame.display.quit()
    pygame.quit()
    quit()


    

""" Init game """
def reset():
    global main_matrix, white_places, black_places, color
    main_matrix = []
    white_places = []
    black_places = []
    color = -1
    for x in range(8):
        main_matrix.append([0,0,0,0,0,0,0,0])

    add_place(3,3,1)
    add_place(3,4,-1)
    add_place(4,3,-1)
    add_place(4,4,1)
    pass

reset()
start()
