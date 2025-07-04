class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        arr = []
        for i in range(len(s)):
            arr.append(s.pop())
            
        arr.sort()
        for j in range(len(arr)):
            s.append(arr.pop(0))
