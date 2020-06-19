#! /usr/bin/python
from tkinter import *
import time

fps = 60

width = 70
height = 100
xPos = 10
yPos = 10
xVel = 40
yVel = -9

gravity = 700

root = Tk()
root.resizable(0,0)
canvas = Canvas(root, width = 600, height = 600, bg = "grey")
canvas.pack()
root.update()

def makeRect(x,y,w,h,c):
    id = canvas.create_rectangle(x,y,x+w,y+h, fill = c)
    root.update()
    canvas.delete(id)
    
    
def moveObjects():
    # must say which variables before reassigning them
    global xPos
    global yPos
    global xVel
    global yVel
    
    xPos += xVel/fps
    yPos += yVel/fps
    yVel += gravity/fps
    
    # check wall collisions
    if xPos <= 0 and xVel < 0 or xPos + width >= canvas.winfo_width() and xVel > 0:
        xVel *= -1
    if yPos <= 0 and yVel < 0 or yPos + height >= canvas.winfo_height() and yVel > 0:
        yVel *= -0.8
        xVel *= 0.9

while True:
    makeRect(xPos, yPos, width,height,"crimson")
    time.sleep(round(1/fps, 2))
    moveObjects()
