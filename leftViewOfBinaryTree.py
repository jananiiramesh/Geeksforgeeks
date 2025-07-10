from collections import deque
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        if not root:
            return []
           
        leftView = [] 
        q = deque()
        q.append(root)
        
        while q:
            lvl_size = len(q)
            
            for i in range(lvl_size):
                node = q.popleft()
                
                if i == 0:
                    leftView.append(node.data)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
                    
        return leftView
