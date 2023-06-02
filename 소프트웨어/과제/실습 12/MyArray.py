# MyArray
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 31, 2023

import numpy as np


def printArray(arr):
    arr_shape = np.shape(arr) # 배열의 shape 확인

    if len(arr_shape) == 1: # 만약 1차원 배열이라면 실행
        for i in range(len(arr)):
            print("{:10.1f}".format(arr[i]), end='') # 너비 10, 소수점 이하 1자리의 실수로 포맷팅하여 출력
        print()

    elif len(arr_shape) == 2: # 만약 2차원 배열이라면 실행
        n_row = len(arr) # 행의 수
        n_col = len(arr[0]) # 열의 수

        for i in range(n_row):
            for j in range(n_col):
                print("{:10.1f}".format(arr[i][j]), end='') # 너비10, 소수점 이하 1자리의 실수로 포맷팅하여 출력
            print()
            

def printArraySample(A, per_line = 10, sample_lines = 2):
    # 출력할 요소의 개수를 기록하는 count를 0으로 초기화
    count = 0
    # 배열 A의 길이를 size 변수에 저장
    size = len(A)
    # Sample_lines 줄까지 요소를 출력
    for i in range(0, sample_lines):
        s = "" # 출력할 요소를 기록하는 문자열 s를 초기화
        for j in range(0, per_line): # 한 줄에 per_line개의 요소를 출력
            if count > size: # 출력할 요소가 남아있지 않는 경우, 반복문을 종료
                break
            s += "{0:>10.1f} ".format(A[count]) # 출력할 요소를 문자열 s에 추가
            count += 1 # 다음 출력할 요소의 인덱스를 계산
        print(s) # 줄을 출력
        if count >= size: # 출력할 요소가 없을 경우 반복문 종료
            break
    # 출력할 요소의 수가 많은 경우 ....을 출력
    if count < size:
        print(' ......')
        # 마지막 simple_lines 줄부터 거꾸로 출력
        if count < (size - per_line * sample_lines):
            count = size - per_line * sample_lines # 마지막 줄의 첫 요소의 인덱스 계산
        for i in range(0, sample_lines):
            s = "" # 출력할 요소를 기록하는 문자열 s를 초기화
            for j in range(0, per_line): # 줄의 per_line개의 요소를 출력
                if count >= size: # 출력할 요소가 남아있지 않는 경우, 반복문을 종료
                    break
                s += "{0:>10.1f} ".format(A[count]) # 출력할 요소를 문자열 s에 추가
                count += 1 # 다음 출력할 요소의 인덱스를 계산
            print(s) # 줄을 출력
            if count >= size: # 출력할 요소가 남아있지 않은 경우, 반복문을 종료
                break