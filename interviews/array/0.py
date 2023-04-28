

# 짝수가 먼저 나오도록 배열을 재배열해보라 (순서는 고려하지 않음. 대신 공간복잡도는 O(1)로 할 것)
def solution(arr):
  next_even, next_odd = 0, len(arr) - 1

  while next_even < next_odd:
    if arr[next_even] % 2 == 0: # 짝수면 그냥 next_even을 1증가
      next_even += 1
    else: # 홀수라면 swap을 해주고 next_odd을 1 감소
      arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
      next_odd -= 1
  
  return arr


if __name__ == "__main__":
    arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

    print(solution(arr)) 