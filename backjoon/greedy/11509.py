# https://www.acmicpc.net/problem/11509
'''
5
4 5 2 1 4

5
1 2 3 4 5
'''


if __name__ == "__main__":
    n = int(input())
    ballons = list(map(int, input().split()))

    arrow_pos = [] # 현재 화살의 위치
    
    for i in range(len(ballons)):
        if ballons[i] in arrow_pos:
            arrow_pos[arrow_pos.index(ballons[i])] -= 1
        else:
            arrow_pos.append(ballons[i] - 1)
    
    print(len(arrow_pos))
    