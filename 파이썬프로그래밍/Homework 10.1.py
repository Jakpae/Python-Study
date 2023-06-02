# Homework 10.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 16, 2023

import os, sys, random, time
import numpy as np
from MyList import *
from MySortings import *


def main():
    num_sample_Lines = 2
    num_elements_per_Line = 10
    test_sizes = [100000, 1000000, 10000000]
    for size_L in test_sizes:
        # 빈 리스트 L 생성
        L = []
        # genRanList 에서 return 된 size만큼의 난수값을 L로 설정
        L = genRandList(L, size_L)
        print("\nBefore mergeSort of L (size: {}):".format(size_L))
        # 리스트 L을 출력하기 위한 printListSample 함수를 호출해서 세로 2줄 가로 10줄의 리스트 L의 값을 출력
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        # mergeSort 시간을 측정하기 위한 t2, t1
        t1 = time.time()
        L = mergeSort(L)
        t2 = time.time()
        print("After mergeSort of L :")
        # 리스트 L을 출력하기 위한 printListSample 함수를 호출해서 세로 2줄 가로 10줄의 리스트 L의 값을 출력
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        # t2 - t1 을 하여 mergesort의 실행시간인 time_elapsed
        time_elapsed = t2 - t1
        print("mergeSort() for list L (size = {}) took {} sec".format(size_L, time_elapsed))
        # 리스트 L을 섞는 random.shuffle
        random.shuffle(L)
        print("\nBefore np.sort of L (size: {}):".format(size_L))
        # 리스트 L을 출력하기 위한 printListSample 함수를 호출해서 세로 2줄 가로 10줄의 리스트 L의 값을 출력
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        # NumpySort 시간을 측정하기 위한 t2, t1
        t1 = time.time()
        L = np.sort(L)
        t2 = time.time()
        print("After np.sort of L :")
        # 리스트 L을 출력하기 위한 printListSample 함수를 호출해서 세로 2줄 가로 10줄의 리스트 L의 값을 출력
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        # t2 - t1 을 하여 NumpySort의 실행시간인 time_elapsed
        time_elapsed = t2 - t1
        print("np.sort() for list L (size = {}) took {} sec".format(size_L, time_elapsed))
        
if __name__ == "__main__":
    main()