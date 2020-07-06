#! /usr/bin/python

from tkinter import Tk, Canvas
from random import randint
from math import sin, cos

root = Tk()
root.title("N-Body Physics Simulation")
canvas = Canvas(root, width = 600, height = 600, bd = 0, bg = "grey27", highlightthickness = 0)

mouseDown = False
nothingGrabbed = True
mouseX = 0
mouseY = 0

def key(data):
    if data.char == 'q':
        root.quit()
    elif data.char == 'r':
        reset()
    elif data.char == 'g':
        global gravityOn
        gravityOn = not gravityOn
        
def buttonPress(data):
    global mouseDown
    global nothingGrabbed
    mouseDown = True
    nothingGrabbed = True
    global mouseX
    global mouseY
    mouseX = data.x
    mouseY = canvas.winfo_height() - data.y

def buttonRelease(data):
    global mouseDown
    global nothingGrabbed
    mouseDown = False
    nothingGrabbed = True
    for i in range(len(bodies)):
        bodies[i].grabbed = False
    
def motion(data):
    if mouseDown:
        global mouseX
        global mouseY
        mouseX = data.x
        mouseY = canvas.winfo_height() - data.y
   
root.bind('<Key>', key)
canvas.bind('<ButtonPress-1>', buttonPress)
canvas.bind('<ButtonRelease-1>', buttonRelease)
canvas.bind('<B1-Motion>', motion)
canvas.pack(fill = 'both', expand = 1)
root.update()

##########################################################################################################
# Simulation Variables

running = True
fps = 120

gravityOn = False
gravity_c = 334000 # universe's gravitational constant

boundaryCollision = True # if true, objects collide with edges of canvas
wallDampen = 1

bodyCollision = True
bodyDampen = 1

falling = False
acceleration = 400


bodies = [] # a list of each Body object
collidingPairs = [] # a list of pairs of colliding bodies

##########################################################################################################
# Body class

class Body:
    id = -1
    def __init__(self, **kwargs):
        # canvas widget that object belongs to, defaults to 'canvas' variable
        self.canvas = kwargs.get('canvas', canvas)
        
        self.x = kwargs.get('x', self.canvas.winfo_width()/2)
        self.y = kwargs.get('y', self.canvas.winfo_height()/2)
        self.a = kwargs.get('a', 0) #angle of rotation in radians
        
        self.xV = kwargs.get('xV', 0) # 0 is the default value
        self.yV = kwargs.get('yV', 0)
        self.aV = kwargs.get('aV', 0)
        
        self.xA = kwargs.get('xA', 0)
        self.yA = kwargs.get('yA', 0)
        self.aA = kwargs.get('aA', 0)
        
        self.grabbed = False
        
        Body.id += 1
        self.id = Body.id
        
        # does object bounce off canvas edge... defaults to value of 'boundaryCollision' variable
        self.edgeBlock = kwargs.get('edgeBlock', boundaryCollision)
        
        # is object influenced by gravity... defaults to value of 'gravityOn' variable
        self.gravity = kwargs.get('gravityOn', gravityOn)

        self.mass = kwargs.get('mass', 6)
        self.density = kwargs.get('density', 0.008)
        pi = 3.141592653589793
        self.radius = kwargs.get('radius', (self.mass/(pi * self.density))**0.5)
        self.color = kwargs.get('color', 'crimson')
        self.lineWidth = kwargs.get('lineWidth', 2)
        
    def move(self):
        self.xV += self.xA/fps
        self.yV += self.yA/fps
        self.aV += self.aA/fps
        self.x += self.xV/fps
        self.y += self.yV/fps
        self.a += self.aV/fps
        
        if self.edgeBlock:
            if self.x + self.radius > self.canvas.winfo_width():
                self.x = self.canvas.winfo_width() - self.radius
                self.xV *= -wallDampen
            elif self.x - self.radius < 0:
                self.x = self.radius
                self.xV *= -wallDampen
            if self.y + self.radius > self.canvas.winfo_height():
                self.y = self.canvas.winfo_height() - self.radius
                self.yV *= -wallDampen
            elif self.y - self.radius < 0:
                self.y = self.radius
                self.yV *= -wallDampen
                
        if self.grabbed:
            self.x = mouseX
            self.y = mouseY
    
    def draw(self):
        x1 = self.x - self.radius
        y1 = self.canvas.winfo_height() - self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.canvas.winfo_height() - self.y + self.radius
        self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, width = self.lineWidth)
        self.canvas.create_line(self.x, self.canvas.winfo_height() - self.y, self.x + self.radius*cos(self.a), self.canvas.winfo_height()-(self.y+self.radius*sin(self.a)), width = self.lineWidth)
        
        #self.canvas.create_text(self.x, self.canvas.winfo_height() - self.y, text=self.id)
        
    def gravityCalc(self, otherObject): #calculates gravitational attraction to 'otherObject'
        x1 = self.x
        y1 = self.y
        x2 = otherObject.x
        y2 = otherObject.y
        distSquare = ((x2-x1)**2 + (y2 - y1)**2)
        const = (gravity_c*otherObject.mass)/((distSquare)**(3/2))
        xA = const * (x2 - x1)
        yA = const * (y2 -y1)
        return [xA, yA]
    
##########################################################################################################
# Vector class

