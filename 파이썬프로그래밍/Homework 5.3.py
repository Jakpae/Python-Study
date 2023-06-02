# Homework 5.3
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 4, 2023
# Major features :
# - Write a function print_mtrx(name.M) that receives and outputs a matrix from a two-dimensional list
# - Implement a function that calculates the sum, difference, and product of a matrix

# 행렬을 표현하는 2차원 리스트를 행렬로 출력하는 함수
def print_mtrx(n, m):
    print("{} =".format(n))
    a_row, a_col = len(m), len(m[0])
    for r in range(a_row):
        for c in range(a_col):
            print("{:3d}".format(m[r][c]), end='')
        print()

# 입력받은 2개의 2차원 리스트의 행렬을 더한후 그 값을 리턴하는 함수


def add_mtrx(m1, m2):
    result = []

    for i in range(len(m1)):
        tep = []
        for j in range(len(m1[i])):
            tep.append(m1[i][j]+m2[i][j])

        result.append(tep)
    return result

# 입력받은 2개의 2차원 리스트의 행렬을 뺀후 그 값을 리턴하는 함수


def sub_mtrx(m1, m2):
    result = []

    for i in range(len(m1)):
        tep = []
        for j in range(len(m1[i])):
            tep.append(m1[i][j]-m2[i][j])

        result.append(tep)
    return result

# 입력받은 2개의 2차원 리스트의 행렬을 곱한후 그 값을 리턴하는 함수


def mul_mtrx(m1, m2):
    mR = []
    for r in range(len(m1)):
        mR_row = []
        for c in range(len(m2[0])):
            mR_rc = 0
            for k in range(len(m2)):
                mR_rc += m1[r][k] * m2[k][c]
            mR_row.append(mR_rc)
        mR.append(mR_row)

    return mR

# 3개의 2차원 리스트 행렬의 덧셈,뺄샘,곱을 출력하는 함수


def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
    B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
    C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    print_mtrx("A", A)
    print_mtrx("B", B)
    print_mtrx("C", C)

    D = add_mtrx(A, B)
    print_mtrx("A + B", D)

    E = sub_mtrx(A, B)
    print_mtrx("A - B", E)

    F = mul_mtrx(A, C)
    print_mtrx("A * C", F)


if __name__ == "__main__":
    main()
