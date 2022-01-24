#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sock_dict = {}
    sock_pair = 0
    for sock_color in ar:
        if sock_color not in sock_dict:
            sock_dict[sock_color] = 1
        else:
            sock_dict[sock_color] = sock_dict[sock_color] + 1

    for sock in sock_dict.keys():
        sock_pair += sock_dict[sock] // 2
    return sock_pair



