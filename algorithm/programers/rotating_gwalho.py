def checker(str):
    stack=[]
    gwalho_dict={')':'(',']':'[','}':'{'}
    for s in str:
        if s in gwalho_dict.values(): #여는 괄호라면 push
            stack.append(s)
        elif s in gwalho_dict.keys(): #닫는 괄호라면 검사
            if len(stack)!=0 and stack[-1]==gwalho_dict[s]:
                stack.pop()
            else:
                return False
    return True if len(stack)==0 else False #여는 괄호가 스택에 남아있는지 확인

def solution(s):
    answer=0
    arr=list(s)
    for i in range(len(s)):
        if checker(arr):
            answer+=1
        arr.extend(arr.pop(0))
        
    return answer