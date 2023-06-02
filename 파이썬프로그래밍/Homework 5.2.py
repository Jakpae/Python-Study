# Homework 5.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 3, 2023
# Major features :
# - Configuring Recursive Functions with Memo Functions
# - Measure the elapsed time taken by the recursive function dynFibo(n) using the time() function

import time  # 시간을 계산하기 위한 time모듈 import

memo = dict()  # 메모 기능을 사용하기 위한 메모 dict 추가


def dynFibo(n):
    if n in memo:  # 만약 n이 메모에 있다면 메모에 있는 n의 값을 리턴시킴
        return memo[n]
    if n == 1:  # 만약 n이 1 이거나 2라면 1을 리턴시킴
        return 1
    elif n == 2:
        return 1
    # 파보나치 수열을 계산하기 위한 식. 메모 기능을 사용하지 않으면 파보나치 수열의 시간 복잡도는 O(n^2)이므로 메모 기능을 사용하는거임
    else:
        temp = dynFibo(n-1) + dynFibo(n-2)
        memo[n] = temp
        return temp  # 계산된 값 temp을 리턴시킴


# 시작과 끝 간격의 정수를 문자열 형태로 입력받은후 split을 통해 나눠진후 map을 이용해 문자열에서 정수형태로 변환되어 각각 start,stop,step이 됨
(start, stop, step) = tuple(
    map(int, input("Input start, stop, step of Fibonacci series : ").split()))

# for 반복은 for i in range(0,5)라고 하면 4까지 반복되므로 stop+1을 하여 stop까지 반복되게 함
for n in range(start, stop+1, step):
    t1 = time.time()
    fibo_n = dynFibo(n)
    t2 = time.time()
    t_elapse_us = t2 - t1
    print("dynFibo({:3d}) = {:25d}, took {:10.2f}[micro_sec]".format(
        n, fibo_n, t_elapse_us))
