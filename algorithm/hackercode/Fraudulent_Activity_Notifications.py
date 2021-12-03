def get_median(counter,d): #중앙값 구하기
    idx_count=0
    for i, val in enumerate(counter): #빈도 누적합 구하기
        idx_count+=val #누적합 계산
        if idx_count>d//2: #idx누적합이 window의 중앙값을 넘었을 때
            if d%2==1: #window가 홀수 크기일 때
                return i*2 #중앙값*2
            else: #window가 짝수 크기일 때 중앙값은 중앙의 두 값(m1,m2)의 평균
                for j in range(i,-1,-1): #넘어간 값부터 cnt 내리면서 중앙의 작은 값 m1구하기
                    idx_count-=counter[j] #두번 째 중앙값 m2 빼준다
                    if idx_count<d//2: #처음으로 중앙값 idx보다 작아졌을 때 m1을 찾았다
                        return i+j


def activityNotifications(expenditure, d):
    # Write your code here
    notice=0 #원하는 answer
    counter=[0]*201 #값의 범위
    for money in expenditure[:d]: #초기 window만큼 계수 count
        counter[money]+=1 #메모리에 등장 빈도 기록
    
    for idx in range(d,len(expenditure)): #notice를 날릴 수 있는 범위부터 시작
        top=expenditure[idx] #window에 삽입할 새로운 값
        bot=expenditure[idx-d] #window에서 짤려나갈 오래된 값
        
        median=get_median(counter,d) #현재 counter에서 중앙값 구하기
        if top>=median: 
            notice+=1
        counter[top]+=1 #새로 등장한 값의 빈도 증가
        counter[bot]-=1 #오래된 값 빈도 감소
    return notice