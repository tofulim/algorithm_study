#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    dict_arr=defaultdict(list)
    for idx,(num,alpha) in enumerate(arr):
        if idx<len(arr)//2:
            alpha='-'
        dict_arr[int(num)].append(alpha)
    
    print(' '.join(list(map(lambda x:' '.join(x), [dict_arr[num] for num in sorted(list(dict_arr.keys()))]))))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
