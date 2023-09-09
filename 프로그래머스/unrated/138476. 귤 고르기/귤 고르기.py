from collections import Counter


def solution(k, tangerine):
    num_tangerine = 0
    tangerine_counter = Counter(tangerine)
    
    # 개수가 많은 귤로 내림차순 정렬
    for idx, tangerine in enumerate(sorted(tangerine_counter.values(), reverse=True)):
        num_tangerine += tangerine
        # 바구니를 초과하면 해당 귤 크기에서 멈춘다.
        if num_tangerine >= k:
            return idx + 1
        
    return len(tangerine)