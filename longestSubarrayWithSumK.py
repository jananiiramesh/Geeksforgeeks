# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k): 
        longest = 0
        diff_set = {}
        n = len(arr)
        prefix = [0]*n
        for i in range(n):
            if i == 0:
                prefix[i] = arr[i]
            else:
                prefix[i] = prefix[i-1] + arr[i]
                
        for j in range(n):
            if prefix[j] == k:
                longest = max(longest, j+1)
            else:
                diff = prefix[j] - k
                if diff in diff_set:
                    longest = max(longest, j - diff_set[diff])
                if prefix[j] not in diff_set:
                    diff_set[prefix[j]] = j
        
        return longest
