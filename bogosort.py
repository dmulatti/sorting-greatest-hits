#!/usr/bin/env python3
import random


# possible O(n) runtime!
def bogo_sort(arr):

    def is_sorted(a): return all(a[i-1] <= a[i] for i in range(1, len(a)))

    while not is_sorted(arr):
        random.shuffle(arr)


def main():
    arr = []
    size = input('How many numbers do you want to sort? ')

    for i in range(int(size)):
        arr.append(random.randint(0, 1000))

    print(arr)
    bogo_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
