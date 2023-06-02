# Homework 2.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 9, 2023
# Major features :
# - Calculate Right Triangle diagonal perimeter area

# 직각삼각형의 밑변과 높이를 실수 float 으로 입력받음
base = float(input("직각삼각형의 밑변을 입력해주세요 = "))
height = float(input("직각삼각형의 높이를 입력해주세요 = "))

# 넒이 대각선 둘레 계산
area = base * height / 2
diagonal = ((base ** 2)+(height ** 2)) ** 0.5
perimeter = base + height + diagonal

# 직각삼각형의 밑변 높이 넒이 대각선 둘레 출력
print("직각삼각형의 밑변 = {: .2f} 높이 = {: .2f} : 넒이 = {: .2f}, 대각선 = {: .2f}, 둘레 = {: .2f}".format(
    base, height, area, diagonal, perimeter))
