'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
            
        ans = [root.data] if root.left or root.right else []
        stack = []
        
        def leftsubtree(node):
            if not node or (not node.left and not node.right):
                #reached a leaf node
                return
            
            ans.append(node.data)
            if node.left:
                leftsubtree(node.left)
            else:
                leftsubtree(node.right)
                
        def leafnodes(node):
            if not node:
                return
            
            if not node.left and not node.right:
                ans.append(node.data)
                return
                
            leafnodes(node.left)
            leafnodes(node.right)
            
        def rightsubtree(node):
            if not node or (not node.left and not node.right):
                return
            
            stack.append(node.data)
            if node.right:
                rightsubtree(node.right)
            else:
                rightsubtree(node.left)
                
                
        leftsubtree(root.left)
        leafnodes(root)
        rightsubtree(root.right)
        
        while stack:
            ans.append(stack.pop())
            
        return ans
