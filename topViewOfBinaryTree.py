# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import deque

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return []
         
        hd_map = {}   
        queue = deque([(root,0)])
        
        while queue:
            
            node, hd = queue.popleft()
            
            if hd not in hd_map:
                hd_map[hd] = node.data
                
            if node.left:
                queue.append([node.left, hd-1])
            if node.right:
                queue.append([node.right, hd+1])
                
        top = []
        for key in sorted(hd_map.keys()):
            top.append(hd_map[key])
            
        return top
