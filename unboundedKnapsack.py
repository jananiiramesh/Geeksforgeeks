#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        n = len(val)
        # def recursive(ind, cap):
        #     if cap == 0:
        #         return 0
        #     if ind < 0:
        #         return 0
                
        #     notTake = recursive(ind - 1, cap)
        #     if cap - wt[ind] >= 0:
        #         take = val[ind] + recursive(ind, cap - wt[ind])
        #     else:
        #         take = 0
                
        #     return max(notTake, take)
            
        # return recursive(n-1, capacity)
        
        # memoization
        # dp = [[-1] * (capacity + 1) for _ in range(n)]
        
        # def recursive(ind, cap):
        #     if cap == 0:
        #         return 0
        #     if ind < 0:
        #         return 0
                
        #     if dp[ind][cap] != -1:
        #         return dp[ind][cap]
                
        #     notTake = recursive(ind - 1, cap)
        #     if cap - wt[ind] >= 0:
        #         take = val[ind] + recursive(ind, cap - wt[ind])
        #     else:
        #         take = 0
                
        #     dp[ind][cap] = max(notTake, take)
            
        #     return dp[ind][cap]
            
        # return recursive(n-1, capacity)
        
        # tabulation
        dp = [[0] * (capacity + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 0
            
        for c in range(capacity + 1):
            if c >= wt[0]:
                dp[0][c] = val[0] + dp[0][c - wt[0]]
            
        for ind in range(1, n):
            for cap in range(1, capacity + 1):
                notTake = dp[ind - 1][cap]
                if cap - wt[ind] >= 0:
                    take = val[ind] + dp[ind][cap - wt[ind]]
                else:
                    take = 0
                    
                dp[ind][cap] = max(notTake, take)
                    
        return dp[n-1][capacity]
                
