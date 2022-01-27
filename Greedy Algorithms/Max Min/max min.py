#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    length = len(arr)
    min_diff = sys.maxsize
    for index in range(0, length):
        if (index + k - 1) < length:
            diff = arr[index + k -1] - arr[index]
            if diff < min_diff:
                min_diff = diff
        else:
            return min_diff
    return min_diff
