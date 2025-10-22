class Solution:
    def leaders(self, arr):
        n = len(arr)
        max_array = [0] * n
        
        for i in range(n-1, -1, -1):
            if i == n - 1:
                max_array[i] = arr[i]
            else:
                max_array[i] = max(max_array[i+1], arr[i])
                
        output = []
        
        for i in range(n):
            if max_array[i] == arr[i]:
                output.append(max_array[i])
                
        return output
