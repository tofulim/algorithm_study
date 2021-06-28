from collections import defaultdict  
from itertools import combinations
import bisect

# info를 받아 dict를 채우는 과정
def fill_dict(info_dict, person):
    language, position, exp, food, score=person.split()
    person=[language, position, exp, food]
    # dontcare '-'이 없는 순수한 info 한개 넣어준다 
    info_dict[''.join(person)].append(int(score))
    # score를 제외한 4개의 선택지에서 1,2,3,4개씩 마스킹해주기 위한 반복문
    for i in range(1,5):
        combs=combinations(range(4),i) #조합 뽑기
        
        for comb in combs: #조합 하나씩 뽑아 마스킹해 dict에 넣어준다
            comb_str=""
            for idx,j in enumerate(person):
                comb_str+='-' if idx in comb else j #해당하는 속성 '-'로 마스킹
            info_dict[comb_str].append(int(score))

def solution(info, query):
    answer = []
    # info에 각종 마스킹을 해 16가지 경우를 모두 만들어 줄 dict 선언
    info_dict=defaultdict(list)
    for person in info:
        fill_dict(info_dict,person)
    #score의 이진탐색을 위해 오름차순 정렬
    for key in info_dict.keys() : info_dict[key].sort()
    
    for q in query:
        language,_,position,_,exp,_,food,score=q.split()
        score=int(score)
        scores=info_dict[language+position+exp+food]
        
        size = len(scores)
        # target score보다 큰 개수를 원하므로 전체에서 target보다 작은 개수를 빼준다
        answer.append(size - bisect.bisect_left(scores, score, lo=0, hi=size))

    
    return answer