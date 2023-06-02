# MyMtrx
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - Generate functions that output a matrix and output the sum, difference, and product of the matrix

# 리스트의 값을 출력하기 위한 printMtrx함수
def printMtrx(name, L):
    print("{} = ".format(name))
    for r in range(len(L)):
        for c in range(len(L[0])):
            print("{:4d}".format(L[r][c]),end='')
        print()
    
# 행렬의 합을 계산하는 addMtrx 함수 생성
def addMtrx(L1,L2):
    mR = []
    for r in range(len(L1)):
        mR_row = []
        for c in range(len(L1[0])):
            mR_row.append(L1[r][c] + L2[r][c])
        mR.append(mR_row)
    return mR

# 행렬의 차를 계산하는 subMtrx 함수 생성
def subMtrx(L1,L2):
    mR = []
    for r in range(len(L1)):
        mR_row = []
        for c in range(len(L1[0])):
            mR_row.append(L1[r][c] - L2[r][c])
        mR.append(mR_row)
    return mR

# 행렬의 곱을 계산하는 mulMtrx 함수 생성
def mulMtrx(L1,L2):
    mR = []
    for r in range(len(L1)):
        mR_row = []
        for c in range(len(L2[0])):
            mR_rc = 0
            for k in range(len(L2)):
                mR_rc += L1[r][k] * L2[k][c]
            mR_row.append(mR_rc)
        mR.append(mR_row)
    return mR