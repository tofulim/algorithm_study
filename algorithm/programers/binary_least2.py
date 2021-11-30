import math

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number=format(number,'b')
        if number%2==0: #짝수일 때
            bin_number=list(bin_number)
            bin_number[-1]='1'
        else: #홀수일 때
            bin_number='0'+bin_number
            idx=bin_number.rfind('0')
            bin_number=list(bin_number)
            bin_number[idx]='1'
            bin_number[idx+1]='0'
        answer.append(int(''.join(bin_number),2))
            
    return answer