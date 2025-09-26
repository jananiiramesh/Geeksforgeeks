from collections import deque, defaultdict
class Solution:
    def isBipartite(self, V, edges):
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        color = [-1]*V
            
        for i in range(V):
            if color[i] == -1:
                color[i] = 0
                queue = deque([i])
                
                while queue:
                    node = queue.popleft()
                    
                    for neighbour in graph[node]:
                        if color[neighbour] == -1:
                            color[neighbour] = 1 - color[node]
                            queue.append(neighbour)
                            
                        elif color[neighbour] == color[node]:
                            return False
                            
        return True
