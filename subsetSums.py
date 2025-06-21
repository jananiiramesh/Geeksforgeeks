#User function Template for python3
class Solution:
	def subsetSums(self, arr):
		sums = []
		
		def subset(currindex, currsum):
		    if currindex == len(arr):
		        sums.append(currsum)
		        return
		    
		    subset(currindex+1, currsum+arr[currindex])
		    subset(currindex+1, currsum)
		    
		subset(0,0)
		return sorted(sums)
