class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def decToBinary(self, n):
        gray=""
        if str(n)=="0":
            gray = "0000"
            return gray
        while((n//2)!=0):
            gray=gray+str(n%2)
            n=n//2
        gray=gray+"1"
        return gray
        
    def revString(self, n):
        newString = ""
        i=-1
        while(i>=(-(len(n)))):
            newString = newString + n[i]
            i=i-1
        return newString
        
    def binaryToDec(self, n):
        dec = 0
        for i in range(len(n)):
            if n[i]=="1":
                dec = dec + 2**(len(n)-1-i)
        return dec
        
    def grayToBinary(self,n):
        gray = self.revString(self.decToBinary(n))
        binary = gray[0]
        for j in range(1, len(gray)):
            binary = binary + str(int(gray[j]) ^ int(binary[j-1]))
        return self.binaryToDec(binary)