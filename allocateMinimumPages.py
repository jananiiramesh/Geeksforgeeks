class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        
        if k > len(arr):
            return -1
            
        def helper(arr, mid):
            students = 1
            page_student = 0
            for i in range(len(arr)):
                if page_student + arr[i] > mid:
                    students += 1
                    page_student = arr[i]
                
                else:
                    page_student += arr[i]
                    
            return students
            
        low, high = max(arr), sum(arr)
        while low < high:
            mid = (low + high) // 2
            students = helper(arr, mid)
            
            if (students > k):
                low = mid + 1
                
            else:
                high = mid
                
        return low
        
        
