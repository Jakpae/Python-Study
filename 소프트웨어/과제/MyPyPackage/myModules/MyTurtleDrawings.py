# Module MyTurtleDrawings.py

# 그림을 그리기 위한 Turtle 모듈과 계산을 위한 math 모듈 import
import turtle
import math

# 다각형을 그리기 위한 drawPolygon_Turtle 함수 생성
def drawPolygon_Turtle(t, num_vertices, cx, cy, line_length, color):
    center_pos = (cx, cy) # 센터 자리를 cx,cy로 설정
    t.up() # 터틀 펜 들기
    t.goto(center_pos) # 센터로 이동
    t.dot(10, "blue") # 현재 위치에 지름 10의 파란색 원 그리기
    t.write(center_pos) # 현재 위치 (센터 자리)를 적기
    t.width(3) # 펜 너비 3으로 설정
    t.pencolor(color) # 펜 색상 color로 변경
    sx = cx - line_length/2 # 다각형의 sx 구하기
    theta = math.radians((180 - 360/num_vertices)/2) # 각을 구하기 위한 계산식
    h = line_length * math.tan(theta) / 2 # h 즉 높이 설정
    sy = cy - h # sy 계산
    t.penup() # 펜 들기
    t.goto(sx, sy) # sx,sy로 이동
    t.pendown() # 펜 내리기
    t.dot(10, "red") # 현재 위치에 지름 10의 빨간색 원 그리기
    t.write((sx, sy)) # 현재 위치에 sx,sy위치 적기
    for i in range(num_vertices): # 다각형의 각 수만큼 for 반복문 반복
        t.forward(line_length) # 한변의 길이만큼 이동
        t.dot(10, "red") # 현재 위치에 지름 10의 빨간색 원 그리기
        t.write(t.pos()) # 현재 위치를 적기
        t.left(360 / num_vertices) # 360 / num_vertices 즉 한 각의 크기만큼 왼쪽으로 돌기
    t.up() # 펜 들기
    t.home() # 홈 (0,0)으로 이동
    t.down() # 펜 내리기

# 원을 그리기 위한 drawCircle 함수 생성
def drawCircle_Turtle(t, cx, cy, radius, color):
    center_pos = (cx, cy)
    t.up()
    t.goto(center_pos)
    t.dot(10, "blue")
    t.write(center_pos)
    t.width(3)
    t.pencolor(color)
    sx, sy = cx, cy - radius # cx,cy 를 이용해 sx,sy 구하기
    t.dot(10, "red")
    t.write((sx, sy))
    t.penup()
    t.goto(sx, sy)
    t.pendown()
    t.circle(radius) # 반지름 만큼의 원 그리기
    t.up()
    t.home()
    t.down()

# 별을 그리기 위한 drawStar 함수 생성
def drawStar_Turtle(t, cx, cy, length, color):
    center = (cx, cy)
    t.pencolor(color)
    t.up()
    t.goto(center)
    t.down()
    t.dot(10, "blue")
    t.write(center)
    sx = cx - length/2  # 각도를 라디안값으로 변환
    theta = math.radians(360 / 5) #반지름 값을 이용해 theta 계산
    h = length / (2 * math.tan(theta)) # h를 구하는 식
    sy = cy + h
    turn_angle = 2*360/5 #별의 각도 144도 구함
    t.penup()
    t.goto(sx, sy)
    t.dot(10, "blue")
    t.write(t.position())
    t.pendown()  # 펜 내리기
    for i in range(5):
        t.forward(length)
        t.right(turn_angle)
    t.up()
    t.home()
    t.down()
