def solution(elements):
    comb_set = set()
    
    len_element = len(elements)
    # 수열 시작점 element 지정
    for idx, element in enumerate(elements):
        # 연속 부분합 초기화
        sequence_sum = 0
        # 1개부터 len개까지 연속 수열합을 구하는 iteration
        for sequence_length in range(len_element):
            # 나머지연산으로 len을 초과하는 수는 원수열 초기 idx로 반환
            curr_idx = (idx + sequence_length) % len_element
            sequence_sum += elements[curr_idx]
            comb_set.add(sequence_sum)
    
    return len(comb_set)