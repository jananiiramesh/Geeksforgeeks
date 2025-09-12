'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        def findSuc(node, succ):
            if not node:
                return succ
                
            if node.data <= key:
                return findSuc(node.right, succ)
                
            else:
                return findSuc(node.left, node)
        
        def findPre(node, pre):
            if not node:
                return pre
                
            if node.data >= key:
                return findPre(node.left, pre)
                
            else:
                return findPre(node.right, node)
            
        return(findPre(root, None), findSuc(root, None))
