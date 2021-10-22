#!/bin/python3

import math
import os
import random
import re
import sys
import math
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s=s.replace(' ','')
    L=math.sqrt(len(s))
    r_len,c_len=math.floor(L),math.ceil(L)
    str_arr=[list() for _ in range(c_len)]
    for idx,s in enumerate(s):
        str_arr[idx%c_len].append(s)
    
    return ' '.join(map(lambda x: ''.join(x),str_arr))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
