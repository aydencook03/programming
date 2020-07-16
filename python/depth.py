#! /usr/bin/python

# https://www.a1k0n.net/2011/07/20/donut-math.html

from tkinter import Tk, Canvas

root = Tk()
root.title('Depth')

def key(data):
    if data.char == 'q':
        root.quit()
    if data.char == 'r':
        reset()

root.bind('<Key>', key)
canvas = Canvas(root, width = 600, height = 600, bg = 'grey27', bd = 0, highlightthickness = 0)
canvas.pack(fill = 'both', expand = 1)



fps = 60

def reset():
    global x1, x2, xV
    global y1, y2, yV
    global z, zV, fovConst
    global x1Prime, x2Prime
    global y1Prime, y2Prime
    global color, lineWidth
    
    width = 100
    height = 70
    
    fovConst = 10
    
    x1 = canvas.winfo_width()/2
    x2 = x1 + width
    xV = 0
    
    y1 = canvas.winfo_height()/2
    y2 = y1 + height
    yV = 0
    
    z = 0
    zV = 40
    
    color = 'crimson'
    lineWidth = 2
    
    x1Prime = None
    x2Prime = None
    y1Prime = None
    y2Prime = None
    
    

def moveCircle():
    global x1, x2, y1, y2, z
    global x1Prime, x2Prime, y1Prime, y2Prime
    
    x1 += xV/fps
    x2 += xV/fps
    y1 += yV/fps
    y2 += yV/fps
    z += zV/fps
    
    x1Prime = (fovConst * x1)/z
    x2Prime = (fovConst * x2)/z
    
    y1Prime = (fovConst * y1)/z
    y2Prime = (fovConst * y2)/z
    
    
def drawCircle():
    canvas.create_rectangle(x1Prime, y1Prime, x2Prime, y2Prime, fill = color, width = lineWidth)
    


def main():
    root.after(round(1000/fps), main)
    canvas.delete('all')
    moveCircle()
    drawCircle()
    
    
reset()
main()
root.mainloop()
