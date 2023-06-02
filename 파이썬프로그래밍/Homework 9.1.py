# Homework 9.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 11, 2023

# 그림을 그리기 위한 turtle 모듈과 다각형의 자료를 가져오고 그리는 TurtleDrawings_classPolygon 함수 Import
import turtle
from TurtleDrawings_classPolygon import *

# 만약 name이 main이라면 실행
if __name__ == "__main__":
    turtle.setup(800, 800)
    # 터틀 타이틀 설정
    turtle.title("HW9.1 Application of user-defined module TurtleDrawings with class Polygon") 
    t = turtle.Turtle()
    t.shape("classic")
    
    # turtle_drawings.txt 파일에서 read모드로 자료를 가져옴
    fin = open("turtle_drawings.txt", 'r')
    L_drawings = fget_drawings(fin)
    fin.close()
    
    # 다각형 그리는 for 반복문
    for polygon in L_drawings:
        print(polygon)
        polygon.turtle_draw(t)