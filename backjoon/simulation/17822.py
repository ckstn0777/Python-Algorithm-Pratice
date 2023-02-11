from collections import deque

# https://www.acmicpc.net/problem/17822
'''
4 6 3
1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
2 1 4
3 0 1
2 1 2
'''

# 내 풀이는 쓰레기라 나중에 개선해서 풀어보길 바란다.. 
if __name__ == "__main__":
    n, m, t = map(int, input().split())

    # 이걸 배열로 관리하는게 좋을까? 그렇다면 회전을 구현할 때 음... 좋지 않을텐데. 근데 여기서 딱히 좋은 방법은 안떠오름.
    # 음... deque로 관리하면 어떨까? 
    # [[1, 1, 2, 3], [5, 2, 4, 2], ....]

    op = []
    for _ in range(n):
        t_list = list(map(int, input().split()))
        op.append(deque(t_list))

    for _ in range(t):
        # x: x 배수의 원판, d: 방향(0=시계, 1=반시계), k: 얼마나 
        x, d, k = map(int, input().split())

        # deque에 rotate가 있는건 처음알았네. 개꿀이잖아?
        if d == 0:
            for i in range(x - 1, n, x):
                op[i].rotate(k)
        else:
            for i in range(x - 1, n, x):
                op[i].rotate(-k)
        
        # 인접한 녀석들이 있는지 확인해서 제거
        # 인접 공식 (i, j) => (i, j - 1), (i, j + 1) // (i - 1, j), (i + 1, j)
        neo_list = []

        for i in range(n):
            for j in range(m):
                if op[i][j] == 0:
                    continue

                if j - 1 >= -n and op[i][j] == op[i][j - 1]:
                    neo_list.append((i, j))
                    neo_list.append((i, j - 1))
                if j + 1 < m and op[i][j] == op[i][j + 1]:
                    neo_list.append((i, j))
                    neo_list.append((i, j + 1))
                if i - 1 > 0 and op[i][j] == op[i - 1][j]:
                    neo_list.append((i, j))
                    neo_list.append((i - 1, j))
                if i + 1 < n and op[i][j] == op[i + 1][j]:
                    neo_list.append((i, j))
                    neo_list.append((i + 1, j))
        
        if len(neo_list) > 0:
            for n_list in neo_list:
                op[n_list[0]][n_list[1]] = 0
        else:
            # 만약 인접이 없다면 평균을 구해서 평균보다 작으면 -1, 크면 +1해줘야 함
            op_sum = 0
            op_cnt = 0
            for i in range(n):
                for j in range(m):
                    if op[i][j] > 0:
                        op_sum += op[i][j]
                        op_cnt += 1
            
            if op_cnt == 0:
                continue
            
            op_avg = op_sum / op_cnt
            for i in range(n):
                for j in range(m):
                    if op[i][j] != 0:
                        if op[i][j] > op_avg:
                            op[i][j] -= 1
                        elif op[i][j] < op_avg:
                            op[i][j] += 1
            
    
    # 최종 결과 다 더하기
    result = 0
    for i in range(n):
        result += sum(op[i])
    print(result)
    