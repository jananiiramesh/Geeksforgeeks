class Solution:
    def findSingle(self, n, arr):
        arr.sort()
        i=0
        while(i<(n-1)):
            if(arr[i]!=arr[i+1]):
                return arr[i]
            i=i+2
        if (i==n-1):
            return arr[i]
        return -1