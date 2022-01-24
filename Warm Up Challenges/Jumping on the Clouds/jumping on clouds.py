#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import cycle


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    consecutive = 0
    last_cloud = 1
    for index, cloud in enumerate(c):
        if index == (len(c) - 1):
            return jump

        next_cloud = c[index + 1]
        if cloud == 1:
            last_cloud = cloud
        elif last_cloud == 0 and next_cloud == 0:
            last_cloud = 1
        else:
            jump += 1
            last_cloud = cloud
    return jump


