class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        repeated = ""
        count = 0

        #keep moving ahead till repeated is as long as b
        while len(repeated) < len(b):
            repeated += a
            count += 1

        if b in repeated:
            return count
        
        #take one more copy as b may cross the boundary
        repeated += a
        count += 1

        if b in repeated:
            return count

        return -1 #if b cannot be formed