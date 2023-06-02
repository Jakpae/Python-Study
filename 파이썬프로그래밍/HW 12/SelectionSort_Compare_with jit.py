import random, time
from numba import jit, njit, prange
import numpy as np


def selectionSort(L):
    size = len(L)
    for i in range(0, size-1):
        min_idx = i
        for j in range(i+1,size):
            if(L[min_idx] > L[j]):
                min_idx = j
        if (min_idx != i):
            L[min_idx], L[i] = L[i], L[min_idx]


@jit(nopython=True)
def selectionSort_jit(L):
    size = len(L)
    for i in range(0, size-1):
        min_idx = i
        for j in range(i+1,size):
            if(L[min_idx] > L[j]):
                min_idx = j
        if (min_idx != i):
            L[min_idx], L[i] = L[i], L[min_idx]


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
            

if __name__ == "__main__":
    L_size = [10000, 50000, 100000]
    print("\nTesting selection sorting algorithms") 
    for size in L_size:
        A = np.arange(size) 
        random.shuffle(A)
        print("\nBefore @jit_Selection-Sort of A :") 
        printListSample(A, 10, 2)
        t1 = time.time()
        selectionSort_jit(A)
        t2 = time.time()
        time_elapsed = t2 - t1
        print("\nAfter @jit_Selection-Sort of A :") 
        printListSample(A, 10, 2)
        print("@jit Selection sorting took {} sec to sort a list(size = {})".format(time_elapsed, size))
        print("\nBefore simple Selection-Sort of A :") 
        random.shuffle(A)
        printListSample(A, 10, 2)
        t1 = time.time()
        selectionSort(A)
        t2 = time.time()
        print("After simple Selection-Sort of A .....") 
        printListSample(A, 10, 2)
        time_elapsed = t2 - t1
        print("Simple Selection sorting took {} sec to sort a list (size = {})".format(time_elapsed, size))