def solution(sizes):
    arr=list(zip(*list(map(lambda x: (min(x),max(x)),sizes))))
    return max(arr[0])*max(arr[1])