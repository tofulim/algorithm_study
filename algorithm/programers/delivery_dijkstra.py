from collections import defaultdict
import heapq

def solution(N, road, K):
    #다익스트라
    answer=[500000]*N
    answer[0]=0
    
    cost_map=defaultdict(list)
    for city in road:
        c1,c2,cost=city
        cost_map[c1-1].append((c2-1,cost))
        cost_map[c2-1].append((c1-1,cost))
        
    queue=[]
    heapq.heappush(queue,(0,0))
    
    while queue:
        cost,now=heapq.heappop(queue)
        
        if answer[now]<cost:
            continue
            
        for node in cost_map[now]:
            next_node,next_cost=node
            new_cost=next_cost+cost
            if answer[next_node]>new_cost:
                answer[next_node]=new_cost
                heapq.heappush(queue,(new_cost,next_node))
                
    return len(list(filter(lambda x:x<=K,answer)))