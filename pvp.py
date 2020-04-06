from pygame import *

def check_win(player, play_area):
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

def win_screen(player, screen):
    win_rect = Rect(0, 0, 600, 700)
    image_win_x = image.load("image/win_x.bmp")
    image_win_o = image.load("image/win_o.bmp")
    image_standoff = image.load("image/standoff.bmp")
    if player == 'x':
        screen.blit(image_win_x, win_rect)
        display.update()
    if player == 'o':
        screen.blit(image_win_o, win_rect)
        display.update()
    if player == 's':
        screen.blit(image_standoff, win_rect)
        display.update()
    while True:
        for i in event.get():
            if i.type == QUIT:
                exit()
            if i.type == MOUSEBUTTONDOWN:
                return
                
def pvp():
    
    init()

    clock = time.Clock()
    main_screen = display.set_mode((600, 700))
    
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
    
    x_image = image.load("image/x.bmp")
    o_image = image.load("image/o.bmp")
    game_zona_image = image.load("image/game_zona.bmp")
    new_game_image = image.load("image/new_game.bmp")
    exit_game_image = image.load("image/exit_game.bmp")
    bottom_bar_image = image.load("image/bottom_bar.bmp")
    bottom_bar_image_o = image.load("image/bottom_bar_o.bmp")
    bottom_bar_image_x = image.load("image/bottom_bar_x.bmp")
    
    while True:
        main_screen.blit(game_zona_image, game_zona_rect)
        display.update()

        play_area = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        queue = 1
        flag = True
        
        while True:
            clock.tick(30)
            if not flag:
                break
            if queue == 1:
                main_screen.blit(bottom_bar_image_x, bottom_bar_x_o_recr)
            else:
                main_screen.blit(bottom_bar_image_o, bottom_bar_x_o_recr)
            display.update()
            for i in event.get():
                if not flag:
                    break
                if i.type == QUIT:
                    exit()
                if i.type == MOUSEMOTION:
                    if i.pos[0] >= 0 and i.pos[0] <= 240 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        main_screen.blit(bottom_bar_image, bottom_bar_rect)
                        main_screen.blit(new_game_image, new_game_rect)
                        display.update()
                    if i.pos[0] >= 360 and i.pos[0] <= 600 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        main_screen.blit(bottom_bar_image, bottom_bar_rect)
                        main_screen.blit(exit_game_image, exit_game_rect)
                        display.update()
                    if i.pos[0] >= 0 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 600:
                        main_screen.blit(bottom_bar_image, bottom_bar_rect)
                        display.update()
                if i.type == MOUSEBUTTONDOWN:
                    # 1 square
                    if i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 0 and i.pos[1] <= 200:
                        if queue == 1:
                            if not play_area[0][0]:
                                queue = 2
                                play_area[0][0] = 'x'
                                main_screen.blit(x_image, square1)
                                display.update()
                                if check_win('x', play_area): 
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[0][0]:
                                queue = 1
                                play_area[0][0] = 'o'
                                main_screen.blit(o_image, square1)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 2 square
                    elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 0 and i.pos[1] <= 200:
                        if queue == 1:
                            if not play_area[0][1]:
                                queue = 2
                                play_area[0][1] = 'x'
                                main_screen.blit(x_image, square2)
                                display.update()
                                if check_win('x', play_area):
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[0][1]:
                                queue = 1
                                play_area[0][1] = 'o'
                                main_screen.blit(o_image, square2)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 3 square
                    elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 200:
                        if queue == 1:
                            if not play_area[0][2]:
                                queue = 2
                                play_area[0][2] = 'x'
                                main_screen.blit(x_image, square3)
                                display.update()
                                if check_win('x', play_area):
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[0][2]:
                                queue = 1
                                play_area[0][2] = 'o'
                                main_screen.blit(o_image, square3)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 4 square
                    elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 200 and i.pos[1] <= 400:
                        if queue == 1:
                            if not play_area[1][0]:
                                queue = 2
                                play_area[1][0] = 'x'
                                main_screen.blit(x_image, square4)
                                display.update()
                                if check_win('x', play_area): 
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[1][0]:
                                queue = 1
                                play_area[1][0] = 'o'
                                main_screen.blit(o_image, square4)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 5 square
                    elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 200 and i.pos[1] <= 400:
                        if queue == 1:
                            if not play_area[1][1]:
                                queue = 2
                                play_area[1][1] = 'x'
                                main_screen.blit(x_image, square5)
                                display.update()
                                if check_win('x', play_area): 
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[1][1]:
                                queue = 1
                                play_area[1][1] = 'o'
                                main_screen.blit(o_image, square5)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 6 square
                    elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 200 and i.pos[1] <= 400:
                        if queue == 1:
                            if not play_area[1][2]:
                                queue = 2
                                play_area[1][2] = 'x'
                                main_screen.blit(x_image, square6)
                                display.update()
                                if check_win('x', play_area):
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[1][2]:
                                queue = 1
                                play_area[1][2] = 'o'
                                main_screen.blit(o_image, square6)
                                display.update()
                                if check_win('o', play_area):
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 7 square
                    elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 400 and i.pos[1] <= 600:
                        if queue == 1:
                            if not play_area[2][0]:
                                queue = 2
                                play_area[2][0] = 'x'
                                main_screen.blit(x_image, square7)
                                display.update()
                                if check_win('x', play_area):
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[2][0]:
                                queue = 1
                                play_area[2][0] = 'o'
                                main_screen.blit(o_image, square7)
                                display.update()
                                if check_win('o', play_area):
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 8 square
                    elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 400 and i.pos[1] <= 600:
                        if queue == 1:
                            if not play_area[2][1]:
                                queue = 2
                                play_area[2][1] = 'x'
                                main_screen.blit(x_image, square8)
                                display.update()
                                if check_win('x', play_area):
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[2][1]:
                                queue = 1
                                play_area[2][1] = 'o'
                                main_screen.blit(o_image, square8)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # 9 square
                    elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 400 and i.pos[1] <= 600:
                        if queue == 1:
                            if not play_area[2][2]:
                                queue = 2
                                play_area[2][2] = 'x'
                                main_screen.blit(x_image, square9)
                                display.update()
                                if check_win('x', play_area):
                                    win_screen('x', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                        else:
                            if not play_area[2][2]:
                                queue = 1
                                play_area[2][2] = 'o'
                                main_screen.blit(o_image, square9)
                                display.update()
                                if check_win('o', play_area): 
                                    win_screen('o', main_screen)
                                    flag = False
                                    break
                                elif check_win('s', play_area):
                                    win_screen('s', main_screen)
                                    flag = False
                                    break
                    # bottom bar
                    elif i.pos[0] >= 0 and i.pos[0] <= 240 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        flag = False
                    elif i.pos[0] >= 360 and i.pos[0] <= 600 and i.pos[1] >= 600 and i.pos[1] <= 700:
                        return
if __name__ == "__main__":
    pvp()