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


# setup window + canvas
root = Tk()
root.title("Pendulum Simulation")
root.resizable(0,0)
canvas = Canvas(root, width = 600, height = 600, bg="grey", bd=0)
canvas.bind("<ButtonPress-1>", mouseDown) # binds an event handler to the canvas widget, calls mouseDown()
canvas.bind("<ButtonRelease-1>", mouseUp)
canvas.bind("<B1-Motion>", mouseDownMotion) # event is called if mouse is moved while left button is down
root.bind("<Key>", keyPress)
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
a = 179 # angle to vertical
a *= math.pi/180 # conversion to radians, needed for math
aV = 0 # angular velocity



# two wrapper functions to draw shapes
def drawLine(x1,y1,x2,y2):
    id = canvas.create_line(x1,canvas.winfo_height()-y1,x2,canvas.winfo_height()-y2, width = 2)
def drawCircle(x,y,r,c):
    id = canvas.create_oval(x - r,canvas.winfo_height()-y -r,x+r,canvas.winfo_height()-y+r, fill = c, width = 2)



def drawObjects():
    global length
    
    if(leftDown):
        x = mouseX
        y = mouseY
        endX = mouseX
        endY = mouseY
        length = math.sqrt(math.pow(canvas.winfo_height()/2 - mouseY, 2) + math.pow(canvas.winfo_width()/2 - mouseX, 2))
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
        
        if mouseX > canvas.winfo_width()/2:
            if mouseY == canvas.winfo_height()/2:
                a = math.pi/2
            else:
                a = math.atan((mouseX-canvas.winfo_width()/2)/(canvas.winfo_height()/2 - mouseY))
                if mouseY > canvas.winfo_height()/2:
                    a += math.pi
                    
        elif mouseX == canvas.winfo_width()/2: 
            if mouseY >= canvas.winfo_height()/2:
                a = math.pi
            else:
                a = 0
                
        elif mouseX < canvas.winfo_width()/2:
            if mouseY == canvas.winfo_height()/2:
                a = -math.pi/2
            else:
                a = math.atan((mouseX-canvas.winfo_width()/2)/(canvas.winfo_height()/2 - mouseY)) + math.pi
                if mouseY < canvas.winfo_height()/2:
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
