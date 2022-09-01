# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

####################
# 내 소스 코드 - 반복문 제한 조건을 "answer <= len(queue1) + len(queue2)" 로 했었는데 테스트 케이스 1번만 통과를 못하네
# 찾아보니 [1, 1, 1, 1, 1], [1, 1, 1, 9, 1] 기댓값 〉12 인 경우 같은게 있네. 호우... 그래서 대충 1000000으로 하면 통과되긴 하더라
def my_solution(queue1, queue2):
    answer = 0

    de_queue1 = deque(queue1)
    de_queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    while answer < 1000000: # 대충 이정도면 반복하면 되지 않을까 생각하는데... 좀 그렇긴 하다 ㅋㅋ
      if queue1_sum == queue2_sum:
        return answer

      answer += 1
      
      if queue1_sum > queue2_sum:
        a = de_queue1.popleft()
        de_queue2.append(a)
        queue1_sum -= a
        queue2_sum += a
      else:
        a = de_queue2.popleft()
        de_queue1.append(a)
        queue2_sum -= a
        queue1_sum += a


    return -1


####################
# 추천 정답 코드 : 와 이 방법이 진짜 확실하네...;; 이렇게도 푸는구나
def solution(queue1, queue2):
  # 먼저 가능한지 여부부터 파악
  queSum = (sum(queue1) + sum(queue2))
  if queSum % 2 != 0:
    return -1

  target = queSum // 2

  n = len(queue1)
  start = 0
  end = n - 1
  ans = 0

  cur = sum(queue1)
  queue3 = queue1 + queue2
  while cur != target:
    if cur < target:
      end += 1
      cur += queue3[end]
    else:
      cur -= queue3[start]
      start += 1
    ans += 1

  return ans
  



print(solution([1], [2]))