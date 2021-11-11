import math
#홀수면 꼭 2로 나눠지므로 result==2
#짝수면 1뺀 홀수를 sqrt(n)부터 시작해서 나눠지는지 보기 
def solution(n):
    if n%2==1: return 2 #n이 홀수일 경우 바로 리턴
    for i in range(2,int(math.sqrt(n-1))+1): #짝수일 경우 홀수를 분해하되 범위를 좁혀 계산한다
        if (n-1)%i==0: #약수를 찾았다면 리턴
            return i
    return n-1 #소수일 경우 자기자신 리턴