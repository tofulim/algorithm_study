def solution(numbers):
    return sum(list(set([i for i in range(10)])-set(numbers)))