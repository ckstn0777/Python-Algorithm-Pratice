# https://www.acmicpc.net/problem/11085
'''
7 11
3 5
0 1 15
0 2 23
1 2 16
1 3 27
2 4 3
2 6 21
3 4 14
3 5 10
4 5 50
4 6 9
5 6 42
'''

import heapq


def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])

  return parent[x]


def union(parent, a, b):
  a_p = find_parent(parent, a)
  b_p = find_parent(parent, b)

  if a_p < b_p:
    parent[b_p] = a_p
  else:
    parent[a_p] = b_p


if __name__ == "__main__":
  p, w = map(int, input().split())
  c, v = map(int, input().split())

  heap = []
  for _ in range(w):
    s, e, w = map(int, input().split())
    heapq.heappush(heap, (-w, s, e)) # 최대힙으로 하려면 앞에 (-) 붙일것

  parent = [i for i in range(p)]
  result = 0

  while heap:
    w, s, e = heapq.heappop(heap)
    w = -w
    union(parent, s, e)
    
    # 마침내 c와 v가 연결이 되었다면
    if find_parent(parent, c) == find_parent(parent, v):
      result = w # 해당 경로가 경로상 가장 너비가 좁은 길임
      break
  
  print(result)
