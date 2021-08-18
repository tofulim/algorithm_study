def solution(price, money, count):
    cnt=sum([i for i in range(1,count+1)])
    answer=cnt*price-money
    return answer if answer>0 else 0