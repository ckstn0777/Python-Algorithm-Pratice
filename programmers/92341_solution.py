
# 92341 문제 다른 사람 풀이
# 진짜 클래스랑 if, else, for 같은 연산, defaultdict를 잘 활용했네.. 파이썬 좀 치네

from collections import defaultdict
import math

class Parking:
  def __init__(self, fees):
    self.fees = fees
    self.in_flag = False
    self.in_time = 0 # IN 시간
    self.total = 0 # 전체 시간
  
  def update(self, t, inout):
    self.in_flag = True if inout == 'IN' else False
    if self.in_flag:
      self.in_time = str2int(t)
    else:
      self.total += (str2int(t) - self.in_time)
  
  def calc_fee(self):
    if self.in_flag: # 마지막에 IN 한 경우는 추가로 update
      self.update('23:59', 'out')
    add_t = self.total - self.fees[0] # 기본시간 차감
    return self.fees[1] + math.ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1] # 기본시간보다 큰 경우 추가시간 계산


def str2int(string):
    return int(string[:2])*60 + int(string[3:])


def solution(fees, records):
  recordsDict = defaultdict(lambda:Parking(fees))
  for rcd in records:
    t, car, inout = rcd.split()
    recordsDict[car].update(t, inout)
    # print(car, recordsDict[car].total)

  return [v.calc_fee() for k, v in sorted(recordsDict.items())]




print(solution(
  [180, 5000, 10, 600],
  ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", 
  "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
))