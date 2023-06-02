# Homework 3.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 18, 2023
# Major features :
# - Print 12 x 12 Multiplication Table


# 12 X 12 Multiplication Table 출력
print("12 X 12 Multiplication Table")

# Y = 1 설정후 While 문이 끝나면 1이 증가되고 12가 되면 끝나는 While문 생성
y = 1
while y <= 12:
    # X = 1 설정후 While 문이 끝나면 1이 증가하고 12가 되면 끝나는 While문 생성
    x = 1
    while x <= 12:
        xy = x * y

        # rjust(10)을 사용해 우측 정렬하고 출력
        print(f" {y:2d} X {x:2d} = {xy:3d},".rjust(10), end=' ')
        x += 1
    print()
    y += 1
