class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n)]

        dp[0][0] = 2 if arr[0] == 0 else 1
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            for s in range(0, target + 1):
                notTake = dp[i - 1][s]
                take = 0
                if arr[i] <= s:
                    take = dp[i - 1][s - arr[i]]
                dp[i][s] = notTake + take

        return dp[n - 1][target]
