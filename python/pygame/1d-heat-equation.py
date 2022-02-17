import pygame as pg
import math

pg.init()
width,height = 600, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Head Rods")
clock = pg.time.Clock()

running = True
fps = 60


def events():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

elementCount = width//5
elementWidth = width/elementCount

timeStep = 1/fps

leftRodTemp = 200
rightRodTemp = -200

heatConstant = 250

elements = []

# initial distrobution of temperature
for i in range(elementCount):
    elements.append(height/3 * 2.718**(-(6*(i/elementCount) - 3)**2) * math.cos((6*(i/elementCount) - 3)*3))
'''
for i in range(elementCount//2):
    elements.append(leftRodTemp)
for i in range(elementCount//2, elementCount):
    elements.append(rightRodTemp)
'''
'''
for i in range(elementCount):
    elements[i] = height/3 * math.sin(2*math.pi/width * i*elementWidth)
'''


def draw():
    for i in range(elementCount-1):
        pg.draw.line(screen, (0,0,0), (i*elementWidth, height/2 - elements[i]), ((i+1)*elementWidth, height/2 - elements[i+1]), 2)

def simulate():
    deltaT = [0 for n in range(elementCount)]

    for i in range(1, elementCount-1):
        deltaT[i] = ((heatConstant*timeStep)/(elementWidth**2))*(elements[i+1] - 2*elements[i] + elements[i-1])

    for i in range(elementCount):
        elements[i] += deltaT[i]

while running:
    clock.tick_busy_loop(fps)
    events()
    screen.fill((70, 70, 70))
    draw()
    simulate()
    pg.display.flip()