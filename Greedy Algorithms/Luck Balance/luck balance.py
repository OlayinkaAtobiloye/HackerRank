#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    luck = 0
    limit = 0
    contests = sorted(contests, reverse=True)
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        else:
            if limit < k:
                luck += contest[0]
            else:
                luck -= contest[0]
            limit += 1
    return luck
