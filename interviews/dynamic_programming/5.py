# 문제 : 정수로 이루어진 2차원 배열(격자)과, 1차원 배열(패턴)이 주어졌다고 가정하자. 
# 격자의 어떤 지점에서 시작해서 인접한 엔트리로 탐색한다고 했을 때, 패턴의 순서대로 탐색할 수 있다면 해당 패턴을 격자에서 발견했다고 한다. 
# 인접한 엔티리란 임의의 지점과 맞닿은 위, 아래, 왼쪽, 오른쪽의 엔트리를 말한다. 중복 방문도 가능하다. 
# 1차원 배열을 2차원 배열에서 발견할 수 있는지 확인하는 프로그램을 작성하라. (!!)

'''
3 3
1 2 3
3 4 5
5 6 7
1 2 3 6
'''

# n, m이 2차원 배열 A의 행과 열의 개수일 때, 시간복잡도는 O(nm|S|)와 같다. 
# 재귀 호출을 제외하면 함수 내에서 일정한 양의 작업을 수행하며, 호출 수는 2차원 배열의 항목 수를 초과하지 않는다. 
def isPatternSuffixContainedStartingAtXY(grid, x, y, pattern, offset, previousAttempts):
    if len(pattern) == offset: # 더 이상 남아 있는 게 없다
        return True

    # (x, y)가 격자에 벗어났는지 확인
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    
    # 이미 탐색을 했는데 아니었던 경우 패스
    if (x, y, offset) in previousAttempts:
        return False

    # (x, y)가 패턴에 존재하는지 확인
    if grid[x][y] != pattern[offset]:
        return False

    # 인접한 엔트리 탐색
    if isPatternSuffixContainedStartingAtXY(grid, x - 1, y, pattern, offset + 1, previousAttempts) or \
        isPatternSuffixContainedStartingAtXY(grid, x + 1, y, pattern, offset + 1, previousAttempts) or \
        isPatternSuffixContainedStartingAtXY(grid, x, y - 1, pattern, offset + 1, previousAttempts) or \
        isPatternSuffixContainedStartingAtXY(grid, x, y + 1, pattern, offset + 1, previousAttempts):
        return True
    
    previousAttempts.append((x, y, offset))
    return False


def isPatternContainedInGrid(grid, pattern):
    previousAttempts = [] # 방문기록
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if isPatternSuffixContainedStartingAtXY(grid, i, j, pattern, 0, previousAttempts):
                return True
    
    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    pattern = list(map(int, input().split()))

    print(isPatternContainedInGrid(grid, pattern))