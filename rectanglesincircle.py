class Solution:
    def rectanglesInCircle(self,r):
        rectangles = 0
        diameter = 2*r 
        square_diameter = diameter*diameter 
        for i in range(1,2*r):
            for j in range(1,2*r):
                diagonal_length=(i*i)+(j*j)
                if diagonal_length <= square_diameter:
                    rectangles+=1
        return rectangles