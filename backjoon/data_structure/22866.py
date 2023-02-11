# https://www.acmicpc.net/problem/22866

'''
8
3 7 1 6 3 5 1 7
'''

if __name__ == "__main__":
    n = int(input())
    l_list = list(map(int, input().split()))

    cnt = [0] * (n + 1) # i번째 건물이 볼 수 있는 다른 건물의 수
    near = [[int(1e9), int(1e9)] for _ in range(n + 1)] # [가장 가까운 건물번호, 가장 가까운 건물거리]


    # 처음부터 순차적 진행 : 해당 건물에서 좌측기준 볼 수 있는 건물이 스택에 들어가게 됨
    stack = []
    for idx, v in enumerate(l_list, 1):
        # stack pop 조건 - 데이터가 있고, 스택 최상위 건물의 높이가 현재 건물 높이와 같거나 작으면 더 이상 안보이기 때문에 제거
        while len(stack) > 0 and stack[-1][1] <= v:
            stack.pop()
        cnt[idx] += len(stack) # 해당건물기준 좌측으로 볼 수 있는 건물 수 

        if len(stack) > 0:
            dist = abs(stack[-1][0] - idx) # 해당 건물기준 가장 가까운 좌측건물과의 거리
            if dist < near[idx][1]:
                near[idx][0] = stack[-1][0]
                near[idx][1] = dist
            elif dist == near[idx][1] and stack[-1][0] < near[idx][0]: # 거리는 같은데 건물번호가 더 작은 경우
                near[idx][0] = stack[-1][0]

        stack.append([idx, v]) # 건물번호와 높이
    
    # 반대로 진행 : 해당 건물에서 우측기준 볼 수 있는 건물이 스택에 들어가게 됨
    stack = []
    for idx, v in reversed(list(enumerate(l_list, 1))):
        # stack pop 조건 - 데이터가 있고, 스택 최상위 건물의 높이가 현재 건물 높이와 같거나 작으면 더 이상 안보이기 때문에 제거
        while len(stack) > 0 and stack[-1][1] <= v:
            stack.pop()
        cnt[idx] += len(stack) # 해당건물기준 우측으로 볼 수 있는 건물 수 

        if len(stack) > 0:
            dist = abs(stack[-1][0] - idx) # 해당 건물기준 가장 가까운 우측건물과의 거리
            if dist < near[idx][1]:
                near[idx][0] = stack[-1][0]
                near[idx][1] = dist
            elif dist == near[idx][1] and stack[-1][0] < near[idx][0]: # 거리는 같은데 건물번호가 더 작은 경우
                near[idx][0] = stack[-1][0]

        stack.append([idx, v]) # 건물번호와 높이
    
    # 최종 결과
    for i in range(1, n + 1):
        if cnt[i] > 0:
            print(f'{cnt[i]} {near[i][0]}') # 해당 건물에서 볼 수 있는 건물 수, 가장 가까운 건물 번호 중 건물 번호가 작은 건물의 번호
        else:
            print(0)