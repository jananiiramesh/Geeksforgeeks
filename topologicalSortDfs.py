from collections import defaultdict
from typing import List
class Solution:
    
    def topoSort(self, V, edges):
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            
        visited = [False]*V
        result = []
        
        def dfs(node):
            visited[node] = True
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
            result.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        return result[::-1]
