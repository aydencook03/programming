#! /usr/bin/python

from tkinter import *

root = Tk()
root.title("BrickBreaker")
canvas = Canvas(root, width = 600, height = 600, highlightthickness = 0, bg = "grey27", bd = 0)
def keyPress(data):
    if data.char == 'q':
        root.quit()
root.bind('<Key>', keyPress)
canvas.pack(fill = BOTH, expand = 1)
root.update()

bricks = []

class Brick:
    def __init__(self):
        

root.mainloop()
