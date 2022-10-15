# https://www.acmicpc.net/problem/9465

'''
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
'''

def my_solution():
    t = int(input())
    answer = []

    for _ in range(t):
        n = int(input())
        
        arr = []
        for _ in range(2):
            arr.append(list(map(int, input().split())))
        
        # 점수 계산
        score_arr = [[0] * (n) for _ in range(2)]
        score_arr[0][0] = arr[0][0]
        score_arr[1][0] = arr[1][0]
        # print(score_arr)

        # 점화식 점수 계산
        # [0][0], [0][1]로 기준을 잡아놓고 다음 [0][1], [1][1] 값은 점화식이 어떻게 될까 생각하면서 풀었다 
        # 두가지 방법이 있는데 이전 값을 바로 가져오는게 이득인 경우와 대각선 방향 + 현재 값이 이득인 경우. 이를 비교해서 높은걸 기록해주면 됨
        for i in range(1, n):
            score_arr[0][i] = max(score_arr[0][i - 1], arr[0][i] + score_arr[1][i - 1])
            score_arr[1][i] = max(score_arr[1][i - 1], arr[1][i] + score_arr[0][i - 1])

        answer.append(max(score_arr[0][n - 1], score_arr[1][n - 1]))
    
    return '\n'.join(map(str, answer))


if __name__ == "__main__":
    print(my_solution())