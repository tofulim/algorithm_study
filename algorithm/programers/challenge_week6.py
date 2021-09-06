def solution(weights, head2head):
    answer = []
    length=len(weights)
    for idx, fight_arr in enumerate(head2head):
        my_weight=weights[idx]
        upper_win,win_rate,win,total=0,0,0,0
        for other_idx in range(length):
            res=fight_arr[other_idx]
            if res=='W':
                    total+=1
                    win+=1
                    if my_weight<weights[other_idx]:
                        upper_win+=1
            elif res=='L':
                total+=1
            win_rate=win/total if total!=0 else 0
        #승률, 상위체급 승리 횟수, 내 몸무게, 내 번호가 담긴 튜플 push
        answer.append((win_rate,upper_win,my_weight,idx+1))
    #4중 정렬 후 맨 마지막 index를 map으로 뽑아온다
    return list(map(lambda x:x[3],sorted(answer,key=lambda x: (-x[0],-x[1],-x[2],x[3]))))