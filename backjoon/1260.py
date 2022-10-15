# https://www.acmicpc.net/problem/1260
'''
4 5 1
1 4
1 2
1 3
2 4
3 4
'''

from collections import deque

def dfs(v, graph, visited):
    visited.append(v)

    # v와 접점인 녀석들 탐색 해서 방문하지 않았다면 재귀
    for vc in graph[v]:
        if vc not in visited:
            dfs(vc, graph, visited)
    
    return visited
        

def bfs(start, graph):
    q = deque([start])
    visited = [start]

    while q:
        v = q.popleft()
        
        # v와 접점인 녀석들 탐색해서 방문하지 않았다면 추가
        for vc in graph[v]:
            if vc not in visited:
                visited.append(vc)
                q.append(vc)
    
    return visited


def my_solution():
    n, m, v = map(int, input().split())

    # graph 구조 생성
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    # graph 마다 정렬을 해줘야 겠네 (출력 조건)
    for g in graph:
        g.sort()
    
    # print(graph)

    dfs_result = dfs(v, graph, [])
    bfs_result = bfs(v, graph)


    return ' '.join(str(s) for s in dfs_result) + '\n' + ' '.join(str(s) for s in bfs_result)


if __name__ == "__main__":
    print(my_solution())