#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    answer=[]
    ranked=sorted(set(ranked))
    ranked_len=len(ranked)+1
    
    for p in player:
        answer.append(ranked_len-bisect_right(ranked,p))
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
