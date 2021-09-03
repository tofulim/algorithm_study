from itertools import product
def solution(word):
    alphas=['','A','E','I','O','U']
    #중복순열 구현
    str_list=set(map(lambda x:''.join(x),product(alphas,repeat=5)))
    #순열의 맨처음 str은 공백5개로 이루어진 ''이므로 +1해줄 필요가 없음
    return sorted(str_list).index(word)