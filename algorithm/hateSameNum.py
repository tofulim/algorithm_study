def solution(arr):
    answer = []
    tmp=-1
    for i in range(0,len(arr)):
        if len(answer)==0 or answer[len(answer)-1]!=arr[i]:
            answer.append(arr[i])
        tmp=arr[i]
    return answer;