# Homework 7.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 10, 2023
# Major features :
# - Preparing custom python packages and sub-packages
# - Implement a function that performs output, addition, subtraction, and multiplication operations of a matrix

# 특정 디렉토리 내의 파일 목록을 구하기 위한 os 모듈
import os
# 사용자 정의 파이썬 패키지 / 서브 패키지의 경로를 위한 sys 모듈
import sys

# 사용자 정의 파이썬 패키지 / 서브 패키지의 경로를 시스템 path에 포함
sys.path.append(
    "/Users/leeseungjun/Library/CloudStorage/GoogleDrive-jfldjd@yu.ac.kr/내 드라이브/소프트웨어와인공지능/실습,과제/MyPyPackage/myModules")
print("sys.path : ", sys.path) # sys.path를 출력하여 사용자 정의 파이썬 패키지 / 서브 패키지의 경로가 포함된 것을 확인

# MyPyPackage/myModules 에 있는 MyMatrix 를 불러와서 사용
from MyMatrix import *


#  행렬 A,B,C 설정
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

# 행렬 A,B,C 출력
printMtrx("A", A)
printMtrx("B", B)
printMtrx("C", C)

# 행렬 A,B의 합 출력
D = addMtrx(A, B)
printMtrx("A + B", D)

# 행렬 A,B의 차 출력
E = subMtrx(A, B)
printMtrx("A - B", E)

# 행렬 A,C의 곱 출력
F = mulMtrx(A, C)
printMtrx("A * C", F)
