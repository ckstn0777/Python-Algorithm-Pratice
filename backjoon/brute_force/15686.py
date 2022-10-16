# 문제 : https://www.acmicpc.net/problem/15686


# 이 문제는 무식하게 완전탐색으로 풀 수 있다는 점에 주목해야한다.
# 일단 치킨집 최대는 13개이다. 또한, 2차원 배열은 최대 50(N)이다. 그냥 집은 2N이므로 100이 최대이다.
# 폐업시키지 않을 치킨집을 최대 M 골랐을때 조합으로 따지면 13_C_6 = 13_C_7 = 13!/6!7! = 1716 이다. (참고.조합 공식 : n!/r!(n-r)!)
# 그리고 조합마다 집과의 거리를 모두 계산하므로 100 * 1716 = 171600 이 된다. 따라서 충분히 완전탐색으로 풀 수 있다. 
from itertools import combinations


def my_solution():
  n, m = map(int, input().split())
  
  chicken_pos = []
  home_pos = []

  for i in range(n):
    row = input().split()
    for j in range(n):
      if row[j] == '2': # 치킨집
        chicken_pos.append((i, j))
      elif row[j] == '1': # 그냥 집
        home_pos.append((i, j))
  
  # print(chicken_pos)
  # print(home_pos)
  
  # 치킨집 조합을 구한다
  chichken_comb = combinations(chicken_pos, m)
  
  # 조합마다 집과의 거리 계산
  result = 1e9
  for comb in chichken_comb:
    # 모든 집에 대해 가장 가까운 치킨 집 찾아서 더해주기
    comb_sum = 0
    for hx, hy in home_pos:
      temp = 1e9
      for cx, cy in comb:
        temp = min(temp, abs(hx - cx) + abs(hy - cy))
      comb_sum += temp
    
    result = min(result, comb_sum)
  
  return result
      

if __name__ == "__main__":
  print(my_solution())