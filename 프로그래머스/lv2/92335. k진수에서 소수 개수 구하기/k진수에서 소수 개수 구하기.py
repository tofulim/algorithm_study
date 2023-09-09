import math


def solution(n, k):
    # n진수 변환
    n_num_str = get_n_number(n, k)
    
    # n진수 내 소수 후보자 반환
    prime_number_candidates = n_num_str.split("0")

    # 소수인 후보자들 중 소수 필터링해 개수 반환
    answer = len(list(filter(lambda candidate: validate_prime(candidate), prime_number_candidates)))
    
    return answer

# n진수 변환
def get_n_number(n, k):
    n_num = []
    
    while n != 0:
        n_num.append(n % k)
        n = n // k
    
    n_num_str = ''.join(list(map(str, reversed(n_num))))

    return n_num_str
        
def validate_prime(candidate_num):
    if candidate_num.isdigit() is False:
        return False
    
    candidate_num = int(candidate_num)
    if candidate_num == 1:
        return False
    
    for divider in range(2, int(candidate_num**0.5) + 1):
        if candidate_num % divider == 0:
            return False
    
    return True

# 에라토스테네스의 체로 소수 체크리스트 구해놓기
# def get_prime_check_list(limit_num: int = 1_000_000):
#     # prime이면 1 아니면 0을 저장해놓은 0부터 백만까지의 소수 체크 리스트를 만든다.
#     prime_check_list = [False, False] + [True] * (limit_num - 1) 
#     prime_nums = []
    
#     for num in range(2, limit_num + 1):
#         if prime_check_list[num]:
#             prime_nums.append(num)
#         for product_num in range(2 * num, int(limit_num**0.5) + 1, num):
#             prime_check_list[product_num] = False

#     return prime_nums
                
                
    