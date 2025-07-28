from collections import defaultdict
from typing import List
class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        graph = defaultdict(list)
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
         
        visited = set()   
        result = []
        
        def dfs_helper(node):
            visited.add(node)
            self.temp.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
            
        for j in range(V):
            if j not in visited:
                self.temp = []
                dfs_helper(j)
                result.append(self.temp)
                
        return result
