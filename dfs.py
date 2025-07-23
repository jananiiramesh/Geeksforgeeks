class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        visited = set()
        result = []
        
        def dfs_helper(node):
            visited.add(node)
            result.append(node)
            
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs_helper(neighbour)
                    
        dfs_helper(0)
        return result
