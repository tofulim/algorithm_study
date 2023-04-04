from itertools import permutations

# 0: dia / 1: iron / 2: stone
pick2cost = {
    0: [1, 1, 1],
    1: [5, 1, 1],
    2: [25, 5, 1],
}
# mineral을 pick_idx로 캤을 때 소요되는 cost
mineral2pick_idx = {
    "diamond": 0,
    "iron": 1,
    "stone": 2,
}


def calc_cost(picks: list, minerals: list):
    cost = 0
    mineral_idx = 0
    max_mineral_idx = len(minerals)

    for pick in picks:
        # 1 pick can dig 5 minerals
        for pick_life in range(1, 6):
            # digged all minerals
            if mineral_idx == max_mineral_idx:
                return cost

            mineral = minerals[mineral_idx]
            pick_cost_list = pick2cost[pick]
            current_cost = pick_cost_list[mineral2pick_idx[mineral]]
            cost += current_cost

            mineral_idx += 1

    return cost


def solution(picks, minerals):
    permuts = list(sum([[pick] * pick_num for pick, pick_num in enumerate(picks)], []))

    picks_list = permutations(permuts, len(permuts))
    # del duplicate candidates
    picks_list = list(set(picks_list))

    min_cost = 1000000
    for picks in picks_list:
        cost = calc_cost(picks, minerals)
        min_cost = min(min_cost, cost)

    return min_cost