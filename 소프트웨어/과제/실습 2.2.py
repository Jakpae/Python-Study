# 실습 2.2
# Author :
# Student ID :
# Dept : Info & Comm. Eng
# Date : March 9, 2023
# Major features :
# - Draw a Triangle with Turtle

# 계산을 위한 Math 모듈과 그림을 그리기 위한 Turtle 모듈 import
import math
import turtle

# 터틀 컨버스(화면) 400,400의 정사각형으로 설정
turtle.setup(400, 400)

# 터틀 제목 설정
turtle.title("정삼각형 그리기")

# Turtle 모듈의 Turtle 호출 함수를 t로 설정
t = turtle.Turtle()

# 터틀 모양 거북이로 설정
t.shape("turtle")

# 터틀 팬 색상 파란색으로 설정
t.pencolor("blue")

# 터틀이 그리는 펜 너비를 10으로 설정
t.width(10)

# 정사각형의 밑변을 Float(실수)로 입력받음
side_length = float(input("정삼각형의 밑변 = "))

# 삼각형이니까 터틀의 회전방향을 120도로 설정
turn_angle = 360 / 3

# 정삼각형의 무게 중심 즉 h를 구하는 공식은 [ √3 / 2 * 밑변 ] 이므로 2.0 * math.tan(math.pi/3)로 적음
h = side_length / (2.0 * math.tan(math.pi/3))


sx, sy = -side_length/2, -h

t.dot(5, "red")
t.write(t.pos())

print("sx, sy =", sx, sy)
t.up()
t.goto(sx, sy)
t.down()
for i in range(3):
    t.write(t.pos())
    t.forward(side_length)
    t.left(turn_angle)

t.up()
t.home()
t.down()
