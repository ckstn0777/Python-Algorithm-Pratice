# https://www.acmicpc.net/problem/2606
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

from collections import defaultdict, deque

def my_solution():
    n = int(input()) # 총 컴퓨터 수 (100이하)
    m = int(input()) # 연결된 쌍 개수

    # graph 형태 만들기 
    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # bfs 탐색
    q = deque(graph[1])
    visited = [False] * (n + 1) # 방문기록 (중복제거)
    answer = 0
    
    while q:
        com = q.popleft()
        if not visited[com]:
            answer += 1
            visited[com] = True

            # 다음 연결되어있는 녀석들 중에 아직 방문하지 않은 녀석은 추가
            for c in graph[com]:
                if not visited[c]:
                    q.append(c)
        
    return answer - 1 # 컴퓨터 1은 제외


if __name__ == "__main__":
    print(my_solution())