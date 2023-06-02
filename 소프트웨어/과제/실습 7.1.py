# 실습 7.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 14, 2023
# Major features :
# - Prepare a custom module, draw circles and polygons using turtle graphics, and then implement functions
# = Organize shape information into a tuple list

# 사용자 정의 모듈 MyTurtleDrwaings.py를 준비, 터틀 그래픽을 사용하여 원 및 다각형을 그리는 함수 구현
from MyPyPackage.myModules import MyTurtleDrawings
import sys
import turtle  # 도형을 그리기 위한 터틀 모듈 import

# myPyPackage 위치 설정 및 디렉터리 경로들이 기록된 문자열 리스트 sys.path 위치 설정
myPyPackage_dir = "/Users/leeseungjun/Library/CloudStorage/GoogleDrive-jfldjd@yu.ac.kr/내 드라이브/소프트웨어와인공지능/실습,과제/MyPyPackage"
sys.path.append(myPyPackage_dir)


def main():
    turtle.setup(600, 400)  # 터틀 컨버스 크기 600,400으로 설정
    # 터틀 프로그램 실행시 뜨는 프로그램 이름 설정
    turtle.title("Drawing polygons with user-defined module")
    t = turtle.Turtle()  # t를 터틀 호출 함수로 설정
    t.shape("classic")  # 터틀 모양 클래식(화살표)
    # 그리는 도형의 타입과 각 , 중심각 , 한 변의 길이 , 색상 설정
    shapes = [("polygon", 3, -200, 100, 100, "red"), ("polygon", 4, 0, 100, 100, "green"),
              ("circle", 200, 100, 50, "blue"), ("star", -200, -100, 100, "orange")]
    # len(shapes) 즉 그리는 도형의 수만큼 반복되는 반복문 for
    for i in range(len(shapes)):
        # 도형의 타입 설정
        shape_type = shapes[i][0]
        # 만약 도형의 타입이 polygon이라면 MyTurtleDrawings 모듈에 있는 drawPolygon 함수 실행
        if shape_type == "polygon":
            st, num_vertices, center_x, center_y, line_length, color = shapes[i]
            MyTurtleDrawings.drawPolygon_Turtle(
                t, num_vertices, center_x, center_y, line_length, color)
        # 만약 도형의 타입이 circle이라면 MyTurtleDrawings 모듈에 있는 drawCircle 함수 실행
        elif shape_type == "circle":
            st, center_x, center_y, radius, color = shapes[i]
            MyTurtleDrawings.drawCircle_Turtle(
                t, center_x, center_y, radius, color)
        # 만약 도형의 타입이 star라면 MyTurtleDrawings 모듈에 있는 drawStar 함수 실행
        elif shape_type == "star":
            st, center_x, center_y, length, color = shapes[i]
            MyTurtleDrawings.drawStar_Turtle(
                t, center_x, center_y, length, color)
        # 만약 도형의 타입이 존재하지 않는다면 Error 코드 출력
        else:
            print("Error - the shape ({}) is not supported yet !!!".format(shape_type))
    t.up()  # 터틀 펜 들기
    t.home()  # 터틀 홈(0,0)으로 이동
    t.down()  # 터틀 펜 내리기


# MyTurtleDrawings 파일의 drawPolygon,drawCircle,drawStar 함수를
# import 시켜 사용하기 위한 if __name__ == "__main__"
# __name__ 변수의 값이 __main__ 인지 확인하는 이유는 프로그램의 시작점이 맞는지 판단하는 작업이다
# 즉 파일이 메인 프로그램으로 사용될 때와, 모듈로 사용될 때를 구분하기 위한 용도이다
# 모듈을 임포트할 때 코드가 실행되지 않도록 하기 위해, 모듈을 입포트할 때는 해당 모듈의 코드가 실행되기 때문에
# if __name__ == "__main__" 을 사용하면 모듈을 실행할 때와 임포트할 때의 동작을 구분 할 수 있다.
if __name__ == "__main__":
    main()
