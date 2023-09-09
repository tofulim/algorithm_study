from collections import Counter


def solution(want, number, discount):
    result = 0
    
    # 첫날 기준 10일치 장바구니를 구한다.
    ten_day_counter = Counter(discount[:10])
    
    # 10일간 장바구니가 want, number 조건을 만족하는지 검사한다.
    def validate_counter(input_counter: Counter):
        for product, num in zip(want, number):
            if input_counter[product] != num:
                return False
        
        return True
    
    # 처음 10일간의 할인이 조건을 만족하면 +1
    if validate_counter(ten_day_counter):
        result += 1
        
    # 11일(둘째날)부터 시작
    for idx, discount_product in enumerate(discount[10:]):
        ten_day_counter[discount_product] += 1
        # 장바구니 앞쪽 날짜에 골랐던 물건들 부터 빼준다.
        drop_product = discount[idx]
        ten_day_counter[drop_product] -= 1
        
        # 장바구니 확인
        if validate_counter(ten_day_counter):
            result += 1
        
    return result