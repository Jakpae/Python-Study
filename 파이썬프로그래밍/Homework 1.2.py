# Homework 1.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 7, 2023
# Major features :
# - turtle drawing of rectangle

import turtle

# 직사각형 가로,세로 입력
width_str = input("직사각형의 가로(width)를 입력해주세요 = ")
length_str = input("직사각형의 세로(length)를 입력해주세요 = ")
width = int(width_str)
length = int(length_str)

t = turtle.Turtle()

# 모양 설정
t.shape("turtle")

# 색상 설정
t.color("blue")

# 너비 설정
t.width(2)

# 속도 설정
t.speed(1)

#(0,0)이동
t.goto(0, 0)

# 현재 위치 표시
t.dot("red")
t.write(t.pos())
t.up()

# 직사각형 꼭지점 위치 설정
loc11 = width / 2
loc12 = length / 2

loc21 = width / 2
loc22 = -(length / 2)

loc31 = -(width / 2)
loc32 = -(length / 2)

loc41 = -(width / 2)
loc42 = (length / 2)

# 직사각형 그리기
t.goto(loc11, loc12)
t.down()
t.write(t.pos())
t.goto(loc21, loc22)
t.write(t.pos())
t.goto(loc31, loc32)
t.write(t.pos())
t.goto(loc41, loc42)
t.write(t.pos())
t.goto(loc11, loc12)
