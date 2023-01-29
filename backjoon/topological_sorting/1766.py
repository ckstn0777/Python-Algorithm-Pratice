# https://www.acmicpc.net/problem/1766
'''
4 3
4 1
3 1
2 3
'''

import heapq


if __name__ == "__main__":
  n, m = map(int, input().split())

  graph = [[] for _ in range(n + 1)]
  in_cnt = [0] * (n + 1) # 자기 자신 위에 선행되는 문제 개수

  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b (a가 b보다 선행되어야 함)
    in_cnt[b] += 1


  # 가능한 시작점 => in_cnt가 0인 경우
  result = []
  heap = []

  for i in range(1, n + 1):
    if in_cnt[i] == 0:
      heapq.heappush(heap, i)

  while heap:
    node = heapq.heappop(heap)

    result.append(node)
    for i in graph[node]:
      in_cnt[i] -= 1
      if in_cnt[i] == 0:
        heapq.heappush(heap, i)
  
  print(' '.join(map(str, result)))

    
  
  
  
  