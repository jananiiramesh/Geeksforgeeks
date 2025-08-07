class Solution:
    def isSubsetSum (self, arr, sum):
        #recursive solution
        n = len(arr)
        def recursive(ind, subset_sum):
            if subset_sum == sum:
                return True
                
            if ind == n or subset_sum > sum:
                return False
                
            return recursive(ind + 1, subset_sum + arr[ind]) or recursive(ind + 1, subset_sum)
            
        return recursive(0,0)
        
