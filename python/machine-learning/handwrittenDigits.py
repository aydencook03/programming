#! /usr/bin/python
from tkinter import Canvas, Tk

root = Tk()
root.title('Handwriting Recognition')
root.resizable(False, False)
canvas = Canvas(root, width=600, height=600, highlightthickness=0, bg='white', bd=0)

def keyPress(data):
    if data.char == 'q':
        root.quit()

mouseX = canvas.winfo_width()/2
mouseY = canvas.winfo_height()/2
leftDown = False

def motion(data):
    global mouseX, mouseY
    mouseX = data.x
    mouseY = data.y

def mouseDown(data):
    global leftDown, mouseX, mouseY
    leftDown = True
    mouseX = data.x
    mouseY = data.y

def mouseUp(data):
    global leftDown
    leftDown = False

def mouseMotion(data):
    global mouseX, mouseY
    mouseX = data.x
    mouseY = data.y

root.bind("<Key>", keyPress)
root.bind("<ButtonPress-1>", mouseDown)
root.bind("<ButtonRelease-1>", mouseUp)
root.bind("<Motion>", mouseMotion)

canvas.pack()
root.update()

fps = 30

def mainLoop():
    root.after(round(1000/fps), mainLoop)
    canvas.delete('all')

mainLoop()
root.mainloop()