# Homework 6.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 10, 2023
# Major features :

# 행렬의 계산을 위한 MyMarix 모듈 import
import MyMatrix

# A,B,C 2차원 리스트 행렬
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

# A,B,C 행렬 출력
MyMatrix.printMtrx("A", A)
MyMatrix.printMtrx("B", B)
MyMatrix.printMtrx("C", C)

# return 된 행렬의 합을 D로 설정
D = MyMatrix.addMtrx(A, B)
MyMatrix.printMtrx("A + B", D)

# return 된 행렬의 차를 D로 설정
E = MyMatrix.subMtrx(A, B)
MyMatrix.printMtrx("A - B", E)

# return 된 행렬의 곱을 D로 설정
F = MyMatrix.mulMtrx(A, C)
MyMatrix.printMtrx("A * C", F)
