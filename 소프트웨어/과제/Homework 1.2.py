# Lab01.4 Basic turtle drawings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 3, 2023
# Major featur :
# - turtle drawing of circle, triangle, and rectangle

import turtle

turtle.setup(800, 400)
t = turtle.Turtle()
t.shape("turtle")
t.width(3)

# drawing a circle
radius = 50
cx, cy = -200, 0
t.up(); t.goto((cx, cy)); t.dot(10, "red")
t.up(); t.goto((cx, cy - radius)); t.down()

t.color("red")
t.circle(radius)

# drawing a triangle

base = 100
cx, cy = 20, 0
t.up(); t.goto((cx, cy)); t.dot(10, "red")
t.up(); t.goto((cx -base/2, cy -base/3)); t.down()
turn_angle = 120
t.color("green")
t.forward(base); t.left(turn_angle)
t.forward(base); t.left(turn_angle)
t.forward(base); t.left(turn_angle)

# drawing a rectangle
width, length = 100, 50
cx, cy = 200, 0
t.up(); t.goto((cx, cy)); t.dot(10, "red")
t.up(); t.goto((cx -width/2, cy-length/2)); t.down()

turn_angle = 90
t.color("blue")
t.forward(width); t.left(turn_angle)
t.forward(length); t.left(turn_angle)
t.forward(width); t.left(turn_angle)
t.forward(length); t.left(turn_angle)
