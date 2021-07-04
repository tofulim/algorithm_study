#해당 시작점에서 가장 최소비용인 노드부터 찾는다
def get_smallest(now_arr,visit):
    small_idx=0
    small_value=100000000
    for idx, value in enumerate(now_arr):
        if not visit[idx] and value<small_value:
            small_value=value
            small_idx=idx
            
    return small_idx
#해당 시작점에서 모든 노드들을 방문했을 때 최소비용을 계산하여 하나의 행을 내놓는다
def dijkstra(now,n,fare_arr,visit):
    now_arr=fare_arr[now]
    for idx in range(n-2):
        min_idx=get_smallest(now_arr,visit)
        visit[min_idx]=True
        
        base_value=now_arr[min_idx]
        for next_idx in range(n):
            now_arr[next_idx]=min(now_arr[next_idx],fare_arr[min_idx][next_idx]+base_value)
        
    return now_arr
    
def solution(n, s, a, b, fares):
    answer = 100000000
    max_fare=100000000
    final_arr=[]
    #make fare_arr
    fare_arr=[[max_fare]*n for _ in range(n)]
    for start,end,fare in fares:
        fare_arr[start-1][end-1]=fare
        fare_arr[end-1][start-1]=fare

    for now in range(n):
        visit=[False]*n
        visit[now]=True
        final_arr.append(dijkstra(now,n,fare_arr,visit))
    
    #움직일 필요가 없는 자기자신이 출발지이자 도착지일 경우 0으로 처리해준다
    for idx in range(n):
        final_arr[idx][idx]=0
    #중간지점의 idx와 중간지점까지 가는데 필요한 비용을 추출한다
    for idx, middle_value in enumerate(final_arr[s-1]):
        #중간지점부터 A/B까지 가는데 필요한 비용
        a_distance=final_arr[idx][a-1]
        b_distance=final_arr[idx][b-1]
        answer=min(answer,middle_value+a_distance+b_distance)

    return answer