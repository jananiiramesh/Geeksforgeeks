from collections import defaultdict
class Solution:
    def celebrity(self, mat):
        #graph based approach
        # n = len(mat)
        # in_degree = [0]*n
        # out_degree = [0]*n
        
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         if mat[i][j] == 1:
        #             out_degree[i] += 1
        #             in_degree[j] += 1
                    
        # for i in range(n):
        #     if in_degree[i] == n - 1  and out_degree[i] == 0:
        #         return i
                
        # return -1
        
        n = len(mat)
        top = 0
        down = n - 1
        while (top < down):
            if mat[top][down] == 1:
                top += 1
            elif mat[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1
                
        candidate = top

        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1:
                    return -1
                if mat[i][candidate] == 0:
                    return -1

        return candidate

        
