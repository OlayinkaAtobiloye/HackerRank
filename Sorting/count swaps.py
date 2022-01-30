#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap = 0
    for element in a:
        for index in range(len(a) - 1):
            if a[index] > a[index + 1]:
                temp = a[index]
                a[index] = a[index + 1]
                a[index + 1] = temp
                swap += 1
    print("Array is sorted in " + str(swap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

