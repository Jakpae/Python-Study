# Homework 6.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 6, 2023
# Major features :
# - Using turtle graphic fuction drawing polygons
# - Making tuple list for n_poly, radius, cx, cy
# - Drawing Circle in blue color, Drawing polygons in red color

import turtle
import math

# draw_polygon 함수 구현


def draw_polygon(t, n_poly, radius, cx, cy):
    t.up()  # 터틀 펜 들기
    # (cx -radius , cy-radius - 20 좌표로 이동)
    t.goto((cx - radius, cy - radius - 20))
    # 현재위치에 n_poly, radius, cx,cy 그리기
    t.write("n_poly({}), radius ({}), cx ({}), cy({})".format(
        n_poly, radius, cx, cy))

    t.up()  # 터틀 펜 들기
    t.goto((cx, cy))  # (cx,cy)좌표로 이동
    t.dot(10, "blue")  # 현재 위치의 지름 10크기의 "blue"색상 점 찍기
    t.write(t.pos())  # 현재위치에 현재좌표 적기
    t.up()  # 터틀 펜 들기
    t.goto((cx, cy-radius))  # 터틀 (cx,cy-radius)로 이동
    t.down()  # 터틀 펜 내리기
    t.width(2)  # 펜 너비 2로 설정
    t.color("blue")  # 터틀 색상 "blue"로 설정
    t.circle(radius)  # 현재위치에 radius 반지름 크기의 원 그리기

    turn_angle_deg = 360 / n_poly  # n_poly로 받은 다각형수를 360에 나눠서 다각형의 한 각을 구함
    theta_rad = (math.pi - math.pi * 2 / n_poly) / 2

    # sin과 cos을 이용해 다각형의 높이와 한 변의 절반 구하기
    h = radius * math.sin(theta_rad)
    b = radius * math.cos(theta_rad)

    sx = cx - b
    sy = cy - h

    t.up()  # 터틀 펜 들기
    t.goto(sx, sy)  # (sx,sy)좌표로 이동
    t.down()  # 터틀 펜 내리기
    t.dot(10, "blue")  # 현재 위치의 지름 10크기의 "blue"색상 점 찍기
    t.write(t.pos())  # 현재위치에 현재좌표 적기
    t.width(5)  # 펜 너비 5로 설정
    t.color("red")  # 터틀 색상 "red"로 설정

    # 다각형 그리기
    for i in range(n_poly):
        t.forward(2 * b)
        t.left(turn_angle_deg)

    t.up()  # 터틀 펜 들기
    t.home()  # 터틀 홈(0,0)으로 돌아가기
    t.down()  # 터틀 펜 내리기
    t.color('black')  # 터틀 색상 "black"을 설정


# 터틀 호출 함수 T로 설정
t = turtle.Turtle()

# 터틀 컨버스 크기 지정
turtle.setup(800, 800)

# 터틀 제목 설정 (다각형 그리기)
turtle.title("Drawing polygon")

# 터틀 모양 설정 (거북이)
t.shape("turtle")

# 터틀 색상 설정
t.color("black")

# 터틀 너비 설정
t.width(3)

# 현재위치의 지름 10의 빨간색 원 그리기
t.dot(10, "red")

# 현재위치를 캔버스에 표시
t.write(t.pos())

# L_polygons 튜플 리스트 구성
L_polygons = [(3, 100, -200, 200), (4, 100, 200, 200),
              (5, 100, -200, -200), (6, 100, 200, -200)]

# for-loop을 사용한 함수 호출
for i in range(len(L_polygons)):
    n_p, r, cx, cy = L_polygons[i]
    draw_polygon(t, n_p, r, cx, cy)

t.up()  # 터틀 펜 들기
t.home()
t.down()
t.color("black")
