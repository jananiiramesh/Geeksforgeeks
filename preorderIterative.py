'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        ans = []
        stack = []
        
        t = root
        while stack or t:
            while t:
                stack.append(t)
                ans.append(t.data)
                t = t.left
                
            temp = stack.pop()
            t = temp.right
            
        return ans
