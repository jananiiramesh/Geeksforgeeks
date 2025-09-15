class Solution:
    def knapsack(self, W, val, wt):
        # recursive solution
        n = len(val)
        # dp = [[-1] * (W+1) for _ in range(n)]
        
        # def recursive(ind, capacity):
        #     if ind < 0:
        #         return 0
                
        #     if dp[ind][capacity] != -1:
        #         return dp[ind][capacity]
                
        #     notTake = recursive(ind - 1, capacity)
        #     take = 0
        #     if capacity - wt[ind] >= 0:
        #         take = val[ind] + recursive(ind - 1, capacity - wt[ind])
                
        #     dp[ind][capacity] = max(notTake, take)
        #     return dp[ind][capacity]
            
        # return recursive(n-1, W)
        
        dp = [[0] * (W+1) for _ in range(n+1)]
        
        #ind needs to be shifted by one, since it starts from -1
        #capacity starts from 0
        
        for ind in range(1, n+1):
            for capacity in range(W+1):
                
                notTake = dp[ind-1][capacity]
                take = 0
                if capacity - wt[ind-1] >= 0:
                    take = val[ind-1] + dp[ind-1][capacity - wt[ind-1]]

                dp[ind][capacity] = max(notTake, take)
            
        return dp[n][W]
