# Class_USD_KRW_ExchangeCalculator
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 11, 2023

from math import *
from tkinter import *


class USD_KRW_ExchangeCalculator():
    def __init__(self, master):
        # GROOVE 모양의 테두리로 LabelFrame을 만들고 text를 USD_KRW_Calculator로 설정
        frame = LabelFrame(master, text="USD_KRW Exchange Calculator", relief=GROOVE)
        frame.pack()
        # 실수로 표현하기 위한 DoubleVar
        self.USD_KRW_Ratio = DoubleVar()
        # 미국달러에 대한 한국 원화의 환율을 입력하는 Entry 와 Label
        Label(frame, text = 'Exchange Ratio (1 USD => x KRW)').grid(row=0, column=0)
        Entry(frame, textvariable=self.USD_KRW_Ratio, justify=RIGHT).grid(row=0, column=1)
        # 미국 달러 금액에 대한 Label
        us_dollar_label = Label(frame, text = 'US Dollar')
        us_dollar_label.grid(row=1, column=0)
        # 실수로 표현하기 위한 DoubleVar
        self.us_dollar_var = DoubleVar()
        # 미국 달러 금액을 입력/출력하는 Entry
        us_dollar_entry = Entry(frame, textvariable=self.us_dollar_var, justify=RIGHT)
        us_dollar_entry.grid(row=1, column=1)
        # 한국 원화 금액에 대한 Label
        us_won_label = Label(frame, text = 'Korean Won')
        us_won_label.grid(row=2, column=0)
        # 실수로 표현하기 위한 DoubleVar
        self.us_won_var = DoubleVar()
        # 한국 원화 금액을 입력/출력하는 Entry
        us_won_entry = Entry(frame, textvariable=self.us_won_var, justify=RIGHT)
        us_won_entry.grid(row=2, column=1)
        # US Dollar -> Kr Won 초록색 버튼 구현
        button_USD_KRW = Button(frame, text='US Dollar -> Kr Won', command=self.convert_USD_KRW, bg="green")
        button_USD_KRW.grid(row=3, column=0)
        # Kr Won -> US Dollar 노랑색 버튼 구현
        button_KRW_USD = Button(frame, text='Kr Won -> US Dollar', command=self.convert_KRW_USD, bg="yellow")
        button_KRW_USD.grid(row=3, column=1)

    # US Dollar -> Kr Won 초록색 버튼을 누르면 실행되는 달러를 원화로 바꿔주는 함수
    def convert_USD_KRW(self):
        currency_ratio = self.USD_KRW_Ratio.get()
        usd = self.us_dollar_var.get()
        krw = usd * currency_ratio
        krw_round = round(krw, 2)
        self.us_won_var.set(krw_round)
    
    # Kr Won -> US Dollar 노랑색 버튼을 누르면 실행되는 원화를 달러로 바꿔주는 함수
    def convert_KRW_USD(self):
        currency_ratio = self.USD_KRW_Ratio.get()
        krw = self.us_won_var.get()
        usd = krw/currency_ratio
        usd_round = round(usd, 2)
        self.us_dollar_var.set(usd_round)