#! /usr/bin/python
from tkinter import *
from threading import Timer
import math



leftDown = False
mouseX = 0
mouseY = 0

def mouseDown(eventData):
    global mouseX
    global mouseY
    global leftDown
    
    leftDown = True
    mouseX = eventData.x
    mouseY = canvas.winfo_height() - eventData.y
    
def mouseUp(eventData):
    global leftDown
    
    leftDown = False
    
def mouseDownMotion(eventData):
    global mouseX
    global mouseY
    global leftDown
    
    mouseX = eventData.x
    mouseY = canvas.winfo_height() - eventData.y
    
def keyPress(eventData):
    if eventData.char == 'q':
        root.quit()

def configureWin(data):
    global pinX
    global pinY
    pinX = data.width/2
    pinY = data.height/2


# setup window + canvas
root = Tk()
root.title("Pendulum Simulation")
canvas = Canvas(root, width = 600, height = 600, bg="grey29", bd=0, highlightthickness = 0)
canvas.bind("<ButtonPress-1>", mouseDown) # binds an event handler to the canvas widget, calls mouseDown()
canvas.bind("<ButtonRelease-1>", mouseUp)
canvas.bind("<B1-Motion>", mouseDownMotion) # event is called if mouse is moved while left button is down
canvas.bind("<Configure>", configureWin) # called when window is resized
root.bind("<Key>", keyPress)
canvas.pack(fill = BOTH, expand = 1)
root.update()

# world variables
fps = 60
gravity = -1250

# Pendulum variables
length = 240
radius = 15
lineWidth = 2
pinX = canvas.winfo_width()/2
pinY = canvas.winfo_height()/2
a = 179 # angle to vertical
a *= math.pi/180 # conversion to radians, needed for math
aV = 0 # angular velocity



# two wrapper functions to draw shapes
def drawLine(x1,y1,x2,y2):
    id = canvas.create_line(x1,canvas.winfo_height()-y1,x2,canvas.winfo_height()-y2, width = lineWidth)
def drawCircle(x,y,r,c):
    id = canvas.create_oval(x - r,canvas.winfo_height()-y -r,x+r,canvas.winfo_height()-y+r, fill = c, width = lineWidth)



def drawObjects():
    global length
    
    if(leftDown):
        x = mouseX
        y = mouseY
        endX = mouseX
        endY = mouseY
        length = math.sqrt(math.pow(pinY - mouseY, 2) + math.pow(pinX - mouseX, 2))
    else:
        x = pinX + length*math.sin(a)
        y = pinY - length*math.cos(a)
        endX = pinX + length*math.sin(a)
        endY = pinY - length*math.cos(a)
    
    drawLine(pinX,pinY, endX, endY)
    drawCircle(pinX,pinY,2,"black")
    drawCircle(x,y,radius, "crimson")
    
def moveObjects():
    global aV
    global a
    
    if(leftDown):
        aA = 0
        aV = 0
        
        if mouseX > pinX:
            if mouseY == pinY:
                a = math.pi/2
            else:
                a = math.atan((mouseX-pinX)/(pinY - mouseY))
                if mouseY > pinY:
                    a += math.pi
                    
        elif mouseX == pinX: 
            if mouseY >= pinY:
                a = math.pi
            else:
                a = 0
                
        elif mouseX < pinX:
            if mouseY == pinY:
                a = -math.pi/2
            else:
                a = math.atan((mouseX-pinX)/(pinY - mouseY)) + math.pi
                if mouseY < pinY:
                    a += math.pi
    else:
        aA = gravity/length * math.sin(a)
    
    aV += aA/fps
    a += aV/fps


def mainLoop():
    canvas.delete(ALL)
    drawObjects()
    moveObjects()
    root.after(round(1000/fps), mainLoop)

mainLoop()
root.mainloop()
