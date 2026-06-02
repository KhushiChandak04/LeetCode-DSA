class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort() #sorts all intervals based on starting points
        ans = [intervals[0]]
        for i in range(1,n):
            last = ans[-1]
            if intervals[i][0] <= last[1]: #overlap where current starts before last ends
                last[1] = max(last[1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans