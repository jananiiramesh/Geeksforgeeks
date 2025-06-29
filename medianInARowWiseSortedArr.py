#User function Template for python3

class Solution:
    def median(self, mat):
    	mat_1d = [ele for sublist in mat for ele in sublist]
    	mat_1d.sort()
    	low, high = 0, len(mat_1d) - 1
    	return mat_1d[(low + high) // 2]
