# 실습 2.3
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 9, 2023
# Major features :
# - Draw a Star with Turtle

import math
import turtle

line_length = float(input("별의 선의 길이 ="))
cx, cy = 0, 0
sx = cx - line_length / 2
theta_rad = math.radians(360 / 5)
sy = cy + line_length / (2 * math.tan(theta_rad))
print("cx ({}), cy ({}), line_length ({}) => sx ({}), sy({})".format(
    cx, cy, line_length, sx, sy))
print("2 * math.tan(theta_rad) = {}".format(2 * math.tan(theta_rad)))

turtle.setup(500, 500)
turtle.title("주어진 위치에서 별을 그리기")
t = turtle.Turtle()
t.shape('classic')
t.width(5)

cx, cy = 0, 0
center = (cx, cy)


t.up()
t.goto(center)
t.down()
t.dot(10, "blue")
t.write(center)

# sx는 별의 선의 길이의 절반
sx = cx - line_length/2

# 세타는 라디안90 즉 1.256정도
theta = math.radians(360 / 5)

# 탄젠트를 이용해서 무게중심 구하는 공식
h = line_length / (2 * math.tan(theta))

sy = cy + h

t.penup()
t.goto(sx, sy)
t.pendown()
t.dot(10, "blue")
t.pencolor('red')
t.write(t.position())
t.pendown()
turn_angle = 2*360/5
count = 0
while count < 5:
    t.forward(line_length)
    t.write(t.pos())
    t.right(turn_angle)
    count = count + 1

t.up()
t.home()
t.down()
