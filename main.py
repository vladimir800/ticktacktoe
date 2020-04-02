from pygame import *

def main():
    init()

    fps = 30
    clock = time.Clock()

    main_display = display.set_mode((600, 600))
    main_display.fill((255,255,255))
    display.set_caption('X - O')
    draw.line(main_display, (0, 0, 0), [0, 200], [600, 200], 9)
    draw.line(main_display, (0, 0, 0), [0, 400], [600, 400], 9)
    draw.line(main_display, (0, 0, 0), [200, 0], [200, 600], 9)
    draw.line(main_display, (0, 0, 0), [400, 0], [400, 600], 9)
    square1 = Rect(5, 5, 190, 190)
    square2 = Rect(205, 5 , 190, 190)
    square3 = Rect(405, 5, 190, 190)
    square4 = Rect(5, 205, 190, 190)
    square5 = Rect(205, 205, 190, 190)
    square6 = Rect(405, 205, 190, 190)
    square7 = Rect(5, 405, 190, 190)
    square8 = Rect(205, 405, 190, 190)
    square9 = Rect(405, 405, 190, 190)
    draw_x = image.load("image/x.bmp")
    draw_o = image.load("image/o.bmp")
    display.update()
    
    queue = 'x'
    
    while True:
        clock.tick(fps)
        for i in event.get():
            if i.type == QUIT:
                return
            if i.type == MOUSEBUTTONDOWN:
                if i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square1)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square1)
                        display.update()
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square2)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square2)
                        display.update()
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square3)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square3)
                        display.update()
                elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square4)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square4)
                        display.update()
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square5)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square5)
                        display.update()
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square6)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square6)
                        display.update()
                elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square7)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square7)
                        display.update()
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square8)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square8)
                        display.update()
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if queue == 'x':
                        queue = 'y'
                        main_display.blit(draw_x, square9)
                        display.update()
                    else:
                        queue = 'x'
                        main_display.blit(draw_o, square9)
                        display.update()
 
if __name__ == "__main__":
    main()