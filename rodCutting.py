#User function Template for python3

class Solution:
    def cutRod(self, price):
        n = len(price)
        
        # def recursive(ind, rod):
        #     if rod == 0:
        #         return 0
        #     if ind < 0:
        #         return 0
                
        #     notTake = 0 + recursive(ind - 1, rod)
        #     take = 0
        #     if rod - (ind + 1) >= 0:
        #         take = price[ind] + recursive(ind, rod - (ind + 1))
                
        #     return max(notTake, take)
            
        # return recursive(n - 1, n)
        # tle only 10 testcases passing
        
        # trying to memoize it
        # dp = [[-1] * (n + 1) for _ in range(n)]
        
        # def recursive(ind, rod):
        #     if rod == 0:
        #         return 0
        #     if ind < 0:
        #         return 0
                
        #     if dp[ind][rod] != -1:
        #         return dp[ind][rod]
                
        #     notTake = 0 + recursive(ind - 1, rod)
        #     take = 0
        #     if rod - (ind + 1) >= 0:
        #         take = price[ind] + recursive(ind, rod - (ind + 1))
                
        #     dp[ind][rod] = max(notTake, take)
            
        #     return dp[ind][rod]
            
        # return recursive(n - 1, n)
        # tle again, 1010 testcases
        
        # tabulation
        # dp = [[0] * (n + 1) for _ in range(n)]
        
        # for i in range(n):
        #     dp[i][0] = 0
            
        # for r in range(1, n + 1):
        #     dp[0][r] = r * price[0]
            
        # for ind in range(1, n):
        #     for rod in range(1, n+1):
        #         notTake = 0 + dp[ind-1][rod]
        #         take = 0
        #         if rod - (ind + 1) >= 0:
        #             take = price[ind] + dp[ind][rod - (ind+1)]
                    
        #         dp[ind][rod] = max(notTake, take)
                
        # return dp[n-1][n]
        # works so perfectly but tle again
        
        #trying a 1d array
        dp = [0] * (n + 1)
        
        for r in range(1, n+1):
            dp[r] = r * price[0]
            
        for ind in range(1, n):
            for rod in range(1, n+1):
                if rod >= ind + 1:
                    dp[rod] = max(dp[rod], price[ind] + dp[rod - (ind + 1)])
                    
        return dp[n]
        
        
        
