class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        n = len(intervals)
        intervals.sort(key = lambda x:x[1]) #sort by ending time
        count = 0 #counter for removing intervals
        prevEnd = intervals[0][1] #initialise ends

        for i in range (1,n):
            if intervals[i][0] < prevEnd: #overlap
                count += 1
            else:
                prevEnd = intervals[i][1] #end of current
        return count