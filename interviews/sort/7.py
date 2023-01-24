## 문제 : 구간의 합 구하기. 열린 구간일 수도, 닫힌 구간일 수도 있다. 이런 구간을 하나로 합치려고 한다. 
## 이러한 구간 집합이 주어졌을 때, 이들을 합친 결과가 서로 중복되지 않고 구간 집합으로 출력하시오. 


class Interval:
  def __init__(self, l_val, l_isClosed, r_val, r_isClosed):
    self.left = Interval.EndPoint(l_val, l_isClosed)
    self.right = Interval.EndPoint(r_val, r_isClosed)

  class EndPoint:
    def __init__(self, val, isClosed):
      self.val = val
      self.isClosed = isClosed


def solution(intervals):
  print(intervals)

  # 정렬부터. 왼쪽 값이 작을수록. 동일하다면 isClosed가 true인게 먼저 나오도록. 
  intervals.sort(key = lambda interval: (interval.left.val, not interval.left.isClosed))

  answer = []
  temp = None
  for i in range(len(intervals)):
    cur = intervals[i]
    if not temp:
      temp = cur
      continue

    # temp 오른쪽과 cur 왼쪽 비교해서 만약 포함된다면
    if temp.right.val > cur.left.val or (temp.right.val == cur.left.val and (temp.right.isClosed or cur.left.isClosed)):

      if temp.right.val < cur.right.val:
        temp.right.val = cur.right.val
        temp.right.isClosed = cur.right.isClosed
      elif temp.right.val == cur.right.val:
        temp.right.isClosed = (temp.right.isClosed or cur.right.isClosed)
    else:
      answer.append(temp)
      temp = cur

  if temp:
    answer.append(temp)

  return answer


if __name__ == "__main__":
  answer = solution([
    Interval(1, True, 1, True), 
    Interval(0, False, 3, False), 
    Interval(2, True, 4, True), 
    Interval(3, True, 4, False), 
    Interval(5, True, 7, False), 
    Interval(7, True, 8, False), 
    Interval(8, True, 11, False), 
    Interval(9, False, 11, True), 
    Interval(12, True, 14, True), 
    Interval(12, False, 16, True), 
    Interval(13, False, 15, False), 
    Interval(16, False, 17, False)
  ])

  for i in range(len(answer)):
    print('[' if answer[i].left.isClosed else '(', end='')
    print('left =', answer[i].left.val, 'right=', answer[i].right.val, end='')
    print(']' if answer[i].right.isClosed else ')')