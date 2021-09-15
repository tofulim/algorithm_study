from collections import defaultdict
from itertools import combinations

def solution(enter, leave):
    person_contact_dict=defaultdict(set)
    #사람 : 입장 순서를 담은 dict
    enter_dict={p:i for i,p in enumerate(enter)}
    #퇴실자를 순서대로 순회
    for out_idx,out_person in enumerate(leave):
        #자기 자신을 포함하여 현재 방에 몇명이 있는지 확인
        before_enter_set=set(enter[:enter_dict[out_person]+1])
        left_person_set=set(leave[:out_idx])
        #나간 사람 제외한 실제 회의실에 남아있는 사람 구하기
        inter_set=before_enter_set-left_person_set
        
        if inter_set:
            for (p1,p2) in combinations(inter_set,2):
                person_contact_dict[p1].add(p2)
                person_contact_dict[p2].add(p1)
        
    answer=[0]*len(enter)
    for p,arr in person_contact_dict.items():
        answer[p-1]=len(arr)
    return answer