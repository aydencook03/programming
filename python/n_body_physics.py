#! /usr/bin/python

from tkinter import *
import random
import math

root = Tk()
root.title("N-Body Physics Simulation")
root.resizable(0,0)
canvas = Canvas(root, width = 600, height = 600, bd = 0, bg = "grey")
def key(data):
    if data.char == 'q':
        root.quit()
root.bind('<Key>', key)
canvas.pack()
root.update()

# simulation variables
fps = 60
gravity_c = 517500 # universe's gravitational constant
bodies = [] # a list of each Body object
running = True
gravityOn = True


class Body:
    def __init__(self, **kwargs):
        self.canvas = kwargs.get('canvas', canvas) #canvas parent that object belongs to
        self.x = kwargs.get('x', self.canvas.winfo_width()/2)
        self.y = kwargs.get('y', self.canvas.winfo_height()/2)
        self.a = kwargs.get('a', 0)
        
        self.xV = kwargs.get('xV', 0) # 0 is the default value
        self.yV = kwargs.get('yV', 0)
        self.aV = kwargs.get('aV', 0)
        
        self.xA = kwargs.get('xA', 0)
        self.yA = kwargs.get('yA', 0)
        self.aA = kwargs.get('aA', 0)
        
        self.mass = kwargs.get('mass', 6)
        self.density = kwargs.get('density', 0.0075)
        self.radius = kwargs.get('radius', math.sqrt(self.mass/(math.pi * self.density)))
        self.color = kwargs.get('color', 'crimson')
        self.lineWidth = kwargs.get('lineWidth', 2)
        
    def move(self):
        self.xV += self.xA/fps
        self.yV += self.yA/fps
        self.aV += self.aA/fps
        self.x += self.xV/fps
        self.y += self.yV/fps
        self.a += self.aV/fps
    
    def draw(self):
        x1 = self.x - self.radius
        y1 = self.canvas.winfo_height() - self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.canvas.winfo_height() - self.y + self.radius
        self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, width = self.lineWidth)
        self.canvas.create_line(self.x, self.canvas.winfo_height() - self.y, self.x + self.radius*math.cos(self.a), self.canvas.winfo_height()-(self.y+self.radius*math.sin(self.a)), width = self.lineWidth)
        
    def gravity(self, otherObject): #calculates gravitational attraction to 'otherObject'
        x1 = self.x
        y1 = self.y
        x2 = otherObject.x
        y2 = otherObject.y
        dist = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2 - y1, 2))
        const = (gravity_c*otherObject.mass)/(math.pow(dist,3))
        xA = const * (x2 - x1)
        yA = const * (y2 -y1)
        return [xA, yA]


def bodyHandle():
    for i in range(len(bodies)):
        bodies[i].draw()
        
        if gravityOn:
            bodies[i].xA = 0
            bodies[i].yA = 0
            for b in range(len(bodies)):
                if i != b:
                    accel = bodies[i].gravity(bodies[b])
                    bodies[i].xA += accel[0]
                    bodies[i].yA += accel[1]
        
        if running:
            bodies[i].move()


bodies.append(Body(x = canvas.winfo_width()/2, y = canvas.winfo_height()/2 + 200, xV = 150, color = 'teal', mass = 1))
bodies.append(Body(x = canvas.winfo_width()/2, y = canvas.winfo_height()/2, xV = -10, mass = 24))

def mainLoop():
    root.after(round(1000/fps), mainLoop)
    canvas.delete(ALL)
    bodyHandle() # draws and moves each Body in bodies[]

mainLoop()
root.mainloop()
