def solution(s):
    answer = ""
    l=len(s)
    if l%2==0:
        answer=s[(int)(l/2)-1:(int)(l/2+1)]
    else :
        answer=s[(int)(l/2)]
    
    return answer
solution("abcd")