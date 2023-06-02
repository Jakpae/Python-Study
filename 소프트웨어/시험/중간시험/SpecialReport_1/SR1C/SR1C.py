# SR1C
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - The main() function generates a non-overlapping integer random number list with 10000, 100000, and 1000000 elements, outputs a list sample before sorting and a list sample after sorting, and measures and outputs the elapsed time of sorting

#시간을 쟤기 위한 time 과 사용자지정 모듈 import
import time
from MyList import *
from MySortings import *


def main():
    print("2023-1 SW&AI_SR1C 학번: 22312050, 성명: 이승준")
    test_size = [10000,100000,1000000] #구할 사이즈 정함
    for size in test_size:
        L = []
        #size만큼의 랜덤 난수 생성
        A = genNonDeuplicatedRandomList(size)
        print("\nBefore Merge-Sort of A (size = {}):".format(size))
        printListSample(A,10,2)
        t1 = time.time()
        # 리스트 a를 병합정렬 실행
        mergeSort(A)
        t2 = time.time()
        print("After Merge-Sort of A .....")
        printListSample(A,10,2)
        time_elapsed = t2 - t1
        print("Merge-Sort for List (size={}) took {} sec".format(size,time_elapsed))

if __name__ == "__main__":
    main()