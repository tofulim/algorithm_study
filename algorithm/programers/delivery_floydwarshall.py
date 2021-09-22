def solution(N, road, K):
    #플로이드 와샬
    cost_map=[[500000]*N for i in range(N)]
    for i in range(N):
        cost_map[i][i]=0
        
    for city in road:
        c1,c2,cost=city
        cost_map[c1-1][c2-1]=min(cost,cost_map[c1-1][c2-1])
        cost_map[c2-1][c1-1]=min(cost,cost_map[c2-1][c1-1])
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                cost_map[j][k]=min(cost_map[j][k],cost_map[j][i]+cost_map[i][k])
    
    return len(list(filter(lambda x:x<=K,cost_map[0])))