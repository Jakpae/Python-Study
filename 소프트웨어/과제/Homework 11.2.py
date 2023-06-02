# Homework 11.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 19, 2023
# Major features :

import math
import numpy as np
EPSILON = 0.0000001

# 행크기와 열크기과 2차원 ndarray를 반환하는 함수 fget_ndArray(f_name) 구현
def fget_ndArray(f_name):
    fin = open(f_name, "r")
    data = []
    for line in range(0,7):
        row_data = list(map(float, fin.readline().split()))
        data.append(row_data)
    A = np.array(data)
    return A

def main():
    A = fget_ndArray("matrix_data.txt")
    print("A ({} x {}) =".format(len(A), len(A[0])))
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