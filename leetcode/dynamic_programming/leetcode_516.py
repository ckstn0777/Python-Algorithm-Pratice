# Solution 1. Top down DP
class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)

        def dp(l, r):
            if l > r: return 0 # l이 r보다 더 커지면 종료 (탈출조건)
            if l == r: return 1 # s의 길이가 1인 경우
            if s[l] == s[r]:
                return dp(l + 1, r - 1) + 2
            
            return max(dp(l, r - 1), dp(l + 1, r))


        return dp(0, n - 1)


# Solution 2. Bottom up DP
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n - 1, -1, -1):
#             dp[i][i] = 1
#             for j in range(i+1, n):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

#         return dp[0][n - 1]