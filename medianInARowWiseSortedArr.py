#User function Template for python3

from bisect import bisect_right
class Solution:
    def median(self, mat):
    	
    	low = min(row[0] for row in mat)
    	high = max(row[-1] for row in mat)
    	
    	n = len(mat)
    	m = len(mat[0])
    	
    	pos = (n*m+1)//2
    	
    	while (low < high):
    	    mid = (low + high) // 2
    	    
    	    count = 0
    	    for row in mat:
    	        count += bisect_right(row, mid)
    	        
    	    if count < pos:
    	        low = mid + 1
    	    
    	    else:
    	        high = mid
    	        
    	        
    	return low
