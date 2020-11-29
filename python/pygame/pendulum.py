#! /usr/bin/python
import pygame as pg
from pygame.color import THECOLORS as colors
import math

# https://realpython.com/pygame-a-primer/

size = width, height = 600, 600

pg.init() # calls each pygame module's init() function
screen = pg.display.set_mode(size = size) # creates a window and returns a pg.Surface to draw things on
pg.display.set_caption("Pendulum Simulation") # set title of window

###########################################################################################################
# Variables

# world variables
running = True
fps = 60
clock = pg.time.Clock() # an object for keeping track of time
bgColor = (72, 72, 72)
gravity = -1250

mousePos = (width/2, height/2)
leftDown = False

plotting = True

# Pendulum variables
length = 240
radius = 20
pendColor = colors['firebrick3']
lineWidth = 2

pinX = width/2
pinY = height/2
initialAngle = 179.8
friction = -0.06

a = initialAngle * math.pi/180
aV = 0  # angular velocity

if plotting:
    import matplotlib.pyplot as plt
    t = 0
    time = []
    angle = []
    vel = []

###########################################################################################################
# Logic

def plot():
    fig = plt.figure()
    axTime = fig.add_subplot(211)
    axPhase = fig.add_subplot(212)

    axTime.plot(time, angle, color = 'crimson', label=f'Friction: {friction}')
    axTime.set_title("Pendulum Motion Over Time")
    axTime.set_xlabel("Time (s)")
    axTime.set_ylabel("Angle")
    axTime.grid(True)
    axTime.legend()

    axPhase.plot(angle, vel, color = 'crimson', label=f'Friction: {friction}')
    axPhase.set_title("Pendulum Phase Space")
    axPhase.set_xlabel("Angle")
    axPhase.set_ylabel("Angular Velocity")
    axPhase.grid(True)
    axPhase.legend()

    fig.tight_layout()
    plt.show()
    

def handleEvents():
    global running
    global mousePos
    global leftDown

    for event in pg.event.get(): # pg.event.get() returns a list of pg.event.EventType objects that represent user events
        if event.type == pg.QUIT:
            running = False
            if plotting:
                plot()
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
                if plotting:
                    plot()
        
        elif event.type == pg.MOUSEMOTION:
            mousePos = event.pos
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftDown = True
                mousePos = event.pos
        
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                leftDown = False

        #print(event)
        #print(type(event), dir(event))


prevA = a
prevV = aV
delta = 1/fps
def moveObjects():
    global aV, a, length, prevA, prevV
    if leftDown:
        aA = 0
        aV = 0
        a = math.atan2(mousePos[0] - pinX, mousePos[1] - pinY)
        length = ((pinX - mousePos[0])**2 + ((height-pinY)-(height-mousePos[1]))**2)**0.5
    else:
        aA = gravity/length * math.sin(a) + friction*aV

    aV += aA/fps
    a += aV/fps
    '''
    # these are obtained using a taylor expansion of a(t + h) around a(t)... much more accurate
    a = prevA + delta*prevV + ((delta**2)/2)*(gravity/length)*(math.sin(prevA)) + ((delta**3)/6)*(gravity/length)*prevV*math.cos(prevA)
    aV = prevV + delta*(gravity/length)*math.sin(prevA) + ((delta**2)/2)*(gravity/length)*prevV*math.cos(prevA) + ((delta**3)/6)*(gravity/length)*(-(prevV**2)*math.sin(prevA) + (gravity/length)*math.sin(prevA)*math.cos(prevA))
    prevA = a
    prevV = aV
    '''

def drawObjects():
    x = pinX + length*math.sin(a)
    y = pinY - length*math.cos(a)

    pg.draw.line(screen, (0, 0, 0), (pinX - lineWidth/2, height-pinY), (x - lineWidth/2, height-y), lineWidth)
    pg.draw.circle(screen, (0, 0, 0), (pinX, height-pinY), lineWidth*1.5)
    pg.draw.circle(screen, pendColor, (x, height-y), radius)
    pg.draw.circle(screen, (0, 0, 0), (x, height-y), radius, width=lineWidth)

###########################################################################################################
# Main Loop


while running:
    
    if plotting and not leftDown:
        time.append(t)
        angle.append(a*(180/math.pi))
        vel.append(aV*(180/math.pi))
        t += 1/fps

    handleEvents()
    screen.fill(bgColor) # fill the display surface with bgColor

    moveObjects()
    drawObjects()

    pg.display.flip() # push the contents of screen Surface to the display

    pg.display.set_caption(f'Pendulum Sim ------ (fps = {str(round(clock.get_fps()))})')

    # clock.tick computes time since previous call.  fps argument will make it delay to keep program running at desired frame rate
    #clock.tick(fps)
    clock.tick_busy_loop(fps) # is more accurate than clock.tick


# alternative way of doing it
'''
from threading import Timer

def main():
    if running:
        Timer(1/fps, main).start()
    handleEvents()
    screen.fill(bgColor) # fill the display surface with bgColor

    moveObjects()
    drawObjects()

    pg.display.flip() # push the contents of screen Surface to the display

    pg.display.set_caption(f'Pendulum Sim ------ (fps = {str(round(clock.get_fps()))})')

    clock.tick()
    clock.get_fps()

main()
'''