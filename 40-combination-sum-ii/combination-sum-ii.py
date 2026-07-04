class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort() #follow the same backtrack template here
        answer = []
        current = [] #stores current choice

        def backtrack(start, remaining):
            if remaining == 0: #when we find a valid combo
                answer.append(current[:])
                return
            #trial of various combinations across candidates
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: #same element found
                    continue
                if candidates[i] <= remaining:
                    current.append(candidates[i]) #onli choose the value that fits

                    backtrack(i+1, remaining - candidates[i]) #move to next index that cannot be used
                    current.pop()
        backtrack(0, target)
        return answer