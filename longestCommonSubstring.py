#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        ans = 0

        for ind1 in range(1, len(s1) + 1):
            for ind2 in range(1, len(s2) + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                    ans = max(ans, dp[ind1][ind2])
                else:
                    dp[ind1][ind2] = 0
                    
        return ans
