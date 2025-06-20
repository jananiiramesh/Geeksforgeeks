#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        #To maximize the number of meetings, its better to keep the 
        #meetings that end earlier first
        meetings = list(zip(start,end))
        meetings.sort(key=lambda x: x[1])
        max_meetings = 1
        i,j = 0, 1
        while j<len(meetings):
            if meetings[j][0] > meetings[i][1]:
                max_meetings += 1
                i = j
            j += 1
        return max_meetings
