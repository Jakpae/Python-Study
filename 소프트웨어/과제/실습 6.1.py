# 실습 6.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 7, 2023
# Major features :
# - Import module random , time
# - Print the first 2 lines and the last 2 lines of list L
# - Sort the elements of the given list in ascending order in a merge sort structure
# - Print the sorted state using the printListSample() function
# - Print the time taken for sorting


# 난수 생성을 위한 random 모듈과 정렬의 시간 계산을 위한 time 모듈
import random
import time

# n을 입력받아 중복되자 않는 n개의 난수를 생성하여 n크기의 리스트에 넣는 함수

# 입력받은 L리스트의 per_line * sample_lines개의 자료 출력


def printListSample(L, per_line, sample_lines):
    count = 0
    size = len(L)
    # L리스트의 0~9 10~19번째 값 출력
    for i in range(0, sample_lines):
        s = ""
        for j in range(0, per_line):
            if count >= size:
                break
            s += "{0:>7} ".format(L[count])
            count += 1
        print(s)
        if count >= size:
            break
    if count < size:
        print('. . . . . .')
        if count < (size - per_line * sample_lines):
            count = size - per_line * sample_lines
        # L 리스트의 뒤에서 0~9 10~19번째 값 출력
        for i in range(0, sample_lines):
            s = ""
            for j in range(0, per_line):
                if count >= size:
                    break
                s += "{0:>7} ".format(L[count])
                count += 1
            print(s)
            if count >= size:
                break

# 병합정렬을 하기위한 _merge 함수


def _merge(L_left, L_right):

    L_res = []
    i, j = 0, 0

    len_left, len_right = len(L_left), len(L_right)

    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1

    while (i < len_left):
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res

# 병합정렬 함수 merge_sort, _merge 함수를 이용해서 병합정렬을 함


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = merge_sort(L[:middle])
        L_right = merge_sort(L[middle:])
        return _merge(L_left, L_right)


# While-loop 반복문
while True:
    print("\nCompare sorting algorithms")
    size = int(input("Array Size (0 to quit) = "))
    # 만약 0 이 입력된다면 While-loop 반복문 종료
    if size == 0:
        break
    A = list(range(size))

    random.shuffle(A)
    print("\nBefore mergeSort of A :")
    printListSample(A, 10, 2)
    t1 = time.time()  # 시간 재기 시작
    sorted_A = merge_sort(A)
    t2 = time.time()  # 시간 재기 끝
    print("After mergeSort of A :")
    printListSample(sorted_A, 10, 2)
    time_elapsed = t2 - t1  # t2 - t1을 하여서 정렬까지 얼마나 걸렸는지 계산
    print("Merge sorting took {} sec".format(time_elapsed))  # 걸린 시간 출력
