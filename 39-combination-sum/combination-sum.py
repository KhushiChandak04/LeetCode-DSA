class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        n = len(candidates)

        def dfs(start, target, current): #recursion function
            if target == 0: #found target combo
                ans.append(current[:])
                return
            if target < 0: #target exceeded
                return
#try every number from current position onwards
            for i in range (start, n):
                current.append(candidates[i])
                dfs(i, target - candidates[i], current)
                current.pop()
        dfs(0, target, [])
        return ans