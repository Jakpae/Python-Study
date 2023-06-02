# MyTurtleDrawings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

# 도형을 그리기 위한 turtle 과 계산을 위한 math 모듈
import turtle
import math

# 각 꼭지점의 갯수를 구하는 getNumVertices 함수
def getNumVertex(polygon_name):
    if polygon_name == "square":
        return 4
    elif polygon_name == "pentagon":
        return 5
    elif polygon_name == "hexagon":
        return 6
    elif polygon_name == "heptagon":
        return 7
    elif polygon_name == "octagon":
        return 8
    elif polygon_name == "nonagon":
        return 9
    elif polygon_name == "decagon":
        return 10
    elif polygon_name == "circle":
        return 0

# 도형의 이름을 구하는 함수
def getPolygonName(num_vertex):
    if num_vertex == 4:
        return "square"
    elif num_vertex == 5:
        return "pentagon"
    elif num_vertex == 6:
        return "hexagon"
    elif num_vertex == 7:
        return "heptagon"
    elif num_vertex == 8:
        return "octagon"
    elif num_vertex == 9:
        return "noagon"
    elif num_vertex == 10:
        return "decagon"
    elif num_vertex == 0:
        return "circle"
    
# 그림을 그리는 draw_polygon함수 꼭지점이 0, 즉 원이면 다르게 작동되도록 설정함
def drawPolygon(t,center_pos,num_vertex,radius,color):
    cx = center_pos[0]
    cy = center_pos[1]
    if num_vertex == 0:
        t.color(color)
        t.up()
        t.goto((cx - radius - 5, cy - radius - 20))
        t.write("{} {}".format(color,getPolygonName(num_vertex)))
        t.up()
        t.goto((cx,cy))
        t.down()
        t.dot(5,"blue")
        t.write(center_pos)
        t.up()
        t.goto(cx,cy-radius)
        t.down()
        t.width(5)
        t.color(color)
        t.circle(radius)
    else:
        t.color(color)
        t.up()
        t.goto((cx - radius - 5, cy - radius - 20))
        t.write("{} {}".format(color,getPolygonName(num_vertex)))
        t.up()
        t.goto((cx,cy))
        t.down()
        t.dot(5,"blue")
        t.write(center_pos)
        t.up()
        t.goto(cx,cy-radius)
        t.down()
        t.width(1)
        t.color("black")
        t.circle(radius)

        turn_angle_deg = 360 / num_vertex
        theta_rad = (math.pi - math.pi * 2 / num_vertex) / 2

        h = radius * math.sin(theta_rad)
        b = radius * math.cos(theta_rad)

        sx = cx - b
        sy = cy - h

        t.up()
        t.goto(sx,sy)
        t.down()
        t.dot(5,"red")
        t.color(color)
        t.write(t.pos())
        t.width(5)
        t.color(color)
        for i in range(num_vertex):
            t.forward(2 * b)
            t.left(turn_angle_deg)
        t.up()
        t.home()
        t.down()

# 별을 그리는 함수
def drawStar(t, center_pos, length, color):
    cx = center_pos[0]
    cy = center_pos[1]
    center = (cx, cy)
    t.pencolor("black")
    t.width(1)
    t.up()
    t.goto(cx,cy-length)
    t.down()
    t.circle(length)
    length = length * 2
    t.color(color)
    t.down()
    t.width(5)
    t.up()
    t.goto((cx - length + 50, cy - length + 30))
    t.write("{} star".format(color))
    t.goto(center_pos)
    t.dot(5, "blue")
    t.write(center_pos)
    t.down()
    sx = cx - length/2  # 각도를 라디안값으로 변환
    theta = math.radians(360 / 5) #반지름 값을 이용해 theta 계산
    h = length / (2 * math.tan(theta)) # h를 구하는 식
    sy = cy + h
    turn_angle = 2*360/5 #별의 각도 144도 구함
    t.penup()
    t.goto(sx, sy)
    t.dot(5, "blue")
    t.write(t.position())
    t.pendown()  # 펜 내리기
    t.dot(5,"red")
    for i in range(5):
        t.forward(length)
        t.right(turn_angle)
    t.up()
    t.home()
    t.down()

