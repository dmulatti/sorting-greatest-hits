#!/usr/bin/env python3
import random
import timeit
from bogosort import bogo_sort
from insertionsort import insertion_sort
from mergesort import merge_sort_init


def test_sort(arr, method, print_output):
    print(method.__name__)

    duplicate_arr = list(arr)
    if print_output:
        print(duplicate_arr)

    start = timeit.default_timer()
    method(duplicate_arr)
    stop = timeit.default_timer()

    if print_output:
        print(duplicate_arr)
    print(str(round(stop-start, 4)) + 's')


def main():
    # change if you want to see the arrays before/after sorting
    print_output = False

    arr = []
    size = int(input('How many numbers do you want to sort? '))

    for i in range(size):
        arr.append(random.randint(0, 1000))

    test_sort(arr, sorted, print_output)
    test_sort(arr, merge_sort_init, print_output)
    test_sort(arr, insertion_sort, print_output)
    # uncomment if you want this to run until the end of time
    # test_sort (arr, bogo_sort, printoutput)


if __name__ == "__main__":
    main()
