# MyTurtleDrawings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - Draw a circle of the specified radius if the n_poly value is 0
# -After drawing all the polygons, move to the coordinate (0, 0), which is the home position of the turtle

import turtle
import math

# 각 꼭지점의 갯수를 구하는 getNumVertices 함수
# sh_name 즉 도형의 이름을 입력받고 그 도향의 이름에 맞는 곡지점 갯수를 return 시킴
def getNumVertices(sh_name):
    if sh_name == "triangle":
        return 3
    elif sh_name == "square":
        return 4
    elif sh_name == "pentagon":
        return 5
    elif sh_name == "hexagon":
        return 6
    elif sh_name == "heptagon":
        return 7
    elif sh_name == "octagon":
        return 8
    elif sh_name == "noagon":
        return 9
    elif sh_name == "decagon":
        return 10
    elif sh_name == "circle":
        return 0

# 그림을 그리는 draw_polygon함수 꼭지점이 0, 즉 원이면 다르게 작동되도록 설정함
def draw_polygon(t,n_poly,cx,cy,radius,color):
    if n_poly == 0:
        t.up()
        # (cx - radius - 30 ) , (cy - radius - 20)으로 가서 해당 도형의 꼭지점 반지름 cx,cy를 적음
        t.goto((cx - radius - 30, cy - radius - 20))
        t.write("n_poly({}), radius({}), cx({}), cy({})".format(n_poly,radius,cx,cy))
        t.up()
        t.goto((cx,cy))
        t.down()
        t.dot(10,"blue")
        t.write(t.pos())
        t.up()
        t.goto(cx,cy-radius)
        t.down()
        t.width(5)
        t.color(color)
        t.circle(radius)
    else:
        t.up()
        # (cx - radius - 30 ) , (cy - radius - 20)으로 가서 해당 도형의 꼭지점 반지름 cx,cy를 적음
        t.goto((cx - radius - 30, cy - radius - 20))
        t.write("n_poly({}), radius({}), cx({}), cy({})".format(n_poly,radius,cx,cy))
        t.up()
        t.goto((cx,cy))
        t.down()
        t.dot(10,"blue")
        t.write(t.pos())
        t.up()
        t.goto(cx,cy-radius)
        t.down()
        t.width(2)
        t.color("black")
        t.circle(radius)

        turn_angle_deg = 360 / n_poly
        
        # import한 math 함수를 이용해서 다각형의 theta_rad , h , b를 구함
        theta_rad = (math.pi - math.pi * 2 / n_poly) / 2

        h = radius * math.sin(theta_rad)
        b = radius * math.cos(theta_rad)

        sx = cx - b
        sy = cy - h

        t.up()
        t.goto(sx,sy)
        t.down()
        t.dot(10, "blue")
        t.write(t.pos())
        t.width(5)
        t.color(color)
        
        # 도형을 그리는 for 반복문
        for i in range(n_poly):
            t.forward(2 * b)
            t.left(turn_angle_deg)

        t.up()
        t.home()
        t.down()
        t.color("black")
