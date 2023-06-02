# MyLIst
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : Aprll 29, 2023
# Major features :
# - Create a custom module for Python function genNonDuplicatedRandomList(size) that generates and returns a specified number of non-overlapping integer random numbers
# - Python function that samples the first and last lines of the elements in the list printListSample(L, per_line, sample_lines)

import random

# random 모듈을 이용해 size만큼의 난수를 생성한후 리스트 L에 저장
def genNonDeuplicatedRandomList(size):
    L = []
    L = random.sample(range(0,size), size)
    return L

# 리스트의 포함된 원소들을 출력하는 함수 printListSample 구현
def printListSample(L, per_line, sample_lines):
    count = 0
    size = len(L)
    # 리스트의 앞 원소 20개를 출력
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
        # 리스트의 뒤 원소 20개를 출력
        if count < (size - per_line * sample_lines):
            count = size - per_line * sample_lines
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

