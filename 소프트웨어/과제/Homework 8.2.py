# Homwork 8.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 3, 2023
# Major features :
# - Create an instance mA and mB, one 5 x 3 class Mtrx instance mC randomly
# - Calculate and output mD = mA + mB, mE = mA – mB, mF = mA * mC

# 행렬의 계산을 위한 Class_Mtrx 모듈 Import
from MyPyPackage.Class_Mtrx import *

if __name__ == "__main__":
    # 3개의 리스트 LA,LB,LC 설정
    LA = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\
        11, 12, 13, 14, 15]
    LB = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0,\
        0, 0, 1, 0, 0]
    LC = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    
    # mA에 lA리스트의 값을 3,5의 크기의 행렬로 넣음
    mA = Mtrx("mA", 3, 5, LA)
    print(mA)
    
    # mB에 lB리스트의 값을 3,5의 크기의 행렬로 넣음
    mB = Mtrx("mB", 3, 5, LB)
    print(mB)
    
    # mC에 lC리스트의 값을 5,3의 크기의 행렬로 넣음
    mC = Mtrx("mC", 5, 3, LC)
    print(mC)
    
    # mD를 mA + mB의 값으로 설정
    mD = mA + mB
    # mD의 이름을 "mD = mA + mB"로 설정
    mD.setName("mD = mA + mB")
    # mD 출력
    print(mD)
    
    # mE를 mA - mB의 값으로 설정
    mE = mA - mB
    # mE의 이름을 "mD = mA - mB"로 설정
    mE.setName("mE = mA - mB")
    # mE 출력
    print(mE)
    
    # mF를 mA * mC의 값으로 설정
    mF = mA * mC
    # mF의 이름을 "mF = mA * mB"로 설정
    mF.setName("mF = mA * mC")
    # mF 출력
    print(mF)