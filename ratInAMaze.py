class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        #paramters to rem
        
        n = len(maze) - 1
        coords = []
        res = []
        
        def Maze(x, y, actionstring):
            if not 0<=x<=n or not 0<=y<=n:
                return
            
            if maze[x][y] == 0:
                return
            
            if (x,y) in coords:
                return
            
            if x == n and y == n:
                #final destination reached
                res.append(actionstring[:])
                
                
            coords.append((x,y))
            Maze(x + 1, y, actionstring + 'D')
            Maze(x, y - 1, actionstring + 'L')
            Maze(x - 1, y, actionstring + 'U')
            Maze(x, y + 1, actionstring + 'R')
            
            coords.pop()
            
        Maze(0,0,"")
        return sorted(res)
