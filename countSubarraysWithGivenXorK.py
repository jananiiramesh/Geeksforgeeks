class Solution:
    def subarrayXor(self, arr, k):
        n = len(arr)
        prefix = [0]*n
        count = 0
        xor_set = {}
        
        for i in range(n):
            if i == 0:
                prefix[i] = arr[i]
            else:
                prefix[i] = prefix[i-1] ^ arr[i]
                
        for j in range(n):
            if prefix[j] == k:
                count += 1
            
            req = prefix[j] ^ k
            if req in xor_set:
                count += xor_set[req]
                    
            xor_set[prefix[j]] = xor_set.get(prefix[j], 0) + 1
        
        return count
