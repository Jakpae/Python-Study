# MyList 
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023


import math

# n개의 실수 데이터를 받아 L_data에 넣은후 반환하는 함수
def get_float_list():
    L_data = []
    data = input("Input float data in a line : ")
    float_strings = data.split()
    L_data = list(map(float,float_strings))
    return L_data

# 리스트 L의 크기 최솟값 최댓값 평균 분산 표준편차를 반환하는 함수
def get_statistics(L):
    L_len = len(L)
    L_min = min(L)
    L_max = max(L)
    L_avg = sum(L) / len(L)
    val = 0
    for i in L:
        val = val + (i - L_avg)**2
    L_var = val / len(L)
    L_std = math.sqrt(L_var)
    
    return L_len,L_min,L_max,L_avg,L_var,L_std