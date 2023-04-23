# 이중 for loop
def solution(targets):
    missile_cnt = 0
    # (s,e) 모두 오름차순 정렬하되 e를 우선으로 정렬한다
    sorted_targets = sorted(targets, key=lambda x: (x[1], x[0]))
    # 요격된 폭격 미사일 체크 리스트
    destroyed_targets = [False] * len(targets)
    for idx, target in enumerate(sorted_targets):
        # 이미 요격된 미사일이라면 점검하지 않는다
        if destroyed_targets[idx] is True:
            continue
        # 현재 미사일을 요격할때 함께 요격할 수 있는 미사일들을 요격한다
        end = target[1]
        for comp_idx in range(idx, len(targets)):
            comp_start, comp_end = sorted_targets[comp_idx]
            if comp_start < end:
                destroyed_targets[comp_idx] = True
            else:
                break
        missile_cnt += 1

    return missile_cnt

# 단일 for loop