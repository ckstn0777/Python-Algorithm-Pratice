# https://www.acmicpc.net/problem/14500
'''
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
'''

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# ㅗ 모양은 dfs로 탐색이 안되므로 별도 탐색
special_case = [
    [(0, 1), (0, 2), (1, 1)],
    [(1, 0), (2, 0), (1, 1)],
    [(0, 1), (0, 2), (-1, 1)],
    [(0, 1), (1, 1), (-1, 1)]
]

def special_search(x, y):
    max_sum = 0

    for d in special_case:
        temp = board[x][y] # 현재 (x, y)
        for k in range(3):
            ax = x + d[k][0]
            ay = y + d[k][1]
            if 0 <= ax < n and 0 <= ay < m:
                temp += board[ax][ay]
        max_sum = max(max_sum, temp)

    return max_sum

# 나머지 도형에 대해서는 dfs + 백트래킹으로 탐색 가능
def dfs(x, y, cnt, sum_num):
    global answer # 전역변수 answer임을 명시해줘야 write 할때 에러가 안난다
    if cnt == 4:
        answer = max(answer, sum_num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, sum_num + board[nx][ny])
            visited[nx][ny] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    answer = 0
    visited = [[0] * m for _ in range(n)]

    # (0, 0) 부터 해서 완전탐색
    for i in range(n):
        for j in range(m):
            dfs(i, j, 0, 0)
            answer = max(answer, special_search(i, j))

    print(answer)