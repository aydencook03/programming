import pygame as pg
import math

pg.init()

width, height = 600, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("2d Wave Equation Simulation")
clock = pg.time.Clock()

running = True
fps = 120


class Point:
    def __init__(self, index, y, yV):
        self.index = index
        self.y = y
        self.yV = yV
        self.yA = 0

    def simulate(self):
        self.yV += self.yA/fps
        self.y += self.yV/fps


# little pieces of string
points = []
pointCount = 400
pointWidth = width/pointCount
stringConstant = 30000
dampening = 0.5

def reset():
    global points
    # initial heights of pieces
    # sine wave
    #points = [Point(i, height/4 * math.sin(i*pointWidth * 2*math.pi/width)) for i in range(pointCount)] # y coordinate of each piece
    # bell curve
    #points = [Point(i, height/6 * math.e**(-((i*pointWidth - width/2)/width/0.1)**2)) for i in range(pointCount)]

    # mix
    points = [Point(i, height/4 * math.sin(i*pointWidth * 2*math.pi/width) + height/8 * math.sin(i*pointWidth * 6*math.pi/width) + height/2 * math.e**(-((i*pointWidth - width/2)/width/0.1)**2), 0) for i in range(pointCount)]

    #points = [Point(i, (height/2 * math.e**(-((i*pointWidth - width/2)/(width*0.1))**2)) + (-height/5 * math.e**(-((pointWidth*i - width/2)/(0.2*width))**2)), 0) for i in range(pointCount)]


def drawString():
    for i in range(pointCount-1):
        pg.draw.line(screen, (0,0,0), (i*pointWidth, height/2 - points[i].y), ((i+1)*pointWidth, height/2 - points[i+1].y), width=2)


def simulateString():
    # boundary conditions
    points[0].y = points[0].yV = points[0].yA = 0
    points[pointCount-1].y = points[pointCount-1].yV = points[pointCount-1].yA = 0

    for i in range(1, pointCount -1):
        leftY = points[i-1].y
        y = points[i].y
        rightY = points[i+1].y

        points[i].yA = (stringConstant/(pointWidth**2)) * (rightY - 2*y + leftY) - dampening*points[i].yV

    for point in points:
        point.simulate()


reset()

while running:
    clock.tick_busy_loop(fps)
    pg.display.set_caption(f'2d Wave Simulation --- fps = {round(clock.get_fps(), 2)}')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_r:
                reset()

    screen.fill((70, 70, 70))

    drawString()
    simulateString()

    pg.display.flip()