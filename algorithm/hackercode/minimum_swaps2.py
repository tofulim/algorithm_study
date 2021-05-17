#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    idx_num_dict=dict()
    num_idx_dict=dict()
    for idx,num in enumerate(arr): #initiate dict
        idx_num_dict[idx+1]=num
        num_idx_dict[num]=idx+1
    
    cnt=0
    for now_val in arr:
        now_idx=num_idx_dict[now_val]
        other_val=idx_num_dict[now_val]
        other_idx=num_idx_dict[other_val]
        
        if now_val==now_idx: #stay
            # print(now_val,": could stay")
            continue
        elif idx_num_dict[now_val]==now_idx:#meet owner
            # print(now_val,now_idx,": bidirectional change")
            idx_num_dict[now_idx]=other_val
            num_idx_dict[now_val]=other_idx
            idx_num_dict[other_idx]=now_val
            num_idx_dict[other_val]=now_idx
            cnt+=1
        else :#one-sided exchange
            idx_num_dict[now_idx]=other_val
            num_idx_dict[now_val]=other_idx
            idx_num_dict[other_idx]=now_val
            num_idx_dict[other_val]=now_idx
            # print(now_val,other_val,": one-directional change")
            cnt+=1
            
    return cnt
            
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
