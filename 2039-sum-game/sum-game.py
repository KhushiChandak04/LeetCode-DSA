class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        mid = n // 2

        leftSum = 0
        rightSum = 0
        leftQ = 0 #no of ? in left side
        rightQ = 0 #no of ? in right side

        #process the first half 
        for i in range(mid):
            if num[i] == '?':
                leftQ += 1
            else:
                leftSum += int(num[i])
        
        #process second half
        for i in range(mid, n):
            if num[i] == '?':
                rightQ += 1
            else:
                rightSum += int(num[i])

        #if no of rightQ and leftQ is same, bob can respond symmetrically
        if leftQ == rightQ:
            return leftSum != rightSum

        # The side with more '?' must have the smaller sum for Bob to have a chance
        if (leftQ > rightQ and leftSum >= rightSum) or (rightQ > leftQ and rightSum >= leftSum):
            return True

        Qdiff = abs(rightQ - leftQ)
        sumDiff = abs(rightSum - leftSum)

        #maximum difference created by ? unmatched characters
        maxDiff = 9 * Qdiff // 2 #divide by 2 because the compensation needs to be in pairs

        if (leftQ + rightQ) % 2 == 1:
            return True

        return sumDiff != maxDiff