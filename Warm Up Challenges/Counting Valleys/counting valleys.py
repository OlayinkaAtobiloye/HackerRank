#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    mountain = 0
    valley = 0
    reference = 0
    for step in path:
        if reference == 0:
            starting_point = step

        if step == 'D':
            reference -= 1
        else:
            reference += 1

        if reference == 0:
            if starting_point == 'U':
                mountain += 1
            else:
                valley += 1
    return valley



