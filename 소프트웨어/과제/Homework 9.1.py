# Homwork 9.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 7, 2023

# txt파일에서 행렬값을 받아오는 함수와 행렬을 출력 계산하는 함수를 가지고있는 Class_Mtrx_fgetMtrx 모듈 Import
from Class_Mtrx import *

# 메인함수 생성
def main():
    # matrix_ABC.txt파일에서 행렬값을 read 모드로 받아옴
    fin = open("matrix_ABC.txt", "r")
    # fgetMtrx함수에서 mA를 받아옴
    mA = fgetMtrx(fin)
    # mA 이름 mA로 설정
    mA.setName("mA")
    # mA 출력
    print(mA)

    # fgetMtrx함수에서 mB를 받아옴
    mB = fgetMtrx(fin)
    # mB 이름 mB로 설정
    mB.setName("mB")
    # mB 출력
    print(mB)
    
    # fgetMtrx함수에서 mC를 받아옴
    mC = fgetMtrx(fin)
    # mC 이름 mC로 설정
    mC.setName("mC")
    # mC 출력
    print(mC)
    
    # fin 종료
    fin.close()
    
    # mA + mB를 mD로 설정
    mD = mA + mB
    # mD의 이름을 mD = mA + mB로 설정
    mD.setName("mD = mA + mB")
    # mD 출력
    print(mD)
    
    # mA - mB를 mE로 설정
    mE = mA - mB
    # mE의 이름을 mE = mA - mB로 설정
    mE.setName("mE = mA - mB")
    # mE 출력
    print(mE)
    
    # mA * mC를 mF로 설정
    mF = mA * mC
    # mF의 이름을 mF = mA * mB로 설정
    mF.setName("mF = mA * mC")
    # mF 출력
    print(mF)

# name이 main이라면 main()실행
if __name__ == "__main__":
    main()