from pygame import *
from main import CLOCK, MAIN_SCREEN

init()

x_image = image.load("image/x.bmp")
o_image = image.load("image/o.bmp")
game_zona_image = image.load("image/game_zona.bmp")
new_game_image = image.load("image/new_game.bmp")
exit_game_image = image.load("image/exit_game.bmp")
bottom_bar_image = image.load("image/bottom_bar.bmp")
bottom_bar_image_o = image.load("image/bottom_bar_o.bmp")
bottom_bar_image_x = image.load("image/bottom_bar_x.bmp")
image_win_x = image.load("image/win_x.bmp")
image_win_o = image.load("image/win_o.bmp")
image_standoff = image.load("image/standoff.bmp")

square1 = Rect(12, 12, 181, 181)
square2 = Rect(208, 12, 181, 181)
square3 = Rect(408, 12, 181, 181)
square4 = Rect(12, 208, 181, 181)
square5 = Rect(208, 208, 181, 181)
square6 = Rect(408, 208, 181, 181)
square7 = Rect(12, 408, 181, 181)
square8 = Rect(208, 408, 181, 181)
square9 = Rect(408, 408, 181, 181)
game_zona_rect = Rect(0, 0, 600, 600)
bottom_bar_rect = Rect(0, 600, 600, 100)
new_game_rect = Rect(0, 600, 240, 100)
exit_game_rect = Rect(360, 600, 240, 100)
bottom_bar_x_o_recr = Rect(240, 600, 120, 100)
win_rect = Rect(0, 0, 600, 700)

def checkWin(player, play_area):
    if player == 's':
        for i in play_area:
            if 0 in i:
                return False
        return True
    elif play_area[0][0] == player and play_area[0][1] == player and play_area[0][2] == player:
        return True
    elif play_area[1][0] == player and play_area[1][1] == player and play_area[1][2] == player:
        return True
    elif play_area[2][0] == player and play_area[2][1] == player and play_area[2][2] == player:
        return True
    elif play_area[0][0] == player and play_area[1][0] == player and play_area[2][0] == player:
        return True
    elif play_area[0][1] == player and play_area[1][1] == player and play_area[2][1] == player:
        return True
    elif play_area[0][2] == player and play_area[1][2] == player and play_area[2][2] == player:
        return True
    elif play_area[0][0] == player and play_area[1][1] == player and play_area[2][2] == player:
        return True
    elif play_area[0][2] == player and play_area[1][1] == player and play_area[2][0] == player:
        return True
    return False 

def winScreen(player):
    if player == 'x':
        MAIN_SCREEN.blit(image_win_x, win_rect)
        display.update()
    if player == 'o':
        MAIN_SCREEN.blit(image_win_o, win_rect)
        display.update()
    if player == 's':
        MAIN_SCREEN.blit(image_standoff, win_rect)
        display.update()
    while True:
        CLOCK.tick(30)
        for i in event.get():
            if i.type == QUIT:
                exit()
            if i.type == MOUSEBUTTONDOWN:
                return

def checkSquare(i1, i2, play_area, square, queue):
    if queue == 1:
        if not play_area[i1][i2]:
            play_area[i1][i2] = 'x'
            MAIN_SCREEN.blit(x_image, square)
            display.update()
            if checkWin('x', play_area): 
                winScreen('x')
                return 'win'
            elif checkWin('s', play_area):
                winScreen('s')
                return 'win'
            return 2
    else:
        if not play_area[i1][i2]:
            play_area[i1][i2] = 'o'
            MAIN_SCREEN.blit(o_image, square)
            display.update()
            if checkWin('o', play_area): 
                winScreen('o')
                return 'win'
            elif checkWin('s', play_area):
                winScreen('s')
                return 'win'
            return 1
    return False
    
def pvp():
    
    while True:
        MAIN_SCREEN.blit(game_zona_image, game_zona_rect)
        display.update()

        play_area = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        queue = 1
        flag = True
        
        while True:
            CLOCK.tick(30)
            if not flag:
                break
            if queue == 1:
                MAIN_SCREEN.blit(bottom_bar_image_x, bottom_bar_x_o_recr)
            else:
                MAIN_SCREEN.blit(bottom_bar_image_o, bottom_bar_x_o_recr)
            display.update()
            for i in event.get():
                if not flag:
                    break
                if i.type == QUIT:
                    exit()
                if i.type == MOUSEMOTION:
                    if i.pos[0] >= 0 and i.pos[0] <= 240 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        MAIN_SCREEN.blit(bottom_bar_image, bottom_bar_rect)
                        MAIN_SCREEN.blit(new_game_image, new_game_rect)
                        display.update()
                    if i.pos[0] >= 360 and i.pos[0] <= 600 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        MAIN_SCREEN.blit(bottom_bar_image, bottom_bar_rect)
                        MAIN_SCREEN.blit(exit_game_image, exit_game_rect)
                        display.update()
                    if i.pos[0] >= 0 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 600:
                        MAIN_SCREEN.blit(bottom_bar_image, bottom_bar_rect)
                        display.update()
                if i.type == MOUSEBUTTONDOWN:
                    # 1 square
                    if i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 0 and i.pos[1] <= 200:
                        box = checkSquare(0, 0, play_area, square1, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 2 square
                    elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 0 and i.pos[1] <= 200:
                        box = checkSquare(0, 1, play_area, square2, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 3 square
                    elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 200:
                        box = checkSquare(0, 2, play_area, square3, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 4 square
                    elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 200 and i.pos[1] <= 400:
                        box = checkSquare(1, 0, play_area, square4, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 5 square
                    elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 200 and i.pos[1] <= 400:
                        box = checkSquare(1, 1, play_area, square5, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 6 square
                    elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 200 and i.pos[1] <= 400:
                        box = checkSquare(1, 2, play_area, square6, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 7 square
                    elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 400 and i.pos[1] <= 600:
                        box = checkSquare(2, 0, play_area, square7, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 8 square
                    elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 400 and i.pos[1] <= 600:
                        box = checkSquare(2, 1, play_area, square8, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                    # 9 square
                    elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 400 and i.pos[1] <= 600:
                        box = checkSquare(2, 2, play_area, square9, queue)
                        if box == 1:
                            queue = 1
                        if box == 2:
                            queue = 2
                        if box == 'win':
                            flag = False
                 
                    # bottom bar
                    elif i.pos[0] >= 0 and i.pos[0] <= 240 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        flag = False
                    elif i.pos[0] >= 360 and i.pos[0] <= 600 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        return
if __name__ == "__main__":
    pvp()