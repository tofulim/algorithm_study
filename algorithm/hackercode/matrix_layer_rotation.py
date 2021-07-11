#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
def rotation(matrix,i1,j1,i2,j2,r):
    arr=[]
    for j in range(j1,j2): #오른쪽
        arr.append(matrix[i1][j])
    for i in range(i1,i2): #아래
        arr.append(matrix[i][j2])
    for j in range(j2,j1,-1): #왼쪽
        arr.append(matrix[i2][j])
    for i in range(i2,i1,-1): #위
        arr.append(matrix[i][j1])
    
    rotate_num=r%((i2-i1)*2+(j2-j1)*2) #회전시킬 횟수 구함
    arr=arr[rotate_num:]+arr[:rotate_num] #회전
    #본 배열 변경시킴
    for j in range(j1,j2):
        matrix[i1][j]=arr.pop(0)
    for i in range(i1,i2):
        matrix[i][j2]=arr.pop(0)
    for j in range(j2,j1,-1):
        matrix[i2][j]=arr.pop(0)
    for i in range(i2,i1,-1):
        matrix[i][j1]=arr.pop(0)

def matrixRotation(matrix, r):
    # Write your code here
    i1,j1,i2,j2=0,0,len(matrix)-1,len(matrix[0])-1
    for rot in range(min(len(matrix),len(matrix[0]))//2):
        rotation(matrix,i1,j1,i2,j2,r)
        i1+=1
        j1+=1
        i2-=1
        j2-=1

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
    for i in range(m):
        print(*matrix[i])
