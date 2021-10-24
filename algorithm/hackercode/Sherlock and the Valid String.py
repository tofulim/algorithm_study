#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter,defaultdict
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    str_counter=Counter(s)
    reverse_counter=defaultdict(list)
    for key,value in str_counter.items():
        reverse_counter[value].append(key)
    
    keys=list(reverse_counter.keys())
    
    if len(keys)==1:
        return "YES"
    elif len(keys)==2:
        min_key=min(keys)
        max_key=max(keys)
        if min_key==1 and len(reverse_counter[min_key])==1:
            return "YES"
        elif max_key-min_key==1 and len(reverse_counter[max_key])==1:
            return "YES" 
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
