#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    min_diff = sys.maxsize
    n = len(arr)
    for index in range(n - 1):
        diff = abs(sorted_arr[index] - sorted_arr[index + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff


