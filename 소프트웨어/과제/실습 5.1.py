# 실습 5.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 30, 2023
# Major features :
# - Create print_mtrx function
# - Print matrix mA,mB,mC
# - Calculate matrix addition , subtraction, multiplication
# - Print matrix addition, subraction, multiplication

# print_mtrx 함수 생성
def print_mtrx(mtrx_name, M):
    print("{} = ".format(mtrx_name))
    for r in range(len(M)):
        for c in range(len(M[0])):
            print("{:3d}".format(M[r][c]), end='')
        print()

# 2차원 리스트 mA,mB,mC 생성
mA = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]  # 3 x 5
mB = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]  # 3 x 5
mC = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0]]  # 5 x 3

# print_mtrx 함수를 이용해서 행렬 mA,mB,mC 출력
print_mtrx("mA", mA)
print_mtrx("mB", mB)
print_mtrx("mC", mC)

# mA,mB 행렬의 합 계산
mR = []
for r in range(len(mA)):
    mR_row = []
    for c in range(len(mA[0])):
        mR_row.append(mA[r][c] + mB[r][c])
    mR.append(mR_row)
print_mtrx("mA + mB", mR)

# mA,mB 행렬의 차 계산
mR = []
for r in range(len(mA)):
    mR_row = []
    for c in range(len(mA[0])):
        mR_row.append(mA[r][c] - mB[r][c])
    mR.append(mR_row)

print_mtrx("mA - mB", mR)

# mA,mC 행렬의 곱 계산
mR = []
for r in range(len(mA)):
    mR_row = []
    for c in range(len(mC[0])):
        mR_rc = 0
        for k in range(len(mC)):  # len(mC) == len(mA[0])
            mR_rc += mA[r][k] * mC[k][c]
        mR_row.append(mR_rc)
    mR.append(mR_row)

print_mtrx("mA * mC", mR)
