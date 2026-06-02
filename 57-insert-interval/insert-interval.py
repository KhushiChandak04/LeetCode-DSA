class Solution(object):
    def insert(self, intervals, newInterval):
        ans = [] #answer array to return intervals
        i = 0 #initialise start for traversing
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]: #left side append as it is
            ans.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]: #for overlapping part merge it, current stats before newinterval ends
            newInterval[0] = min(newInterval[0], intervals[i][0]) #start of new interval
            newInterval[1] = max(newInterval[1], intervals[i][1]) #end of new interval
            i += 1
        ans.append(newInterval)
        while i<n: #right side append as it is
            ans.append(intervals[i])
            i += 1
        return ans