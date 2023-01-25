'''
11 12
12 1 11 2 10 3 4 5 6 6 1
'''


def solution():
  n, m = map(int, input().split())  
  if n == 0:
    return 0
  
  books = list(map(int, input().split()))
  result = 0
  temp_sum = 0

  for i in range(len(books)):
    temp_sum += books[i]
    if temp_sum > m:
      result += 1
      temp_sum = books[i]

  if temp_sum > 0:
    result += 1
  
  return result
      



if __name__ == "__main__":
    print(solution())
