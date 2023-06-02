# Class_StopWatch
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 11, 2023

# 시간을 귀하기 위한 time 모듈과 스톱워치 구현을 위한 tkinter 모듈 import
import time
from tkinter import *

# 스톱워치를 사용하는데 사용되는 데이터 멤버들의 초기값을 설정 및 구현
class StopWatch():
    def __init__(self, window):
        self.window = window
        # 프로그램 타이틀 설정
        self.frame = LabelFrame(window, text="My Simple Stop Watch", relief=GROOVE)
        self.frame.grid(row=0, column=0)
        self.start_time = time.time()
        self.stop_time = time.time()
        self.elapsed_time = 0.0
        self.prev_elapsed_time = 0.0
        self.running = False
        self.timeText = Label(self.frame, height = 5, text="{:>7s}".format("0.000"), font=("Arial 40 bold"))
        self.timeText.pack(side = TOP)
        # Start, Stop , Reset 버튼 설정 및 구현
        self.startButton = Button(self.frame, width=10, text="Start", bg="green", command=self.start)
        self.startButton.pack(side = LEFT)
        self.stopButton = Button(self.frame, width=10, text="Stop", bg="red", command=self.stop)
        self.stopButton.pack(side = LEFT)
        self.resetButton = Button(self.frame, width=10, text="Reset", bg="yellow", command=self.reset)
        self.resetButton.pack(side = LEFT)
    

    # running 상태가 True 면 시간이 증가하고 증가한 누적 시간을 표시하는 runTimer 함수 
    def runTimer(self):
        if self.running == True:
            self.cur_time = time.time()
            time_diff = self.cur_time - self.start_time
            self.elapsed_time = time_diff +  self.prev_elapsed_time
            self.timeText.configure(text="{:7.3f}".format(self.elapsed_time))
            # 10ms마다 자기 자신을 호출
        self.window.after(10,self.runTimer)
    
    # start버튼이 눌러졌을때 호출되며 runtimer가 실행되게 하는 start함수
    def start(self):
        if (self.running != True):
            self.running = True
            self.start_time = time.time()
            self.prev_elapsed_time = self.elapsed_time
    
    # stop 버튼이 눌러졌을때 호출되며 stop watch를 중단시켜 시간 증가를 중단 시키는 stop 함수 
    def stop(self):
        self.running = False
        self.prev_elapsed_time = self.elapsed_time
    
    # Reset 버튼이 눌러졌을 때 호출되며, 전체 누적 시간을 0.0 으로 초기화 시키는 reset 함수
    def reset(self):
        self.running = False
        self.elapsed_time = 0.0
        self.prev_elapsed_time = 0.0
        self.timeText.configure(text="{:>7s}".format("0.000"))