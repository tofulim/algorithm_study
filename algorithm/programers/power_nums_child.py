def get_cnt(num):
    cnt=1
    max_div=num//2
    for i in range(1,max_div+1):
        if num%i==0:
            cnt+=1
    return cnt

def solution(left, right):
    return sum([num if get_cnt(num)%2==0 else -num for num in range(left,right+1)])


# def solution(left, right):
#     return sum([-num if int(num**0.5)==num**0.5 else num for num in range(left,right+1)])