#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    n=len(container)
    row_sum,col_sum=[0]*n,[0]*n
    for i in range(n):
        r_cnt=0
        for j in range(n):
            value=container[i][j]
            r_cnt+=value
            col_sum[j]+=value
        row_sum[i]=r_cnt
    
    answer=[False]*n
    for i in range(n):
        for j in range(n):
            if row_sum[i]==col_sum[j]:
                answer[j]=True
    
    print(answer)
    return "Possible" if sum(answer)==n else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
