# 실습 4.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 22, 2023
# Major features :
# - Fuctions for matrix operations

# mA, mB 리스트 생성
mA = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
mB = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0]]

# mA 출력
print("mA = ")
n_row, n_col = len(mA), len(mA[0])
for r in range(n_row):
    for c in range(n_col):
        print("{:3d}".format(mA[r][c]), end='')
    print()

# mB 출력
print("mB = ")
n_row, n_col = len(mB), len(mB[0])
for r in range(n_row):
    for c in range(n_col):
        print("{:3d}".format(mB[r][c]), end='')
    print()

# 행렬의 곱인 mR을 계산하는 계산식
mR = []
for r in range(len(mA)):
    mR_row = []
    for c in range(len(mB[0])):
        mR_rc = 0
        for k in range(len(mB)):
            mR_rc += mA[r][k] * mB[k][c]
        mR_row.append(mR_rc)
    mR.append(mR_row)

# 위에서 구한 행렬의 곱을 출력
print("mA * mB = ")
n_row, n_col = len(mR), len(mR[0])
for r in range(n_row):
    for c in range(n_col):
        print("{:3d}".format(mR[r][c]), end='')
    print()
