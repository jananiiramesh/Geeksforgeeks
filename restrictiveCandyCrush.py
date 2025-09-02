#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        if k == 1:
            return ""
            
        length = len(s)
        stack = []
        
        for i in range(length):
            if not stack or s[i] != stack[-1][0]:
                stack.append([s[i],1])
            else:
                if stack[-1][1] + 1 == k:
                    stack.pop()
                else:
                    stack[-1][1] += 1
                    
        string = ""
        for i in range(len(stack)):
            string += stack[i][0] * stack[i][1]
            
        return string
