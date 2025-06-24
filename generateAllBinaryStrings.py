#User function Template for python3

class Solution:
    def generateBinaryStrings(self, n):
        res = []
        
        def generate(index, string):
            #either put 0 or 1
            if index == n:
                res.append(string[:])
                return
                
            generate(index + 1, string + "0")
            if not string or string[-1] != '1':
                generate(index + 1, string + "1")
            
        generate(0,"")
        
        return res
