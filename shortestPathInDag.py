#User function Template for python3
from collections import defaultdict
from typing import List


class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
                         dag = defaultdict(list)
                         for edge in edges:
                             dag[edge[0]].append((edge[1], edge[2]))
                          
                         visited = [0]*V
                         stack = []
                         
                         def dfs_topo(node):
                             visited[node] = 1
                             for neighbour, weight in dag[node]:
                                 if not visited[neighbour]:
                                     dfs_topo(neighbour)
                             stack.append(node)
                             
                         for i in range(V):
                             if not visited[i]:
                                 dfs_topo(i)
                                 
                         distances = [float('inf')]*V
                         distances[0] = 0
                         
                         while stack:
                             node = stack.pop()
                             for neighbour, weight in dag[node]:
                                 if distances[node] + weight < distances[neighbour]:
                                     distances[neighbour] = distances[node] + weight
                                     
                         for i in range(V):
                             if distances[i] == float('inf'):
                                 distances[i] = -1
                                 
                         return distances
