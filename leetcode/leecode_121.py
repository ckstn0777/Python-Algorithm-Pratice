# 문제 : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 참고 : https://www.youtube.com/watch?v=1pkOgXD63yU  (여기서는 투포인터 방식을 이용했네)

# 내가 푼 코드 - 저점과 고점을 두고 계산
def maxProfit(prices):
  min_p = 1e9 # 저점
  max_p = -1 # 고점

  answer = 0 # 저점에 샀다가 고점에 판 경우 이익
  for price in prices:
    if min_p > price:
      min_p = price # 저점 갱신
      max_p = -1 # 저점이 갱신되면 고점은 초기화
    
    if max_p < price:
      max_p = price # 고점 갱신
      answer = max(answer, (max_p - min_p)) # 저점 이후에 고점이 되야 이익이 되므로
  
  return answer


# 추천코드 - 저점과 최대이익을 두고 계산한다. 
# 고점이 아닌 최대 이익을 두고 판단하는 게 중요하군. 그리고 순서가 중요하네.
def maxProfit2(prices):
  minPrice = 1e9
  maxProfit = 0

  for price  in prices:
    maxProfit = max(maxProfit, price - minPrice)
    minPrice = min(minPrice, price)
  
  return maxProfit




print(maxProfit2([3,2,6,5,0,3]))