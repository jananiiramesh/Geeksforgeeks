#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        ##note: in reality, you don't actually need to keep track of arrival and departure
        ##of one train together. You can always, keep them separate cuz at the end of the
        ##the day, all you wanna know is how many trains are intersecting in times, not which one
        arr.sort()
        dep.sort()
        i, j = 0, 0
        max_platforms = 0
        intersections = 0
        while i<len(arr) and j<len(dep):
            #+1 to intersections when a train arrival time is first
            #-1 to intersections when train departure time is first
            if arr[i] <= dep[j]:
                intersections += 1
                i += 1
            else:
                intersections -= 1
                j += 1
            max_platforms = max(max_platforms, intersections)
        return max_platforms
