from itertools import combinations
import sys

def get_dots(lines):
    dots=set()
    x,y=0,0
    for (line1,line2) in combinations(lines,2):
        x1,y1,a1=line1
        x2,y2,a2=line2
        if x1*y2-x2*y1==0:#직교 or 일치
            continue
        else:
            x=(y1*a2-a1*y2)/(x1*y2-y1*x2)
            y=(a1*x2-x1*a2)/(x1*y2-y1*x2)
            
        if x.is_integer() and y.is_integer():
            dots.add((int(y),int(x)))
    return dots
    
def solution(line):
    dots=list(get_dots(line))
    max_num = sys.maxsize
    n1,m1,n2,m2=max_num,max_num,-max_num,-max_num
    for (i,j) in dots:
        n1=min(n1,i)
        m1=min(m1,j)
        n2=max(n2,i)
        m2=max(m2,j)
    
    n,m=n2-n1+1,m2-m1+1
    answer=[['.']*m for _ in range(n)]
    for (i,j) in dots:
        answer[n2-i][j-m1]='*'
    return [''.join(a) for a in answer]