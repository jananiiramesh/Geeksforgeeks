class Solution:
    def findMissing(self,a,b,n,m):
        missing_ele = []
        b_set = set(b)
        for num in a:
            if num not in b_set:
                missing_ele.append(num)
        return missing_ele