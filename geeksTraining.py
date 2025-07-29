class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        dp = [[0 for _ in range(3)] for _ in range(n)]

        for task in range(3):
            dp[0][task] = arr[0][task]

        for day in range(1, n):
            for task in range(3):
                max_points = 0
                for prev_task in range(3):
                    if prev_task != task:
                        max_points = max(max_points, dp[day - 1][prev_task])
                dp[day][task] = arr[day][task] + max_points

        return max(dp[n - 1])
