import random, time

from MyArray import *
from MySortings import *
import numpy as np


if __name__ == "__main__":
    Test_size = [1000, 100000, 1000000, 10000000]
    print("\nComparing sort algorithms")
    for size in Test_size:
        A = np.arange(size)
        np.random.shuffle(A)
        print("Before quick_sort() of A :")
        printArraySample(A, 10, 2)
        t1 = time.time()
        quick_sort(A) # basic quick_sort() in divide-and-conquer
        t2 = time.time()
        print("After quick_sort() of A :")
        printArraySample(A, 10, 2)
        time_elapsed_ms = (t2 - t1) * 1000
        print("quick_sort() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        np.random.shuffle(A)
        print("\nBefore quick_sort_jit() of A :")
        printArraySample(A, 10, 2)
        t1 = time.time()
        quick_sort_jit(A) # quick_sort with @jit of Numba
        t2 = time.time()
        print("After quick_sort_jit() of A :")
        printArraySample(A, 10, 2)
        time_elapsed_ms = (t2 - t1) * 1000
        print("quick_sort_jit() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        np.random.shuffle(A)
        print("\nBefore np.sort() of A :")
        printArraySample(A, 10, 2)
        t1 = time.time()
        sorted_A = np.sort(A) # Numpy sort() (quick_sort() implemented in C/C++)
        t2 = time.time()
        print("After np.sort() of A :")
        printArraySample(sorted_A, 10, 2)
        time_elapsed_ms = (t2 - t1) * 1000
        print("np.sort() took {:8.2f} msec to sort a numpy array of size ({:8d})".format(time_elapsed_ms, size))
        print()