def solution(lottos, win_nums):
    my_set=set(lottos)
    win_set=set(win_nums)

    my_set.discard(0)
    zero_len=6-len(my_set)

    base_score=6-len(win_set-my_set)
    best=base_score+zero_len
    best=7-best if best>=2 else 6
    worst=7-base_score if base_score>=2 else 6

    return [best,worst]