# 문제 : https://leetcode.com/problems/trapping-rain-water/
# 해결방법 참고: https://www.youtube.com/watch?v=ZI2z5pq0TqA

# 위 영상에서는 해결방법을 2가지로 설명하고 있다. 
# i) O(n) memory solution : maxLeft, maxRight 표를 만들고 min(maxLeft, maxRight) - h[i] 방식으로 해결
# ii) O(1) memory solution : 투포인터 방식... 어찌됐건 "min(maxLeft, maxRight) - h[i]" 이게 핵심이네..;; 
def trap(height):
  if not height:
    return 0
  
  l, r = 0, len(height) - 1 # 투 포인터
  leftMax, rightMax = height[l], height[r]
  res = 0

  while l < r:
    if leftMax < rightMax:
      l += 1
      leftMax = max(leftMax, height[l])
      res += leftMax - height[l]
    else:
      r -= 1
      rightMax = max(rightMax, height[r])
      res += rightMax - height[r]

  return res



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))