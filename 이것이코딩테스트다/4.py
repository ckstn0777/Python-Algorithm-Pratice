# p.311 문제 : 모험가 N이 주어진다. 각 모험가는 공포도가 존재하는데, 공포도가 X인 모함가는 반드시 X명 이상으로 
# 구성된 모험가에 참여해야만 여행을 떠날 수 있다. 이때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라. 

'''
5
2 3 1 2 2 3
'''

# 해결방법 : 단순히 정렬한 다음에 그룹을 나누면 된다. 
def my_solution():
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  
  result, cnt = 0, 0
  for a in arr:
    cnt += 1  

    if a == cnt:
      result += 1
      cnt = 0
  
  return result



if __name__ == "__main__":
  print(my_solution())
