from math import sqrt
class Solution:
    def maxVolume(self, perimeter, area):
       # Calculation of formula to find the maximum volume
        part1 = perimeter - math.sqrt(perimeter**2 - (24 * area))
        term = (part1 / 12)**2
        height = (perimeter / 4) - (2 * (part1 / 12))
        ans = term * height

        # Returning the maximum volume
        return ans