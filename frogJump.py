#User function Template for python3
class Solution:
    def minCost(self, height):
        # self.min_cost = float("inf")
        # self.max_step = len(height) - 1
        
        # def helper(step, cost):
        #     if step == self.max_step:
        #         self.min_cost = min(self.min_cost, cost)
        #         return
            
        #     if step+1 <= self.max_step:
        #         helper(step+1, cost + abs(height[step] - height[step+1]))
        #     if step+2 <= self.max_step:
        #         helper(step+2, cost + abs(height[step] - height[step+2]))
            
        # helper(0, 0)
        # return self.min_cost
        
        n = len(height)
        dp = [0]*n
        dp[0] = 0
        if n > 1:
            dp[1] = abs(height[1] - height[0])
            
        for i in range(2, n):
            dp[i] = min(
                dp[i-1] + abs(height[i] - height[i-1]),
                dp[i-2] + abs(height[i] - height[i-2])
                )
                
        return dp[-1]
