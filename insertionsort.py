#!/usr/bin/env python3
import random


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (arr[i] > key) and (i >= 0):
            # move everything over
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key    # insert into proper spot
    return arr


def main():
    arr = []
    size = input('How many numbers do you want to sort? ')

    for i in range(int(size)):
        arr.append(random.randint(0, 1000))

    print(arr)
    insertion_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()
