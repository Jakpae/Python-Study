# Homework 9.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 11, 2023

# 시간을 구하기 위한 time 모듈과 스톱워치 구현을 위한 tkinter , Class_StopWatch 모듈 Import
import time
from tkinter import *
from Class_StopWatch import *

# 만약 name이 main이라면 실행
if __name__ == '__main__':
    # 스톱워치 실행 코드
    win = Tk()
    stop_watch = StopWatch(win)
    stop_watch.runTimer()
    win.mainloop()