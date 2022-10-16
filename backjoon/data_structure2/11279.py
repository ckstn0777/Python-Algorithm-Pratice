# https://www.acmicpc.net/problem/11279

'''
13
0
1
2
0
0
3
2
1
0
0
0
0
0
'''

import heapq
import sys

if __name__ == "__main__":
    n = int(input())
    
    q = []

    for _ in range(n):
        num = int(sys.stdin.readline()) # 주의) 반복문으로 여러 줄을 입력받아야 할 때 input으로 하면 시간초과 발생.
        if num == 0:
            if not q:
                print(0)
            else:
                print(-1 * heapq.heappop(q))
        else:
            heapq.heappush(q, -1 * num) # 파이썬에서 힙은 기본적으로 최소힙으로 되어있다. 따라서 최대힙으로 사용하기 위해서 음수로 저장
