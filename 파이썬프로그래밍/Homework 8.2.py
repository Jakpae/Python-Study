# Homework 8.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 4, 2023

# 행렬의 계산과 txt파일에서 read받은 데이터를 행렬로 만들어주는 함수가 존재하는 Class_Mtrx 를 Import
from Class_Mtrx import *

def main():
    # matrix_data.txt 파일을 read 상태로 open
    fin = open("matrix_data.txt", "r")
    # result.txt에 write 상태로 open
    fout = open("result.txt", "w")
    # mA에 fgetMtrx에서 구한 행렬을 입력
    mA = fgetMtrx(fin)
    # 행렬의 이름을 mA라 설정
    mA.setName("mA")
    # 행렬 mA 출력
    print(mA)
    # fout.write 를 사용해서 result.txt에 mA를 write
    fout.write("{}".format(mA))
    # mB에 fgetMtrx에서 구한 행렬을 입력
    mB = fgetMtrx(fin)
    # 행렬의 이름을 mB라 설정
    mB.setName("mB")
    # 행렬 mB 출력
    print(mB)
    # fout.write 를 사용해서 result.txt에 mB를 write
    fout.write("{}".format(mB))
    # mC에 fgetMtrx에서 구한 행렬을 입력
    mC = fgetMtrx(fin)
    # 행렬의 이름을 mC라 설정
    mC.setName("mC")
    # 행렬 mC를 출력
    print(mC)
    # fout.write 를 사용해서 result.txt에 mC를 write
    fout.write("{}".format(mC))
    # fin.close를 사용해서 read open 종료
    fin.close()
    
    # __add__ 메서드를 사용해 mA와 mB의 합을 mD로 리턴
    mD = mA + mB
    # 행렬의 이름을 "mD = mA + mB"라 설정
    mD.setName("mD = mA + mB")
    # 행렬 mD를 출력
    print(mD)
    # fout.write 를 사용해서 result.txt에 mD를 write
    fout.write("{}".format(mD))
    
    # __sub__ 메서드를 사용해 mA와 mB의 차를 mE로 리턴
    mE = mA - mB
    # 행렬의 이름을 "mE = mA - mB"라 설정
    mE.setName("mE = mA - mB")
    # 행렬 mE를 출력
    print(mE)
    # fout.write 를 사용해서 result.txt에 mE를 write
    fout.write("{}".format(mE))
    
    # __mul__ 메서드를 사용해 mA와 mC의 곱을 mF로 리턴
    mF = mA * mC
     # 행렬의 이름을 "mF = mA * mC"라 설정
    mF.setName("mF = mA * mC")
    # 행렬 mF를 출력
    print(mF)
    # fout.write 를 사용해서 result.txt에 mF를 write
    fout.write("{}".format(mF))
    # fout.close를 사용해서 write open 종료
    fout.close()
    
# 만약 name이 main이라면 main() 실행
if __name__ == "__main__":
    main()