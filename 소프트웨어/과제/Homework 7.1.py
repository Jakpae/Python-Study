# Homework 7.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 16, 2023
# Major features :
# - Make Personal python module MyList.py , MySortings.py
# - import Module MyList,MySortings

# 정렬 시간을 구하기 위한 time 모듈과 정수형 난수의 리스트 생성, 샘플 출력 및 뒤섞기 기능을 제공하는 MyList 모듈 Import
# 선택정렬과 병합정렬 기능을 수행하는 MySorting 모듈 Import
import time
import MyList
import MySortings


def main():
    # 리스트의 크기를 정하는 test_sizes 리스트 생성
    test_sizes = [10000, 20000, 30000, 40000, 50000]
    for size in test_sizes:
        # 빈 리스트 L 생성
        L = []
        # size 만큼의 정수형 난수 리스트 만듬
        L = MyList.genRandList(L, size)
        print("\nList (size : {}) before merge sorting : ".format(size))
        # MyList 모듈에 있는 printListSample 함수를 불러와 L라는 리스트의 앞 10개씩 2줄 그리고 뒤 10개씩 2줄 출력
        MyList.printListSample(L, 10, 2)
        # 병합정렬을 하기 직전의 시간을 구하기 위한 t1
        t1 = time.time()
        # MySorting 모듈에 있는 mergeSort 함수를 불러와 L라는 리스트를 병합정렬 실행
        MySortings.mergeSort(L)
        # 병합 정렬이 끝난후의 시간을 구하기 위한 t2
        t2 = time.time()
        print("List (size : {}) after merge sorting : ".format(size))
        # MyList 모듈에 있는 printListSample 함수를 불러와 L라는 리스트의 앞 10개씩 2줄 그리고 뒤 10개씩 2줄 출력
        MyList.printListSample(L, 10, 2)
        # t2 - t1을 하여서 병합정렬이 몇초가 걸렸는지 구하고 출력
        print("Merge sorting for list of {} integers took {} sec".format(size, t2-t1))

        # L리스트 셔플
        MyList.shuffleList(L)
        print("\nList (size : {}) before selection sorting : ".format(size))
        MyList.printListSample(L, 10, 2)
        t1 = time.time()
        # MySorting 모듈에 있는 selctionSort 함수를 불러와 L라는 리스트를 선택정렬 실행
        MySortings.selectionSort(L) 
        t2 = time.time()
        print("List (size : {}) after selection sorting : ".format(size))
        MyList.printListSample(L, 10, 2)
        print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))


if __name__ == "__main__":
    main()
