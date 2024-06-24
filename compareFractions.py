from fractions import Fraction

class Solution:
    def compareFrac (self, str):
        l = [s.strip() for s in str.split(",")]  # Strip whitespace from each element
        frac1 = Fraction(l[0])
        frac2 = Fraction(l[1])
        
        if frac1 > frac2:
            return l[0]
        elif frac1 < frac2:
            return l[1]
        else:
            return "equal"