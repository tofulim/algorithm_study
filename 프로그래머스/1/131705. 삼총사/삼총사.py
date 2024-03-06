from collections import Counter
from itertools import combinations


def solution(number):
    # 숫자로 만들 수 있는 삼총사의 조합을 계산한다.
    combs = combinations(number, 3)
            
    return len(list(filter(lambda comb: sum(comb) == 0, combs)))