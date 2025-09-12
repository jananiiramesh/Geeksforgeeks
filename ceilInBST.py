''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # helper function
        def findSuc(node, succ):
            if not node:
                return succ
                
            if node.data == x:
                return node
                
            if node.data < x:
                return findSuc(node.right, succ)
                
            else:
                return findSuc(node.left, node)
                
        successor = findSuc(root, None)
        if not successor:
            return -1
        return successor.data
