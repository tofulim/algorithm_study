from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for perm in permutations(range(len(dungeons)),len(dungeons)):
        energy=k
        cnt=0
        for idx in perm:
            req_energy,cost_energy=dungeons[idx]
            if energy<req_energy:
                break
            energy-=cost_energy
            cnt+=1
        answer=max(answer,cnt)
        
    return answer