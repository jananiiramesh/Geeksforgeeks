#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        stack = []
        postorder = []
        
        lastVisited = None
        t = root
        
        while stack or t:
            if t:
                stack.append(t)
                t = t.left
            else:
                top = stack[-1]
                if top.right and lastVisited != top.right:
                    t = top.right
                else:
                    postorder.append(top.data)
                    lastVisited = stack.pop()
                    
        return postorder
