# https://www.acmicpc.net/problem/11404
'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 1단계. 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 2단계. 각 간선에 대한 정보를 입력받아 그 값으로 초기화
    for _ in range(m):
        i, j, cost = map(int, input().split())
        graph[i][j] = min(graph[i][j], cost) # 중복되는 노선이 있을 수 있으므로
    
    # 3단계. 점화식에 따라 플로이드 워셜 수행 (k를 거처가는 게 더 유리하다면 바꿔줌)
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    # 결과 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print(0, end=" ")
            else:
                print(graph[a][b], end=" ")
        print()
    
