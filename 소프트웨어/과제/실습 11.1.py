# 실습 11.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 19, 2023
# Major features :

import numpy as np


# 계수행렬과 상수열의 행렬을 각각 NumPy 2차원 배열과 1차원 리슽로 구성하여 반환하는 함수 구현
def fget_LinearSystemArrays(f_name):
    print("Getting linear system arrays from file ({})".format(f_name))
    # f_name을 read상태로 열기
    f_in = open(f_name, "r")
    # n_row와 n_col의 크기를 readline을 사용해서 불러오기
    str_line = f_in.readline()
    # 불러온 값을 n_row 와 n_col에 넣기
    n_row, n_col = map(int, str_line.split())
    print("fget_LinearSystemArrays :: n_row = {}, n_col = {}".format(n_row, n_col))
    # 빈 리스트 coeff_mtrx 만들기
    coeff_mtrx = []
    # n_row만큼 반복해서 coeff_mtrx에 넣는 for 반복문
    for i in range(n_row):
        row_data = list(map(int, f_in.readline().split()))
        coeff_mtrx.append(row_data)
    coeff_npArray = np.array(coeff_mtrx)
    # n_row와 n_col의 크기를 readline을 사용해서 불러오기
    B_n_row, B_n_col = map(int, f_in.readline().split())
    # B에 값을 넣고 np.array를 사용해서 행렬 생성
    B = list(map(int, f_in.readline().split()))
    B = np.array(B)
    return coeff_npArray, B


def main():
    # "electronicCircuit.txt"로 fget_LinearSystemArrays 실행
    A, B = fget_LinearSystemArrays("electronicCircuit.txt")
    # 행렬 A와 B 실행
    print("A =\n", A)
    print("B =\n", B)
    A_inv = np.linalg.inv(A)
    # Numpy Solve를 사용해서 A와 B의 Solve값을 X로 설정하고 출력
    # X = np.linalg.solve(A, B)
    X = np.matmul(A_inv, B)
    print("X =\n", X)
    # Numpy matmul를 사용해서 A와 X의 matmul값을 B1으로 설정하고 출력
    B1 = np.matmul(A, X)
    print("B1 = np.matmul(A, X) =\n", B1)


# name을 main이면 실행
if __name__ == "__main__":
    main()