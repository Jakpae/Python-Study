# MyTurtleDrawings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :

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
    
    sh_name = ""
    
    # 도형의 이름을 알기위한 if문
    if n_poly == 3:
        sh_name = "triangle"
    elif n_poly == 4:
        sh_name = "square"
    elif n_poly == 5:
        sh_name = "pentagon"
    elif n_poly == 6:
        sh_name = "hexagon"
    elif n_poly == 7:
        sh_name = "heptagon"
    elif n_poly == 8:
        sh_name = "octagon"
    elif n_poly == 9:
        sh_name = "noagon"
    elif n_poly == 10:
        sh_name = "decagon"
    elif n_poly == 0:
        sh_name = "circle"
    
    if n_poly == 0:
        t.up()
        # (cx - radius) , (cy - radius - 20)으로 가서 해당 도형의 색상과 이름을 출력
        t.goto((cx - radius, cy - radius - 20))
        t.write("{} {}".format(color,sh_name))
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
        # (cx - radius) , (cy - radius - 20)으로 가서 해당 도형의 색상과 이름을 출력
        t.goto((cx - radius, cy - radius - 20))
        t.write("{} {}".format(color,sh_name))
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
