def solution(sequence, k):
    answer = []
    cnt, right = 0, 0
    # 점점 증가하며 짧아질 left를 기점으로 순회한다
    for left in range(len(sequence)):
        # right는 기준 left로부터 오른쪽으로 조건을 넘지 않을만큼만 뻗어나간다
        while right < len(sequence) and cnt < k:
            cnt += sequence[right]
            right += 1
        # 조건에 부합했을 때 정답 계산
        if cnt == k:
            if len(answer) == 0:
                answer = [left, right - 1]
            else:
                answer = answer if answer[1] - answer[0] <= (right - 1) - left else [left, right - 1]
        # 조건 부합 여부와 상관없이 좌측을 한칸 땡겨준다
        cnt -= sequence[left]

    return answer
