# https://www.acmicpc.net/problem/1916
'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''

import heapq


def dijkstra(startn, end):
  heap = []
  heapq.heappush(heap, (0, start))
  distance[start] = 0

  while heap:
    dist, now = heapq.heappop(heap)

    # 최단경로 테이블보다 큰 경우라면 볼 필요도 없음
    if distance[now] < dist:
      continue

    # 현재 도시와 연결된 다른 도시 확인
    for i in bus[now]:
      cost = dist + i[1] # 비용계산

      # 최신 비용이 최단경로 테이블보다 더 싼 경우 업데이트
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(heap, (cost, i[0]))

  return distance[end]

if __name__ == "__main__":
  n = int(input())
  m = int(input())

  bus = [[] for _ in range(n + 1)]
  distance = [int(1e9)] * (n + 1) # start 기준 최단거리 테이블

  for _ in range(m):
    start, end, cost = map(int, input().split()) # 단방향
    bus[start].append((end, cost))
  
  # 찾고자하는 비용경로(출발지, 도착지)
  start, end = map(int, input().split())
  print(dijkstra(start, end))
