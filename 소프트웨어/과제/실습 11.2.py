# 실습 11.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 19, 2023
# Major features :

# 계산을 위한 math 와 numpy 모듈 import
import math
import numpy as np
EPSILON = 0.0000001


# txt파일을 부르는 loadtxt실행
def fget_ndAarray(f_name):
    ndArray = np.loadtxt(f_name)
    return ndArray


# 메인 함수 생성
def main():
    # square_mtrx_5x5.txt 파일 load txt
    A = fget_ndAarray("square_mtrx_5x5.txt")
    print("A ({} x {}) =".format(len(A), len(A[0])))
    # 행렬 A출력
    print(A)
    # 선형대수 관련 유니버셜 함수 det과 inv 함수를 사용해서 행렬식과 역행렬 계산하고 출력
    det_A = np.linalg.det(A)
    inv_A = np.linalg.inv(A)
    E = np.matmul(A, inv_A)
    print("det_A = ", det_A)
    # math.fabs(det_A)가 EPSILON보다 작다면 print실행 아니면 inv_출력 및 matmul 값 출력
    if math.fabs(det_A) < EPSILON:
        print("Matrix inversion is not available for this matrix")
    else:
        print("inv_A = \n", inv_A)
        print("E= np.matmul(A, inv_A) = \n", E)


# name이 main이라면 실행
if __name__ == "__main__":
    main()