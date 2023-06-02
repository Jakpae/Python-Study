# MySortings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 31, 2023

# Quick_Sort의 Just in Time 을 구현하기 위한 모듈 Numba Import
from numba import jit, njit, prange

def _partition(arr, left, right, pi):
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

def _quickSortLoop(arr, left, right):
    #print("quickSort", left, right)
    if (left >= right):
        return
    pi = (left + right)//2
    new_pi = _partition(arr, left, right, pi)
    #print("after partition : ", left, right, new_pi)
    if (left < new_pi -1): 
        _quickSortLoop(arr, left, new_pi-1)
    if (new_pi + 1 < right): 
        _quickSortLoop(arr, new_pi+1, right)

def quick_sort(arr):
    size = len(arr) 
    _quickSortLoop(arr, 0, size-1)

@jit(nopython=True)
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

@jit(nopython=True)
def _quickSortLoop_jit(arr, left, right):
    #print("quickSort", left, right)
    if (left >= right):
        return
    pi = (left + right)//2
    new_pi = _partition_jit(arr, left, right, pi)
    #print("after partition : ", left, right, new_pi)
    if (left < new_pi -1): 
        _quickSortLoop_jit(arr, left, new_pi-1)
    if (new_pi + 1 < right): 
        _quickSortLoop_jit(arr, new_pi+1, right)

@jit(nopython=True)
def quick_sort_jit(arr):
    size = len(arr) 
    _quickSortLoop_jit(arr, 0, size-1)
