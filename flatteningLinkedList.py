'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
                
            if a.data < b.data:
                result = a
                result.bottom = merge(a.bottom, b)
            else:
                result = b
                result.bottom = merge(a, b.bottom)
                
            return result 
            
        def flatten_helper(root):
            if root is None or root.next is None:
                return root
                
            root.next = flatten_helper(root.next)
            
            root = merge(root, root.next)
            
            return root
            
        return flatten_helper(root)
