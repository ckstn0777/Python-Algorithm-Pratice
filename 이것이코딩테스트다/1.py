# 문제 : 배열이 있을때 주어진 수들을 M번 더하여 가장 큰 수를 만들어라
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

'''
5 7 3
2 4 5 4 6
=> 41이 나와야 함
'''

#############################################
# 내 코드 - 약간 아쉽네. b를 따로 만들필요없이 가장 큰 수 카운트만 구했으면 되었군. 
def mySolution():
  n, m, k = map(int, input().split())
  arr = list(map(int, input().split()))

  max1, max2 = 0, 0
  for i in arr:
    if max2 < i:
      if max1 < i:
        max2 = max1
        max1 = i
      else:
        max2 = i
  
  a = int(m / (k + 1))
  b = m % (k + 1)

  result = (a * k + b) * max1 + a * max2
  return result


#############################################
# 책 코드 - 시간복잡도는 이게 더 걸리긴 할 듯. 정렬 때문에 O(nlog(n))이겠지
def solution():
  n, m, k = map(int, input().split())
  arr = list(map(int, input().split()))

  arr.sort(reverse=True)
  
  result = 0
  
  # 가장 큰 수가 더해지는 횟수
  count = int(m / (k + 1)) * k + m % (k + 1)

  result += count * arr[0]
  result += (m - count) * arr[1]
  
  return result


if __name__ == "__main__":
  print(solution())
  






