from pygame import *

def checkWin(player):
    if PLAY_AREA[0][0] == player and PLAY_AREA[0][1] == player and PLAY_AREA[0][2] == player:
        return True
    elif PLAY_AREA[1][0] == player and PLAY_AREA[1][1] == player and PLAY_AREA[1][2] == player:
        return True
    elif PLAY_AREA[2][0] == player and PLAY_AREA[2][1] == player and PLAY_AREA[2][2] == player:
        return True
    elif PLAY_AREA[0][0] == player and PLAY_AREA[1][0] == player and PLAY_AREA[2][0] == player:
        return True
    elif PLAY_AREA[0][1] == player and PLAY_AREA[1][1] == player and PLAY_AREA[2][1] == player:
        return True
    elif PLAY_AREA[0][2] == player and PLAY_AREA[1][2] == player and PLAY_AREA[2][2] == player:
        return True
    elif PLAY_AREA[0][0] == player and PLAY_AREA[1][1] == player and PLAY_AREA[2][2] == player:
        return True
    elif PLAY_AREA[0][2] == player and PLAY_AREA[1][1] == player and PLAY_AREA[2][0] == player:
        return True
    return False 

def winScreen(player):
    PLAY_AREA[:] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    QUEUE = 1
    winX = image.load("image/winX.bmp")
    winO = image.load("image/winO.bmp")
    if player == 1:
        MAIN_SCREEN.blit(winX, SCREEN)
        display.update()
    else:
        MAIN_SCREEN.blit(winO, SCREEN)
        display.update()
    while True:
        CLOCK.tick(30)
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN:
                MAIN_SCREEN.fill((255,255,255))
                draw.line(MAIN_SCREEN, (0, 0, 0), [0, 200], [600, 200], 9)
                draw.line(MAIN_SCREEN, (0, 0, 0), [0, 400], [600, 400], 9)
                draw.line(MAIN_SCREEN, (0, 0, 0), [200, 0], [200, 600], 9)
                draw.line(MAIN_SCREEN, (0, 0, 0), [400, 0], [400, 600], 9)
                display.update()
                return

def main():
    global PLAY_AREA, MAIN_SCREEN, QUEUE, CLOCK, SCREEN
    
    init()

    CLOCK = time.Clock()
    MAIN_SCREEN = display.set_mode((600, 600))
    MAIN_SCREEN.fill((255,255,255))
    display.set_caption('X - O')
    draw.line(MAIN_SCREEN, (0, 0, 0), [0, 200], [600, 200], 9)
    draw.line(MAIN_SCREEN, (0, 0, 0), [0, 400], [600, 400], 9)
    draw.line(MAIN_SCREEN, (0, 0, 0), [200, 0], [200, 600], 9)
    draw.line(MAIN_SCREEN, (0, 0, 0), [400, 0], [400, 600], 9)
    square1 = Rect(5, 5, 190, 190)
    square2 = Rect(205, 5 , 190, 190)
    square3 = Rect(405, 5, 190, 190)
    square4 = Rect(5, 205, 190, 190)
    square5 = Rect(205, 205, 190, 190)
    square6 = Rect(405, 205, 190, 190)
    square7 = Rect(5, 405, 190, 190)
    square8 = Rect(205, 405, 190, 190)
    square9 = Rect(405, 405, 190, 190)
    SCREEN = Rect(0, 0, 600, 600)
    draw_1 = image.load("image/x.bmp")
    draw_2 = image.load("image/o.bmp")
    display.update()

    PLAY_AREA = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    QUEUE = 1

    while True:
        CLOCK.tick(30)
        for i in event.get():
            if i.type == QUIT:
                return
            if i.type == MOUSEBUTTONDOWN:
                # 1 square
                if i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[0][0] = 1
                        MAIN_SCREEN.blit(draw_1, square1)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[0][0] = 2
                        MAIN_SCREEN.blit(draw_2, square1)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 2 square
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[0][1] = 1
                        MAIN_SCREEN.blit(draw_1, square2)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[0][1] = 2
                        MAIN_SCREEN.blit(draw_2, square2)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 3 square
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[0][2] = 1
                        MAIN_SCREEN.blit(draw_1, square3)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[0][2] = 2
                        MAIN_SCREEN.blit(draw_2, square3)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 4 square
                elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[1][0] = 1
                        MAIN_SCREEN.blit(draw_1, square4)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[1][0] = 2
                        MAIN_SCREEN.blit(draw_2, square4)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 5 square
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[1][1] = 1
                        MAIN_SCREEN.blit(draw_1, square5)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[1][1] = 2
                        MAIN_SCREEN.blit(draw_2, square5)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 6 square
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[1][2] = 1
                        MAIN_SCREEN.blit(draw_1, square6)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[1][2] = 2
                        MAIN_SCREEN.blit(draw_2, square6)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 7 square
                elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[2][0] = 1
                        MAIN_SCREEN.blit(draw_1, square7)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[2][0] = 2
                        MAIN_SCREEN.blit(draw_2, square7)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 8 square
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[2][1] = 1
                        MAIN_SCREEN.blit(draw_1, square8)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[2][1] = 2
                        MAIN_SCREEN.blit(draw_2, square8)
                        display.update()
                        if checkWin(2): winScreen(2)
                # 9 square
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if QUEUE == 1:
                        QUEUE = 2
                        PLAY_AREA[2][2] = 1
                        MAIN_SCREEN.blit(draw_1, square9)
                        display.update()
                        if checkWin(1): winScreen(1)
                    else:
                        QUEUE = 1
                        PLAY_AREA[2][2] = 2
                        MAIN_SCREEN.blit(draw_2, square9)
                        display.update()
                        if checkWin(2): winScreen(2)
 
if __name__ == "__main__":
    main()