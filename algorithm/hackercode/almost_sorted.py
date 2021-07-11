#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def swap(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp
    
def reverse_arr(a,b,arr):
    arr[a:b+1]=list(reversed(arr[a:b+1]))
    
def almostSorted(arr):
    # Write your code here
    start_idx=0
    for i in range(0,len(arr)-1):
        cnt=0
        if arr[i+1]>arr[i]: continue
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                cnt+=1
        start_idx=i
        break
    # print(cnt)
    method="swap"
    answer="no"
    
    end_idx=start_idx+cnt
    # print(cnt,start_idx,end_idx)
    
    swap(start_idx,end_idx,arr)
    
    if sorted(arr)!=arr:
        method="reverse"
        swap(end_idx,start_idx,arr)
        reverse_arr(start_idx,end_idx,arr)
        
    if sorted(arr)==arr:
        answer="yes"+f'\n{method} {start_idx+1} {end_idx+1}'
    
    return answer
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    answer=almostSorted(arr)
    print(answer)