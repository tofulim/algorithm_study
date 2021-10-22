#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    sorted_w=sorted(w)
    if len(w)==1 or w==reversed(sorted_w):
        return "no answer"
    arr_w=list(w)
    for idx in range(len(w)-2,-1,-1):
        alpha=arr_w[idx]
        for idx2 in range(len(w)-1,idx,-1):
            next_alpha=w[idx2]
            if alpha<next_alpha:
                tmp=next_alpha
                arr_w[idx2]=alpha
                arr_w[idx]=tmp
                return ''.join(arr_w[:idx+1]+sorted(arr_w[idx+1:]))
            
    return "no answer"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
