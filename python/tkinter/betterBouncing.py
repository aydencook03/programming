#! /usr/bin/python
from tkinter import *
import time

fps = 60

width = 70
height = 100
xPos = 10
yPos = 10
xVel = 120
yVel = -9
bouncing = True

gravity = 700

root = Tk()
root.resizable(0,0)
root.title("Bouncing Block")
canvas = Canvas(root, width = 600, height = 600, bg = "grey")
canvas.pack()
root.update()

def makeRect(x,y,w,h,c):
    canvas.create_rectangle(x,y,x+w,y+h, fill = c)
    
def moveObjects():
    # must say which variables before reassigning them
    global xPos
    global yPos
    global xVel
    global yVel
    global bouncing
    
    xPos += xVel/fps
    if bouncing:
        yPos += yVel/fps
        yVel += gravity/fps
    
    # check wall collisions
    if xPos + width > canvas.winfo_width() and xVel > 0:
        xVel *= -0.8
        xPos = canvas.winfo_width() - width
    elif xPos < 0 and xVel < 0:
        xVel *= -0.8
        xPos = 0
    if yPos + height > canvas.winfo_height() and yVel > 0 and bouncing:
        if abs(yVel) < 100:
            bouncing = False
            yVel = 0
            yPos = canvas.winfo_height() - height
        else:
            yPos = canvas.winfo_height() - height
            yVel *= -0.8
            xVel *= 0.85
    elif not bouncing:
        xVel *= 0.95
    elif yPos < 0 and yVel < 0:
        yVel *= -0.8
        yPos = 0

while True:
    makeRect(xPos, yPos, width,height,"crimson")
    root.update()
    time.sleep(round(1/fps, 2))
    moveObjects()
    canvas.delete(ALL)
