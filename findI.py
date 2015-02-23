__author__ = 'amir'

import array
import math


def main():
    """
    Test file for the two parts of the question
    """
    arr = []
    val = -4
    for i in range(12):
        arr.append(val)
        val += 2
    find(arr, 0)


def find(arr, offset):
    if len(arr) == 1:
        if arr[0] == offset:
            return True
        else:
            return False
    half = math.floor(len(arr) / 2)
    left = arr[:half]
    right = arr[half:]

    if arr[half] > (half + offset):
        return find(left, offset)
    else:
        return find(right, half + offset)


if __name__ == '__main__':
    main()