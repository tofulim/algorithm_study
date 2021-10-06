def search(n,wire_map,start,v2):
    visit=[False]*n
    visit[start]=True
    queue=[start]
    cnt=1
    while queue:
        start=queue.pop(0)
        for idx,i in enumerate(wire_map[start]):
            if i==0 or idx==v2 or visit[idx]:
                continue
            visit[idx]=True
            queue.append(idx)
            cnt+=1
    
    return cnt

def solution(n, wires):
    wire_map=[[0]*n for _ in range(n)]
    answer = 10000000
    
    for (v1,v2) in wires:
        wire_map[v1-1][v2-1]=1
        wire_map[v2-1][v1-1]=1
    
    for (v1,v2) in wires:
        answer=min(abs(search(n,wire_map,v1-1,v2-1)-search(n,wire_map,v2-1,v1-1)),answer)
    
    return answer