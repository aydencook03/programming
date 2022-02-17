#! /usr/bin/python
######################################################################################
# SETUP

import pygame as pg
import numpy as np


running = False
simulating = False
recording = False
FPS = 24
simFPS = 120
frameCount = 0
clock = pg.time.Clock()

res = (256, 256)

bgColor = (72, 72, 72)
crimson = (220, 20, 60)
green = (119, 221, 119)

pg.init()
screen = pg.display.set_mode(res)
pg.display.set_caption("Simulation")

pixels = pg.PixelArray(screen)

mesh = np.array(pixels)

waveVelocity = (res[0]/3)/simFPS

######################################################################################
# LOGIC

def restart():
    global running
    global simulating
    resetMesh()
    running = True
    simulating = True
    loop()

def resetMesh():
    xRange = (-4, 4)
    yRange = (-4, 4)

def paintScreen():
    pixels[:][:] = crimson

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
        clock.tick_busy_loop(FPS)

######################################################################################

restart()