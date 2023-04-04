from itertools import permutations

# 0: dia / 1: iron / 2: stone
pick2cost = {
    0: {"diamond": 1, "iron": 1, "stone": 1},
    1: {"diamond": 5, "iron": 1, "stone": 1},
    2: {"diamond": 25, "iron": 5, "stone": 1},
}


def get_part_costs(minerals, picks):
    num_picks = sum(picks)
    part_len = len(minerals) // 5 if len(minerals) % 5 == 0 else (len(minerals) // 5) + 1
    part_costs = {i: 0 for i in range(part_len)}

    part_cost = 0
    for idx, mineral in enumerate(minerals[:num_picks * 5]):
        part_costs[idx // 5] += pick2cost[2][mineral]

    return part_costs


def dig_mine(part2pick: dict, minerals: list):
    cost = 0
    mineral_idx = 0
    max_mineral_idx = len(minerals)
    for part_idx, pick in part2pick.items():
        # 곡괭이를 다 쓴 part일 경우 다음 곡괭이로 넘어간다
        if pick == -1:
            return cost
        # 곡괭이를 다 소모한다
        for i in range(5):
            mineral_idx = part_idx * 5 + i
            # 광물을 다 캔 경우 곡괭이를 채광를 종료한다
            if mineral_idx >= max_mineral_idx:
                break

            mineral = minerals[mineral_idx]
            current_cost = pick2cost[pick][mineral]
            cost += current_cost

    return cost


def _get_best_pick(picks: list):
    for idx, pick in enumerate(picks):
        if pick > 0:
            picks[idx] -= 1
            return idx, picks

    return -1, None


def get_part2pick(picks: list, sorted_part2cost: dict):
    part2pick = dict()

    for part_idx, _ in sorted_part2cost:
        pick, picks = _get_best_pick(picks)
        part2pick[part_idx] = pick

    return part2pick


def solution(picks, minerals):
    # 가진 곡괭이 갯수만큼만 구간 비용을 구한다
    part2cost = get_part_costs(minerals, picks)
    # 비싼 구간 내림차순 정렬
    sorted_part2cost = list(sorted(part2cost.items(), key=lambda x: -x[1]))
    # 비싼 구간 순서대로 좋은 곡괭이를 배치한다
    part2pick = get_part2pick(picks, sorted_part2cost)
    # 시뮬레이션 수행해 피로도를 계산한다
    cost = dig_mine(part2pick, minerals)

    return cost