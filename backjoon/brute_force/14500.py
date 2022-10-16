# https://www.acmicpc.net/problem/14500
'''
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
'''

ds = [
    [[0, 1], [0, 2], [0, 3]], # 1
    [[1, 0], [2, 0], [3, 0]], # 1
    [[0, 1], [1, 0], [1, 1]], # 2
    [[1, 0], [2, 0], [2, 1]], # 3
    [[1, 0], [2, 0], [2, -1]], # 3
    [[0, 1], [0, 2], [1, 0]], # 3
    [[0, 1], [0, 2], [1, 2]], # 3
    [[0, 1], [1, 1], [2, 1]], # 3
    [[0, 1], [1, 0], [2, 0]], # 3
    [[0, 1], [0, 2], [-1, 2]], # 3
    [[1, 0], [1, 1], [1, 2]], # 3
    [[1, 0], [1, 1], [2, 1]], # 4
    [[1, 0], [1, -1], [2, -1]], # 4
    [[0, 1], [-1, 1], [-1, 2]], # 4
    [[0, 1], [1, 1], [1, 2]], # 4
    [[0, 1], [0, 2], [1, 1]], # 5
    [[1, 0], [1, 1], [2, 0]], # 5
    [[1, 0], [1, -1], [2, 0]], # 5
    [[0, 1], [0, 2], [-1, 1]], # 5
]

def search(sarr, x, y, n, m):
    max_sum = 0
    # 모든 도형 경우에 대해 검사
    for d in ds:
        temp = sarr[x][y] # 현재 (x, y)
        for k in range(3):
            ax = x + d[k][0]
            ay = y + d[k][1]
            if 0 <= ax < n and 0 <= ay < m:
                temp += sarr[ax][ay]
        max_sum = max(max_sum, temp)

    return max_sum


def my_solution():
    n, m = map(int, input().split())
    sarr = []
    for _ in range(n):
        sarr.append(list(map(int, input().split())))
    
    # (0, 0) 부터 해서 완전탐색
    answer = 0
    for i in range(n):
        for j in range(m):
            answer = max(answer, search(sarr, i, j, n, m))

    return answer

if __name__ == "__main__":
    print(my_solution())