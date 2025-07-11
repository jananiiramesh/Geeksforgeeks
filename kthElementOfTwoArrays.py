#User function Template for python3
from bisect import bisect_right

class Solution:

    def kthElement(self, a, b, k):
        if not a:
            return b[k-1]
        if not b:
            return a[k-1]
        
        low = min(a[0], b[0])
        high = max(a[-1], b[-1])
        
        def count_less(x):
            return bisect_right(a,x) + bisect_right(b,x)
        
        while low < high:
            mid = (low + high) // 2
            
            if count_less(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low
            
        pass
