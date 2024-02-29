def solution(t, p):
    answer = 0
    p_val, p_len = int(p), len(p)
    for idx in range(0, len(t) - p_len + 1):
        num = int(t[idx:idx + p_len])
        if p_val >= num:
            answer += 1
            
    return answer