#! /usr/bin/python

from tkinter import Tk, Canvas
from random import randint

root = Tk()
root.title("BrickBreaker")
canvas = Canvas(root, width = 600, height = 600, highlightthickness = 0, bg = "grey27", bd = 0)

def keyPress(data):
    if data.char == 'q':
        root.quit()
    elif data.char == 'r':
        reset()
        
mouseX = canvas.winfo_width()
mouseY = canvas.winfo_height()

def motion(data):
    global mouseX, mouseY
    
    mouseX = data.x
    mouseY = data.y
    
root.bind('<Key>', keyPress)
root.bind('<Motion>', motion)
canvas.pack(fill = 'both', expand = 1)
root.update()


fps = 60

colCount = 7
rowCount = 10
brickWidth = canvas.winfo_width()/colCount
brickHeight = canvas.winfo_height()/rowCount
brickC = 'teal'

ballRadius = 11
ballC = 'crimson'
lineWidth = 2

paddleW = 80
paddleH = 15
padding = paddleH
paddleC = 'white'
paddleX = canvas.winfo_width()
paddleY = canvas.winfo_height() - padding - paddleH


bricks = []

class Brick:
    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.color = kwargs.get('color', brickC)
        
    def draw(self):
        canvas.create_rectangle(self.x, self.y, self.x + brickWidth, self.y + brickHeight, fill = self.color, width = lineWidth)
        

class Ball:
    cWidth = canvas.winfo_width()
    cHeight = canvas.winfo_height()
    
    def  __init__(self, **kwargs):
        self.x = kwargs.get('x', Ball.cWidth/2)
        self.y = kwargs.get('y', Ball.cHeight/2)
        self.xV = kwargs.get('xV', 0)
        self.yV = kwargs.get('yV', 0)
        self.color = kwargs.get('color', ballC)
        self.r = kwargs.get('r', ballRadius)
        
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width = lineWidth)
        
    def move(self):
        global fps
        
        if self.x - self.r < 0:
            self.x = self.r
            self.xV *= -1
        elif self.x + self.r > Ball.cWidth:
            self.x = Ball.cWidth - self.r
            self.xV *= -1
        if self.y - self.r < 0:
            self.y = self.r
            self.yV *= -1
        elif self.y - self.r > Ball.cHeight:
            reset()
        
        self.x += self.xV/fps
        self.y += self.yV/fps
        


ball = None

def reset():
    global ball
    
    bricks.clear()
    
    lower = 100
    upper = 250
    xV = 0
    yV = 0
    while abs(xV) < lower:
        xV = randint(-upper, upper)
    while abs(yV) < lower:
        yV = randint(-upper, -lower)
    
    ball = Ball(xV = xV, yV = yV)

def drawBricks():
    for i in range(len(bricks)):
        bricks[i].draw()


def main():
    global paddleX, paddleY
    root.after(round(1000/fps), main)
    canvas.delete('all')
    drawBricks()
    ball.draw()
    ball.move()
    paddleX = mouseX - paddleW/2
    canvas.create_rectangle(paddleX, paddleY, paddleX + paddleW, paddleY + paddleH, fill = paddleC, width = lineWidth)

reset()
main()
root.mainloop()
