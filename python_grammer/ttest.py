#희망 평균 거리 설정, 하루에 평균 3km씩 뛰기를 희망
target_daily_distance=3

#현재 당일 러닝 거리 설정
daily_distance=0
while True :
    
    #총 러닝거리
    daily_distance+=1
    total_distance=0
    week=0

    while week<7:
        week+=1
        total_distance+=daily_distance
    
    #평균러닝 거리 출력
    avg_distance=total_distance/7
    print("평균 러닝 거리 출력", avg_distance)

    if target_daily_distance <= avg_distance:
        break

