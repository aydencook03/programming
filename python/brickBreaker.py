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
    
    if testing:
        ball.x = mouseX
        ball.y = mouseY
        ball.xV = 50
        ball.yV = -50
    
root.bind('<Key>', keyPress)
root.bind('<Motion>', motion)
canvas.pack(fill = 'both', expand = 1)
root.update()


fps = 60

testing = False

colCount = 7
rowCount = 9
emptyRowCount = 2
brickWidth = canvas.winfo_width()/colCount
brickHeight = canvas.winfo_height()/2.2/rowCount
brickC = 'teal'

ballRadius = 4
ballC = 'crimson'
lineWidth = 2

paddleW = 80
paddleH = 15
padding = paddleH*1.5
paddleC = 'white'
paddleX = canvas.winfo_width()
paddleY = canvas.winfo_height() - padding - paddleH


brick = []


class Ball:
    def  __init__(self, **kwargs):
        self.x = kwargs.get('x', canvas.winfo_width()/2)
        self.y = kwargs.get('y', canvas.winfo_height()/2)
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
        elif self.x + self.r > canvas.winfo_width():
            self.x = canvas.winfo_width() - self.r
            self.xV *= -1
        if self.y - self.r < 0:
            self.y = self.r
            self.yV *= -1
        elif self.y - self.r > canvas.winfo_height():
            reset()
            
            
        if self.x + self.r >= paddleX and self.x - self.r <= paddleX + paddleW and self.y + self.r > paddleY and self.y + self.r <= paddleY + paddleW/2:
            self.y = paddleY - self.r
            self.yV *= -1
            val = paddleW/11
            self.xV = (self.x - (paddleX + paddleW/2)) * val
        
        self.x += self.xV/fps
        self.y += self.yV/fps
        
    def reset(self):
        global ball
        
        lower = 10
        upper = 300
        xV = 0
        yV = 0
        
        while abs(xV) < lower:
            xV = randint(-upper, upper)
        yV = -upper
        
        self.xV = xV
        self.yV = yV
        self.x = canvas.winfo_width()/2
        self.y = paddleY - paddleH
        


def reset():
    global brick
    
    brick.clear()
    brick = [False] * (rowCount * colCount)
    ball.reset()
    
    for col in range(colCount):
        for row in range(rowCount):
            index = colCount*row + col
            brick[index] = True
    for i in range(emptyRowCount * colCount):
        brick[i] = False
  
def paddleHandle():
    global paddleX
    
    paddleX = mouseX - paddleW/2
    if paddleX < 0:
        paddleX = 0
    elif paddleX > canvas.winfo_width() - paddleW:
        paddleX = canvas.winfo_width() - paddleW
    canvas.create_rectangle(paddleX, paddleY, paddleX + paddleW, paddleY + paddleH, fill = paddleC, width = lineWidth)
    
def drawBricks():
    for col in range(colCount):
        for row in range(rowCount):
            index = colCount*row + col
            
            if brick[index]:
                x1 = col*brickWidth
                x2 = x1 + brickWidth
                y1 = row*brickHeight
                y2 = y1 + brickHeight
                canvas.create_rectangle(x1, y1, x2, y2, fill = brickC, width = lineWidth)
                
def brickCollision():
    prevC = int((ball.x - ball.xV/fps)//brickWidth)
    prevR = int((ball.y - ball.yV)//brickHeight)
    ballC = int(ball.x//brickWidth)
    ballR = int(ball.y//brickHeight)
    ballIndex = colCount*ballR + ballC
    
    try:
        if brick[ballIndex]:
            brick[ballIndex] = False
            
            if prevC != ballC:
                ball.xV *= -1
            elif prevR != ballR:
                ball.yV *= -1
    except:
        pass
    
def main():
    root.after(round(1000/fps), main)
    canvas.delete('all')
    ball.draw()
    ball.move()
    paddleHandle()
    drawBricks()
    brickCollision()


ball = Ball()
reset()
main()
root.mainloop()
