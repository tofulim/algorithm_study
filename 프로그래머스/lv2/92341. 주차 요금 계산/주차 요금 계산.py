import math


def solution(fees, records):
    answer = []
    car_num2record = {}
    
    # 차번호별 출입 레코드 정리
    for record in records:
        time, car_num, action = record.split()
        
        car_records = car_num2record.get(car_num, [])
        car_records.append((time, action))
        car_num2record[car_num] = car_records
    
    # 차번호로 정렬 후 차번호별 요금 계산
    for car_num, car_records in sorted(car_num2record.items(), key=lambda x: x[0]):
        fee = 0
        total_minutes = 0
        for idx, car_record in enumerate(car_records):
            time, action = car_record
            # 마지막 기록이 IN일 경우
            if idx == len(car_records) - 1 and action == "IN":
                total_minutes += get_used_total_minutes(in_time=time)
            # 출차기록일 경우 입차 기록을 가져와 계산한다.
            if action == "OUT":
                in_time = car_records[idx - 1][0]
                total_minutes += get_used_total_minutes(in_time=in_time, out_time=time)
        
        fee += calc_fee(fees, total_minutes)
        answer.append(fee)
    
    return answer

def get_used_total_minutes(in_time: str, out_time: str = "23:59"):
    def str_time2int_minutes(time_str):
        hours, minutes = list(map(int, time_str.split(":")))
        
        total_minutes = 60 * hours + minutes
        
        return total_minutes
    
    out_minutes = str_time2int_minutes(out_time)
    in_minutes = str_time2int_minutes(in_time)
    
    return str_time2int_minutes(out_time) - str_time2int_minutes(in_time)
    
def calc_fee(fees, total_minutes):
    base_time, base_fee, extra_time, extra_fee = fees
    
    fee = 0
    if total_minutes >= base_time:
        # 기본요금 부과
        fee = base_fee
    else:
        return base_fee
    
    total_minutes -= base_time
    # 초과요금 부과
    fee += int(math.ceil(total_minutes / extra_time)) * extra_fee
        
    return fee
     
        
        
