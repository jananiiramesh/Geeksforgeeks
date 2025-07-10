#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def inOrder(self, root):
        ans = []
        stack = []
        
        t = root
        while stack or t:
            while t:
                stack.append(t)
                t = t.left
            
            temp = stack.pop()
            ans.append(temp.data)
            t = temp.right
            
        return ans
