# MySortings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 31, 2023


# Quick_Sort의 Just in Time 을 구현하기 위한 모듈 Numba Import
from numba import jit, prange


# 배열 분할을 수행하기 위한 함수 _partition
def _partition(arr, left, right, pi):
    # 리스트에서 선택한 중간값을 pivot으로 설정하고, pivot을 기준으로 파티션을 나누어 새로운 pivot 위치를 반환
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    new_pi = i = left
    while (i<=right-1):
        if (arr[i] <= pv):
            arr[new_pi], arr[i] = arr[i], arr[new_pi]
            new_pi += 1 
        i += 1
    arr[new_pi], arr[right] = arr[right], arr[new_pi]
    return new_pi


# 비재귀형태로 구현된 퀵정렬 함수 _quickSortLoop
def _quickSortLoop(arr, left, right):
    # 분할과정을 재귀적으로 진행하되, 리스트의 길이가 짧아지면 스택을 쌓는 대신 반복문을 사용하여 인라인 연산을 수행
    if (left >= right):
        return
    pi = (left + right)//2
    new_pi = _partition(arr, left, right, pi)
    if (left < new_pi -1): 
        _quickSortLoop(arr, left, new_pi-1)
    if (new_pi + 1 < right): 
        _quickSortLoop(arr, new_pi+1, right)


#리스트와 리스트이 길이를 입력받아 _quickSortLoop 함수를 호출하여 정렬을 하는 quick_sort 함수
def quick_sort(arr):
    size = len(arr) 
    _quickSortLoop(arr, 0, size-1)


@jit(nopython=True) # Numba JIT 컴파일러를 사용하여 함수를 미리 컴파일
def _partition_jit(arr, left, right, pi):
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    new_pi = i = left
    while (i<=right-1):
        if (arr[i] <= pv):
            arr[new_pi], arr[i] = arr[i], arr[new_pi]
            new_pi += 1 
        i += 1
    arr[new_pi], arr[right] = arr[right], arr[new_pi]
    return new_pi


@jit(nopython=True) # Numba JIT 컴파일러를 사용하여 함수를 미리 컴파일
def _quickSortLoop_jit(arr, left, right):
    if (left >= right):
        return
    pi = (left + right)//2
    new_pi = _partition_jit(arr, left, right, pi)
    if (left < new_pi -1): 
        _quickSortLoop_jit(arr, left, new_pi-1)
    if (new_pi + 1 < right): 
        _quickSortLoop_jit(arr, new_pi+1, right)


@jit(nopython=True) # Numba JIT 컴파일러를 사용하여 함수를 미리 컴파일
def quick_sort_jit(arr):
    size = len(arr) 
    _quickSortLoop_jit(arr, 0, size-1)
