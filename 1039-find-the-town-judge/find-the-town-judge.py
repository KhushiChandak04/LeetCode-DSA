class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        #town judge - outgoing trust = 0, incoming trust = n-1(excluding their own)

        outgoing = [0]*(n+1)
        incoming = [0]*(n+1)

        for a,b in trust: #given that a trusts b, count outgoing and incoming trust
            outgoing[a] += 1
            incoming[b] += 1
        
        #chk who satisfies the conditions
        for i in range(1,n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i

        return -1 #otherwise