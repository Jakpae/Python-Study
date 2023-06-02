# 실습 8.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 27, 2023
# Major features :
# - Draw Polygons with Turtle and Class_Drawing

# 그림을 그리기 위한 Class_Drawings 모듈 import 
from Class_Drawings import *

# 만약 name이 __main__ 라면 실행
if __name__ == "__main__":
    t = turtle.Turtle()
    t.width(3)
    # 다각형 2차원 리스트
    L_polygons = [(3, -300, 200, 100, 'Red'), (4, 0, 200, 100, "Blue"), (5, 300, 200, 100, "Green"),\
        (6, -300, -200, 100, "Red"), (7, 0, -200, 100, "Blue"), (8, 300, -200, 100, "Green")]
    for pg_data in L_polygons: 
        n_vert, cx, cy, radius, color = pg_data
        s = Polygon(n_vert, cx, cy, radius, color)
        s.turtle_draw(t)