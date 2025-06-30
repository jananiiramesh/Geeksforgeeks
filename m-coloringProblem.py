# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        
        clashes = {}
        for edge in edges:
            if edge[0] not in clashes:
                clashes[edge[0]] = []
            if edge[1] not in clashes:
                clashes[edge[1]] = []
                
            clashes[edge[0]].append(edge[1])
            clashes[edge[1]].append(edge[0])
            
        color_set = [0]*v
        
        def graph(node, color):
            if node == v:
                ##successfully allocated for all nodes
                return True
                
            for n in clashes.get(node, []):
                if color_set[n] == color:
                    if color < m:
                        return graph(node, color + 1)
                    else:
                        return False
                        
            color_set[node] = color
            if graph(node + 1, 1):
                return True
                
            else:
                #backtrack
                color_set[node] = 0
                
            if color < m:
                return graph(node, color + 1)
                
            return False
            
            
        return graph(0,1)
