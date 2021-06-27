from itertools import combinations
from collections import defaultdict,Counter

def get_course_menu(orders,course_n):
    combs=[]
    answer=[]
    for order in orders:
        combs.extend(combinations(sorted(order),course_n))
    
    course_candidate=defaultdict(int)
    for comb in combs:
        comb_str=''.join(comb)
        course_candidate[comb_str]+=1

    for courses in course_candidate:
        if course_candidate[courses]>1 and course_candidate[courses] == max(list(course_candidate.values())):
            answer.append(courses)
    
    return answer
    

def solution(orders, course):
    answer = []
    for course_n in course:
        answer.extend(get_course_menu(orders,course_n))
        
    return sorted(answer)