from tkinter import *
import time

WIDTH = 600
HEIGHT = 600
running = True
fps = 60

PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 5

root = Tk()
root.title("Bounce")
root.resizable(0,0) # Prevents window from resizing
canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg = "grey", bd = 0, highlightthickness = 0)
canvas.pack()
root.update()

class Paddle():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.x = WIDTH/2 - PADDLE_WIDTH/2
        self.y = HEIGHT - PADDLE_HEIGHT * 2
        self.xV = 0
        self.id = canvas.create_rectangle(self.x, self.y, self.x + PADDLE_WIDTH, self.y + PADDLE_HEIGHT, fill = color)
    def move(self):
        self.canvas.move(self.id,self.xV, 0)
        
class Ball():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.xV = 3
        self.yV = 2
        self.d = BALL_RADIUS*2
        self.canHeight = self.canvas.winfo_height()
        self.canWidth = self.canvas.winfo_width()
        self.id = canvas.create_oval(self.x, self.y, self.x + self.d, self.y + self.d, fill = color)

    def move(self):
        self.canvas.move(self.id,self.xV,self.yV)
        pos = self.canvas.coords(self.id) # returns [x1,y1,x2,y2]
        
        if pos[0] <= 0: #left
            self.canvas.move(self.id,-self.xV,0)
            self.xV *= -1
        if pos[2] >= self.canWidth: #right
            self.canvas.move(self.id,-self.xV,0)
            self.xV *= -1
        if pos[1] <= 0: #top
            self.canvas.move(self.id,0,-self.yV)
            self.yV *= -1
        if pos[3] >= self.canHeight: #bottom
            self.canvas.move(self.id,0,-self.yV)
            self.yV *= -1

paddle = Paddle(canvas, "crimson")
ball = Ball(canvas, "teal")

while running:
    paddle.move()
    ball.move()
    root.update_idletasks()
    root.update()
    time.sleep(round(1/fps, 2))
