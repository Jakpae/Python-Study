# Homework 10.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 11, 2023


# 에니메이션 구현을 위한 tkinter 모듈 import
from tkinter import * 

# 환율 계산기 구현을 위한 Class_USD_KRW_ExchangeCalculator 모듈 Import
from Class_USD_KRW_ExchangeCalculator import *

# 메인 함수 생성
def main():
    win = Tk()
    # 프로그램 title을 USD_KRW_Exchange Calculator로 설정
    win.wm_title('USD_KRW Exchange Calculator')
    app = USD_KRW_ExchangeCalculator(win)
    win.mainloop()
    
# __name__이 __main__ 이라면 실행
if __name__ == "__main__":
    main()
