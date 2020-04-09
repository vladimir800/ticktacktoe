from pygame import *

init()
MAIN_SCREEN = display.set_mode((600, 700))
CLOCK = time.Clock()

x_image = image.load("image/x_4x4.bmp")
o_image = image.load("image/o_4x4.bmp")
game_zona_image = image.load("image/zona_4x4.bmp")
new_game_image = image.load("image/new_game.bmp")
exit_game_image = image.load("image/exit_game.bmp")
bottom_bar_image = image.load("image/bottom_bar.bmp")
bottom_bar_image_o = image.load("image/bottom_bar_o.bmp")
bottom_bar_image_x = image.load("image/bottom_bar_x.bmp")
image_win_x = image.load("image/win_x.bmp")
image_win_o = image.load("image/win_o.bmp")
image_standoff = image.load("image/standoff.bmp")

square1 = Rect(12, 12, 131, 131)
square2 = Rect(158, 12, 131, 131)
square3 = Rect(308, 12, 131, 131)
square4 = Rect(458, 12, 131, 131)
square5 = Rect(12, 158, 131, 131)
square6 = Rect(158, 158, 131, 131)
square7 = Rect(308, 158, 131, 131)
square8 = Rect(458, 158, 131, 131)
square9 = Rect(12, 308, 131, 131)
square10 = Rect(158, 308, 131, 131)
square11 = Rect(308, 308, 131, 131)
square12 = Rect(458, 308, 131, 131)
square13 = Rect(12, 458, 131, 131)
square14 = Rect(158, 458, 131, 131)
square15 = Rect(308, 458, 131, 131)
square16 = Rect(458, 458, 131, 131)
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
    for i1, line in enumerate(play_area):
        for i2, square in enumerate(line):
            if play_area[i1][i2] == player:
                try:
                    if play_area[i1][i2 + 1] == player:
                        if play_area[i1][i2 + 2] == player:
                            return True
                except IndexError: pass
                try:
                    if play_area[i1 + 1][i2] == player:
                        if play_area[i1 + 2][i2] == player:
                            return True
                except IndexError: pass
                try:
                    if play_area[i1 + 1][i2 + 1] == player:
                        if play_area[i1 + 2][i2 + 2] == player:
                            return True
                except IndexError: pass
                try:
                    if play_area[i1 + 1][i2 - 1] == player:
                        if play_area[i1 + 2][i2 - 2] == player:
                            return True
                except IndexError: pass
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
                return

def checkSquare(i1, i2, play_area, square, queue):
    if queue == 'x':
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
            return 'o'
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
            return 'x'
    return False
 
def game4x4():
    while True:
        MAIN_SCREEN.blit(game_zona_image, game_zona_rect)
        display.update()

        play_area = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        queue = 'x'
        flag = True

        while True:
            CLOCK.tick(30)
            if not flag:
                break
            if queue == 'x':
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
                    if i.pos[0] >= 0 and i.pos[1] >= 0 and i.pos[0] <= 150 and i.pos[1] <= 150:
                        box = checkSquare(0, 0, play_area, square1, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 150 and i.pos[1] >= 0 and i.pos[0] <= 300 and i.pos[1] <= 150:
                        box = checkSquare(0, 1, play_area, square2, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 300 and i.pos[1] >= 0 and i.pos[0] <= 450 and i.pos[1] <= 150:
                        box = checkSquare(0, 2, play_area, square3, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 450 and i.pos[1] >= 0 and i.pos[0] <= 600 and i.pos[1] <= 150:
                        box = checkSquare(0, 3, play_area, square4, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 0 and i.pos[1] >= 150 and i.pos[0] <= 150 and i.pos[1] <= 300:
                        box = checkSquare(1, 0, play_area, square5, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 150 and i.pos[1] >= 150 and i.pos[0] <= 300 and i.pos[1] <= 300:
                        box = checkSquare(1, 1, play_area, square6, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 300 and i.pos[1] >= 150 and i.pos[0] <= 450 and i.pos[1] <= 300:
                        box = checkSquare(1, 2, play_area, square7, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 450 and i.pos[1] >= 150 and i.pos[0] <= 600 and i.pos[1] <= 300:
                        box = checkSquare(1, 3, play_area, square8, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 0 and i.pos[1] >= 300 and i.pos[0] <= 150 and i.pos[1] <= 450:
                        box = checkSquare(2, 0, play_area, square9, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 150 and i.pos[1] >= 300 and i.pos[0] <= 300 and i.pos[1] <= 450:
                        box = checkSquare(2, 1, play_area, square10, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 300 and i.pos[1] >= 300 and i.pos[0] <= 450 and i.pos[1] <= 450:
                        box = checkSquare(2, 2, play_area, square11, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 450 and i.pos[1] >= 300 and i.pos[0] <= 600 and i.pos[1] <= 450:
                        box = checkSquare(2, 3, play_area, square12, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 0 and i.pos[1] >= 450 and i.pos[0] <= 150 and i.pos[1] <= 600:
                        box = checkSquare(3, 0, play_area, square13, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 150 and i.pos[1] >= 450 and i.pos[0] <= 300 and i.pos[1] <= 600:
                        box = checkSquare(3, 1, play_area, square14, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 300 and i.pos[1] >= 450 and i.pos[0] <= 450 and i.pos[1] <= 600:
                        box = checkSquare(3, 2, play_area, square15, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 450 and i.pos[1] >= 450 and i.pos[0] <= 600 and i.pos[1] <= 600:
                        box = checkSquare(3, 3, play_area, square16, queue)
                        if box == 'x':
                            queue = 'x'
                        if box == 'o':
                            queue = 'o'
                        if box == 'win':
                            flag = False
                    elif i.pos[0] >= 0 and i.pos[0] <= 240 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        flag = False
                    elif i.pos[0] >= 360 and i.pos[0] <= 600 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        return
if __name__ == "__main__":
    game4x4()