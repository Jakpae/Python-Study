# Module MyList.py

import random

# 랜덤 난수 생성을 위한 genRandList 생성


def genRandList(L, size):
    L = []
    L = random.sample(range(0, size), size)
    return L

# 리스트 출력을 위한 printListSample 생성


def printListSample(L, per_line, sample_lines):
    count = 0
    size = len(L)
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

# 리스트 셔플을 위한 shuffleList 생성


def shuffleList(L):
    random.shuffle(L)
    return L
