#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    s_counter=Counter([item%k for item in s])
    answer=0
    if s_counter[0]>0:
        answer+=1
        
    for i in range(1,k//2+1):
        if i*2==k:
            answer+=1
        else :
            answer+=max(s_counter[i],s_counter[k-i])
    
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
