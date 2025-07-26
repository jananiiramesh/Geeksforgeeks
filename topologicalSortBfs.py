from collections import defaultdict, deque
from typing import List
class Solution:
    
    def topoSort(self, V, edges):
        graph = defaultdict(list)
        in_degree = [0]*V
        
        for src, dest in edges:
            graph[src].append(dest)
            in_degree[dest] += 1
            
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        topo_sort = []
        
        
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return topo_sort
