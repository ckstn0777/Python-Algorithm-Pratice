# 문제 : https://www.acmicpc.net/problem/17071
from collections import deque


# 틀린 코드 : 예시) 5, 11 => 4가 나와야 한다. 왜냐하면 5 -> 10 -> 11 -> 22 -> 21이 정답이기 때문
# 5 -> 10 -> 20 -> 21 이런식으로 가면 21 -> 20 -> 21이나 21 -> 22 -> 21 만큼 다시 이동해야 하므로 더 걸리게 된다.
# 즉, 내 코드는 수빈이가 이동하지 않을 수 있다고 생각했다... 근데 그게 아니었다... 무조건 움직여야 한다. 
def my_solution():
  n, k = map(int, input().split())
  dp = [-1] * 500001
  dp[n] = 0

  if n == k: # 특이 조건. 처음부터 같이 있는 경우 
    return 0

  q = deque([(0, n)]) # (이동횟수, 위치정보)
  av = 1 # k의 이동 가속도
  pos_cnt = 0 # 이동 횟수
  while q:
    pos_cnt += 1
    k += av # 동생 이동
    if k > 500000: # 형이 갈수 없는 마지노선까지 이동한 경우 -1
      return -1
    
    while q and q[0][0] == pos_cnt - 1:
      cnt, pos = q.popleft()
      next_pos = [pos - 1, pos + 1, pos * 2]  # 경우가 -1, 1, 순간이동(현재 * 2)

      for p in next_pos:
        if p <= 500000 and p >= 0 and (dp[p] == -1 or dp[p] > cnt + 1): # 이전에 한번도 방문하지 않았거나 방문했더라도 더 비효율적인경우
          dp[p] = cnt + 1
          q.append((cnt + 1, p))
      
    print('q', q)
    print('dp', dp[:100])

    if dp[k] != -1:
      if pos_cnt % 2 == dp[k] % 2:
        return pos_cnt
      else:
        return pos_cnt + 1

    av += 1
  


# 정답 코드 : 결국 홀수, 짝수 구분해서 기록하는 것이 필요했네;;; (왔다갔다 할 수 있으니까...)
def answer_solution():
  n, k = map(int, input().split())
  # visited[loc][0] : loc 위치에 짝수초에 도달, visited[loc][1] : loc 위치에 홀수초에 도달
  visited = [[-1] * 2 for _ in range(500000 + 1)]

  if n == k: # 특이 조건. 처음부터 같이 있는 경우 
    return 0
  

  q = [n]
  time = 1
  k += time

  while True:
    if k > 500000: # 동생이 500,000을 넘어서면 탐색 종료
      break
    
    nextQ = []
    for subin in q:
      for nextSubin in [subin + 1, subin - 1, subin * 2]:
        # 수빈이의 다음 위치가 범위 안에 있고 아직 도착한 적이 없는 위치라면
        if 0 <= nextSubin <= 500000 and visited[nextSubin][time % 2] == -1:
          nextQ.append(nextSubin)  # 새로운 큐에 위치를 넣어주고
          visited[nextSubin][time % 2] = time  # 방문 체크를 해준다.

    # 동생의 위치 K가 짝수초 또는 홀수초에 도착한 적이 있다면
    # 현재 시간을 출력하고 시스템 종료
    if visited[k][time % 2] != -1:
      return time
    
    time += 1
    k += time
    q = nextQ
  
  return -1 


if __name__ == "__main__":
  print(answer_solution())