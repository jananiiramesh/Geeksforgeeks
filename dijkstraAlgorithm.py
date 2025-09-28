import heapq
from collections import defaultdict
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # use priority queue
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
            graph[edge[1]].append([edge[0], edge[2]])
            
        distances = [float('inf')] * V
        distances[src] = 0
        min_heap = []
        
        heapq.heappush(min_heap, [distances[src], src])
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            for neighbour in graph[node]:
                if distances[neighbour[0]] > dist + neighbour[1]:
                    distances[neighbour[0]] = dist + neighbour[1]
                    heapq.heappush(min_heap, [distances[neighbour[0]], neighbour[0]])
                    
        for i in range(V):
            if distances[i] == float('inf'):
                distances[i] = -1
                
        return distances
        
        
