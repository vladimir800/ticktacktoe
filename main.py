from pygame import *
from pvp import *

init()

MAIN_SCREEN = display.set_mode((600, 700))
display.set_caption('ticktacktoe')
CLOCK = time.Clock()

menu_image = image.load("image/menu.bmp")
pvp_image = image.load("image/pvp_menu.bmp")
easy_image = image.load("image/easy_menu.bmp")
hard_image = image.load("image/hard_menu.bmp")
exit_image = image.load("image/exit_menu.bmp")

menu_rect = Rect(0, 0, 600, 600)
pvp_rect = Rect(100, 200, 400, 100)
easy_rect = Rect(100, 300, 400, 100)
hard_rect = Rect(100, 400, 400, 100)
exit_rect = Rect(100, 500, 400, 100)

def main():
    
    while True:
        MAIN_SCREEN.blit(menu_image, menu_rect)
        display.update()
        flag = True
        while True:
            CLOCK.tick(30)
            if not flag:
                break
            for i in event.get():
                if i.type == QUIT:
                    return
                if i.type == MOUSEMOTION:
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 200 and i.pos[1] <= 300:
                        MAIN_SCREEN.blit(menu_image, menu_rect)
                        MAIN_SCREEN.blit(pvp_image, pvp_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 300 and i.pos[1] <= 400:
                        MAIN_SCREEN.blit(menu_image, menu_rect)
                        MAIN_SCREEN.blit(easy_image, easy_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 400 and i.pos[1] <= 500:
                        MAIN_SCREEN.blit(menu_image, menu_rect)
                        MAIN_SCREEN.blit(hard_image, hard_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 500 and i.pos[1] <= 600:
                        MAIN_SCREEN.blit(menu_image, menu_rect)
                        MAIN_SCREEN.blit(exit_image, exit_rect)
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