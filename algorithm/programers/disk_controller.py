from queue import PriorityQueue

def solution(jobs):
    jobs.sort(key=lambda x:(x[0], x[1]))
    answer = 0
    count=0
    last=-1
    timestamp=jobs[0][0]
    jobs_len=len(jobs)
    
    pq=PriorityQueue()
    
    while count < jobs_len:
        
        for req_time,proc_time in jobs:
            if last<req_time<=timestamp:
                pq.put((proc_time,[req_time,proc_time]))
                
        if pq.qsize()>0:
            req_time,proc_time=pq.get()[1]
            last=timestamp
            timestamp+=proc_time
            count+=1
            answer+=timestamp-req_time
        else :
            timestamp+=1
    
    return answer//jobs_len