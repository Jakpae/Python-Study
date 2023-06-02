# Homework 6.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 9, 2023
# Major features :
# - Make Personal python module MyList.py , MySortings.py
# - import Module MyList,MySortings

# 시간 계산을 위한 time 모듈, 중복되지 않는 정수형 난수 리스트 생성, 샘플 출력 및 뒤섞기 기능을 위한 Mylist 모듈
# 선택정렬과 병합정렬을 위한 MySortings 모듈 import
import time
import MyList
import MySortings

# While-Loop 함수
while True:
    # 중복되지 않는 size만큼의 정수형 난수 리스트 생성을 위한 size 입력
    size = int(input("\nsize of list (0 to terminate) = "))
    # 빈 리스트 L 생성
    L = []
    # Return 된 size 크기의 정수형 난수 리스트를 L로 설정
    L = MyList.genRandList(L, size)
    print("List (size : {}) before merge sorting : ".format(size))
    # MyList의 샘플 출력을 위한 printListSample 함수 호출
    MyList.printListSample(L, 10, 2)
    # 병합정렬 계산전의 시간을 알기위한 t1
    t1 = time.time()
    # 병합정렬한 L리스트를 L로 설정
    L = MySortings.mergeSort(L)
    # 병합정렬 계산후의 시간을 알기위한 t2
    t2 = time.time()
    print("\nList (size : {}) after merge sorting : ".format(size))
    # 병합정렬된 리스트를 출력하기 위한 printListSample 함수 호출
    MyList.printListSample(L, 10, 2)
    print("Merge sorting for list of {} integers took {} sec".format(size, t2-t1))
    # 리스트L를 뒤섞고 L로 설정
    L = MyList.shuffleList(L)
    print("\nList (size : {}) before selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    # 선택정렬 계산전의 시간을 알기위한 t1
    t1 = time.time()
    # 선택정렬한 L리스트를 L로 설정
    L = MySortings.selectionSort(L)
    # 선택정렬 계산전의 시간을 알기위한 t1
    t2 = time.time()
    print("\nList (size : {}) after selection sorting : ".format(size))
    # 선택정렬된 리스트를 출력하기 위한 printListSample 함수 호출
    MyList.printListSample(L, 10, 2)
    print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))
