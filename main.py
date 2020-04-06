from pygame import *
from pvp import *

def main():

    main_screen = display.set_mode((600, 700))
    menu_rect = Rect(0, 0, 600, 600)
    pvp_rect = Rect(100, 200, 400, 100)
    easy_rect = Rect(100, 300, 400, 100)
    hard_rect = Rect(100, 400, 400, 100)
    exit_rect = Rect(100, 500, 400, 100)
    
    display.set_caption('ticktacktoe')
    menu_image = image.load("image/menu.bmp")
    pvp_image = image.load("image/pvp_menu.bmp")
    easy_image = image.load("image/easy_menu.bmp")
    hard_image = image.load("image/hard_menu.bmp")
    exit_image = image.load("image/exit_menu.bmp")
    
    while True:
        main_screen.blit(menu_image, menu_rect)
        display.update()
        flag = True
        while True:
            if not flag:
                break
            for i in event.get():
                if i.type == QUIT:
                    return
                if i.type == MOUSEMOTION:
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 200 and i.pos[1] <= 300:
                        main_screen.blit(menu_image, menu_rect)
                        main_screen.blit(pvp_image, pvp_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 300 and i.pos[1] <= 400:
                        main_screen.blit(menu_image, menu_rect)
                        main_screen.blit(easy_image, easy_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 400 and i.pos[1] <= 500:
                        main_screen.blit(menu_image, menu_rect)
                        main_screen.blit(hard_image, hard_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 500 and i.pos[1] <= 600:
                        main_screen.blit(menu_image, menu_rect)
                        main_screen.blit(exit_image, exit_rect)
                        display.update()
                if i.type == MOUSEBUTTONDOWN:
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 200 and i.pos[1] <= 300:
                        pvp()
                        flag = False
                        break
                    elif i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 300 and i.pos[1] <= 400:
                        pass
                    elif i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 400 and i.pos[1] <= 500:
                        pass
                    elif i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 500 and i.pos[1] <= 600:
                        exit()
                    
                
if __name__ == "__main__":
    main()