class Vect:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def __add__(self, other): # operator overload for '+' operation
        return Vect(self.i + other.i, self.j + other.j)
    def __sub__(self, other):
        return Vect(self.i - other.i, self.j - other.j)
    def __mul__(self, value):
        return Vect(self.i * value, self.j * value)
    def __truediv__(self, value):
        return Vect(self.i / value, self.j / value)
    def __floordiv__(self, value):
        return Vect(self.i // value, self.j // value)
    def __mod__(self, value):
        return Vect(self.i % value, self.j % value)
    def __pow__(self, value):
        return Vect(self.i**value, self.j**value)
    
    @property # function acts as an attribute instead of called function
    def mag(self): # returns the magnitude
        return ((self.i**2) + (self.j**2))**0.5
    
    @property
    def norm(self): # returns the normal vector
        return Vect(self.i/self.mag, self.j/self.mag)
    
    def dot(self, other): # dot product
        return ((self.i * other.i) + (self.j * other.j))
    
    def cross(self, other): # returns the magnitude of the cross product vector
        return ((self.i * other.j) - (self.j * other.i))
    
    def draw(self, fromX, fromY, **kwargs):
        # what canvas does object belong to, defaults to 'canvas' variable
        self.canvas = kwargs.get('canvas', canvas)
        self.color = kwargs.get('color', 'black')
        self.width = kwargs.get('width', 2)
        
        self.canvas.create_line(fromX, self.canvas.winfo_height() - fromY, fromX + self.i, self.canvas.winfo_height() - (fromY + self.j), width = self.width, fill = self.color)
        
##########################################################################################################
# Simulation Code

def bodyHandle():
    global nothingGrabbed
    for i in range(len(bodies)):
        
        if mouseDown and nothingGrabbed:
            if abs((mouseX - bodies[i].x)**2 + (mouseY - bodies[i].y)**2) <= bodies[i].radius ** 2:
                bodies[i].grabbed = True
                nothingGrabbed = False
                
        bodies[i].draw()
            
    
        if running:
            if falling:
                bodies[i].yV -= acceleration/fps
            bodies[i].move()
        
        bodies[i].xA = 0
        bodies[i].yA = 0
        collidingPairs.clear()
        if gravityOn or bodyCollision:
            for b in range(len(bodies)):
                if i != b:
                    if bodyCollision:
                        x1 = bodies[i].x
                        y1 = bodies[i].y
                        r1 = bodies[i].radius
                        x2 = bodies[b].x
                        y2 = bodies[b].y
                        r2 = bodies[b].radius
                        dist = Vect(x2-x1, y2-y1)
                        if dist.mag <= r1 + r2: # handles static collision
                            overlap = (r1 + r2) - dist.mag
                            bodies[i].x -= overlap/2 * dist.norm.i
                            bodies[i].y -= overlap/2 * dist.norm.j
                            bodies[b].x += overlap/2 * dist.norm.i
                            bodies[b].y += overlap/2 * dist.norm.j
                            collidingPairs.append([bodies[i], bodies[b]])
                            
                    if gravityOn:
                        if bodies[i].gravity:
                            accel = bodies[i].gravityCalc(bodies[b])
                            bodies[i].xA += accel[0]
                            bodies[i].yA += accel[1]
                            
        for i in range(len(collidingPairs)):
            x1 = collidingPairs[i][0].x
            y1 = collidingPairs[i][0].y
            r1 = collidingPairs[i][0].radius
            x2 = collidingPairs[i][1].x
            y2 = collidingPairs[i][1].y
            r2 = collidingPairs[i][1].radius
            dist = Vect(x2-x1, y2-y1)
            m1 = collidingPairs[i][0].mass
            m2 = collidingPairs[i][1].mass
            
            norm = Vect(-dist.j, dist.i).norm # along 'wall' of collision
            perp = dist.norm # perpendicular to radius
            
            vel1 = Vect(collidingPairs[i][0].xV, collidingPairs[i][0].yV)
            vel2 = Vect(collidingPairs[i][1].xV, collidingPairs[i][1].yV)
            
            nV1Perp = (vel1.dot(perp))*(m1-m2)/(m1+m2) + (vel2.dot(perp))*(2*m2)/(m1+m2)
            nV2Perp = (vel1.dot(perp))*(2*m1)/(m1+m2) + (vel2.dot(perp))*(m2-m1)/(m1+m2)
            
            collidingPairs[i][0].xV = vel1.dot(norm)*norm.i + nV1Perp*perp.i * bodyDampen
            collidingPairs[i][0].yV = vel1.dot(norm)*norm.j + nV1Perp*perp.j * bodyDampen
                            
            collidingPairs[i][1].xV = vel2.dot(norm)*norm.i + nV2Perp*perp.i * bodyDampen
            collidingPairs[i][1].yV = vel2.dot(norm)*norm.j + nV2Perp*perp.j * bodyDampen
                    


def reset():
    canvas.delete('all')
    bodies.clear()
    Body.id = -1
    collidingPairs.clear()
    
    for i in range(50):
        mass = randint(1, 24)
        x = randint(0, canvas.winfo_width())
        y = randint(0, canvas.winfo_height())
        bounds = 200
        xV = randint(-bounds, bounds)
        yV = randint(-bounds, bounds)
        bodies.append(Body(x = x, y = y, xV = xV, yV = yV, mass = mass))
    '''
    bodies.append(Body(x = canvas.winfo_width()/2, y = canvas.winfo_height()/2, mass = 24, xV = -10.83))
    bodies.append(Body(x = canvas.winfo_width()/2, y = canvas.winfo_height()/2 + 150, mass = 1, xV = 260, color = 'teal'))
    '''
    
def mainLoop():
    root.after(round(1000/fps), mainLoop)
    canvas.delete('all')
    bodyHandle() # draws and moves each Body in bodies[]

reset()
mainLoop()
root.mainloop()
