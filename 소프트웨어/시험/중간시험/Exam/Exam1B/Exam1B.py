#Exam1A
#Name : LeeSeungJun
#St_id : 22312050

import math
import turtle
from MyTurtleDrawings import *

def main():
    # 캔버스 크기 설정 및 함수호출 t 설정 그리고 터틀 모양 호살표 설정
    turtle.setup(800,800)
    turtle.title("2023-1 SW&AI_Exam1B 학번: 22312050, 성명: 이승준")
    t = turtle.Turtle()
    t.shape("classic")
    t.width(3)

    # 출력할 모양 리스트 생성
    shapes = [("triangle", -250, 250, 50, "red"), ("square", 0, 250, 50, "green"),\
         ("pentagon", 250, 250, 50, "blue"), ("hexagon", -250, 0, 50, "red"),\
              ("heptagon",0,0,50,"green"),("octagon",250,0,50,"magenta"),("noagon",-250,-250,50,"red"),\
                  ("decagon",0,-250,50,"green"),("circle",250,-250,50,"orange")]

    # 도형을 그리는 for 반복문
    for shape in shapes:
        sh_name = shape[0]
        n_poly = getNumVertices(sh_name)
        sh_name, cx, cy, radius, color = shape[0], int(shape[1]), int(shape[2]), int(shape[3]), shape[4]
        draw_polygon(t,n_poly,cx,cy,radius,color)

    # 0,0 으로 돌아오는 t.home()
    t.up()
    t.home()
    t.down()

if __name__ == "__main__":
    main()
