class Solution:
    def threeWayPartition(self, array, a, b):
        if a > b:  # Handling invalid range
            return array
        
        left, mid, right = 0, 0, len(array) - 1
        
        while mid <= right:
            if array[mid] < a:
                array[left], array[mid] = array[mid], array[left]
                left += 1
                mid += 1
            elif array[mid] >= a and array[mid] <= b:
                mid += 1
            else:
                array[mid], array[right] = array[right], array[mid]
                right -= 1
        
        return array