# Homework 10.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 18, 2023

# Numpy 모듈 import
import numpy as np


def main():
    # Numpy 배열 A의 생성
    A = np.array([[1, 5, 3, 3, 7], [3, 4, 5, 6, 7], [1, 3, 5, 7, 9], [3, 1, 4, 1, 5], [5, 5, 3, 3, 1]])
    # Numpy 배열 B의 생성
    B = np.array([105, 135, 145, 74, 75])

    # 배열 A,B 출력
    print("A =\n", A)
    print("B =\n", B)

    # 배열 A의 행렬식 det_A 계산
    det_A = np.linalg.det(A)

    # 배열 A의 행렬식 det_A 출력
    print("det_A =\n", det_A)

    # 배열 A의 역행렬 inv_A 출력
    inv_A = np.linalg.inv(A)

    # 배열 A의 역행렬 inv_A 출력
    print("inv_A =\n", inv_A)

    # 선형시스템 AX = B의 해인 X 산출
    X = np.linalg.solve(A, B)

    # 선형시스템 AX = B의 해인 X 출력
    print("X = \n", X)

    # B1 = A * X의 계산 
    B1 = np.matmul(A, X)

    # B1 = A * X의 출력
    print("B1 = A * X =\n", B1)

    # X1 = inv_A * B의 계산
    X1 = np.matmul(inv_A, B)

    # X1 = inv_A * B의 출력
    print("X1 = inv_A * B =\n", X1)


if __name__ == "__main__":
    main()
