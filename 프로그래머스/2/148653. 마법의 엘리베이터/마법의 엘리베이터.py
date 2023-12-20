# 1을 포함하여 10으로 나눠 떨어지는 수가 되기 위한 min step
# 각 자리수마다 0을 만들어 주면 됨
# 6이상이면 10 - n 이후 윗자리 재귀로 채워주기
# 5이하라면 n
def solution(storey):
    answer = 0
    
    reversed_storey_arr = list(map(lambda x: int(x), reversed(str(storey))))
    for idx in range(len(reversed_storey_arr)):
        num = reversed_storey_arr[idx]
        if idx + 1 <= len(reversed_storey_arr) -1:
            next_num = reversed_storey_arr[idx + 1]
        else:
            next_num = -1
            
        # print(f"num {num} running ...")
        # 1개 올림. 재귀함수 작동
        if num >= 6 or (num == 5 and next_num >=5):
            answer += 10 - num
            
            reversed_storey_arr[idx] = 0
            reversed_storey_arr = upcount_number(reversed_storey_arr, idx + 1)
            # print(f"now {''.join(reversed(list(map(lambda x: str(x), reversed_storey_arr))))}")
        else:
            answer += num
    
    if len(reversed_storey_arr) != len(str(storey)):
        answer += 1
            
    return answer

def upcount_number(arr, num_idx):
    if num_idx >= len(arr):
        arr.append(1)
        return arr
    
    else:
        if arr[num_idx] == 9:
            arr[num_idx] = 0
            
            return upcount_number(arr, num_idx + 1)
        else:
            arr[num_idx] += 1
            return arr
        