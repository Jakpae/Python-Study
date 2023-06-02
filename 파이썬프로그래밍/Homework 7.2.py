# Homework 7.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 16, 2023
# - Implementing class Mtrx in the custom module Class_Mtrx.py

# 행렬의 덧셈, 뺄셈, 곱셈 연산을 연산자 오버로딩 기능을 사용할 수 있게 하는 사용자 정의모듈 Class_Mtrx 모듈 import
from Class_Mtrx import *

# # 모듈을 임포트할 때 코드가 실행되지 않도록 하기 위해, 모듈을 입포트할 때는 해당 모듈의 코드가 실행되기 때문에
# if __name__ == "__main__" 을 사용하면 모듈을 실행할 때와 임포트할 때의 동작을 구분 할 수 있다.
if __name__ == "__main__":
    
    # LA 리스트 생성
    LA = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # LB 리스트 생성
    LB = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    
    # LC 리스트 생성
    LC = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    
    # LA리스트를 3열 5행의 행렬로 만든후 mA로 설정
    mA = Mtrx("mA", 3, 5, LA)
    print(mA)
    
    # LB리스트를 3열 5행의 행렬로 만든후 mB로 설정
    mB = Mtrx("mB", 3, 5, LB)
    print(mB)
    
    # LB리스트를 5열 3행의 행렬로 만든후 mC로 설정
    mC = Mtrx("mC", 5, 3, LC)
    print(mC)
    
    # Class_Mtrx의 __add__ 를 사용해서 mA 와 mB 의 합을 구한후 mD로 설정
    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD)
    mE = mA - mB
    mE.setName("mE = mA - mB")
    print(mE)
    mF = mA * mC
    mF.setName("mF = mA * mC")
    print(mF)