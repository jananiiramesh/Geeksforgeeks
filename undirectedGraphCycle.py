from collections import defaultdict
from typing import List

class Solution:
	def isCycle(self, V, edges):
	    graph = defaultdict(list)
	    
	    for src, dest in edges:
	        graph[src].append(dest)
	        graph[dest].append(src)
	        
	    visited = [False]*V
	    
	    def dfs(node, parent):
	        visited[node] = True
	        for neighbor in graph[node]:
	            if not visited[neighbor]:
	                if dfs(neighbor, node):
	                    return True
	            elif neighbor != parent:
	                return True
	        return False
	        
	    for j in range(V):
	        if not visited[j]:
	            if dfs(j,-1):
	                return True
	                
	    return False
	    
