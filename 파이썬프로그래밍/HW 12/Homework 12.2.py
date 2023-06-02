# Homework 12.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 31, 2023


import random, time
from MyArray import *
from MySortings import *
import numpy as np

# 최적의 ss_cutoff를 찾기위한 test_1 함수
def test_1(test_size):
    print("Checking selection_sort cutoff . . . ")
    # start지점와 end지점 설정
    start, end, step = 1, 30, 1
    t_min = 1000
    ss_min = start
    for i in range(start, end, step):
        A = np.arange(0.0, test_size)
        np.random.shuffle(A)
        ss_cutoff = i
        t1 = time.time()
        hybrid_sort_jit(A, ss_cutoff)
        t2 = time.time()
        time_elapsed_ms = (t2 - t1) * 1000
        # 최적의 ss_cutoff를 찾기 위한 if,elif문
        if i == start:
            t_min = time_elapsed_ms
        elif t_min > time_elapsed_ms:
            ss_min = i
            t_min = time_elapsed_ms
        print("hybrid_sort_jit() (ss_cutoff: {:2d}) took {:10.3f} msec to sort a numpy array (size = {:8d})".format(ss_cutoff, time_elapsed_ms, test_size))
    print("Selection_sort cutoff ({:3d}) took the minimun elapsed time ({:8.6f})".format(ss_min, t_min))
    # 최적의 ss_cutoff 반환
    return ss_min

# test_1에서 구해진 최적의 ss_cutoff를 사용해서 3개의 배열에서 실수형 난수 배열에 대한 hybird_srot와 numpy_sort의 실행 시간을 각각 실행 및 측정
def test_2(ss_cutoff):
    # 3개의 배열 크기 설정
    L_size = [100000, 1000000, 10000000]
    print("\nComparing sort algorithms")
    for size in L_size:
        # numpy arange 설정
        A = np.arange(0.0, size)
        # A크기 만큼의 난수 리스트를 생성
        np.random.shuffle(A)
        print("Before hybrid_sort_jit() of A :")
        printArraySample(A, 10, 2)
        t1 = time.time()
        # 최적의 ss_cutoff를 사용해 hybrid_sort_jit 실행
        hybrid_sort_jit(A, ss_cutoff)
        t2 = time.time()
        print("After hybrid_sort_jit() of A :")
        printArraySample(A, 10, 2)
        time_elapsed_ms = (t2 - t1) * 1000
        print("hybrid_sort_jit() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        np.random.shuffle(A)
        print("\nBefore np.sort() of A :")
        printArraySample(A, 10, 2)
        t1 = time.time()
        # Numpy에 내장되어있는 sort를 실행
        sorted_A = np.sort(A)
        t2 = time.time()
        print("After np.sort() of A :")
        printArraySample(sorted_A, 10, 2)
        time_elapsed_ms = (t2 - t1) * 1000
        print("np.sort() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        print()


if __name__ == "__main__":
    test_size = 10000000
    ss_min = test_1(test_size)
    test_2(ss_min)

