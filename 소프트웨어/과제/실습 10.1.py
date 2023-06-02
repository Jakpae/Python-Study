# 실습 10.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 18, 2023
# Major features :

from tkinter import *

# Max Speed와 Initial Speed , Canvas_Width, Canvas_Height 설정
MAX_SPEED = 100
INITIAL_SPEED = 5
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300

# 애니메이션 구현을 위한 Class_BouncingBallSimulator 모듈 Import
from Class_BouncingBallSimulator import *

# 만약 __name__ 이 __main__ 이라면 실행
if __name__ == '__main__':
    window = Tk()
    # tkinter의 title을 Simulator_BouncingBall로 설정
    window.title("Simulator_BouncingBall") 
    sim_animation = BouncingBallSimulator(window, CANVAS_WIDTH,\
        CANVAS_HEIGHT, MAX_SPEED, INITIAL_SPEED)
    sim_animation.animate()
    mainloop()