class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort( key=lambda x: x[1]) #sort by end value
        count = 1 #initilise count val as least it can be is 1
        last_end = pairs[0][1] #initilse

        for start, end in pairs[1:]: #slice from 1st pair
            if start > last_end:
                count += 1
                last_end = end
        return count