# https://www.acmicpc.net/problem/1655

'''
7
1
5
2
10
-99
7
5
'''

import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n = int(input())
  max_heap = [] # 왼쪽 부분 (왼쪽에서 최대)
  min_heap = [] # 오른쪽 부분 (오른쪽에서 최소)

  for i in range(n):
    x = int(input())
    if i % 2 == 0:
      heapq.heappush(max_heap, -x)
    else:
      heapq.heappush(min_heap, x)
    
    # 왼쪽 영역에서 가장 큰 값과 오른쪽 영역에서 가장 작은 값 비교해서 둘이 바뀔 필요가 있다면
    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
      max_value = -heapq.heappop(max_heap)
      min_value = heapq.heappop(min_heap)

      heapq.heappush(max_heap, -min_value)
      heapq.heappush(min_heap, max_value)
    
    print(-max_heap[0]) # 왼쪽에서 최대를 출력해주면 됨