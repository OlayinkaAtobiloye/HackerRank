#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    no_toys = 0
    for price in prices:
        if price <= k:
            k -= price
            no_toys += 1
        else:
            break
    return no_toys

