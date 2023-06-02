# Module MyTurtleDrawings.py

import turtle
import math


def drawPolygon_Turtle(t, num_vertices, cx, cy, line_length, color):
    center_pos = (cx, cy)
    t.up()
    t.goto(center_pos)
    t.dot(10, "blue")
    t.write(center_pos) t.width(3)
    t.pencolor(color)
    sx = cx - line_length/2
    theta = math.radians((180 - 360/num_vertices)/2)
    h = line_length * math.tan(theta) / 2
    sy = cy - h
    t.penup()
    t.goto(sx, sy)
    t.pendown()
    t.dot(10, "red")
    t.write((sx, sy))
    for i in range(num_vertices):
        t.forward(line_length)
        t.dot(10, "red")
        t.write(t.pos())
        t.left(360 / num_vertices)
    t.up()
    t.home()
    t.down()


def drawCircle_Turtle(t, cx, cy, radius, color):
    center_pos = (cx, cy)
    t.up()
    t.goto(center_pos)
    t.dot(10, "blue")
    t.write(center_pos) t.width(3)
    t.pencolor(color)
    sx, sy = cx, cy - radius
    t.dot(10, "red")
    t.write((sx, sy))
    t.penup()
    t.goto(sx, sy)
    t.pendown()
    t.circle(radius)
    t.up()
    t.home()
    t.down()


def drawStar_Turtle(t, cx, cy, length, color):
    center = (cx, cy)
    t.pencolor(color)
    t.up()
    t.goto(center)
    t.down()
    t.dot(10, "blue")
    t.write(center)
    sx = cx - length/2  # convert angle in degree into angle in radian
    theta = math.radians(360 / 5)
    h = length / (2 * math.tan(theta)
    sy=cy + h
    turn_angle=2*360/5
    t.penup()
    t.goto(sx, sy)
    t.dot(10, "blue")
    t.write(t.position())
    t.pendown()  # pen down to draw
    for i in range(5):
        t.forward(length)
        t.right(turn_angle)
    t.up()
    t.home()
    t.down()
