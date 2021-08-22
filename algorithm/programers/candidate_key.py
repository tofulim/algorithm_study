from itertools import combinations
def solution(relation):
    answer = 0
    rows=len(relation)
    columns=len(relation[0])
    final_comb=[]
    comb=combinations(range(1,columns+1),1)
    
    for i in range(1,columns+1):
        combs=combinations(range(columns),i)
        for comb in combs:
            comb=set(comb)
            new_arr=[]
            for index in range(rows):
                new_arr.append(' '.join([relation[index][j] for j in comb]))
            
            if len(set(new_arr))==rows:
                flag=True
                if i!=1 :
                    for ori_comb in final_comb:
                        if ori_comb.issubset(comb):
                            flag=False
                            break
                if flag:
                    final_comb.append(comb)
    
    return len(final_comb)