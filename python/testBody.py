#! /usr/bin/python

from tkinter import *
import random
import math

root = Tk()
root.title("N-Body Physics Simulation")
root.resizable(0,0)
canvas = Canvas(root, width = 600, height = 600, bd = 0, bg = "grey")
canvas.pack()
root.update()

# simulation variables
fps = 60
gravity_c = 517500 # universe's gravitational constant
bodies = [] # a list of each Body object
running = True


class Body:
    def __init__(self, **kwargs):
        self.canvas = kwargs.get('canvas', canvas) # the parent canvas that the object belongs to
        self.x = kwargs.get('x', self.canvas.winfo_width()/2)
        self.y = kwargs.get('y', self.canvas.winfo_height()/2)
        self.a = kwargs.get('a', 0)
        
        self.xV = kwargs.get('xV', 0) # 0 is the default value
        self.yV = kwargs.get('yV', 0)
        self.aV = kwargs.get('aV', 0)
        
        self.xA = kwargs.get('xA', 0)
        self.yA = kwargs.get('yA', 0)
        self.aA = kwargs.get('aA', 0)
        
        self.radius = kwargs.get('radius', 10)
        self.mass = kwargs.get('mass', 6)
        self.color = kwargs.get('color', 'crimson')
        
        x1 = self.x - self.radius
        y1 = self.canvas.winfo_height() - self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.canvas.winfo_height() - self.y + self.radius
        self.lineWidth = 2
        
        self.id = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, width = self.lineWidth)
        self.id2 = self.canvas.create_line(self.x, self.canvas.winfo_height() - self.y, self.x + self.radius*math.cos(self.a), self.canvas.winfo_height()-(self.y+self.radius*math.sin(self.a)), width = self.lineWidth)
        
    def move(self):
        self.xV += self.xA/fps
        self.yV += self.yA/fps
        self.aV += self.aA/fps
        self.canvas.move(self.id, self.xV/fps, -self.yV/fps)
        self.x = self.canvas.coords(self.id)[0] + self.radius
        self.y = self.canvas.winfo_height() - self.canvas.coords(self.id)[1] - self.radius
        self.a += self.aV/fps
        self.canvas.coords(self.id2, self.x, canvas.winfo_height() - self.y, self.x + self.radius*math.cos(self.a), self.canvas.winfo_height()-(self.y+self.radius*math.sin(self.a)))
        

def bodyHandle():
    for i in range(len(bodies)):
        if running:
            bodies[i].move()
        
        
bodies.append(Body(x = 20, y = 20, aA = 4, xV = 8, yV = 9))
bodies.append(Body(xV = 250, yV = -80, aV = -4, color = 'teal'))


def mainLoop():
    bodyHandle() # draws and moves each Body in bodies[]
    root.after(round(1000/fps), mainLoop)

mainLoop()
root.mainloop()
