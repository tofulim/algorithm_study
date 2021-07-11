#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    cnt=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                cnt+=1
    
    return "YES" if cnt%2==0 else "NO"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        
        fptr.write(result + '\n')

    fptr.close()
