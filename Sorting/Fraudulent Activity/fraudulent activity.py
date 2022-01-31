#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def calculatemedian(arr):
    mid = len(arr) // 2
    median = (arr[mid] + arr[~mid]) / 2
    return median


def pop_and_insort(arr, oldval, newval):
    index = bisect.bisect_left(arr, oldval)
    arr.pop(index)
    bisect.insort_right(arr, newval)
    return arr


def activityNotifications(expenditure, d):
    # Write your code here
    notices = 0
    trailingdays = []
    for day in range(d, len(expenditure)):
        if not trailingdays:
            trailingdays = expenditure[day - d: day]
            trailingdays.sort()
        oldval = expenditure[day - d]
        newval = expenditure[day]

        median = (calculatemedian(trailingdays))
        trailingdays = pop_and_insort(trailingdays, oldval, newval)

        if expenditure[day] >= 2 * median:
            notices += 1
    return notices
