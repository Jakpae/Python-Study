# 실습 3.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 16, 2023
# Major features :
# - Draw Polygons with trutle

# 다각형을 그리기 위한 Turtle 모듈과 수학적 계산을 위한 Math 모듈 Import
import turtle
import math

# 터틀 호출 함수 T로 변환
t = turtle.Turtle()

# 터틀 컨버스 크기 지정
turtle.setup(800, 800)

# 터틀 제목 설정 (다각형 그리기)
turtle.title("다각형 글기")

# 터틀 모영 설정 (거북이)
t.shape("turtle")

# 터틀 색상 설정
t.color("black")

# 터틀 너비 설정
t.width(3)

# 현재위치의 지름 10의 빨간색 원 그리기
t.dot(10, "red")

# 현재위치를 캔버스에 표시
t.write(t.pos())

# While 무한반복문
while True:
    
    # 꼭지점 개수 반지름 Cx,Cy를 리스트로 입력받고 Split을 이용해 나눈후 Map을 이용해 실수형 자료로 입력
    n_poly, radius, cx, cy = map(int, input(
        "꼭지점 개수, 반지름, Cx, Cy를 입력해주세요 : ").split())

    #  0을 입력하면 While 무한반복문 종료
    if n_poly == 0:
        break

    # 터틀 팬 들기
    t.up()

    # 밑에 글자를 적기 위해 이동
    t.goto((cx - radius, cy - radius - 20))

    # 각형의 수, 반지름, Cx, Cy 적기
    t.write("n_poly({}), radius ({}), cx({}), cy({})".format(
        n_poly, radius, cx, cy))

    # 터틀 팬 들기
    t.up()

    # 터틀 Cx,Cy로 이동
    t.goto((cx, cy))

    # 터틀 팬 놓기
    t.down()

    # 터틀 현재 위치에 파란색으로 된 지름 10의 원 그리기
    t.dot(10, "blue")

    # 터틀의 현재위치를 컨버스에 적기
    t.write(t.pos())

    # 터틀 팬 들기
    t.up()

    # 터틀 Cx, Cy-radius로 이동
    t.goto((cx, cy-radius))

    # 터틀 팬 놓기
    t.down()

    # 터틀 팬 너비 2로 설정
    t.width(2)

    # 팬 색상 블루로 설정
    t.color("blue")

    # 현재위치에 Radius를 반지름으로 한 원 그리기
    t.circle(radius)

    # 다각형의 한 각을 구하기 위해 360 / n_poly를 하여서 다각형의 한 각을 계산
    turn_angle_deg = 360 / n_poly
    theta_rad = (math.pi - math.pi * 2 / n_poly) / 2
    
    # 다각형의 높이 구하기
    h = radius * math.sin(theta_rad)
    b = radius * math.cos(theta_rad)

    sx = cx - b
    sy = cy - h

    # 터틀 팬 들기
    t.up()

    # 터틀 Sx , Sy 이동
    t.goto(sx, sy)

    # 터틀 팬 놓기
    t.down()

    # 터틀 현재 위치에 지름 10의 파란색 원 그리기
    t.dot(10, "blue")

    # 터틀 현재 위치 캔버스에 펴시
    t.write(t.pos())

    # 터틀 팬 너비 5
    t.width(5)

    # 터틀 팬 색상 빨강 설정
    t.color("red")

    # N각형의 모형 그리기
    for i in range(n_poly):
        t.forward(2 * b)
        t.left(turn_angle_deg)

    # 터틀 팬 들기
    t.up()

    # 터틀 홈(0,0)으로 아동
    t.home()

    # 터틀 팬 들기
    t.down()

    # 터틀 팬 색상 검정 설정
    t.color("black")
