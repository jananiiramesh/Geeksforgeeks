'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
            
        hd_map = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            hd_map[hd] = node.data
            
            if node.left:
                queue.append([node.left, hd-1])
            if node.right:
                queue.append([node.right, hd+1])
                
        bottom = []
        for key in sorted(hd_map.keys()):
            bottom.append(hd_map[key])
            
        return bottom
