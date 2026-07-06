class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #sort intervals first, smaller first... but if same start, then larger end first
        intervals.sort(key = lambda x:( x[0], -x[1]))
        count = 0 #initilise
        max_end = 0 #largest ending pt seen so far

        for start, end in intervals:
            if end <= max_end: #covered interval
                continue
            #not covered case
            count += 1
            max_end = end
        return count