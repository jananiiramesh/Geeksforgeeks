class Solution:
    def decToBinary(self, n):
        rev_bin=""
        if str(n)=="0":
            rev_bin = "0000"
            return rev_bin
        while((n//2)!=0):
            rev_bin=rev_bin+str(n%2)
            n=n//2
        rev_bin=rev_bin+"1"
        return rev_bin
        
    def revString(self, n):
        newString = ""
        i=-1
        while(i>=(-(len(n)))):
            newString = newString + n[i]
            i=i-1
        return newString
        
    def reversedBits(self, x):
        
        x_str = str(self.revString(self.decToBinary(x)))
        dec = 0
        if(len(x_str)!=32):
            x_str = '0'*(32-len(x_str)) + x_str
        for i in range(32):
            if x_str[i] == '1':
                dec = dec + 2**i
        return dec