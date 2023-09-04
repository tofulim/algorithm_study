# def solution(numbers):
#     answer = []
    
#     prev_number, prev_big = 0, -1
#     # 역순 진행
#     for number in reversed(numbers):
#         # 직전 수가 뒷 큰 수
#         if prev_number > number:
#             prev_big = prev_number
#             _answer = prev_number
#         # 직전보다 오래된 뒷 큰 수
#         elif prev_big > number:
#             _answer = prev_big
#         # 뒷 큰 수가 없음
#         else:
#             prev_big = number
#             _answer = -1 
#         # 직전 수 갱신
#         prev_number = number
            
#         answer.append(_answer)
        
#     return answer[::-1]

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number

        stack.append(idx)

    return answer
