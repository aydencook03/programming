import pygame as pg
import numpy as np

clock = pg.time.Clock()
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("3d Test")
running = True
fps = 60

bg = (75, 75, 75)
pointSize = 4
pointColor = (0, 0, 0)
lineWidth = 2
lineColor = (153, 0, 0)

class Point:
    def __init__(self, coords): #coords should be list/tuple of length 3
        self.coords = np.array([ coords[0],
                                 coords[1],
                                 coords[2] ])
    
    def draw(self):
        pg.draw.circle(screen, pointColor, (self.coords[0] + width/2, height/2 - self.coords[1]), pointSize)

class Transformation:
    def __init__(self, ihat_land, jhat_land, khat_land): #should be 3 lists/tuples of length 3
        self.matrix = np.array([[ihat_land[0], jhat_land[0], khat_land[0]], 
                                [ihat_land[1], jhat_land[1], khat_land[1]],
                                [ihat_land[2], jhat_land[2], khat_land[2]]])

    def transform(self, point):
        return Point(self.matrix.dot(point.coords))

size = 200

points = [
    Point((-size/2, -size/2, -size/2)),
    Point((-size/2, size/2, -size/2)),
    Point((size/2, size/2, -size/2)),
    Point((size/2, -size/2, -size/2)),

    Point((-size/2, -size/2, size/2)),
    Point((-size/2, size/2, size/2)),
    Point((size/2, size/2, size/2)),
    Point((size/2, -size/2, size/2))
]

vel = 0.006
rotate = Transformation( (np.cos(vel), np.sin(vel), 0) , (np.cos(vel + np.pi/2), np.sin(vel + np.pi/2), 0), (0, 0, 1))
rotate2 = Transformation( (1, 0, 0), (0, np.sin(vel+np.pi/2), np.cos(vel+np.pi/2)), (0, np.sin(vel), np.cos(vel)) )


def draw():
    for i in range(0, 3):
        pg.draw.line(screen, lineColor, (points[i].coords[0]+width/2, height/2 - points[i].coords[1]), (points[i+1].coords[0]+width/2, height/2 - points[i+1].coords[1]), lineWidth)
    pg.draw.line(screen, lineColor, (points[3].coords[0]+width/2, height/2 - points[3].coords[1]), (points[0].coords[0]+width/2, height/2 - points[0].coords[1]), lineWidth)

    for i in range(4, 7):
        pg.draw.line(screen, lineColor, (points[i].coords[0]+width/2, height/2 - points[i].coords[1]), (points[i+1].coords[0]+width/2, height/2 - points[i+1].coords[1]), lineWidth)
    pg.draw.line(screen, lineColor, (points[7].coords[0]+width/2, height/2 - points[7].coords[1]), (points[4].coords[0]+width/2, height/2 - points[4].coords[1]), lineWidth)

    for i in range(4):
        pg.draw.line(screen, lineColor, (points[i].coords[0]+width/2, height/2 - points[i].coords[1]), (points[i+4].coords[0]+width/2, height/2 - points[i+4].coords[1]), lineWidth)

    for i in range(len(points)):
        points[i].draw()
        points[i] = rotate.transform(points[i])
        points[i] = rotate2.transform(points[i])


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

    screen.fill(bg)

    draw()

    pg.display.flip()
    clock.tick_busy_loop(fps)