# https://www.acmicpc.net/problem/16198
'''
5
100 2 1 3 100
'''



def dfs(i, tt_list, t_sum):
  global result
  if len(tt_list) == 3:
    t_sum += tt_list[i-1] * tt_list[i+1]
    result = max(result, t_sum)
  
  t_sum += tt_list[i-1] * tt_list[i+1]
  r = tt_list.pop(i) # i번째 원소 제거
  
  for ni in range(1, len(tt_list) - 1):
    dfs(ni, tt_list, t_sum)

  tt_list.insert(i, r) # i번째 원소 다시 추가




if __name__ == "__main__":
  n = int(input())
  t_list = list(map(int, input().split()))

  result = 0

  # 완전 탐색 - DFS + 백트래킹?
  for i in range(1, n - 1):
    dfs(i, t_list, 0)

  print(result)
