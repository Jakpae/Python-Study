# Homework 4.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 23, 2023
# Major features :
# -  Calculate Matrix A + Matrix B
# -  Calculate Matrix A - Matrix B


# 2차원 리스트 mA, mB 생성
mA = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
mB = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]

# 2차원 리스트 mA출력
print("mA =")
a_row, a_col = len(mA), len(mA[0])
for r in range(a_row):
    for c in range(a_col):
        print("{:3d}".format(mA[r][c]), end='')
    print()

# 2차원 리스트 mB출력
print("mB =")
b_row, b_col = len(mB), len(mB[0])
for r in range(b_row):
    for c in range(b_col):
        print("{:3d}".format(mB[r][c]), end='')
    print()

# 행렬의 합 구하는 식
mC = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for r in range(3):
    for c in range(5):
        mC[r][c] = mA[r][c] + mB[r][c]

# mA와 mB의 합 출력
print("mA + mB =")
for r in range(3):
    for c in range(5):
        print("{:3d}".format(mC[r][c]), end='')
    print()

# 행렬의 차 구하는 식
mC = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for r in range(3):
    for c in range(5):
        mC[r][c] = mA[r][c] - mB[r][c]

# mA와 mB의 차 출력
print("mA - mB =")
for r in range(3):
    for c in range(5):
        print("{:3d}".format(mC[r][c]), end='')
    print()
