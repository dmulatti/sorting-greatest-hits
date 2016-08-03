#!/usr/bin/env python3
import random


def merge(arr, p, q, r):
    first_half = arr[p:q + 1]
    second_half = arr[q + 1:r + 1]

    # print('merging ' + str(first_half) + ' and ' + str(second_half))

    k = p
    i = 0
    j = 0

    while (i < len(first_half)) and (j < len(second_half)):
        if first_half[i] < second_half[j]:
            arr[k] = first_half[i]
            i += 1
        else:
            arr[k] = second_half[j]
            j += 1
        k += 1

    while i < len(first_half):
        arr[k] = first_half[i]
        i += 1
        k += 1

    while j < len(second_half):
        arr[k] = second_half[j]
        j += 1
        k += 1

    # print(arr[p:k])


def merge_sort(arr, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


def merge_sort_init(arr):
    merge_sort(arr, 0, (len(arr) - 1))


def main():
    arr = []
    size = input('How many numbers do you want to sort? ')

    for i in range(int(size)):
        arr.append(random.randint(0, 100))

    print(arr)
    merge_sort_init(arr)
    print(arr)

if __name__ == "__main__":
    main()
