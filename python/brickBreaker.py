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
brickPadding = 4
emptyRowCount = 2
brickWidth = canvas.winfo_width()/colCount
brickHeight = canvas.winfo_height()/2.2/rowCount
brickC = 'teal'

ballRadius = 4
ballC = 'crimson'
lineWidth = 2

paddleW = 80
paddleH = 15
padding = paddleH
paddleX = canvas.winfo_width()
paddleY = canvas.winfo_height() - padding - paddleH


brick = []
bricksLeft = 0
textC = 'white'



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
                    val = paddleW/10
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
        global ball
        
        lower = 10
        upper = 350
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
    global brick, bricksLeft, lives, paddleC
    
    brick.clear()
    brick = [False] * (rowCount * colCount)
    ball.reset()
    bricksLeft = 0
    lives = 3
    paddleC = 'SpringGreen3'
    
    for col in range(colCount):
        for row in range(rowCount):
            index = colCount*row + col
            brick[index] = True
            bricksLeft += 1
    for i in range(emptyRowCount * colCount):
        brick[i] = False
        bricksLeft -= 1
  
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
    
    
    
def main():
    root.after(round(1000/fps), main)
    canvas.delete('all')
    ball.draw()
    ball.move()
    paddleHandle()
    drawBricks()
    brickCollision()
    #text()

ball = Ball()
reset()
main()
root.mainloop()
