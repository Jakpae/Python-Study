# 실습 6.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 7, 2023
# Major features :
# - Configuring Recursive Functions with Memo Functions
# - Measure the elapsed time taken by the recursive function dynFibo(n) using the time() function

import time

# 피보나치 정렬의 계산 복잡도를 줄이기 위한 메모 딕셔너리 생성
memo = dict()

# 피보나치 수열을 위한 dynFibo 함수 생성


def dynFibo(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = n  # 만약 dynFibo가 메모에 있다면 메모의 있는 값을 불러와 return 시킴
        return n
    else:
        fn = dynFibo(n-1) + dynFibo(n-2)  # 피보나치 수열 계산
        memo[n] = fn
        return fn  # 계산된 값 리턴


if __name__ == '__main__':
    # 시작점 종료점 그리고 간격을 입력받아 정수로 바꾸고 각각 start,stop,step에 넣음
    (start, stop, step) = tuple(map(int,
                                    input("input start, stop, step of Fibonacci series : ").split(' ')))
    for n in range(start, stop+1, step):
        t_before = time.time()  # 시간 쟤기 시작
        fibo_n = dynFibo(n)
        t_after = time.time()  # 시간 쟤기 종료
        t_elapse_sec = t_after - t_before  # after-before를 하여서 피보나치 수열에 걸린 시간 측정
        t_elapse_ms = t_elapse_sec * 1000
        print("dynFibo({:3d}) = {:45d}, took {:10.2f}[milli_sec]".format(
            n, fibo_n, t_elapse_ms))
