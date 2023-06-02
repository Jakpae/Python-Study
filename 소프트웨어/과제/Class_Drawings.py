# Class_Drawings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 27, 2023
# Major features :

# 그림을 그리기 위한 Turtle 모듈과 
# 수학적인 계산을 위한 math 모듈
import turtle
import math

# 클래스 self에 관한 설명
# 실습 8.1에서 s = Polygon이라고 쓸때 self를 쓰지 않으면 s.turtle_draw에서 오류가 발생하게 됨
# 그 이유는 self는 클래스를 저장할 변수를 뜻하는데 이는 s.turtle_draw 에서 s. 이 __init__을 실행하는거와 같이
# s. 에서 실행되는 변수를 뜻하기 때문이다.

# Shape 클래스 생성
class Shape:
    # 생성자 __init__을 사용해서 stype,cx,cy,color 정의 
    def __init__(self, stype, cx, cy, color): 
        self.stype = stype
        self.cx = cx
        self.cy = cy
        self.color = color
        
class Circle(Shape):
    # 생성자 __init__을 사용해서 radius(반지름) 정의
    def __init__(self, cx, cy, radius, color='Black'): 
        Shape.__init__(self, "Circle", cx, cy, color) 
        self.radius = radius #radius of circle
    def __str__(self):
        return "a {} circle: [center=({}, {}), radius ={}]".\
        format(self.color, self.cx, self.cy, self.radius) 
    def turtle_draw(self, t):
        t.penup(); t.goto(self.cx, self.cy);
        t.pendown()
        t.dot(10, "blue")
        t.write(t.pos())
        sx = self.cx
        sy = self.cy - self.radius
        t.penup(); t.goto(sx, sy); t.pendown() 
        t.dot(10, "red")
        t.write((sx, sy))
        t.circle(self.radius)
        t.up()
        t.goto((self.cx, self.cy))
        t.down()
        
shape_types = {3:"Triangle", 4:"Square", 5:"Pentagon", 6:"Hexagon", 7:"Heptagon", 8:"Octagon", 9:"Septagon"}

class Polygon(Shape):
    def __init__(self, n_vert, cx, cy, radius, color = 'Black'): 
        Shape.__init__(self, shape_types[n_vert], cx, cy, color) 
        self.n_vert = n_vert # number of vertices
        self.radius = radius # radius of circumcircle (외접원) 
        self.color = color
    def __str__(self):
        return "a {} {} at center_pos(center=({}, {}) with circumcircle_radius = {}".\
            format(self.color, self.stype, self.cx, self.cy, self.radius) 
    
    def turtle_draw(self, t):
        t.penup(); t.goto(self.cx, self.cy)
        t.pendown() 
        t.dot(10, "blue")
        t.write(t.pos())
        t.width(1)
        t.up(); t.goto(self.cx, self.cy-self.radius)
        t.down() 
        t.color("black")
        t.circle(self.radius)
        t.up(); t.goto(self.cx-80, self.cy - self.radius - 15)
        t.down() 
        s = "{} {} centered at ({}, {})".\
            format(self.color, self.stype, self.cx, self.cy) 
        t.write(s)
        t.width(3)
        theta = math.radians(180/self.n_vert)
        sx = self.cx - self.radius*math.sin(theta) 
        side_length = 2 * self.radius*math.sin(theta)
        sy = self.cy - self.radius * math.cos(theta) 
        t.penup()
        t.goto(sx, sy)
        t.pendown()
        t.dot(10, "red"); t.write((round(sx, 2), round(sy, 2)))
        t.color(self.color)
        for i in range(self.n_vert):
            t.forward(side_length) 
            #t.dot(10, "red"); t.write(t.pos()) 
            t.left(360 / self.n_vert)
        t.up(); t.goto((self.cx, self.cy)); t.down()
