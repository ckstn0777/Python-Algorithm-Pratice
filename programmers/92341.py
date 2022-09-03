# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 단순 구현문제. 하지만 문제 자체가 길고 조건이 까다로울 수 있으므로 침착하게 꼼꼼히 빠르게.. 푸는게 중요할듯..

import math


### hh:mm -> 정수로 바꿔주는 함수
def timeToNum(hhmm):
  hh, mm = hhmm.split(':')
  hh, mm = int(hh), int(mm)

  time = hh * 60 + mm
  return time


## 주차시간 계산함수
def calculation_fee(fees, duration):
  time, cost, add_time, add_cost = fees

  print(duration)
  if duration <= time: #기본요금
    return cost
  else: # 추가요금 계산 (올림처리)
    return cost + math.ceil((duration - time) / add_time) * add_cost


def solution(fees, records):
    cars_record = {}
    for record in records:
      time, car_num, inout = record.split()
      time = timeToNum(time)

      if car_num not in cars_record.keys():
        cars_record[car_num] = [(time, inout)]
      else:
        cars_record[car_num].append((time, inout))
    
    
    cards_cost = {}
    for car_num, car_records in cars_record.items():
      # print(car_num, car_records)
      sum_time = 0
      start_time = -1

      for car_record in car_records:
        time, inout = car_record
        
        if inout == 'IN':
          start_time = time
        else:
          duration = time - start_time
          sum_time += duration
          start_time = -1 # 초기화


      if start_time != -1: # 마지막에 출차하지 않은경우 (초기화는 0이 아닌 -1로 해야하는군... 00:00도 있으니까)
        sum_time += (timeToNum("23:59") - start_time)
      
      sum_cost = calculation_fee(fees, sum_time)
      cards_cost[car_num] = sum_cost

    # dict key 정렬
    cards_cost_sort = sorted(cards_cost.items(), key = lambda x: x[0])
    result = list(map(lambda x:x[1], cards_cost_sort))

    return result




print(solution(
  [180, 5000, 10, 600],
  ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", 
  "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
))