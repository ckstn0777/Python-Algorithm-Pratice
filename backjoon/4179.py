# 문제 : https://www.acmicpc.net/problem/4179
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


#########################################################
### 내가 푼 코드 : 문제에서 주어진 테스트는 통과했는데 메모리 초과... (내가 봤을때 배열을 계속 새로 만들어서 그런듯?). 
# 이제보니 나는 너무 time을 생각했다..
def my_solution():
  r, c = map(int, input().split())
  
  fire = [] # 불이 난 좌표
  my_pos = [] # 내가 이동이 가능한 좌표

  miro = []
  for i in range(r):
    arr = list(input())
    miro.append(arr)
    
    for j in range(c):
      if arr[j] == 'J':
        my_pos.append((i, j))
      elif arr[j] == 'F':
        fire.append((i, j))
  
  # print(my_pos)
  # print(fire)

  time = 0
  # 불 확산
  while True:
    if not fire or not my_pos: # 더이상 확산될 공간이 없거나 내가 이동가능한 곳이 없는경우
      return "IMPOSSIBLE"
    
    time += 1

    newFire = []
    for f in fire:
      for i in range(4):
        mx = f[0] + dx[i]
        my = f[1] + dy[i]
        if 0 <= mx < r and 0 <= my < c and (miro[mx][my] == 'J' or miro[mx][my] == '.'):
          miro[mx][my] = 'F'
          newFire.append((mx, my))
    fire = newFire

    newMyPos = []
    for m in my_pos:
      for i in range(4):
        mx = m[0] + dx[i]
        my = m[1] + dy[i]
        if 0 <= mx < r and 0 <= my < c and miro[mx][my] == '.':
          newMyPos.append((mx, my))
        elif mx < 0 or mx >= r or my < 0 or my >= c:
          return time
    my_pos = newMyPos



#########################################################
### 정답 코드 : 그니까 time을 순환 체크할 필요업이 지훈이동 -> 불 이동 -> 지훈이동 -> 불 이동... 이런식으로 생각하면 되겠네
def answer_solution():
  n, m = map(int, input().split())
  graph = []

  for i in range(n):
    graph.append(list(input()))
    if 'J' in graph[i]:
      q = deque([(0, i, graph[i].index('J'))]) # (타임, 행, 열)
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 'F':
        q.append((-1, i, j)) # 불은 그냥 -1 로 한건가? 
  
  while q:
    time, x, y = q.popleft()

    # 지훈이 탈출
    if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
      ans = time + 1
      return ans
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
        # 지훈이 이동
        if time > -1 and graph[nx][ny] == '.':
          graph[nx][ny] = '_' # 중복방지
          q.append((time + 1, nx, ny))

        # 불 퍼뜨리기
        elif time == -1 and graph[nx][ny] != 'F':
          graph[nx][ny] = 'F'
          q.append((-1, nx, ny))

  return 'IMPOSSIBLE'


if __name__ == "__main__":
  print(answer_solution())