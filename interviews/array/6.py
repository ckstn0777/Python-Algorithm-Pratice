
'''
이 문제에 핵심은 최솟값을 계속 갱신하면서 현재값과 비교해서 최대 이익을 찾는거임
'''

def solution(cost):
  min_price, max_profit = 1e9, 0
  for price in cost:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)
  
  return max_profit


if __name__ == "__main__":
    cost = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

    print(solution(cost)) # 30이 정답임 (260, 290)
