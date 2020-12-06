############################################################################
# Generating Frames

import pygame as pg
import os

import math

pg.init()

resolution = (500, 500)
fps = 24 # frames per second
length_of_animation = 20 # seconds

# styling
background = (74, 74, 74)
pendulum = (106, 23, 26)
line_width = 2
line_color = (0, 0, 0)

image = pg.Surface(resolution)


# pendulum simulation variables
gravity = -1250
length = min(resolution)*0.4
radius = 20

center = (resolution[0]/2, resolution[1]/2)
angle = 179.99 * math.pi/180
velocity = 0
friction = 0.06

def draw_pendulum():
    x = resolution[0]/2 + length * math.sin(angle)
    y = resolution[1]/2 - -length * math.cos(angle)
    # draw line
    pg.draw.line(image, line_color, (center[0]-line_width/2, center[1]-line_width/2), (x-line_width/2, y-line_width/2), width = line_width)
    # draw pivot
    pg.draw.circle(image, (0,0,0), center, line_width)
    # draw mass
    pg.draw.circle(image, pendulum, (x, y), radius)
    pg.draw.circle(image, (0,0,0), (x, y), radius, width = line_width)

def move_pendulum():
    global angle, velocity
    aA = gravity/length * math.sin(angle) - friction*velocity
    velocity += aA/fps
    angle += velocity/fps

for frame_number in range(int(fps * length_of_animation)):
    image.fill(background)
    draw_pendulum()
    move_pendulum()
    pg.image.save(image, f'pend_anim_({frame_number}).png')
    os.rename(f'pend_anim_({frame_number}).png', f'images/pend_anim_({frame_number}).png')

############################################################################
# Generating the GIF

from PIL import Image

# generate frames
frames = []
for i in range(int(fps*length_of_animation)):
    new_frame = Image.open(f'images/pend_anim_({i}).png')
    #new_frame = new_frame.resize((300, 300), Image.ANTIALIAS)
    frames.append(new_frame)
    os.remove(f'images/pend_anim_({i}).png')

# save into GIF
frames[0].save("Pendulum_Animation.gif", format='GIF', append_images=frames[1:], save_all = True, loop = 0, duration = 1000/fps)