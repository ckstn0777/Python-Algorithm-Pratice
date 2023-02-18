# 투포인터라고 볼 수도 있고... 아무튼 규칙만 잘 찾아서 구현만 잘 하면 됨. 

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        odd_pos = [-1]
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_pos.append(i)
        odd_pos.append(len(nums))
        
        result = 0

        for i in range(1, len(odd_pos) - k):
            result += (odd_pos[i] - odd_pos[i - 1]) * (odd_pos[i + k] - odd_pos[i + k - 1])

        return result
