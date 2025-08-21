'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        if not root:
            return False
            
        def children_checker(node):
            if not node:
                return True
                
            if not node.left and not node.right:
                return True
                
            left_side = children_checker(node.left)
            right_side = children_checker(node.right)
            
            if left_side and right_side:
                left_val = node.left.data if node.left else 0
                right_val = node.right.data if node.right else 0
                return node.data == left_val + right_val
                
            return False
            
        return children_checker(root)
