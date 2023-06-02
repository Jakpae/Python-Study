# TurtleDrawings_classPolygons
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 11, 2023

import turtle
import math

class Shape:
    
    __slots__ = ['shape_name','cx','cy','color']

# 꼭지점 개수로 부터 정다각형 이름을 찾을 수 있는 딕셔너리 shape_types
shape_types = {0: "circle", 3: "triangle", 4: "square", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon"}
# 정사각형 이름으로 부터 꼭지점 개수를 찾을 수 있는 딕셔너리 num_vert
num_vert = {"circle": 0, "triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8, "nonagon": 9, "decagon": 10}


class Polygon(Shape):
    
    # 도형의 기본정보 color,shape_name,cx,cy,radius 전달
    def __init__(self, color, shape_name, cx, cy, radius):
        self.color = color
        self.shape = shape_name
        self.cx = cx
        self.cy = cy
        self.radius = radius
    
    # 도형의 색상, 이름, 중심좌표, 외접원의 반지름 출력 
    def __str__(self):
        return '{} {} {} {} {}'.format(self.color, self.shape, self.cx, self.cy, self.radius)
        
    # 지정된 터틀 객체 t를 사용하여 도형을 그리는 함수 turtle_draw
    def turtle_draw(self,t):
        # 색상, 이름, 중심좌표, 반지름 입력
        color, shape_name, cx, cy, radius = self.color, self.shape, self.cx, self.cy, self.radius
        # 도형의 이름을 기준으로 num_vertex 즉, 꼭지점 수를 찾아냄
        num_vertex = num_vert[shape_name]
        if num_vertex == 0:
            t.color(color)
            t.up()
            t.goto((cx - radius - 5, cy - radius - 20))
            t.write("{} {} centered at ({}, {})".format(color, shape_types[num_vertex], cx, cy))
            t.up()
            t.goto((cx, cy))
            t.down()
            t.dot(10, "blue")
            t.write("({:0.2f}, {:0.2f})".format(cx, cy))
            t.up()
            t.goto(cx, cy-radius)
            t.down()
            t.width(5)
            t.color(color)
            t.circle(radius)
            t.dot(10, "red")
        else:
            t.color(color)
            t.up()
            t.goto((cx - radius - 5, cy - radius - 20))
            t.write("{} {} centered at ({}, {})".format(color, shape_types[num_vertex], cx, cy))
            t.up()
            t.goto((cx, cy))
            t.down()
            t.dot(10, "blue")
            t.write("({:0.2f}, {:0.2f})".format(cx, cy))
            t.up()
            t.goto(cx, cy-radius)
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
            t.goto(sx, sy)
            t.down()
            t.dot(5, "red")
            t.color(color)
            t.write(t.pos())
            t.width(5)
            t.color(color)
            # 도형을 그리는 for 반복문
            for i in range(num_vertex):
                t.forward(2 * b)
                t.left(turn_angle_deg)
            t.dot(10, "red")
            t.up()
            t.home()
            t.down()

# 재졍됴ㅐㄴ 텍스트 파일 객체 fin으로 부터 다각형의 정보를 읽고 return 시켜주는 fget_drawings 함수
def fget_drawings(fin):
    L_draw = []
    for line in fin:
        # line_split()을 사용해 도형의 자료를 나눈후 각각 color, shape_name, cx, cy, radius 로 지정
        color, shape_name, cx, cy, radius = line.split()
        st = Polygon(color, shape_name, int(cx), int(cy), int(radius))
        # 구한 st를 L_draw리스트에 넣음
        L_draw.append(st)
    # 구한 도형의 기본정보를 return 시킴
    return L_draw