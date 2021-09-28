import sys
def solution(n, times):
    answer = 0
    left=1
    right=sys.maxsize
    while left<=right:
        mid=(left+right)//2
        num=sum([mid//time for time in times])
        if num<n:
            left=mid+1
        else:
            answer=mid
            right=mid-1
            
    return answer