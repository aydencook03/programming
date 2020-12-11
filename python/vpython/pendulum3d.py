import vpython as vp
import math

screen = vp.canvas(title="Pendulum", background = vp.vector(0.6,.6,.6))

fps = 60
running = True

gravity = -9.8
length = 2.5
radius = 0.2
friction = 0.15

color = vp.color.red
lineWidth = 0.04

angle = 179.9 * math.pi/180
angleV = 0

ball = vp.sphere(pos=vp.vector(length*math.sin(angle), -length*math.cos(angle), 0), radius = radius, color=color)
joint = vp.sphere(pos=vp.vector(0,0,0), radius=lineWidth, color=vp.color.black)
rod = vp.cylinder(pos=joint.pos, axis=ball.pos, radius=0.02, color = vp.vector(0,0,0))

def movePend():
    global angle, angleV, ball, rod

    aA = gravity/length * math.sin(angle)
    angleV += aA/fps
    angle += angleV/fps

    ball.pos = vp.vector(length*math.sin(angle), -length*math.cos(angle), 0)
    rod.pos = joint.pos
    rod.axis = ball.pos


while running:
    vp.rate(fps)
    movePend()