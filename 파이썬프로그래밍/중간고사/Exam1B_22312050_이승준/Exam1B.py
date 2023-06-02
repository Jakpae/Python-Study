# Exam1B
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

# 계산을 위한 math 그림을 그리기 위한 turtle MyturtleDrawings 모듈 import
import math
import turtle
from MyTurtleDrawings import *

def main():
    # 캔버스 크기 설정 및 함수호출 t 설정 그리고 터틀 모양 호살표 설정
    turtle.setup(800,800)
    turtle.title("2023-1 컴싸파Exam1B 학번: 22312050, 성명: 이승준")
    t = turtle.Turtle()
    t.shape("classic")
    t.width(3)

    # 출력할 모양 리스트 생성
    L_drawings = [(-250, 250, "star", 50, "red"), (0, 250, "square", 50, "green"),\
        ( 250, 250, "pentagon", 50, "blue"), (-250, 0, "hexagon", 50, "navy"),\
            ( 0, 0, "heptagon", 50, "brown"), ( 250, 0, "octagon", 50, "darkred"),\
                (-250, -250, "nonagon", 50, "orange"), ( 0, -250, "decagon", 50, "magenta"),\
                    ( 250, -250, "circle", 50, "red")]

    # 도형을 그리는 for 반복문 만약 이름이 별이면 별을 그리고 아니라면 다각형 그리기 실행
    for drawing in L_drawings:
        shape_name, color = drawing[2], drawing[4]
        cx, cy, radius = drawing[0], drawing[1], drawing[3]
        print("drawing a {} {} at ({}, {}), circumcircle_radius ({})".format(color, shape_name, cx, cy, radius))
        if shape_name == "star":
            drawStar(t, (cx, cy), radius, color)
        else:
            num_vertex = getNumVertex(shape_name)
            drawPolygon(t, (cx, cy), num_vertex, radius, color)

if __name__ == "__main__":
    main()
