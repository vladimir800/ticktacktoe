from pygame import *
from game3x3 import game3x3
from game4x4 import game4x4

init()

MAIN_SCREEN = display.set_mode((600, 700))
CLOCK = time.Clock()
display.set_caption('ticktacktoe')

menu_image = image.load("image/menu.bmp")
game3x3_image = image.load("image/menu_3x3.bmp")
game4x4_image = image.load("image/menu_4x4.bmp")
exit_image = image.load("image/exit_menu.bmp")

menu_rect = Rect(0, 0, 600, 600)
game3x3_rect = Rect(100, 200, 400, 100)
game4x4_rect = Rect(100, 300, 400, 100)
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
                        MAIN_SCREEN.blit(game3x3_image, game3x3_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 300 and i.pos[1] <= 400:
                        MAIN_SCREEN.blit(menu_image, menu_rect)
                        MAIN_SCREEN.blit(game4x4_image, game4x4_rect)
                        display.update()
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 400 and i.pos[1] <= 500:
                        pass
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 500 and i.pos[1] <= 600:
                        MAIN_SCREEN.blit(menu_image, menu_rect)
                        MAIN_SCREEN.blit(exit_image, exit_rect)
                        display.update()
                if i.type == MOUSEBUTTONDOWN:
                    if i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 200 and i.pos[1] <= 300:
                        game3x3()
                        flag = False
                        break
                    elif i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 300 and i.pos[1] <= 400:
                        game4x4()
                        flag = False
                        break
                    elif i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 400 and i.pos[1] <= 500:
                        pass
                    elif i.pos[0] >= 100 and i.pos[0] <= 500 and i.pos[1] >= 500 and i.pos[1] <= 600:
                        exit()

if __name__ == "__main__":
    main()