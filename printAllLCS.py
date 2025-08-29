class Solution:
    def allLCS(self, s1, s2):
        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        memo = [[None] * (m + 1) for _ in range(n + 1)]

        def backtrack(i, j):
            if i == 0 or j == 0:
                return {""}

            if memo[i][j] is not None:
                return memo[i][j]

            if s1[i - 1] == s2[j - 1]:
                prev = backtrack(i - 1, j - 1)
                result = {s + s1[i - 1] for s in prev}
            else:
                result = set()
                if dp[i - 1][j] >= dp[i][j - 1]:
                    result |= backtrack(i - 1, j)
                if dp[i][j - 1] >= dp[i - 1][j]:
                    result |= backtrack(i, j - 1)

            memo[i][j] = result
            return result

        all_lcs = list(backtrack(n, m))
        return sorted(all_lcs) 
