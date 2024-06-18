class Solution:
    def armstrongNumber (self, n):
        original=n
        sum_cube=0
        while n>0:
            cube = (n%10)*(n%10)*(n%10)
            sum_cube = sum_cube + cube
            n = n//10
        if sum_cube == original:
            return "true"
        else:
            return "false"