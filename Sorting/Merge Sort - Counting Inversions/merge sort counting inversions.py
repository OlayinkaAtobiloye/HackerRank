#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


# O(nlogn + n) runtime

def merge(left, right):
    inversions = 0
    arr = []
    while True:
        if len(right) == 0:
            arr = arr + left
            break
        if len(left) == 0:
            arr = arr + right
            break
        if left[0] <= right[0]:
            arr.append(left[0])
            left.pop(0)
        else:
            inversions += len(left)
            arr.append(right[0])
            right.pop(0)
    return inversions, arr


def sort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        arr1, count1 = sort(left)
        arr2, count2 = sort(right)
        swaps, newarr = merge(arr1, arr2)
    return newarr, count1 + count2 + swaps


def countInversions(arr):
    # Write your code here
    # swaps = 0
    # swaps += merge(sort(left), sort(right))
    newarr, inversions = sort(arr)
    return inversions


# A faster algo - O(nlogn)


def merge(left, right):
    inversions = 0
    arr = []
    i_left = 0
    i_right = 0
    len_left = len(left)
    len_right = len(right)
    while True:
        if i_right == len_right:
            arr = arr + left[i_left:]
            break
        if i_left == len_left:
            arr = arr + right[i_right:]
            break
        # for i in range(len_left):
        if left[i_left] <= right[i_right]:
            arr.append(left[i_left])
            i_left += 1
        else:
            inversions += len_left - i_left
            arr.append(right[i_right])
            i_right += 1
    return inversions, arr


def sort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        arr1, count1 = sort(left)
        arr2, count2 = sort(right)
        swaps, newarr = merge(arr1, arr2)
    return newarr, count1 + count2 + swaps


def countInversions(arr):
    # Write your code here
    newarr, inversions = sort(arr)
    return inversions


