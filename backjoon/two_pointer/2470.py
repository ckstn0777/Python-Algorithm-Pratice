# https://www.acmicpc.net/problem/2470
'''
5
-2 4 -99 -1 98
'''

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    # 정렬
    arr.sort()

    sum_min = 1e11 # 범위가 중요하네... -10억 ~ 10억 이니까 1e9로 하면 안되네
    answer = None

    # 투 포인터 탐색
    left, right = 0, len(arr) - 1
    while left < right:
        temp = arr[left] + arr[right]

        if sum_min > abs(temp):
            answer = [arr[left], arr[right]]
            sum_min = abs(temp)

        if temp < 0:
            left += 1
        else:
            right -= 1
    
    print(' '.join(map(str, answer)))