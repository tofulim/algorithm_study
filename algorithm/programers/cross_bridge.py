def solution(stones, k):
    answer=0
    left=1
    right=200000000
    while left<=right:
        mid=(left+right)//2
        cnt=0
        for stone in stones:
            if stone-mid<=0:
                cnt+=1
            else :
                cnt=0
            if cnt>=k:
                break
                
        if cnt<k:
            left=mid+1
        else :
            answer=mid
            right=mid-1
            
    return answer