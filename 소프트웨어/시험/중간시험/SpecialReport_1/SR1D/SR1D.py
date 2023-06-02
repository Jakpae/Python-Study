# SR1D
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - Print your student number and name at the beginning of the program output

# 사용자 지정 모듈 MyMtrx Import
from MyMtrx import *

# Main 함수 생성
def main():

    # 2차원 리스트 mA,mB,mC 생성
    mA = [[1,2,3,4,5],[6,7,8,9,10],[11,12,12,14,15]]
    mB = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,1,1]]
    mC = [[1,0,0],[0,1,0],[0,0,1],[0,0,0],[0,0,0]]
    
    # 신상정보 출력
    print("2023-1 SW&AI_SR1D 학번:22312050, 성명: 이승준")

    # MyMtrx 모듈안에 있는 printMtrx를 사용해 mA,mB,mC 출력
    printMtrx("mA", mA)
    printMtrx("mB", mB)
    printMtrx("mC", mC)

    # mD는 mA,mB의 합이라고 설정 및 mD출력
    mD = addMtrx(mA,mB)
    printMtrx("mD = mA + mB", mD)

    # mE는 mA,mB의 차라고 설정 및 mE출력
    mE = subMtrx(mA,mB)
    printMtrx("mE = mA - mB", mE)

    # mF는 mA,mC의 곱이라고 설정 및 mF출력
    mF = mulMtrx(mA,mC)
    printMtrx("mF = mA * mC", mF)

# 만약 name이 main이라면 실행
if __name__ == "__main__":
    main()