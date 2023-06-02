# 실습 12.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 31, 2023

import random, time

# 행렬을 출력하고 만들기 위한 MyArray 모둘과 정렬을 하기 위한 MySortings 모듈 Import
from MyArray import *
from MySortings import *
# Numpy Sort와 Numpy.random.shuffle을 구현하기 위한 Numpy 모듈 Import
import numpy as np

# 만약 Name 이 Main이라면 실행
if __name__ == "__main__":
    # 정렬을 테스트 하기 위한 크기 Test_size 설정
    Test_size = [1000, 100000, 1000000, 10000000]
    print("\nComparing sort algorithms")
    # 테스트 사이즈 즉 3번 반복하는 For 반복문 생성
    for size in Test_size:

        # Numpy를 사용해서 Size크기의 랜덤 행렬 생성
        A = np.arange(size)

        # Numpy를 사용해서 리스트 A의 값을 랜덤으로 셔플
        np.random.shuffle(A)
        print("Before quick_sort() of A :")

        # A리스트를 앞 뒤로 10행 2열의 구조로 출력
        printArraySample(A, 10, 2)

        # Quick_Sort의 시간을 쟤기 위한 t1과 t2
        t1 = time.time()
        quick_sort(A) # basic quick_sort() in divide-and-conquer
        t2 = time.time()

        # Quick_Sort된 리스트 A의 값을 출력
        print("After quick_sort() of A :")
        printArraySample(A, 10, 2)

        # Quick_Sort의 절린시간을 1000을 곱해 msc의 구조로 출력
        time_elapsed_ms = (t2 - t1) * 1000

        print("quick_sort() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        # Numpy를 사용해서 리스트 A의 값을 랜덤으로 셔플
        np.random.shuffle(A)
        print("\nBefore quick_sort_jit() of A :")

        # A리스트를 앞 뒤로 10행 2열의 구조로 출력
        printArraySample(A, 10, 2)

        # Quick_Sort_jit의 시간을 쟤기 위한 t1과 t2
        t1 = time.time()
        quick_sort_jit(A) # quick_sort with @jit of Numba
        t2 = time.time()
        print("After quick_sort_jit() of A :")

        # A리스트를 앞 뒤로 10행 2열의 구조로 출력
        printArraySample(A, 10, 2)

        # Quick_Sort_jit의 절린시간을 1000을 곱해 msc의 구조로 출력
        time_elapsed_ms = (t2 - t1) * 1000
        print("quick_sort_jit() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        np.random.shuffle(A)
        print("\nBefore np.sort() of A :")

        # A리스트를 앞 뒤로 10행 2열의 구조로 출력
        printArraySample(A, 10, 2)

        # Numpy_Sort의 시간을 쟤기 위한 t1과 t2
        t1 = time.time()
        sorted_A = np.sort(A) # Numpy sort() (quick_sort() implemented in C/C++)
        t2 = time.time()
        print("After np.sort() of A :")

        # A리스트를 앞 뒤로 10행 2열의 구조로 출력
        printArraySample(sorted_A, 10, 2)

        # Numpy_Sort의 절린시간을 1000을 곱해 msc의 구조로 출력
        time_elapsed_ms = (t2 - t1) * 1000
        print("np.sort() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        print()