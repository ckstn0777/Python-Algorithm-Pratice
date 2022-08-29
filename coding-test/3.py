# p.99 문제 : 어떠한 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 
# 1. N에서 1을 뺀다. 2. N을 K로 나눈다. (단, 나눌 수 있는 경우에만 가능)
# 이 때, 최소 횟수를 구하는 프로그램을 작성하시오. 

'''
25 4
'''

# 내 코드
def mySolution():
  n, k = map(int, input().split())
  result = 0

  while n != 1:
    if n % k == 0:
      n = n // k
    else:
      n = n - 1
  
    result += 1
  
  return result


# 추천 코드. N이 100억 이상의 큰 수가 되는 경우를 가정했을 때 빠르게 동작시키기 위해 1씩 빼주는 대신
# N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식으로 코드를 작성할 수 있다. ex) 124 25
def solution():
  n, k = map(int, input().split())
  result = 0
  
  while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
      break

    # k로 나누기
    result += 1
    n = n // k
  
  return result - 1 # 음.. 마지막에 result += (n - target) 해줬으니까... 

  
if __name__ == "__main__":
  print(solution())