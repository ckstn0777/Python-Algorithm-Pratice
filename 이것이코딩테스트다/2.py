# p.96 문제 : N x M 형태로 숫자가 쓰인 카드들이 놓여 있다. 가장 높은 숫자가 쓰인 카드 한장을 뽑아야 한다. 
# 단, 먼저 뽑고자 하는 카드가 있는 행을 선택한 다음, 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드만 뽑을 수 있다. 

'''
3 3
3 1 2
4 1 4
2 2 2
'''

def mySolution():
  n, m = map(int, input().split())
  
  result = 0
  for _ in range(n):
    arr = list(map(int, input().split()))
    result = max(result, min(arr))
  
  return result

  
if __name__ == "__main__":
  print(mySolution())