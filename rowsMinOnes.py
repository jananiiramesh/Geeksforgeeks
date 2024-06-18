class Solution:
    def minRow(self,n,m,a):
        min_ones = 1001
        index = 0
        for i in range(1,n+1):
            if a[i-1].count(1)<min_ones:
                min_ones = a[i-1].count(1)
                index = i
        return index