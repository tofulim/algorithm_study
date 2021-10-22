#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    g_len=len(G)
    g_col_len=len(G[0])
    p_len=len(P)
    p_col_len=len(P[0])
    
    offset=str(g_col_len-p_col_len+1)
    concated_g='.'.join(G)
    
    pattern=''
    for i in range(p_len):
        if i!=p_len-1:
            pattern+='(' + P[i] + ').{' + offset + '}'
        else :
            pattern+='(' + P[i] + ')'
            
    if re.search(pattern,concated_g):
        return "YES"
    return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
