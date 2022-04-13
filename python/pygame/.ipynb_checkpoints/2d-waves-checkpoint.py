#! /usr/bin/python
######################################################################################
# SETUP

import pygame as pg
import math


running = False
simulating = False
recording = False
FPS = 24
simFPS = 30
clock = pg.time.Clock()

res = (256, 256)

bgColor = (72, 72, 72)
crimson = (220, 20, 60)
forestGreen = (0,110,51)
teal = (0,124,128)

peakColor = crimson
crestColor = teal
peakHeight = 0

pg.init()
screen = pg.display.set_mode(res)
pg.display.set_caption("Simulation")

pixels = pg.PixelArray(screen)

mesh = [[[0, 0, 0] for y in range(res[1])] for x in range(res[0])] # mesh[x][y][height, vel, accel]

waveVelocity = res[0]/3

######################################################################################
# INITIALIZE

def restart():
    global running
    global simulating
    resetMesh()
    running = True
    simulating = True
    loop()

def resetMesh():
    global peakHeight
    peakHeight = -math.inf

    xRange = (-4, 4)
    yRange = (-4, 4)
    shape = lambda x,y: math.exp(-(x**2 + y**2))

    for i in range(res[0]):
        for j in range(res[1]):
            x = xRange[0] + i*(xRange[1] - xRange[0])/res[0]
            y = yRange[0] + j*(yRange[1] - yRange[0])/res[1]

            mesh[i][j] = shape(x, y)
            peakHeight = mesh[i][j] if mesh[i][j] > peakHeight else peakHeight

######################################################################################
# GRAPHICS

def interpolateColor(height):
    return (255, 255, 255)

def paintScreen():
    for x in range(res[0]):
        for y in range(res[1]):
            colors = interpolateColor(mesh[x][y])
            r = colors[0]
            g = colors[1]
            b = colors[2]
            pixels[x][-1 - y] = (r, g, b)

######################################################################################
# MATH

def firstDiff(mesh, x, y, dimension):
    value = 0
    if dimension == 0:
        value = (mesh[x+1][y] - mesh[x-1][y])/2
    else:
        value = (mesh[x][y+1] - mesh[x][y-1])/2
    return value

def secondDiff(mesh, x, y, dimension):
    value = 0
    if dimension == 0:
        value = mesh[x+1][y] + mesh[x-1][y] - 2*mesh[x][y]
    else:
        value = mesh[x][y+1] + mesh[x][y-1] - 2*mesh[x][y]
    return value

def laplace(mesh, x, y):
    return secondDiff(mesh, x, y, 0) + secondDiff(mesh, x, y, 1)

######################################################################################
# LOOP

def handleEvents():
    global running

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

def loop():
    while running:
        handleEvents()

        screen.fill(bgColor)
        paintScreen()

        pg.display.flip()
        pg.display.set_caption(f'Simulation ------ (fps = {str(round(clock.get_fps()))})')
        clock.tick_busy_loop(simFPS)

######################################################################################
# START LOOP

restart()