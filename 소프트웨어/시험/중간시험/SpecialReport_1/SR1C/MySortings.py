# MySortings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - Python function mergeSort(L) that sorts a list given as an argument in ascending order with mergeSort algorithm
# - The mergeSort(L) function includes the ability to copy sorted results to list L passed as arguments

# 병합 정렬을 위한 _merge와 mereSort함수
def mergeSort(L):
    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]

        # 왼쪽과 오른쪽 부분 리스트를 각각 병합정렬로 정렬
        _mergeSort(left)
        _mergeSort(right)

        # 정렬된 부분 리스트들을 병합하여 전체 리스트를 정렬
        _merge(left, right, L)

# 리스트 L을 병합정렬하는 함수 merge_sort에서 호출되는 재귀함수 _mergeSort
def _mergeSort(L):

    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]
        
        _mergeSort(left)
        _mergeSort(right)

        #전체 리스트를 정렬
        _merge(left, right, L)

# 리스트 L을 병합정렬하는 함수 merge_sort에서 호출되는 재귀함수 _merge
def _merge(L_left, L_right, L):
    i = j = k = 0
    while i < len(L_left) and j < len(L_right):
        if L_left[i] < L_right[j]:
            L[k] = L_left[i]
            i += 1
        else:
            L[k] = L_right[j]
            j += 1
        k += 1
    while i < len(L_left):
        L[k] = L_left[i]
        i += 1
        k += 1

    while j < len(L_right):
        L[k] = L_right[j]
        j += 1
        k += 1
