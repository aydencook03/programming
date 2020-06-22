#! /usr/bin/python
from tkinter import *
from time import sleep
import math

# setup window + canvas
root = Tk()
root.title("Pendulum Simulation")
root.resizable(0,0)
canvas = Canvas(root, width = 600, height = 600, bg="grey", bd=0)
canvas.pack()
root.update()

# world variables
fps = 60
gravity = -1250

# Pendulum variables
length = 240
radius = 15
pinX = canvas.winfo_width()/2
pinY = canvas.winfo_height()/2
a = 179.9 # angle to vertical
a *= math.pi/180 # conversion to radians, needed for math
aV = 0 # angular velocity



# two wrapper functions to draw shapes
def drawLine(x1,y1,x2,y2):
    id = canvas.create_line(x1,canvas.winfo_height()-y1,x2,canvas.winfo_height()-y2, width = 2)
def drawCircle(x,y,r,c):
    id = canvas.create_oval(x - r,canvas.winfo_height()-y -r,x+r,canvas.winfo_height()-y+r, fill = c, width = 2)



def drawObjects():
    x = pinX + length*math.sin(a)
    y = pinY - length*math.cos(a)
    drawLine(pinX,pinY, pinX + length*math.sin(a), pinY - length*math.cos(a))
    drawCircle(pinX,pinY,2,"black")
    drawCircle(x,y,radius, "crimson")
    
def moveObjects():
    global aV
    global a
    
    aA = gravity/length * math.sin(a)
    aV += aA/fps
    a += aV/fps

while True: # main loop
    drawObjects()
    root.update()
    sleep(round(1/fps, 2))
    canvas.delete(ALL)
    moveObjects()
