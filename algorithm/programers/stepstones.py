def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks_len=len(rocks)
    left=0
    right=distance
    
    while left<=right:
        mid=(left+right)//2
        rock_cnt=0
        last_rock=0
        for i in range(rocks_len-1): #모든 돌다리를 건널 때 현재 최소값 mid보다 큰 돌 몇개인지 확인
            if rocks[i]-last_rock>=mid:
                rock_cnt+=1
                last_rock=rocks[i]
        
        if (rocks[rocks_len-1]-last_rock)>=mid and (distance-rocks[rocks_len-1])>=mid :
            rock_cnt+=1 #마지막 돌과 마지막 도착지점 고려
        
        if rocks_len-rock_cnt > n: #뺀 돌이 n개보다 많을 때 거리를 좁혀줘야 함
            right=mid-1
        else: # n개보다 적개 빼서 짧은 거리를 순회했으므로 거리를 늘려줌
            left=mid+1
            answer=mid 
        
    return answer