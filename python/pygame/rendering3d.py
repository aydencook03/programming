#! /usr/bin/python
import pygame as pg

width, height = 600, 600
pg.display.set_caption("Rendering 3d")
clock = pg.time.Clock()

running = True
fps = 60

backColor = (74, 74, 74) #color of background


class Scene:
    def __init__(self, size):
        self.size = size

class Camera:
    def __init__(self, coords, angle, fieldOfView):
        self.coords = coords
        self.angle = angle
        self.fieldOfView = fieldOfView

class Point:
    def __init__(self, coords, radius, color=(0,0,0)):
        self.coords = coords
        self.radius = radius
        self.color = color

class Line:
    def __init__(self, startCoords, endCoords, width, color=(0, 0, 0)):
        self.startCoords = startCoords
        self.endCoords = endCoords

        self.width = width
        self.color = color

class Cube:
    def __init__(self, coords, sideLength, angle=(0,0,0), vertices=True, edges=True, verticeColor=(0,0,0), edgeColor=(97,0,0)):
        '''
        coords: a length 3 tuple/list.  Right Handed Coordinate System with (0,0,0) being furthest into the screen at the bottom right.  Left is positive x, up is positive z, out of the screen is positive y.  Each axis on a range of [0, 1]

        sideLength:  float on range [0, 1].  With sideLength=1 being the width of the entire scene
        '''
        # cube information
        self.coords = coords
        self.sideLength = sideLength

        # cube looks
        self.vertices = vertices
        self.edges = edges
        self.verticeColor = verticeColor
        self.edgeColor = edgeColor


def events():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

def mainLoop():
    while running:
        clock.tick(fps)
        screen.fill(backColor)
        events()

        pg.display.flip()
    
if __name__ == '__main__':
    global screen
    pg.init()
    screen = pg.display.set_mode((width, height))
    mainLoop()