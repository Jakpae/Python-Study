# MySortings
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : June 2, 2023

from numba import jit, njit, prange


@jit(nopython=True) # Numba JIT 컴파일러를 사용하여 함수를 미리 컴파일
def _partition_jit(arr, left, right, pi):
    '''
    배열 arr에서 left 인덱스와 right 인덱스 사이의 값들을 퀵소트 알고리즘으로렬하여
    left 부터 right까지 위쪽과 아래쪽으로 나누고, pi 인덱스의 값을 피봇으로 설정하여
    피봇 기준으로 양쪽을 분할하는 과정을 수행하는 함수
    '''
    pv = arr[pi] #피봇 값을 arr[pi]로 설정
    arr[pi], arr[right] = arr[right], arr[pi] # 피봇과 오른 쪽 끋 값(right)를 교체
    npi = i = left # npi와 i를 left로 초기화
    while (i<=right-1): # 조건문이 만족하는 동안 반복문 실행
        if (arr[i] <= pv): # 만약 arr[i]가 피봇보다 작거나 같으면 실행
            arr[npi], arr[i] = arr[i], arr[npi] # arr[i]와 arr[npi]를 교환
            npi += 1 # 새로운 피봇(npi)를 하나 증가시킴
        i += 1
    arr[npi], arr[right] = arr[right], arr[npi] # 새로운 피봇 위치(npi)와 오른쪽 끝 값(right)를 교환
    return npi # npi 반환


@jit(nopython=True)
def _hybridSortLoop_jit(arr, left, right, ss_cutoff):
    """
    배열 arr에서 left 인덱스와 right 인덱스 사이의 값들을 Quick sort과 Insertion sort를
    혼합한 하이브리드 정렬 알고리즘으로 정렬하는 함수.
    """
    if (left >= right): # 왼족 인덱스가 오른쪽 인덱스와 같거나 큰 경우,더 이상 정렬할 필요가 없음, 즉 구간의 길이가 0이면 실행
        return
    if (right - left) <= ss_cutoff: # 만약 인덱스 사이의 길이가 ss_cutoff 이하라면, 즉 배열의 길이가 threshold 이하일 경우 Insertion Sort를 수행
        for i in range(left, right+1):
            min_v = arr[i]
            min_idx = i
            for j in range(i, right+1):
                if arr[ j] < min_v:
                    min_v = arr[ j]
                    min_idx = j
                if min_idx != i:
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return
    pi = (left + right) // 2 # 배열의 가운데 인덱스를 피봇으로 설정
    new_pi = _partition_jit(arr, left, right, pi)
    if (left < new_pi -1): # 새로운 피봇의 왼쪽 부분을 다시 정렬
        _hybridSortLoop_jit(arr, left, new_pi-1, ss_cutoff)
    if (new_pi + 1 < right): # 새로운 피봇의 오른쪽 부분을 다시 정렬
        _hybridSortLoop_jit(arr, new_pi+1, right, ss_cutoff)


@jit(nopython=True)
def hybrid_sort_jit(arr, ss_cutoff):
    left, right = 0, len(arr) -1 # 정렬할 구가의 인덱스(left,right)
    _hybridSortLoop_jit(arr, left, right, ss_cutoff)