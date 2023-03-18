# https://www.acmicpc.net/problem/14728

'''
3 310
50 40
100 70
200 150
'''

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, T = map(int, input().split())
    times, scores = [0], [0]

    for _ in range(N):
        t, s = map(int, input().split())
        times.append(t)
        scores.append(s)
    
    # i개의 단원을 j시간 동안 공부했을 때 얻을 수 있는 최대 점수
    dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, T + 1):
            if j >= times[i]: 
                # i 단원을 안 듣는 경우, i 단원을 들어서 점수를 올리는 경우 -> 둘 중 뭐가 좋을지
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - times[i]] + scores[i])
            else:
                dp[i][j] = dp[i - 1][j]

        # print(dp)
    
    print(dp[N][T])