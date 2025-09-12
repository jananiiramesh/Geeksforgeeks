#User function Template for python3

class Solution:
    def floor(self, root, x):
        # helper function
        def findPre(node, pre):
            if not node:
                return pre
                
            if node.data == x:
                return node
                
            if node.data > x:
                return findPre(node.left, pre)
                
            else:
                return findPre(node.right, node)
                
        predecessor = findPre(root, None)
        if not predecessor:
            return -1
        return predecessor.data
