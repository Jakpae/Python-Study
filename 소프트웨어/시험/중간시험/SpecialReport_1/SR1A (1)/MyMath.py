# MyMath
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - The first row (row) of the trigonometric table is the output of a deg value increasing in step_deg units from 0 to 360° (degree)
# - Each float data in the table of trigonometric functions is output up to 4 decimal places in a total of 8 spaces
# - The output format of the trigonometric table is tabular with '-' and '|' or '+'
# - The rows 2 to 4 of the trigonometric function table calculate the rad value, sin(rad) value, and cos(rad) value for the deg value, respectively Output to column position in turn

# 계산을 위한 math 함수 import
import math

# printinTrigonometricTable 함수 생성
def prinTrigonometricTable(step_deg):
    print(">>> Trigonmetric Table (step_deg = {}) <<<".format(step_deg))
    print("     deg|",end='')
    for i in range(0,361,step_deg):
        print("{:8d}".format(i),end='')
    print()
    
    # - 8번 출력 및 + 한번 출력
    print("-" * 8,end='')
    print("+",end='')

    # - 출력을 위한 tep 생성과 for 반복문 사용
    tep = int(360 / step_deg + 1)

    for i in range(tep):
        print("-" * 8,end='')
    print()

    # sin(rad) 줄 출력
    print("     rad|",end='')
    for i in range(0,361,step_deg):
        print("{:8.4f}".format(math.radians(i)),end='')
    print()

    # sin(rad) 줄 출력
    print("sin(rad)|",end='')
    for i in range(0,361,step_deg):
        print("{:8.4f}".format(math.sin(math.radians(i))),end='')
    print()

    # cos(rad) 줄 출력
    print("cos(rad)|",end='')
    for i in range(0,361,step_deg):
        print("{:8.4f}".format(math.cos(math.radians(i))),end='')
    print()
    print()
