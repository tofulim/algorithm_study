def solution(k, m, score):
    # 내림차순 정렬 - m개로 나눠 상자 개수 구하기
    
    sorted_score = sorted(score, key=lambda x: -x)
    
    box_nums = len(sorted_score) // m
    
    answer = 0
    for idx in range(box_nums):
        box_sum = m * sorted_score[(idx + 1) * m - 1]
        answer += box_sum

    return answer