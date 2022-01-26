#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    mincost = 0
    purchase_round = 0
    arrayCount = 0
    for cost in c:
        if arrayCount < k:
            mincost += (purchase_round + 1) * cost
        else:
            arrayCount = 0
            purchase_round += 1
            mincost += (purchase_round + 1) * cost
        arrayCount += 1

    return mincost