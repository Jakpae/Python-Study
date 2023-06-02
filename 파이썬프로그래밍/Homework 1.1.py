# Homework 1.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 7, 2023
# Major features :
# - input radius
# - calculate circle area and circumference

from math import *


# 문제 번호, 학번, 이름 출력
print("Homework 1.1 , 학번: 22312050 , 이름: 이승준")

# 반지름 입력
radius_str = input("원의 반지름(radius)을 입력해주세요 = ")
radius = int(radius_str)

# 원의 넒이 (area) 및 원둘레 (circumference) 계산
area = radius * radius * pi
circumference = radius * 2 * pi

# 원의 넒이 및 원둘레 출력
print("원의 반지름({}) : 원의 넒이 ({}) , 원둘레 ({})".format(radius, area, circumference))
