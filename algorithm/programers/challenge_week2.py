def get_grade(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=50:
        return 'D'
    else :
        return 'F'
    
def solution(scores):
    length=len(scores)
    answer=[]
    for i in range(length):
        score=scores[i][i]
        new_arr=[scores[j][i] for j in range(length)]
        max_val=max(new_arr)
        min_val=min(new_arr)
        if (score==max_val and new_arr.count(score)==1) or (score==min_val and new_arr.count(score)==1):
            answer.append(get_grade((sum(new_arr)-score)/(length-1)))
        else :
            answer.append(get_grade(sum(new_arr)/length))

    return ''.join(answer)