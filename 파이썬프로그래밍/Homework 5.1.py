# Homework 5.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 3, 2023
# Major features :
# - Import module random , time
# - Generate a non-duplicate random number list L
# - Print the first 2 lines and the last 2 lines of list L
# - Sort the elements of the given list in ascending order in a merge sort structure
# - Print the sorted state using the printListSample() function
# - Print the time taken for sorting

# 난수 생성을 위한 random 모듈과 정렬의 시간 계산을 위한 time 모듈
import random
import time

# n을 입력받아 중복되지 않는 n개의 난수를 생성하여 n크기의 리스트에 넣는 함수


def genBingRandList(n):
    list_L = []
    list_L = random.sample(range(0, n), n)
    return list_L

# 리스트의 이름과 한줄에 몇개의 숫자 그리고 몇개줄을 출력하는지 입력받고 입력받은 리스트를 출력하는 함수


def printListSample(list_name, per_line, sample_lines):
    for s in range(sample_lines):
        for p in range(per_line):
            a = s*10 + p  # 입력받은 per_line , sample_lines에 따라 리스트의 값을 출력하기 위한 변수 A
            print("{:7d}".format(list_name[a]), end=' ')
        print()  # 줄바꿈을 위한 print
    print("    . . . . . .")
    list_length = len(list_name)
    # 입력받은 per_line , sample_lines에 따라 리스트의 값을 출력하기 위한 변수 B
    b = list_length - 1 - (s*10 + p)
    for s in range(sample_lines):
        for p in range(per_line):
            print("{:7d}".format(list_name[b]), end=' ')
            b += 1  # B를 1만큼 더해줘서 마지막엔 마지막 리스트의 값을 출력하게 만듬
        print()

# 주어진 리스트의 원소들을 오름차순을 병합정렬 구조로 정렬하기 위해서 재귀함수 구조로 구현


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list)//2  # 구간을 1/2로 게속 쪼갬
    left = merge_sort(unsorted_list[:mid])
    right = merge_sort(unsorted_list[mid:])

    return merge(left, right)


def merge(left, right):  # 나눠둔 구간을 하나로 합치기 위한 함수 구현

    sorted_list = []
    i = 0
    j = 0

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if i < len(left):
        sorted_list += left[i:]
    if j < len(right):
        sorted_list += right[j:]
    return sorted_list


while True:
    print("Performance test of merge sorting algorithm")
    # 입력받은 size개의 난수를 만든후 리스트L에 포함시킴
    size = int(input("Input size of random list L (0 to quit) = "))
    if size == 0:  # 만약 size가 0 이라면 while True 무한반복문은 끝나게 됨, 즉 코드 종료
        break
    L = genBingRandList(size)  # 입력받은 난수들의 리스트를 L로 설정
    print("Before mergeSort of L")
    printListSample(L, 10, 2)
    t1 = time.time()  # 행렬계산 직전에 시간 쟤기
    sorted_L = merge_sort(L)
    t2 = time.time()  # 행렬계산 끝난후의 시간 쟤기
    print("After mergeSort of L :")
    printListSample(sorted_L, 10, 2)
    time_elapsed = t2 - t1  # 끝난후의 시간과 직전의 시간을 빼서 행렬이 얼마나 걸린지 계산
    print("Merge sorting took {} sec".format(time_elapsed))
