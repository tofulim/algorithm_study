#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes=0
    
    min1=100000
    min2=100001
    
    for (idx,val) in zip([_ for _ in range(len(q),0,-1)],list(reversed(q))):
        bribe=0
        if val-idx>2:
            print("Too chaotic")
            return
        elif val>min2:
            bribe+=2
        elif val<min2 and val>min1:
            bribe+=1
            min2=val
        else :
            min2=min1
            min1=val
            
        bribes+=bribe    
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
