# https://www.acmicpc.net/problem/1561
'''
7 2
3 2
'''

import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n, m = map(int, input().split())
  t_list = list(map(int, input().split()))

  # 기본적으로 놀이기구의 수보다 아이들의 수가 적으면 아이들의 수를 출력하고 끝냄
  if n < m:
    print(n)
  else:
    # 이진 탐색. 최대 20억 * 30 = 600억...
    left, right = 0, 60000000000
    t = None

    while left <= right:
      mid = (left + right) // 2

      cnt = m # 처음에 다 태우고 시작하니까
      for i in range(m):
        cnt += mid // t_list[i]
      
      if cnt >= n: # n명을 다 태울 수 있음
        t = mid
        right = mid - 1
      else:
        left = mid + 1
      
    # t - 1에 탑승한 아이들의 숫자를 계산
    cnt = m
    for i in range(m):
      cnt += (t - 1) // t_list[i]
    
    # t에 탑승한 아이를 계산
    for i in range(m):
      if t % t_list[i] == 0: # t 시간에 탑승한 아이
        cnt += 1
      if cnt == n:
        print(i + 1)
        break