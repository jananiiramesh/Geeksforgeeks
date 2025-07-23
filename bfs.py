from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        visited = set()
        result = []
        queue = deque([0])
        visited.add(0)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbour in adj[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        
        return result
