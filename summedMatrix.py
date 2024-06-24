class Solution:
    def sumMatrix(self, n, q):
        max_val_of_matrix = 2*n
        if q>max_val_of_matrix:
            return 0
        if q==max_val_of_matrix:
            return 1
        diagonal = n+1
        if q==diagonal:
            return n
        else:
            diff = abs(diagonal-q)
            return n-diff