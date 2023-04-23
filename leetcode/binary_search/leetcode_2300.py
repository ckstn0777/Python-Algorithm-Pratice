class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        potions.sort() # 일단 혹시 몰라 정렬해준다
        answer = []

        for i in range(len(spells)):
            s = spells[i]
            # s_p = list(map(lambda x : s * x, potions))

            # 이진 탐색
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2

                if success <= s * potions[mid]:
                    # 같으면 좋은거고, 최소한 sucess보다 커야 우리가 구하는 정답임
                    right = mid - 1
                else:
                    left = mid + 1

            # print(left, right, s_idx)
            answer.append(len(potions) - left)
        
        return answer