#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    string = s
    count = 0
    if len(string) >= n:
        for index in range(n):
            if string[index] == 'a':
                count += 1
        return count
    else:
        for letter in string:
            if letter == 'a':
                count += 1 
        multiplyingFactor = n//len(string)
        count *= multiplyingFactor
        remainder = n % len(string)
        for letter in string[:remainder]:
            if letter == 'a':
                count += 1
    return count



