#! /usr/bin/python

from tkinter import Tk, Canvas
from random import randint
from math import cos, sin, atan

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
        
def button(data):
    global running
    
    if not running:
        running = True
    
root.bind('<Key>', keyPress)
root.bind('<Motion>', motion)
root.bind('<Button-1>', button)
canvas.pack(fill = 'both', expand = 1)
root.update()

######################################################################################################################
# Ball Class

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
        global lives, paddleC
        
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
            global running
            running = False
            if lives > 0:
                lives -= 1
                self.reset() 
            if lives <= 0: 
                reset()
            if lives == 3:
                paddleC = 'SpringGreen3'
            elif lives == 2:
                paddleC = 'orange'
            elif lives == 1:
                paddleC = 'crimson'
            
        if self.x + self.r >= paddleX and self.x - self.r <= paddleX + paddleW:
            if self.y + self.r >= paddleY and self.y - self.r <= paddleY + paddleH:
                prevX = self.x - self.xV/fps
                prevY = self.y - self.yV/fps
                
                if prevY + self.r < paddleY:
                    self.y = paddleY - self.r
                    self.yV *= -1
                    val = paddleW/9
                    self.xV = (self.x - (paddleX + paddleW/2)) * val
                elif prevX + self.r < paddleX:
                    self.x = paddleX - self.r
                    self.xV *= -1
                elif prevX - self.r > paddleX + paddleW:
                    self.x = paddleX + paddleW + self.r
                    self.xV *= -1
                
        
        self.x += self.xV/fps
        self.y += self.yV/fps
        
    def reset(self):
        lower = 10
        upper = 400
        xV = 0
        yV = 0
        
        while abs(xV) < lower:
            xV = randint(-upper, upper)
        yV = -upper
        
        self.xV = xV
        self.yV = yV
        self.x = paddleX + paddleW/2
        self.y = paddleY - paddleH
        
######################################################################################################################
# Initialization Code

def reset():
    global fps; fps = 60
    global running; running = False
    
    global testing; testing = False

    global colCount; colCount = 7
    global rowCount; rowCount = 9
    global brickPadding; brickPadding = 4
    global emptyRowCount; emptyRowCount = 2
    global heightDown; heightDown = canvas.winfo_height()/2.2
    global brickWidth; brickWidth = canvas.winfo_width()/colCount
    global brickHeight; brickHeight = heightDown/rowCount
    global brickC; brickC = 'teal'

    global ballRadius; ballRadius = 4
    global ballC; ballC = 'crimson'
    global lineWidth; lineWidth = 2

    global paddleW; paddleW = 80
    global paddleH; paddleH = 15
    global padding; padding = paddleH
    global paddleX; paddleX = canvas.winfo_width()
    global paddleY; paddleY = canvas.winfo_height() - padding - paddleH
    global paddleC; paddleC = 'SpringGreen3'


    global brick; brick = []
    global bricksLeft; bricksLeft = 0
    global textC; textC = 'white'
    global lives; lives = 3
    
    brick.clear()
    brick = [False] * (rowCount * colCount)
    try:
        ball.reset()
    except:
        pass
    bricksLeft = 0
    
    for col in range(colCount):
        for row in range(rowCount):
            index = colCount*row + col
            brick[index] = True
            bricksLeft += 1
    for i in range(emptyRowCount * colCount):
        brick[i] = False
        bricksLeft -= 1

######################################################################################################################
# Game Logic
  
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
                x1 = brickPadding/2 + col*brickWidth
                x2 = x1 + brickWidth - brickPadding
                y1 = brickPadding/2 + row*brickHeight
                y2 = y1 + brickHeight - brickPadding
                canvas.create_rectangle(x1, y1, x2, y2, fill = brickC, width = lineWidth)
                
def getIndex(col, row):
    return int(col + colCount * row)
                
def brickCollision():
    global bricksLeft
    
    prevC = int((ball.x - ball.xV/fps)//brickWidth)
    prevR = int((ball.y - ball.yV/fps)//brickHeight)
    ballC = int(ball.x//brickWidth)
    ballR = int(ball.y//brickHeight)
    
    ballIndex = getIndex(ballC, ballR)
    
    bothTestsFailed = True
    
    if ballC >= 0 and ballC < colCount and ballR >= 0 and ballR < rowCount and brick[ballIndex]:
        brick[ballIndex] = False
        bricksLeft -= 1
        if bricksLeft <= 0:
            reset()
        
        if prevC != ballC and brick[getIndex(prevC, ballR)] == False:
            ball.xV *= -1
            bothTestsFailed = False
        try:
            if prevR != ballR and brick[getIndex(ballC, prevR)] == False:
                ball.yV *= -1
                bothTestsFailed = False
        except:
            ball.yV *= -1
            bothTestsFailed = False
        if bothTestsFailed:
            ball.xV *= -1
            ball.yV *= -1
            
def text():
    canvas.create_text(canvas.winfo_width()/2, brickHeight * 1*emptyRowCount/3, fill = textC, text = 'Bricks: ' + str(bricksLeft))
    canvas.create_text(canvas.winfo_width()/2, brickHeight * 2*emptyRowCount/3, fill = textC, text = 'Lives: ' + str(lives))
    val = canvas.winfo_height() - (canvas.winfo_height()-heightDown)/2
    canvas.create_text(mouseX, mouseY, fill = textC, text = 'Click to Continue')
    canvas.create_text(canvas.winfo_height()/2, val, fill = textC, text = 'Game by Ayden Cook')
    
######################################################################################################################
# Game Loop
    
def main():
    root.after(round(1000/fps), main)
    canvas.delete('all')
    ball.draw()
    if running:
        ball.move()
    else:
        ball.x = paddleX + paddleW/2
    paddleHandle()
    drawBricks()
    brickCollision()
    if not running:
        text()

reset()
ball = Ball()
reset()
main()
root.mainloop()
