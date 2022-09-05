# 문제 : https://leetcode.com/problems/climbing-stairs/
# 참고 : https://www.youtube.com/watch?v=Y0lT9Fck7qI

# 해결방법 : 만약에 n = 3일때라고 생각해보자. n = 3을 도달하려면 결국 n = 2일때에서는 1 step만 가능하다. 
# n = 1일때에서는 1 or 2 step이 가능하다. 하지만 1 step인 경우는 이미 n = 2랑 중복되므로 2 step만 생각하면 된다.
# 이를 공식으로 만들어보면 N[3] = N[2] + N[1]이 된다. (N[n] = N[n-1] + N[n-2].. 피보나치 수열...)

# 피보나치 수열 구현 방법은 캐시를 이용한 방법이 있지만, 상향식 방식으로 캐시를 반복적으로 채우면
# 공간복잡성을 줄이고, 캐시를 재사용할 수 있다. 
def climbStairs(n):
  if n <= 2:
    return n
  
  fMinus2 = 1 # 뒤에거
  fMinus1 = 2 # 앞에거 

  for _ in range(3, n + 1):
    f = fMinus2 + fMinus1 # 더해준다음
    fMinus2 = fMinus1 # 한칸씩 이동(f2는 f1이 되고)
    fMinus1 = f # 한칸씩 이동(f1은 f가 되고)
  
  return fMinus1




print(climbStairs(4))