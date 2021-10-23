#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    n=len(A)
    m=len(A[0])
    bird_view=sum([True if a!=0 else False for arr in A for a in arr])
    side_view1=0
    for i in range(n):
        max_val=0
        for j in range(m):
            now_val=A[i][j]
            if now_val>max_val:
                side_view1+=now_val-max_val
                max_val=now_val
            else:
                max_val=now_val
                
    side_view2=0
    for i in range(m):
        max_val=0
        for j in range(n):
            now_val=A[j][i]
            if now_val>max_val:
                side_view2+=now_val-max_val
                max_val=now_val
            else:
                max_val=now_val
    
    side_view3=0
    for i in range(n):
        max_val=0
        for j in reversed(range(m)):
            now_val=A[i][j]
            if now_val>max_val:
                side_view3+=now_val-max_val
                max_val=now_val
            else:
                max_val=now_val
    
    side_view4=0
    for i in range(m):
        max_val=0
        for j in reversed(range(n)):
            now_val=A[j][i]
            if now_val>max_val:
                side_view4+=now_val-max_val
                max_val=now_val
            else:
                max_val=now_val
                
    return bird_view*2+side_view1+side_view2+side_view3+side_view4
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
