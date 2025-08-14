from collections import deque

class Solution:
    def shortestPath(self, adj, src):
        V = len(adj)
        distances = [float('inf')]*V
        distances[src] = 0
        
        queue = deque([(src, distances[src])])
        
        while queue:
            node, dist = queue.popleft()
            for neighbour in adj[node]:
                if dist + 1 < distances[neighbour]:
                    distances[neighbour] = dist + 1
                    queue.append((neighbour, distances[neighbour]))
                    
        for i in range(V):
            if distances[i] == float('inf'):
                distances[i] = -1
                
        return distances
