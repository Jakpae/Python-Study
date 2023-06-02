# Exam1D
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

# 행렬 출력 및 계산을 위한 Class_Mtrx 모듈 import
from Class_Mtrx import *

def main():
    print("2023-1 컴사파Exam1D_22312050_이승준")
    # 3개의 행렬을 위한 1차원 리스트 La,Lb,lC준비 
    La = [0.0, 1.1, 2.2, 3.3, 4.4,\
        5.5, 6.6, 7.7, 8.8, 9.9,\
            10.1, 11.2, 12.3, 13.4, 14.5]
    Lb = [1.0, 0.0, 0.0, 0.0, 0.0,\
        0.0, 1.0, 0.0, 0.0, 0.0,\
            0.0, 0.0, 1.0, 0.0, 0.0]
    Lc = [1.0, 0.0, 0.0,\
        0.0, 1.0, 0.0,\
            0.0, 0.0, 1.0,\
                0.0, 0.0, 0.0,\
                    0.0, 0.0, 0.0]
    
    # Class Mtrx 인스탄스 mA,mB,C를 생성
    mA = Mtrx("mA", 3, 5, La)
    print(mA)
    mB = Mtrx("mB", 3, 5, Lb) 
    print(mB)
    mC = Mtrx("mC", 5, 3, Lc)
    print(mC)
    
    # mA와 mB의 합을 mD에 저장한 다음 출력
    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD)
    
    # mA와 mB의 차를 mE에 저장한 다음 출력
    mE = mA - mB
    mE.setName("mE = mA - mB")
    print(mE)
    
    # mA와 mC의 곱을 mF에 저장한 다음 출력
    mF = mA * mC
    mF.setName("mF = mA * mC")
    print(mF)
    
    # 행렬 mA의 전치행렬을 생성해 mG에 저장후 print 함수로 출력
    mG = mA.transpose()
    mG.setName("mG = mA.transpose()")
    print(mG)
    
if __name__ == "__main__":
    main()