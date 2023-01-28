# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# 23.1.28 기록
# 최단 경로를 구하는 문제이지만 추가로 k 경유지를 초과해서는 안된다는 조건이 있다. 

import heapq
import collections

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
        k = 0
        visit = {}
        Q = [(0, src, 0)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if node not in visit or visit[node] > k:
                visit[node] = k
                for v, w in graph[node]:
                    if k <= K:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))
        return -1