import heapq

def solution(operations):
    queue=[]
    for oper in operations:
        oper,num=oper.split()
        num=int(num)
        if oper=='I':
            heapq.heappush(queue,num)
        elif queue:
            queue.pop() if num>0 else heapq.heappop(queue)    
            
    return [max(queue),min(queue)] if queue else [0,0]