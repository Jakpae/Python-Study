# Homework Homework 2.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 9, 2023
# Major features :
# - input sphere radius
# - calcucate sphere surface , sphere volume

import math

# 구 반지름 입력 int로 받
radius = int(input("구의 반지름을 입력해주세요 = "))

# 구의 표면적 구하기
volume = 4 / 3 * math.pi * (radius ** 3)

# 구의 체적 구하
surface_area = 4 * math.pi * (radius ** 2)

# 구의 반지름 표면적 체적 출력
print("구의 반지름 = ({}) : 구의 표면적 = {}, 구의 체적 = {}".format(
    radius, volume, surface_area))
