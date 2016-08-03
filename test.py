#!/usr/bin/env python3
import random
import sys
import timeit
from bogosort import bogo_sort
from insertionsort import insertion_sort
from mergesort import merge_sort_init
from quicksort import quick_sort_init, quick_sort_hoare_init, quick_sort_random_init


# arr: array to sort
# method: a sorting function which takes one argument (arr)
# returns: run time in seconds
def time_sort(arr, method):
    duplicate_arr = list(arr)

    sys.setrecursionlimit(10000)    # for sorting very large lists
    start = timeit.default_timer()
    method(duplicate_arr)
    stop = timeit.default_timer()

    return stop-start


# arr: array to be sorted
# method: a sorting function which takes one argument (arr)
# iterations: number of times to sort list
# returns: prints average time of all iterations
def test_sort(arr, method, iterations=1):
    avg_time = 0
    for i in range(iterations):
        avg_time += time_sort(arr, method)
    avg_time /= iterations
    print(round(avg_time, 4))


def python_sort(a):
    a.sort()


def main():
    iterations = 500

    arr = []
    size = int(input('How many numbers do you want to sort? '))

    for i in range(size):
        arr.append(random.randint(0, 1000))

    print('built in python sort')
    test_sort(arr, python_sort, iterations)
    print('quick sort')
    test_sort(arr, quick_sort_init, iterations)
    print('quick sort w/ hoare partitioning')
    test_sort(arr, quick_sort_hoare_init, iterations)
    print('quick sort with randomized partitioning')
    test_sort(arr, quick_sort_random_init, iterations)
    print('merge sort')
    test_sort(arr, merge_sort_init, iterations)
    print('insertion sort')
    test_sort(arr, insertion_sort, iterations)
    # uncomment if you want this to run until the end of time
    # print("bogo sort (I hope you're feeling lucky)")
    # test_sort(arr, bogo_sort)


if __name__ == "__main__":
    main()
