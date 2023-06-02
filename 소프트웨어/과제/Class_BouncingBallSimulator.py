# Class_BouncingBallSimulator
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 18, 2023
# Major features :

from tkinter import *


class BouncingBallSimulator():
    def __init__(self, win, canvas_width, canvas_height, ball_speed_limit, initial_speed):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_speed_limit = ball_speed_limit
        self.radius = 50
        self.speed = initial_speed
        self.dx, self.dy = -1, -1
        self.radius_var = IntVar()
        self.speed_var = IntVar()
        cx, cy = 50, 50 
        self.ball_pos_x = cx
        self.ball_pos_y = cy
        self.ball_pos_x_var = IntVar()
        self.ball_pos_y_var = IntVar()
        
        
        # LabelFram을 사용하여 시뮬레이션 파라미터 영역을 생성
        fr1 = LabelFrame(win, text="Simulation Parameters", bg="light green",bd=10, padx=5, pady=5, relief=GROOVE)
        fr1.grid(row=0, column=0)
        Label(fr1, text="ball speed control", width=15).grid(row=0, column=0)
        # 공의 속도를 조절하는 바에 대한 Frame
        scale_speed = Scale(fr1, length = 250, from_= initial_speed, to= ball_speed_limit,orient= HORIZONTAL, command=self.updateSpeed)
        scale_speed.grid(row=0, column=1)
        # 공의 속도를 표시하는 Frame
        Entry(fr1, textvariable=self.speed_var, justify='right').grid(row=0, column=2)
        self.speed_var.set(self.speed)
        # 프레임 모양 GROOVE로 설정
        fr2 = Frame(win, bg="white", relief=GROOVE)
        fr2.grid(row=1, column=0)
        self.canvas = Canvas(fr2, width=canvas_width, height=canvas_height, bd=0, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.create_oval(cx - self.radius/2, cy - self.radius/2, cx + self.radius/2, cy + self.radius/2, fill="red", tags="BouncingBall")
        # 현재위치를 표시해주는 Entry 생성과 글자 Label 생성 
        fr3 = LabelFrame(win, text="Ball Position", bg="light green", bd=10, padx=5, pady=5, relief=GROOVE)
        fr3.grid(row=2, column=0) 
        Label(fr3, text="ball pos_x", width=15).grid(row=0, column=0) 
        Entry(fr3, textvariable=self.ball_pos_x_var, justify='right').grid(row=0, column=1) 
        Label(fr3, text="ball pos_y", width=15).grid(row=0, column=2) 
        Entry(fr3, textvariable=self.ball_pos_y_var, justify='right').grid(row=0, column=3)
        
        # 속도 변화를 위한 함수 UpdataSpeed
    def updateSpeed(self, duty): 
        self.speed = int(duty)
        self.speed_var.set(self.speed * 2) 
        
        # 에니메이션 구현을 위한 함수 animate
    def animate(self): 
        self.canvas.move("BouncingBall", self.dx, self.dy) 
        pos = self.canvas.coords("BouncingBall") 
        #print("coords of Ball : {}, {}, {}, {}".format(pos[0], pos[1], pos[2], pos[3])) 
        self.ball_pos_x_var.set(pos[0] + self.radius / 2) 
        self.ball_pos_y_var.set(pos[1] + self.radius / 2) 
        # 만약 공이 왼쪽 벽을 부딫치면 bounced by left board 출력
        # 왼쪽 벽에 닿으면 dx의 부호를 변경하여 공이 반대 반향으로 움직이도록 설정
        if pos[0] <= 2: # use margin 2 
            print("bounced by left board ")
            self.dx *= -1
        # 만약 공이 우측 벽을 부딫치면 bounced by right board 출력
        # 우측 벽에 닿으면 dx의 부호를 변경하여 공이 반대 반향으로 움직이도록 설정
        if pos[2] >= self.canvas_width: 
            print("bounced by right board")
            self.dx *= -1
        # 위쪽 벽에 닿으면 dy의 부호를 변경하여 공이 반대 방향으로 움직이도록 설정
        if pos[1] <= 2:
            self.dy *= -1
        # 만약 공이 아랫 벽을 부딫치면 bounced by bottom board 출력
        # 아래쪽 벽에 닿으면 dy의 부호를 변경하여 공이 반대 방향으로 움직이도록 설정
        if pos[3] >= self.canvas_height: 
            print("bounced by bottom board")
            self.dy *= -1
        self.canvas.update_idletasks() 
        self.canvas.update()
        # 애니메이션의 속도를 업데이트하고 animate() 함수를 재취적으로 호출하여 에니메이션 게속 반복
        self.canvas.after((self.ball_speed_limit - self.speed), self.animate)