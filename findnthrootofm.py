#User function Template for python3

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		low = 1
		high = m
		while (low <= high):
		    mid = (low + high) // 2
		    if mid ** n == m:
		        return mid
		    else:
		        if mid ** n > m:
		            high = mid - 1
		        else:
		            low = mid + 1
		            
        return -1 
