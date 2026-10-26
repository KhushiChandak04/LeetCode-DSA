class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []

        #check every operation
        for op in operations:
            if op == 'C': #remove the last score
                scores.pop()
            elif op == 'D': #double the last score
                scores.append(scores[-1] * 2) #top stack = -1
            elif op == '+':
                scores.append(scores[-1] + scores[-2]) #add prev 2 scores
            else:
                scores.append(int(op)) #add number as a score
        
        #return sum of all scores
        ans = 0
        for score in scores:
            ans += score
        return ans