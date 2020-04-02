from pygame import *

def drawX(md, square):
    if square == 1:
        draw.line(md, (0, 200, 64), [10, 10], [190, 190], 9)
        draw.line(md, (0, 200, 64), [190, 10], [10, 190], 9)
        display.update()
    elif square == 2:
        draw.line(md, (0, 200, 64), [210, 10], [390, 190], 9)
        draw.line(md, (0, 200, 64), [390, 10], [210, 190], 9)
        display.update()
    elif square == 3:
        draw.line(md, (0, 200, 64), [410, 10], [590, 190], 9)
        draw.line(md, (0, 200, 64), [590, 10], [410, 190], 9)
        display.update()
    elif square == 4:
        draw.line(md, (0, 200, 64), [10, 210], [190, 390], 9)
        draw.line(md, (0, 200, 64), [190, 210], [10, 390], 9)
        display.update()
    elif square == 5:
        draw.line(md, (0, 200, 64), [210, 210], [390, 390], 9)
        draw.line(md, (0, 200, 64), [390, 210], [210, 390], 9)
        display.update()
    elif square == 6:
        draw.line(md, (0, 200, 64), [410, 210], [590, 390], 9)
        draw.line(md, (0, 200, 64), [590, 210], [410, 390], 9)
        display.update()
    if square == 7:
        draw.line(md, (0, 200, 64), [10, 410], [190, 590], 9)
        draw.line(md, (0, 200, 64), [190, 410], [10, 590], 9)
        display.update()
    if square == 8:
        draw.line(md, (0, 200, 64), [210, 410], [390, 590], 9)
        draw.line(md, (0, 200, 64), [390, 410], [210, 590], 9)
        display.update()
    if square == 9:
        draw.line(md, (0, 200, 64), [410, 410], [590, 590], 9)
        draw.line(md, (0, 200, 64), [590, 410], [410, 590], 9)
        display.update()

def drawY(md, square):
    if square == 1:
        draw.circle(md, (64, 128, 255), (100, 100), 90, 8)
        display.update()
    elif square == 2:
        draw.circle(md, (64, 128, 255), (300, 100), 90, 8)
        display.update()
    elif square == 3:
        draw.circle(md, (64, 128, 255), (500, 100), 90, 8)
        display.update()
    elif square == 4:
        draw.circle(md, (64, 128, 255), (100, 300), 90, 8)
        display.update()
    elif square == 5:
        draw.circle(md, (64, 128, 255), (300, 300), 90, 8)
        display.update()
    elif square == 6:
        draw.circle(md, (64, 128, 255), (500, 300), 90, 8)
        display.update()
    elif square == 7:
        draw.circle(md, (64, 128, 255), (100, 500), 90, 8)
        display.update()
    elif square == 8:
        draw.circle(md, (64, 128, 255), (300, 500), 90, 8)
        display.update()
    elif square == 9:
        draw.circle(md, (64, 128, 255), (500, 500), 90, 8)
        display.update()
def main():
    init()

    fps = 60
    clock = time.Clock()

    main_display = display.set_mode((600, 600))
    main_display.fill((255,255,255))
    display.set_caption('X - O')
    draw.line(main_display, (0, 0, 0), [0, 200], [600, 200], 10)
    draw.line(main_display, (0, 0, 0), [0, 400], [600, 400], 10)
    draw.line(main_display, (0, 0, 0), [200, 0], [200, 600], 10)
    draw.line(main_display, (0, 0, 0), [400, 0], [400, 600], 10)
    
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
                        drawX(main_display, 1)
                    else:
                        queue = 'x'
                        drawY(main_display, 1)
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 2)
                    else:
                        queue = 'x'
                        drawY(main_display, 2)
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 0 and i.pos[1] <= 200:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 3)
                    else:
                        queue = 'x'
                        drawY(main_display, 3)
                elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 4)
                    else:
                        queue = 'x'
                        drawY(main_display, 4)
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 5)
                    else:
                        queue = 'x'
                        drawY(main_display, 5)
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 200 and i.pos[1] <= 400:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 6)
                    else:
                        queue = 'x'
                        drawY(main_display, 6)
                elif i.pos[0] >= 0 and i.pos[0] <= 200 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 7)
                    else:
                        queue = 'x'
                        drawY(main_display, 7)
                elif i.pos[0] >= 200 and i.pos[0] <= 400 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 8)
                    else:
                        queue = 'x'
                        drawY(main_display, 8)
                elif i.pos[0] >= 400 and i.pos[0] <= 600 and i.pos[1] >= 400 and i.pos[1] <= 600:
                    if queue == 'x':
                        queue = 'y'
                        drawX(main_display, 9)
                    else:
                        queue = 'x'
                        drawY(main_display, 9)
 
if __name__ == "__main__":
    main()