# https://www.acmicpc.net/problem/2661
# 백트래킹 없어도 될 줄 알았는데 1213121 한 다음에 3이 될 수 없으니까 백트래킹을 해야 되네
'''
7
'''

# 좋은 수열 여부 판단
def checking(cur, add):
    tmp = cur + add
    for i in range(1, len(tmp)):
        if tmp[len(tmp)-i:len(tmp)] == tmp[len(tmp)-2*i:len(tmp)-i]: # 살짝 까다로웠다. (파이썬 인덱싱...)
            return False
    return True


def dfs_backtracking(cur):
    # print('cur', cur)
    if len(cur) == n:
        return cur
    
    for i in range(1, 4):
        if checking(cur, str(i)):
            tmp = dfs_backtracking(cur + str(i))
            if tmp == None: # 1도 아니고, 2도 아니고, 3도 될 수 없는 경우
                continue
            else:
                return tmp

if __name__ == "__main__":
    n = int(input())
    print(dfs_backtracking("1")) # 첫 시작은 무조건 1이겠지


